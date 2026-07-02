# Phase 0 & 5 — Tracked, surgical, approval-gated editing

The mechanic that makes AI editing trustworthy to a human supervisor: every
change is visible, scoped, and reversible until a human approves it.

## The two-tier color system

Install `templates/revision-macros.tex` in the preamble — in Mode B at Phase
0; in Mode A at the moment the accepted v0 draft becomes the tracked baseline
(there is no preamble before Phase D). Two tiers:

- **RED** (`\rev{new text}`, `\revdel{deleted text}` → red strikethrough):
  substantive changes — anything touching claims, math-adjacent prose,
  citations, numbers, structure. Red means "not yet checked by the human
  chain"; in a supervised project, red is what the supervisor reviews.
- **YELLOW** (`\yel{new text}`, `\yeldel{deleted text}`): pure writing-style
  changes with zero substantive content. The user pre-reviews yellow; items
  that turn out substantive get escalated to red.

Rules:
- Never unwrap markup ("finalize", "make it black") without an explicit user
  instruction naming the passage.
- Never reuse markup macros from previous revision rounds (e.g. an old no-op
  `\NEW{}`): one round, one live macro set. Retired macros must render as
  plain black text and never be written again.
- **Any change, no matter how small, gets wrapped.** A one-word swap the user
  cannot see is a breach of trust, not a convenience.

## Surgical scope

Each edit touches ONLY the passage under discussion. Do not "improve" earlier
paragraphs in passing, re-wrap lines, reformat whitespace, or restyle
neighboring sentences. Scope creep was the most-corrected AI failure in the
source project; the user must never discover an unrequested change.

## The per-passage loop

1. **Verify before editing.** Read the passage and everything it depends on:
   the original draft (if restyling), the relevant equations and appendix
   proofs, the plots/code behind any numeric claim, and the relevant
   style-guide section. If the passage's substance is wrong (inequality
   direction, misstated proposition, unsupported claim), fix substance first
   (red) before touching style.
2. Propose the wrapped edit. State in one line what changed and why.
3. **STOP for approval.** The user approves ("do it"), rejects, or refines.
   Batched proposals get itemized verdicts ("R3 remove, R4 keep, R5 trim");
   apply exactly the verdicts, nothing more.
4. **Recompile and visually confirm** the PDF actually shows the change.
   Reporting "done" from a .tex diff without a recompile caused repeated
   trust damage. If a watcher auto-commits the PDF, the PDF must be the
   freshly compiled one.
5. **Commit** `paper.tex` + `paper.pdf` with a message naming the passage.
   One discrete edit (or one section pass) per commit; never batch.

## Canonical-file policy

One manuscript, one location, one branch. No scratch copies of the paper in
temp directories, no parallel "experimental" versions. If a holistic preview
is needed (see below), it is generated FROM the canonical file and clearly
named as a derived artifact.

## Accept-all preview build

When many tracked cuts have accumulated, generate a derived
`paper-no-cuts.tex/.pdf` in which all proposed edits are applied cleanly, so
the user can read the would-be-final text and then approve/revert each cut in
the canonical marked-up file. Never let the preview replace the canonical
file.

## Multi-agent write discipline

If multiple agents edit the manuscript concurrently, partition by section and
never let two agents hold the same file region; serialize commits. Safer
default: agents propose patches, one orchestrator applies them sequentially.

## Auto-commit watcher (optional)

A file watcher that commits `paper.{tex,pdf}` on every change gives
fine-grained history when several agents work. Two caveats from experience:
the watcher does NOT compile (compiling stays the editor's job), and pushing
requires credentials to be cached once manually.
