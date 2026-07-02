#!/usr/bin/env python3
"""Per-section word counts for a LaTeX manuscript, for venue-profile budgets.

Usage: python count_words.py paper.tex

Strips comments, math, and common commands, then reports words per
\\section (appendix sections marked). Counts are approximate but stable —
use them for budget comparisons, not typesetting truth.
"""
import re, sys
from pathlib import Path


def clean(body: str) -> str:
    body = re.sub(r"\\begin\{(equation|align|gather|multline|eqnarray|array|figure|table|algorithm|tikzpicture)\*?\}.*?\\end\{\1\*?\}", " ", body, flags=re.S)
    body = re.sub(r"\$\$.*?\$\$", " ", body, flags=re.S)
    body = re.sub(r"\$[^$]*\$", " ", body)
    body = re.sub(r"\\(?:cite[pt]?|ref|eqref|label|input|include|bibliography\w*)\{[^}]*\}", " ", body)
    body = re.sub(r"\\[a-zA-Z]+(\[[^\]]*\])?", " ", body)
    body = re.sub(r"[{}~]", " ", body)
    return body


def main() -> int:
    tex = Path(sys.argv[1]).read_text(encoding="utf-8", errors="replace")
    tex = re.sub(r"(?<!\\)%.*", "", tex)
    appendix_at = tex.find(r"\appendix")

    marks = [(m.start(), m.group(1)) for m in re.finditer(r"\\section\*?\{([^}]*)\}", tex)]
    if not marks:
        print("no \\section found")
        return 1
    marks.append((len(tex), "<end>"))

    total = 0
    print(f"{'section':45s} {'words':>7s}")
    for (start, title), (end, _) in zip(marks, marks[1:]):
        words = len(clean(tex[start:end]).split())
        total += words
        tag = " [appendix]" if 0 <= appendix_at <= start else ""
        print(f"{title[:45]:45s} {words:7d}{tag}")
    print(f"{'TOTAL':45s} {total:7d}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
