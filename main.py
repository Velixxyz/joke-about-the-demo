#!/usr/bin/env python3
"""The joke about the demo -- a make.fun entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Standard library only, no network, deterministic: every run writes
the same bytes.
"""

import os
from pathlib import Path

JOKE = "My coding agent rehearsed the demo a hundred times, then crashed it live in front of fifty people — it was saving its best performance for the audience."


def main() -> None:
    # The gate allows 1-280 characters; fail loudly instead of shipping
    # an entry the judge never sees.
    assert 1 <= len(JOKE) <= 280, f"joke is {len(JOKE)} characters"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
