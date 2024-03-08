"""
Higher-level utility library for use with standard argparse.
Define simple namespace-like class (like dataclass) with fields defined as
objects with classes defined in this library.
"""

# TODO use class decorator to inspect field type annotation, then write appropriate variant, defaultable and flag classes

from abc import ABC
import argparse
from collections.abc import Callable, Iterable, Iterator
from enum import Enum
from functools import partial
from pathlib import Path
import typing
from typing import Any, Literal, TypeGuard


type _Lazy[T] = Callable[[], T]
type _PairIter[L, R] = Iterator[tuple[L, R]]

Name = str
Value = Any


class ArgParsingError(Exception):
    pass


class ParameterAliasError(ArgParsingError):
    pass


class ParameterTypeError(ArgParsingError, TypeError):
    pass


class NotCliArgNamespaceError(ArgParsingError, TypeError):
    pass


class UnreachableCodeError(ArgParsingError):
    pass


# can't figure out what would work, because type[Literal[""]] does not
type LiteralVariants = Any
type ParamType[T] = type[T] | Callable[[str], T] | LiteralVariants


def cli_arg_namespace[Cls: type](cls: Cls) -> Cls:
    def __cli_arg_namespace_repr__(self) -> str:
        clsname = type(self).__name__
        fields = ", ".join(f"{name}={getattr(self, name)!r}" for name in vars(self))
        return f"{clsname}({fields})"

    add_cli_attr = partial(setattr, cls)

    add_cli_attr("__is_cli_arg_namespace__", True)
    add_cli_attr("__repr__", __cli_arg_namespace_repr__)
    add_cli_attr("_cli_args", dict[str, _BaseParam]())

    return cls


def _define_boolean(
    parser: argparse.ArgumentParser,
    in_shell_name: str,
    spec: "_Boolean",
    invert_bool: bool = False,
) -> None:
    define = parser.add_argument
    default = spec.default if not invert_bool else not spec.default

    match spec:
        case _FlagTrue(), _FlagFalse():
            define(
                f"--{in_shell_name}",
                *spec.aliases,
                action=f"store_{'true' if isinstance(spec, _FlagTrue) else 'false'}",
            )
        case _:
            define(f"--{in_shell_name}", *spec.aliases, type=bool, default=default)


def get_cli_arg_registry(arg_namespace: type) -> dict[str, "_BaseParam"]:
    try:
        return getattr(arg_namespace, "_cli_args")
    except AttributeError as e:
        raise NotCliArgNamespaceError(
            "provided class/object is not a CLI argument namespace"
        ) from e


def define_args(
    arg_namespace: type, parser: argparse.ArgumentParser | None = None
) -> argparse.ArgumentParser:
    if parser is None:
        parser = argparse.ArgumentParser()

    define = parser.add_argument
    define_boolean = partial(_define_boolean, parser)

    registry = get_cli_arg_registry(arg_namespace)

    # iterate over namespace fields
    for name, spec in vars(arg_namespace).items():
        if not isinstance(spec, _BaseParam):
            continue

        registry[name] = spec

        in_shell_name = name.replace("_", "-")

        match spec:
            # from the most specific (if necessary) to the least
            case _Boolean(
                aliases=aliases,
                default=default,
                with_opposite=with_opposite,
                opposite_prefix=opposite_prefix,
            ):
                define_boolean(in_shell_name, spec)

                if with_opposite:
                    # like --burgers, --no-burgers
                    define_boolean(
                        f"{opposite_prefix}{in_shell_name}", spec, invert_bool=True
                    )
            case _Parameter(
                aliases=aliases,
                cli_type=cli_type,
                default=default,
                choices=choices,
            ):
                if default is not None and callable(default):
                    default = default()

                if isinstance(spec, (_Defaultable, _EnumVariant)):
                    in_shell_name = f"--{in_shell_name}"

                define(
                    in_shell_name,
                    *aliases,
                    type=cli_type,
                    default=default,
                    choices=choices,
                )
            case _:
                raise UnreachableCodeError

    return parser


def iter_parsed_args(arg_namespace: type) -> _PairIter[Name, Value]:
    yield from get_cli_arg_registry(arg_namespace).items()


def parse_args[T](
    arg_namespace: type[T], parser: argparse.ArgumentParser | None = None
) -> T:
    if parser is None:
        parser = define_args(arg_namespace)

    args = parser.parse_args()

    # dumb class, simplest constructor
    # uninitialized
    ns = arg_namespace()

    read_cli_arg = partial(getattr, args)
    set_arg = partial(setattr, ns)

    for name, spec in get_cli_arg_registry(arg_namespace).items():
        val = read_cli_arg(name)

        # enums need special care - post-conversion
        match spec:
            case _EnumVariant():
                match val:
                    case str():
                        # convert
                        val = spec.enum_t[val.upper()]
                    case Enum():
                        pass
                    case _:
                        raise TypeError(
                            f"unexpected type of parsed CLI argument: expected {spec.enum_t.__qualname__}, got {type(val).__qualname__}"
                        )
                set_arg(name, val)
            case _:
                set_arg(name, val)

    return ns


# Functions below exist to cheat typecheckers, like dataclass.field does


def is_literal(val: object) -> TypeGuard[LiteralVariants]:
    return typing.get_origin(val) is Literal


def parameter[T](
    *aliases: str,
    type: ParamType[T],
    default: T | _Lazy[T] | None = None,
    choices: Iterable[T] | None = None,
    converter: Callable[[str], T] | None = None,
) -> T:
    return typing.cast(
        T,
        _Parameter(
            *aliases, cli_type=type, default=default, choices=choices, py_type=converter
        ),
    )


def positional[T](
    *aliases: str,
    type: ParamType[T],
    default: T | _Lazy[T] | None = None,
    choices: Iterable[T] | None = None,
    converter: Callable[[str], T] | None = None,
) -> T:
    """Positional argument"""
    return typing.cast(
        T,
        _Positional(
            *aliases, cli_type=type, default=default, choices=choices, py_type=converter
        ),
    )


def defaultable[T](
    *aliases: str,
    type: ParamType[T],
    default: str | T | _Lazy[T],
    choices: Iterable[T] | None = None,
    converter: Callable[[str], T] | None = None,
) -> T:
    """Short or long flag (-f | --flag | --alias | ...) with default value"""
    return typing.cast(
        T,
        _Defaultable(
            *aliases, cli_type=type, default=default, choices=choices, py_type=converter
        ),
    )


def boolean(
    *aliases: str,
    default: bool,
    with_opposite: bool = False,
    opposite_prefix: str = "no-",
) -> bool:
    """Boolean switch"""
    return typing.cast(
        bool,
        _Boolean(
            *aliases,
            default=default,
            with_opposite=with_opposite,
            opposite_prefix=opposite_prefix,
        ),
    )


def enum_variant[E: Enum](*aliases: str, e: type[E], default: E) -> E:
    """
    Assumes that enum values are named in UPPER_CASE and CLI argument will be
    given in lower_case"""

    return _EnumVariant(*aliases, enum_t=e, default=default)


def flag_true(
    *aliases: str, with_opposite: bool = False, opposite_prefix: str = "no-"
) -> bool:
    """True-by-default flag"""
    return typing.cast(
        bool,
        _FlagTrue(
            *aliases, with_opposite=with_opposite, opposite_prefix=opposite_prefix
        ),
    )


def flag_false(
    *aliases: str, with_opposite: bool = False, opposite_prefix: str = "no-"
) -> bool:
    """False-by-default flag"""
    return typing.cast(
        bool,
        _FlagFalse(
            *aliases, with_opposite=with_opposite, opposite_prefix=opposite_prefix
        ),
    )


# helpers
defaultable_int = partial(defaultable, type=int)
defaultable_float = partial(defaultable, type=float)
defaultable_str = partial(defaultable, type=str)
defaultable_path = partial(defaultable, type=Path)


class _BaseParam(ABC):
    pass


class _AliasableParam(_BaseParam):
    def __init__(self, aliases: tuple[str, ...]) -> None:
        super().__init__()
        self.aliases = aliases


class _Parameter[T](_AliasableParam):
    def __init__(
        self,
        *aliases: str,
        cli_type: ParamType[T],
        default: T | _Lazy[T] | None = None,
        choices: Iterable[T] | None = None,
        py_type: Callable[[str], T] | None = None,
    ) -> None:
        super().__init__(aliases)

        if is_literal(cli_type):
            choices = typing.get_args(cli_type)
            cli_type = type(choices[0])

            if any(type(c) != cli_type for c in choices):
                raise ParameterTypeError(
                    "for type given as typing.Literal, all literal variants "
                    "must be of the same underlying type"
                )

        self.cli_type = cli_type
        self.default = default
        self.choices = choices
        self.py_type = py_type


class _Positional[T](_Parameter[T]):
    """Positional argument"""

    def __init__(
        self,
        *aliases: str,
        cli_type: type[T] | LiteralVariants,
        default: T | _Lazy[T] | None = None,
        choices: Iterable[T] | None = None,
        py_type: Callable[[str], T] | None = None,
    ) -> None:
        if any(a.startswith("-") for a in aliases):
            raise ParameterAliasError(
                "Positional argument aliases must not start with '-'"
            )
        super().__init__(
            *aliases,
            cli_type=cli_type,
            default=default,
            choices=choices,
            py_type=py_type,
        )


class _Defaultable[T](_Parameter[T]):
    """short or long flag (-f | --flag | --alias | ...) with default value"""

    def __init__(
        self,
        *aliases: str,
        cli_type: ParamType,
        default: T | _Lazy[T],
        choices: Iterable[T] | LiteralVariants | None = None,
        py_type: Callable[[str], T] | None = None,
    ) -> None:
        if any(not a.startswith("-") for a in aliases):
            raise ParameterAliasError("Parameter aliases must start with '-'")
        super().__init__(
            *aliases,
            cli_type=cli_type,
            default=default,
            choices=choices,
            py_type=py_type,
        )


class _EnumVariant[E: Enum](_Parameter):
    def __init__(self, *aliases: str, enum_t: type[E], default: E) -> None:
        super().__init__(
            *aliases,
            cli_type=str,
            default=default,
            choices=tuple(variant.name.lower() for variant in enum_t),
            py_type=lambda e_str: enum_t[e_str.upper()],
        )
        self.enum_t = enum_t


class _Boolean(_AliasableParam):
    """Boolean switch"""

    def __init__(
        self,
        *aliases: str,
        default: bool,
        with_opposite: bool = False,
        opposite_prefix: str = "no-",
    ) -> None:
        super().__init__(aliases)
        self.default = default
        self.with_opposite = with_opposite
        self.opposite_prefix = opposite_prefix


class _FlagTrue(_Boolean):
    """True-by-default flag"""

    def __init__(
        self,
        *aliases: str,
        with_opposite: bool = False,
        opposite_prefix: str = "no-",
    ) -> None:
        super().__init__(
            *aliases,
            default=True,
            with_opposite=with_opposite,
            opposite_prefix=opposite_prefix,
        )


class _FlagFalse(_Boolean):
    """False-by-default flag"""

    def __init__(
        self,
        *aliases: str,
        with_opposite: bool = False,
        opposite_prefix: str = "no-",
    ) -> None:
        super().__init__(
            *aliases,
            default=False,
            with_opposite=with_opposite,
            opposite_prefix=opposite_prefix,
        )
