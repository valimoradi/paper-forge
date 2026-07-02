# Mode C — Revision after referee reports

Papers spend most of their life in revision. Mode C starts when a decision
letter arrives (major/minor revision, or reject-and-resubmit) and ends with
a resubmission package: revised manuscript, marked-changes copy, and a
point-by-point response letter.

## C1. Intake

Collect: the decision letter, every referee report, the journal's revision
rules (deadline, response-letter format/length limits, whether a
marked-changes copy is required), and the exact submitted version (the
pre-bake tagged branch — this is why Phase 8 keeps it forever).

## C2. Issue ledger

Parse every report into a numbered ledger, one row per distinct point
(`templates/response-to-reviewers-template.md`): reviewer, point number,
**verbatim quote**, type (must-fix / clarification / new-experiment request /
disagreement / editorial), affected sections, and — later — disposition,
what changed, and where. Editors' own comments are rows too. Nothing may be
left unanswered: the completeness check at the end is "every row has a
response and every response is true."

## C3. Triage with the user (STOP)

For each row the user decides: **agree** (fix it), **partially agree** (fix
the valid core, rebut the rest), or **rebut** (respond with evidence, no
manuscript change). Agents propose dispositions; the user rules. Requests
for new experiments route back through Phase R — new analysis enters the
claims ledger like any other, and is never faked or approximated to satisfy
a reviewer.

## C4. Fixes as tracked edits

Standard Phase-5 discipline: surgical, tracked, per-passage approval,
compile + commit each. One revision round = one fresh macro set (retire the
previous round's macros as no-ops; never reuse them). The marked-up file
becomes the "changes marked" resubmission copy; baking a clean copy follows
Phase 8 as usual.

## C5. Response letter

One entry per ledger row, in the reviewers' own numbering:

1. Reviewer's point, quoted verbatim (or faithfully condensed if the journal
   caps response length).
2. Response: what was done and why, or the evidence-based rebuttal.
3. Pointer to the change: section/page/line in the *revised* version, with
   the new text quoted when short.

Tone rules: thank reviewers once at the top, not per point; no sycophancy,
no defensiveness; rebuttals cite evidence (a result, a source, a
computation), never authority; if a reviewer misread the paper, the fix is
usually clearer prose, and the response says what was clarified rather than
that the reviewer erred. Claims in the response letter obey the same
guardrails as the manuscript — every stated change must actually exist in
the revision (verify each pointer against the compiled PDF before sending).

## C6. Post-fix consistency sweep

Fixes interact: R1's added assumption can contradict R2's added experiment;
a renamed term must change everywhere. Rerun the coherence/notation sweep
and a one-round venue-reviewer pass over the diff before assembling the
package.

## C7. Resubmission package

Revised clean manuscript (on the official class, hard gates rechecked —
revisions grow and page limits still apply), marked-changes copy, response
letter (within its own length limit if the journal sets one), and any
updated statements. User signs off on the full package.
