# Phase D — Skeleton and first draft (Mode A)

Writing a main draft from research artifacts, after Phase R has hardened the
results. Prose is assembled around verified claims, never the reverse.

## D1. Contribution map (before any prose)

With the user, write 3–4 contribution bullets in the venue's register
(parallel verbs, scope-bounded). For each contribution, list the evidence
that supports it — claims-ledger rows, theorems, propositions. A contribution
without evidence is cut or demoted; validation work is not a contribution.
The user approves this map; it is the paper's spine and the abstract's
outline.

## D2. Skeleton from the exemplar

Build the section skeleton by diffing against the Phase-1 structural exemplar
(the one real paper chosen from the venue corpus): same top-level structure,
related-work placement, proof/appendix split, and the body-vs-appendix triage
decided in Phase 1. Write one-line section briefs: what each section must
establish, its word budget (venue medians), and which contributions it
carries. User approves the skeleton.

## D3. Drafting order

Draft in evidence-first order, not reading order:

1. **Methods/model** — closest to the verified artifacts, anchors notation.
2. **Results** — each empirical sentence cites a claims-ledger row; numbers
   are pasted from regenerated outputs, never typed from memory.
3. **Related work / positioning** — only with verified citations in hand
   (the citation rule applies at insertion time, not audit time).
4. **Introduction** — written against the contribution map, to the venue's
   measured intro budget.
5. **Abstract** — last, contribution-first, to the venue's measured length.
6. Conclusion/limitations; title candidates for the user to pick.

Each section: author persona drafts per the style guide → concision gate →
present to user → revise → user accepts → commit. Plain text in v0 (no
tracked markup yet); the accepted v0 becomes the black baseline and every
later change follows the tracked-edit law.

## D4. Drafting rules

- **No invented anything.** No citations from memory (verify at insertion or
  leave a `\todo{cite: ...}`), no numbers not in the ledger, no claims about
  figures not rendered and looked at.
- Notation introduced once, plain English before symbols, and recorded in a
  running symbol table (seeds the Phase-6 coherence sweep).
- Proofs go to the appendix as they are written; the main text carries the
  statement plus the intuition sandwich, nothing more.
- Every paragraph must serve a section brief; a paragraph that serves none is
  cut now, not in Phase 6.
- Hedge exactly to the evidence: the ledger row's scope is the claim's scope
  ("on N instances from X", not "in general").

## D5. Exit to Phase 5

When all sections have an accepted v0: run one whole-paper read for flow,
then enter the standard tracked-edit loop (Phase 5) and quality passes
(Phase 6) exactly as in Mode B. The citation audit still runs in full — the
insertion-time rule reduces its findings; it does not replace it.
