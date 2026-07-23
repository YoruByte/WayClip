"""
Development test for restore_entry().
"""

from wayclip.history import list_history, restore_entry
import subprocess


def main():
    history = list_history()

    if not history:
        print("History is empty.")
        return

    newest = history[0]

    print(f"Restoring entry {newest.id}...")

    restore_entry(newest.id)

    restored = subprocess.run(
        ["wl-paste"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout

    print("Clipboard now contains:")
    print(restored)


if __name__ == "__main__":
    main()
