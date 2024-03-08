from collections.abc import Callable, Sequence
from contextlib import ContextDecorator
from dataclasses import dataclass
from pathlib import Path
import sys
from types import TracebackType
import typing
from typing import Any, Mapping, NoReturn, Self

import rich.console

from ._core import resolve_one_or_more
from .type_utils import OneOrMore, is_subtype, typechecker_factory


type _Lazy[T] = Callable[[], T]


@dataclass(frozen=True, slots=True)
class pretty_err_printing[Err: Exception](ContextDecorator):
    suppress: OneOrMore[type[Err]] = typing.cast(type[Err], BrokenPipeError)
    terminate: bool = False
    exit_code: int = 1

    def __enter__(self):
        pass

    def __exit__(self, exc_type: type[Exception], *_):
        if exc_type is not None:
            if issubclass(exc_type, BrokenPipeError):
                return True

            self._pretty_print_current_exception()

            if self.terminate:
                sys.exit(self.exit_code)

            return self._is_expected(exc_type)

    @staticmethod
    def _pretty_print_current_exception() -> None:
        console = rich.console.Console()
        console.print_exception()

    def _is_expected(self, exc_type: type[Exception]) -> bool:
        return issubclass(exc_type, self.suppress)


@dataclass(frozen=True, slots=True)
class reraise_as[Err: Exception](ContextDecorator):
    """Contextmanager and decorator"""

    err_t: _Lazy[Err]
    expected_err_types: OneOrMore[type[Err]] = typing.cast(type[Err], Exception)
    err_args: Sequence[Any] = ()
    err_kwargs: Mapping[str, Any] | None = None
    excluded: OneOrMore[type[Err]] = ()
    exclude_expected_subclasses = True

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        _exc_type: type[Exception] | None,
        exc_val: Exception | None,
        _exc_tb: TracebackType | None,
    ) -> None:
        del _exc_type, _exc_tb  # for linters

        if exc_val is None:
            return

        if self.__is_expected(exc_val):
            self.__reraise(reason=exc_val)

    def __is_expected(self, err: Exception) -> bool:
        return is_expected(
            err,
            self.expected_err_types,
            self.excluded,
            self.exclude_expected_subclasses,
        )

    def __reraise(self, reason: Exception) -> NoReturn:
        raise self.__build_err() from reason

    def __build_err(self) -> Err:
        return self.err_t(*self.err_args, **(self.err_kwargs or {}))


def is_expected(
    err: Exception,
    expected: OneOrMore[type[BaseException]],
    excluded: OneOrMore[type[BaseException]] = (),
    exclude_expected_subclasses: bool = True,
) -> bool:
    expected = resolve_one_or_more(expected)
    excluded = resolve_one_or_more(excluded)

    naive_is_expected = typechecker_factory(*expected)
    naive_is_excluded = typechecker_factory(*excluded) if excluded else lambda _: False

    return naive_is_expected(err) and not (
        (exclude_expected_subclasses and is_subtype(err, *expected))
        or naive_is_excluded(err)
    )


@dataclass(frozen=True, slots=True, unsafe_hash=True)
class DirNotFoundError(FileNotFoundError):
    path: str | Path
