from collections.abc import Iterable, Iterator
from datetime import datetime
from pathlib import Path
import re
import shutil
import sys

from . import tree
from .type_utils import Predicate as _Predicate


DirPath = FilePath = Path


def normalize_path(p: Path | str) -> Path:
    return Path(p).expanduser().resolve()


if sys.version_info >= (3, 12, 0):

    def walk(
        root_dir: str | Path = ".",
    ) -> Iterator[tuple[DirPath, list[DirPath], list[FilePath]]]:
        for temp_root, dir_names, file_names in normalize_path(root_dir).walk():
            dir_paths = [temp_root / dir_name for dir_name in dir_names]
            file_paths = [temp_root / file_name for file_name in file_names]

            yield temp_root, dir_paths, file_paths
else:
    import os

    def walk(
        root_dir: str | Path = ".",
    ) -> Iterator[tuple[DirPath, list[DirPath], list[FilePath]]]:
        for dir_path, dir_names, file_names in os.walk(root_dir):
            dir_path = Path(dir_path)

            dir_paths = [dir_path / dir_name for dir_name in dir_names]
            file_paths = [dir_path / file_name for file_name in file_names]

            yield dir_path, dir_paths, file_paths


def walk_files(root_dir: str | Path = ".", pattern: str = "") -> Iterator[Path]:
    path = normalize_path(root_dir)

    if pattern:
        yield from path.rglob(pattern)
        return

    for temp_root, _, file_names in path.walk():
        for x in file_names:
            yield Path(temp_root, x)


def walk_dirs(root_dir: str | Path = ".") -> Iterator[Path]:
    for temp_root, dir_names, _ in normalize_path(root_dir).walk():
        for x in dir_names:
            yield Path(temp_root, x)


def walk_all(root_dir: str | Path = ".") -> Iterator[Path]:
    for _, dirs, files in walk(root_dir):
        yield from dirs
        yield from files


def iter_dirs(root_dir: str | Path = ".") -> Iterator[Path]:
    yield from filter(Path.is_dir, normalize_path(root_dir).iterdir())


def iter_files(root_dir: str | Path = ".", extension: str = "") -> Iterator[Path]:
    pred: _Predicate[Path] = (
        (lambda p: p.is_file and p.suffix == f".{extension}")
        if extension
        else Path.is_file
    )

    yield from filter(pred, normalize_path(root_dir).iterdir())


def find(ptn: str | re.Pattern, root_dir: str | Path) -> Iterator[Path]:
    if isinstance(ptn, str):
        ptn = re.compile(ptn)

    for p in walk_all(root_dir):
        if ptn.match(p.name):
            yield p


def mkdir_fresh(path: str | Path) -> Path:
    """If directory exists, removes its child nodes recursively."""
    path = Path(path)
    shutil.rmtree(path, ignore_errors=True)
    path.mkdir(parents=True, exist_ok=True)
    return path


def paths_to_multitree(paths: Iterable[Path]) -> tree.TreeDict[str, str]:
    paths = list(paths)

    result = dict()

    for p in paths:
        tree.assign_multitree_leaf(result, p.parts[:-1], p.parts[-1])

    return result


def timestamped_filename(name: str, suffix: str = "") -> str:
    time_str = datetime.now().strftime(r"%y-%m-%d-%H:%M:%S")
    return f"{name}_{time_str}{suffix}"
