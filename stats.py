def count_words(text: str) -> int:
    return len(text.split())


def count_characters(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for c in text.lower():
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    return counts
