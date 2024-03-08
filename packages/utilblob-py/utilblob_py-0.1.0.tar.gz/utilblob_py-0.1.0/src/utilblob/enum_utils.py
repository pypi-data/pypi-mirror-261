from collections.abc import Iterator
from enum import Flag
import itertools
from typing import Self

from .numeric_utils import is_power_of_2

type _Pair[T] = tuple[T, T]

type FlagTree[F: Flag] = dict[F, list[F]]


def is_flag_primitive(f: Flag) -> bool:
    return is_power_of_2(f.value)


def idistinct_flags[F: Flag](flag_enum: type[F]) -> Iterator[F]:
    yield from filter(is_flag_primitive, flag_enum)


def distinct_flags[F: Flag](flag_enum: type[F]) -> list[F]:
    return list(idistinct_flags(flag_enum))


def decompose_flag[F: Flag](flag: F) -> list[F]:
    return [
        primitive
        for primitive in distinct_flags(type(flag))
        if primitive.value & flag.value
    ]


def partition_flag[F: Flag](flag_enum: type[F]) -> _Pair[list[F]]:
    """
    Partition flag enum into primitive and merged flags
    Returns
    -------
    (primitive flags iter, merged flags iter)"""

    groups = itertools.groupby(flag_enum, is_flag_primitive)

    # list[Iterator[F]]
    partitions: list = [None, None]

    for k, p in groups:
        partitions[k] = p

    primitives = partitions[True]  # partitions that are primitive
    merged = partitions[False]  # non-primitive

    return list(primitives), list(merged)


def flag_tree[F: Flag](flag_enum: type[F]) -> FlagTree[F]:
    primitives, multiflags = partition_flag(flag_enum)

    tree: FlagTree = {p: [] for p in primitives}

    for f in multiflags:
        superflag = next(p for p in primitives if f in p)
        tree[superflag].append(f)

    return tree


class DistinctFlag(Flag):
    @classmethod
    def distinct(cls) -> list[Self]:
        return distinct_flags(cls)

    def decompose(self) -> list[Self]:
        return decompose_flag(self)
