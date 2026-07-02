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

## Standing rule for all writing phases

Never add a citation during drafting without verifying it against a
downloaded source at insertion time. "I remember this paper" is how
fabrications enter. If the source cannot be obtained now, mark the spot with
a TODO macro and list it as unverified — do not typeset a guess.
