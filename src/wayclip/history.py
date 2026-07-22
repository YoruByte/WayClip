"""
WayClip History API.
"""

from wayclip.backend import run_cliphist

def list_history():
    """Return clipboard history as a list of lines."""
    output = run_cliphist("list")

    if not output.strip():
        return []

    return output.splitlines()


if __name__ == "__main__":
    history = list_history()

    print(f"History contains {len(history)} entries.")

    if history:
        print()
        print("Newest entry:")
        print(history[0])
