from dataclasses import dataclass


@dataclass
class HistoryEntry:
    """Represents a single clipboard history entry."""

    id: str
    preview: str
    raw: str
