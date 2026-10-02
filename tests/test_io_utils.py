import pytest

import io_utils


def test_read_text_reads_utf8(tmp_path):
    path = tmp_path / "utf8.txt"
    path.write_bytes("café\nnaïve\n".encode("utf-8"))

    assert io_utils.read_text(path) == "café\nnaïve\n"


def test_read_text_falls_back_to_a_second_encoding(tmp_path):
    path = tmp_path / "latin1.txt"
    path.write_bytes("café".encode("latin-1"))

    assert io_utils.read_text(path) == "café"


def test_read_text_refuses_a_file_over_the_limit(tmp_path, monkeypatch):
    path = tmp_path / "big.txt"
    path.write_bytes(b"x" * 100)
    monkeypatch.setattr(io_utils, "MAX_FILE_BYTES", 10)

    with pytest.raises(io_utils.FileTooLargeError):
        io_utils.read_text(path)


def test_read_lines_splits_on_line_breaks(tmp_path):
    path = tmp_path / "lines.txt"
    path.write_bytes(b"one\n\nthree\n")

    assert io_utils.read_lines(path) == ["one", "", "three"]
