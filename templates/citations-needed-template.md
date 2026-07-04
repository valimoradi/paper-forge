# Citations needed — <PAPER>

Papers the manuscript must cite but whose source is NOT yet in `sources/`
(gated, paywalled, book, or otherwise undownloadable by the assistant).
**Nothing here may be cited with a real `\cite` until its source lands in
`sources/`** — the spot holds a `\needcite{...}` placeholder meanwhile.

Fed by the citation audit (existing cites lacking a source) and the
positioning/novelty audit (proposed must-cites). Hand this list to the user
and ask them to download each into `sources/`.

| bib key | Title | Authors | Venue / Year | DOI / URL | Supports which claim (§/line) | Why needed | Status |
|---------|-------|---------|--------------|-----------|-------------------------------|------------|--------|
| smith2019 | | | | | | must-cite / should-cite / novelty-threat | NEEDS DOWNLOAD |

Status: NEEDS DOWNLOAD → (user provides file to `sources/`) → DOWNLOADED →
(verified + `\needcite` replaced with `\cite`) → RESOLVED.

Before submission this file is empty or every row is RESOLVED, and
`scripts/check_citations.py` reports zero `\needcite` and zero unsourced
`\cite` keys.
