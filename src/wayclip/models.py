"""
WayClip data models.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class HistoryEntry:
    """A single clipboard history entry."""

    id: str
    preview: str
