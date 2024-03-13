#!/usr/bin/env python3
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace
from json import dumps
from re import compile
from sys import argv, stdin, stderr
from textwrap import dedent
from typing import Any, List

from boto3 import client
from yatc import TermColor

from .secretsmanager import get_secrets


SECRETS = client("secretsmanager")
ANSI_RE = compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

stdin_help_string = dedent(
    f"""
    When using stdin, a subset of arguments are taken as lowercase strings matching the long version of argument names and separated by a pipe. You don't actually {TermColor.decorate("have", decorations=["ITALIC", "WHITE"])} to use this argument to use stdin.
    Technically just passing data on stdin is enough.
    Example:\n
    {TermColor.decorate("echo 'myvar | upper | prefix TF_VAR_;' | secrets-env -", ["WHITE", "BOLD"])}\n
    This is the equivalent of passing {TermColor.decorate("-u -p TF_VAR_ myvar", ["WHITE", "BOLD"])} as commandline arguments. {TermColor.decorate("Note the ending '-'.", ["BOLD", "ITALIC", "UNDERLINE"])} Multiple secrets are supported, with each
    one taking its own set of arguments and separated by a semi-colon.
    """
)

main_description_string = dedent(
    """
    Return one or more secrets by either name or pattern, using Unix style glob matching. When using glob style matches then all secret names that
    match the pattern will be returned. When using stdin and specifying options per pattern the options will be applied to the first match whereas multiple secrets
    supplied as positional args will have the options provided as commandline arguments applied to all of them.
    """
)


def parse_args(args: List[Any] = []) -> Namespace:
    parser = ArgumentParser(
        formatter_class=RawTextHelpFormatter, description=main_description_string
    )
    parser.add_argument(
        "-p", "--prefix", type=str, help="Prepend a prefix to each value", default=""
    )
    parser.add_argument(
        "-m",
        "--merge-keys",
        action="store_true",
        help="Merge all secrets into one object. Secrets that are simple strings will have the last segment of their name (characters following the last /) as they key.",
    )
    parser.add_argument("secret", type=str, nargs="+")
    parser.add_argument(
        "--stdin",
        help=f"Read secret options from stdin. See details below for more info.\n{stdin_help_string}\n",
        default=(not stdin.isatty()),
    )
    parser.add_argument("-e", "--env", help="Format output as env vars for a shell to consume", action="store_true")
    casing_group = parser.add_mutually_exclusive_group()
    casing_group.add_argument(
        "-u",
        "--upper",
        action="store_true",
        help="Cast secret names to upper case. Does not apply to prefixes.",
    )
    casing_group.add_argument(
        "-l",
        "--lower",
        action="store_true",
        help="Cast secret names to lower case. Does not apply to prefixes.",
    )

    if args:
        res = parser.parse_args(args)
    else:
        res = parser.parse_args()

    return res


def parse_stdin() -> List[Namespace]:
    """Handles receiving special syntax on stdin for retreiving secrets"""
    arg_groups = []

    # Consume any args supplied through normal CLI args
    if len(argv) > 1:
        base_args = parse_args()

        # Create a separate entry in arg_groups so separate secret positional args
        # are treated the same way as separate entries from stdin
        for secret in base_args.secret:
            cmd = [secret]
            if base_args.upper:
                cmd.append("--upper")
            if base_args.lower:
                cmd.append("--lower")
            if base_args.merge_keys:
                cmd.append("--merge-keys")
            if base_args.prefix:
                cmd += ["--prefix", base_args.prefix]
            if base_args.env:
                cmd.append("--env")
            arg_groups.append(cmd)

    # Trim terminal garbage off of stdin
    stdin_args = [
        ANSI_RE.sub("", x).replace("\n", "").strip().split("|")
        for x in stdin.read().strip().split(";")
    ]

    # Parse each semicolon delimited entry into its own commandline args as if it were its own
    # invocation. --merge-keys will be overwritten by the main commandline inputs.
    for group in stdin_args:
        # When passing a list to `parse_args()` the positional arguments HAVE to come first.
        secret = group.pop(0).strip()
        cmd = [secret]
        if base_args.merge_keys:
            cmd.append("--merge")
        while group:
            next_cmd = group.pop(0).strip()
            if next_cmd.startswith("prefix"):
                cmd += ["--prefix", next_cmd.split(" ")[1]]
            else:
                cmd.append(f"--{next_cmd}")

        arg_groups.append(cmd)

    # Parse all of the inputs and get back regular argparse namespaces
    args = [parse_args(group) for group in arg_groups]
    return args


def main() -> None:
    args = parse_args()
    env = args.env

    if args.stdin:
        args = parse_stdin()

    res = get_secrets(args)

    if not env:
        res = dumps(res, indent=2)

    print(res)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        stderr.write("\rCanceled by user. Exiting.")
        exit(1)
