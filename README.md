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

Run the suite from the repo root — `conftest.py` is what puts the root on
the import path, so running it from anywhere else fails with
`ModuleNotFoundError`.

```bash
pytest
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
├── tests/
├── conftest.py
└── requirements.txt
```
