# Phase 3 — Building the corpus-grounded style guide

Goal: a style guide where every rule is traceable to real sentences the target
author published, so "does this edit match the style?" is a checkable question
rather than a vibe.

## The method (proven format)

For each analysis dimension below, have a reader agent sweep the approved
corpus and pull **verbatim quotes with paper + section + page attribution**.
Then write **one generalizable imperative rule per observed pattern**, followed
by the 2–8 quotes as evidence blocks. Never paraphrase the evidence; verbatim
quotes are what keep the guide honest and let a checker agent verify
compliance later. Close the guide with a consolidated Do/Don't checklist.

## The 12 dimensions

1. **Voice and rhythm** — person, sentence-length pattern (e.g. short claim
   sentence followed by longer elaboration), paragraph shape.
2. **Openings and hooks** — how papers and sections start; hook taxonomy.
3. **Contribution framing** — numbered vs. prose, parallel verb structure
   ("We develop / generalize / prove / demonstrate"), scope-bounding.
4. **Notation introduction** — plain English before symbols; how much at once.
5. **Intuition-around-math sandwich** — (A) plain-English setup, (B) the
   formal object verbatim, (C) an "in other words" gloss ending in stakes.
6. **Theorem/proposition presentation** — statement style, where proofs live,
   how much bridge narration between results (often: almost none).
7. **Cross-references** — one light prose pointer, never stacked \ref+\eqref;
   never restate an already-defined object.
8. **Narrating results and numbers** — number → consequence-for-the-reader
   (the practical takeaway for the field's stakeholders).
9. **Figure/table narration** — what the prose says vs. what the caption says.
10. **Transitions and signposting** — declarative signposts only; the actual
    transition vocabulary the author uses (build a template bank).
11. **Hedging and limitations** — where limitation statements sit and how
    strong they are.
12. **Analogies and domain grounding** — whether and how the author uses them.

## Two-layer output

Produce two artifacts:

1. **`<AUTHOR>_STYLE_GUIDE.md`** (portable): the 12-dimension rulebook with
   verbatim page-cited evidence. Domain specifics in the quotes are
   illustrative; the rules transfer to any technical paper.
2. **`_STYLE_GUIDE.md`** (applied, lives next to the paper): a shorter
   distillation fitted to THIS manuscript — template bank of openers and
   transitions, the mandatory equation-wrapper pattern, and paper-specific
   fidelity guardrails. Skeleton: `templates/applied-style-guide-template.md`.

(The two filenames are suggestions; keep whatever names the user prefers, but
keep two artifacts: one portable, one applied.)

## The style stack: where this guide sits

The author guide is Layer 3 of a three-layer stack, all three always in
force:

1. **Layer 1 — academic base** (`references/academic-register.md`, bundled):
   formal register plus the anti-AI-tell hard bans (no em-dashes, rhetorical
   questions, hype words, `\textbf` in prose, formulaic transitions,
   rule-of-three tics, over-claiming).
2. **Layer 2 — venue register** (`venue-register.md`, built in Phase 1 from
   the venue corpus): this journal's actual vocabulary, voice, terminology,
   and phrase bank.
3. **Layer 3 — author voice** (this phase): the target author's structural
   and narrative techniques.

Precedence on conflict: venue register beats author voice; both may override
the base layer only with verbatim corpus evidence. During Phase 3, record
every author-vs-venue clash you discover in `venue-register.md`'s conflicts
section so writer and checker agents resolve it the same way every time.

## The concision gate

Author-style accessibility must never inflate length. Before presenting any
rewrite, check: no restated points, no throat-clearing, no filler adjectives,
no tutorial content the venue's readers do not need, hedges only where the
evidence demands them. If a proposed edit is longer than what it replaces,
justify the extra words by a specific comprehension gain; if you cannot, cut.
"A more understandable paper is usually a shorter one."

## Approval gate

Present both artifacts to the user and STOP. The user may reject dimensions,
add personal rules (these go in a "house rules" section), or demand more
evidence. Only an approved guide governs Phase 5.
