"""One Letter for Your Day entry program.

Writes exactly one letter, Z, to MAKEFUN_OUTPUT_DIR/entry.txt.
The letter stands for the hidden word "zero sleep": the day in one
letter, the sound of sleep itself (Zzz), and the most honest of the
day's words. Stdlib only.
"""

import os
import sys

LETTER = "Z"


def main():
    if len(LETTER) != 1 or not ("A" <= LETTER <= "Z"):
        print(f"entry must be exactly one letter A-Z, got {LETTER!r}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LETTER:
        print("read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
