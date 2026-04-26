# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

This is a personal LLM wiki following the pattern described in `docs/karpathy_gist.md`. Claude Code maintains the wiki — creating, updating, and cross-referencing markdown pages. The human curates sources and asks questions; Claude does all the bookkeeping.

## Directory structure

```
raw/              # Immutable source documents (articles, papers, notes, images)
  Articles/       # Web clips and articles to ingest into the wiki
  Personal/       # Owner's personal documentation — NOT ingested as articles
  assets/         # Locally downloaded images referenced by source files
wiki/             # LLM-generated and maintained markdown pages
  index.md        # Content catalog — updated on every ingest
  log.md          # Append-only chronological record of all operations
docs/             # Meta files (karpathy_gist.md, diagrams)
```

The `raw/` directory is read-only. Never modify files there. The `wiki/` directory is fully owned by Claude.

### raw/Personal/

Contains the owner's own writing: career documentation, interview prep, project notes, and a personal profile for AI agents. This folder is **not processed like articles**. It is a primary source about the person, not external content to summarize.

When a file appears in `raw/Personal/`, treat it as authoritative first-person context about the owner — their skills, projects, goals, and background. Use it to:
- Inform answers and wiki pages with accurate personal context
- Build or update a `wiki/Dan-Orlando.md` profile page when asked
- Provide richer context if automation agents need to know who they're working for

Do not run the standard ingest pipeline on these files. Do not create `wiki/sources/` pages for them. When the user asks to "process" or "document" personal files, ask what they want — a profile page, talking-point extracts, or something else — rather than assuming article ingest.

## Design decisions

These are settled choices about how this wiki operates. Follow them unless the user explicitly overrides.

**`raw/` is a curation record, not a mirror.** The purpose of `raw/` is to record what the user decided was worth their attention — not to store a complete copy of every source. Clipping something is the curation act itself.

**For repos, the README web clip is the raw artifact.** Clipping a repo's README signals "I found this worth saving" — the same as clipping an article. During ingest, fetch supplemental detail live (specific source files, docs site, author blog posts) as needed to inform the wiki page. Do not try to pre-mirror the whole repo into `raw/`. The wiki page is the durable artifact, not a raw dump.

**Live fetching during ingest is fine.** The wiki page becomes the permanent, synthesized record. The raw artifact is just the anchor.

**Model selection by operation.** Ingest is bounded compilation work — use Sonnet (cheaper, fast enough). Query starts on Sonnet; switch to Opus when synthesizing across many pages or when the answer feels shallow. Lint defaults to Opus, since finding subtle contradictions across the whole wiki is exactly the deep-reasoning job it handles best.

## Core operations

### Ingest

When the user drops a new source into `raw/` and asks to process it:

1. Read the source (and any referenced images separately if needed)
2. Discuss key takeaways with the user
3. Write a summary page in `wiki/sources/<slug>.md`
4. Update `wiki/index.md` with a new entry
5. Update all relevant entity and concept pages across the wiki — a single source may touch 10–15 pages
6. Append an entry to `wiki/log.md` in the format: `## [YYYY-MM-DD] ingest | <Title>`

### Ingest (repo README variant)

When the source is a clipped README from a code repository:

1. Read the README; fetch supplemental detail live if needed (key source files, docs site, author blog posts)
2. Focus extraction on **design decisions**, not feature lists:
   - What problem does it solve, and what's the core insight behind the approach?
   - What's novel or non-obvious about how it works?
   - How does it handle the hard cases and edge cases?
   - What tradeoffs did the author make, and why?
3. Write the summary page in `wiki/sources/<slug>.md` emphasizing those decisions
4. Update `wiki/index.md` and `wiki/log.md` as with a standard ingest
5. Update relevant concept/entity pages — repos often have strong opinions about architecture that cross-cut many topics

### Query

When the user asks a question:

1. Read `wiki/index.md` to find relevant pages
2. Drill into those pages and synthesize an answer with citations
3. If the answer is non-trivial or reusable, offer to file it as a new wiki page

Good answers should be filed back into the wiki. Explorations should compound, not disappear into chat history.

### Lint

When asked to health-check the wiki, look for:
- Contradictions between pages
- Stale claims superseded by newer sources
- Orphan pages with no inbound links
- Important concepts mentioned but lacking their own page
- Missing cross-references
- Data gaps that could be filled with a web search

## Wiki page conventions

- Use `[[WikiLinks]]` style for cross-references between pages (Obsidian-compatible)
- Add YAML frontmatter to pages with at least `tags:` and `updated:` fields
- Source summary pages live in `wiki/sources/`; entity/concept pages live directly in `wiki/`
- Each entity or concept page should have an **inbound sources** section listing which source files support its claims

## index.md format

One entry per wiki page, grouped by category (Sources, Entities, Concepts, Analyses):

```
## Sources
- [[sources/slug]] — One-line summary (YYYY-MM-DD)

## Entities
- [[PageName]] — One-line summary
```

## log.md format

Append-only. Each entry starts with a parseable prefix:

```
## [YYYY-MM-DD] ingest | Article Title
## [YYYY-MM-DD] query | Question asked
## [YYYY-MM-DD] lint | Health check summary
```

This makes the log greppable: `grep "^## \[" wiki/log.md | tail -5` shows the last 5 operations.
