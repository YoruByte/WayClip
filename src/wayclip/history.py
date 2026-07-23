"""
WayClip History API.
"""

from wayclip.backend import run_cliphist, copy_to_clipboard
from wayclip.models import HistoryEntry


def list_history():
    """Return clipboard history as structured data."""

    output = run_cliphist("list")

    if not output.strip():
        return []

    entries = []

    for line in output.splitlines():
        parts = line.split("\t", 1)

        if len(parts) != 2:
            continue

        entries.append(
            HistoryEntry(
                id=parts[0],
                preview=parts[1],
            )
        )

    return entries


def decode_entry(entry_id: str):
    """Return the full contents of a clipboard entry."""

    return run_cliphist("decode", entry_id)


def restore_entry(entry_id: str):
    """Restore a clipboard entry."""

    text = decode_entry(entry_id)
    copy_to_clipboard(text)
