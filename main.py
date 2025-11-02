import sys
from stats import count_characters, count_words, sort_counts


def get_book_text(filepath: str) -> str:
    file_contents = ""
    with open(filepath, "r") as f:
        file_contents = f.read()
    return file_contents


def print_counts(counts: list[dict[str, str | int]]) -> None:
    for count in counts:
        if not count["char"].isalpha():  # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]
            continue
        print(f"{count['char']}: {count['num']}")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    book_filepath = sys.argv[1]
    print(f"Analyzing book found at {book_filepath}")
    book_text = get_book_text(book_filepath)
    print("----------- Word Count ----------")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    counts = count_characters(book_text)
    sorted_chars = sort_counts(counts)
    print_counts(sorted_chars)
    print("============= END ===============")


main()
