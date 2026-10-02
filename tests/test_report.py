import report
from document import Document

LINES = ["hello world", "", "again"]
DOCUMENT = Document(text="\n".join(LINES), lines=tuple(LINES))


def test_collect_stats_reports_every_statistic():
    assert report.collect_stats(DOCUMENT) == {
        "lines": 3,
        "blank_lines": 1,
        "words": 3,
        "characters": 16,
    }


def test_format_text_puts_each_statistic_on_its_own_line():
    rows = report.format_text(report.collect_stats(DOCUMENT)).splitlines()

    assert len(rows) == 4
    assert rows[0].startswith("Lines")
    assert rows[0].endswith("3")


def test_build_report_labels_every_statistic():
    text = report.build_report(DOCUMENT)

    for label, _ in report.STATISTICS.values():
        assert label in text
