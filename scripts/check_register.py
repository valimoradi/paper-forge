#!/usr/bin/env python3
"""Grep-level checks for the academic base layer (Layer 1).

Usage: python check_register.py paper.tex

Reports em-dashes, question marks in prose, \\textbf in running prose, and
banned filler words. Findings are pointers for a human/agent pass, not
auto-fixes; some hits are legitimate (verbatim quotes, research questions).
"""
import re, sys
from pathlib import Path

BANNED_WORDS = [
    "crucially", "remarkably", "notably", "importantly", "interestingly",
    "delve", "leverage", "groundbreaking", "cutting-edge", "state-of-the-art",
    "it is worth noting", "needless to say", "at the end of the day",
    "not only", "moreover, ",
]


def main() -> int:
    path = Path(sys.argv[1])
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    hits = 0
    for i, raw in enumerate(lines, 1):
        line = re.sub(r"(?<!\\)%.*", "", raw)
        prose = re.sub(r"\$[^$]*\$", "", line)
        checks = []
        if "—" in prose or "---" in prose:
            checks.append("em-dash")
        if re.search(r"\?\s*($|\\\\|})", prose) and "??" not in prose:
            checks.append("question mark")
        if re.search(r"\\textbf\{", prose) and not re.match(r"\s*\\(section|subsection|paragraph|caption)", line):
            checks.append("\\textbf in prose")
        low = prose.lower()
        for w in BANNED_WORDS:
            if w in low:
                checks.append(f"banned: '{w.strip()}'")
        for c in checks:
            print(f"{path.name}:{i}: {c}: {raw.strip()[:90]}")
            hits += 1
    print(f"\n{hits} findings (review each; quotes and research questions may be legitimate)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
