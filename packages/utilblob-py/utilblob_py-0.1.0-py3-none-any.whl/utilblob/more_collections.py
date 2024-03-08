from collections.abc import Callable, Collection, Hashable, Iterable, Iterator, Mapping
import itertools as it
import typing
from typing import Self, overload
import sys


class FrozenDict[K: Hashable, V](Mapping[K, V]):
    """Immutable dictionary

    Based on: https://stackoverflow.com/a/2704866/16371297
    """

    __slots__ = ("__wrapped_dict", "_hash")

    dict.fromkeys

    @overload
    @classmethod
    def fromkeys(
        cls, __iterable: Iterable[K], __value: None = None
    ) -> "FrozenDict[K, None]": ...

    @overload
    @classmethod
    def fromkeys(cls, __iterable: Iterable[K], __value: V) -> "FrozenDict[K, V]": ...

    @classmethod
    def fromkeys(  # type: ignore
        cls, __iterable: Iterable[K], __value: V | None = None
    ) -> "FrozenDict[K, V | None]":
        instance = FrozenDict[K, V]()
        instance.__wrapped_dict = dict.fromkeys(__iterable, __value)

        return typing.cast("FrozenDict", instance)

    def __init__(
        self, *args: Mapping[K, V] | Iterable[tuple[K, V]], **kwargs: V
    ) -> None:
        self.__wrapped_dict = dict[K, V](*args, **kwargs)

    def copy(self) -> Self:
        return type(self)(self.__wrapped_dict.copy())

    def __iter__(self) -> Iterator[K]:
        return iter(self.__wrapped_dict)

    def __len__(self) -> int:
        return len(self.__wrapped_dict)

    def __getitem__(self, key) -> V:
        return self.__wrapped_dict[key]

    if sys.version_info.minor < 7:

        def __hash__(self) -> int:
            # It would have been simpler and maybe more obvious to
            # use hash(tuple(sorted(self._d.iteritems()))) from this discussion
            # so far, but this solution is O(n). I don't know what kind of
            # n we are going to run into, but sometimes it's hard to resist the
            # urge to optimize when it will gain improved algorithmic performance.
            if getattr(self, "_hash", None) is None:
                hash_ = 0
                for pair in self.items():
                    hash_ ^= hash(pair)
                self._hash = hash_
            return self._hash

    else:

        def __hash__(self) -> int:
            return hash(tuple(self.__wrapped_dict.items()))


def mapping_and[K1: Hashable, V1, K2: Hashable, V2](
    left: Mapping[K1, V1], right: Mapping[K2, V2]
) -> dict[K2, V2]:
    return {k: v for k, v in right.items() if k in left}


def filter_keys[K: Hashable, V](
    m: Mapping[K, V], pred: Callable[[K], bool]
) -> dict[K, V]:
    return {k: v for k, v in m.items() if pred(k)}


def blacklist_keys[K: Hashable, V](m: Mapping[K, V], keys: Collection[K]) -> dict[K, V]:
    return filter_keys(m, lambda k: k not in keys)


def swap[L, R](x: L, y: R) -> tuple[R, L]:
    return y, x


def invert_mapping[T1: Hashable, T2: Hashable](m: Mapping[T1, T2]) -> dict[T2, T1]:
    return dict(it.starmap(swap, m.items()))  # type: ignore
