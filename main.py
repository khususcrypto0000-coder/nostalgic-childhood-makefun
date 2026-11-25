"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one single-sentence childhood memory (at most 280 characters)
to /output/entry.txt, exactly as the gate requires.
"""

import os

ENTRY = (
    "On hot afternoons I still hear the ice-cream cart's little bell, "
    "and for a second I'm seven again, barefoot on the cracked pavement, "
    "coins warm in my fist, while my mother calls my name from the doorway "
    "before the cart rolls away."
)


def main() -> None:
    text = ENTRY
    # Gate: UTF-8 text of 1 to 280 characters, not only whitespace,
    # a single clean sentence.
    assert isinstance(text, str)
    assert 1 <= len(text) <= 280, f"entry is {len(text)} characters"
    assert text.strip(), "entry must not be only whitespace"
    assert text.count(".") == 1 and text.endswith("."), (
        "entry must be a single sentence"
    )
    # Deterministic output: the exact bytes written are always the UTF-8
    # encoding of this one fixed string, nothing more.
    assert text.encode("utf-8").decode("utf-8") == text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
