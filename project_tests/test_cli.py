import pytest

import cli


def test_parse_args_takes_a_single_path():
    args = cli.parse_args(["notes.txt"])
    assert args.path == "notes.txt"
    assert args.words_only is False


@pytest.mark.parametrize("flag", ["-w", "--words-only"])
def test_parse_args_accepts_words_only(flag):
    args = cli.parse_args([flag, "notes.txt"])
    assert args.path == "notes.txt"
    assert args.words_only is True


def test_main_prints_a_report_for_the_given_file(tmp_path, capsys):
    path = tmp_path / "notes.txt"
    path.write_bytes(b"hello world\n\nagain\n")

    cli.main([str(path)])

    captured = capsys.readouterr()
    assert captured.out == (
        "Lines        3\n"
        "Blank lines  1\n"
        "Words        3\n"
        "Characters   16\n"
    )
    assert captured.err == ""


@pytest.mark.parametrize("flag", ["-w", "--words-only"])
@pytest.mark.parametrize(
    ("content", "expected"),
    [
        (b"hello world\n\nagain\n", "3\n"),
        (b"  don't\tstop.  \n\n again!\t\n", "3\n"),
        (b"", "0\n"),
    ],
)
def test_main_prints_only_the_word_count(tmp_path, capsys, content, expected, flag):
    path = tmp_path / "notes.txt"
    path.write_bytes(content)

    cli.main([str(path), flag])

    captured = capsys.readouterr()
    assert captured.out == expected
    assert captured.err == ""
