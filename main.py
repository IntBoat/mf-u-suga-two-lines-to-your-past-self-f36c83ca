#!/usr/bin/env python3
"""Two Lines to Your Past Self (make.fun).

Writes the entry to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = 'When the senior engineer offers to rewrite your module for you the week before launch, say no and ship your own ugly version.\nThat ugly version taught you the system; his clean rewrite would have taught you only how to ask him next time.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
