#!/usr/bin/env python3
"""Enforce "no source on disk, no cite".

Usage:
  python check_citations.py paper.tex --sources sources/ [--bib refs.bib]

Checks:
  1. Every \\needcite{...} placeholder is reported (must be ZERO before
     submission — each means a citation whose source is not yet downloaded).
  2. Every \\cite key has a matching source in the sources folder — matched
     against sources/MANIFEST.md (key -> filename) if present, else against
     filenames in the sources folder (a file whose name contains the key).
Keys with no source on disk are flagged: they must not be cited.
Exit 1 if any \\needcite remains or any cited key lacks a source.
Findings are pointers; the human/agent resolves each.
"""
import argparse, re, sys
from pathlib import Path


def strip_comments(t): return re.sub(r"(?<!\\)%.*", "", t)


def cite_keys(tex: str):
    keys = set()
    for m in re.finditer(r"\\(?:cite|citep|citet|citealp|citeauthor|citeyear)\*?(?:\[[^\]]*\])*\{([^}]*)\}", tex):
        for k in m.group(1).split(","):
            k = k.strip()
            if k:
                keys.add(k)
    return keys


def needcites(tex: str):
    return re.findall(r"\\needcite\{([^}]*)\}", tex)


def sourced_keys(sources: Path):
    """Keys with a source on disk: from MANIFEST.md if present, else filenames."""
    manifest = sources / "MANIFEST.md"
    keys = set()
    files = [p.name for p in sources.glob("*") if p.is_file() and p.name != "MANIFEST.md"]
    if manifest.exists():
        text = manifest.read_text(encoding="utf-8", errors="replace")
        # any token that also appears as a bib-key-looking string; pragmatic:
        # a key is "present" if it appears in the manifest AND some file is listed
        for tok in re.findall(r"[A-Za-z][A-Za-z0-9:_-]{2,}", text):
            keys.add(tok)
    return keys, files


def key_has_source(key: str, manifest_keys, files):
    if key in manifest_keys:
        return True
    kl = key.lower()
    return any(kl in f.lower() for f in files)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("texfile", type=Path)
    ap.add_argument("--sources", type=Path, default=Path("sources"))
    ap.add_argument("--bib", type=Path)
    a = ap.parse_args()

    tex = strip_comments(a.texfile.read_text(encoding="utf-8", errors="replace"))
    nc = needcites(tex)
    keys = cite_keys(tex)

    problems = 0
    print(f"{len(keys)} distinct \\cite keys, {len(nc)} \\needcite placeholders")

    if nc:
        problems += len(nc)
        print(f"\nBLOCKING — {len(nc)} \\needcite placeholder(s) (download the source, then cite):")
        for n in nc:
            print(f"  [CITE NEEDED: {n}]")

    if not a.sources.exists():
        print(f"\nsources folder '{a.sources}' not found — create it and download every cited work into it.")
        return 1

    mkeys, files = sourced_keys(a.sources)
    print(f"\nsources/: {len(files)} source file(s)"
          + (", MANIFEST.md present" if mkeys else ", no MANIFEST.md (matching by filename)"))
    unsourced = sorted(k for k in keys if not key_has_source(k, mkeys, files))
    if unsourced:
        problems += len(unsourced)
        print(f"\nBLOCKING — {len(unsourced)} cited key(s) with NO source on disk (must not be cited):")
        for k in unsourced:
            print(f"  {k}")
    else:
        print("all cited keys have a source on disk.")

    if problems:
        print(f"\nFAILED: {problems} citation(s) without a downloaded source. "
              "Add them to citations-needed.md and hand to the user.")
        return 1
    print("\nOK: no source missing, no placeholder left.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
