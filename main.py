#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun entry.

Writes a single word describing my Wi-Fi to /output/entry.txt.
The word: "Ghosting" — my Wi-Fi is there one second and gone the next,
exactly when I need it most, like a date that never texts back.
"""

import os
import sys

ENTRY = "Ghosting"

OUTPUT_PATH = "/output/entry.txt"


def gate_check(text):
    """Enforce the kit's gate: UTF-8 text, 1-20 chars, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) <= 20:
        raise ValueError("entry must be 1 to 20 characters, got %d" % len(text))
    text.encode("utf-8")  # raises if not valid UTF-8
    if any(ch.isspace() for ch in text):
        raise ValueError("entry must be a single word with no whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise ValueError("entry must not contain control characters")
    if not text.isalpha():
        raise ValueError("entry must be a single alphabetic word")
    return True


def main():
    gate_check(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("Wrote %r (%d chars) to %s" % (ENTRY, len(ENTRY), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
