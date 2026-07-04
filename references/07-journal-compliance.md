# Phases 7 & 8 — Journal compliance and submission bake

## Phase 7 — Compliance check against the venue profile

Diff the manuscript against the Phase-1 venue profile AND the official author
guidelines. Checklist (extend per venue):

**Hard gates (BLOCKING — quoted official limits; a violation stops
submission, no exceptions)**
- [ ] Figure count ≤ the venue's maximum (count them; check whether
      appendix/e-companion figures count toward the gate)
- [ ] Table count ≤ the venue's maximum
- [ ] Body within the page/word limit, **compiled on the venue's official
      LaTeX class** — a page count on any other class is meaningless
- [ ] Abstract within the official word limit
- [ ] Any other quoted limits (references, title length, appendix count)
- [ ] Manuscript actually built on the official template/class, with its
      bst/csl in use

These were budgets from Phase 1 onward (skeleton allocation in Phase D,
figure selection in Phase R); Phase 7 confirms nothing drifted over a gate.
If one is violated, cutting to fit is a red-edit round of its own before
anything else proceeds.

**Lengths (measured, not eyeballed)**
- [ ] Abstract within the venue limit and shaped per the profile (e.g. ~150
      words, one setup sentence, contribution-first)
- [ ] Introduction within the measured venue median ± tolerance
- [ ] No section exceeding its role (diagnostic material, sensitivity
      archaeology, implementation detail → appendix/e-companion or out;
      "readers can check the released code" is a valid reason to cut)

**Structure**
- [ ] Section skeleton matches venue norms (related work woven vs. separate;
      proofs in appendix; body ends, then references, then appendix — verify
      the venue's ordering explicitly)
- [ ] **Formatting idiom matches the venue register**, not the model's
      default: run-in-header density within the corpus norm (run
      `scripts/check_headers.py`); no per-experiment "Discussion"/"Summary"
      labels unless the corpus uses them; no checklist-style micro-headers
      ("Normalization.", "Predictive accuracy.") beyond what Stratum A shows
- [ ] Contribution list matches what the paper actually delivers; the
      abstract promises nothing the intro's contributions do not claim;
      validation work is not listed as a contribution
- [ ] Body/appendix split matches the dual-venue decision made in Phase 1

**Register and claims**
- [ ] No `\textbf` in running prose; no editorial/hype words; venue register
      throughout (run one final supervisor-persona + register sweep)
- [ ] Every claim calibrated to evidence; data provenance described exactly
      (e.g. "simulated instances derived from real inputs", not "real
      operational data", when the instances are model-generated)
- [ ] Tables carry no bare "n/a" — every dash/blank explained in notes

**Mechanics**
- [ ] Reference style/bst per guidelines; every bib entry passed the
      citation audit
- [ ] **Every `\cite` has its source in `sources/`; zero `\needcite`
      placeholders remain** (run `scripts/check_citations.py`) — no citation
      ships without its downloaded source, and `citations-needed.md` is empty
      or its items resolved
- [ ] Anonymization rules if double-blind; data/code statement per policy
- [ ] Figures: format, fonts, no overflow past margins, colors sane in print

Findings → red edits → user approval, as always.

## Phase 8 — Bake and submission hygiene

Run ONLY after the user explicitly says the marked-up version is fully
approved (e.g. after their supervisor's pass).

1. Strip all revision macros: replace `\rev{x}`/`\yel{x}` with `x`, delete
   `\revdel{x}`/`\yeldel{x}` contents, remove retired no-op macros.
2. **Grep-verify zero leftovers and report the counts.** Experience: the
   first "clean" pass left hundreds of markers in place. Iterate
   until every count is 0: `\rev{`, `\revdel{`, `\yel{`, `\yeldel{`,
   `\added{`, `\deleted{`, `\NEW{`, plus the macro definitions themselves.
3. Remove dead scaffolding: commented-out blocks, unused packages, TODO
   markers, draft-mode flags.
4. Verify label/citation parity vs. the pre-bake version (same `\cite` set,
   same `\label`/`\ref` set) so the bake changed markup only.
5. Final compile from a clean aux state; visually skim the whole PDF once.
6. Final commit, tagged (e.g. `submission-v1`).

Keep the marked-up pre-bake version on its own branch/tag forever — revision
requests after review will need it.
