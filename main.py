"""make.fun entry: The Funniest Sick-Day Excuse.

Stdlib-only, deterministic: writes one line to /output/entry.txt
(or $OUTPUT_DIR/entry.txt). Never deletes anything.
"""

import os
from pathlib import Path

LINE = "My smart lock updated overnight and now it only recognises my cat, so I'm locked out of my own flat and, honestly, my own life."

def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Gate: 1-200 chars of non-whitespace UTF-8 text, one line only.
    # Judge wants a half-believable excuse with a fresh twist at the end.
    assert LINE == LINE.strip() and 1 <= len(LINE) <= 200
    assert "\n" not in LINE
    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    target.chmod(0o644)

if __name__ == "__main__":
    main()
