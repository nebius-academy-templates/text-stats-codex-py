# text-stats

A small command-line tool for looking at text files.

## Install

Requires **Python 3.10+**.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python cli.py samples/sample.txt
```

## Tests

Run the application suite from the repository root. Project tests live in
`project_tests/`; `pytest.ini` limits default discovery to that directory.
The name `tests/` is reserved for the learning platform's validation scripts,
which are distributed separately and are not part of the application suite.

```bash
python -m pytest -q
```

## Layout

```
text-stats/
├── cli.py            # argparse entry point
├── stats.py          # the statistics themselves
├── report.py         # formats the statistics for the terminal
├── io_utils.py       # reading files
├── samples/
│   └── sample.txt
├── project_tests/
├── pytest.ini
├── conftest.py
└── requirements.txt
```
