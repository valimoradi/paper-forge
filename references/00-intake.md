# Phase –1 — Intake interview and mode selection

Run this before anything else. Ten minutes of questions prevents building the
wrong pipeline.

## Questions to ask the user

1. **Venue**: target journal/conference? Secondary venue? (→ Phase 1)
2. **Draft status**: is there an existing draft, are we writing from
   research artifacts (code, data, results, notes) — or has the paper been
   submitted and referee reports arrived (→ Mode C)?
3. **Results status**: are the experiments finished and trusted? Are there
   numbers/figures the user considers final, or does analysis still need to
   run? **Writing never proceeds on top of unverified numbers.**
4. **Data & code**: where do the data, experiment code, and result files
   live? Can the assistant execute the code? Which environment?
5. **Paper type**: methods/theory (proofs), empirical/data-driven
   (experiments, comparisons), or both? This decides whether the
   math-vs-source verifier or the data-analysis phase carries more weight.
6. **Supervision chain**: is there a supervisor/co-author who reviews
   changes? If yes, tracked red/yellow markup is mandatory from day one. If
   the user is sole author, tracked markup starts after the v0 draft is
   approved (see modes below).
7. **Target author**: whose style to emulate (or an exemplar paper)? Second
   anchor? (→ Phase 2)
8. **Toolchain**: LaTeX (assumed default)? Word and Markdown are supported
   with adapted mechanics — see `references/toolchains.md` for the mapping
   (tracked edits, bake, and gate checks per toolchain).
9. **Constraints**: deadline, page limit, double-blind, model policy for
   sub-agents.

Record answers in `paper-profile.md` in the paper's working directory, using
`templates/paper-profile-template.md` (Mode A: create the working directory
now; the manuscript joins it in Phase D).

## Mode A — new paper from research artifacts

For users with results but no draft. Phase order:

```
–1 Intake → 0 Setup → 1 Venue → 2 Corpus → 3 Style guide → 4 Roster
→ R  Data analysis & results hardening   (references/data-analysis.md)
→ D  Skeleton & first draft              (references/drafting.md)
→ 5 Tracked-edit loop → 6 Quality passes → 7 Compliance → 8 Bake
```

Markup rule for Mode A: the v0 draft is written plainly (wrapping an entirely
new document in red is noise). The moment the user reads and accepts v0 as
the working baseline, it becomes "black" and every subsequent change follows
the tracked-edit law.

## Mode B — existing draft (restyle / harden / submission-prep)

The original pipeline as documented: phases 0–8 in order, tracked markup from
the very first edit. If the draft contains empirical claims, run Phase R in
audit-only form (claims ledger + verification, no new analysis) before
Phase 5, so prose is never polished on top of numbers that will change.

## Mode C — revision after referee reports

For papers already submitted, when the decision letter arrives. Skips
straight to the revision loop (`references/revision-mode.md`): issue ledger
from the reports → user triage → tracked fixes (new-experiment requests
route through Phase R) → point-by-point response letter → post-fix
consistency sweep → resubmission package. Phase-1/2/3 artifacts (venue
profile, register, style guides, claims ledger) are reused from the original
submission; rebuild them only if the resubmission targets a different
journal.

## Readiness gate (Modes A and B)

Do not enter Phase 5 (prose work) until:
- [ ] every number destined for the paper has a generating artifact
      (script + output) the assistant has actually executed or verified
- [ ] the primary metric is fixed and consistent across all experiments
- [ ] the user has approved venue profile, corpus, and style guide
