"""
Development test for clearing clipboard history.
"""

from wayclip.history import clear_history


def main():
    print("WARNING: This will permanently delete ALL clipboard history.")
    print()

    answer = input("Continue? [y/N]: ")

    if answer.lower() != "y":
        print("Cancelled.")
        return

    clear_history()
    print("Clipboard history cleared.")


if __name__ == "__main__":
    main()