#!/usr/bin/env python3
"""Check a LaTeX manuscript against the venue's hard gates.

Usage:
  python check_gates.py paper.tex --max-figures 5 --max-tables 3 \
      --max-abstract-words 150 [--max-pages 32 --pdf paper.pdf]

Counts figure/table environments (starred included), abstract words, and
optionally PDF pages (needs pypdf). Exit code 1 if any gate is violated,
so it can gate a commit or CI step. Counts cover \\input/\\include'd files
one level deep.
"""
import argparse, re, sys
from pathlib import Path


def strip_comments(tex: str) -> str:
    return re.sub(r"(?<!\\)%.*", "", tex)


def gather_source(main: Path) -> str:
    tex = strip_comments(main.read_text(encoding="utf-8", errors="replace"))
    parts = [tex]
    for name in re.findall(r"\\(?:input|include)\{([^}]+)\}", tex):
        p = (main.parent / name)
        if p.suffix == "":
            p = p.with_suffix(".tex")
        if p.exists():
            parts.append(strip_comments(p.read_text(encoding="utf-8", errors="replace")))
    return "\n".join(parts)


def count_env(tex: str, env: str) -> int:
    return len(re.findall(r"\\begin\{" + env + r"\*?\}", tex))


def abstract_words(tex: str) -> int:
    m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", tex, re.S)
    if not m:
        return -1
    body = re.sub(r"\\[a-zA-Z]+(\[[^\]]*\])?(\{[^{}]*\})?", " ", m.group(1))
    body = re.sub(r"[\\{}$~]", " ", body)
    return len(body.split())


def pdf_pages(path: Path) -> int:
    try:
        from pypdf import PdfReader
    except ImportError:
        try:
            from PyPDF2 import PdfReader  # type: ignore
        except ImportError:
            return -1
    return len(PdfReader(str(path)).pages)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("texfile", type=Path)
    ap.add_argument("--max-figures", type=int)
    ap.add_argument("--max-tables", type=int)
    ap.add_argument("--max-abstract-words", type=int)
    ap.add_argument("--max-pages", type=int)
    ap.add_argument("--pdf", type=Path)
    a = ap.parse_args()

    tex = gather_source(a.texfile)
    failures = []

    def gate(label, value, limit):
        if value < 0:
            print(f"  {label}: could not measure (skipped)")
            return
        status = "OK" if limit is None or value <= limit else "VIOLATION"
        lim = "-" if limit is None else limit
        print(f"  {label}: {value} / {lim}  {status}")
        if status == "VIOLATION":
            failures.append(label)

    print(f"Hard gates for {a.texfile}:")
    gate("figures", count_env(tex, "figure"), a.max_figures)
    gate("tables", count_env(tex, "table"), a.max_tables)
    gate("abstract words", abstract_words(tex), a.max_abstract_words)
    if a.max_pages is not None:
        if not a.pdf:
            print("  pages: pass --pdf to check the page gate")
        else:
            gate("pages (official class build)", pdf_pages(a.pdf), a.max_pages)

    if failures:
        print(f"FAILED gates: {', '.join(failures)}")
        return 1
    print("All measured gates OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
