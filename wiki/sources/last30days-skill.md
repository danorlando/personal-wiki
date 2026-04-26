---
tags:
  - repository
  - research
  - skill
  - agent_dev
  - claude_code
updated: 2026-04-26
source: https://github.com/mvanhorn/last30days-skill
---

A Claude Code (and Codex CLI) skill that researches any topic across up to 10 live sources — Reddit, X/Twitter, YouTube, Hacker News, Polymarket, Bluesky, TikTok, Instagram, web search — scoring, deduplicating, and synthesizing results into a grounded narrative with real citations, typically taking 2–8 minutes per run.

## Key Design Decisions

**Two-phase search architecture.** Phase 1 is broad parallel discovery across all configured sources. Phase 2 is targeted supplemental search: the engine extracts `@handles` and subreddit names from Phase 1 results and runs follow-up queries against those specific accounts and communities. This catches high-signal content that keyword search misses entirely — e.g., a viral tweet from a creator whose post never mentions the topic by name. Phase 2 is skipped in `--quick` mode and extended in `--deep` mode, giving the user explicit control over the speed/depth tradeoff.

**Progressive source unlocking as a design pattern.** Three sources (Reddit public JSON, Hacker News via Algolia, Polymarket via Gamma API) work with zero configuration — no API keys, no setup. Additional sources are unlocked incrementally as users add credentials: browser cookies for X (auto-extracted by a setup wizard), `yt-dlp` for YouTube, `EXA_API_KEY` for semantic web search, `SCRAPECREATORS_API_KEY` for Reddit enrichment + TikTok + Instagram, `BSKY_HANDLE`/`BSKY_APP_PASSWORD` for Bluesky. The design avoids the common tool trap of requiring full configuration before any value is delivered.

**Multi-signal composite scoring.** Every result runs through a shared scoring pipeline regardless of source: bidirectional text similarity with synonym expansion, engagement velocity normalization, source authority weighting, temporal recency decay, and cross-platform convergence detection (when the same story appears on multiple platforms, it is flagged as a stronger signal). Polymarket markets get a separate 5-factor weighted composite (text relevance 30%, 24-hour volume 30%, liquidity depth 15%, price velocity 15%, outcome competitiveness 10%). The tradeoff is complexity — this is a sophisticated scoring system for a research tool, not a simple aggregator.

**Prediction markets as a first-class signal source.** Polymarket integration is notable: it surfaces what people are betting real money on alongside what they are saying. The two-pass query expansion with tag-based domain bridging addresses a hard problem — a topic like "Arizona basketball" appears as an *outcome* inside broader "NCAA Tournament" markets, not as a top-level market title. The engine does a first-pass keyword search, extracts domain tags from results, then runs a second-pass on those tags to surface markets the Gamma API cannot find by title alone.

**Neg-risk binary market synthesis.** Polymarket structures multi-outcome events (e.g., "which team wins") as separate Yes/No markets per entity. The skill detects this pattern and synthesizes a unified display ("Arizona: 12%, Duke: 18%") rather than showing raw "Yes: 12%, No: 88%" for each sub-market — a significant UX improvement that required understanding Polymarket's data model.

**Auto-save to a personal research library.** Every run saves the complete briefing as a topic-named `.md` file to `~/Documents/Last30Days/`. The open variant persists findings to SQLite for watchlists, briefings, and full-text history queries. The design frames the skill as a compounding knowledge asset, not a one-shot lookup.

**Comparative mode with parallel research passes.** "X vs Y" queries trigger 3 parallel research passes and produce a structured side-by-side comparison with strengths, weaknesses, a head-to-head table, and a data-driven verdict. This is built into the skill invocation pattern, not a post-hoc formatting choice.

**Model fallback chain.** Reddit search (which uses OpenAI's Responses API with web search) automatically falls back through `gpt-4.1 → gpt-4o → gpt-4o-mini` if a model is unavailable. This makes the skill robust to API access tier differences without requiring user configuration.

## Notable Patterns

- The skill is cross-agent: the same Python engine and `SKILL.md` work in Claude Code (installed to `~/.claude/skills/`), OpenAI Codex CLI (installed to `~/.agents/skills/`), and Gemini CLI (via extensions). The host agent provides the invocation interface; the Python engine does the actual work.
- X/Twitter access uses auto-extracted browser cookies rather than API credentials (which became expensive/restricted). The setup wizard reads cookies from Chrome, Firefox, and Safari silently — no manual extraction required.
- Smart subreddit discovery uses `frequency × recency × topic-word match` scoring to find the right communities, not just the most frequently mentioned ones. A `UTILITY_SUBS` blocklist filters generic subreddits (r/tipofmytongue, r/whatisthisthing) that have high frequency but low topic relevance.
- Top Reddit comments carry a 10% weight in the engagement scoring formula and are displayed inline with upvote counts — a recognition that comment-layer insights often exceed post-layer insights in research value.
- The README is itself a research artifact: every example shows actual output (quoted text, engagement stats, generated prompts), not screenshots or marketing copy. This makes the quality of synthesis directly verifiable.

## Concepts touched

- [[Agent-Skills]] — canonical example of a Claude Code skill: a SKILL.md-driven, Python-backed, installable capability that extends the base agent
- [[Claude-Code]] — primary deployment target; the skill integrates with Claude Code's plugin marketplace and session lifecycle hooks
- [[Self-Evolving-Skills]] — the watchlist/briefing open variant, paired with cron and SQLite persistence, illustrates how skills can compound knowledge over time
- [[Agent-Memory]] — the auto-save to `~/Documents` and SQLite accumulation are lightweight external memory patterns for agent workflows
- [[Skills-Ecosystem]] — demonstrates the cross-agent portability pattern: one skill engine, multiple agent hosts
