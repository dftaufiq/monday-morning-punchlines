#!/usr/bin/env python3
"""Monday Morning Punchlines: one joke about Monday mornings — make.fun entry.

Writes the entry joke to /output/entry.txt. Deterministic: the same line
every run, so the two grading runs are byte-identical.

The line (129 chars, under the 200-char gate): a named alarm clock, Dave,
rings at 6:00, 6:09, 6:18, gives up, and snitches to the boss — a 2-beat
setup with the reveal in the last clause.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-200 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 200:
        print(f"ERROR: entry is {len(line)} chars, over the 200-char limit",
              file=sys.stderr)
        sys.exit(1)


LINE = (
    "My alarm is called Dave. On Monday he rang at 6 a.m., 6:09, 6:18, "
    "then gave up and texted my boss: 'He's awake. He's just lying.'"
)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back: never ship a silently truncated or altered entry.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        print("ERROR: entry.txt does not match the entry line", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
