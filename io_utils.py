"""Everything in this project that touches the filesystem lives here.

The modules that compute statistics (``stats``) and format them
(``report``) only ever see data handed to them, so they can be tested
without a file on disk.
"""

from pathlib import Path

from document import Document

#: Refuse to read anything larger than this, in bytes.
MAX_FILE_BYTES = 5_000_000

PRIMARY_ENCODING = "utf-8"
FALLBACK_ENCODING = "latin-1"


class FileTooLargeError(Exception):
    """Raised when a file is bigger than :data:`MAX_FILE_BYTES`."""


def read_text(path: Path) -> str:
    """Read ``path`` and return its contents as text."""
    size = path.stat().st_size
    if size > MAX_FILE_BYTES:
        raise FileTooLargeError(
            f"{path} is {size} bytes, over the {MAX_FILE_BYTES} byte limit"
        )

    raw = path.read_bytes()
    try:
        return raw.decode(PRIMARY_ENCODING)
    except UnicodeDecodeError:
        return raw.decode(FALLBACK_ENCODING)


def read_lines(path: Path) -> list[str]:
    """Read ``path`` and return its contents split into lines."""
    return read_text(path).splitlines()


def read_document(path: Path) -> Document:
    """Read ``path`` into the shared document model."""
    return Document.from_path(path)
