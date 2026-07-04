# Phase 6 — Citation audit (download-and-verify)

Silent citation error was the single most serious failure class found in the
source project: a substantial fraction of the bibliography was wrong,
including a fabricated paper and a nonexistent journal article. Bib-file
well-formedness catches none of this. The only reliable audit reads the
actual source.

## Procedure

1. **Extract** every `\cite` key and its bib entry; build an audit manifest
   (key, claimed authors/title/venue/year, the sentence(s) in the manuscript
   that cite it, and what the sentence attributes to the source).
2. **Download every cited work** into `citation_audit/` — publisher page,
   arXiv, author homepage, library. Books: obtain the relevant chapter or a
   reliable secondary confirmation of the exact claim + edition/year. Record
   anything unobtainable as UNVERIFIED (a finding, not a pass).
3. **One checker agent per reference** (cheap model, parallel fleet). Each
   agent receives the PDF and the citing sentences and answers:
   - Does the work exist as described (authors, title, venue, year, pages)?
   - Does it actually contain/support what our sentence attributes to it?
   - Is the attribution original to this work (or are we crediting a survey
     for another author's result, or misattributing a coinage)?
4. **Findings report**, one line per reference: OK / metadata-wrong (with
   correction) / claim-unsupported (with what the source actually says) /
   fabricated / unverifiable.
5. **Fixes as red edits**: bib corrections and any prose changes where the
   cited source does not support the sentence. User approves each.

## Failure taxonomy to check against (all observed in a single real bibliography)

- fabricated reference (paper does not exist)
- wrong title/pages on a real paper
- wrong author list (right result, different authors' paper)
- wrong year
- nonexistent venue (preprint cited as a journal article)
- misattributed coinage (term credited to a book that quotes someone else)

## The sources folder and the "no source, no cite" rule

Every cited work has its PDF/source in the project's `sources/` folder, one
file per bib key (a `sources/MANIFEST.md` maps key → filename). This is a
**hard rule for all writing phases**: a `\cite` may be typeset only when its
source is on disk. Never cite from memory, a search snippet, or a DOI alone —
that is how fabrications and misattributions enter (see the failure taxonomy
above).

**Gated / unobtainable papers → hand them to the user, do not cite on faith.**
When a paper must be cited but cannot be downloaded (paywall, no institutional
access, book, unavailable preprint):

1. Do NOT emit a real `\cite`. Put `\needcite{key — what it should support}`
   at the spot; it renders conspicuously and greps to zero before submission.
2. Add a row to `citations-needed.md`
   (`templates/citations-needed-template.md`): title, authors, venue, year,
   DOI/URL, the claim it supports, and why it is needed.
3. Present the list to the user and ask them to download the sources into
   `sources/`. Only once the file is present is the `\needcite` replaced with
   a verified `\cite`.

Both the citation audit (existing cites) and the positioning/novelty audit
(proposed new cites) feed the same `citations-needed.md` queue. Run
`scripts/check_citations.py` to flag any `\needcite` left in the manuscript
and any `\cite` key with no matching source file.
