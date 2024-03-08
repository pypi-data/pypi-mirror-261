from collections.abc import Callable
from functools import partial
from dataclasses import dataclass
from pathlib import Path
import typing

import pandas as pd

PathOrBuffer = str | bytes | Path
SheetId = str | int | list | None


def get_excel_reader(file_extension: str) -> Callable[[PathOrBuffer], pd.DataFrame]:
    """Determines the reader by looking at extension. Could also be done by looking
    at the mimetype, see: https://stackoverflow.com/a/65267285/16371297"""

    match file_extension:
        case "xlsx":
            return partial(pd.read_excel, engine="openpyxl")
        case "xls" | "odf":
            return pd.read_excel
        case "csv":
            return typing.cast(Callable[[PathOrBuffer], pd.DataFrame], pd.read_csv)
        case _:
            raise FileExtensionError(
                got=file_extension, expected=("xlsx", "xls", "odf", "csv")
            )


def read_excel(path: str | Path, *args, **kwargs) -> pd.DataFrame:
    """High-level wrapper for properly handling reading backends"""

    path = Path(path)
    reader = get_excel_reader(_get_file_extension(path))
    return reader(path, *args, **kwargs)


def get_xlsx(path: str | Path, sheet: SheetId = 0) -> pd.DataFrame:
    with pd.ExcelFile(path, engine="openpyxl") as xlsx:
        return typing.cast(pd.DataFrame, pd.read_excel(xlsx, sheet))
    # content = Path(path).read_bytes()
    # result = pd.read_excel(content, sheet, engine="openpyxl")
    #
    # return typing.cast(pd.DataFrame, result)


@dataclass(frozen=True, slots=True)
class FileExtensionError(Exception):
    got: str
    expected: str | tuple[str, ...] | None


def _get_file_extension(path: str | Path) -> str:
    return Path(path).suffix.lower()[1:]
