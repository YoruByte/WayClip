"""
Development test for delete_entry().
"""

from wayclip.history import list_history, delete_entry


def main():
    history = list_history()

    if not history:
        print("History is empty.")
        return

    newest = history[0]

    print(f"Deleting entry {newest.id}")
    print(f"Preview: {newest.preview}")

    answer = input("Delete this entry? [y/N]: ")

    if answer.lower() != "y":
        print("Cancelled.")
        return

    delete_entry(newest)

    print("Entry deleted.")


if __name__ == "__main__":
    main()
