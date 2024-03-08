from collections.abc import Callable
from contextlib import (
    AbstractContextManager,
    ContextDecorator,
    redirect_stderr,
    redirect_stdout,
)
import io
from typing import Self


type Redirector = Callable[[io.StringIO], AbstractContextManager]


class _capture_stream(AbstractContextManager, ContextDecorator):
    def __init__(self, redirect_ctxt_mgr_factory: Redirector) -> None:
        super().__init__()
        self._buff = io.StringIO()
        self._redirect_ctxt_mgr = redirect_ctxt_mgr_factory(self._buff)

    def __enter__(self) -> Self:
        self._redirect_ctxt_mgr.__enter__()
        return self

    def __exit__(self, *_):
        self._redirect_ctxt_mgr.__exit__(*_)
        self._buff.close()

    def __str__(self) -> str:
        oldpos = self._buff.seek(0)
        captured = self._buff.read()
        self._buff.seek(oldpos)
        return captured


class capture_stderr(_capture_stream):
    def __init__(self) -> None:
        super().__init__(redirect_stderr)


class capture_stdout(_capture_stream):
    def __init__(self) -> None:
        super().__init__(redirect_stdout)
