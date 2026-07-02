---
name: paper-forge
description: >
  End-to-end, agent-assisted academic paper writing pipeline: select a target
  venue, harvest its norms from real published papers, emulate a target
  author's style from a downloaded corpus, harden the empirical results
  (metric selection, baseline fidelity, leakage audit, script-generated
  figures, a claims ledger tracing every number to code + data + commit),
  write the main draft from research artifacts or restyle an existing one,
  then polish through tracked (red/yellow) surgical edits, persona reviewer
  agents, and systematic quality passes (conciseness, coherence, citation
  audit, figure integrity, journal compliance). Use when the user wants to
  write a paper from their data/code/results, rewrite or submission-harden a
  draft, emulate a specific author's or venue's style, audit citations or
  baselines, or run reviewer-style audits on a manuscript.
---

# paper-forge — venue-targeted, author-emulating paper writing

A systematized pipeline distilled from a real, month-long, supervised journal
submission project. Every rule below exists because its absence caused a
concrete failure in that project.

## The two laws (read first)

1. **Nothing becomes permanent without human approval.** Every change to the
   manuscript is wrapped in visible tracked markup (red = substantive, yellow =
   style-only) and stays wrapped until the user explicitly approves it. See
   `references/04-tracked-edits.md`.
2. **Never state what has not been verified.** No added claims, no invented
   citations, no narrated figure descriptions, no "results show" without
   re-running the code or reading the source. Claims are calibrated exactly to
   the evidence: no overstatement, no understatement. See
   `references/guardrails.md` — these are hard rules, not suggestions.

## Pipeline overview

Start with the intake interview (`references/00-intake.md`): it selects
**Mode A** (no draft yet — write the main draft from research artifacts;
inserts phases R and D) or **Mode B** (existing draft — restyle/harden;
phase R runs in audit-only form). Then run the phases in order. Each phase
ends with a user checkpoint (STOP and get approval) before the next begins.
Phases 1–4 are setup and typically run once; phases 5–7 loop.

| Phase | What happens | Reference | Checkpoint |
|-------|--------------|-----------|------------|
| –1 | Intake interview; mode selection; paper profile | `00-intake.md` | user confirms mode + profile |
| 0 | Repo, branch, canonical file, revision macros, auto-commit | `04-tracked-edits.md` | branch + macros confirmed |
| 1 | Venue selection; venue profile (structure) + venue register (how the journal writes) from real recent papers + author guidelines | `01-venue-profile.md` | user confirms profile + register |
| 2 | Target author / exemplar paper; download the author corpus | `02-corpus.md` | user approves corpus list |
| 3 | Build the corpus-grounded style guide (verbatim, page-cited) | `03-style-guide.md` | user approves style guide |
| 4 | Define the agent roster (personas, checkers) | `05-review-passes.md` | user confirms roster + model policy |
| R | Data analysis & results hardening: metric spine, baselines, leakage audit, figures, claims ledger (Mode A full; Mode B audit-only) | `data-analysis.md` | user approves ledger + interpretation |
| D | Mode A only: contribution map, skeleton from exemplar, evidence-first v0 draft | `drafting.md` | per-section v0 acceptance |
| 5 | Section-by-section drafting/restyling loop, tracked + surgical | `04-tracked-edits.md` | per-passage approval ("do it") |
| 6 | Quality passes: conciseness, coherence, citations, figures, adversarial review | `05-review-passes.md`, `06-citation-audit.md` | per-pass findings approved as red edits |
| 7 | Journal-compliance check against the venue profile | `07-journal-compliance.md` | compliance checklist signed off |
| 8 | Bake markup, submission hygiene, final compile | `07-journal-compliance.md` | user says "bake" |

## Phase 0 — Setup

- One canonical manuscript location, one branch. Never create throwaway copies
  of the paper in temp directories; all work happens on the canonical file.
- **Mode B**: commit the current draft as-is, then create a dedicated branch
  (e.g. `restyle-<author>`). Install the revision macros
  (`templates/revision-macros.tex`) in the preamble now — tracked markup
  applies from the very first edit.
- **Mode A**: create the paper directory, repo, and working branch now; the
  manuscript itself does not exist until Phase D. Install the revision macros
  at the moment the accepted v0 becomes the tracked baseline (per
  `00-intake.md`), not before.
- Cadence rule for the whole project, both modes: after every discrete edit,
  **compile first, then commit** `paper.tex` + `paper.pdf`. Never batch
  several sections into one diff. Optionally install a file-watcher auto-commit daemon
  (`templates/auto-commit-watcher.md`), but remember the watcher does not
  compile; compiling is your job before reporting done.

## Phase 1 — Venue profile and venue register

Ask the user for the target venue (and any secondary venue, e.g. a conference
presentation of the same work). Then build two evidence-based artifacts from
5–10 recent, well-regarded papers plus the official author guidelines:

1. **Venue profile** (structure): *measured* norms — abstract length, intro
   length, related-work placement, proof placement, section skeleton, claim
   register. Skeleton: `templates/venue-profile-template.md`.
2. **Venue register** (style): how papers in this journal are actually
   written — its working vocabulary (which verbs introduce contributions and
   state results, counted across the corpus), voice and tense conventions,
   preferred terminology, hedging norms, and a verbatim page-cited phrase
   bank. Skeleton: `templates/venue-register-template.md`.

Do not work from remembered "journal style" folklore; measure real papers.
Full procedure in `references/01-venue-profile.md`.

## Phase 2 — Target author corpus

Ask the user to name an author (or a specific exemplar paper) whose style the
manuscript should resemble. Optionally a second anchor author for a different
dimension (the original project used "accessible like author A, precise like
author B" — the tension between them is a feature). Download 4–6 papers by
the target author, preferring papers published in the target venue. Present
the list (title, venue, year, file path) and STOP for approval before using
it. Procedure in `references/02-corpus.md`.

## Phase 3 — Author style guide (Layer 3 of the style stack)

From the approved corpus, build a corpus-grounded style guide: ~12 analysis
dimensions, each dimension gets one imperative rule backed by 2–8 **verbatim,
page-cited quotes** from the corpus. Never paraphrase the evidence. The
manuscript's prose is governed by a three-layer stack, all always in force:
Layer 1 = the bundled academic base (`references/academic-register.md`:
formal register + anti-AI-tell hard bans), Layer 2 = the venue register
(Phase 1), Layer 3 = this author guide. On conflict: venue beats author;
both override the base only with verbatim corpus evidence. Procedure and
dimension list in `references/03-style-guide.md`, skeleton in
`templates/style-guide-template.md`.

## Phase 4 — Agent roster

Define the reviewer/writer agents before drafting. Standard roster (prompt
templates in `templates/agent-prompts.md`):

- **Author persona** — writes/rewrites in the target style.
- **Supervisor persona** — word-precision critic; hates overstatement and
  newspaper phrasing; reads passage by passage, never skims.
- **Venue reviewer** — adversarial peer reviewer for the target journal;
  produces numbered "still problematic" lists, iterated until dry.
- **Conciseness pipeline** — 4 chained single-purpose agents:
  cut → fidelity-verify (nothing lost vs. pre-cut) → style-check → structure-check.
- **Citation auditor** — download-and-verify, one agent per reference.
- **Figure/claims verifier** — regenerates plots from code; checks every
  numeric claim in prose against actual outputs.

Model policy: checking/reading agents run on a cheaper model (the original
project mandated Sonnet for all sub-agents); synthesis can use a stronger one
if the user allows. Confirm the policy with the user.

## Phase R — Data analysis and results hardening

For any paper with empirical content. Before results prose exists: inventory
the user's data/code, fix one primary metric used consistently everywhere,
implement baselines faithfully to their cited sources, audit for leakage,
generate every figure/table from committed scripts, and fill the **claims
ledger** (`templates/claims-ledger-template.md`) — one row per number/figure
mapping it to its generating script, data, output, and commit. A sentence may
be typeset only if its ledger row was regenerated, not remembered. Ends with
an interpretation gate: agents report what the numbers show; what they *mean*
is decided with the user. Full procedure: `references/data-analysis.md`.

## Phase D — Skeleton and first draft (Mode A)

Contribution map (3–4 bullets, each backed by ledger rows or theorems; user
approves) → skeleton diffed against the venue exemplar with per-section word
budgets → draft in evidence-first order (methods → results → related work →
intro → abstract last). v0 is written plainly; once the user accepts it as
baseline, the tracked-edit law governs everything after. Full procedure:
`references/drafting.md`.

## Phase 5 — Drafting / restyling loop

Strictly sequential, section by section (§1 → §2 → … → appendix). Per passage:

1. Read the passage plus everything it depends on (the math, the appendix
   proof, the original draft if this is a restyle, the relevant style-guide
   section).
2. Verify before editing: check the passage's claims against plots, code,
   appendix. Fix substance (red) before style (yellow).
3. Propose the edit wrapped in tracked markup, touching **only** the passage
   under discussion.
4. STOP. User approves ("do it"), rejects, or refines. Only then finalize,
   recompile, visually confirm the PDF changed, commit.
5. After every few sections, run a joint-consistency sweep across finalized
   sections (notation, symbols, cross-references) before moving forward.

## Phase 6 — Quality passes

Run each as a separate, named pass with its own findings report; every
proposed fix enters the manuscript as a red edit awaiting approval. Order that
worked: coherence/notation → conciseness → adversarial review rounds (repeat
until a round produces nothing new) → citation audit → figure integrity.
Details and prompts in `references/05-review-passes.md` and
`references/06-citation-audit.md`.

## Phases 7–8 — Compliance and bake

Check the manuscript against the Phase-1 venue profile and the official author
guidelines (structure, lengths, reference style, data/code policy,
anonymization). Only after the user signs off: strip all revision macros,
grep-verify **zero** leftover markers (count them; "mostly clean" is not
clean), final compile, final commit. `references/07-journal-compliance.md`.

## Working style

- When the user critiques a word or sentence, the critique generalizes: add it
  to the project's guardrail list so no agent reintroduces it.
- Prefer showing over telling: regenerate the figure, paste the word count,
  quote the source paper. The user will check; be checkable.
- If two style authorities conflict (author guide vs. venue register), the
  venue wins. If accessibility conflicts with concision, concision wins:
  a more understandable paper is usually a shorter one.
