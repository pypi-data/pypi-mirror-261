from collections.abc import Iterable, Iterator, Sequence
from dataclasses import dataclass
from enum import StrEnum
from typing import Literal

import more_itertools as mit


TableEntry = str

type Alignment = Literal["<", ">", "^"]
type TableRow = tuple[TableEntry, ...]


def remove_linefeed(s: str) -> str:
    if s.endswith("\r\n"):
        return s[:-2]
    if s.endswith("\n"):
        return s[:-1]

    return s


def align_to_longest(
    lines: Sequence[str], filler: str = " ", alignment: Alignment = "<"
) -> list[str]:
    assert len(filler) == 1
    n = max(map(len, lines or ((),)))
    return [f"{line:{filler}{alignment}{n}}" for line in lines]


class _align_rows:
    @classmethod
    def __call__(cls, *rows: TableRow, filler: str = " ") -> list[TableRow]:
        return cls.fromiter(rows, filler=filler)

    @classmethod
    def fromiter(cls, rows: Iterable[TableRow], filler: str = " ") -> list[TableRow]:
        columns = tuple(zip(*rows, strict=True))
        max_line_lengths = tuple(max(map(len, col)) for col in columns)
        return [
            tuple(
                f"{entry:{filler}<{width}}"
                for entry, width in zip(row, max_line_lengths, strict=True)
            )
            for row in zip(*columns, strict=True)
        ]


align_rows = _align_rows()


def table_from_rows(rows: Iterable[TableRow], sep: str = " ") -> str:
    return "\n".join(sep.join(r) for r in align_rows.fromiter(rows))


def split_camel_case(s: str) -> Iterator[str]:
    yield from map("".join, mit.split_before(s, str.isupper))


class CaseSep(StrEnum):
    SPACE = " "
    CAMEL = ""
    SNAKE = "_"
    UNDERSCORE = SNAKE
    KEBAB = "-"
    DASH = KEBAB


class _to_camel_case:
    def __call__(self, s: str, sep: str | CaseSep = " ") -> str:
        if sep == CaseSep.CAMEL:
            return s

        return self.from_iter(s.split(str(sep)))

    @staticmethod
    def from_iter(words: Iterable[str]) -> str:
        return "".join(map(str.capitalize, words))


@dataclass(frozen=True, slots=True)
class to_interleaved:
    sep: str | CaseSep

    def __call__(self, s: str, sep: str | CaseSep = " ") -> str:
        if sep == self.sep:
            return s

        return self.from_iter(s.split(sep))

    def from_iter(self, words: Iterable[str]) -> str:
        return self.sep.join(words)


class _to_case(to_interleaved):
    def __call__(self, s: str, sep: str | CaseSep = " ") -> str:
        return super()(s, sep).lower()

    def from_iter(self, words: Iterable[str]) -> str:
        return super().from_iter(words).lower()


to_camel_case = _to_camel_case()
to_snake_case = _to_case(CaseSep.SNAKE)
to_kebab_case = _to_case(CaseSep.KEBAB)


def change_case(s: str, sep_in: str | CaseSep, sep_out: str | CaseSep) -> str:
    if sep_in == sep_out:
        return s

    if sep_in == CaseSep.CAMEL:
        words = split_camel_case(s)
    else:
        words = sep_in.split(s)

    if sep_out == CaseSep.CAMEL:
        return to_camel_case.from_iter(words)

    return _to_case(sep_out).from_iter(words)
