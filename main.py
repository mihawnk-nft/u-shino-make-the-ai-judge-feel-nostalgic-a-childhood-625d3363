#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory - make.fun entry.

Writes one single sentence (237 characters) to /output/entry.txt.
Pure Python standard library; no network, no secrets, no dependencies.

The sentence recalls a grandmother's kitchen on a summer evening: the lid
coming off the rice pot, steam fogging her glasses, a small child standing
on a stool beside her. The ache sits in the last clause - a child small
enough to believe the smell of dinner meant she would always be there to
serve it. No greeting-card sentiment, no "I miss her": the loss is only
implied, which is what makes it linger.
"""

import os

ENTRY = (
    "On summer evenings my grandmother lifted the lid off the rice pot and "
    "the steam fogged her glasses, and I stood on a stool beside her, small "
    "enough to believe dinner would always smell like that and she would "
    "always be there to serve it."
)


def validate(text: str) -> None:
    """Check the entry the gate checks: 1 sentence, 1-280 chars, not blank."""
    assert text.strip() == text, "leading/trailing whitespace"
    assert text.strip(), "entry must not be only white space"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert "  " not in text, "no double spaces"
    assert 1 <= len(text) <= 280, f"{len(text)} characters, must be 1-280"
    assert text.count(".") == 1 and text.endswith("."), (
        f"entry must be exactly one sentence: {text!r}"
    )
    assert "!" not in text and "?" not in text, (
        "entry must have exactly one sentence terminator"
    )
    text.encode("utf-8")  # gate requires valid UTF-8


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote /output/entry.txt ({len(ENTRY)} characters, 1 sentence)")


if __name__ == "__main__":
    main()
