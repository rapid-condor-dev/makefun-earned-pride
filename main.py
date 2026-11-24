#!/usr/bin/env python3
"""One Line of Earned Pride - make.fun entry.

Writes a single line (1-240 characters) to /output/entry.txt: a quiet,
earned moment of pride for someone in a scene. Three winters of mending
nets by lamplight, a granddaughter's first catch hauled in alone, and a
grandfather who says nothing - the pride is earned inside the line, by
effort the reader can feel, and it lands on the last word.
"""

import os

LINE = (
    "Three winters he mended nets by lamplight; tonight his granddaughter "
    "hauled the first catch in alone, and Tomas said nothing \u2014 just kept "
    "mending, smiling at the rope."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
