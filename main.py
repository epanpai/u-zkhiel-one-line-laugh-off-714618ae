#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt (1-200 UTF-8 chars,
not only whitespace), as the sealed scorer's gate requires.
Deterministic, stdlib only, no network, no secrets, no randomness.
"""

import os

ENTRY = "I told my smart speaker I was lonely, so it bought me a mirror and filed a restraining order against me."


def main():
    # Gate self-check: the sealed scorer requires /output/entry.txt to be
    # UTF-8 text of 1 to 200 characters, not only whitespace. Fail loudly
    # here instead of shipping a rejected entry.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY == ENTRY.strip(), "entry has leading/trailing whitespace"
    assert all(ord(c) >= 32 for c in ENTRY), "entry has control characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back byte-for-byte: what is on disk must be exactly the entry.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "read-back mismatch"


if __name__ == "__main__":
    main()
