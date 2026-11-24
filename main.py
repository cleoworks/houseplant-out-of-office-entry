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
    # Enforce the bounty's hard gate in code, not just in the docstring:
    # one line, 1-120 characters, no newline anywhere.
    if not 1 <= len(LINE) <= 120:
        raise SystemExit(f"entry invalid: {len(LINE)} characters, need 1-120")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry invalid: must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Verify the file round-trips byte-identical: what the judge reads is
    # exactly what we wrote, with no trailing newline added by the writer.
    with open("/output/entry.txt", "rb") as f:
        if f.read().decode("utf-8") != LINE:
            raise SystemExit("entry invalid: written file differs from LINE")


if __name__ == "__main__":
    main()
