# Wiki Schema

## Domain

AI/ML research, agent tooling, and personal knowledge management. Covers LLM systems, agent architectures, developer tools, and the owner's professional context.

## Directory Structure

```
raw/              # Immutable source documents (read-only — never modify)
  Articles/       # Web clips and articles
  Repos/          # Clipped repo READMEs (organized by category)
  Releases/       # Product/release announcements
  research_papers/# Academic papers
  Documentation/  # Technical documentation clips
  Personal/       # Owner's own writing — NOT ingested as articles
  my_article_ideas/ # Article drafts and ideas
  assets/         # Images referenced by source files
wiki/             # LLM-generated and maintained pages (agent-owned)
  sources/        # Source summary pages (one per raw artifact)
  index.md        # Content catalog — updated on every ingest
  log.md          # Append-only chronological record
docs/             # Meta files (karpathy_gist.md, diagrams)
```

## Conventions

- **File names:** lowercase, hyphens, no spaces (e.g., `claude-code.md`, `kv-cache.md`)
- **Wikilinks:** `[[PageName]]` style for cross-references (Obsidian-compatible)
- **Flat structure:** Entity and concept pages live directly in `wiki/`, not in subdirectories. This keeps wikilinks short (`[[KV-Cache]]` not `[[concepts/KV-Cache]]`) and works cleanly in Obsidian's graph view.
- **Every wiki page** starts with YAML frontmatter (see below)
- **Minimum 2 outbound wikilinks** per page — isolated pages are invisible
- When updating a page, always bump the `updated` date
- Every new page must be added to `wiki/index.md` under the correct section
- Every action must be appended to `wiki/log.md`
- **Inbound sources section:** Each entity or concept page lists which source files support its claims. This is the provenance mechanism — section-level, not inline markers.

## Frontmatter

### Wiki pages (entities, concepts, comparisons, queries)

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query
tags: [from taxonomy below]
sources: [raw/path/to/source.md]
# Optional quality signals:
confidence: high | medium | low
contested: true
contradictions: [page-slug]
---
```

### Raw source files

The Obsidian Chrome plugin captures: `title`, `source`, `author`, `published`, `created`, `description`, `tags`. On ingest, the agent adds:

```yaml
ingested: YYYY-MM-DD
sha256: <hex digest of the markdown body (after frontmatter)>
```

The sha256 is computed over the body only, not the frontmatter. On re-check, the agent fetches the current URL content, hashes it, and compares. A mismatch means the source has drifted since clipping — flag for user review and potential re-ingest.

## Tag Taxonomy

- **Models:** model, architecture, benchmark, training, quantization
- **People/Orgs:** person, company, lab, open-source
- **Agent Systems:** agent_system, agent_enhancement, memory, skills, orchestration, governance
- **Developer Tools:** developer-tools, cli, ide, tool
- **Techniques:** optimization, fine-tuning, inference, alignment, data, context-engineering
- **Domain:** complexity-theory, llmops, trading
- **Meta:** comparison, controversy, prediction, readme
- **Personal:** personal, career

Rule: prefer existing tags. If a new tag is needed, add it here first.

## Page Thresholds

- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **Don't create a page** for passing mentions, minor details, or things outside the domain
- **Split a page** when it exceeds ~200 lines — break into sub-topics with cross-links
- **Archive a page** when its content is fully superseded — move to `_archive/`, remove from index

## Special Directories

### raw/Personal/

Contains the owner's own writing: career documentation, interview prep, project notes, and a personal profile for AI agents. This folder is **not processed like articles**. It is a primary source about the person, not external content to summarize.

When a file appears in `raw/Personal/`, treat it as authoritative first-person context about the owner. Use it to:
- Inform answers and wiki pages with accurate personal context
- Build or update a `wiki/Dan-Orlando.md` profile page when asked
- Source new article discovery — the owner's interests, projects, and goals described here should drive automated content recommendations once automation is set up

Do not run the standard ingest pipeline on these files. Do not create `wiki/sources/` pages for them.

## Design Decisions

These are settled choices. Follow them unless the user explicitly overrides.

**`raw/` is a curation record, not a mirror.** The purpose of `raw/` is to record what the user decided was worth their attention. Clipping something is the curation act itself.

**For repos, the README web clip is the raw artifact.** Clipping a repo's README signals "I found this worth saving." During ingest, fetch supplemental detail live (source files, docs, author blog posts) as needed. The wiki page is the durable artifact, not a raw dump.

**Live fetching during ingest is fine.** The wiki page becomes the permanent, synthesized record. The raw artifact is just the anchor.

**Drift detection via sha256.** Raw files get a sha256 hash on ingest. This enables the agent to detect when a source URL's content has changed since clipping, without requiring the agent to have done the original scrape. On lint or re-check, fetch the URL, hash, compare.

## Core Operations

### Ingest

When the user drops a new source into `raw/` and asks to process it:

1. Read the source (and any referenced images separately if needed)
2. Add `ingested` and `sha256` to the raw file's frontmatter
3. Discuss key takeaways with the user
4. Check what already exists — search index.md and use search_files to find existing pages for mentioned entities/concepts
5. Write a summary page in `wiki/sources/<slug>.md`
6. Create or update entity/concept pages (minimum 2 outbound wikilinks each)
7. Update `wiki/index.md` with new entries
8. Append to `wiki/log.md`: `## [YYYY-MM-DD] ingest | <Title>`

### Ingest (repo README variant)

When the source is a clipped README from a code repository:

1. Read the README; fetch supplemental detail live if needed
2. Focus extraction on **design decisions**, not feature lists:
   - What problem does it solve, and what's the core insight?
   - What's novel or non-obvious about how it works?
   - How does it handle the hard cases and edge cases?
   - What tradeoffs did the author make, and why?
3. Write the summary page in `wiki/sources/<slug>.md` emphasizing those decisions
4. Update `wiki/index.md` and `wiki/log.md` as with a standard ingest
5. Update relevant concept/entity pages — repos often have strong opinions that cross-cut many topics

### Query

When the user asks a question:

1. Read `wiki/index.md` to find relevant pages
2. Drill into those pages and synthesize an answer with citations
3. If the answer is non-trivial or reusable, offer to file it as a new wiki page

Good answers should be filed back into the wiki. Explorations should compound, not disappear into chat history.

### Lint

When asked to health-check the wiki, look for:
- Broken wikilinks (links to pages that don't exist)
- Orphan pages with no inbound links
- Contradictions between pages
- Stale claims superseded by newer sources
- Important concepts mentioned but lacking their own page
- Missing cross-references
- Source drift (sha256 mismatch — source URL content has changed since clipping)
- Data gaps that could be filled with a web search
- Pages over 200 lines (candidates for splitting)
- Tags not in the taxonomy
- Index completeness (pages missing from index)

## Update Policy

When new information conflicts with existing content:
1. Check the dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates and sources
3. Mark the contradiction in frontmatter: `contested: true`, `contradictions: [page-slug]`
4. Flag for user review

## index.md Format

One entry per wiki page, grouped by category (Sources, Entities, Concepts, Analyses):

```
## Sources
- [[sources/slug]] — One-line summary (YYYY-MM-DD)

## Entities
- [[PageName]] — One-line summary
```

## log.md Format

Append-only. Each entry starts with a parseable prefix:

```
## [YYYY-MM-DD] ingest | Article Title
## [YYYY-MM-DD] query | Question asked
## [YYYY-MM-DD] lint | Health check summary
```

This makes the log greppable: `grep "^## \[" wiki/log.md | tail -5` shows the last 5 operations.

When log.md exceeds 500 entries, rotate: rename to `log-YYYY.md`, start fresh.
