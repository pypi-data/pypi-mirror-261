from collections.abc import Callable, Iterator, Sequence
from contextlib import AbstractContextManager, ContextDecorator
from dataclasses import dataclass
from functools import wraps
import logging
import typing
from typing import Any, NoReturn, overload
from typing import Self
import os
import sys
import signal
import shlex
import subprocess

from ..func_utils import decorate as _decorate, DecoratorFactory as _DecoratorFactory
from ..text import remove_linefeed


SimpleLoggerT = Callable[[str], Any]
RetCode = int
SignalCode = int
StackFrame = Any
SigintHandler = Callable[[SignalCode, StackFrame], Any]


LOG_MSG_FMT = "%(message)s"
LOG_DATE_FMT = "[%X]"


def exec_cmd(cmd: str | Sequence[str]) -> RetCode:
    """Runs command as subprocess and returns its exit code"""
    proc = subprocess.run(
        shlex.split(cmd) if isinstance(cmd, str) else cmd,
        stdout=sys.stdout,
        stderr=sys.stderr,
        text=True,
    )

    return proc.returncode


def sys_exec(cmd: str | Sequence[str]) -> NoReturn:
    """Runs command as subprocess and exits with its exit code.
    Consider alternatives: os.exec*"""
    sys.exit(exec_cmd(cmd))


def is_not_flag(arg: str) -> bool:
    return not arg.startswith("-")


@dataclass(frozen=True, slots=True)
class CmdError(Exception):
    cmd: Sequence[str]


class ProcessNotEndedError(CmdError):
    pass


class cmd_iter(Iterator[str]):
    def __init__(self, cmd: str | Sequence[str]):
        self.cmd = shlex.split(cmd) if isinstance(cmd, str) else cmd
        self._returncode = None
        self._stderr_output = ""
        self._cmd_iter = self._init_cmd_iter()

    def check_completed(self) -> bool:
        return self._returncode is not None

    def assert_completed(self) -> None:
        if self.check_completed():
            return

        raise ProcessNotEndedError(self.cmd)

    @property
    def returncode(self):
        self.assert_completed()
        return self._returncode

    @property
    def stderr(self):
        self.assert_completed()
        return self._stderr_output

    def __str__(self) -> str:
        cmd_str = shlex.join(self.cmd)

        if self.check_completed():
            return f"<command completed (status: {self._returncode}): {cmd_str}>"

        return f"<command in progress: {cmd_str}>"

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._cmd_iter)

    def _init_cmd_iter(self):
        try:
            with subprocess.Popen(
                self.cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            ) as p:
                assert p.stdout is not None
                assert p.stderr is not None

                for line in p.stdout:
                    if not self._check_proc(p):
                        self._returncode = p.returncode
                        self._stderr_output = p.stderr.read()
                        return self._returncode
                    yield line.removesuffix("\n").removesuffix("\r")
                else:
                    self._stderr_output = p.stderr.read()

            # must be here, after contextmanager closes
            self._returncode = p.returncode
            return self._returncode
        except CmdError:
            raise
        except Exception as err:
            raise CmdError(self.cmd) from err

    @staticmethod
    def _check_proc(p: subprocess.Popen) -> bool:
        code = p.poll()
        if code is None:
            code = 0

        if code != 0:
            if p.stderr:
                sys.stderr.write(p.stderr.read())

        return code == 0


def exit_and_handle_broken_pipe_error(exit_code: int | None = None):
    # Python flushes standard streams on exit; redirect remaining output
    # to /dev/null to avoid another BrokenPipeError at shutdown
    devnull = os.open(os.devnull, os.O_WRONLY)
    os.dup2(devnull, sys.stdout.fileno())
    sys.exit(exit_code)  # Python exits with error code 1 on EPIPE


class _ignore_broken_pipe_error(AbstractContextManager, ContextDecorator):
    def __exit__(self, __exc_type: type[BaseException] | None, *_) -> bool | None:
        if __exc_type is not None and issubclass(__exc_type, BrokenPipeError):
            exit_and_handle_broken_pipe_error()

    @overload
    def __call__(self, f: None = None) -> Self: ...

    @overload
    def __call__[**P, R](self, f: Callable[P, R]) -> Callable[P, R]: ...

    def __call__(self, f=None):
        if f is None:
            return self
        else:
            return super().__call__(f)


ignore_broken_pipe_error = _ignore_broken_pipe_error()


def _exit_and_handle_sigint_factory(
    exit_code: int | None, logger: SimpleLoggerT = print
) -> SigintHandler:
    def _exit_and_handle_sigint(sig: SignalCode, _: StackFrame) -> NoReturn:
        logger("Cancelled by user")
        sys.exit(sig if exit_code is None else exit_code)

    return _exit_and_handle_sigint


def graceful_sigint[**P, R](
    f: Callable[P, R],
    sigint_handler: SigintHandler | None = None,
    exit_code: int = signal.SIGINT,
) -> Callable[P, R]:
    @wraps(f)
    def _graceful_sigint_decorator(*args: P.args, **kwargs: P.kwargs) -> R:
        prev_handler = signal.signal(
            signal.SIGINT, sigint_handler or _exit_and_handle_sigint_factory(exit_code)
        )
        result = f(*args, **kwargs)
        # restore previous signal handler
        signal.signal(signal.SIGINT, prev_handler)
        return result

    return _graceful_sigint_decorator


def interactive_entrypoint[**P, R](f: Callable[P, R]) -> Callable[P, R]:
    return typing.cast(
        Callable[P, R],
        _decorate(
            f,
            graceful_sigint,
            typing.cast(_DecoratorFactory[P, R], ignore_broken_pipe_error),
        ),
    )


def piped_input() -> Iterator[str]:
    yield from map(remove_linefeed, iter(sys.stdin.readline, ""))


def _config_rich_logging() -> None:
    from rich.logging import RichHandler

    logging.basicConfig(
        level=logging.WARNING,
        format=LOG_MSG_FMT,
        datefmt=LOG_DATE_FMT,
        handlers=[RichHandler()],
    )


@overload
def config_rich_logging() -> None: ...


@overload
def config_rich_logging[**P, R](f: Callable[P, R], /) -> Callable[P, R]: ...


def config_rich_logging[**P, R](
    f: Callable[P, R] | None = None, /
) -> Callable[P, R] | None:
    if f is None:
        _config_rich_logging()
        return

    @wraps(f)
    def _decorator_err_logging(*args: P.args, **kwargs: P.kwargs) -> R:
        _config_rich_logging()
        return f(*args, **kwargs)

    return _decorator_err_logging


def log_errors[**P, R](f: Callable[P, R]) -> Callable[P, R]:
    @wraps(f)
    def _decorator(*args: P.args, **kwargs: P.kwargs) -> R:
        try:
            return f(*args, **kwargs)
        except Exception as e:
            logger = logging.getLogger()
            logger.error(e)
            raise

    return _decorator
