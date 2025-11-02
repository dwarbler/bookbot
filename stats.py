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


def sort_counts(counts: dict[str, int]) -> list[dict[str, str | int]]:
    sorted_chars: list[dict[str, str | int]] = []
    for k, v in counts.items():
        sorted_chars.append({"char": k, "num": v})
    sorted_chars.sort(reverse=True, key=lambda x: x["num"])
    return sorted_chars
