# Phase 6 pass — Positioning and novelty audit

The citation audit verifies references that exist; this pass finds the ones
that are **missing** — the adjacent work a referee will name in the first
review round — and stress-tests the novelty claim before a reviewer does.

## Inputs

The contribution map (or intro contribution bullets), the manuscript's
positioning paragraphs, the current bibliography, and the topic keywords
from the paper profile.

## Procedure

1. **Extract the novelty claim.** State, in one or two sentences per
   contribution, exactly what the paper claims is new. These sentences are
   what the audit attacks.
2. **Multi-modal search sweep** (parallel agents, each blind to the others'
   angle — one search angle never finds everything):
   - keyword search: topic terms + synonyms + the venue register's
     terminology variants
   - citation chasing backward: references-of-references of the paper's
     key sources
   - citation chasing forward: papers citing the key sources since their
     publication
   - author chasing: recent work of the most-adjacent authors (including
     the target author)
   - recency sweep: preprint servers and the venue's own last two years,
     which reviewers know best
3. **Overlap assessment, one agent per candidate.** For each candidate
   paper: what does it actually do (from its abstract/intro, downloaded
   when overlap looks real), and how does it relate to each novelty
   sentence — verdict per candidate: `unrelated` / `should-cite`
   (adjacent, strengthens positioning) / `must-cite` (a referee would call
   its absence a gap) / `novelty-threat` (does part of what we claim as
   new), with quotes as evidence.
4. **Loop until dry**: repeat the sweep with terms learned from round-1
   findings until a round adds nothing.
5. **User triage (STOP).** must-cite and novelty-threat items are decisions,
   not automatic edits. For threats, the resolution is honest
   repositioning — sharpen the contribution wording to what is genuinely
   new relative to the found work, never spin or omission. The found paper
   gets cited and differentiated explicitly.
6. **Insertion.** New citations obey "no source, no cite" (guardrail 11): a
   must-cite paper is added as a verified `\cite` only if its source is in
   `sources/`. A must-cite paper that is gated/unobtainable does NOT get
   cited on faith — it goes on `citations-needed.md` for the user to
   download, with a `\needcite{...}` placeholder at the spot, and the
   differentiating sentence is written once the source arrives.

## Output

`positioning-audit.md` next to the manuscript: the novelty sentences, the
candidate table with verdicts and evidence, the user's rulings, and the
resulting edits. Rerun the pass in Mode C if reviewers name works the sweep
missed — and add the miss to the search-angle list for next time.
