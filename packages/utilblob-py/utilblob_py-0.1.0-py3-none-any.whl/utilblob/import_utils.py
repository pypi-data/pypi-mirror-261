from collections.abc import Callable
from types import ModuleType
import sys
import importlib
import typing


def reload_module[M: ModuleType](m: M, hard: bool = False) -> M:
    return reload_module_by_name(m.__name__, hard=hard)


def reload_module_by_name(name: str, hard: bool = False) -> ModuleType:
    m = importlib.reload(sys.modules[name])

    if hard:
        globals()[name] = m

    return m


def reload_module_of(obj: object, hard: bool = False) -> ModuleType:
    return reload_module_by_name(obj.__module__, hard=hard)


def reload_func(f: Callable, hard: bool = False) -> Callable:
    m = reload_module_of(f, hard=hard)
    return getattr(m, f.__name__)


def reload_func_typed[F: Callable](f: F, hard: bool = False) -> F:
    """Like reload_func, but for better linting. Use with caution!"""
    return typing.cast(F, reload_func(f, hard=hard))
