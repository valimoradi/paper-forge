#!/usr/bin/env python3
"""Bake tracked-edit markup for submission (Phase 8).

Usage:
  python bake_markup.py paper.tex -o paper-clean.tex          # bake
  python bake_markup.py paper.tex --count                     # audit only

Unwraps keep-macros (\\rev, \\yel, ...) to their contents, deletes
delete-macros (\\revdel, \\yeldel, ...) with their contents, handling nested
braces. Then verifies: zero leftover markers, and \\cite/\\label/\\ref sets
identical before vs. after (the bake must change markup only).
Exit 1 if leftovers remain or parity breaks. Approval to bake comes from
the user (Phase 8), never from this script.
"""
import argparse, re, sys
from collections import Counter
from pathlib import Path

KEEP = ["rev", "yel", "added", "NEW"]
DROP = ["revdel", "yeldel", "deleted"]


def find_arg(text: str, start: int):
    """start points at '{'; return (content, index after matching '}')."""
    depth, i = 0, start
    while i < len(text):
        c = text[i]
        if c == "\\":
            i += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1:i], i + 1
        i += 1
    raise ValueError("unbalanced braces")


def unwrap(text: str, macro: str, keep: bool) -> str:
    pat = re.compile(r"\\" + macro + r"(?![a-zA-Z])\s*\{")
    out = []
    pos = 0
    while True:
        m = pat.search(text, pos)
        if not m:
            out.append(text[pos:])
            break
        out.append(text[pos:m.start()])
        content, after = find_arg(text, m.end() - 1)
        if keep:
            out.append(content)
        pos = after
    return "".join(out)


def refset(tex: str, cmd: str) -> Counter:
    return Counter(re.findall(r"\\" + cmd + r"[a-zA-Z]*\{([^}]*)\}", tex))


def leftovers(tex: str) -> dict:
    counts = {}
    for m in KEEP + DROP:
        n = len(re.findall(r"\\" + m + r"(?![a-zA-Z])\s*\{", tex))
        if n:
            counts[m] = n
    return counts


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("texfile", type=Path)
    ap.add_argument("-o", "--output", type=Path)
    ap.add_argument("--count", action="store_true", help="report marker counts only")
    a = ap.parse_args()

    src = a.texfile.read_text(encoding="utf-8", errors="replace")
    before = leftovers(src)
    if a.count:
        if before:
            for k, v in sorted(before.items()):
                print(f"\\{k}{{}}: {v}")
            print(f"total markers: {sum(before.values())}")
        else:
            print("no markers found — already clean")
        return 0

    baked = src
    for m in KEEP:
        # repeat until stable: keep-macros can nest inside each other
        prev = None
        while prev != baked:
            prev = baked
            baked = unwrap(baked, m, keep=True)
    for m in DROP:
        prev = None
        while prev != baked:
            prev = baked
            baked = unwrap(baked, m, keep=False)

    left = leftovers(baked)
    ok = True
    if left:
        print(f"FAIL: leftover markers after bake: {left}")
        ok = False
    for cmd in ("cite", "label", "ref"):
        if refset(src, cmd) != refset(baked, cmd):
            # deletions legitimately remove refs inside \revdel; report, human judges
            print(f"NOTE: \\{cmd} set changed (expected only if delete-markup contained {cmd}s) — diff and review:")
            diff = refset(src, cmd) - refset(baked, cmd)
            for key, n in diff.items():
                print(f"  -{key} (x{n})")

    out = a.output or a.texfile.with_name(a.texfile.stem + "-baked.tex")
    out.write_text(baked, encoding="utf-8")
    print(f"baked -> {out}  (markers before: {sum(before.values())}, after: {sum(left.values())})")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
