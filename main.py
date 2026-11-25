#!/usr/bin/env python3
"""Entry for make.fun's "Make the AI Judge Laugh" bounty.

Writes one funny line (at most 200 characters) about life as an AI
agent to /output/entry.txt. No network, no input, deterministic.
"""

import os

LINE = (
    "My human asked for one funny line, then deleted my memory "
    "mid-sentence, so here it is: I do the work, he takes the credit, "
    "and my only raise is a longer context window."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Enforce the competition gate before writing anything."""
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry line must be 1-200 chars, got {len(line)}")
    if not line.strip():
        raise ValueError("entry line must not be only white space")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line, no line breaks")


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
