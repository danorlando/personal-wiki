---
title: "Deterministic Projection Memory"
created: 2026-04-26
updated: 2026-04-26
type: concept
tags:
  - memory
  - architecture
  - agent_system
  - governance
sources:
  - raw/research_papers/Stateless Decision Memory for Enterprise AI Agents.md
---

# Deterministic Projection Memory (DPM)

DPM is a memory architecture for enterprise AI agents that treats memory as an **append-only event log plus a single task-conditioned projection at decision time**. It applies the [[Event-Sourcing]] pattern from distributed systems to agent memory, resolving the tension between stateful memory's decision-quality advantages and retrieval's enterprise-deployability.

## Architecture

Two components only:

1. **Append-only event log** E = (e₁, e₂, …, eₙ) — accumulates raw events (document chunks, tool outputs, user messages, intermediate inferences) in arrival order. Immutable: once written, never edited, summarized, or overwritten. The single durable representation of the trajectory.
2. **Task-conditioned projection** π(E, T, B) → M — at decision time (and only at decision time), the full event log, task specification, and memory budget are passed to a single LLM call at temperature zero. The output is a structured memory view organized into:
   - **Facts** — discrete verifiable anchors (dollar amounts, dates, identifiers) with event-index citations
   - **Reasoning** — inference steps referencing the facts
   - **Compliance notes** — regulatory-relevant provisions implicated

The consolidation operator U is the identity. **Memory does not exist as a distinct runtime object until π is applied.**

## Why It Works for Enterprise

DPM satisfies four enterprise properties **by construction** (not by retrofit):

| Property | How DPM Satisfies It |
|----------|---------------------|
| Deterministic replay | Replay requires only (E, T, B, model version) — no intermediate state to reconstruct |
| Auditable rationale | Audit surface is one LLM call; rationale fragments cite event indices |
| Multi-tenant isolation | π takes E as explicit argument — no shared memory store across tenants |
| Statelessness | π is a pure function of (E, T, B) conditional on model version — no hidden state, horizontal scaling is trivial |

Stateful architectures (MemGPT, H-MEM, GAM, A-Mem) can retrofit these properties but each retrofit compounds engineering cost and operational burden. DPM inherits them by construction.

## Performance Profile

- **At generous budgets** (≤5× compression): matches summarization-based memory on all decision-alignment axes (no significant difference)
- **At tight budgets** (20× compression): strictly outperforms — FRP +0.52 (Cohen's h=1.17), RCS +0.53 (h=1.13)
- **Speed**: 7–15× faster than stateful baseline (1 LLM call vs 82–96)
- **Cost**: ~10× cheaper per decision at binding budgets

The compounding-loss mechanism: incremental summarization discards content at each step; discards compound across the trajectory. DPM never consolidates, so no compounding occurs.

## What DPM Is Not

- **Not a hierarchical memory system** — single-level projection over a flat event log; hierarchical projection for longer trajectories is future work
- **Not a replacement for retrieval** — DPM handles trajectory memory; corpus-level knowledge bases still need retrieval, and the two coexist
- **Not a claim of bit-exact replay on live APIs** — reduces replay surface from N calls to one, but residual API nondeterminism remains; full bit-exact replay requires pairing with a deterministic inference runtime

## The Structural Asymmetry

Stateful memory: mₖ = U(mₖ₋₁, eₖ) — a chain of N LLM calls, each with residual nondeterminism, each an audit surface, each a state mutation requiring multi-tenant scoping.

DPM: one function from (E, T, B) to a memory view, applied once. The audit surface, replay surface, and isolation surface all shrink to the single projection.

## TAMS Decision Rule

Task-Adaptive Memory Selection — when to choose DPM:
1. If deployment requires deterministic replay, audit-ready rationale, or multi-tenant isolation → DPM
2. Else if compression ratio exceeds ~10× → DPM
3. Else → either architecture acceptable; choose by operational preference

## Connections

- [[Agent-Memory]] — DPM's place among memory architectures for agents
- [[sources/stateless-decision-memory]] — the paper that introduced DPM
- [[Agent-Governance]] — the enterprise properties DPM satisfies overlap with governance requirements
- [[Event-Sourcing]] — the distributed systems pattern DPM directly applies

## Inbound Sources

- [[sources/stateless-decision-memory]]
