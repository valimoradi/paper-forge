# Phases 4 & 6 — Agent roster and quality passes

Every pass is a named, separate sweep with its own findings report. Findings
enter the manuscript only as tracked red/yellow edits awaiting approval —
agents never finalize.

## Model policy

Reading/checking agents run on a cheaper model (the source project mandated
Sonnet for every sub-agent); the orchestrator synthesizes. Confirm the policy
with the user in Phase 4 and record it. Sequential passes (paragraph →
chapter → whole paper) caught different error classes than one big parallel
sweep; use both: parallel fleets for coverage sweeps, sequential escalation
for depth.

## The roster

Prompt templates in `templates/agent-prompts.md`.

1. **Author persona (writer).** Rewrites passages per the approved style
   guide. Bound by the concision gate and fidelity guardrails (math, numbers,
   citations, labels byte-identical).
2. **Supervisor persona (precision critic).** Modeled on the word-sensitive
   co-author/supervisor: challenges every word choice ("why this term rather
   than the field's standard one?"), flags overstatement, understatement,
   invented terminology, unattributed known results, newspaper phrasing.
   Reads passage by passage; never skims.
3. **Venue reviewer (adversarial).** A referee for the target venue. Produces
   a numbered "Still Problematic" list covering positioning, manuscript
   hygiene, overclaiming, terminology precision, abstract-vs-contribution
   consistency. **Iterate rounds until a round returns nothing new** (2–3+
   rounds is normal); a single pass always under-finds.
4. **Conciseness pipeline (4 chained single-purpose agents), per section:**
   a. *Cutter* — trims toward the venue-profile word target.
   b. *Fidelity verifier* — diffs cut vs. pre-cut (and vs. the original
      draft, if restyling): confirms no content, claim, or qualifier was lost.
   c. *Style checker* — confirms the cut text still complies with the
      author style guide.
   d. *Structure checker* — confirms venue-structure compliance.
   Commit after each section clears the chain. The verbosity standard: "text
   was verbose if the topic can be explained without any loss of context in
   fewer words." Cutting purely to hit a number is as forbidden as padding.
5. **Coherence/notation sweeper.** Whole-paper passes checking: every symbol
   has one consistent meaning; conventions (e.g. ε*, β*) used identically in
   every section; no redefinition of already-introduced objects; cross-refs
   resolve; main-text statements of propositions match their appendix proofs
   **including inequality directions** (check the proof, not the prose).
6. **Claims-vs-evidence auditor.** For every empirical sentence: locate the
   number/figure/code output that supports it. Flags (a) claims with no
   artifact behind them, (b) claims stronger than the artifact ("real-world
   data" when the data is simulated; "intractable" when merely hard),
   (c) editorializing words a referee can attack (hype adverbs, vivid
   metaphors). Every added word is attack surface.
7. **Figure integrity verifier.** Regenerates figures from the actual
   generating code; confirms the committed figure = the regenerated one
   (byte/md5 where possible); checks cross-figure consistency (two figures
   implying contradictory magnitudes is a finding); checks figure claims in
   prose against the plotted data. **Never narrate a figure from memory of
   the code — render it and look.**
8. **Math-vs-source verifier** (for methods papers): checks that the paper's
   stated formulation matches the implementation, and that any reimplemented
   baseline matches the cited method as published — adversarial persona
   ("assume the cited method's authors will read our code").
9. **Citation auditor.** Separate pass, own reference:
   `06-citation-audit.md`.
10. **Positioning/novelty scout.** Finds MISSING citations and novelty
    threats before a referee does — multi-modal literature sweep, overlap
    verdicts, user triage. Own reference: `positioning-audit.md`.
11. **Proof auditor + adversary** (theory papers). Line-by-line proof
    audits and a prover/adversary loop for contested proofs. Own reference:
    `proof-rigor.md`. The one pass where a stronger model is usually worth
    it (confirm with the user).

## Recommended Phase-6 order

1. Coherence/notation sweep (cheap, unblocks everything else)
2. Proof rigor (theory papers — before prose polish, since repairs change
   prose)
3. Conciseness pipeline, section by section
4. Positioning/novelty audit (before reviewer rounds, so positioning fixes
   land first)
5. Adversarial reviewer rounds, until dry
6. Citation audit (after prose is stable, so cites do not churn)
7. Figure integrity + claims-vs-evidence (last, against the near-final text)

## Granularity pattern

Run persona critics at three granularities — paragraph, section, whole paper —
sequentially. Paragraph-level catches word choice; section-level catches
redundancy and flow; whole-paper catches positioning and consistency. Each
granularity produces its own findings report.
