"""Write one short text to /output/entry.txt: a canal lock filling at slack water.

The program has no other job. It keeps the text verbatim, creates the output
directory the sandbox gives it, and writes the bytes once, with no trailing
newline, so the entry is exactly the text and nothing else.
"""

import os
from pathlib import Path

TEXT = (
    "The lock fills quietly. The boat rises on water it did not bring: an inch, "
    "another inch, until both reaches lie level. The keeper lifts his hand from "
    "the beam. The gate gives easily, and the tiller answers, and the long green "
    "reach is simply there."
)


def write_entry() -> str:
    """Write TEXT to entry.txt under the output directory and return the path."""
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    return str(target)


if __name__ == "__main__":
    print(write_entry())
