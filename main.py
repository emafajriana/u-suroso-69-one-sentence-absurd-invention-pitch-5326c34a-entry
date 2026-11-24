#!/usr/bin/env python3
"""Entry for make.fun: 'One-Sentence Absurd Invention Pitch'.

Writes one sentence pitching a ridiculous invention that fixes a tiny
everyday annoyance to the output entry file. Stdlib only, deterministic.
"""

import os
import sys

PITCH = (
    "The Polite Escape Hat lowers itself over your eyes the moment "
    "someone begins a story with 'So, basically…', so you miss the "
    "next forty minutes and look like you're simply napping."
)

MAX_CHARS = 220


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def verify(path: str) -> None:
    """Read the written file back and check it against the kit gate:
    UTF-8 text, 1 to 220 characters, not only whitespace, one sentence.
    """
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    if not text.strip():
        raise SystemExit("gate FAIL: entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            "gate FAIL: entry is %d chars, over the 220-char limit"
            % len(text)
        )
    if text.count(".") != 1 or not text.rstrip().endswith("."):
        raise SystemExit("gate FAIL: entry must be exactly one sentence")
    print("gate PASS: %d chars, one sentence" % len(text))


def main() -> int:
    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(PITCH)
    verify(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
