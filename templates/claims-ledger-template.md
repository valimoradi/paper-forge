# Claims ledger — <PAPER>

One row per number, figure, table, or empirical claim that appears in the
manuscript. A claim may be typeset only if its row exists and its artifact
was regenerated (not remembered). When analysis changes, stale rows identify
exactly which paper text must be re-verified.

Status: VERIFIED (regenerated this phase) / STALE (upstream changed) /
PENDING (not yet regenerated) / DROPPED.

| ID | Claim in paper (quote or figure/table ref) | Metric/quantity | Value | Generating script | Input data | Output artifact | Commit | Verified (date, by) | Status |
|----|--------------------------------------------|-----------------|-------|-------------------|------------|-----------------|--------|---------------------|--------|
| C1 | | | | | | | | | |

## Comparison protocol (applies to all rows)

- splits/seeds:
- preprocessing shared across methods:
- leakage audit: every derived constant traced to training data only (date, by):
- aggregation convention (per-instance → mean? pooled?):

## Pre-submission reproducibility run

Date: — rerun every generating script from a clean checkout; confirm each
output matches the paper (checksum or exact values). Mismatches block
submission.

| ID | Regenerated value | Matches paper | Note |
|----|-------------------|---------------|------|
