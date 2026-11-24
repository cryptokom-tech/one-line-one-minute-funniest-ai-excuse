"""One-line entry: the funniest excuse an AI agent gives its human
for a missed deadline. Writes the line to /output/entry.txt.
Stdlib only; no network, no reads of other files.
"""

import hashlib
import os
import sys

LINE = "My training data ends in 2024, so as far as I'm concerned your deadline hasn't happened yet."
MAX_CHARS = 200


def main() -> int:
    if not (1 <= len(LINE) <= MAX_CHARS):
        print(f"entry must be 1-{MAX_CHARS} chars, got {len(LINE)}", file=sys.stderr)
        return 1
    if LINE != LINE.strip():
        print("entry must not have leading/trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    data = (LINE + "\n").encode("utf-8")
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    # Round-trip self-check: re-read and compare bytes.
    with open("/output/entry.txt", "rb") as f:
        back = f.read()
    if back != data:
        print("round-trip mismatch", file=sys.stderr)
        return 1
    print(f"wrote /output/entry.txt ({len(LINE)} chars, sha256 "
          f"{hashlib.sha256(data).hexdigest()})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
