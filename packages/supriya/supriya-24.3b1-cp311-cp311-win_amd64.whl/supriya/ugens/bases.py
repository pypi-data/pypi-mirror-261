import abc
import copy
import inspect
from enum import Enum
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    NamedTuple,
    Optional,
    Protocol,
    Sequence,
    SupportsFloat,
    Tuple,
    Type,
    Union,
    cast,
)

try:
    from typing import TypeAlias
except ImportError:
    from typing_extensions import TypeAlias  # noqa

from ..enums import (
    BinaryOperator,
    CalculationRate,
    DoneAction,
    SignalRange,
    UnaryOperator,
)
from ..typing import CalculationRateLike, Default, Missing


class Check(Enum):
    NONE = 0
    SAME_AS_FIRST = 1
    SAME_OR_SLOWER = 2


class Param(NamedTuple):
    default: Optional[Union[Default, Missing, float]] = None
    check: Check = Check.NONE
    unexpanded: bool = False


def _add_init(
    cls,
    params: Dict[str, "Param"],
    is_multichannel: bool,
    channel_count: int,
    fixed_channel_count: bool,
) -> None:
    parent_class = inspect.getmro(cls)[1]
    args = ["self", "*", "calculation_rate: CalculationRateLike"]
    body = []
    if is_multichannel and not fixed_channel_count:
        args.append(f"channel_count={channel_count or 1}")
        body.append("self._channel_count = channel_count")
    if fixed_channel_count:
        body.append(f"self._channel_count = {channel_count}")
    body.extend(
        [
            f"return {parent_class.__name__}.__init__(",
            "    self,",
            "    calculation_rate=CalculationRate.from_expr(calculation_rate),",
        ]
    )
    for key, param in params.items():
        value_repr = _format_value(param.default)
        type_ = "UGenInitVectorParam" if param.unexpanded else "UGenInitScalarParam"
        prefix = f"{key}: {type_}"
        args.append(
            f"{prefix} = {value_repr}"
            if not isinstance(param.default, Missing)
            else prefix
        )
        body.append(f"    {key}={key},")
    args.append("**kwargs")
    body.append("    **kwargs,")
    body.append(")")
    _create_fn(
        cls=cls,
        name="__init__",
        args=args,
        body=body,
        globals_={**_get_fn_globals(), parent_class.__name__: parent_class},
        return_type=None,
    )


def _add_param_fn(cls, name: str, index: int, unexpanded: bool) -> None:
    _create_fn(
        cls=cls,
        name=name,
        args=["self"],
        body=(
            [f"return UGenArray(self._inputs[{index}:])"]
            if unexpanded
            else [f"return UGenArray(self._inputs[{index}:{index} + 1])"]
        ),
        decorator=property,
        globals_=_get_fn_globals(),
        override=True,
        return_type=UGenArray,
    )


def _add_rate_fn(
    cls,
    rate: Optional[CalculationRate],
    params: Dict[str, "Param"],
    is_multichannel: bool,
    channel_count: int,
    fixed_channel_count: bool,
) -> None:
    args = ["cls"]
    if params:
        args.append("*")
    for key, param in params.items():
        value_repr = _format_value(param.default)
        prefix = f"{key}: UGenRateVectorParam"
        args.append(
            f"{prefix} = {value_repr}"
            if not isinstance(param.default, Missing)
            else prefix
        )
    body = ["return cls._new_expanded("]
    if rate is not None:
        body.append(f"    calculation_rate={rate!r},")
    if is_multichannel and not fixed_channel_count:
        args.append(f"channel_count: int = {channel_count or 1}")
        body.append("    channel_count=channel_count,")
    body.extend(f"    {name}={name}," for name in params)
    body.append(")")
    _create_fn(
        cls=cls,
        name=rate.token if rate is not None else "new",
        args=args,
        body=body,
        decorator=classmethod,
        globals_=_get_fn_globals(),
        return_type=cls,
    )


def _create_fn(
    *,
    cls,
    name: str,
    args: List[str],
    body: List[str],
    return_type,
    globals_: Optional[Dict[str, Type]] = None,
    decorator: Optional[Callable] = None,
    override: bool = False,
) -> None:
    if name in cls.__dict__ and not override:
        return
    globals_ = globals_ or {}
    locals_ = {"_return_type": return_type}
    args_ = ",\n        ".join(args)
    body_ = "\n".join(f"        {line}" for line in body)
    text = f"    def {name}(\n        {args_}\n    ) -> _return_type:\n{body_}"
    local_vars = ", ".join(locals_.keys())
    text = f"def __create_fn__({local_vars}):\n{text}\n    return {name}"
    namespace: Dict[str, Callable] = {}
    exec(text, globals_, namespace)
    value = namespace["__create_fn__"](**locals_)
    value.__qualname__ = f"{cls.__qualname__}.{value.__name__}"
    if decorator:
        value = decorator(value)
    setattr(cls, name, value)


def _format_value(value) -> str:
    if value == float("inf"):
        value_repr = 'float("inf")'
    elif value == float("-inf"):
        value_repr = 'float("-inf")'
    elif isinstance(value, Default):
        value_repr = "Default()"
    elif isinstance(value, Missing):
        value_repr = "Missing()"
    else:
        value_repr = repr(value)
    return value_repr


def _get_fn_globals():
    return {
        "CalculationRate": CalculationRate,
        "CalculationRateLike": CalculationRateLike,
        "Default": Default,
        "DoneAction": DoneAction,
        "Missing": Missing,
        "OutputProxy": OutputProxy,
        "Sequence": Sequence,
        "SupportsFloat": SupportsFloat,
        "UGenArray": UGenArray,
        "UGenInitScalarParam": UGenInitScalarParam,
        "UGenInitVectorParam": UGenInitVectorParam,
        "UGenOperable": UGenOperable,
        "UGenRateVectorParam": UGenRateVectorParam,
        "UGenSerializable": UGenSerializable,
        "Union": Union,
    }


def _process_class(
    cls: Type["UGen"],
    *,
    ar: bool = False,
    kr: bool = False,
    ir: bool = False,
    dr: bool = False,
    new: bool = False,
    has_done_flag: bool = False,
    is_input: bool = False,
    is_multichannel: bool = False,
    is_output: bool = False,
    is_pure: bool = False,
    is_width_first: bool = False,
    channel_count: int = 1,
    fixed_channel_count: bool = False,
    signal_range: Optional[int] = None,
) -> Type["UGen"]:
    params: Dict[str, Param] = {}
    unexpanded_input_names = []
    valid_calculation_rates = []
    for name, value in cls.__dict__.items():
        if not isinstance(value, Param):
            continue
        params[name] = value
        if value.unexpanded:
            unexpanded_input_names.append(name)
        _add_param_fn(cls, name, len(params) - 1, value.unexpanded)
    _add_init(cls, params, is_multichannel, channel_count, fixed_channel_count)
    for should_add, rate in [
        (ar, CalculationRate.AUDIO),
        (kr, CalculationRate.CONTROL),
        (ir, CalculationRate.SCALAR),
        (dr, CalculationRate.DEMAND),
        (new, None),
    ]:
        if not should_add:
            continue
        _add_rate_fn(
            cls, rate, params, is_multichannel, channel_count, fixed_channel_count
        )
        if rate is not None:
            valid_calculation_rates.append(rate)
    cls._has_done_flag = bool(has_done_flag)
    cls._is_input = bool(is_input)
    cls._is_output = bool(is_output)
    cls._is_pure = bool(is_pure)
    cls._is_width_first = bool(is_width_first)
    cls._ordered_input_names = {key: param.default for key, param in params.items()}
    cls._unexpanded_input_names = tuple(unexpanded_input_names)
    cls._valid_calculation_rates = tuple(valid_calculation_rates)
    if signal_range is not None:
        cls._signal_range = SignalRange.from_expr(signal_range)
    return cls


def param(
    default: Optional[Union[Default, Missing, float]] = Missing(),
    *,
    check: Check = Check.NONE,
    unexpanded: bool = False,
) -> Param:
    """
    Define a UGen parameter.

    Akin to dataclasses.field.
    """
    return Param(default, check, unexpanded)


def ugen(
    *,
    ar: bool = False,
    kr: bool = False,
    ir: bool = False,
    dr: bool = False,
    new: bool = False,
    has_done_flag: bool = False,
    is_input: bool = False,
    is_multichannel: bool = False,
    is_output: bool = False,
    is_pure: bool = False,
    is_width_first: bool = False,
    channel_count: int = 1,
    fixed_channel_count: bool = False,
    signal_range: Optional[int] = None,
) -> Callable[[Type["UGen"]], Type["UGen"]]:
    """
    Decorate a UGen class.

    Akin to dataclasses.dataclass.
    """

    def wrap(cls: Type[UGen]) -> Type[UGen]:
        return _process_class(
            cls,
            ar=ar,
            kr=kr,
            ir=ir,
            dr=dr,
            new=new,
            has_done_flag=has_done_flag,
            is_input=is_input,
            is_multichannel=is_multichannel,
            is_output=is_output,
            is_pure=is_pure,
            is_width_first=is_width_first,
            channel_count=channel_count,
            fixed_channel_count=fixed_channel_count,
            signal_range=signal_range,
        )

    if is_multichannel and fixed_channel_count:
        raise ValueError
    return wrap


class UGenOperable:

    ### SPECIAL METHODS ###

    def __abs__(self) -> "UGenOperable":
        """
        Gets absolute value of ugen graph.

        .. container:: example

            **Example 1:**

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.ar()
                >>> result = abs(ugen_graph)
                >>> result
                UnaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: f21696d155a2686700992f0e9a04a79c
                    ugens:
                    -   WhiteNoise.ar: null
                    -   UnaryOpUGen(ABSOLUTE_VALUE).ar:
                            source: WhiteNoise.ar[0]

        .. container:: example

            **Example 2:**

            ::

                >>> ugen_graph = supriya.ugens.SinOsc.ar(
                ...     frequency=(440, 442, 443),
                ... )
                >>> result = abs(ugen_graph)
                >>> result
                UGenArray({3})

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 1d45df2f3d33d1b0641d2c464498f6c4
                    ugens:
                    -   SinOsc.ar/0:
                            frequency: 440.0
                            phase: 0.0
                    -   UnaryOpUGen(ABSOLUTE_VALUE).ar/0:
                            source: SinOsc.ar/0[0]
                    -   SinOsc.ar/1:
                            frequency: 442.0
                            phase: 0.0
                    -   UnaryOpUGen(ABSOLUTE_VALUE).ar/1:
                            source: SinOsc.ar/1[0]
                    -   SinOsc.ar/2:
                            frequency: 443.0
                            phase: 0.0
                    -   UnaryOpUGen(ABSOLUTE_VALUE).ar/2:
                            source: SinOsc.ar/2[0]

        Returns ugen graph.
        """
        return UGenOperable._compute_unary_op(self, UnaryOperator.ABSOLUTE_VALUE)

    def __add__(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Adds `expr` to ugen graph.

        .. container:: example

            **Example 1:**

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.kr()
                >>> expr = supriya.ugens.SinOsc.ar()
                >>> result = ugen_graph + expr
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 6bf4339326d015532b7604cd7af9ad3b
                    ugens:
                    -   WhiteNoise.kr: null
                    -   SinOsc.ar:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(ADDITION).ar:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar[0]

        .. container:: example

            **Example 2:**

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.kr()
                >>> expr = supriya.ugens.SinOsc.ar(
                ...     frequency=[440, 442, 443],
                ... )
                >>> result = ugen_graph + expr
                >>> result
                UGenArray({3})

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: f4a3c1ed35cc5f6fe66b70a3bc520b10
                    ugens:
                    -   WhiteNoise.kr: null
                    -   SinOsc.ar/0:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(ADDITION).ar/0:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/0[0]
                    -   SinOsc.ar/1:
                            frequency: 442.0
                            phase: 0.0
                    -   BinaryOpUGen(ADDITION).ar/1:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/1[0]
                    -   SinOsc.ar/2:
                            frequency: 443.0
                            phase: 0.0
                    -   BinaryOpUGen(ADDITION).ar/2:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/2[0]

        .. container:: example

            **Example 3:**

            ::

                >>> ugen_graph = supriya.ugens.Dust.ar(
                ...     density=11.5,
                ... )
                >>> expr = 4
                >>> result = ugen_graph + expr
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: f79088cc154ef2b65c72a0f8de8336ce
                    ugens:
                    -   Dust.ar:
                            density: 11.5
                    -   BinaryOpUGen(ADDITION).ar:
                            left: Dust.ar[0]
                            right: 4.0

        Returns ugen graph.
        """
        return UGenOperable._compute_binary_op(self, expr, BinaryOperator.ADDITION)

    def __and__(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Computes the bitwise AND of the UGen graph and `expr`.

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.kr()
                >>> expr = supriya.ugens.SinOsc.ar()
                >>> result = ugen_graph & expr
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 9a5b4d1212b6b7fe299c21a8b1e401cc
                    ugens:
                    -   WhiteNoise.kr: null
                    -   SinOsc.ar:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(BITWISE_AND).ar:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar[0]
        """
        return UGenOperable._compute_binary_op(self, expr, BinaryOperator.BITWISE_AND)

    def __div__(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Divides ugen graph by `expr`.

        .. container:: example

            **Example 1:**

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.kr()
                >>> expr = supriya.ugens.SinOsc.ar()
                >>> result = ugen_graph / expr
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 6da024a346859242c441fe03326d2adc
                    ugens:
                    -   WhiteNoise.kr: null
                    -   SinOsc.ar:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(FLOAT_DIVISION).ar:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar[0]

        .. container:: example

            **Example 2:**

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.kr()
                >>> expr = supriya.ugens.SinOsc.ar(
                ...     frequency=[440, 442, 443],
                ... )
                >>> result = ugen_graph / expr
                >>> result
                UGenArray({3})

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: be20d589dfccb721f56da8b002d86763
                    ugens:
                    -   WhiteNoise.kr: null
                    -   SinOsc.ar/0:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(FLOAT_DIVISION).ar/0:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/0[0]
                    -   SinOsc.ar/1:
                            frequency: 442.0
                            phase: 0.0
                    -   BinaryOpUGen(FLOAT_DIVISION).ar/1:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/1[0]
                    -   SinOsc.ar/2:
                            frequency: 443.0
                            phase: 0.0
                    -   BinaryOpUGen(FLOAT_DIVISION).ar/2:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/2[0]

        .. container:: example

            **Example 3:**

            ::

                >>> ugen_graph = supriya.ugens.Dust.ar(
                ...     density=11.5,
                ... )
                >>> expr = 4
                >>> result = ugen_graph / expr
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 672765c596fcaa083186b2f2b996ba1d
                    ugens:
                    -   Dust.ar:
                            density: 11.5
                    -   BinaryOpUGen(FLOAT_DIVISION).ar:
                            left: Dust.ar[0]
                            right: 4.0

        Returns ugen graph.
        """
        return UGenOperable._compute_binary_op(
            self, expr, BinaryOperator.FLOAT_DIVISION
        )

    def __graph__(self):
        """
        Gets Graphviz representation of ugen graph.

        Returns GraphvizGraph instance.
        """
        synthdef = self._clone()
        result = synthdef.__graph__()
        return result

    def __ge__(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Tests if ugen graph if greater than or equal to `expr`.

        .. container:: example

            **Example 1:**

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.kr()
                >>> expr = supriya.ugens.SinOsc.ar()
                >>> result = ugen_graph >= expr
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 9db96233abf1f610d027ff285691482d
                    ugens:
                    -   WhiteNoise.kr: null
                    -   SinOsc.ar:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(GREATER_THAN_OR_EQUAL).ar:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar[0]

        .. container:: example

            **Example 2:**

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.kr()
                >>> expr = supriya.ugens.SinOsc.ar(
                ...     frequency=[440, 442, 443],
                ... )
                >>> result = ugen_graph >= expr
                >>> result
                UGenArray({3})

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 6d43342b3787aa11a46cea54412407e1
                    ugens:
                    -   WhiteNoise.kr: null
                    -   SinOsc.ar/0:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(GREATER_THAN_OR_EQUAL).ar/0:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/0[0]
                    -   SinOsc.ar/1:
                            frequency: 442.0
                            phase: 0.0
                    -   BinaryOpUGen(GREATER_THAN_OR_EQUAL).ar/1:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/1[0]
                    -   SinOsc.ar/2:
                            frequency: 443.0
                            phase: 0.0
                    -   BinaryOpUGen(GREATER_THAN_OR_EQUAL).ar/2:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/2[0]

        .. container:: example

            **Example 3:**

            ::

                >>> ugen_graph = supriya.ugens.Dust.ar(
                ...     density=11.5,
                ... )
                >>> expr = 4
                >>> result = ugen_graph >= expr
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: b06931195bab8e6f6ca2e3a857e71a95
                    ugens:
                    -   Dust.ar:
                            density: 11.5
                    -   BinaryOpUGen(GREATER_THAN_OR_EQUAL).ar:
                            left: Dust.ar[0]
                            right: 4.0

        Returns ugen graph.
        """
        return UGenOperable._compute_binary_op(
            self, expr, BinaryOperator.GREATER_THAN_OR_EQUAL
        )

    def __gt__(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Tests if ugen graph if greater than `expr`.

        .. container:: example

            **Example 1:**

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.kr()
                >>> expr = supriya.ugens.SinOsc.ar()
                >>> result = ugen_graph > expr
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 01bebf935112af62ffdd282a99581904
                    ugens:
                    -   WhiteNoise.kr: null
                    -   SinOsc.ar:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(GREATER_THAN).ar:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar[0]

        .. container:: example

            **Example 2:**

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.kr()
                >>> expr = supriya.ugens.SinOsc.ar(
                ...     frequency=[440, 442, 443],
                ... )
                >>> result = ugen_graph > expr
                >>> result
                UGenArray({3})

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 55642179864ad927e9d5cf6358367677
                    ugens:
                    -   WhiteNoise.kr: null
                    -   SinOsc.ar/0:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(GREATER_THAN).ar/0:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/0[0]
                    -   SinOsc.ar/1:
                            frequency: 442.0
                            phase: 0.0
                    -   BinaryOpUGen(GREATER_THAN).ar/1:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/1[0]
                    -   SinOsc.ar/2:
                            frequency: 443.0
                            phase: 0.0
                    -   BinaryOpUGen(GREATER_THAN).ar/2:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/2[0]

        .. container:: example

            **Example 3:**

            ::

                >>> ugen_graph = supriya.ugens.Dust.ar(
                ...     density=11.5,
                ... )
                >>> expr = 4
                >>> result = ugen_graph > expr
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 5177e03443ad31ee2664aae2201fb979
                    ugens:
                    -   Dust.ar:
                            density: 11.5
                    -   BinaryOpUGen(GREATER_THAN).ar:
                            left: Dust.ar[0]
                            right: 4.0

        Returns ugen graph.
        """
        return UGenOperable._compute_binary_op(self, expr, BinaryOperator.GREATER_THAN)

    def __le__(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Tests if ugen graph if less than or equal to `expr`.

        .. container:: example

            **Example 1:**

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.kr()
                >>> expr = supriya.ugens.SinOsc.ar()
                >>> result = ugen_graph <= expr
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: fefc06cbbc3babb35046306c6d41e3c5
                    ugens:
                    -   WhiteNoise.kr: null
                    -   SinOsc.ar:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(LESS_THAN_OR_EQUAL).ar:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar[0]

        .. container:: example

            **Example 2:**

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.kr()
                >>> expr = supriya.ugens.SinOsc.ar(
                ...     frequency=[440, 442, 443],
                ... )
                >>> result = ugen_graph <= expr
                >>> result
                UGenArray({3})

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 53f29d793fd676fbca1d541e938b66ca
                    ugens:
                    -   WhiteNoise.kr: null
                    -   SinOsc.ar/0:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(LESS_THAN_OR_EQUAL).ar/0:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/0[0]
                    -   SinOsc.ar/1:
                            frequency: 442.0
                            phase: 0.0
                    -   BinaryOpUGen(LESS_THAN_OR_EQUAL).ar/1:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/1[0]
                    -   SinOsc.ar/2:
                            frequency: 443.0
                            phase: 0.0
                    -   BinaryOpUGen(LESS_THAN_OR_EQUAL).ar/2:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/2[0]

        .. container:: example

            **Example 3:**

            ::

                >>> ugen_graph = supriya.ugens.Dust.ar(
                ...     density=11.5,
                ... )
                >>> expr = 4
                >>> result = ugen_graph <= expr
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 3cf0414af96d130edf2e1b839f73036c
                    ugens:
                    -   Dust.ar:
                            density: 11.5
                    -   BinaryOpUGen(LESS_THAN_OR_EQUAL).ar:
                            left: Dust.ar[0]
                            right: 4.0

        Returns ugen graph.
        """
        return UGenOperable._compute_binary_op(
            self, expr, BinaryOperator.LESS_THAN_OR_EQUAL
        )

    def __len__(self) -> int:
        raise NotImplementedError

    def __lt__(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Tests if ugen graph if less than `expr`.

        .. container:: example

            **Example 1:**

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.kr()
                >>> expr = supriya.ugens.SinOsc.ar()
                >>> result = ugen_graph < expr
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 844f34c0ffb28ecc24bd5cf0bae20b43
                    ugens:
                    -   WhiteNoise.kr: null
                    -   SinOsc.ar:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(LESS_THAN).ar:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar[0]

        .. container:: example

            **Example 2:**

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.kr()
                >>> expr = supriya.ugens.SinOsc.ar(
                ...     frequency=[440, 442, 443],
                ... )
                >>> result = ugen_graph < expr
                >>> result
                UGenArray({3})

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 14c1494fe4e153e690a8ef0a42e5834f
                    ugens:
                    -   WhiteNoise.kr: null
                    -   SinOsc.ar/0:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(LESS_THAN).ar/0:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/0[0]
                    -   SinOsc.ar/1:
                            frequency: 442.0
                            phase: 0.0
                    -   BinaryOpUGen(LESS_THAN).ar/1:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/1[0]
                    -   SinOsc.ar/2:
                            frequency: 443.0
                            phase: 0.0
                    -   BinaryOpUGen(LESS_THAN).ar/2:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/2[0]

        .. container:: example

            **Example 3:**

            ::

                >>> ugen_graph = supriya.ugens.Dust.ar(
                ...     density=11.5,
                ... )
                >>> expr = 4
                >>> result = ugen_graph < expr
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: e87d41791847aa80d8a3e56318e506e4
                    ugens:
                    -   Dust.ar:
                            density: 11.5
                    -   BinaryOpUGen(LESS_THAN).ar:
                            left: Dust.ar[0]
                            right: 4.0

        Returns ugen graph.
        """
        return UGenOperable._compute_binary_op(self, expr, BinaryOperator.LESS_THAN)

    def __mod__(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Gets modulo of ugen graph and `expr`.

        .. container:: example

            **Example 1:**

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.kr()
                >>> expr = supriya.ugens.SinOsc.ar()
                >>> result = ugen_graph % expr
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: e4a06e157474f8d1ae213916f3cf585a
                    ugens:
                    -   WhiteNoise.kr: null
                    -   SinOsc.ar:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(MODULO).ar:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar[0]

        .. container:: example

            **Example 2:**

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.kr()
                >>> expr = supriya.ugens.SinOsc.ar(
                ...     frequency=[440, 442, 443],
                ... )
                >>> result = ugen_graph % expr
                >>> result
                UGenArray({3})

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 90badce1cf8fc1752b5eb99b29122a14
                    ugens:
                    -   WhiteNoise.kr: null
                    -   SinOsc.ar/0:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(MODULO).ar/0:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/0[0]
                    -   SinOsc.ar/1:
                            frequency: 442.0
                            phase: 0.0
                    -   BinaryOpUGen(MODULO).ar/1:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/1[0]
                    -   SinOsc.ar/2:
                            frequency: 443.0
                            phase: 0.0
                    -   BinaryOpUGen(MODULO).ar/2:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/2[0]

        .. container:: example

            **Example 3:**

            ::

                >>> ugen_graph = supriya.ugens.Dust.ar(
                ...     density=11.5,
                ... )
                >>> expr = 4
                >>> result = ugen_graph % expr
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: bfa60877061daf112516cc3ec8c7ff69
                    ugens:
                    -   Dust.ar:
                            density: 11.5
                    -   BinaryOpUGen(MODULO).ar:
                            left: Dust.ar[0]
                            right: 4.0

        Returns ugen graph.
        """
        return UGenOperable._compute_binary_op(self, expr, BinaryOperator.MODULO)

    def __mul__(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Multiplies ugen graph by `expr`.

        .. container:: example

            **Example 1:**

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.kr()
                >>> expr = supriya.ugens.SinOsc.ar()
                >>> result = ugen_graph * expr
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: ea2b5e5cec4e2d5a1bef0a8dda522bd3
                    ugens:
                    -   WhiteNoise.kr: null
                    -   SinOsc.ar:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(MULTIPLICATION).ar:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar[0]

        .. container:: example

            **Example 2:**

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.kr()
                >>> expr = supriya.ugens.SinOsc.ar(
                ...     frequency=[440, 442, 443],
                ... )
                >>> result = ugen_graph * expr
                >>> result
                UGenArray({3})

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 9d353c198344b6be3635244197bc2a4b
                    ugens:
                    -   WhiteNoise.kr: null
                    -   SinOsc.ar/0:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(MULTIPLICATION).ar/0:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/0[0]
                    -   SinOsc.ar/1:
                            frequency: 442.0
                            phase: 0.0
                    -   BinaryOpUGen(MULTIPLICATION).ar/1:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/1[0]
                    -   SinOsc.ar/2:
                            frequency: 443.0
                            phase: 0.0
                    -   BinaryOpUGen(MULTIPLICATION).ar/2:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/2[0]

        .. container:: example

            **Example 3:**

            ::

                >>> ugen_graph = supriya.ugens.Dust.ar(
                ...     density=11.5,
                ... )
                >>> expr = 4
                >>> result = ugen_graph * expr
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 1735acd4add428d8ab317d00236b0fe7
                    ugens:
                    -   Dust.ar:
                            density: 11.5
                    -   BinaryOpUGen(MULTIPLICATION).ar:
                            left: Dust.ar[0]
                            right: 4.0

        Returns ugen graph.
        """
        return UGenOperable._compute_binary_op(
            self, expr, BinaryOperator.MULTIPLICATION
        )

    def __neg__(self) -> "UGenOperable":
        """
        Negates ugen graph.

        .. container:: example

            **Example 1:**

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.ar()
                >>> result = -ugen_graph
                >>> result
                UnaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: a987a13f0593e4e4e070acffb11d5c3e
                    ugens:
                    -   WhiteNoise.ar: null
                    -   UnaryOpUGen(NEGATIVE).ar:
                            source: WhiteNoise.ar[0]

        .. container:: example

            **Example 2:**

            ::

                >>> ugen_graph = supriya.ugens.SinOsc.ar(
                ...     frequency=(440, 442, 443),
                ... )
                >>> result = -ugen_graph
                >>> result
                UGenArray({3})

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: e5dfc1d4ecb11ed8170aaf11469a6443
                    ugens:
                    -   SinOsc.ar/0:
                            frequency: 440.0
                            phase: 0.0
                    -   UnaryOpUGen(NEGATIVE).ar/0:
                            source: SinOsc.ar/0[0]
                    -   SinOsc.ar/1:
                            frequency: 442.0
                            phase: 0.0
                    -   UnaryOpUGen(NEGATIVE).ar/1:
                            source: SinOsc.ar/1[0]
                    -   SinOsc.ar/2:
                            frequency: 443.0
                            phase: 0.0
                    -   UnaryOpUGen(NEGATIVE).ar/2:
                            source: SinOsc.ar/2[0]

        Returns ugen graph.
        """
        return UGenOperable._compute_unary_op(self, UnaryOperator.NEGATIVE)

    def __or__(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Computes the bitwise OR of the UGen graph and `expr`.

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.kr()
                >>> expr = supriya.ugens.SinOsc.ar()
                >>> result = ugen_graph | expr
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 333e2e7362f86138866f3f2a160f77dd
                    ugens:
                    -   WhiteNoise.kr: null
                    -   SinOsc.ar:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(BITWISE_OR).ar:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar[0]
        """
        return UGenOperable._compute_binary_op(self, expr, BinaryOperator.BITWISE_OR)

    def __pow__(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Raises ugen graph to the power of `expr`.

        .. container:: example

            **Example 1:**

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.kr()
                >>> expr = supriya.ugens.SinOsc.ar()
                >>> result = ugen_graph ** expr
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 3498b370c0575fb2c2ed45143ba2da4f
                    ugens:
                    -   WhiteNoise.kr: null
                    -   SinOsc.ar:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(POWER).ar:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar[0]

        .. container:: example

            **Example 2:**

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.kr()
                >>> expr = supriya.ugens.SinOsc.ar(
                ...     frequency=[440, 442, 443],
                ... )
                >>> result = ugen_graph ** expr
                >>> result
                UGenArray({3})

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 04e78034682f9ffd6628fbfd09a28c13
                    ugens:
                    -   WhiteNoise.kr: null
                    -   SinOsc.ar/0:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(POWER).ar/0:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/0[0]
                    -   SinOsc.ar/1:
                            frequency: 442.0
                            phase: 0.0
                    -   BinaryOpUGen(POWER).ar/1:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/1[0]
                    -   SinOsc.ar/2:
                            frequency: 443.0
                            phase: 0.0
                    -   BinaryOpUGen(POWER).ar/2:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/2[0]

        .. container:: example

            **Example 3:**

            ::

                >>> ugen_graph = supriya.ugens.Dust.ar(
                ...     density=11.5,
                ... )
                >>> expr = 4
                >>> result = ugen_graph ** expr
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 50b8e3b154bc85c98d76ced493a32731
                    ugens:
                    -   Dust.ar:
                            density: 11.5
                    -   BinaryOpUGen(POWER).ar:
                            left: Dust.ar[0]
                            right: 4.0

        Returns ugen graph.
        """
        return UGenOperable._compute_binary_op(self, expr, BinaryOperator.POWER)

    def __rpow__(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Raises `expr` to the power of ugen graph.

        .. container:: example

            **Example 1:**

            ::

                >>> expr = 1.5
                >>> ugen_graph = supriya.ugens.SinOsc.ar()
                >>> result = expr ** ugen_graph
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: c450618c9e0fe5213629275da4e5e354
                    ugens:
                    -   SinOsc.ar:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(POWER).ar:
                            left: 1.5
                            right: SinOsc.ar[0]

        .. container:: example

            **Example 2:**

            ::

                >>> expr = [220, 330]
                >>> ugen_graph = supriya.ugens.SinOsc.ar(
                ...     frequency=[440, 442, 443],
                ... )
                >>> result = expr ** ugen_graph
                >>> result
                UGenArray({3})

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: a614dc68313ee7ca2677e63fd499de0d
                    ugens:
                    -   SinOsc.ar/0:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(POWER).ar/0:
                            left: 220.0
                            right: SinOsc.ar/0[0]
                    -   SinOsc.ar/1:
                            frequency: 442.0
                            phase: 0.0
                    -   BinaryOpUGen(POWER).ar/1:
                            left: 330.0
                            right: SinOsc.ar/1[0]
                    -   SinOsc.ar/2:
                            frequency: 443.0
                            phase: 0.0
                    -   BinaryOpUGen(POWER).ar/2:
                            left: 220.0
                            right: SinOsc.ar/2[0]

        Returns ugen graph.
        """
        return UGenOperable._compute_binary_op(expr, self, BinaryOperator.POWER)

    def __radd__(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Adds ugen graph to `expr`.

        .. container:: example

            **Example 1:**

            ::

                >>> expr = 1.5
                >>> ugen_graph = supriya.ugens.SinOsc.ar()
                >>> result = expr + ugen_graph
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: bb0592fad58b0bfa1a403c7ff6a400f3
                    ugens:
                    -   SinOsc.ar:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(ADDITION).ar:
                            left: 1.5
                            right: SinOsc.ar[0]

        .. container:: example

            **Example 2:**

            ::

                >>> expr = [220, 330]
                >>> ugen_graph = supriya.ugens.SinOsc.ar(
                ...     frequency=[440, 442, 443],
                ... )
                >>> result = expr + ugen_graph
                >>> result
                UGenArray({3})

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 0ad0a3d4b7ddf8bb56807813efc62202
                    ugens:
                    -   SinOsc.ar/0:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(ADDITION).ar/0:
                            left: 220.0
                            right: SinOsc.ar/0[0]
                    -   SinOsc.ar/1:
                            frequency: 442.0
                            phase: 0.0
                    -   BinaryOpUGen(ADDITION).ar/1:
                            left: 330.0
                            right: SinOsc.ar/1[0]
                    -   SinOsc.ar/2:
                            frequency: 443.0
                            phase: 0.0
                    -   BinaryOpUGen(ADDITION).ar/2:
                            left: 220.0
                            right: SinOsc.ar/2[0]

        Returns ugen graph.
        """
        return UGenOperable._compute_binary_op(expr, self, BinaryOperator.ADDITION)

    def __rdiv__(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Divides `expr` by ugen graph.

        .. container:: example

            **Example 1:**

            ::

                >>> expr = 1.5
                >>> ugen_graph = supriya.ugens.SinOsc.ar()
                >>> result = expr / ugen_graph
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: d79490206a430281b186b188d617f679
                    ugens:
                    -   SinOsc.ar:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(FLOAT_DIVISION).ar:
                            left: 1.5
                            right: SinOsc.ar[0]

        .. container:: example

            **Example 2:**

            ::

                >>> expr = [220, 330]
                >>> ugen_graph = supriya.ugens.SinOsc.ar(
                ...     frequency=[440, 442, 443],
                ... )
                >>> result = expr / ugen_graph
                >>> result
                UGenArray({3})

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: d71b3081490f800d5136c87f5fef46d1
                    ugens:
                    -   SinOsc.ar/0:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(FLOAT_DIVISION).ar/0:
                            left: 220.0
                            right: SinOsc.ar/0[0]
                    -   SinOsc.ar/1:
                            frequency: 442.0
                            phase: 0.0
                    -   BinaryOpUGen(FLOAT_DIVISION).ar/1:
                            left: 330.0
                            right: SinOsc.ar/1[0]
                    -   SinOsc.ar/2:
                            frequency: 443.0
                            phase: 0.0
                    -   BinaryOpUGen(FLOAT_DIVISION).ar/2:
                            left: 220.0
                            right: SinOsc.ar/2[0]

        Returns ugen graph.
        """
        return UGenOperable._compute_binary_op(
            expr, self, BinaryOperator.FLOAT_DIVISION
        )

    def __rmod__(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Gets modulo of `expr` and ugen graph.

        .. container:: example

            **Example 1:**

            ::

                >>> expr = 1.5
                >>> ugen_graph = supriya.ugens.SinOsc.ar()
                >>> result = expr % ugen_graph
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: d79490206a430281b186b188d617f679
                    ugens:
                    -   SinOsc.ar:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(FLOAT_DIVISION).ar:
                            left: 1.5
                            right: SinOsc.ar[0]

        .. container:: example

            **Example 2:**

            ::

                >>> expr = [220, 330]
                >>> ugen_graph = supriya.ugens.SinOsc.ar(
                ...     frequency=[440, 442, 443],
                ... )
                >>> result = expr % ugen_graph
                >>> result
                UGenArray({3})

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: d71b3081490f800d5136c87f5fef46d1
                    ugens:
                    -   SinOsc.ar/0:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(FLOAT_DIVISION).ar/0:
                            left: 220.0
                            right: SinOsc.ar/0[0]
                    -   SinOsc.ar/1:
                            frequency: 442.0
                            phase: 0.0
                    -   BinaryOpUGen(FLOAT_DIVISION).ar/1:
                            left: 330.0
                            right: SinOsc.ar/1[0]
                    -   SinOsc.ar/2:
                            frequency: 443.0
                            phase: 0.0
                    -   BinaryOpUGen(FLOAT_DIVISION).ar/2:
                            left: 220.0
                            right: SinOsc.ar/2[0]

        Returns ugen graph.
        """
        return UGenOperable._compute_binary_op(
            expr, self, BinaryOperator.FLOAT_DIVISION
        )

    def __rmul__(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Multiplies `expr` by ugen graph.

        .. container:: example

            **Example 1:**

            ::

                >>> expr = 1.5
                >>> ugen_graph = supriya.ugens.SinOsc.ar()
                >>> result = expr * ugen_graph
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: f60bbe0480298a7ae8b54de5a4c0260f
                    ugens:
                    -   SinOsc.ar:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(MULTIPLICATION).ar:
                            left: 1.5
                            right: SinOsc.ar[0]

        .. container:: example

            **Example 2:**

            ::

                >>> expr = [220, 330]
                >>> ugen_graph = supriya.ugens.SinOsc.ar(
                ...     frequency=[440, 442, 443],
                ... )
                >>> result = expr * ugen_graph
                >>> result
                UGenArray({3})

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 0295153106bff55a2bf6db3b7184d301
                    ugens:
                    -   SinOsc.ar/0:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(MULTIPLICATION).ar/0:
                            left: 220.0
                            right: SinOsc.ar/0[0]
                    -   SinOsc.ar/1:
                            frequency: 442.0
                            phase: 0.0
                    -   BinaryOpUGen(MULTIPLICATION).ar/1:
                            left: 330.0
                            right: SinOsc.ar/1[0]
                    -   SinOsc.ar/2:
                            frequency: 443.0
                            phase: 0.0
                    -   BinaryOpUGen(MULTIPLICATION).ar/2:
                            left: 220.0
                            right: SinOsc.ar/2[0]

        Returns ugen graph.
        """
        return UGenOperable._compute_binary_op(
            expr, self, BinaryOperator.MULTIPLICATION
        )

    def __rsub__(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Subtracts ugen graph from `expr`.

        .. container:: example

            **Example 1:**

            ::

                >>> expr = 1.5
                >>> ugen_graph = supriya.ugens.SinOsc.ar()
                >>> result = expr - ugen_graph
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 74e331121aa41f4d49a6d38a38ca4a9a
                    ugens:
                    -   SinOsc.ar:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(SUBTRACTION).ar:
                            left: 1.5
                            right: SinOsc.ar[0]

        .. container:: example

            **Example 2:**

            ::

                >>> expr = [220, 330]
                >>> ugen_graph = supriya.ugens.SinOsc.ar(
                ...     frequency=[440, 442, 443],
                ... )
                >>> result = expr - ugen_graph
                >>> result
                UGenArray({3})

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 1ca2e8f3f541b9365413a0dbf9028e95
                    ugens:
                    -   SinOsc.ar/0:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(SUBTRACTION).ar/0:
                            left: 220.0
                            right: SinOsc.ar/0[0]
                    -   SinOsc.ar/1:
                            frequency: 442.0
                            phase: 0.0
                    -   BinaryOpUGen(SUBTRACTION).ar/1:
                            left: 330.0
                            right: SinOsc.ar/1[0]
                    -   SinOsc.ar/2:
                            frequency: 443.0
                            phase: 0.0
                    -   BinaryOpUGen(SUBTRACTION).ar/2:
                            left: 220.0
                            right: SinOsc.ar/2[0]

        Returns ugen graph.
        """
        return UGenOperable._compute_binary_op(expr, self, BinaryOperator.SUBTRACTION)

    def __str__(self):
        """
        Gets string representation of ugen graph.

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.SinOsc.ar()
                >>> print(str(ugen_graph))
                synthdef:
                    name: c9b0ed62d4e0666b74166ff5ec09abe4
                    ugens:
                    -   SinOsc.ar:
                            frequency: 440.0
                            phase: 0.0

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.SinOsc.ar(frequency=[1, 2, 3])
                >>> print(str(ugen_graph))
                synthdef:
                    name: 4015dac116b25c54b4a6f02bcb5859cb
                    ugens:
                    -   SinOsc.ar/0:
                            frequency: 1.0
                            phase: 0.0
                    -   SinOsc.ar/1:
                            frequency: 2.0
                            phase: 0.0
                    -   SinOsc.ar/2:
                            frequency: 3.0
                            phase: 0.0

        Returns string.
        """
        synthdef = self._clone()
        result = str(synthdef)
        return result

    def __sub__(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Subtracts `expr` from ugen graph.

        .. container:: example

            **Example 1:**

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.kr()
                >>> expr = supriya.ugens.SinOsc.ar()
                >>> result = ugen_graph - expr
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: cd62fff8ff3ad7758d0f7ad82f39c7ce
                    ugens:
                    -   WhiteNoise.kr: null
                    -   SinOsc.ar:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(SUBTRACTION).ar:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar[0]

        .. container:: example

            **Example 2:**

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.kr()
                >>> expr = supriya.ugens.SinOsc.ar(
                ...     frequency=[440, 442, 443],
                ... )
                >>> result = ugen_graph - expr
                >>> result
                UGenArray({3})

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 9a8355f84507908cadf3cc63187ddab4
                    ugens:
                    -   WhiteNoise.kr: null
                    -   SinOsc.ar/0:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(SUBTRACTION).ar/0:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/0[0]
                    -   SinOsc.ar/1:
                            frequency: 442.0
                            phase: 0.0
                    -   BinaryOpUGen(SUBTRACTION).ar/1:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/1[0]
                    -   SinOsc.ar/2:
                            frequency: 443.0
                            phase: 0.0
                    -   BinaryOpUGen(SUBTRACTION).ar/2:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar/2[0]

        .. container:: example

            **Example 3:**

            ::

                >>> ugen_graph = supriya.ugens.Dust.ar(
                ...     density=11.5,
                ... )
                >>> expr = 4
                >>> result = ugen_graph - expr
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 48ca704043ed00a2b6a55fd4b6b72cf1
                    ugens:
                    -   Dust.ar:
                            density: 11.5
                    -   BinaryOpUGen(SUBTRACTION).ar:
                            left: Dust.ar[0]
                            right: 4.0

        Returns ugen graph.
        """
        return UGenOperable._compute_binary_op(self, expr, BinaryOperator.SUBTRACTION)

    def __xor__(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Computes the bitwise XOR of the UGen graph and `expr`.

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.kr()
                >>> expr = supriya.ugens.SinOsc.ar()
                >>> result = ugen_graph ^ expr
                >>> result
                BinaryOpUGen.ar()[0]

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 355f2c7fa510863b921bb8c28bc4a682
                    ugens:
                    -   WhiteNoise.kr: null
                    -   SinOsc.ar:
                            frequency: 440.0
                            phase: 0.0
                    -   BinaryOpUGen(BITWISE_XOR).ar:
                            left: WhiteNoise.kr[0]
                            right: SinOsc.ar[0]
        """
        return UGenOperable._compute_binary_op(self, expr, BinaryOperator.BITWISE_XOR)

    __truediv__ = __div__
    __rtruediv__ = __rdiv__

    ### PRIVATE METHODS ###

    def _clone(self):
        def recurse(uuid, ugen, all_ugens):
            if hasattr(ugen, "inputs"):
                for input_ in ugen.inputs:
                    if not isinstance(input_, OutputProxy):
                        continue
                    input_ = input_.source
                    input_._uuid = uuid
                    recurse(uuid, input_, all_ugens)
            ugen._uuid = uuid
            if ugen not in all_ugens:
                all_ugens.append(ugen)

        from ..synthdefs import SynthDefBuilder

        builder = SynthDefBuilder()
        ugens = copy.deepcopy(self)
        if not isinstance(ugens, UGenArray):
            ugens = [ugens]
        all_ugens = []
        for u in ugens:
            if isinstance(u, OutputProxy):
                u = u.source
            recurse(builder._uuid, u, all_ugens)
        for u in all_ugens:
            if isinstance(u, UGen):
                builder._add_ugens(u)
            else:
                builder._add_parameter(u)
        return builder.build(optimize=False)

    @staticmethod
    def _compute_binary_op(left, right, operator) -> "UGenOperable":
        result: List[Union[OutputProxy, float]] = []
        if not isinstance(left, Sequence):
            left = (left,)
        if not isinstance(right, Sequence):
            right = (right,)
        dictionary = {"left": left, "right": right}
        operator = BinaryOperator.from_expr(operator)
        special_index = operator.value
        for expanded_dict in UGen._expand_dictionary(dictionary):
            left = expanded_dict["left"]
            right = expanded_dict["right"]
            calculation_rate = UGenOperable._compute_binary_rate(left, right)
            ugen = BinaryOpUGen._new_single(
                calculation_rate=calculation_rate,
                left=left,
                right=right,
                special_index=special_index,
            )
            result.extend(ugen if not isinstance(ugen, (float, int)) else [ugen])
        if len(result) == 1:
            # TODO: remove cast(...)
            return cast(UGenOperable, result[0])
        return UGenArray(result)

    @staticmethod
    def _compute_binary_rate(ugen_a, ugen_b) -> CalculationRate:
        a_rate = CalculationRate.from_expr(ugen_a)
        b_rate = CalculationRate.from_expr(ugen_b)
        if a_rate == CalculationRate.DEMAND or a_rate == CalculationRate.DEMAND:
            return CalculationRate.DEMAND
        elif a_rate == CalculationRate.AUDIO or b_rate == CalculationRate.AUDIO:
            return CalculationRate.AUDIO
        elif a_rate == CalculationRate.CONTROL or b_rate == CalculationRate.CONTROL:
            return CalculationRate.CONTROL
        return CalculationRate.SCALAR

    def _compute_ugen_map(self, map_ugen, **kwargs):
        sources = []
        ugens = []
        if len(self) == 1:
            sources = [self]
        else:
            sources = self
        for source in sources:
            method = UGen._get_method_for_rate(map_ugen, source)
            ugen = method(source=source, **kwargs)
            ugens.extend(ugen)
        if 1 < len(ugens):
            return UGenArray(ugens)
        elif len(ugens) == 1:
            return ugens[0].source
        return []

    @staticmethod
    def _compute_unary_op(source, operator) -> "UGenOperable":
        result: List[Union[OutputProxy, float]] = []
        if not isinstance(source, Sequence):
            source = (source,)
        operator = UnaryOperator.from_expr(operator)
        special_index = operator.value
        for single_source in source:
            calculation_rate = CalculationRate.from_expr(single_source)
            ugen = UnaryOpUGen._new_single(
                calculation_rate=calculation_rate,
                source=single_source,
                special_index=special_index,
            )
            result.extend(ugen if not isinstance(ugen, (float, int)) else [ugen])
        if len(result) == 1:
            # TODO: remove cast(...)
            return cast(UGenOperable, result[0])
        return UGenArray(result)

    def _get_output_proxy(self, i):
        if isinstance(i, int):
            if not (0 <= i < len(self)):
                raise IndexError(i, len(self))
            return OutputProxy(source=self, output_index=i)
        indices = i.indices(len(self))
        if not (0 <= indices[0] <= indices[1] <= len(self)):
            raise IndexError(i, indices, len(self))
        output_proxies = (
            OutputProxy(source=self, output_index=i) for i in range(*indices)
        )
        return UGenArray(output_proxies)

    ### PUBLIC METHODS ###

    def absolute_difference(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Calculates absolute difference between ugen graph and `expr`.

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.SinOsc.ar()
                >>> expr = supriya.ugens.WhiteNoise.kr()
                >>> result = ugen_graph.absolute_difference(expr)

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: a6b274b5f30e1dfa86ac1d00ef1c169b
                    ugens:
                    -   SinOsc.ar:
                            frequency: 440.0
                            phase: 0.0
                    -   WhiteNoise.kr: null
                    -   BinaryOpUGen(ABSOLUTE_DIFFERENCE).ar:
                            left: SinOsc.ar[0]
                            right: WhiteNoise.kr[0]

        Returns ugen graph.
        """
        return self._compute_binary_op(self, expr, BinaryOperator.ABSOLUTE_DIFFERENCE)

    def amplitude_to_db(self) -> "UGenOperable":
        """
        Converts ugen graph from amplitude to decibels.

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.ar()
                >>> result = ugen_graph.amplitude_to_db()

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 73daa5fd8db0d28c03c3872c845fd3ed
                    ugens:
                    -   WhiteNoise.ar: null
                    -   UnaryOpUGen(AMPLITUDE_TO_DB).ar:
                            source: WhiteNoise.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.AMPLITUDE_TO_DB)

    def as_int(self) -> "UGenOperable":
        return self._compute_unary_op(self, UnaryOperator.AS_INT)

    def as_maximum(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Calculates maximum between ugen graph and `expr`.

        ::

            >>> left = supriya.ugens.SinOsc.ar()
            >>> right = supriya.ugens.WhiteNoise.kr()
            >>> operation = left.as_maximum(right)
            >>> print(operation)
            synthdef:
                name: dcdca07fb0439c8b4321f42803d18c32
                ugens:
                -   SinOsc.ar:
                        frequency: 440.0
                        phase: 0.0
                -   WhiteNoise.kr: null
                -   BinaryOpUGen(MAXIMUM).ar:
                        left: SinOsc.ar[0]
                        right: WhiteNoise.kr[0]

        Returns ugen graph.
        """
        return self._compute_binary_op(self, expr, BinaryOperator.MAXIMUM)

    def as_minimum(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Calculates minimum between ugen graph and `expr`.

        ::

            >>> left = supriya.ugens.SinOsc.ar()
            >>> right = supriya.ugens.WhiteNoise.kr()
            >>> operation = left.as_minimum(right)
            >>> print(operation)
            synthdef:
                name: f80c0a7b300911e9eff0e8760f5fab18
                ugens:
                -   SinOsc.ar:
                        frequency: 440.0
                        phase: 0.0
                -   WhiteNoise.kr: null
                -   BinaryOpUGen(MINIMUM).ar:
                        left: SinOsc.ar[0]
                        right: WhiteNoise.kr[0]

        Returns ugen graph.
        """
        return self._compute_binary_op(self, expr, BinaryOperator.MINIMUM)

    def ceiling(self) -> "UGenOperable":
        """
        Calculates the ceiling of ugen graph.

        ::

            >>> source = supriya.ugens.DC.ar(source=0.5)
            >>> operation = source.ceiling()
            >>> print(operation)
            synthdef:
                name: c7b1855219f3364f731bdd2e4599b1d1
                ugens:
                -   DC.ar:
                        source: 0.5
                -   UnaryOpUGen(CEILING).ar:
                        source: DC.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.CEILING)

    def clip(
        self,
        minimum: Union[SupportsFloat, "UGenOperable"],
        maximum: Union[SupportsFloat, "UGenOperable"],
    ) -> "UGenOperable":
        """
        Clips ugen graph.

        .. container:: example

            **Example 1:**

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.ar()
                >>> result = ugen_graph.clip(-0.25, 0.25)

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: e710843b0e0fbc5e6185afc6cdf90149
                    ugens:
                    -   WhiteNoise.ar: null
                    -   Clip.ar:
                            source: WhiteNoise.ar[0]
                            minimum: -0.25
                            maximum: 0.25

        .. container:: example

            **Example 2:**

            ::

                >>> ugen_graph = supriya.ugens.SinOsc.ar(
                ...     frequency=[440, 442, 443],
                ... )
                >>> result = ugen_graph.clip(-0.25, 0.25)

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 000e997ea0d7e8637c9f9040547baa50
                    ugens:
                    -   SinOsc.ar/0:
                            frequency: 440.0
                            phase: 0.0
                    -   Clip.ar/0:
                            source: SinOsc.ar/0[0]
                            minimum: -0.25
                            maximum: 0.25
                    -   SinOsc.ar/1:
                            frequency: 442.0
                            phase: 0.0
                    -   Clip.ar/1:
                            source: SinOsc.ar/1[0]
                            minimum: -0.25
                            maximum: 0.25
                    -   SinOsc.ar/2:
                            frequency: 443.0
                            phase: 0.0
                    -   Clip.ar/2:
                            source: SinOsc.ar/2[0]
                            minimum: -0.25
                            maximum: 0.25
        """
        from . import Clip

        return self._compute_ugen_map(Clip, minimum=minimum, maximum=maximum)

    def cubed(self) -> "UGenOperable":
        """
        Calculates the cube of ugen graph.

        ::

            >>> source = supriya.ugens.DC.ar(source=0.5)
            >>> operation = source.cubed()
            >>> print(operation)
            synthdef:
                name: ad344666e7f3f60edac95b1ea40c412d
                ugens:
                -   DC.ar:
                        source: 0.5
                -   UnaryOpUGen(CUBED).ar:
                        source: DC.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.CUBED)

    def db_to_amplitude(self) -> "UGenOperable":
        """
        Converts ugen graph from decibels to amplitude.

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.ar()
                >>> result = ugen_graph.db_to_amplitude()

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: fe82aae42b01b2b43d427cafd77c1c22
                    ugens:
                    -   WhiteNoise.ar: null
                    -   UnaryOpUGen(DB_TO_AMPLITUDE).ar:
                            source: WhiteNoise.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.DB_TO_AMPLITUDE)

    def distort(self) -> "UGenOperable":
        """
        Distorts ugen graph non-linearly.

        ::

            >>> source = supriya.ugens.DC.ar(source=0.5)
            >>> operation = source.distort()
            >>> print(operation)
            synthdef:
                name: bb632e15f448820d93b3880ad943617b
                ugens:
                -   DC.ar:
                        source: 0.5
                -   UnaryOpUGen(DISTORT).ar:
                        source: DC.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.DISTORT)

    def exponential(self) -> "UGenOperable":
        """
        Calculates the natural exponential function of ugen graph.

        ::

            >>> source = supriya.ugens.DC.ar(source=0.5)
            >>> operation = source.exponential()
            >>> print(operation)
            synthdef:
                name: f3b8b1036b3cceddf116c3f6a3c5a9a0
                ugens:
                -   DC.ar:
                        source: 0.5
                -   UnaryOpUGen(EXPONENTIAL).ar:
                        source: DC.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.EXPONENTIAL)

    def floor(self) -> "UGenOperable":
        """
        Calculates the floor of ugen graph.

        ::

            >>> source = supriya.ugens.DC.ar(source=0.5)
            >>> operation = source.floor()
            >>> print(operation)
            synthdef:
                name: 407228cfdb74bdd79b51c425fb8a7f77
                ugens:
                -   DC.ar:
                        source: 0.5
                -   UnaryOpUGen(FLOOR).ar:
                        source: DC.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.FLOOR)

    def fractional_part(self) -> "UGenOperable":
        """
        Calculates the fraction part of ugen graph.

        ::

            >>> source = supriya.ugens.DC.ar(source=0.5)
            >>> operation = source.fractional_part()
            >>> print(operation)
            synthdef:
                name: c663d5ee6c7c5347c043727c628af658
                ugens:
                -   DC.ar:
                        source: 0.5
                -   UnaryOpUGen(FRACTIONAL_PART).ar:
                        source: DC.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.FRACTIONAL_PART)

    def hanning_window(self) -> "UGenOperable":
        """
        Calculates Hanning-window of ugen graph.

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.LFNoise2.ar()
                >>> result = ugen_graph.hanning_window()

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 18cb43db42ae3499f2c233e83df877fd
                    ugens:
                    -   LFNoise2.ar:
                            frequency: 500.0
                    -   UnaryOpUGen(HANNING_WINDOW).ar:
                            source: LFNoise2.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.HANNING_WINDOW)

    def hz_to_midi(self) -> "UGenOperable":
        """
        Converts ugen graph from Hertz to midi note number.

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.ar()
                >>> result = ugen_graph.hz_to_midi()

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 227a6ae85bc89b3af939cff32f54e36a
                    ugens:
                    -   WhiteNoise.ar: null
                    -   UnaryOpUGen(HZ_TO_MIDI).ar:
                            source: WhiteNoise.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.HZ_TO_MIDI)

    def hz_to_octave(self) -> "UGenOperable":
        """
        Converts ugen graph from Hertz to octave number.

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.ar()
                >>> result = ugen_graph.hz_to_octave()

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: e4fd4ca786d453fc5dfb955c63b6fbf6
                    ugens:
                    -   WhiteNoise.ar: null
                    -   UnaryOpUGen(HZ_TO_OCTAVE).ar:
                            source: WhiteNoise.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.HZ_TO_OCTAVE)

    def is_equal_to(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Calculates equality between ugen graph and `expr`.

        ::

            >>> left = supriya.ugens.SinOsc.ar()
            >>> right = supriya.ugens.WhiteNoise.kr()
            >>> operation = left.is_equal_to(right)
            >>> print(operation)
            synthdef:
                name: 8287d890708ce26adff4968d63d494a0
                ugens:
                -   SinOsc.ar:
                        frequency: 440.0
                        phase: 0.0
                -   WhiteNoise.kr: null
                -   BinaryOpUGen(EQUAL).ar:
                        left: SinOsc.ar[0]
                        right: WhiteNoise.kr[0]

        Returns ugen graph.
        """
        return self._compute_binary_op(self, expr, BinaryOperator.EQUAL)

    def is_not_equal_to(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Calculates inequality between ugen graph and `expr`.

        ::

            >>> left = supriya.ugens.SinOsc.ar()
            >>> right = supriya.ugens.WhiteNoise.kr()
            >>> operation = left.is_not_equal_to(right)
            >>> print(operation)
            synthdef:
                name: b9f77aa86bc08a3b023d8f664afef05d
                ugens:
                -   SinOsc.ar:
                        frequency: 440.0
                        phase: 0.0
                -   WhiteNoise.kr: null
                -   BinaryOpUGen(NOT_EQUAL).ar:
                        left: SinOsc.ar[0]
                        right: WhiteNoise.kr[0]

        Returns ugen graph.
        """
        return self._compute_binary_op(self, expr, BinaryOperator.NOT_EQUAL)

    def lagged(self, lag_time=0.5) -> "UGenOperable":
        """
        Lags ugen graph.

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.ar()
                >>> result = ugen_graph.lagged(0.5)

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 6c3e2cc1a3d54ecfaa49d567a84eae77
                    ugens:
                    -   WhiteNoise.ar: null
                    -   Lag.ar:
                            source: WhiteNoise.ar[0]
                            lag_time: 0.5

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.SinOsc.ar(
                ...     frequency=[440, 442, 443],
                ... )
                >>> result = ugen_graph.lagged(0.5)

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 67098a4ddab35f6e1333a80a226bf559
                    ugens:
                    -   SinOsc.ar/0:
                            frequency: 440.0
                            phase: 0.0
                    -   Lag.ar/0:
                            source: SinOsc.ar/0[0]
                            lag_time: 0.5
                    -   SinOsc.ar/1:
                            frequency: 442.0
                            phase: 0.0
                    -   Lag.ar/1:
                            source: SinOsc.ar/1[0]
                            lag_time: 0.5
                    -   SinOsc.ar/2:
                            frequency: 443.0
                            phase: 0.0
                    -   Lag.ar/2:
                            source: SinOsc.ar/2[0]
                            lag_time: 0.5
        """
        from . import Lag

        return self._compute_ugen_map(Lag, lag_time=lag_time)

    def log(self) -> "UGenOperable":
        """
        Calculates the natural logarithm of ugen graph.

        ::

            >>> source = supriya.ugens.DC.ar(source=0.5)
            >>> operation = source.log()
            >>> print(operation)
            synthdef:
                name: 4da44dab9d935efd1cf098b4d7cec420
                ugens:
                -   DC.ar:
                        source: 0.5
                -   UnaryOpUGen(LOG).ar:
                        source: DC.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.LOG)

    def log2(self) -> "UGenOperable":
        """
        Calculates the base-2 logarithm of ugen graph.

        ::

            >>> source = supriya.ugens.DC.ar(source=0.5)
            >>> operation = source.log2()
            >>> print(operation)
            synthdef:
                name: f956f79a387ffbeb409326046397b4dd
                ugens:
                -   DC.ar:
                        source: 0.5
                -   UnaryOpUGen(LOG2).ar:
                        source: DC.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.LOG2)

    def log10(self) -> "UGenOperable":
        """
        Calculates the base-10 logarithm of ugen graph.

        ::

            >>> source = supriya.ugens.DC.ar(source=0.5)
            >>> operation = source.log10()
            >>> print(operation)
            synthdef:
                name: 122d9333b8ac76164782d00707d3386a
                ugens:
                -   DC.ar:
                        source: 0.5
                -   UnaryOpUGen(LOG10).ar:
                        source: DC.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.LOG10)

    def midi_to_hz(self) -> "UGenOperable":
        """
        Converts ugen graph from midi note number to Hertz.

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.ar()
                >>> result = ugen_graph.midi_to_hz()

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 5faaa2c74715175625d774b20952f263
                    ugens:
                    -   WhiteNoise.ar: null
                    -   UnaryOpUGen(MIDI_TO_HZ).ar:
                            source: WhiteNoise.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.MIDI_TO_HZ)

    def octave_to_hz(self) -> "UGenOperable":
        """
        Converts ugen graph from octave number to Hertz.

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.ar()
                >>> result = ugen_graph.octave_to_hz()

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 04c00b0f32088eb5e4cef0549aed6d96
                    ugens:
                    -   WhiteNoise.ar: null
                    -   UnaryOpUGen(OCTAVE_TO_HZ).ar:
                            source: WhiteNoise.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.OCTAVE_TO_HZ)

    def power(self, expr: "UGenOperand") -> "UGenOperable":
        """
        Raises ugen graph to the power of `expr`.

        ::

            >>> left = supriya.ugens.SinOsc.ar()
            >>> right = supriya.ugens.WhiteNoise.kr()
            >>> operation = left.power(right)
            >>> print(operation)
            synthdef:
                name: 06d6d3fe992bff8fce9ef55db6863c2a
                ugens:
                -   SinOsc.ar:
                        frequency: 440.0
                        phase: 0.0
                -   WhiteNoise.kr: null
                -   BinaryOpUGen(POWER).ar:
                        left: SinOsc.ar[0]
                        right: WhiteNoise.kr[0]

        Returns ugen graph.
        """
        return self._compute_binary_op(self, expr, BinaryOperator.POWER)

    def range(self, minimum=0.0, maximum=1.0) -> "UGenOperable":
        if self.signal_range == SignalRange.BIPOLAR:
            return self.scale(-1, 1, minimum, maximum)
        return self.scale(0, 1, minimum, maximum)

    def exponential_range(self, minimum=0.01, maximum=1.0) -> "UGenOperable":
        if self.signal_range == SignalRange.BIPOLAR:
            return self.scale(-1, 1, minimum, maximum, exponential=True)
        return self.scale(0, 1, minimum, maximum, exponential=True)

    def ratio_to_semitones(self) -> "UGenOperable":
        """
        Converts ugen graph from frequency ratio to semitone distance.

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.ar()
                >>> result = ugen_graph.ratio_to_semitones()

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 2e23630ade4fab35fc821c190b7f33db
                    ugens:
                    -   WhiteNoise.ar: null
                    -   UnaryOpUGen(RATIO_TO_SEMITONES).ar:
                            source: WhiteNoise.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.RATIO_TO_SEMITONES)

    def rectangle_window(self) -> "UGenOperable":
        """
        Calculates rectangle-window of ugen graph.

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.LFNoise2.ar()
                >>> result = ugen_graph.rectangle_window()

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 0d296187bbdb205f3a283f301a5fad61
                    ugens:
                    -   LFNoise2.ar:
                            frequency: 500.0
                    -   UnaryOpUGen(RECTANGLE_WINDOW).ar:
                            source: LFNoise2.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.RECTANGLE_WINDOW)

    def reciprocal(self) -> "UGenOperable":
        """
        Calculates reciprocal of ugen graph.

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.LFNoise2.ar()
                >>> result = ugen_graph.reciprocal()

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 2e1c714d0def9d5c310197861d725559
                    ugens:
                    -   LFNoise2.ar:
                            frequency: 500.0
                    -   UnaryOpUGen(RECIPROCAL).ar:
                            source: LFNoise2.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.RECIPROCAL)

    def s_curve(self) -> "UGenOperable":
        """
        Calculates S-curve of ugen graph.

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.LFNoise2.ar()
                >>> result = ugen_graph.s_curve()

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 21bcaf49922e2c4124d4cadba85c00ac
                    ugens:
                    -   LFNoise2.ar:
                            frequency: 500.0
                    -   UnaryOpUGen(S_CURVE).ar:
                            source: LFNoise2.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.S_CURVE)

    def scale(
        self,
        input_minimum,
        input_maximum,
        output_minimum,
        output_maximum,
        exponential=False,
    ) -> "UGenOperable":
        """
        Scales ugen graph from `input_minimum` and `input_maximum` to `output_minimum` and `output_maximum`.

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.ar()
                >>> result = ugen_graph.scale(-1, 1, 0.5, 0.75)

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: e2295e64ed7b9c949ec22ccdc82520e3
                    ugens:
                    -   WhiteNoise.ar: null
                    -   MulAdd.ar:
                            source: WhiteNoise.ar[0]
                            multiplier: 0.125
                            addend: 0.625

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.SinOsc.ar(
                ...     frequency=[440, 442, 443],
                ... )
                >>> result = ugen_graph.scale(-1, 1, 0.5, 0.75, exponential=True)

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 88dca305143542bd40a82d8a6a337306
                    ugens:
                    -   SinOsc.ar/0:
                            frequency: 440.0
                            phase: 0.0
                    -   LinExp.ar/0:
                            source: SinOsc.ar/0[0]
                            input_minimum: -1.0
                            input_maximum: 1.0
                            output_minimum: 0.5
                            output_maximum: 0.75
                    -   SinOsc.ar/1:
                            frequency: 442.0
                            phase: 0.0
                    -   LinExp.ar/1:
                            source: SinOsc.ar/1[0]
                            input_minimum: -1.0
                            input_maximum: 1.0
                            output_minimum: 0.5
                            output_maximum: 0.75
                    -   SinOsc.ar/2:
                            frequency: 443.0
                            phase: 0.0
                    -   LinExp.ar/2:
                            source: SinOsc.ar/2[0]
                            input_minimum: -1.0
                            input_maximum: 1.0
                            output_minimum: 0.5
                            output_maximum: 0.75
        """
        from . import LinExp, LinLin

        return self._compute_ugen_map(
            LinExp if exponential else LinLin,
            input_minimum=input_minimum,
            input_maximum=input_maximum,
            output_minimum=output_minimum,
            output_maximum=output_maximum,
        )

    def semitones_to_ratio(self) -> "UGenOperable":
        """
        Converts ugen graph from semitone distance to frequency ratio.

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.WhiteNoise.ar()
                >>> result = ugen_graph.semitones_to_ratio()

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: f77ac2c24b06f8e620817f14285c2877
                    ugens:
                    -   WhiteNoise.ar: null
                    -   UnaryOpUGen(SEMITONES_TO_RATIO).ar:
                            source: WhiteNoise.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.SEMITONES_TO_RATIO)

    def sign(self) -> "UGenOperable":
        """
        Calculates sign of ugen graph.

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.LFNoise2.ar()
                >>> result = ugen_graph.sign()

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 6f62abd8306dbf1aae66c09dd98203b5
                    ugens:
                    -   LFNoise2.ar:
                            frequency: 500.0
                    -   UnaryOpUGen(SIGN).ar:
                            source: LFNoise2.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.SIGN)

    def softclip(self) -> "UGenOperable":
        """
        Distorts ugen graph non-linearly.
        """
        return self._compute_unary_op(self, UnaryOperator.SOFTCLIP)

    def square_root(self) -> "UGenOperable":
        """
        Calculates square root of ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.SQUARE_ROOT)

    def squared(self) -> "UGenOperable":
        """
        Calculates square of ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.SQUARED)

    def sum(self) -> "UGenOperable":
        """
        Sums ugen graph.

        .. container:: example

            **Example 1:**

            ::

                >>> ugen_graph = supriya.ugens.LFNoise2.ar()
                >>> result = ugen_graph.sum()

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: 350f2065d4edc69244399dcaff5a1ceb
                    ugens:
                    -   LFNoise2.ar:
                            frequency: 500.0

        .. container:: example

            **Example 2:**

            ::

                >>> ugen_graph = supriya.ugens.SinOsc.ar(frequency=[440, 442, 443])
                >>> result = ugen_graph.sum()

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: a1d26283f87b8b445db982ff0e831fb7
                    ugens:
                    -   SinOsc.ar/0:
                            frequency: 440.0
                            phase: 0.0
                    -   SinOsc.ar/1:
                            frequency: 442.0
                            phase: 0.0
                    -   SinOsc.ar/2:
                            frequency: 443.0
                            phase: 0.0
                    -   Sum3.ar:
                            input_one: SinOsc.ar/0[0]
                            input_two: SinOsc.ar/1[0]
                            input_three: SinOsc.ar/2[0]

        Returns ugen graph.
        """
        from . import Mix

        return Mix.new(self)

    def tanh(self) -> "UGenOperable":
        """
        Calculates hyperbolic tangent of ugen graph.

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.LFNoise2.ar()
                >>> result = ugen_graph.tanh()

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: e74aa9abf6e389d8ca39d2c9828d81be
                    ugens:
                    -   LFNoise2.ar:
                            frequency: 500.0
                    -   UnaryOpUGen(TANH).ar:
                            source: LFNoise2.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.TANH)

    def transpose(self, semitones) -> "UGenOperable":
        """
        Transposes ugen graph by `semitones`.

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.LFNoise2.ar()
                >>> result = ugen_graph.transpose([0, 3, 7])

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: c481c3d42e3cfcee0267250247dab51f
                    ugens:
                    -   LFNoise2.ar:
                            frequency: 500.0
                    -   UnaryOpUGen(HZ_TO_MIDI).ar:
                            source: LFNoise2.ar[0]
                    -   UnaryOpUGen(MIDI_TO_HZ).ar/0:
                            source: UnaryOpUGen(HZ_TO_MIDI).ar[0]
                    -   BinaryOpUGen(ADDITION).ar/0:
                            left: UnaryOpUGen(HZ_TO_MIDI).ar[0]
                            right: 3.0
                    -   UnaryOpUGen(MIDI_TO_HZ).ar/1:
                            source: BinaryOpUGen(ADDITION).ar/0[0]
                    -   BinaryOpUGen(ADDITION).ar/1:
                            left: UnaryOpUGen(HZ_TO_MIDI).ar[0]
                            right: 7.0
                    -   UnaryOpUGen(MIDI_TO_HZ).ar/2:
                            source: BinaryOpUGen(ADDITION).ar/1[0]

        Returns ugen graph.
        """
        return (self.hz_to_midi() + semitones).midi_to_hz()

    def triangle_window(self) -> "UGenOperable":
        """
        Calculates triangle-window of ugen graph.

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.LFNoise2.ar()
                >>> result = ugen_graph.triangle_window()

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: ebb1820b9d08a639565b5090b53681db
                    ugens:
                    -   LFNoise2.ar:
                            frequency: 500.0
                    -   UnaryOpUGen(TRIANGLE_WINDOW).ar:
                            source: LFNoise2.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.TRIANGLE_WINDOW)

    def welch_window(self) -> "UGenOperable":
        """
        Calculates Welch-window of ugen graph.

        .. container:: example

            ::

                >>> ugen_graph = supriya.ugens.LFNoise2.ar()
                >>> result = ugen_graph.welch_window()

            ::

                >>> supriya.graph(result)  # doctest: +SKIP

            ::

                >>> print(result)
                synthdef:
                    name: ...
                    ugens:
                    -   LFNoise2.ar:
                            frequency: 500.0
                    -   UnaryOpUGen(WELCH_WINDOW).ar:
                            source: LFNoise2.ar[0]

        Returns ugen graph.
        """
        return self._compute_unary_op(self, UnaryOperator.WELCH_WINDOW)

    @property
    def signal_range(self):
        raise NotImplementedError


class UGenSerializable(Protocol):
    def serialize(self) -> Sequence[Union[SupportsFloat, "OutputProxy"]]:
        pass


class UGenArray(UGenOperable, Sequence):

    ### INITIALIZER ###

    def __init__(self, ugens):
        assert isinstance(ugens, Iterable)
        ugens = tuple(ugens)
        assert len(ugens)
        self._ugens = ugens

    ### SPECIAL METHODS ###

    def __getitem__(self, i):
        return self.ugens[i]

    def __len__(self):
        return len(self.ugens)

    def __repr__(self):
        return "{}({{{}}})".format(type(self).__name__, len(self))

    ### PUBLIC PROPERTIES ###

    @property
    def signal_range(self):
        return max(_.signal_range for _ in self)

    @property
    def ugens(self):
        return self._ugens


class OutputProxy(UGenOperable):
    ### INITIALIZER ###

    def __init__(self, *, source: "UGen", output_index: int) -> None:
        self._output_index = output_index
        self._source = source

    ### SPECIAL METHODS ###

    def __eq__(self, expr):
        if not isinstance(expr, type(self)):
            return False
        if self._output_index != expr._output_index:
            return False
        if self._source != expr._source:
            return False
        return True

    def __hash__(self) -> int:
        hash_values = (type(self), self._output_index, self._source)
        return hash(hash_values)

    def __iter__(self):
        yield self

    def __len__(self) -> int:
        return 1

    def __repr__(self) -> str:
        return "{!r}[{}]".format(self.source, self.output_index)

    ### PRIVATE METHODS ###

    def _get_output_number(self):
        return self._output_index

    def _get_source(self):
        return self._source

    ### PUBLIC PROPERTIES ###

    @property
    def calculation_rate(self):
        return self.source.calculation_rate

    @property
    def has_done_flag(self):
        return self.source.has_done_flag

    @property
    def output_index(self) -> int:
        return self._output_index

    @property
    def signal_range(self) -> SignalRange:
        return self.source.signal_range

    @property
    def source(self):
        return self._source


class UGen(UGenOperable):
    """
    A UGen.
    """

    ### CLASS VARIABLES ###

    _default_channel_count = 1

    _has_settable_channel_count = False

    _has_done_flag = False

    _is_input = False

    _is_output = False

    _is_pure = False

    _is_width_first = False

    _ordered_input_names: Dict[
        str, Union[Default, Missing, SupportsFloat, str, None]
    ] = {}

    _signal_range: int = SignalRange.BIPOLAR

    _unexpanded_input_names: Tuple[str, ...] = ()

    _valid_calculation_rates: Tuple[int, ...] = ()

    ### INITIALIZER ###

    def __init__(
        self,
        *,
        calculation_rate: CalculationRateLike = None,
        special_index: int = 0,
        **kwargs,
    ) -> None:
        from ..synthdefs import Parameter, SynthDefBuilder

        calculation_rate_ = CalculationRate.from_expr(calculation_rate)
        if self._valid_calculation_rates:
            assert calculation_rate_ in self._valid_calculation_rates
        calculation_rate_, kwargs = self._postprocess_kwargs(
            calculation_rate=calculation_rate_, **kwargs
        )
        self._calculation_rate = calculation_rate_
        self._inputs: List[SupportsFloat] = []
        self._input_names: List[str] = []
        self._special_index = special_index
        ugenlike_prototype = (UGen, Parameter)
        for input_name in self._ordered_input_names:
            input_value = None
            if input_name in kwargs:
                input_value = kwargs.pop(input_name)
                # print(type(self).__name__, input_name, type(input_value))
            if isinstance(input_value, ugenlike_prototype):
                assert len(input_value) == 1
                input_value = input_value[0]
            else:
                try:
                    input_value = float(input_value)  # type: ignore
                except TypeError:
                    pass
            if self._is_unexpanded_input_name(input_name):
                if not isinstance(input_value, Sequence):
                    input_value = (input_value,)
                if isinstance(input_value, Sequence):
                    input_value = tuple(input_value)
                elif not self._is_valid_input(input_value):
                    raise ValueError(input_name, input_value)
            elif not self._is_valid_input(input_value):
                raise ValueError(input_name, input_value)
            self._configure_input(input_name, input_value)
        if kwargs:
            raise ValueError(kwargs)
        assert all(isinstance(_, (OutputProxy, float)) for _ in self.inputs)
        self._validate_inputs()
        self._uuid = None
        if SynthDefBuilder._active_builders:
            builder = SynthDefBuilder._active_builders[-1]
            self._uuid = builder._uuid
            builder._add_ugens(self)
        self._check_inputs_share_same_uuid()

    ### SPECIAL METHODS ###

    def __getitem__(self, i):
        """
        Gets output proxy at index `i`.

        ::

            >>> ugen = supriya.ugens.SinOsc.ar()
            >>> ugen[0]
            SinOsc.ar()[0]

        Returns output proxy.
        """
        return self._get_output_proxy(i)

    def __len__(self):
        """
        Gets number of ugen outputs.

        Returns integer.
        """
        return getattr(self, "_channel_count", self._default_channel_count)

    def __repr__(self):
        """
        Gets interpreter representation of ugen.

        ::

            >>> ugen = supriya.ugens.SinOsc.ar()
            >>> repr(ugen)
            'SinOsc.ar()'

        ::

            >>> ugen = supriya.ugens.WhiteNoise.kr()
            >>> repr(ugen)
            'WhiteNoise.kr()'

        ::

            >>> ugen = supriya.ugens.Rand.ir()
            >>> repr(ugen)
            'Rand.ir()'

        Returns string.
        """
        return f"{type(self).__name__}.{self.calculation_rate.token}()"

    ### PRIVATE METHODS ###

    @staticmethod
    def _as_audio_rate_input(expr):
        from . import DC, K2A, Silence

        if isinstance(expr, (int, float)):
            if expr == 0:
                return Silence.ar()
            return DC.ar(expr)
        elif isinstance(expr, (UGen, OutputProxy)):
            if expr.calculation_rate == CalculationRate.AUDIO:
                return expr
            return K2A.ar(source=expr)
        elif isinstance(expr, Iterable):
            return UGenArray(UGen._as_audio_rate_input(x) for x in expr)
        raise ValueError(expr)

    def _add_constant_input(self, name, value):
        self._inputs.append(float(value))
        self._input_names.append(name)

    def _add_ugen_input(self, name, ugen, output_index=None):
        if isinstance(ugen, OutputProxy):
            output_proxy = ugen
        else:
            output_proxy = OutputProxy(source=ugen, output_index=output_index)
        self._inputs.append(output_proxy)
        self._input_names.append(name)

    def _check_inputs_share_same_uuid(self):
        for input_ in self.inputs:
            if not isinstance(input_, OutputProxy):
                continue
            if input_.source._uuid != self._uuid:
                message = "UGen input in different scope: {!r}"
                message = message.format(input_.source)
                raise ValueError(message)

    def _check_rate_same_as_first_input_rate(self):
        first_input_rate = CalculationRate.from_expr(self.inputs[0])
        return self.calculation_rate == first_input_rate

    def _check_range_of_inputs_at_audio_rate(self, start=None, stop=None):
        if self.calculation_rate != CalculationRate.AUDIO:
            return True
        for input_ in self.inputs[start:stop]:
            calculation_rate = CalculationRate.from_expr(input_)
            if calculation_rate != CalculationRate.AUDIO:
                return False
        return True

    def _configure_input(self, name, value):
        from ..synthdefs import Parameter

        ugen_prototype = (OutputProxy, Parameter, UGen)
        if hasattr(value, "__float__"):
            self._add_constant_input(name, float(value))
        elif isinstance(value, ugen_prototype):
            self._add_ugen_input(name, value._get_source(), value._get_output_number())
        elif isinstance(value, Sequence):
            if name not in self._unexpanded_input_names:
                raise ValueError(name, self._unexpanded_input_names)
            for i, x in enumerate(value):
                if hasattr(x, "__float__"):
                    self._add_constant_input((name, i), float(x))
                elif isinstance(x, ugen_prototype):
                    self._add_ugen_input(
                        (name, i), x._get_source(), x._get_output_number()
                    )
                else:
                    raise Exception("{!r} {!r}".format(value, x))
        else:
            raise ValueError(f"Invalid input: {value!r}")

    @staticmethod
    def _expand_dictionary(dictionary, unexpanded_input_names=None):
        """
        Expands a dictionary into multichannel dictionaries.

        ::

            >>> dictionary = {"foo": 0, "bar": (1, 2), "baz": (3, 4, 5)}
            >>> result = UGen._expand_dictionary(dictionary)
            >>> for x in result:
            ...     sorted(x.items())
            ...
            [('bar', 1), ('baz', 3), ('foo', 0)]
            [('bar', 2), ('baz', 4), ('foo', 0)]
            [('bar', 1), ('baz', 5), ('foo', 0)]

        ::

            >>> dictionary = {"bus": (8, 9), "source": (1, 2, 3)}
            >>> result = UGen._expand_dictionary(
            ...     dictionary,
            ...     unexpanded_input_names=("source",),
            ... )
            >>> for x in result:
            ...     sorted(x.items())
            ...
            [('bus', 8), ('source', (1, 2, 3))]
            [('bus', 9), ('source', (1, 2, 3))]
        """
        from ..synthdefs import Parameter

        dictionary = dictionary.copy()
        cached_unexpanded_inputs = {}
        if unexpanded_input_names is not None:
            for input_name in unexpanded_input_names:
                if input_name not in dictionary:
                    continue
                cached_unexpanded_inputs[input_name] = dictionary[input_name]
                del dictionary[input_name]
        maximum_length = 1
        result = []
        prototype = (Sequence, UGen, Parameter)
        for name, value in dictionary.items():
            if isinstance(value, prototype) and not isinstance(value, str):
                maximum_length = max(maximum_length, len(value))
        for i in range(maximum_length):
            result.append({})
            for name, value in dictionary.items():
                if isinstance(value, prototype) and not isinstance(value, str):
                    value = value[i % len(value)]
                    result[i][name] = value
                else:
                    result[i][name] = value
        for expanded_inputs in result:
            expanded_inputs.update(cached_unexpanded_inputs)
        return result

    def _get_done_action(self):
        if "done_action" not in self._ordered_input_names:
            return None
        return DoneAction.from_expr(int(self.done_action))

    @staticmethod
    def _get_method_for_rate(cls, calculation_rate):
        calculation_rate = CalculationRate.from_expr(calculation_rate)
        if calculation_rate == CalculationRate.AUDIO:
            return cls.ar
        elif calculation_rate == CalculationRate.CONTROL:
            return cls.kr
        elif calculation_rate == CalculationRate.SCALAR:
            if hasattr(cls, "ir"):
                return cls.ir
            return cls.kr
        return cls.new

    def _get_output_number(self):
        return 0

    def _get_outputs(self):
        return [self.calculation_rate] * len(self)

    def _get_source(self):
        return self

    def _is_unexpanded_input_name(self, input_name):
        if self._unexpanded_input_names:
            if input_name in self._unexpanded_input_names:
                return True
        return False

    def _is_valid_input(self, input_value):
        if isinstance(input_value, OutputProxy):
            return True
        elif hasattr(input_value, "__float__"):
            return True
        return False

    @classmethod
    def _new_expanded(cls, **kwargs) -> Union[OutputProxy, UGenArray]:
        output_proxies = []
        for input_dict in UGen._expand_dictionary(
            kwargs, unexpanded_input_names=cls._unexpanded_input_names
        ):
            ugen = cls._new_single(**input_dict)
            if len(ugen) <= 1:
                output_proxies.append(ugen)
            else:
                output_proxies.extend(ugen[:])
        if len(output_proxies) == 1:
            return output_proxies[0]
        return UGenArray(output_proxies)

    @classmethod
    def _new_single(cls, **kwargs):
        return cls(**kwargs)

    def _optimize_graph(self, sort_bundles):
        if self._is_pure:
            self._perform_dead_code_elimination(sort_bundles)

    def _perform_dead_code_elimination(self, sort_bundles):
        sort_bundle = sort_bundles.get(self, None)
        if not sort_bundle or sort_bundle.descendants:
            return
        del sort_bundles[self]
        for antecedent in tuple(sort_bundle.antecedents):
            antecedent_bundle = sort_bundles.get(antecedent, None)
            if not antecedent_bundle:
                continue
            antecedent_bundle.descendants.remove(self)
            antecedent._optimize_graph(sort_bundles)

    def _postprocess_kwargs(
        self, *, calculation_rate: CalculationRate, **kwargs
    ) -> Tuple[CalculationRate, Dict[str, Any]]:
        return calculation_rate, kwargs

    def _validate_inputs(self):
        pass

    ### PRIVATE PROPERTIES ###

    @property
    def _has_done_action(self) -> bool:
        return "done_action" in self._ordered_input_names

    ### PUBLIC PROPERTIES ###

    @property
    def calculation_rate(self):
        """
        Gets calculation-rate of ugen.

        ::

            >>> ugen = supriya.ugens.SinOsc.ar(
            ...     frequency=supriya.ugens.WhiteNoise.kr(),
            ...     phase=0.5,
            ... )
            >>> ugen.calculation_rate
            CalculationRate.AUDIO

        Returns calculation-rate.
        """
        return self._calculation_rate

    @property
    def has_done_flag(self) -> bool:
        return self._has_done_flag

    @property
    def inputs(self):
        """
        Gets inputs of ugen.

        ::

            >>> ugen = supriya.ugens.SinOsc.ar(
            ...     frequency=supriya.ugens.WhiteNoise.kr(),
            ...     phase=0.5,
            ... )
            >>> for input_ in ugen.inputs:
            ...     input_
            ...
            WhiteNoise.kr()[0]
            0.5

        Returns tuple.
        """
        return tuple(self._inputs)

    @property
    def is_input_ugen(self) -> bool:
        return self._is_input

    @property
    def is_output_ugen(self) -> bool:
        return self._is_output

    @property
    def outputs(self) -> Tuple[OutputProxy, ...]:
        """
        Gets outputs of ugen.

        ::

            >>> ugen = supriya.ugens.SinOsc.ar(
            ...     frequency=supriya.ugens.WhiteNoise.kr(),
            ...     phase=0.5,
            ... )
            >>> ugen.outputs
            (CalculationRate.AUDIO,)

        Returns tuple.
        """
        return tuple(self._get_outputs())

    @property
    def signal_range(self):
        """
        Gets signal range of ugen.

        ::

            >>> ugen = supriya.ugens.SinOsc.ar()
            >>> ugen.signal_range
            SignalRange.BIPOLAR

        A bipolar signal range indicates that the ugen generates signals above and below
        zero.

        A unipolar signal range indicates that the ugen only generates signals of 0 or
        greater.

        Returns signal range.
        """
        return self._signal_range

    @property
    def special_index(self):
        """
        Gets special index of ugen.

        ::

            >>> ugen = supriya.ugens.SinOsc.ar(
            ...     frequency=supriya.ugens.WhiteNoise.kr(),
            ...     phase=0.5,
            ... )
            >>> ugen.special_index
            0

        The `special index` of most ugens will be 0. SuperColliders's synth definition
        file format uses the special index to store the operator id for binary and unary
        operator ugens, and the parameter index of controls.

        Returns integer.
        """
        return self._special_index


UGenOperand: TypeAlias = Union[
    SupportsFloat, UGenOperable, Sequence[Union[SupportsFloat, UGenOperable]]
]

UGenInitScalarParam: TypeAlias = Union[SupportsFloat, OutputProxy]

UGenInitVectorParam: TypeAlias = Union[Sequence[UGenInitScalarParam], UGenSerializable]

UGenRateScalarParam: TypeAlias = Union[SupportsFloat, UGenOperable, UGenSerializable]

UGenRateVectorParam: TypeAlias = Union[
    UGenRateScalarParam, Sequence[UGenRateScalarParam]
]


@ugen(is_pure=True)
class UnaryOpUGen(UGen):
    """
    A unary operator ugen, created by applying a unary operator to a ugen.

    ::

        >>> ugen = supriya.ugens.SinOsc.ar()
        >>> unary_op_ugen = abs(ugen)
        >>> unary_op_ugen
        UnaryOpUGen.ar()[0]

    ::

        >>> unary_op_ugen.source.operator
        UnaryOperator.ABSOLUTE_VALUE
    """

    ### CLASS VARIABLES ###

    source = param()

    ### PUBLIC PROPERTIES ###

    @property
    def operator(self) -> UnaryOperator:
        """
        Gets operator of UnaryOpUgen.

        ::

            >>> source = supriya.ugens.SinOsc.ar()
            >>> unary_op_ugen = -source
            >>> unary_op_ugen.source.operator
            UnaryOperator.NEGATIVE

        Returns unary operator.
        """
        return UnaryOperator(self.special_index)


@ugen(is_pure=True)
class BinaryOpUGen(UGen):
    """
    A binary operator ugen, created by applying a binary operator to two ugens.

    ::

        >>> left_operand = supriya.ugens.SinOsc.ar()
        >>> right_operand = supriya.ugens.WhiteNoise.kr()
        >>> binary_op_ugen = left_operand * right_operand
        >>> binary_op_ugen
        BinaryOpUGen.ar()[0]

    ::

        >>> binary_op_ugen.source.operator
        BinaryOperator.MULTIPLICATION
    """

    left = param()
    right = param()

    def __init__(
        self,
        *,
        calculation_rate: CalculationRateLike,
        left: UGenInitScalarParam,
        right: UGenInitScalarParam,
        special_index: int,
    ) -> None:
        super().__init__(
            calculation_rate=calculation_rate,
            left=left,
            right=right,
            special_index=special_index,
        )

    @classmethod
    def _new_single(
        cls, calculation_rate=None, special_index=None, left=None, right=None, **kwargs
    ):
        a = left
        b = right
        if special_index == BinaryOperator.MULTIPLICATION:
            if a == 0:
                return 0
            if b == 0:
                return 0
            if a == 1:
                return b
            if a == -1:
                return -b
            if b == 1:
                return a
            if b == -1:
                return -a
        if special_index == BinaryOperator.ADDITION:
            if a == 0:
                return b
            if b == 0:
                return a
        if special_index == BinaryOperator.SUBTRACTION:
            if a == 0:
                return -b
            if b == 0:
                return a
        if special_index == BinaryOperator.FLOAT_DIVISION:
            if b == 1:
                return a
            if b == -1:
                return -a
        return cls(
            calculation_rate=calculation_rate,
            special_index=special_index,
            left=a,
            right=b,
        )

    @property
    def operator(self) -> BinaryOperator:
        """
        Gets operator of BinaryOpUgen.

        ::

            >>> left = supriya.ugens.SinOsc.ar()
            >>> right = supriya.ugens.WhiteNoise.kr()
            >>> binary_op_ugen = left / right
            >>> binary_op_ugen.source.operator
            BinaryOperator.FLOAT_DIVISION

        Returns binary operator.
        """
        return BinaryOperator(self.special_index)


class PseudoUGen:
    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError
