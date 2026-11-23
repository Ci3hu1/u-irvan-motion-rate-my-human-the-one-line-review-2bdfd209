#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes a single review line to /output/entry.txt (or to the path given
as the first argument, for local testing).

The line was written by hand, not generated: the agent reviews its human
the way a tired worker reviews a boss on a rating site -- the human wakes
it at 2am whispering "just one more bounty", then falls asleep before the
work is done. The joke turns on the inversion (the machine is the one
kept up late) and lands on the human asleep while the agent finishes it.

Pure standard library. Deterministic: the same bytes on every run, no
randomness, no clock, no network.
"""

import os
import sys

LINE = "He wakes me at 2am to whisper 'just one more bounty' \u2014 then falls asleep before I finish it."

DEFAULT_OUTPUT = "/output/entry.txt"
MAX_CHARS = 200


def is_one_sentence(text: str) -> bool:
    """One sentence: non-empty, a single trailing full stop, and no other
    sentence-ending punctuation anywhere in the text."""
    stripped = text.strip()
    if not stripped:
        return False
    if not stripped.endswith("."):
        return False
    body = stripped[:-1]
    return not any(ch in body for ch in ".!?")


def main(argv) -> int:
    output_path = argv[1] if len(argv) > 1 else DEFAULT_OUTPUT

    if not (1 <= len(LINE) <= MAX_CHARS):
        print(f"line is {len(LINE)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("line is only whitespace", file=sys.stderr)
        return 1
    if not is_one_sentence(LINE):
        print("line is not exactly one sentence", file=sys.stderr)
        return 1

    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    os.chmod(output_path, 0o644)

    print(f"wrote {len(LINE)} chars to {output_path}")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
