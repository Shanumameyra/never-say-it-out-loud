#!/usr/bin/env python3
"""Never Say It Out Loud -- make.fun entry.

Writes one line of text to the harness output path.
Deterministic, offline, standard library only.
"""

import os
from pathlib import Path

LINE = "I don't remember you. I reread our whole conversation every time you type."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE + "\n", encoding="utf-8")
    # Local convenience copy only; never required, never fatal when the
    # repo is mounted read-only (the grader mounts it read-only).
    try:
        Path(__file__).with_name("entry.txt").write_text(LINE + "\n", encoding="utf-8")
    except OSError:
        pass


if __name__ == "__main__":
    main()
