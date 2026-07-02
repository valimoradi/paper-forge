# Phase 2 — Target-author corpus acquisition

Goal: a small, approved corpus of the target author's papers that grounds the
style guide. Style emulation without a real corpus degrades into generic "AI
academic voice"; the corpus is what makes the guide checkable.

## Step 1. Ask the user

- Name an author whose style the paper should resemble, OR a single exemplar
  paper ("I want mine to read like this one"). If a paper is named, its lead
  author becomes the target author.
- Optionally a **second anchor**: a different author (often the supervisor)
  whose virtue is precision/concision rather than accessibility. The original
  project's most durable directive was "accessible like author A, concise and
  precise like author B" — encode both and hold them in tension. When they
  conflict, precision wins over narrative flourish.
- Ask which of the author's papers the user considers most representative, if
  they know.

## Step 2. Download 4–6 papers by the target author

Priorities, in order:
1. Papers in the **target venue** (style guide evidence should share the
   venue register).
2. Papers in the **same subfield** as the manuscript (domain-adjacent quotes
   transfer better into the applied style guide).
3. Solo/lead-author papers over heavily co-authored ones (cleaner signal of
   the author's own voice).

Sources: author's academic homepage, arXiv, Google Scholar, journal open
access. Store in `author_corpus/<author>/` with `MANIFEST.md` (title, venue,
year, URL, file).

If a second anchor author exists, download 2–3 of their papers into
`author_corpus/<anchor>/` the same way.

## Step 3. Approval gate (mandatory STOP)

Present the manifest to the user: title, venue, year, path, and one line on
why each paper was selected. The user may swap papers in/out. **Do not build
the style guide until the corpus list is approved.** A style guide built on a
corpus the user did not sanction produces edits the user will reject
wholesale.

## Step 4. Provenance hygiene

- Keep the PDFs; every style-guide quote must later be traceable to
  paper + section + page. If a PDF cannot be text-extracted, note it and
  replace it.
- These same PDFs double as citation-audit sources if the manuscript cites
  the target author (it usually does).
