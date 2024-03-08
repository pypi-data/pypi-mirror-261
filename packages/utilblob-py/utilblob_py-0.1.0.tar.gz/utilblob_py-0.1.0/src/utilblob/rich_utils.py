import typing
from typing import Literal


RichTermColor = Literal["auto", "standard", "256", "truecolor", "windows"]
MoreTermColor = Literal["none", "force"]
TermColor = RichTermColor | MoreTermColor

TERM_COLORS = typing.get_args(RichTermColor) + typing.get_args(MoreTermColor)


def parse_term_color(c: TermColor | None) -> RichTermColor | None:
    match c:
        case "none" | None:
            return None
        case "force":
            return "truecolor"
        case _:
            return c
