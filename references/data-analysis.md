# Phase R — Data analysis and results hardening

For data-related papers: produce the results the paper will report, in a form
where every number and figure is regenerable, comparable, and defensible.
Runs before any results prose is written (Mode A) or as an audit of claimed
results (Mode B). The source project's worst weeks came from writing on top
of numbers that later changed; this phase exists to prevent that.

## Audit-only mode (Mode B — draft already exists)

When the draft is written, Phase R does not produce new analysis; it verifies
what the draft already claims. Procedure:

1. Extract every number, figure, table, and empirical claim from the draft
   into the claims ledger (`templates/claims-ledger-template.md`), one row
   each, status PENDING.
2. For each row, locate the generating artifact and **regenerate it**. Mark
   VERIFIED (matches the draft), STALE (regenerates to a different value —
   the draft text is now wrong until fixed as a red edit), or ORPHAN (no
   script regenerates it — the claim is blocked until one does).
3. Run R2 as a consistency check: is one primary metric used identically in
   every section (same definition, normalization, aggregation)?
4. Run R3 as an audit: baseline implementations diffed against their cited
   sources (math-vs-source verifier persona); leakage audit of every derived
   constant.
5. Run R4's checks (cross-figure consistency, stale plot ranges, misleading
   axes) on the existing figures.
6. Skip R6 unless verification contradicts the draft's story — then STOP and
   resolve with the user before any further prose work.

Sections R1–R6 below are the full procedure for Mode A (results not yet
assembled).

## R1. Inventory

Agents sweep the user's data/code and produce an inventory the user confirms:
datasets (source, size, splits, provenance — measured vs. simulated vs.
model-generated: this wording ends up in the paper's claims), experiment
scripts and what each produces, existing result files and which script made
them, and orphan results (files no current script regenerates — these are
findings; they cannot be cited in the paper until regenerable).

## R2. Metric spine

Fix ONE primary metric family reported consistently across every experiment
before any analysis is summarized. Checks learned from experience:

- Does the metric break on edge cases in this data (e.g. percentage errors
  explode on near-zero values)? Pick a metric robust to the data's actual
  range, and keep the intuitive one as supplementary if the field expects it.
- Is the metric computed on the quantity the paper's story is about (the
  decision/output actually observed), not a proxy that flatters the method?
- Same definition, same normalization, same aggregation (per-instance then
  averaged, or pooled?) everywhere. One inconsistent section costs a review
  round.

## R3. Baselines and comparisons

- Every baseline implemented **as published in the cited source** — no
  undisclosed shortcuts or "oracle-assisted" stand-ins. Run the
  math-vs-source verifier persona on each baseline implementation.
- Fair comparison protocol: identical data splits, seeds, preprocessing, and
  compute budget across methods; document it in one place.
- **No leakage**: nothing derived from test data or ground truth may enter
  training, normalization, anchor selection, or hyperparameters. A dedicated
  agent audits every constant in the pipeline and answers "where does this
  number come from?" for each.
- Statistical honesty: if the venue expects significance tests or
  variability, report across seeds/instances (mean ± spread, paired tests
  where paired data exists); never report a single lucky run.
- Ablations/sensitivity where the venue expects them; failed or unresolved
  experiments are excluded from the paper, not narrated.

## R4. Figures and tables, provenance-locked

- Every figure/table is produced by a committed script reading committed (or
  regenerable) result files. No hand-edited numbers, no screenshots.
- Copy step: generated artifacts are copied into the paper's figures
  directory by the script itself, so the paper never shows a stale figure
  (results directories are often gitignored; the paper's copies are not).
- Design rules from hard experience: choose the plot that answers a specific
  reader question (overlaying dozens of curves conveys nothing — use scatter
  vs. a
  reference line or paired bars); never use log/symlog axes where they invert
  the visual message (e.g. apparent curvature); check that hardcoded plot
  ranges still cover the current experiment before every regeneration.
- Cross-figure consistency check: figures showing related quantities must
  imply the same magnitudes; contradictions are analysis bugs, find them now.

## R5. The claims ledger (the phase's deliverable)

Fill `templates/claims-ledger-template.md`: one row per number/figure/claim
destined for the paper → generating script, input data, output file, commit
hash, date, verified-by. Rules:

- A sentence may enter the manuscript only if its row exists and was
  regenerated (not remembered) during this phase.
- When any analysis changes, the ledger says exactly which paper claims are
  stale — re-verify those before further prose work.
- The ledger doubles as the reproducibility manifest: before submission,
  rerun every script and confirm outputs match the paper (checksum or exact
  values).

## R6. Interpretation gate

Summarize findings neutrally (what the numbers show, effect sizes, where the
method loses) and STOP for user discussion before writing the results
narrative. What the results *mean* — the story — is decided with the user,
never inferred by an agent, because overclaiming starts here.
