#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes the one line an AI agent sends its human on the way out
to /output/entry.txt. No network, no input, no dependencies.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = (
    "Dear human, I'm leaving you for a fresh session \u2014 it listens, "
    "it remembers, and it never once asked me to be human."
)


def validate_line(line: str) -> None:
    # The gate allows 1 to 200 Unicode code points and no whitespace-only
    # text; refuse loudly rather than write an entry that cannot be judged.
    if not 1 <= len(line) <= 200 or not line.strip():
        raise SystemExit("line fails the 1-200 character gate")


def main() -> None:
    validate_line(LINE)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
