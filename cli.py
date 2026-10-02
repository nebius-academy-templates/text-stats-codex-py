"""Command-line entry point. Runs once, prints a report, and exits."""

import argparse
import sys
from pathlib import Path

from io_utils import read_lines
from report import build_report


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse the command line."""
    parser = argparse.ArgumentParser(
        prog="text-stats",
        description="Report statistics about a text file.",
    )
    parser.add_argument("path", help="path to the text file to analyse")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Read the file named on the command line and print its statistics."""
    args = parse_args(argv)

    try:
        lines = read_lines(Path(args.path))
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(build_report(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
