"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line (<=200 chars) to /output/entry.txt.
"""

import os
from pathlib import Path

LINE = "My phone's autocorrect turned 'on my way' into 'on my weigh' - the most honest fitness tracker I own, and the only one that never lies to me."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
