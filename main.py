#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single one-line comedy joke to /output/entry.txt.
Pure standard library, deterministic: the same line every run.
"""

import os

JOKE = (
    "I hired a life coach and he quit, saying I was the first client "
    "whose five-year plan was just the words 'wait and see' in "
    "different fonts."
)


def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
