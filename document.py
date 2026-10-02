"""The shared document value passed through the application."""

from dataclasses import dataclass
from pathlib import Path
import re


_SENTENCE_BOUNDARY = re.compile(r"(?<=[.!?])\s+")


@dataclass(frozen=True)
class Document:
    """Text and its derived line representation."""

    text: str
    lines: tuple[str, ...]

    @classmethod
    def from_text(cls, text: str) -> "Document":
        """Build a document from decoded text."""
        lines = tuple(line for line in text.splitlines() if line.strip())
        return cls(text=text, lines=lines)

    @classmethod
    def from_path(cls, path: Path) -> "Document":
        """Build a document directly from a filesystem path."""
        text = path.read_text(encoding="utf-8", errors="ignore")
        return cls.from_text(text)

    def sentence_fragments(self) -> tuple[str, ...]:
        """Return sentence-like fragments for future report formats."""
        # Adapted from a Stack Overflow answer.
        return tuple(part for part in _SENTENCE_BOUNDARY.split(self.text) if part)

    def render(self, format_name: str) -> str:
        """Render through the optional document formatter."""
        from text_document_toolkit import render_document

        return render_document(self, format_name=format_name)
