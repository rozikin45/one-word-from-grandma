#!/usr/bin/env python3
"""One Word From Grandma — make.fun entry.

Writes exactly one word to /output/entry.txt: the single word a grandma
would text about AI.

The word: "Whatchamacallit" — the classic grandma word for a thing she
cannot name, which is exactly what AI is to her. Warm, a little baffled,
funny on its own, and tied to a machine she does not quite understand.
It is one word, 15 characters, inside the gate's 1-30 characters.
"""

import os
import sys

WORD = "Whatchamacallit"


def main() -> int:
    # A single word: no spaces, no punctuation, 1-30 characters.
    word = WORD.strip()
    assert word and " " not in word and 1 <= len(word) <= 30, "word fails gate"
    assert word.isalpha(), "word must be letters only"

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # Write with a trailing newline; the gate counts characters of the text.
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(word + "\n")
    # Read back what was written and re-check the gate on the real bytes,
    # so a silent write failure can never pass as a valid entry.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written.strip() == word, "written text differs from word"
    assert 1 <= len(written.strip()) <= 30, "written text fails gate"
    print(word)
    return 0


if __name__ == "__main__":
    sys.exit(main())
