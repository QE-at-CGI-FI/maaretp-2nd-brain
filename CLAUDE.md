# maaretp-2nd-brain — LLM Wiki schema

This repo follows the "LLM Wiki" pattern: raw sources → a persistent,
LLM-maintained wiki, kept current incrementally rather than re-derived per
query. See `LLM-wiki-idea.md` (or the conversation that introduced it) for
the general pattern this instantiates.

## What this instance is

Two separate wikis, both built by processing Maaret's public post history
(Twitter 2010–2022, Mastodon 2022–present) in chronological batches:

- **`wiki/testing/`** — professional/testing craft: ideas, practices, people,
  talks, and how her thinking on testing evolved over 16 years.
- **`wiki/personal/`** — personal reflection, growth, values, life context.

They stay structurally separate. A single ingest batch (one raw time range)
is read once and may produce updates in *both* wikis, but pages in one never
`[[wikilink]]` into the other — if a topic genuinely spans both, note it in
prose with a relative path instead.

## Layers

- **`raw/`** — immutable. Original archive exports (`raw/archives/twitter/`,
  `raw/archives/mastodon/`). Never edit, delete, or reformat these files.
  The wiki (`wiki/progress.md` specifically), not the archive, is the
  record of what's been processed.
- **`raw/parsed/timeline.jsonl`** — derived, regenerable. The two archives
  merged into one chronological JSONL stream (one post per line: `date`,
  `platform`, `id`, `url`, `text`, `is_retweet`, `is_reply`, `in_reply_to`).
  Rebuild with `python3 tools/build_timeline.py` whenever the raw archives
  change. Safe to delete and regenerate at any time.
- **`wiki/testing/`, `wiki/personal/`** — LLM-owned. Markdown, Obsidian
  conventions (below). This is what gets read, browsed, and linked.
- **`wiki/progress.md`** — shared ingestion tracker across both wikis (see
  Ingest workflow).
- **`tools/`** — parsing/utility scripts. `build_timeline.py` (rebuild the
  merged timeline), `extract_batch.py` (pull a date-range slice to read).

## Wiki structure (same shape in both `wiki/testing/` and `wiki/personal/`)

```
index.md        catalog of every page in this wiki, one-line summaries, by category
log.md          append-only event log: "## [YYYY-MM-DD] ingest | <batch label>"
entities/       people, orgs, tools, places — one page each
concepts/       recurring ideas/themes/practices — one page each
batches/        one summary page per ingested chronological range
```

## Workflows

### Ingest a batch

1. Check `wiki/progress.md` for the next `not started` range (oldest first —
   the story starts in 2010). Default batch size is one calendar year; split
   a dense year into quarters if it's unwieldy to read in one sitting
   (`tools/extract_batch.py 2016-Q1`), and split that row in the table.
2. Pull the slice: `python3 tools/extract_batch.py <range> --skip-retweets`
   (drop `--skip-retweets` if retweets seem worth reading for that range;
   add `--skip-replies` for noisy reply-heavy years if needed).
3. Read it, discuss what's notable with Maaret before writing anything.
4. For each wiki the batch's content touches:
   - create/update `entities/*.md` and `concepts/*.md` pages
   - write `batches/<range>.md` summarizing the batch and linking what it touched
   - append to `log.md`
   - update `index.md`
5. Update the row in `wiki/progress.md`: status → done, which wikis were
   touched, links to the batch pages created.

Stay involved batch-by-batch rather than racing through the whole archive
unsupervised — this is a slow-cooked personal project, not a bulk import.

### Query

Read the relevant wiki's `index.md` first, drill into linked pages, answer
with citations back to wiki pages (and to `raw/parsed/timeline.jsonl`
entries by id/url where a specific post matters). A good answer that's
worth keeping gets filed back as a new page (probably under `concepts/`),
not left in chat history.

### Lint

Periodically check each wiki for: contradictions between pages, orphan pages
with no inbound links, concepts mentioned on multiple pages but lacking
their own page, and stale `index.md` entries.

## Obsidian conventions

- `[[wikilink]]` between pages *within* the same wiki (filename = link
  target). Never link across `wiki/testing/` ↔ `wiki/personal/`.
- Every wiki page gets YAML frontmatter: at minimum `tags:`; add `date:` and
  `sources:` (list of raw post ids/urls) where relevant.
- Open the repo root as the Obsidian vault — both wikis and `raw/` live
  under it. `raw/` can be excluded from Obsidian's indexing later via vault
  settings if it gets in the way of graph view.
