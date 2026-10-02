import cli
import pytest


def test_parse_args_takes_a_single_path():
    assert cli.parse_args(["notes.txt"]).path == "notes.txt"


def test_main_prints_a_report_for_the_given_file(tmp_path, capsys):
    path = tmp_path / "notes.txt"
    path.write_bytes(b"hello world\n\nagain\n")

    exit_code = cli.main([str(path)])

    out = capsys.readouterr().out
    assert exit_code == 0
    assert "Lines" in out
    assert "Words" in out
    assert "Characters" in out


def test_main_reports_a_missing_input_without_a_traceback(tmp_path, capsys):
    path = tmp_path / "missing.txt"
    with pytest.raises(OSError) as os_error:
        path.stat()

    exit_code = cli.main([str(path)])

    captured = capsys.readouterr()
    assert exit_code != 0
    assert captured.out == ""
    assert captured.err.startswith("error: ")
    assert str(path) in captured.err
    assert os_error.value.strerror in captured.err
    assert captured.err.count("\n") == 1
    assert "Traceback" not in captured.err


def test_main_reports_a_directory_input_without_a_traceback(tmp_path, capsys):
    with pytest.raises(OSError) as os_error:
        tmp_path.read_bytes()

    exit_code = cli.main([str(tmp_path)])

    captured = capsys.readouterr()
    assert exit_code != 0
    assert captured.out == ""
    assert captured.err.startswith("error: ")
    assert str(tmp_path) in captured.err
    assert os_error.value.strerror in captured.err
    assert captured.err.count("\n") == 1
    assert "Traceback" not in captured.err
