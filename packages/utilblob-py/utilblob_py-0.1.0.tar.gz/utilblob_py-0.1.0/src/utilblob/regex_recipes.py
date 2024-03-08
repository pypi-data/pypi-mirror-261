"""
Regex templates and patterns
"""

from string import Template

NUM_UINT8 = r"(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
"""Number in range 0-255. Leading zeros allowed (max string length == 3)"""

EVEN_CHAR_TPL = Template(r"(?:(?:${c}{2})+)")
"""Placeholder: `c`"""

EVEN_CHAR_STAR_TPL = Template(r"(?:(?:${c}{2})*)")
"""Placeholder: `c`"""

# `{1}` at the end is necessary, because if `c` == '\', then
# the following ')' is escaped in regex
ODD_CHAR_TPL = Template(r"(?:" + EVEN_CHAR_TPL.template + r"*${c}{1})")
"""Placeholder: `c`"""

MOD_N_CHAR_TPL = Template(r"(?:(?:${c}${n})+)")
"""modulo N occurences of CHAR
Placeholder: `c`, `n`
"""

MOD_N_CHAR_STAR_TPL = Template(r"(?:(?:${c}${n})*)")
"""modulo N occurences of CHAR
Placeholder: `c`, `n`
"""

EVEN_BACKSLASH_PTN = EVEN_CHAR_TPL.substitute(c="\\")
EVEN_BACKSLASH_STAR_PTN = EVEN_CHAR_STAR_TPL.substitute(c="\\")
ODD_BACKSLASH_PTN = ODD_CHAR_TPL.substitute(c="\\")

ESCAPED_TPL = Template(r"(?:" + ODD_BACKSLASH_PTN + r"${c}{1})")
"""Placeholder: `c`"""

ESCAPED_SPACE_PTN = ESCAPED_TPL.substitute(c=" ")

SIMPLE_QUOTED_NONGREEDY_TPL = Template(r"(?:${q}[^${q}]*?${q})")
"""Placeholder: `q`"""
SIMPLE_QUOTED_GREEDY_TPL = Template(r"(?:${q}[^${q}]*${q})")
"""Placeholder: `q`"""
SIMPLE_QUOTED_TPL = SIMPLE_QUOTED_NONGREEDY_TPL
"""Placeholder: `q`"""

QUOTED_TPL = Template(r"${q}(?:[^${q}\\]|\\.)*${q}")
"""Placeholder: `q`"""
QUOTED_DBL_PTN = QUOTED_TPL.substitute(q='"')
QUOTED_SGL_PTN = QUOTED_TPL.substitute(q="'")

QUOTED_ANY_PTN = rf"(?:{QUOTED_DBL_PTN}|{QUOTED_SGL_PTN})"
QUOTED_PATH_TPL = Template(
    rf"(?:{QUOTED_DBL_PTN}${{suffix}}|{QUOTED_SGL_PTN}${{suffix}})"
)
"""Placeholder: `suffix`"""

ESCAPED_SPACE_STRING_PTN = rf'(?:(?:[^\s"\']|{ESCAPED_SPACE_PTN})+)'

PATH_SIMPLE_TPL = Template(rf"(?:{ESCAPED_SPACE_STRING_PTN}${{suffix}})")
"""Placeholder: `suffix`"""

# PATH_FAST_PTN = rf'(?:(?:[^ "\']|{ESCAPED_SPACE_PTN})+)'
PATH_ANY_SIMPLE_PTN = PATH_SIMPLE_TPL.substitute(suffix="")
"""Dumber version of PATH, for faster processing"""

PATH_TPL = Template(rf"(?:{PATH_SIMPLE_TPL.template}|{QUOTED_PATH_TPL.template})")
"""File with suffix. Suffix can be discarded bu substituting with ""
Placeholder: `suffix`"""

PATH_ANY_PTN = rf"(?:{PATH_ANY_SIMPLE_PTN}|{QUOTED_ANY_PTN})"

LINE_END_PTN = "rf(?:\n|\r\n)"

CLI_FLAG_SHORT_PTN = r"(?:(?<=\s|^)-[\w\d](?=\s|$))"
CLI_FLAG_LONG_PTN = r"(?:(?<=\s|^)--[\w\d]+(?=\s|$))"
CLI_FLAG_PTN = rf"(?:{CLI_FLAG_SHORT_PTN}|{CLI_FLAG_LONG_PTN})"

CLI_FLAG_ARG_SHORT_PTN = rf"(?:-[\w\d](?:{ESCAPED_SPACE_STRING_PTN}|{QUOTED_ANY_PTN})*)"
CLI_FLAG_ARG_LONG_PTN = (
    rf"(?:(?:+|--)[\w\d-]+[ =](?:{ESCAPED_SPACE_STRING_PTN}|{QUOTED_ANY_PTN})*)"
)
CLI_FLAG_ARG_PTN = rf"(?:{CLI_FLAG_ARG_SHORT_PTN}|{CLI_FLAG_ARG_LONG_PTN})"

CLI_ARG_PTN = rf"(?:(?<=\s|^)(?:{ESCAPED_SPACE_STRING_PTN}|{QUOTED_ANY_PTN})(?=\s|$))"
