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

## Step 3. Build a stratified venue corpus (three strata)

A venue publishes many kinds of papers; a flat "reputable papers" sample
mixes subfields and produces a vocabulary that matches none of them. The
corpus has three strata with distinct roles:

**Stratum A — topic-matched (up to 20 papers; the most important).**
Papers in this venue on the same topic/subfield as the user's paper. Derive
the topic terms from the paper profile, abstract/draft, and the user's own
keywords, then search the venue's archive for matches; confirm the keyword
list with the user before searching. These papers define the manuscript's
**vocabulary and terminology**: the words of the venue's optimization
papers, not its behavioral or empirical papers (or whatever the analogous
split is in the user's field). If the target author (Phase 2) has papers in
this venue on this topic, they belong here.

**Stratum B — venue flagship (top 10).** The venue's most reputable/cited
papers regardless of topic. These define what the venue's editors reward:
structure, positioning, contribution framing, claim register.

**Stratum C — latest (10 most recent issues' papers).** The venue's newest
publications regardless of topic. These catch current conventions that older
flagship papers miss (formatting drift, section naming, data/code statement
norms, current abstract style).

Store PDFs in `venue_corpus/<venue>/A_topic/`, `B_top/`, `C_latest/` with a
`MANIFEST.md` per stratum (title, authors, year, DOI/URL, why selected, and
for Stratum A: which topic terms it matched). If the venue's archive yields
fewer than 20 topic matches, take what exists and say so — do not pad
Stratum A with off-topic papers.

**STOP: present the stratified manifest to the user for approval** (they
know their subfield's landmark papers and will spot misclassified or missing
ones) before measuring anything.

## Step 4. Measure the norms (do not guess them)

Structural norms are measured across ALL strata (medians), with Stratum C
breaking ties toward current practice. For each downloaded paper, measure
and tabulate:

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
different vocabularies, voices, and sentence rhythms — and within one
journal, each subfield has its own working vocabulary. Reader agents sweep
the venue corpus and build `venue-register.md` from
`templates/venue-register-template.md`, with **verbatim page-cited quotes**
as evidence (the same corpus-grounded method as the Phase-3 author guide).
Source each part from the right stratum:

- **Lexicon, terminology, phrase bank → Stratum A (topic-matched) only.**
  The manuscript must sound like the venue's papers *on this topic*; quoting
  vocabulary from another subfield's papers defeats the purpose.
- **Voice, tense, hedging, sentence/paragraph norms → all strata**, flagging
  any drift between flagship (B) and latest (C) papers; prefer current
  practice where they differ.

Dimensions:

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

Pick ONE real paper from Stratum A (topic-matched; ideally by the target
author) as the structural exemplar. Later compliance passes diff the
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
