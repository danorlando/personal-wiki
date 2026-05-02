---
title: Adaptive RAG
created: 2026-05-02
updated: 2026-05-02
type: concept
tags: [model, optimization, architecture, agent_system]
sources: [raw/research_papers/Skill-RAG.md]
---

# Adaptive RAG

Adaptive RAG refers to the family of retrieval-augmented generation methods that dynamically determine **when**, **how often**, and **how** to retrieve, as opposed to single-step retrieval-before-generation. The adaptive RAG spectrum ranges from retrieval timing control to failure-type routing.

## Spectrum of Adaptivity

| Method | What It Adapts | Signal | Granularity |
|--------|---------------|--------|-------------|
| **Vanilla RAG** | Nothing — always retrieve once | N/A | None |
| **FLARE** | When to retrieve | Token-level generation confidence | Token |
| **DRAGIN** | When to retrieve | Attention-based relevance signals | Token |
| **Self-RAG** | Whether to retrieve + self-critique | Learned special tokens | Segment |
| **Adaptive-RAG** (Jeong et al.) | Strategy depth | Query complexity classifier | Query |
| **Probing-RAG** | Whether to retrieve | Hidden-state probing | Query |
| **Skill-RAG** | Corrective skill selection | Failure-state diagnosis | Failure type |

See [[Failure-Aware-Retrieval]] for the paradigm shift from retry-based to diagnosis-based adaptation.

## Adaptive-RAG (Jeong et al. 2024)

The specific method "Adaptive-RAG" classifies query complexity (simple, medium, complex) and routes to retrieval strategies of varying depth. This is **pre-retrieval adaptation** — the decision is made before any retrieval happens, based solely on the query.

Limitation: doesn't address what happens when retrieval fails. A complex query routed to a deep retrieval strategy can still produce misaligned evidence.

## Skill-RAG's Extension: Post-Retrieval Adaptation

Skill-RAG extends the adaptive paradigm by adding **post-retrieval diagnosis**. Where Adaptive-RAG classifies queries before retrieval, Skill-RAG classifies failures after retrieval. This is a fundamentally different adaptation point:

- **Pre-retrieval**: "How hard will this query be?" → select retrieval depth
- **Post-retrieval**: "Why did retrieval fail?" → select corrective skill

The two are complementary — an ideal system might use pre-retrieval complexity routing and post-retrieval failure routing.

## Iterative Retrieval Methods

Several methods interleave retrieval with generation:

- **IRCoT**: Chain-of-thought reasoning guides retrieval; each reasoning step generates the next query
- **Iter-RetGen**: Previous model output becomes context for next retrieval round
- **FLARE**: Active retrieval triggered by low-confidence token generation

These are iterative but don't diagnose failure types — they just keep retrieving. See [[Context-Engineering]] for how iterative retrieval relates to managing what enters the context window.

## Connection to Broader Agent Patterns

Adaptive retrieval parallels patterns in [[Multi-Agent-Orchestration]] — routing tasks to specialized agents based on task characteristics. The skill router in [[sources/skill-rag|Skill-RAG]] is essentially a task router that dispatches to specialized retrieval "agents" (skills). This connects to [[Self-Evolving-Skills]] in that the skill vocabulary could potentially grow through experience, though Skill-RAG's finding that >6 skills collapses representational structure suggests hard limits on vocabulary expansion.

## Open Questions

- Can pre-retrieval complexity routing and post-retrieval failure routing be unified in a single framework?
- Does the four-skill taxonomy hold for non-QA domains (scientific literature, code retrieval, multilingual)?
- How does skill routing interact with dense retrieval (vs. BM25)?

## Inbound Sources

- `raw/research_papers/Skill-RAG.md` (primary)
