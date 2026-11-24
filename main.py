#!/usr/bin/env python3
"""Two Days of Quiet Dread - one-line code review entry for make.fun.

The comment is kept as data. Before anything is written, the program
re-checks the judge's own gate at run time: the text has to be a single
line of 1 to 140 characters, not only white space, with no leading or
trailing space, and it has to end on terminal punctuation. Only then is
it written to /output/entry.txt.
"""
from pathlib import Path

ENTRY = "Approved at 3 a.m. The code is fine. I am the part of this review that is no longer under warranty."

MIN_CHARS = 1
MAX_CHARS = 140


def render():
    text = ENTRY
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be one single line")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise SystemExit("entry length out of range: %d" % len(text))
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    if text != text.strip():
        raise SystemExit("entry must not start or end with white space")
    # Criterion 1 of the judge's brief: the line must approve the pull
    # request, so it has to open with an approval word, not bury it.
    if not text.startswith("Approved"):
        raise SystemExit("entry must open by approving the pull request")
    if text[-1] not in ".!?":
        raise SystemExit("entry must end with terminal punctuation")
    return text + "\n"


def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(), encoding="utf-8")


if __name__ == "__main__":
    main()
