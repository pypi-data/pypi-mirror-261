from collections.abc import Callable
from functools import wraps


def print_inout[R, **P](f: Callable[P, R]) -> Callable[P, R]:
    @wraps(f)
    def d(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"DEBUG called {f=}, {args=}, {kwargs=}")
        r = f(*args, **kwargs)
        print(f"DEBUG returning {f=}, {r=}")
        return r

    return d
