# Phase 8b — Submission package assembly

A clean manuscript is not a submission. After the bake, assemble everything
the portal asks for; each artifact is drafted by an agent and approved by
the user like any other text.

## Checklist (trim per venue — the guidelines page from Phase 1 says which
apply)

- [ ] **Cover letter** (skeleton below)
- [ ] **Title page** vs. **blinded manuscript** if double-blind: strip
      author block, acknowledgments, self-identifying phrases ("our earlier
      work [X]" → "prior work [X]"), grant numbers, repo URLs that reveal
      identity; grep the blinded PDF for every author's name
- [ ] **Author statements**: contributions (CRediT if requested), conflicts
      of interest, funding, data & code availability (must match what the
      repo actually provides — claims-ledger reproducibility run backs this)
- [ ] **AI-use / generative-tool disclosure**: check the venue's policy (most
      now require one) and write the statement it asks for, describing how AI
      assistance was used and affirming the authors are responsible for all
      content. A pipeline this AI-heavy makes the disclosure mandatory, not
      optional; never claim sole human authorship where the policy asks
      otherwise
- [ ] **Text-overlap / self-plagiarism check**: run the manuscript through a
      similarity tool (the venue often runs iThenticate anyway) — reused
      passages from the authors' own prior papers, proposals, or preprints
      must be rewritten or quoted+cited, not silently carried over
- [ ] **Suggested reviewers** (and opposed, if justified): qualified, no
      recent co-authors or same-institution researchers, with a one-line
      rationale each; the user picks from candidates
- [ ] **Keywords / classification codes** (MSC, JEL, or the venue's own
      taxonomy) chosen from the venue's list, matched to Stratum-A papers'
      choices
- [ ] **Highlights / one-sentence summary** if the venue wants them —
      derived from the contribution map, same claim calibration rules
- [ ] **Supplementary / e-companion bundle**: everything triaged out of the
      body in Phase 1's split decision, compiled per the venue's rules
- [ ] **Source files** as the portal wants them: tex + figures + bst/bbl,
      figure formats/resolutions per guidelines, no unused files
- [ ] **Preprint**: check the journal's preprint policy; if posting to
      arXiv, prepare the arXiv-safe version (single-column or journal class
      as policy allows, no journal branding) and record the version match
      in the claims ledger
- [ ] **ORCID and metadata** fields ready for the portal form (title,
      abstract, authors exactly as in the manuscript)

## Cover letter skeleton

Half a page, no hype, calibrated claims:

1. One sentence: title + what the paper does.
2. Two or three sentences: the contribution and why it fits THIS journal
   (name the department/area if the journal has them; cite fit via the kind
   of papers it publishes, not flattery).
3. Standard declarations: original work, not under consideration elsewhere,
   all authors approved, any prior-presentation disclosure (e.g. a
   conference talk of the same work, per the venue's policy).
4. Suggested-reviewer list if the letter is where the venue wants it.

The cover letter obeys the full style stack and guardrails: no
"groundbreaking", no over-claiming — editors read hundreds of these and the
register is part of the impression.

## Final gate

Re-run the Phase-7 hard-gate checks on the exact files being uploaded (not
an earlier build), then the user uploads. Keep a `submission/` folder with
the byte-exact uploaded artifacts and a manifest, tagged in git — Mode C
starts from this snapshot.
