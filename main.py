"""Write one short text to /output/entry.txt: stepping stones across a river.

The program has no other job. It keeps the text verbatim, creates the output
directory the sandbox gives it, and writes the bytes once, with no trailing
newline, so the entry is exactly the text and nothing else.
"""

import os
from pathlib import Path

TEXT = (
    "Third stone farther out than she remembers, water quick and brown. "
    "She stops, one hand out for balance, looks at the bank, not the water. "
    "Steps. The stone takes her weight, cold and sure. Two more, and grass. "
    "She walks on, wet shoes, breathing even, river loud behind her."
)


def write_entry() -> str:
    """Write TEXT to entry.txt under the output directory, and return its path."""
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    return str(target)


if __name__ == "__main__":
    print(write_entry())
