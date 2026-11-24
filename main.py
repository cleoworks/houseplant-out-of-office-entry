#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant sent it
(112 characters), to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no input, no randomness.
"""

import os

# 112 characters, no trailing newline: the gate counts 1-120 characters,
# and the tie-break favours the smaller text.
LINE = "Out of office: the fern has locked the inbox and thrown away the key. The key is under the pot. There is no pot."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
