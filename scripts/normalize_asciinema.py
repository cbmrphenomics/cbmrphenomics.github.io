#!/usr/bin/env python3
# -*- coding: utf8 -*-
# pyright: strict
import argparse
import json
import random
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, TypedDict


class Header(TypedDict):
    version: int
    width: int
    height: int
    timestamp: Optional[int]
    duration: Optional[float]
    idle_time_limit: Optional[float]
    command: Optional[str]
    title: Optional[str]
    env: Optional[Dict[str, str]]


Record = Tuple[float, str, str]


def eprint(*args: Any, **kwargs: Any) -> None:
    kwargs["file"] = sys.stderr
    print(*args, **kwargs)


def read_asciinema_v2(filepath: Path) -> Tuple[Header, List[Record]]:
    with filepath.open() as handle:
        header = json.loads(handle.readline())

        return header, [tuple(json.loads(line)) for line in handle]


def write_asciinema_v2(header: Header, rows: List[Record]) -> str:
    lines = [json.dumps(header)]

    for row in rows:
        lines.append(json.dumps(row))

    return "\n".join(lines)


class HelpFormatter(argparse.ArgumentDefaultsHelpFormatter):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault("width", 79)

        super().__init__(*args, **kwargs)


def normalize_timings(args: argparse.Namespace, records: List[Record]) -> List[Record]:
    timings: Dict[Tuple[str, str], int] = {
        # Setup
        ("?", "a"): 0,
        ("?", "o"): 0,
        # User input
        ("o", "a"): args.after_output,
        ("a", "a"): args.input_rate,
        # Output
        ("o", "o"): 0,
        ("a", "o"): args.before_output,
    }

    offset = 0.0
    last_kind = "?"
    normalized: List[Tuple[float, str, Any]] = []
    for _offset, kind, values in records:
        if kind == "c":
            kind = "a"
        else:
            values = (values,)

        for value in values:
            timing = timings[(last_kind, kind)]
            jitter = random.gauss(0, 1) * args.jitter if kind == "a" else 0
            offset = max(offset, offset + timing + jitter)
            last_kind = kind

            normalized.append((offset / 1000.0, "o" if kind == "a" else kind, value))

    return normalized


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        formatter_class=HelpFormatter,
        description="Normalizes timings in an asciinema JSON file, to produce output "
        "typed at regular intervals (with slight randomness), with regular pauses "
        "inserted between (user) input and terminal output. User input must be marked "
        'by changing "o" to "a" on relevant rows in the JSON file.',
    )
    parser.add_argument(
        "input",
        type=Path,
        help="asciinema v2 file in JSON format",
    )
    parser.add_argument(
        "output",
        nargs="?",
        type=Path,
        help="Output asciinema v2 file in JSON format [defaults: stdout]",
    )
    parser.add_argument(
        "--input-rate",
        metavar="MS",
        type=int,
        default=100,
        help="Rate of user input (milliseconds)",
    )
    parser.add_argument(
        "--before-output",
        metavar="MS",
        type=int,
        default=1500,
        help="Pause after showing output before next input (milliseconds)",
    )
    parser.add_argument(
        "--after-output",
        metavar="MS",
        type=int,
        default=500,
        help="Pause after showing output before next input (milliseconds)",
    )
    parser.add_argument(
        "--jitter",
        metavar="MS",
        type=int,
        default=30,
        help="Mean of normal distribution describing variation in input/output rates",
    )
    parser.add_argument(
        "--gif",
        action="store_true",
        help="Generate GIF using agg (https://github.com/asciinema/agg)",
    )

    return parser.parse_args(argv)


def main(argv: List[str]) -> int:
    args = parse_args(argv)
    eprint("Reading asciinema file", args.input)
    header, records = read_asciinema_v2(args.input)

    if not any(kind == "a" for _, kind, _ in records):
        eprint(
            "No user input in recording. Please edit the second column in rows "
            'representing user input from "o" to "a" (converted to "a" as is) or "c" ('
            "(split into a key-press per character). This allows this script to "
            "normalize timings for key presses, etc."
        )

        return 1

    eprint("Generating updated asciinema file")
    records = normalize_timings(args, records)
    blob = write_asciinema_v2(header, records)

    if args.gif is None:
        if args.output is None:
            print(blob)
        else:
            args.output.write_text(blob)
    else:
        if args.output is None:
            eprint("ERROR: An output file MUST be specified when using --gif")
            return 1
        elif not shutil.which("agg"):
            eprint("ERROR: `agg` not found in PATH")
            return 1

        eprint("Running agg to generate GIF")
        proc = subprocess.Popen(
            ["agg", "--last-frame-duration", "1", "/dev/stdin", args.output],
            stdin=subprocess.PIPE,
        )

        proc.communicate(input=blob.encode())

        return proc.returncode

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
