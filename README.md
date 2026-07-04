# paper-forge

An agent-assisted academic paper writing pipeline for Claude Code, distilled
from a real, month-long, supervised journal submission project. It systematizes the whole arc: pick a venue, learn the venue
from real papers, emulate a target author from a downloaded corpus, then
draft and harden the manuscript through tracked surgical edits, persona
reviewer agents, and systematic audits — with a human approval gate on every
change.

## What it does

```
Phase –1 Intake: interview → Mode A (write the main draft from research
         artifacts), Mode B (restyle/harden an existing draft), or
         Mode C (revision after referee reports)
Phase 0  Setup: branch, canonical file, tracked-edit macros, commit cadence
Phase 1  Venue: download author guidelines + a stratified corpus — up to 20
         venue papers on the SAME TOPIC as yours (sole source of vocabulary
         and terminology), the venue's top 10 (structure norms), and the 10
         latest (current conventions). MEASURE the structural norms (venue
         profile) AND extract how the journal writes this topic — lexicon,
         voice, phrase bank with verbatim quotes (venue register). Extract
         HARD GATES (max figures/tables, page & abstract limits — budgets
         from day one, never exceeded) and download the official LaTeX
         template; the manuscript is built on it
Phase 2  Author: user names a target author/paper; download 4–6 of their
         papers; user approves the corpus
Phase 3  Author style guide: 12-dimension, corpus-grounded, verbatim
         page-cited rules. Prose is governed by a 3-layer stack:
         academic base (bundled) < venue register < author voice,
         venue winning on conflict
Phase 4  Agent roster: author persona, supervisor persona (precision critic),
         adversarial venue reviewer, 4-agent conciseness pipeline,
         coherence sweeper, claims/figure verifiers, citation auditor
Phase R  Data analysis & results hardening: metric spine, faithful baselines,
         leakage audit, script-generated figures, claims ledger (every number
         in the paper traceable to script + data + commit)
Phase D  (Mode A) Contribution map → skeleton from a venue exemplar →
         evidence-first v0 draft (methods → results → intro → abstract last)
Phase 5  Drafting loop: section by section, every edit wrapped in red/yellow
         markup, surgical scope, per-passage approval, compile + commit each
Phase 6  Quality passes: coherence → proof rigor (theory) → conciseness →
         positioning/novelty audit (find MISSING citations before a referee
         does) → reviewer rounds until dry → citation download-and-verify
         audit → figure integrity
Phase 7  Journal compliance vs. the measured venue profile; hard gates block
Phase 8  Bake (strip markup, grep-verified to zero) + submission package:
         cover letter, blinded copy, statements, suggested reviewers,
         supplements, preprint version
Mode C   Revision loop: referee reports → issue ledger → user triage →
         tracked fixes → point-by-point response letter → resubmission
```

The design principles: nothing becomes permanent without human approval, and
nothing is stated that has not been verified against an artifact (source PDF,
regenerated figure, executed code, appendix proof).

## Install

Clone into your skills directory:

```
git clone https://github.com/valimoradi/paper-forge ~/.claude/skills/paper-forge
```

- Claude Code (user-level): `~/.claude/skills/paper-forge/`
- Project-level: `<repo>/.claude/skills/paper-forge/`

Then just describe your paper task ("help me write/restyle my paper for
<venue>") or invoke the skill directly.

## Layout

```
SKILL.md                       orchestrator playbook (phases, gates, laws)
references/
  00-intake.md                 intake interview, Mode A/B selection
  01-venue-profile.md          venue selection + norm measurement
  02-corpus.md                 target-author corpus acquisition + approval
  03-style-guide.md            corpus-grounded style-guide construction
  04-tracked-edits.md          red/yellow markup, surgical scope, cadence
  05-review-passes.md          agent roster + quality passes
  06-citation-audit.md         download-and-verify citation audit
  07-journal-compliance.md     compliance checklist + submission bake
  academic-register.md         Layer 1: formal register + anti-AI-tell bans
  data-analysis.md             Phase R: results hardening + claims ledger
  drafting.md                  Phase D: contribution map, skeleton, v0 draft
  positioning-audit.md         novelty threats + missing-citation sweep
  proof-rigor.md               line-by-line proof audits + adversary loop
  revision-mode.md             Mode C: referee reports → response letter
  submission-package.md        cover letter, statements, reviewers, preprint
  toolchains.md                Word/Markdown mechanics mapping
  extras.md                    titles/abstracts, co-authors, talk handoff
  guardrails.md                hard rules from observed AI failures
scripts/
  check_gates.py               hard-gate counts (figures/tables/abstract/pages)
  count_words.py               per-section word budgets
  bake_markup.py               Phase-8 bake + zero-leftover + cite parity
  check_register.py            Layer-1 grep checks
  check_headers.py             run-in-header density + "Discussion"-label idiom
  check_citations.py           no source on disk, no \cite (+ \needcite flags)
templates/
  revision-macros.tex          \rev/\revdel/\yel/\yeldel LaTeX macros
  claims-ledger-template.md    number/figure → script/data/commit provenance
  paper-profile-template.md    intake answers + readiness gate
  venue-register-template.md   the journal's vocabulary/voice/phrase bank
  applied-style-guide-template.md  short per-manuscript style distillation
  response-to-reviewers-template.md  Mode C issue ledger + letter skeleton
  citations-needed-template.md   download queue for gated/unsourced cites
  venue-profile-template.md    skeleton for the measured venue profile
  style-guide-template.md      skeleton for the author style guide
  agent-prompts.md             copy-paste prompts for all 9 agent roles
  auto-commit-watcher.md       optional per-change auto-commit daemon
```

## Provenance

Every rule in `references/guardrails.md` corresponds to a failure that
actually happened (fabricated citations, narrated-but-wrong figures,
scope-creeping edits, stale PDFs reported as done, overclaimed data
provenance). The style-guide method (verbatim page-cited quotes, one
imperative rule per pattern) made style compliance a checkable property
rather than a vibe.
