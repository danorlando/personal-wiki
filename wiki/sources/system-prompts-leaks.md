---
title: "system prompts leaks"
created: 2026-04-26
updated: 2026-04-26
type: summary
tags:
  - repository
  - prompts
  - agent_dev
  - OSS
  - llm_internals
source: https://github.com/asgeirtj/system_prompts_leaks
---

A community-maintained, regularly updated archive of extracted system prompts from major AI products — ChatGPT (GPT-5.4, GPT-5.3, Codex), Claude (Opus 4.6, Sonnet 4.6, Claude Code), Gemini (3.1 Pro, 3 Flash, CLI), Grok (4.2, 4), Perplexity, and a growing miscellaneous category covering products like Notion AI, Raycast AI, Warp 2.0 Agent, and GitHub Copilot.

## Key Design Decisions

**Extraction as primary artifact.** The repo's value is raw system prompt text, not analysis or commentary. Each file is a markdown document containing the verbatim (or near-verbatim) prompt as extracted, organized by provider and model. The design decision is to prioritize completeness and freshness over curation — the index is a table of links, not a synthesis.

**Provider-model hierarchy as taxonomy.** Files are organized by company (Anthropic, OpenAI, Google, xAI, Perplexity, Misc), then by model or product variant within each. This makes it easy to find a specific prompt but does not facilitate cross-provider comparison out of the box. The `Misc` category catches products that use third-party models under the hood (Notion AI, Raycast AI, Warp), which is itself a signal: many products are thin wrappers with custom system prompts.

**Tool-level granularity for OpenAI.** The OpenAI section breaks out not just model versions but individual tool prompts — web search, deep research, Python, Canvas, image generation, memory/bio, file search. This reflects how modern LLM products are assembled from composable tool-specific prompt layers rather than monolithic system prompts.

**Personality variants as first-class entries.** GPT-5.1 personality variants (Default, Friendly, Professional, Candid, Cynical, Efficient, Nerdy, Quirky) each get their own file. This is notable: it documents that model personality differentiation is implemented at the prompt level, not the weights level — a meaningful architectural observation about how consumer AI products are actually built.

**Community-sourced, PR-driven.** The README invites PRs for new models with a simple convention: drop the raw text as a `.md` in the appropriate folder. This lowers contribution friction to near zero and is the mechanism by which the repo stays current across a rapidly changing landscape.

**Notable absence: analysis.** The repo does not include commentary on what these prompts reveal about each provider's values, safety approach, or behavioral constraints. That interpretive layer is left entirely to the reader.

## Notable Patterns

- Claude Code has its own dedicated entry, separate from Claude.ai — confirming that the agentic coding context receives a distinct, purpose-built system prompt.
- The Anthropic section includes `claude.ai-injections.md` separately from the main system prompt, suggesting Claude's deployed behavior is assembled from multiple prompt layers, not a single document.
- The `Default Styles` entry for Anthropic captures formatting/response-style instructions as a distinct artifact from behavioral instructions.
- The repo's Trendshift badge and star growth chart indicate it reached significant GitHub traction quickly — a sign that system prompt transparency is a high-interest area for developers and researchers.

## Concepts touched

- [[Claude-Code]] — Claude Code's system prompt is a direct entry; understanding it informs how the tool positions itself to the model
- [[Agent-Native-Software]] — the tool-level granularity of OpenAI prompts illustrates how agentic products compose behavior from stacked prompt layers
- [[Agent-Skills]] — tool-specific prompts (web search, Python, Canvas) are functionally analogous to skills — discrete behavioral modules activated by context
- [[Agent-Memory]] — OpenAI's `tool-memory-bio.md` entry documents how persistent memory is implemented at the prompt layer
