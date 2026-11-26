"""The Internet in One Word.

One word for the whole internet: Toilet.

Why it fits: the entire internet is read on the toilet, and it is
mostly crap. It makes the reader laugh first, then nod.
"""

import os

WORD = "Toilet"


def validate(text: str) -> str:
    """Gate: UTF-8 text, 1-30 chars, a single word, not only whitespace."""
    stripped = text.strip()
    assert stripped, "word must not be only whitespace"
    assert 1 <= len(stripped) <= 30, "gate: 1-30 characters"
    assert len(stripped.split()) == 1, "entry must be a single word"
    return stripped


def main() -> None:
    text = validate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
