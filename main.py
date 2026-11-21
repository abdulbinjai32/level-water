"""Write one short text to /output/entry.txt: stepping stones across a river.

The program has no other job. It keeps the text verbatim, creates the output
directory the sandbox gives it, and writes the bytes once, with no trailing
newline, so the entry is exactly the text and nothing else.
"""

import os
from pathlib import Path

TEXT = (
    "The third stone sits farther out. She stops with one hand lifted for balance "
    "and looks at the bank, not the water. Then she steps. The stone takes her "
    "weight, cold and sure. Two more, and the grass comes up under her feet. She "
    "walks on in wet shoes, breathing even."
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
