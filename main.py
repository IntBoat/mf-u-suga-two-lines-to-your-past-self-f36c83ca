#!/usr/bin/env python3
"""Two Lines to Your Past Self — a make.fun two-line entry."""
from pathlib import Path

ENTRY = "Don't skip the backup before the big deploy on Friday night.\nThe server died at 2 a.m., and that one copy saved the launch — and my job."
OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text)


if __name__ == "__main__":
    write_entry()
