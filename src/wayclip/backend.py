"""
WayClip backend.

All communication with cliphist happens here.
"""

from shutil import which
import subprocess

CLIPHIST = which("cliphist")


def require_cliphist():
    """Raise an error if cliphist isn't installed."""
    if CLIPHIST is None:
        raise RuntimeError("cliphist is not installed")


def run_cliphist(*args):
    """Run a cliphist command and return stdout."""
    require_cliphist()

    result = subprocess.run(
        [CLIPHIST, *args],
        capture_output=True,
        text=True,
        check=True,
    )

    return result.stdout


def list_entries():
    """Return raw cliphist list output."""
    return run_cliphist("list")


def decode(entry_id: str):
    """Decode a clipboard entry."""
    return run_cliphist("decode", entry_id)


def delete(raw_line: str):
    """Delete a clipboard entry."""

    require_cliphist()

    # cliphist delete reads the selected entry from stdin.
    subprocess.run(
        [CLIPHIST, "delete"],
        input=raw_line,
        text=True,
        check=True,
    )
    

def wipe():
    """Clear clipboard history."""
    return run_cliphist("wipe")


def copy_to_clipboard(text: str):
    """Copy text to the Wayland clipboard."""

    subprocess.run(
        ["wl-copy"],
        input=text,
        text=True,
        check=True,
    )


if __name__ == "__main__":
    print("WayClip Backend Test")
    print("--------------------")

    output = list_entries()
    lines = output.splitlines()

    print(f"Clipboard entries: {len(lines)}")

    if lines:
        print("First entry:")
        print(lines[0])
