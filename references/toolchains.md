# Toolchains — LaTeX (default), Word, Markdown

The pipeline's phases are toolchain-neutral; only the mechanics of tracked
edits, compiling, and gate-checking change. LaTeX is the primary, fully
supported path. This file maps the LaTeX-specific mechanics onto Word and
Markdown so non-LaTeX users get a workable, if thinner, experience.

## What changes per toolchain

| Mechanic | LaTeX (default) | Word | Markdown |
|----------|-----------------|------|----------|
| Tracked edits (red/yellow) | `templates/revision-macros.tex` | native Track Changes; red/yellow split via two comment prefixes `[SUBST]`/`[STYLE]` on each change | CriticMarkup: `{++add++}`, `{--del--}`, with `{>>SUBST/STYLE<<}` comments |
| Approval / finalize | unwrap macros per passage | Accept/Reject per change | strip CriticMarkup per passage |
| Compile + visually confirm | latexmk → PDF | the .docx IS the document; still re-open and confirm | render (pandoc/site) and confirm |
| Commit cadence | tex + pdf per edit | docx per edit (binary diffs are opaque — commit messages must carry the "what changed") | md (+ rendered artifact) per edit |
| Bake (Phase 8) | `scripts/bake_markup.py` + zero-leftover grep | Accept All + search for leftover `[SUBST]`/`[STYLE]` comments | strip CriticMarkup + grep `{++`, `{--`, `{>>` = 0 |
| Register checks | `scripts/check_register.py` | same script on a pandoc-exported .md/.txt | same script directly |
| Word counts / budgets | `scripts/count_words.py` | Word's per-section counts or pandoc export + script | script directly (it tolerates plain text) |
| Hard gates: figures/tables | `scripts/check_gates.py` | count manually or via pandoc export | grep image/table syntax |
| Official template | venue `.cls`/`.sty`, build on it | venue's `.dotx`/styles if published | usually N/A — export to the venue format at the end |
| Page-limit gate | compile on official class | measured in the venue template directly | only meaningful after export — check early and often |

## Rules that do not change

Everything else is toolchain-independent and stays in force: surgical scope,
approval gates, commit-per-edit, claims ledger, citation
verify-at-insertion, the three-layer style stack, hard gates as day-one
budgets, and every guardrail.

## Bridging advice

- Word users collaborating with LaTeX users: keep the canonical manuscript
  in ONE toolchain (canonical-file policy applies to formats too); convert
  copies are read-only.
- Markdown-first users targeting a LaTeX venue: switch to the official
  class no later than Phase D's skeleton — page-gate measurements before
  the switch are fiction.
- Pandoc is the bridge for running the scripts against Word documents:
  `pandoc paper.docx -t markdown -o paper.md`, run checks on the export,
  apply fixes in the .docx.
