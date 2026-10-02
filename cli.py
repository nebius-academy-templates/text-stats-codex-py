"""Command-line entry point. Runs once, prints a report, and exits."""

import argparse
import sys
import traceback
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


def main(argv: list[str] | None = None) -> None:
    """Read the file named on the command line and print its statistics."""
    args = parse_args(argv)

    try:
        lines = read_lines(Path(args.path))
    except OSError:
        # Dump the whole failure while the tool is still young.
        traceback.print_exc()
        return

    print(build_report(lines))


if __name__ == "__main__":
    sys.exit(main())
