from collections.abc import Callable, Collection, Hashable
from enum import Enum, Flag
from typing import Any, Protocol, TypeGuard, TypeVar, overload, runtime_checkable


type Many[T] = tuple[T, ...]
type OneOrMore[T] = T | Many[T]

type Pair[T] = tuple[T, T]
type Triple[T] = tuple[T, T, T]
type Quadruple[T] = tuple[T, T, T, T]
type Quintuple[T] = tuple[T, T, T, T, T]
type Sextuple[T] = tuple[T, T, T, T, T, T]
type Septuple[T] = tuple[T, T, T, T, T, T, T]
type Octuple[T] = tuple[T, T, T, T, T, T, T, T]
type Nontuple[T] = tuple[T, T, T, T, T, T, T, T, T]

type TypeChecker[T] = Callable[[object], TypeGuard[T]]
type TypeCheckerMulti = Callable[[object], bool]

type InstanceOrType[T] = T | type[T]

type Comparator[T] = Callable[[T, T], bool]
type Comparator2[T1, T2] = Callable[[T1, T2], bool]
type Predicate[T] = Callable[[T], bool]

type Endomorphism[T] = Callable[[T], T]
type UnOp[T, R] = Callable[[T], R]
type BinOp[T1, T2, R] = Callable[[T1, T2], R]
type BinOpEndo[T] = BinOp[T, T, T]

type Lazy[T] = Callable[[], T]

T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)
T_ct = TypeVar("T_ct", contravariant=True)

ErrT = TypeVar("ErrT", bound=Exception)
ErrT_co = TypeVar("ErrT_co", bound=Exception, covariant=True)
ErrT_ct = TypeVar("ErrT_ct", bound=Exception, contravariant=True)

HashableT = TypeVar("HashableT", bound=Hashable)
HashableT_co = TypeVar("HashableT_co", bound=Hashable, covariant=True)
HashableT_ct = TypeVar("HashableT_ct", bound=Hashable, contravariant=True)

EnumT = TypeVar("EnumT", bound=Enum)
FlagT = TypeVar("FlagT", bound=Flag)


@runtime_checkable
class ComparableLE[T](Protocol):
    def __le__(self, __other: T) -> bool: ...


@runtime_checkable
class ComparableLT[T](Protocol):
    def __lt__(self, __other: T) -> bool: ...


@runtime_checkable
class ComparableGE[T](Protocol):
    def __ge__(self, __other: T) -> bool: ...


@runtime_checkable
class ComparableGT[T](Protocol):
    def __gt__(self, __other: T) -> bool: ...


@runtime_checkable
class ComparableEq(Protocol):
    def __eq__(self, __other: object) -> bool: ...


@runtime_checkable
class ComparableNE(Protocol):
    def __ne__(self, __other: object) -> bool: ...


@runtime_checkable
class ComparableWeak(ComparableLT, ComparableGT, Protocol): ...


@runtime_checkable
class ComparableStrong(ComparableLE, ComparableGE, Protocol): ...


@runtime_checkable
class ComparableEquality(ComparableEq, ComparableNE, Protocol): ...


@runtime_checkable
class Comparable(
    ComparableWeak,
    ComparableStrong,
    ComparableEquality,
    Protocol,
): ...


LeT = TypeVar("LeT", bound=ComparableLE)
LtT = TypeVar("LtT", bound=ComparableLT)
GtT = TypeVar("GtT", bound=ComparableGT)
GeT = TypeVar("GeT", bound=ComparableGE)
EqT = TypeVar("EqT", bound=ComparableEq)
NeT = TypeVar("NeT", bound=ComparableNE)

CmpT = TypeVar("CmpT", bound=Comparable)


@runtime_checkable
class Indexable[Idx: Hashable, R](Protocol):
    def __getitem__(self, __idx: Idx) -> R: ...


@runtime_checkable
class Appendable(Protocol[T_ct]):
    def append(self, __x: T_ct) -> Any: ...


@runtime_checkable
class AppendableCollection[T](Collection, Appendable[T], Protocol): ...


class DecoratorFactory[**P, R](Protocol):
    def __call__(self, __f: Callable[P, R]) -> Callable[P, R]: ...


def resolve_cls[T](type_or_instance: T | type[T]) -> type[T]:
    """Resolves type from its instance or the type itself"""
    return (
        type_or_instance
        if isinstance(type_or_instance, type)
        else type(type_or_instance)
    )


@overload
def typechecker_factory[T](expected_type: type[T], /) -> TypeChecker[T]: ...


@overload
def typechecker_factory(
    expected_type1: type, expected_type2: type, /, *expected_types: type
) -> TypeCheckerMulti: ...


def typechecker_factory(
    expected_type: type, /, *expected_types: type
) -> TypeCheckerMulti:
    expected_types = (expected_type, *expected_types)

    def typechecker(x: object, /) -> bool:
        return isinstance(x, expected_types)

    return typechecker


def is_expected_type(
    cls: type,
    expected_type: type,
    *expected_types: type,
) -> bool:
    """Compares classes with `is` operator"""
    expected_types = (expected_type, *expected_types)
    return any(cls is other for other in expected_types)


def is_subtype(
    type_or_instance: InstanceOrType, expected_type: type, *expected_types: type
) -> bool:
    """Strict version of isinstance and issubclass - object must be a strict subclass"""
    cls = resolve_cls(type_or_instance)
    expected_types = (expected_type, *expected_types)

    return issubclass(cls, expected_types) and not is_expected_type(
        cls, *expected_types
    )


def instantiate[T](f: Lazy[T]) -> T:
    """
    For example to replace private classes that exist only to create one object
    (e.g. when defining ContextDecorator to avoid always using with dec() syntax - unnecessary parentheses)"""
    return f()
