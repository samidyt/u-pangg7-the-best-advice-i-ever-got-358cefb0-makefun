#!/usr/bin/env python3
"""The Best Advice I Ever Got -- make.fun bounty entry.

Writes one sentence (at most 200 characters) about the best advice
ever received to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt)
and prints the same sentence to stdout.
"""

import os
import sys

ENTRY = "My father, wiping down the stall past midnight, said: don\u2019t chase the money \u2014 feed the people who keep coming back, and it will find you."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
