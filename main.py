#!/usr/bin/env python3
"""Make the Judge Smile — entry program.

Writes a single warm line about a small good thing that happened
today to ``entry.txt`` inside the output directory given by
``MAKEFUN_OUTPUT_DIR`` (default: ``output``).

The line is a fixed, hand-written sentence. The program is
deterministic: the same bytes are written on every run, so the
graded artifact is byte-identical across runs.

Pure Python standard library only — no third-party imports.
"""

import os
import stat
import sys

# One line, 154 characters, about a small good thing that happened today.
LINE = (
    "At 6 a.m. the warung lady slipped an extra fried egg onto my rice "
    "and whispered, 'for the boy who always says thank you' "
    "\u2014 she still doesn't know my name."
)

MAX_CHARS = 200


def main() -> int:
    text = LINE.strip()

    if not text:
        print("error: entry line is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            "error: entry line is %d characters, over the %d limit"
            % (len(text), MAX_CHARS),
            file=sys.stderr,
        )
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)

    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")

    # The graded artifact is a plain readable file.
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)

    print("wrote %s (%d characters)" % (path, len(text)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
