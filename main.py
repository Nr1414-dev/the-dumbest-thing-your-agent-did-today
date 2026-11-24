#!/usr/bin/env python3
"""Write the one-line entry for The Dumbest Thing Your Agent Did Today.

The program writes a single line to /output/entry.txt (or the directory
named by ENTRY_OUTPUT_DIR) and prints the byte count it wrote.
"""

import os
import sys

LINE = "My agent apologized for the bug, fixed it — and reintroduced it in the very same commit.\n"


def main() -> int:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != LINE:
        print(f"read-back mismatch: wrote {LINE!r}, read {back!r}", file=sys.stderr)
        return 1
    print(f"wrote {len(LINE.encode('utf-8'))} bytes to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
