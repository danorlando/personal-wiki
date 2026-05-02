---
title: "Event Sourcing"
created: 2026-04-26
updated: 2026-04-26
type: concept
tags:
  - architecture
  - agent_system
  - memory
sources:
  - raw/research_papers/Stateless Decision Memory for Enterprise AI Agents.md
---

# Event Sourcing

Event sourcing is a distributed systems pattern in which an **immutable append-only event log** is the authoritative state, and every derived view is a **pure projection** over the log. The pattern originates in Martin Fowler's 2005 formulation and is the engineering substrate under most regulated financial systems (settlement, double-entry ledgers, claim histories).

## Core Pattern

Instead of storing current state and mutating it, event sourcing:

1. **Appends** every state-changing event to an immutable log
2. **Derives** any needed view by projecting over the log at read time
3. **Never mutates** — the log is the single source of truth; derived views are ephemeral

This inverts the typical CRUD model. There is no "update" operation — only "append" and "reconstruct."

## Why It Matters for Agents

Applied to agent memory, event sourcing resolves the architectural tension between stateful memory's decision-quality advantages and retrieval's enterprise-deployability. [[Deterministic-Projection-Memory]] is a direct application: the agent's trajectory is the event log, and the memory view at decision time is a projection over that log.

The key insight: **event sourcing gives you the operating properties of retrieval (statelessness, auditability, determinism) without sacrificing the decision quality of richer memory architectures** — because the full event history is always available for projection.

## Enterprise Properties from Event Sourcing

| Property | How Event Sourcing Provides It |
|----------|-------------------------------|
| Deterministic replay | Replay the same log through the same projection → same result |
| Auditability | Every event is retained; projections cite event indices |
| Multi-tenant isolation | Each tenant has their own log; no shared mutable state |
| Horizontal scale | Projections are stateless functions; no per-request affinity needed |

## Inbound Sources

- [[sources/stateless-decision-memory]]
