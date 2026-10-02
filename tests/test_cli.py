import cli


def test_parse_args_takes_a_single_path():
    assert cli.parse_args(["notes.txt"]).path == "notes.txt"


def test_main_prints_a_report_for_the_given_file(tmp_path, capsys):
    path = tmp_path / "notes.txt"
    path.write_bytes(b"hello world\n\nagain\n")

    cli.main([str(path)])

    out = capsys.readouterr().out
    assert "Lines" in out
    assert "Words" in out
    assert "Characters" in out
