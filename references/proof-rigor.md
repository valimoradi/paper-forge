# Phase 6 pass — Proof rigor (theory papers)

For manuscripts with theorems, propositions, or lemmas. The coherence sweep
checks that statements match their proofs; this pass checks that the proofs
are actually correct. It exists because a supervised real project found
multiple proof errors that earlier casual readings had missed.

## Per-proof audit (one agent per proof)

The auditor walks the proof line by line and, for every step, answers:
what justifies this step (a named assumption, a previously proved result, a
standard cited theorem, or algebra it re-derives itself)? Flags:

- **leaps**: steps asserted without justification ("it is easy to see" is
  allowed only when the step is one named manipulation the auditor can
  perform)
- inequality directions and sign errors, checked by re-derivation, not by
  reading
- quantifier order and variable scope; symbols used before definition
- boundary and degenerate cases (empty sets, zero denominators, equality
  cases of strict inequalities, limits at the domain edge)
- circularity (using the result being proved, or a later result)
- **unused assumptions** (either the statement is stronger than needed or
  the proof is wrong) and untracked constants

Verdict per step: JUSTIFIED / GAP (with what is missing) / ERROR (with the
counter-derivation).

## Adversary loop (for any proof with a GAP/ERROR, or that the user
distrusts)

Two agents alternate: the **adversary** tries to break the proof — construct
a counterexample to the claim or to an intermediate step, or exhibit an
instance where a "clearly" fails; the **prover** repairs. Iterate until the
adversary concedes with a written reason per prior objection, or a genuine
flaw survives — which is escalated to the user, never patched silently.

## Repair rules

- Never silently "fix" mathematics: every repair is a red edit the user
  approves, checked against everything downstream that uses the result.
- If a claim cannot be repaired, it is weakened to what is provable or
  removed — the calibration guardrail applies to theorems exactly as to
  empirical claims.
- Known results used in proofs are named and cited (never presented as
  original), and their hypotheses verified to actually hold in our setting.

## Statement hygiene (whole-paper, after per-proof audits)

- Main-text statement and appendix statement byte-identical; numbering
  consistent; every assumption stated is referenced by at least one proof.
- The dependency graph of results is acyclic and matches presentation
  order.
- Notation in proofs matches the manuscript's symbol table.

## Model policy exception

This is the one pass where spending a stronger model is usually justified —
confirm with the user. Findings enter the manuscript as red edits like every
other pass.
