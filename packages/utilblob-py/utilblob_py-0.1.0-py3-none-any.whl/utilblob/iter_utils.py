from collections.abc import Callable, Hashable, Iterable, Iterator, Sequence
import copy as _copy
import itertools as it
import operator as op
import typing
from typing import overload

from .type_utils import (
    Comparator,
    LeT,
    Predicate,
    Pair,
    Quadruple,
    Quintuple,
    Septuple,
    Sextuple,
    Triple,
)


_LabelInt = int

type _LabeledInt[T] = tuple[_LabelInt, T]
type _Dispatcher[T] = Iterator[_LabeledInt[T]]


class EmptyIterableError(Exception):
    """Raised when iterable is expected to yield at least one element"""


def _identity[T](x: T) -> T:
    return x


def before_and_after[T](
    values: Iterable[T], pred: Predicate[T], keep: bool = False
) -> tuple[list[T], Iterable[T]]:
    """keep - whether to keep the element for which `pred` is `True` in 'after'.
    Consider more_itertools.before_and_after."""
    left = []

    # without wrapping with iter, collections e.g. lists would be
    # just iterated and returned without skipping
    values = iter(values)

    for x in values:
        if pred(x):
            if keep:
                values = it.chain((x,), values)  # reinsert the element into iterator
            break

        left.append(x)

    return left, values


@overload
def partition_n[T](values: Iterable[T], p: Predicate[T], /) -> Pair[Iterator[T]]: ...


@overload
def partition_n[T](
    values: Iterable[T], p1: Predicate[T], p2: Predicate[T], /
) -> Triple[Iterator[T]]: ...


@overload
def partition_n[T](
    values: Iterable[T], p1: Predicate[T], p2: Predicate[T], p3: Predicate[T], /
) -> Quadruple[Iterator[T]]: ...


@overload
def partition_n[T](
    values: Iterable[T],
    p1: Predicate[T],
    p2: Predicate[T],
    p3: Predicate[T],
    p4: Predicate[T],
    /,
) -> Quintuple[Iterator[T]]: ...


@overload
def partition_n[T](
    values: Iterable[T],
    p1: Predicate[T],
    p2: Predicate[T],
    p3: Predicate[T],
    p4: Predicate[T],
    p5: Predicate[T],
    /,
) -> Sextuple[Iterator[T]]: ...


@overload
def partition_n[T](
    values: Iterable[T],
    p1: Predicate[T],
    p2: Predicate[T],
    p3: Predicate[T],
    p4: Predicate[T],
    p5: Predicate[T],
    p6: Predicate[T],
    /,
) -> Septuple[Iterator[T]]: ...


@overload
def partition_n[T](
    values: Iterable[T], *predicates: Predicate[T]
) -> tuple[Iterator[T], ...]: ...


def partition_n[T](
    values: Iterable[T], *predicates: Predicate[T]
) -> tuple[Iterator[T], ...]:
    """
    Returns
    -------
    tuple of n+1 iterators, where n is the number of predicates. Each iterator has
    values for which the corresponding predicate returns True. The last iterator
    contains elements that did not match any of predicates.
    """
    n = len(predicates)
    residue_iter_idx = n

    def _partition_n_dispatcher() -> _Dispatcher[T]:
        for x in iter(values):
            for iter_idx, pred in enumerate(predicates):
                if pred(x):
                    yield iter_idx, x
                    break
            else:
                yield residue_iter_idx, x

    def _checker_factory(expected_label: _LabelInt) -> Predicate[_LabeledInt[T]]:
        def _checker(item: _LabeledInt[T]) -> bool:
            label, _ = item
            return expected_label == label

        return _checker

    dispatchers = it.tee(_partition_n_dispatcher(), n + 1)
    discard_idx = op.itemgetter(1)

    def _partition(label: int, dispatcher: _Dispatcher[T]) -> Iterator[T]:
        return map(discard_idx, filter(_checker_factory(label), dispatcher))

    return tuple(
        _partition(label, dispatcher) for label, dispatcher in enumerate(dispatchers)
    )


def partition_n_eager[T](
    values: Iterable[T], *predicates: Predicate[T]
) -> tuple[list[T]]:
    partitions = tuple[list[T]]([] for _ in range(len(predicates) + 1))

    for x in values:
        for partition_idx, pred in enumerate(predicates):
            if pred(x):
                partitions[partition_idx].append(x)
                break
        else:
            partitions[-1].append(x)

    return partitions


@overload
def groupby_eager[T](
    values: Iterable[T], key: None = None
) -> tuple[list[T], list[list[T]]]: ...


@overload
def groupby_eager[T, Label](
    values: Iterable[T], key: Callable[[T], Label]
) -> tuple[list[Label], list[list[T]]]: ...


def groupby_eager[T, Label](  # type: ignore
    values: Iterable[T], key: Callable[[T], Label] | None = None
) -> tuple[list[Label | T], list[list[T]]]:
    labels: list[Label | T] = []
    groups: list[list[T]] = []

    for label, g in it.groupby(values, key=key):
        labels.append(label)
        groups.append(list(g))

    return labels, groups


@overload
def groupby_dict[T: Hashable](
    values: Iterable[T], key: None = None
) -> dict[T, list[T]]: ...


@overload
def groupby_dict[T, K: Hashable](
    values: Iterable[T], key: Callable[[T], K]
) -> dict[K, list[T]]: ...


def groupby_dict[T, K: Hashable](
    values: Iterable[T], key: Callable[[T], K] | None = None
) -> dict[K, list[T]]:
    result: dict[K | T, list[T]] = {}

    for k, vs in it.groupby(values, key=key):
        result[k] = list(vs)

    return typing.cast(dict[K, list[T]], result)


def current_and_tail[T](seq: Sequence[T]) -> Iterator[tuple[T, list[T]]]:
    for i, x in enumerate(seq):
        yield x, list(seq[i + 1 :])


def _resolve_copier[T](copy: bool, deep: bool) -> Callable[[T], T]:
    if copy:
        if deep:
            return _copy.deepcopy
        else:
            # shallow copy of prevs
            return _copy.copy
    else:
        return _identity


def current_and_prevs[T](
    values: Iterable[T], copy: bool = True, deep: bool = False
) -> Iterator[tuple[T, list[T]]]:
    prevs: list[T] = []
    copier = _resolve_copier(copy, deep)

    for x in values:
        yield x, copier(prevs)
        prevs.append(x)


def prevs_cur_tail[T](
    values: Sequence[T], copy: bool = True, deep: bool = False
) -> Iterator[tuple[list[T], T, list[T]]]:
    if len(values) == 0:
        return

    prevs: list[T] = []
    cur, tail = values[0], list(values[1:])

    copier = _resolve_copier(copy, deep)

    for x in tail:
        yield copier(prevs), cur, copier(tail)
        prevs.append(x)
        del tail[0]


def all_eq(values: Iterable) -> bool:
    ivalues = iter(values)
    nothing = object()

    if (v := next(ivalues, nothing)) is nothing:
        return True

    for v2 in ivalues:
        if v != v2:
            return False
        v = v2

    return True


@overload
def zip_sorted2(s1: Iterable[LeT], s2: Iterable[LeT]) -> Iterator[LeT]: ...


@overload
def zip_sorted2[T](
    s1: Iterable[T], s2: Iterable[T], key: Comparator
) -> Iterator[T]: ...


def zip_sorted2[T](
    s1: Iterable[T], s2: Iterable[T], key: Comparator[T] = op.le
) -> Iterator[T]:
    is1 = iter(s1)
    is2 = iter(s2)

    if (x := next(is1, None)) is None:
        yield from is2
        return
    if (y := next(is2, None)) is None:
        yield x
        yield from is1
        return

    while True:
        if key(x, y):
            yield x
            x = next(is1, None)
        else:
            yield y
            y = next(is2, None)
        if x is None:
            if y is None:
                return
            yield y
            yield from is2
            return
        elif y is None:
            if x is None:
                return
            yield x
            yield from is1
            return


def minmax[T](it: Iterable[T], key: Comparator[T] = op.lt) -> tuple[T, T]:
    it = iter(it)

    if (minval := next(it, None)) is None:
        raise EmptyIterableError

    maxval = minval

    for x in it:
        if key(x, minval):
            minval = x
        if not key(x, maxval):
            maxval = x

    return (minval, maxval)


def filter_cls[T](cls: type[T] | tuple[type[T], ...], values: Iterable) -> Iterator[T]:
    yield from filter(lambda x: isinstance(x, cls), values)
