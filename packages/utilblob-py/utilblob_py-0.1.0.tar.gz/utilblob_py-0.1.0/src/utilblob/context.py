from collections.abc import Callable, Mapping
from contextlib import AbstractContextManager
from dataclasses import dataclass
from functools import partial
from typing import Any, override


@dataclass(frozen=True, init=False, slots=True)
class finalizer[**P](AbstractContextManager):
    f: Callable[P, Any]
    args: tuple
    kwargs: Mapping[str, Any]

    def __init__(self, f: Callable[P, Any], *args: P.args, **kwargs: P.kwargs) -> None:
        # because frozen
        setfield = partial(object.__setattr__, self)

        setfield("f", f)
        setfield("args", args)
        setfield("kwargs", kwargs)

    @override
    def __exit__(self, *_) -> None:
        self.f(*self.args, **self.kwargs)  # type: ignore
