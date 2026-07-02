# Phase 1 — Venue selection, venue profile, and venue register

Goal: replace "journal style" folklore with measured facts about the target
venue, harvested from real recent papers and the official author guidelines.
Phase 1 produces two artifacts: the **venue profile** (structural norms and
official rules) and the **venue register** (how papers in this journal are
actually written — Layer 2 of the style stack; see
`references/academic-register.md` for the stack).

## Step 1. Ask the user

- Primary venue (the journal/conference the paper will be submitted to).
- Any secondary venue (e.g. a domain conference where the work is presented).
  A dual-venue target drives a structural decision: which content lives in the
  main body vs. the appendix / e-companion. Decide this early and record it.
- Field and subfield, so the "reputable papers" search is scoped correctly.

## Step 2. Download the venue's official author guidelines

Fetch the journal's submission/author-guidelines page and extract into the
venue profile:

- abstract word limit; page/word limit for the body
- reference style (bst/csl), bibliography-vs-appendix ordering
- structure requirements (structured abstract? separate related-work section
  allowed or woven into intro? e-companion/online-supplement conventions)
- anonymization / double-blind rules
- data & code availability policy
- figure/table format rules

## Step 3. Download 5–10 reputable recent papers from the venue

Selection heuristics: recent (last ~5 years), well-cited for their age, and —
if the user has already named a target author (Phase 2) — include that
author's papers in this venue. Store PDFs in `venue_corpus/<venue>/` with a
`MANIFEST.md` (title, authors, year, DOI/URL, why selected).

## Step 4. Measure the norms (do not guess them)

For each downloaded paper, measure and tabulate:

- abstract word count
- introduction word count and paragraph count
- where related work lives (intro-woven vs. separate section)
- where proofs live (inline vs. appendix vs. e-companion)
- contribution presentation (numbered list? prose? how many items?)
- section skeleton (typical top-level structure)
- claim register: how strongly results are stated; hedging conventions
- typography: is `\textbf` used in running prose? (In OR/MS journals it is
  not; manual bolding is an AI tell and a register violation.)

Medians across the sample become the manuscript's targets (e.g. "intro target
= 1200 words because the venue median is ~1150").

## Step 5. Extract the venue register (how this journal writes)

Structure is not style: two journals with identical skeletons can use
different vocabularies, voices, and sentence rhythms. Reader agents sweep the
same venue corpus and build `venue-register.md` from
`templates/venue-register-template.md`, with **verbatim page-cited quotes**
as evidence (the same corpus-grounded method as the Phase-3 author guide):

- voice and person (first-person plural? passive where? tense per section)
- the venue's working vocabulary: which verbs introduce contributions, state
  proved results, report empirical results; count occurrences across the
  corpus so the manuscript defaults to the venue's most frequent choices
- terminology conventions: which of several synonymous field terms this
  journal prefers, hyphenation, capitalization
- sentence and paragraph norms; signposting density
- hedging vocabulary and where it appears
- a phrase bank of verbatim openers, transitions, and result-narration frames
  for the writer agent

The venue register sits between the universal academic base layer
(`references/academic-register.md`) and the author voice (Phase 3): author
voice yields to venue register on any conflict, and both override the base
layer only with verbatim corpus evidence.

## Step 6. Benchmark against one exemplar

Pick ONE real paper from the sample (ideally by the target author, in the
target venue) as the structural exemplar. Later compliance passes diff the
manuscript against this concrete paper — abstract length, intro length,
contribution framing — not against abstract rules. Abstracted style rules
drift; a concrete exemplar does not.

## Output

Write `venue-profile.md` (structure, from
`templates/venue-profile-template.md`) and `venue-register.md` (style, from
`templates/venue-register-template.md`) in the paper's directory. Present
both to the user and STOP for approval. These documents are the arbiter in
every later conflict: when the author-style guide and the venue disagree,
the venue wins.
