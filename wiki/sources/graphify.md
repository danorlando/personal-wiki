---
title: "Graphify"
created: 2026-04-26
updated: 2026-04-26
type: summary
tags:
  - [knowledge-graph, claude-code, token-efficiency, tree-sitter, leiden, obsidian, karpathy]
---

# Graphify

One-line summary: A Claude Code skill that converts any folder (code, docs, papers, images) into a queryable knowledge graph and installs a PreToolUse hook so the agent navigates by graph structure instead of keyword search.

## Problem it solves

When an agent needs to understand a large codebase or document corpus, the default behavior is Glob/Grep: keyword search over raw files. This is expensive in tokens (every file read costs), fragile (renames break searches), and opaque (the agent doesn't know what it doesn't know). Karpathy's `/raw` folder practice — clipping sources into a directory — creates exactly this problem at scale: the raw files are there, but navigating them is expensive. The README cites this directly.

## Core architectural insight

The core insight is that **the graph is the compression**. On a 52-file corpus, graph-mediated queries use 71.5x fewer tokens than reading raw files. The graph encodes structure, relationships, and rationale that would otherwise require reading many files to reconstruct.

The extraction pipeline makes two careful distinctions:

**Two-pass extraction by source type:**
1. Deterministic AST extraction via tree-sitter for code (19 languages) — no LLM required, no hallucination risk on the structural layer
2. Claude subagents in parallel for docs, papers, and images — LLM handles semantics where there's no grammar to parse

This split is principled: code structure is computable; document semantics are not. Mixing them into one LLM pass wastes the reliability of the deterministic layer.

**Three relationship confidence tiers:**
- `EXTRACTED` — found directly in source
- `INFERRED` (with confidence score 0.0–1.0) — derived by the LLM; should be treated as hypothesis
- `AMBIGUOUS` — flagged for human review

This matters because graph queries are only as useful as the graph's epistemic labeling. An `INFERRED` edge with confidence 0.3 should be weighted differently than an `EXTRACTED` edge.

**Leiden community detection** runs on graph topology directly — no embeddings. Because semantic similarity edges (`INFERRED`) are already in the graph, Leiden clusters by both structural and semantic proximity without a separate embedding pass. Communities become navigational units: "auth flow," "rendering pipeline," "test infrastructure."

The **PreToolUse hook** is the behavioral payoff. It fires before every Glob/Grep call and injects: "read GRAPH_REPORT.md before searching raw files." This redirects the agent's default behavior at the tool level — no prompt engineering, no per-task instruction. The hook is architectural, not advisory.

Additional non-obvious features: **hyperedges** group 3+ nodes (all classes implementing a protocol); **rationale nodes** capture `# NOTE:`, `# WHY:`, `# IMPORTANT:` comments as first-class graph entities, preserving the "why" behind code that otherwise disappears into diffs.

## Key capabilities

- 71.5x token reduction on 52-file corpus (benchmark result in README)
- Outputs: `graph.html` (interactive), `graph.json` (queryable), `GRAPH_REPORT.md` (plain-language audit), SHA256 cache for incremental updates
- MCP server mode: `python -m graphify.serve graph.json` for structured access from other tools
- `--obsidian` flag generates Obsidian vault directly
- 19 language support via tree-sitter; parallel Claude subagents for non-code content

## Tradeoffs and limitations

- Initial graph build is expensive: parallel LLM subagents for large corpora means significant API cost and latency
- SHA256 cache helps with incremental updates, but schema changes (new relationship types) may invalidate the cache
- Leiden community detection is non-deterministic at the margin — communities may shift between runs on the same graph if edge weights change
- `INFERRED` edges depend on LLM extraction quality; a bad extraction run pollutes the graph with false relationships
- The PreToolUse hook redirects all Glob/Grep calls, which may be overly aggressive for simple lookups where graph navigation is slower

## Relation to other work

Graphify directly cites the [[sources/karpathy-gist]] practice as the problem it solves — making it the only repo in this set explicitly positioned against that workflow. The knowledge graph approach overlaps with [[sources/hindsight]]'s graph-based retrieval, but Hindsight builds its graph from agent interactions at runtime while Graphify builds it from static source artifacts at ingest. The Obsidian export connects to this wiki's own [[WikiLinks]] conventions.

## Inbound sources

- [[sources/graphify]] ← this page
