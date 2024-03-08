#!/usr/bin/env python3
from argparse import ArgumentParser
from collections.abc import Iterable
import sys

import rich
import rich.console

from .cli import cmd_iter, interactive_entrypoint, piped_input
from .err import pretty_err_printing
from .iter_utils import before_and_after


def parse_argv():
    args = sys.argv[1:]
    if "--" not in args:
        if args and args[0].startswith("-"):
            flags = args
            wrapped_cmd = ()
        else:
            flags = ()
            wrapped_cmd = args
    else:
        flags, wrapped_cmd = before_and_after(args, lambda s: s == "--")
        wrapped_cmd = tuple(wrapped_cmd)

    parser = ArgumentParser()
    parser.add_argument(
        "-t", "--title", type=str, help="default: wrapped command name or 'In progress'"
    )
    args = parser.parse_args(flags)

    if not args.title:
        if wrapped_cmd:
            args.title = wrapped_cmd[0]
        else:
            args.title = "In progress"

    return args, wrapped_cmd


def wrap_output_lines(
    lines: Iterable[str] | cmd_iter, title: str, style: str = "bold green"
):
    console = rich.console.Console()

    with console.status(f"[{style}]{title}...[/]", spinner="dots") as status:
        status.update(rf"[bold gray]\[{title} - waiting for input...][/]")
        for line in lines:
            status.update(rf"[{style}]\[{title}]:[/] {line}")

    if isinstance(lines, cmd_iter) and lines.returncode:
        cmd = " ".join(lines.cmd)
        console.print(rf"[bold red]\[ERROR {lines.returncode}]:[/] {cmd}")
        sys.exit(lines.returncode)


@pretty_err_printing(terminate=True)
@interactive_entrypoint
def main():
    args, wrapped_cmd = parse_argv()

    if wrapped_cmd:
        lines = cmd_iter(wrapped_cmd)
    else:
        lines = piped_input()

    wrap_output_lines(lines, args.title)


if __name__ == "__main__":
    main()
