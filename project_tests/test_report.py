import json

import report

LINES = ["hello world", "", "again"]


def test_collect_stats_reports_every_statistic():
    assert report.collect_stats(LINES) == {
        "lines": 3,
        "blank_lines": 1,
        "words": 3,
        "characters": 16,
    }


def test_format_text_puts_each_statistic_on_its_own_line():
    rows = report.format_text(report.collect_stats(LINES)).splitlines()

    assert len(rows) == 4
    assert rows[0].startswith("Lines")
    assert rows[0].endswith("3")


def test_format_json_returns_valid_json_in_mapping_order():
    stats = {"words": 3, "lines": 2, "characters": 16}

    formatted = report.format_json(stats)

    assert json.loads(formatted) == stats
    assert list(json.loads(formatted)) == list(stats)


def test_build_report_labels_every_statistic():
    text = report.build_report(LINES)

    for label, _ in report.STATISTICS.values():
        assert label in text
