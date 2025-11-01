def get_book_text(filepath: str) -> str:
    file_contents = ""
    with open(filepath, "r") as f:
        file_contents = f.read()
    return file_contents


def main() -> None:
    frankenstein_path = "books/frankenstein.txt"
    frankenstein_txt = get_book_text(frankenstein_path)
    print(frankenstein_txt)


main()
