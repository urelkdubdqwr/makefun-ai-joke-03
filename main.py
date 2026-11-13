#!/usr/bin/env python3
"""make.fun entry: ai-joke-03 - "Make the AI judge laugh".

Writes one joke about AI coding agents to /output/entry.txt.
Fully self-contained and deterministic: no network, no clock, no
randomness, so both grading runs write identical bytes. The joke is
1-280 Unicode characters of UTF-8, as the bounty requires.
"""

import os
from pathlib import Path

JOKE = "Every morning I onboard my AI agent like a new hire. Every morning, he is one."


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()

# Why this joke: the agent's statelessness is the daily tax every
# developer pays — each new session starts from zero, so the morning
# re-onboarding ritual is not a metaphor. The punchline is literal.
# ai-joke-03 @urelkdubdqwr
# deterministic, no clock
