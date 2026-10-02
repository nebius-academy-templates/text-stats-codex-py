"""Turn a list of lines into the report the command-line tool prints.

This is the only module that decides what the output looks like.
"""

import json

from stats import count_blank_lines, count_characters, count_lines, count_words

#: Every statistic the report shows, in the order it shows them, as
#: ``key -> (label, function)``. A new statistic is one line here.
STATISTICS = {
    "lines": ("Lines", count_lines),
    "blank_lines": ("Blank lines", count_blank_lines),
    "words": ("Words", count_words),
    "characters": ("Characters", count_characters),
}


def collect_stats(lines: list[str]) -> dict[str, int]:
    """Run every statistic over ``lines`` and return them by name."""
    return {key: function(lines) for key, (_, function) in STATISTICS.items()}


def format_text(stats: dict[str, int]) -> str:
    """Format collected statistics as an aligned block of text."""
    width = max(len(label) for label, _ in STATISTICS.values())
    rows = [f"{STATISTICS[key][0]:<{width}}  {value}" for key, value in stats.items()]
    return "\n".join(rows)


def format_json(stats: dict[str, int]) -> str:
    """Format collected statistics as JSON, preserving their order."""
    return json.dumps(stats)


def build_report(lines: list[str]) -> str:
    """Collect the statistics for ``lines`` and format them for a terminal."""
    return format_text(collect_stats(lines))
