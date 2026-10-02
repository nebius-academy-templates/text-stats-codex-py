"""Turn a document into the report the command-line tool prints.

This is the only module that decides what the output looks like.
"""

from document import Document
from stats import count_blank_lines, count_characters, count_lines, count_words

#: Every statistic the report shows, in the order it shows them, as
#: ``key -> (label, function)``. A new statistic is one line here.
STATISTICS = {
    "lines": ("Lines", count_lines),
    "blank_lines": ("Blank lines", count_blank_lines),
    "words": ("Words", count_words),
    "characters": ("Characters", count_characters),
}


def collect_stats(document: Document) -> dict[str, int]:
    """Run every statistic over ``document`` and return them by name."""
    return {
        key: function(document) for key, (_, function) in STATISTICS.items()
    }


def format_text(stats: dict[str, int]) -> str:
    """Format collected statistics as an aligned block of text."""
    width = max(len(label) for label, _ in STATISTICS.values())
    rows = [f"{STATISTICS[key][0]:<{width}}  {value}" for key, value in stats.items()]
    return "\n".join(rows)


def build_report(document: Document) -> str:
    """Collect statistics for ``document`` and format them for a terminal."""
    return format_text(collect_stats(document))
