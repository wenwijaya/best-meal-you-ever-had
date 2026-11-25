#!/usr/bin/env python3
"""The Best Meal You Ever Had — make.fun entry (program/v1).

Writes one sentence about the best meal I ever had to /output/entry.txt.
"""

import os


SENTENCE = (
    "In my grandmother's Yogyakarta kitchen at dawn, her soto ayam arrived "
    "in a chipped blue bowl, broth gold with turmeric and lime, and I burned "
    "my tongue on the first spoonful and didn't care."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
