import stats
from document import Document

LINES = [
    "the quick brown fox",
    "",
    "jumps over the lazy dog",
]
DOCUMENT = Document(text="\n".join(LINES), lines=tuple(LINES))


def make_document(lines):
    return Document(text="\n".join(lines), lines=tuple(lines))


def test_count_lines_includes_blank_lines():
    assert stats.count_lines(DOCUMENT) == 3


def test_count_lines_of_no_lines_is_zero():
    assert stats.count_lines(make_document([])) == 0


def test_count_blank_lines_counts_whitespace_only_lines():
    assert stats.count_blank_lines(DOCUMENT) == 1
    assert stats.count_blank_lines(make_document(["   ", "\t"])) == 2


def test_count_characters_excludes_line_breaks():
    assert stats.count_characters(DOCUMENT) == 42


def test_count_words_splits_on_whitespace():
    assert stats.count_words(DOCUMENT) == 9


def test_count_words_keeps_punctuation_attached():
    assert stats.count_words(make_document(["don't stop, he said."])) == 4
