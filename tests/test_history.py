"""
Development test for WayClip history module.
"""

from wayclip.history import list_history, decode_entry


def main():
    history = list_history()

    print(f"History contains {len(history)} entries.")

    if not history:
        return

    newest = history[0]

    print()
    print("Newest entry:")
    print(f"ID     : {newest.id}")
    print(f"Preview: {newest.preview}")

    decoded = decode_entry(newest.id)

    if "\n" in decoded:
        print()
        print("Decoded content:")
        print(decoded)
    else:
        print()
        print(f"Decoded content: {decoded}")


if __name__ == "__main__":
    main()
