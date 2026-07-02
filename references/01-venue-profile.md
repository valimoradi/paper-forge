# Phase 1 — Venue selection and venue profile

Goal: replace "journal style" folklore with measured facts about the target
venue, harvested from real recent papers and the official author guidelines.

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

## Step 5. Benchmark against one exemplar

Pick ONE real paper from the sample (ideally by the target author, in the
target venue) as the structural exemplar. Later compliance passes diff the
manuscript against this concrete paper — abstract length, intro length,
contribution framing — not against abstract rules. Abstracted style rules
drift; a concrete exemplar does not.

## Output

Write `venue-profile.md` in the paper's directory using
`templates/venue-profile-template.md`. Present it to the user and STOP for
approval. This document is the arbiter in every later conflict: when the
author-style guide and the venue register disagree, the venue profile wins.
