from stats import count_words, count_characters


def get_book_text(filepath: str) -> str:
    file_contents = ""
    with open(filepath, "r") as f:
        file_contents = f.read()
    return file_contents


def main() -> None:
    frankenstein_path = "books/frankenstein.txt"
    frankenstein_txt = get_book_text(frankenstein_path)
    num_words = count_words(frankenstein_txt)
    num_chars = count_characters(frankenstein_txt)
    print(f"Found {num_words} total words")
    print(num_chars)


main()
