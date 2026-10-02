import stats

LINES = [
    "the quick brown fox",
    "",
    "jumps over the lazy dog",
]


def test_count_lines_includes_blank_lines():
    assert stats.count_lines(LINES) == 3


def test_count_lines_of_no_lines_is_zero():
    assert stats.count_lines([]) == 0


def test_count_blank_lines_counts_whitespace_only_lines():
    assert stats.count_blank_lines(LINES) == 1
    assert stats.count_blank_lines(["   ", "\t"]) == 2


def test_count_characters_excludes_line_breaks():
    assert stats.count_characters(LINES) == 42


def test_longest_line_length_counts_characters_in_longest_line():
    assert stats.longest_line_length(LINES) == 23


def test_longest_line_length_counts_whitespace_but_not_line_breaks():
    assert stats.longest_line_length([" a \n", "\t\t\r\n"]) == 3


def test_longest_line_length_of_no_lines_is_zero():
    assert stats.longest_line_length([]) == 0


def test_count_words_splits_on_whitespace():
    assert stats.count_words(LINES) == 9


def test_count_words_keeps_punctuation_attached():
    assert stats.count_words(["don't stop, he said."]) == 4
