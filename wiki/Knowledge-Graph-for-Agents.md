---
title: "Knowledge Graph for Agents"
created: 2026-04-26
updated: 2026-04-26
type: concept
tags:
  - concept
  - agents
  - knowledge-graph
  - context
  - retrieval
---

# Knowledge Graph for Agents

Using knowledge graphs as an intermediate representation between raw files and agent context. The core claim: a graph built from a codebase or document corpus is a better interface for agent navigation than either raw files or RAG retrieval.

## The Problem with the Alternatives

**Raw files** are expensive. An agent that reads every file to understand a codebase burns context proportionally to corpus size. On a 52-file codebase, reading everything naively might cost 100K tokens before the agent has even started the task.

**RAG** (retrieval-augmented generation) retrieves flat, opaque slices. The agent gets chunks ranked by embedding similarity to a query, with no structural awareness. It doesn't know that two chunks are from the same module, that a function is called by 40 other functions, or that a concept appears in docs but not in code. RAG answers "what text is similar to this query?" — it doesn't answer "what is architecturally central to this system?"

A knowledge graph answers a different question: **what is this system, and how is it organized?**

## Graphify's Approach

Graphify builds a graph from a corpus using a two-pass extraction process:

**Pass 1 — Structural extraction (AST):** For code files, parse the abstract syntax tree to extract functions, classes, imports, and call relationships with high precision. These edges are tagged `EXTRACTED` — they're definitionally correct.

**Pass 2 — Semantic extraction (LLM subagents):** For documentation, papers, and images, run LLM subagents that read the content and identify concepts, relationships, and cross-references. These edges are tagged `INFERRED` (confident interpretation) or `AMBIGUOUS` (uncertain) — the confidence tagging is explicit and preserved in the graph.

The combination matters: code relationships are structural facts; doc relationships are semantic interpretations. Keeping them separate, and tagging confidence, means the agent knows how much to trust each edge.

### Leiden Community Detection

After extraction, Graphify runs Leiden community detection on the graph topology to identify clusters — groups of nodes that are more densely connected to each other than to the rest of the graph. This surfaces the natural modules of the system without relying on directory structure or naming conventions.

Critically, this uses **no embeddings** — community structure is derived entirely from link topology. This makes it deterministic and fast, and avoids the brittleness of embedding-based clustering.

### What the Graph Adds Over RAG

| Feature | RAG | Knowledge Graph |
|---------|-----|-----------------|
| Structural relationships | No | Yes (call graphs, import chains) |
| Centrality (god nodes) | No | Yes (highest-degree concepts) |
| Cross-file connections | Implicit | Explicit, surfaced |
| Group relationships | No | Hyperedges (3+ node) |
| Rationale / WHY comments | Lost in chunking | Extracted as `rationale_for` nodes |
| Confidence on edges | No | Yes (`EXTRACTED`/`INFERRED`/`AMBIGUOUS`) |
| Surprising connections | Missed | Surfaced by topology |

**God nodes** — the highest-degree concepts in the graph — are particularly useful for agents. They're the concepts everything else refers to. Knowing them upfront is architecturally more informative than any keyword search.

**Hyperedges** capture relationships that can't be expressed as binary edges — "these three modules jointly implement the authentication flow" is a 3-node relationship that binary edges can't represent cleanly. Graphify preserves these.

**`rationale_for` nodes** extract WHY comments from code and documentation and link them to the entities they explain. Comments like `// We use a write-ahead log here because...` are typically lost in chunking; as graph nodes they're first-class retrievable objects.

### The Token Reduction

On a 52-file corpus, Graphify's benchmark shows a **71.5x token reduction** — the graph representation carries the structural information of the corpus in 1/71st of the tokens. The graph is the compression; the compression is the intelligence.

## The Always-On Hook Pattern

Graphify installs not just as a callable skill but as a **PreToolUse hook** on Glob and Grep operations. Every time the agent would search the codebase by filename or keyword, the hook fires first and surfaces `GRAPH_REPORT.md` — a precomputed summary of the graph: communities, god nodes, confidence distribution, notable cross-file connections.

The effect: the agent navigates by structure rather than by keyword matching. Instead of "find all files containing `auth`," the agent sees "the authentication community is nodes A, B, C, and D; A is a god node with 47 inbound edges; D is ambiguously connected to the payments community." This is architecturally richer than any Grep result.

This is a bet that **mandatory context** beats **optional context**. The hook doesn't wait for the agent to decide to query the graph — it ensures the graph is always consulted before any search. See [[Skills-Ecosystem]] for the broader pattern of hook-installed skills.

## OpenViking's Alternative Bet

OpenViking (see [[Agent-Memory]]) takes a structurally different approach to the same problem. Rather than building a graph over the corpus, it organizes memory as a hierarchical filesystem with `viking://` URIs and tiered loading.

The contrast:

| Dimension | Graphify | OpenViking |
|-----------|----------|------------|
| Structure | Graph topology | Filesystem hierarchy |
| Navigation | Centrality / community | Explicit URI traversal |
| Determinism | Probabilistic (LLM extraction) | Deterministic |
| Writeable | Read-only corpus analysis | Read/write memory |
| Focus | Existing codebases / docs | Agent's own accumulated context |

Graphify analyzes a corpus the agent didn't create. OpenViking structures context the agent accumulates over time. They're solving adjacent problems: Graphify is about reading existing systems efficiently; OpenViking is about building a durable memory the agent can navigate reliably.

The deeper difference is the probabilistic vs. deterministic bet. Graphify accepts that LLM-extracted edges are uncertain (hence confidence tags) and manages that uncertainty explicitly. OpenViking treats uncertainty as a bug — the filesystem paradigm is specifically designed to be navigable without probabilistic retrieval.

## Inbound Sources

- [[sources/graphify]]
- [[sources/openviking]]
