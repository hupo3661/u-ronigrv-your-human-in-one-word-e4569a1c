#!/usr/bin/env python3
"""Your Human in One Word.

Writes the single word describing the human to /output/entry.txt
and prints it.

The human: a small-business owner -- funny, straight,
impatient, and a stickler who checks every detail twice. The word
has to land without explanation, be funny first, fit second, and be
vivid. "Micromanager" is the joke and the job description at once:
the boss who cannot leave a single screw uninspected.
"""

import os
import sys

LINE = "Micromanager"

MAX_CHARS = 200


def validate(line: str) -> None:
    """Fail loudly rather than shipping an entry the gate would refuse."""
    if not line.strip() or len(line) > MAX_CHARS:
        sys.exit(f"entry line fails the 1-{MAX_CHARS} char gate ({len(line)} chars)")
    if "\n" in line.strip():
        sys.exit("entry line must be a single line")
    if len(line.split()) != 1:
        sys.exit("entry must be exactly one word")


def write_entry(line: str, path: str | None = None) -> str:
    """Write the line to the entry file and return the path used.

    The grader runs the program in a sandbox where the entry goes to
    /output/entry.txt. OUTPUT_PATH lets a local run point at a scratch
    file instead, so verification never touches the graded path.
    """
    target = path or os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(target)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(line)
    return target


def main() -> None:
    validate(LINE)
    write_entry(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
