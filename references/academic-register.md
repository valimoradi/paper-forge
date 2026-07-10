# Layer 1 — Academic register (universal base layer)

The always-on baseline under every venue and author style. Its job is twofold:
enforce formal academic prose, and strip the tells that make text read as
AI-generated. This layer is self-contained; no external skill is required.

## Target register

Formal, precise, neutral academic prose. Every sentence earns its place;
every word means exactly what it says. The reader is a skeptical expert.

## Hard bans (checkable by grep; the style checker enforces all of them)

1. **Em-dashes** — restructure the sentence, use a comma, colon, or
   parentheses, or split into two sentences.
2. **Rhetorical questions** — replace with a declarative statement of what
   the question implied.
3. **Colloquialisms and metaphors** — no "a price to pay", "the elephant in
   the room", "at the end of the day". State the technical fact.
4. **Hype and intensifier filler** — "crucially", "remarkably", "notably",
   "significantly" (unless statistical), "powerful", "novel" as
   self-description, "state-of-the-art" without a benchmark.
5. **Formulaic AI transitions** — "It is worth noting that", "Importantly,",
   "Moreover," chains, "In conclusion" outside an actual conclusion,
   "delve", "landscape", "leverage" as a verb for "use".
6. **Second person and exclamation** — never address the reader; never "!".
7. **Structural tics** — rule-of-three lists as rhythm, "not just X, but Y",
   "X is not merely Y, it is Z", paired-synonym doublets ("clear and
   concise").
8. **Unqualified over-claiming** — superlatives and universals ("always",
   "guarantees", "solves") only where the evidence is a proof.
9. **Manual emphasis and bold** — no `\textbf`, bold, or italics-for-emphasis
   anywhere the reader reads as content: running prose, pseudo-headers, and
   table cells. Emphasis comes from sentence structure, not weight. Math
   notation is bold-free too; see "Math and typographic conventions" below.

## Math and typographic conventions

Typography is a paper-wide invariant, not a per-passage choice: fix the
convention once from the target author/venue corpus and apply it identically
everywhere. Absent corpus evidence for a different convention, the defaults are:

1. **Vectors and matrices are plain italic, not bold.** Write the decision
   vector, parameter, and feature matrix as `x`, `\theta`, `A` — never
   `\mathbf{x}`, `\boldsymbol{\theta}`, `\mathbf{A}`. This follows the modern
   OR/optimization convention (e.g. Jonathan Li's papers). Some fields do bold
   vectors, so confirm against the corpus; but once chosen the convention is
   uniform. A mixed manuscript (some vectors bold, some plain) is always a
   defect, regardless of which convention won.
2. **No bold anywhere the ink is content** — not in math (`\mathbf`,
   `\boldsymbol`, `\bm`), not in table cells or numeric entries (a "best" row
   is marked by structure, a rule, or a note, not by bolding the number), not
   as prose emphasis.
3. **Documented exceptions only.** A small, explicitly listed set may stay bold
   when weight carries meaning the plain glyph would lose: a ones-vector macro
   (`\one = \mathbf{1}`, disambiguating from the scalar 1), graphical figure
   panel labels, and Left:/Right: caption anchors. List every exception in the
   applied style guide so a checker agent does not "correct" them.

Applying or switching this convention is a single typographic-normalization
pass over the whole manuscript (un-bold every `\mathbf`, strip emphasis-bold
from tables), verified by grep to zero remaining hits outside the exception
list — not a drive-by fix during a prose pass.

## Fidelity when editing existing text

Change only wording and punctuation. Preserve byte-for-byte: equations,
inline math, `\cite` keys, `\label`/`\ref`, numbers, units, table entries,
figure references, theorem statements' conditions. Inline math stays in the
document's existing delimiter convention.

## Verification recipe (run after every register pass)

- grep the em-dash character and count = 0 in prose (allow inside verbatim
  quotes of sources)
- grep `? ` outside of research-questions sections; justify every hit
- diff the `\cite`/`\label`/`\ref` sets before vs. after the pass: identical
- word-level diff shows changes only in prose, never inside math environments
- grep `\mathbf`/`\boldsymbol`/`\bm` and `\textbf` = 0 outside the documented
  exception list (vectors plain italic, no bold table cells)
- document compiles; page count moved only as expected

## What to KEEP

Technical hedges that bound claims ("under Assumption 2", "in our
experiments"), field-standard terminology however informal it sounds,
first-person plural for the authors' own actions ("we prove"), and the
author's/venue's own signature constructions once Layers 2–3 are built —
this layer never overrides a pattern that the venue or author corpus
demonstrably uses.

## Position in the style stack

Layer 1 (this file, universal) < Layer 2 (venue register, from the venue
corpus — `templates/venue-register-template.md`) < Layer 3 (author voice,
from the author corpus — Phase 3). On any conflict, the more specific,
corpus-evidenced layer wins: author voice yields to venue register; both
override this base layer only with verbatim corpus evidence.
