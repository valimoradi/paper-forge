# Extras — title/abstract candidates, co-author workflow, talk handoff

## Title and abstract optimization

Both are written last (Phase D order) and are the highest-leverage words in
the paper: most readers see nothing else.

**Titles.** Generate 6–10 candidates spanning types observed in Stratum A
(descriptive "X for Y", result-stating, method-naming, question titles only
if the venue's corpus actually uses them). Score each against: venue-title
norms (measure Stratum A title lengths and word patterns), searchability
(would the topic keywords find it?), claim calibration (the title is a
claim — the guardrails apply), and any hard gate on title length. Present a
short table to the user with a recommendation; the user picks.

**Abstracts.** Draft against the venue profile's measured shape (length,
setup-vs-contribution ratio, whether numbers appear). Two or three variants
at most, differing in emphasis (method-first vs. result-first). Verify every
sentence against the contribution map: the abstract may promise nothing the
paper does not deliver. The chosen abstract then locks: later prose edits
that drift from it trigger a flag in the coherence sweep.

## Co-author collaboration

- The canonical-file policy extends to people: one canonical location; every
  co-author edits it or sends patches — no emailed copies merged by hand.
- If co-authors use Overleaf: Overleaf's git bridge becomes `origin`; the
  local clone is where agents work; pull before every session, push after
  every commit; never let the two diverge for more than a working session.
- Human co-author edits arrive as commits like anyone else's; run the
  coherence sweep over their diffs too (politely: findings are proposals).
- The red/yellow markup convention must be agreed with co-authors before
  they see the first marked draft — a supervisor who does not know what
  yellow means will reject the file, not the edits.

## Talk / slides handoff

When the paper is submitted and a talk is needed (conference presentation
of the same work), the paper's artifacts drive the deck; do not write slides
from memory:

- narrative spine = the contribution map (Phase D1), one contribution per
  slide block
- every figure in the deck comes from the claims ledger's generating
  scripts, re-rendered at slide aspect ratio and font size — never a
  screenshot of the paper's figure
- the venue-register work transfers: a talk for the paper's community uses
  Stratum A's vocabulary
- claim calibration applies verbatim; a slide is not a license to
  overstate what the paper hedges
- if a dedicated slides skill/tooling exists in the environment, hand it
  the contribution map + claims ledger as inputs.
