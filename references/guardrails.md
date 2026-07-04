# Guardrails — hard rules from observed failures

Each rule below exists because an AI assistant made the mistake repeatedly in
a real month-long paper project. These override style preferences and apply to
every agent in the roster. When the user corrects a word or behavior once,
append it here so no agent reintroduces it.

## Claims and truth

1. **Never add a claim you have not verified.** No "the structure is too
   rigid", no "the model overfits", no causal explanation — unless the
   artifact (plot, table, proof, source paper) proving it is in hand.
2. **Calibrate exactly.** Neither overstate ("computationally intractable"
   for merely-hard, "real-world data" for simulated) nor understate.
   Every word conveys a meaning the author must be able to defend for days.
3. **Attribute known results.** If a property has a standard name (e.g.
   Lipschitz gradient smoothness), use it and cite it; never present known
   material as novel.
4. **Every added word is reviewer attack surface.** Editorial asides,
   meta-commentary ("we introduce them one at a time because..."), and vivid
   metaphors invite questions. Default to the neutral technical statement.
5. **Do not mention abandoned experiments or speculative future work** unless
   the user asks. The paper reports what was done and holds.

## Figures, numbers, code

6. **Never narrate a figure or result from memory.** Regenerate the plot from
   the actual code, look at it, then write. "Recovery is almost perfect" said
   about a mess destroys trust permanently.
7. **Run the user's actual code/notebooks; never reimplement from scratch**
   and pass it off as the same experiment. Divergent reimplementations
   produced wrong paper figures more than once.
8. **Reimplemented baselines must match the cited method as published** — no
   silent shortcuts "to make it work". Assume the method's authors will read
   the released code.
9. **No information leakage**: normalization constants, anchors, and
   hyperparameters must not encode test-set or ground-truth information.
10. **Repo/paper provenance**: any released code must reproduce the paper's
    exact numbers and figures (verify by regeneration + checksum before
    claiming reproducibility).

## Citations

11. **No source on disk, no `\cite`.** A citation may be typeset only if the
    cited work's PDF/source is present in the project's sources folder
    (`sources/`, one file per bib key). Never cite from memory, a
    search-result snippet, or a DOI alone. If a needed paper is gated or
    otherwise unobtainable, it does NOT get a real `\cite`: put
    `\needcite{key — what it should support}` at the spot and add the paper
    to `citations-needed.md` for the user to download. The paper never ships
    with a `\needcite` left in it, and every `\cite` key must have its source
    file. See `06-citation-audit.md`.

## Editing discipline

12. **Surgical scope**: touch only the passage under discussion. No drive-by
    improvements, reformatting, or restyling of neighboring text.
13. **All changes wrapped in tracked markup**, however small; nothing
    finalized without explicit approval naming the passage.
14. **Recompile and visually confirm the PDF before reporting done.** A .tex
    diff is not evidence the reader's document changed.
15. **Commit after every discrete edit** (tex + freshly compiled pdf); never
    batch sections into one diff.
16. **One canonical manuscript** — one file, one branch; no scratch copies.
17. **Cross-check prose against its own appendix** before editing any
    proposition/lemma statement (inequality directions drift in paraphrase).
18. **A broken build is never "done" and never committed.** If an edit stops
    the document compiling, fix it or revert the edit before reporting or
    committing — do not commit a stale PDF beside broken source, and do not
    report success from an errored compile.

## Register

19. No `\textbf` in running prose or as pseudo-headers.
20. No em-dashes, rhetorical questions, hype words, colloquialisms,
    rule-of-three tics, formulaic transitions, second person.
21. **No padding to seem accessible, no cutting purely to hit a word count.**
    Length changes are justified only by comprehension gain or genuine
    redundancy ("verbose = explainable in fewer words without loss").
22. Do not restate already-defined notation or results; one light prose
    cross-reference suffices.

## Structure and formatting

23. **The model's own defaults are the adversary — override them with corpus
    measurement.** Wherever an LLM has a strong training-data habit (dense
    bold run-in headers, a "Discussion" label after every experiment,
    checklist-style micro-sections, hype vocabulary, ML/CS-conference
    layout), that habit is almost certainly wrong for a prose-forward
    journal. Section granularity, header density, and where interpretation
    lives are taken from the venue corpus (Phase 1 structural-idiom
    measurement), never inherited from what the model would write by default.
    This is the root cause behind most style mistakes: the skill measured the
    corpus for words but the model still supplied the *structure* from habit.
24. **No sectioning command used as emphasis or as a micro-header.** Rule 19's
    ban on `\textbf` in prose extends to `\paragraph{}`, `\subparagraph{}`,
    and any bold run-in label used to tag a micro-topic
    ("Ground-truth utility.", "Normalization.", "Predictive accuracy.") or to
    mark a per-experiment "Discussion."/"Summary.". Use at most the run-in
    density the venue corpus demonstrates (often ≈2–4 per experiment,
    sometimes zero); fold interpretation into the closing prose of the
    results rather than labeling it. Keep a run-in header only when it marks a
    genuinely distinct scenario the corpus would also head (e.g. a separate
    robustness test).
