"""Statistics over a list of lines.

Every function here is pure: it takes the lines it is given and returns a
number. Nothing in this module opens a file.
"""


def count_lines(lines: list[str]) -> int:
    """Count every line, blank ones included."""
    return len(lines)


def count_blank_lines(lines: list[str]) -> int:
    """Count lines that are empty or contain nothing but whitespace."""
    return sum(1 for line in lines if not line.strip())


def count_characters(lines: list[str]) -> int:
    """Count the characters in the text, not counting the line breaks."""
    return sum(len(line) for line in lines)


def longest_line_length(lines: list[str]) -> int:
    """Return the length of the longest line, excluding its line break."""
    return max((len(line.rstrip("\r\n")) for line in lines), default=0)


def count_words(lines: list[str]) -> int:
    """Count words, where a word is whatever whitespace separates.

    Punctuation stays attached to the token beside it, so ``"don't"`` is
    one word and ``"stop."`` keeps its full stop.
    """
    return sum(len(line.split()) for line in lines)
