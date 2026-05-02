---
title: Failure-Aware Retrieval
created: 2026-05-02
updated: 2026-05-02
type: concept
tags: [model, optimization, alignment, agent_system]
sources: [raw/research_papers/Skill-RAG.md]
---

# Failure-Aware Retrieval

Failure-aware retrieval is a paradigm shift in RAG systems: instead of treating post-retrieval failure as a signal to **retry** (retrieve again with the same or lightly modified query), it treats failure as a signal to **diagnose** — identifying the structural cause of query–evidence misalignment and applying a targeted correction.

## Core Principle: Misalignment is Typed, Not Monolithic

Traditional adaptive RAG methods (see [[Adaptive-RAG]]) treat retrieval control as a coarse-grained decision — whether to retrieve and how many times. Failure-aware retrieval recognizes that persistent failures exhibit **structured patterns**:

- **Surface form divergence**: Query vocabulary doesn't match corpus indexing → query rewriting
- **Entangled premises**: Multi-hop questions treated as single queries → question decomposition
- **Semantic breadth**: Query too broad, evidence too shallow → evidence focusing
- **Irreducible gaps**: Missing knowledge or model capacity limits → graceful exit

These failure types have **geometric structure** in the model's hidden-state representation space. t-SNE projections show separable clusters for fixable vs. irreducible failures. This structure is what makes targeted routing possible.

## Hidden-State Probing

The diagnostic mechanism relies on probing the model's internal representations. Key properties:

- Hidden states from the posterior layers carry answer-readiness signals
- A lightweight feed-forward classifier can detect "failure states" — when the model's current evidence is insufficient
- Probers trained on one set of tasks can generalize to OOD datasets (though skill routing adds further robustness)

See [[Context-Engineering]] for how this relates to deliberate design of what enters an LLM's context window.

## Skill Vocabulary Parsimony

A critical finding: the geometric structure that enables typed diagnosis **collapses** when the skill vocabulary exceeds ~6 skills. Over-diversified skill sets cause failure clusters to merge, destroying the separability needed for targeted routing. This suggests the failure space has intrinsic low dimensionality — the four-skill taxonomy in [[sources/skill-rag|Skill-RAG]] may be near-optimal.

## Contrast with Retry-Based Approaches

| Approach | On Failure | Risk |
|----------|-----------|------|
| Naive re-retrieval | Retrieve again with same query | Same irrelevant evidence |
| Context-concatenation | Append prior context to query | Query drift to off-topic |
| Failure-aware | Diagnose failure type → apply corrective skill | None if diagnosis is accurate |

Naive retry approaches suffer from **query drift** — concatenating prior failed context causes the query to wander to unrelated topics (demonstrated in Skill-RAG's My Hero Academia case study).

## Connection to Agent Systems

Failure-aware retrieval mirrors patterns in [[Agent-Memory]] and [[Self-Evolving-Skills]]: agents that learn from failure rather than simply retrying. The prober + router pattern is analogous to an agent that detects its own incompetence on a task and selects an appropriate remediation strategy. This connects to broader themes in [[Context-Engineering]] — the prober is essentially a meta-cognitive monitor over the generation context.

## Inbound Sources

- `raw/research_papers/Skill-RAG.md` (primary)
