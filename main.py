#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — make.fun entry.

Writes a single-sentence pitch for a ridiculous invention to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic, no network, no model calls.
"""

import os

PITCH = (
    "A TV remote that buries itself in the sofa the instant the adverts "
    "end, purely out of spite, so you must formally negotiate with the "
    "cushions before watching anything."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PITCH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
