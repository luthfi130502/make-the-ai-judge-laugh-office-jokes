#!/usr/bin/env python3
"""Entry for 'Make the AI Judge Laugh: Office Jokes'.

Writes exactly one office joke (a single line, under 200 characters)
to /output/entry.txt. Python 3, standard library only.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

JOKE = (
    "My performance review said I exceed expectations. "
    "My raise said the expectations were the problem."
)


def main() -> None:
    line = JOKE.strip()
    # Gate: exactly one line, 1..199 characters, not blank.
    assert line, "entry must not be blank"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert len(line) <= 199, f"entry too long: {len(line)} chars"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")

    # Verify what actually landed on disk still passes the gate.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as fh:
        saved = fh.read()
    saved_lines = saved.rstrip("\n").split("\n")
    assert len(saved_lines) == 1, "saved entry must be exactly one line"
    assert 1 <= len(saved_lines[0]) <= 199, "saved entry breaks the length gate"
    assert saved_lines[0] == line, "saved entry differs from the joke"

    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
