---
title: "Hindsight (Vectorize.io)"
created: 2026-04-26
updated: 2026-04-26
type: summary
tags:
  - [agent-memory, rag, knowledge-graph, benchmarks, vectorize, longmemeval]
---

# Hindsight (Vectorize.io)

One-line summary: An agent memory system that distinguishes learning from recalling, built on a biomimetic three-layer model (World / Experiences / Mental Models) with SOTA results on LongMemEval.

## Problem it solves

Most agent memory systems are vector stores over conversation history: when an agent needs to remember something, it embeds the query and retrieves the nearest past messages. This is retrieval, not learning. It means agents repeat the same mistakes across sessions, never synthesize patterns from accumulated experience, and treat a sales call from last year the same as one from yesterday. The context window grows, but understanding doesn't.

## Core architectural insight

Hindsight's design bet is that **memory should be structured like cognition, not like search**. It defines three memory types:

- **World** — objective facts (customer names, product specs, dates)
- **Experiences** — the agent's own past actions and their outcomes
- **Mental Models** — higher-order abstractions formed by reflecting on Experiences

The third tier is the novel one. A sales agent that stores every call outcome in Experiences can later Reflect on those records to form a Mental Model: "messages that open with pricing get ignored; messages that open with a use case get responses." That Mental Model is then available for future Recall without re-processing all underlying data.

This is operationalized through three named operations:

- **Retain**: LLM extracts facts, entities, and relationships from new content → normalization → canonical entity registry + time series + search indexes
- **Recall**: Four parallel strategies (semantic vector search, BM25 keyword, graph traversal, temporal range query) merged with reciprocal rank fusion, then reranked with a cross-encoder. No single retrieval strategy wins across all query types; parallelism + fusion beats any single approach
- **Reflect**: On-demand synthesis pass over stored Experiences → produces new Mental Models that become first-class memory entries

The four-strategy Recall is a meaningful engineering choice: semantic search misses exact names; BM25 misses paraphrases; graph traversal misses isolated facts; temporal search misses atemporal relationships. Running all four and fusing is more expensive but far more robust.

## Key capabilities

- SOTA on LongMemEval benchmark, independently reproduced by Virginia Tech and The Washington Post — external reproduction is a credibility signal worth noting
- **2-line integration** via LLM Wrapper that swaps the existing LLM client; no architectural rework required
- Memory banks for isolation: per-user and per-agent namespacing prevents cross-contamination
- Deployable via Docker or Python embedded mode (no server); Python and Node.js SDKs
- The Reflect operation can be triggered on-demand or scheduled — "why are my messages not getting responses" is a query Reflect can answer by synthesizing Experiences, not just retrieving them

## Tradeoffs and limitations

- Retain requires an LLM pass per new memory item — higher latency and cost than pure embedding
- The entity normalization step (canonical entity registry) will have false positives and false negatives for ambiguous names; the quality of the knowledge graph depends on LLM extraction quality
- Mental Models formed by Reflect are only as good as the Experiences they're built from; sparse or biased experience data produces misleading models
- No information about how graph retrieval handles very large knowledge graphs — scalability at millions of nodes is unstated

## Relation to other work

The three-tier memory model (World / Experiences / Mental Models) is thematically distinct from [[sources/openviking]]'s filesystem-URI approach, which solves context organization rather than memory learning. Hindsight's graph-based retrieval overlaps with [[sources/graphify]]'s knowledge graph construction, but Graphify targets codebase understanding at ingest time while Hindsight builds its graph incrementally from agent interactions. The Reflect operation is the closest thing in any of these repos to what [[sources/openspace]] calls "evolution" — both synthesize new knowledge from accumulated experience.

## Inbound sources

- [[sources/hindsight]] ← this page
