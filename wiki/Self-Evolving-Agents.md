---
title: "Self-Evolving Agents"
created: 2026-05-02
updated: 2026-05-02
type: concept
tags:
  - concept
  - agent_system
  - self-improvement
  - orchestration
---

# Self-Evolving Agents

Agents that modify their own components — prompts, tools, memory, even architectural structure — based on execution feedback, without human intervention. The shift is from predefined execution to dynamic adaptation: the system that runs the agent also improves it.

## The Core Problem

Static agent designs fail when facing real-world diversity and stochasticity. Existing protocols like [[MCP]] and [[A2A]] solve connectivity (invocation, communication) but leave lifecycle management, version tracking, and safe update interfaces under-specified. Without these, self-modification risks runtime instability, irrecoverable errors, and untraceable changes.

## Two Architectural Approaches

### Protocol-Level: Autogenesis (AGP)

The [[sources/autogenesis|Autogenesis]] protocol decouples **what evolves** (RSPL resources: prompts, agents, tools, environments, memory) from **how evolution occurs** (SEPL: Reflect → Select → Improve → Evaluate → Commit). Every mutation passes through a commit gate that enforces safety invariants and performance monotonicity. Failed updates roll back cleanly; successful ones carry auditable lineage.

Key constraint: RSPL resources are **passive** — they cannot self-modify. All evolution happens through the SEPL operator interface. This makes the process composable, traceable, and safe-by-construction.

### Skill-Level: OpenSpace

[[Self-Evolving-Skills]] takes a narrower scope, evolving executable skill packages (FIX/DERIVED/CAPTURED mutations) triggered by three independent monitors (post-execution, tool degradation, metric thresholds). The unit of evolution is the skill, not the full agent stack.

## What Actually Evolves

Empirical data from both systems shows a consistent pattern: the system primarily learns **execution reliability**, not domain competence. OpenSpace's GDPVal benchmark found that auto-evolved skills cluster around file I/O edge cases and error recovery. Autogenesis shows the largest gains on the hardest task tiers (GAIA Level 3: +33.3%), where tool chains fail in complex ways that reflection can diagnose and repair.

## Safety Mechanisms

Self-modification without safeguards is dangerous. Both approaches implement:

- **Commit/gate mechanisms** — no change accepted without verification (SEPL's Commit operator, OpenSpace's validation-before-replacement)
- **Rollback** — failed evolution attempts restore previous state without side effects
- **Version lineage** — every change is tracked with predecessor links
- **Learnability constraints** — not everything should evolve; explicit masks define the trainable subspace

## Relation to Other Concepts

- [[Agent-Skills]] — skills are one of the five RSPL resource types that can evolve under Autogenesis; they are also the sole unit of evolution in OpenSpace
- [[Multi-Agent-Orchestration]] — Autogenesis uses an Agent Bus architecture where evolved resources become immediately available to all sub-agents; the orchestration plan itself is a versioned, evolvable resource
- [[Self-Evolving-Skills]] — the skill-level specialization of self-evolution; Autogenesis generalizes the concept to the full agent stack
- [[Agent-Governance]] — governance sits above self-evolution, enforcing policy constraints; the SEPL commit gate is a governance mechanism at the protocol level
- [[Agent-Protocol]] — the protocol-level standardization that makes self-evolution composable and interoperable

## Inbound Sources

- [[sources/autogenesis]]
- [[sources/openspace]]
- [[sources/hermes-agent]]
