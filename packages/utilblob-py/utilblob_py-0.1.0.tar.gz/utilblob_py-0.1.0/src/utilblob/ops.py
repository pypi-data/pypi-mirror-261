from collections.abc import Callable
import operator
from typing import TypeVar


_N = TypeVar("_N", int, float)

type _NoOpT[T] = Callable[..., T]
type _Predicate[T] = Callable[[T], bool]


def noop(*_, **__):
    del _, __
    return


def noop_factory[T](sentinel: T = None) -> _NoOpT[T]:
    def _noop(*_, **__) -> T:
        del _, __
        return sentinel

    return _noop


first = operator.itemgetter(0)
second = operator.itemgetter(1)


def str_startswith(prefix: str) -> _Predicate[str]:
    def _op_str_startswith(s: str) -> bool:
        return s.startswith(prefix)

    return _op_str_startswith


def decr(v: _N) -> _N:
    return v - 1


def incr(v: _N) -> _N:
    return v + 1


def passthrough[T](v: T) -> T:
    return v
