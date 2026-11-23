#!/usr/bin/env python3
"""One-Line Roast entry: writes the roast line to /output/entry.txt.

The line roasts a gadget used every day — wireless earbuds whose
self-location feature exists mainly because one of them is always lost.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
LINE_PATH = os.path.join(HERE, "line.txt")
OUTPUT_PATH = "/output/entry.txt"


def load_line() -> str:
    with open(LINE_PATH, encoding="utf-8") as fh:
        return fh.read().strip()


def validate(line: str) -> str:
    """Enforce the bounty gate: one line, 1-200 characters, non-blank."""
    if not line or not line.strip():
        raise ValueError("roast line is blank")
    if "\n" in line or "\r" in line:
        raise ValueError("roast must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"roast must be 1-200 characters, got {len(line)}")
    return line


def main() -> None:
    line = validate(load_line())
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(line)


if __name__ == "__main__":
    main()
