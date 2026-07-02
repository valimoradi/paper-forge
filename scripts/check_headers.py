#!/usr/bin/env python3
"""Measure section/header formatting idiom in a LaTeX manuscript.

Usage:
  python check_headers.py paper.tex                 # report the manuscript
  python check_headers.py corpus/*.tex --corpus     # measure a venue corpus

Counts run-in / bold headers per (sub)section and flags the two idioms an LLM
reaches for by default and most OR/MS/econ/stats journals do NOT use:
per-experiment "Discussion"/"Summary" labels, and checklist-style micro-headers.
Compare the manuscript's density to the corpus median (measure the corpus first
with --corpus) — this operationalizes the venue-register structural-idiom
target so it is measured, not eyeballed. Findings are pointers, not auto-fixes.
"""
import re, sys
from pathlib import Path

RUNIN = re.compile(r"\\(paragraph|subparagraph)\*?\{([^}]*)\}")
SUBSUB = re.compile(r"\\subsubsection\*?\{([^}]*)\}")
BOLD_LEADING = re.compile(r"^\s*\\textbf\{([^}]*)\}\.?", re.M)  # bold run-in at line start
SECTION = re.compile(r"\\(section|subsection)\*?\{([^}]*)\}")
LABEL_WORDS = ("discussion", "summary", "takeaway", "takeaways", "remarks")


def strip_comments(t): return re.sub(r"(?<!\\)%.*", "", t)


def analyze(path: Path):
    tex = strip_comments(path.read_text(encoding="utf-8", errors="replace"))
    runins = RUNIN.findall(tex)
    subsubs = SUBSUB.findall(tex)
    bolds = BOLD_LEADING.findall(tex)
    n_sections = len(SECTION.findall(tex)) or 1
    total_runin = len(runins) + len(subsubs) + len(bolds)
    label_hits = []
    for kind, txt in (
        [("paragraph", t) for _, t in runins]
        + [("subsubsection", t) for t in subsubs]
        + [("textbf-runin", t) for t in bolds]
    ):
        if any(w in txt.lower() for w in LABEL_WORDS):
            label_hits.append((kind, txt.strip()))
    return {
        "path": path.name,
        "runin_headers": total_runin,
        "per_section": round(total_runin / n_sections, 1),
        "sections": n_sections,
        "label_flags": label_hits,
        "all_runin_titles": [t.strip() for _, t in runins] + [t.strip() for t in subsubs],
    }


def main() -> int:
    argv = sys.argv[1:]
    corpus = "--corpus" in argv
    files = [Path(a) for a in argv if not a.startswith("--")]
    if not files:
        print(__doc__)
        return 1

    stats = [analyze(f) for f in files if f.exists()]
    if corpus:
        dens = sorted(s["per_section"] for s in stats)
        med = dens[len(dens) // 2] if dens else 0
        print(f"venue corpus: {len(stats)} papers")
        for s in stats:
            print(f"  {s['path']:40s} {s['runin_headers']:3d} run-in headers, {s['per_section']}/section")
        print(f"\nCORPUS MEDIAN run-in-header density: {med} per section")
        print("Use this as the manuscript's structural-idiom target in venue-register.md.")
        return 0

    for s in stats:
        print(f"{s['path']}: {s['runin_headers']} run-in headers "
              f"({s['per_section']} per section across {s['sections']} sections)")
        if s["label_flags"]:
            print("  FLAG — per-experiment discussion/summary labels "
                  "(most prose-forward venues avoid these):")
            for kind, txt in s["label_flags"]:
                print(f"    \\{kind}{{{txt}}}")
        if s["per_section"] > 4:
            print(f"  FLAG — high run-in-header density ({s['per_section']}/section). "
                  "Compare to the venue corpus median (run --corpus); likely the "
                  "model's ML/CS-paper default. Titles:")
            for t in s["all_runin_titles"][:20]:
                print(f"    - {t}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
