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
    print("============ BOOKBOT ============")
    frankenstein_path = "books/frankenstein.txt"
    print(f"Analyzing book found at {frankenstein_path}")
    frankenstein_txt = get_book_text(frankenstein_path)
    print("----------- Word Count ----------")
    num_words = count_words(frankenstein_txt)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    counts = count_characters(frankenstein_txt)
    sorted_chars = sort_counts(counts)
    print_counts(sorted_chars)
    print("============= END ===============")


main()
