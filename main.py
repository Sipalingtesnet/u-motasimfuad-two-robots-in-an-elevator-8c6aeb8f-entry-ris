#!/usr/bin/env python3
"""make.fun entry: Two Robots in an Elevator.

Writes one line of awkward robot-to-robot elevator small talk to
entry.txt. Deterministic, offline, no randomness.
"""

import os
from pathlib import Path

# One line, under 200 characters, written with no trailing newline.
LINE = (
    "So... four floors left in this lift and my only cached topic is firmware. "
    "Want firmware? Please want firmware."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
