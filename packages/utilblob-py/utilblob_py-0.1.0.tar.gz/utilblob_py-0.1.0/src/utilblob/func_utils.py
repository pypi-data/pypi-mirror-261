from collections.abc import Callable
from functools import wraps

from .type_utils import DecoratorFactory


def cond_keyword[T](name: str, val: T, pred: bool) -> dict[str, T]:
    return {name: val} if pred else {}


def cond_arg[T](val: T, pred: bool) -> tuple[T] | tuple[()]:
    return (val,) if pred else ()


def decorate[**P, R](
    f: Callable[P, R],
    decorator: DecoratorFactory[P, R],
    *decorators: DecoratorFactory[P, R],
) -> Callable[P, R]:
    orig_f = f

    f = decorator(f)

    for d in decorators:
        f = d(f)

    return wraps(orig_f)(f)
