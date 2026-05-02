---
title: "Autogenesis: A Self-Evolving Agent Protocol"
created: 2026-04-26
updated: 2026-04-26
type: summary
tags:
  - agent_system
  - self-improvement
  - orchestration
  - governance
  - optimization
source: https://arxiv.org/abs/2604.15034
---

# Autogenesis: A Self-Evolving Agent Protocol

**Authors:** Wentao Zhang, Zhe Zhao, Haibin Wen, Yingcheng Wu, Ming Yin, Bo An, Mengdi Wang (Nanyang Technological University, Stanford, City University of Hong Kong, Princeton)

**Published:** April 2026 | **Code:** https://github.com/DVampire/Autogenesis

## Core Thesis

Existing agent protocols (MCP, A2A) solve connectivity — how agents invoke tools and communicate — but they under-specify lifecycle management, version tracking, and safe update interfaces for self-evolution. Autogenesis introduces a two-layer protocol (AGP) that **decouples what evolves from how evolution occurs**, enabling modular, traceable, and safe self-modification.

## The Protocol: Two Layers

### Layer 1 — Resource Substrate Protocol Layer (RSPL)

RSPL models five entity types as **protocol-registered resources** with explicit state, lifecycle, and versioned interfaces:

1. **Prompt** (instructions) — `εPrompt`
2. **Agent** (decision policies) — `εAgent`
3. **Tool** (actuation interfaces, including native scripts, MCP tools, agent skills) — `εTool`
4. **Environment** (task/world dynamics) — `εEnv`
5. **Memory** (persistent state) — `εMem`

Resources are **passive** — they encapsulate no optimization logic and cannot self-modify. All state transitions occur only through controlled, interface-mediated operations from higher layers.

Each resource type is managed by a **context manager** (lifecycle, version history, dependency constraints) and exposed through a **server interface** (stable external API). The context manager supports contract generation, producing capability/constraint specifications (e.g., skills.md-style descriptions for tools) that enable systematic [[Context-Engineering]].

**Infrastructure services** support reliable evolution:
- **Model manager** — unified API across providers with routing/fallback
- **Version manager** — lineage tracking, rollback, branching, diffing
- **Dynamic manager** — hot-swapping resources at runtime without restart
- **Tracer module** — fine-grained execution traces for debugging and training signals

### Layer 2 — Self-Evolution Protocol Layer (SEPL)

SEPL defines a control-theoretic formalism: a **closed-loop operator algebra** over evolvable variables. It introduces **variable lifting**, projecting heterogeneous RSPL resources onto a unified representation (`Vevo`), with a binary learnability mask defining the trainable subspace.

Five atomic operators:

| Operator | Signature | Role |
|----------|-----------|------|
| **Reflect** (ρ) | Z × Vevo → ℘(H) | Maps execution traces to causal failure hypotheses — the "semantic gradient" |
| **Select** (σ) | Vevo × ℘(H) → ℘(D) | Translates hypotheses into concrete modification proposals |
| **Improve** (ι) | Vevo × ℘(D) → Vevo' | Applies updates via RSPL interfaces to produce a candidate state |
| **Evaluate** (ε) | Vevo' × G → S | Maps candidate state + objective to evaluation space (scores + safety invariants) |
| **Commit** (κ) | Vevo' × S → Vevo | Conditional gate — accepts candidate only if performance improves and safety is preserved; otherwise rolls back |

The loop (Algorithm 1) iterates: execute → reflect → select → improve → evaluate → commit. Failed evolution attempts roll back without side effects; successful ones become immediately available to all sub-agents.

**Alternative optimizers** fit the same SEPL interface:
- **TextGrad** — natural-language feedback as "textual gradient"; σ as gradient-informed proposal generator
- **GRPO / Reinforce++** — RL perspective; treats evolvable variables as policy, evaluation signal as reward

## AGS: The Reference Implementation

AGS (Autogenesis System) instantiates the protocol as a **multi-agent system with Agent Bus architecture**:

- **Orchestrator** — generates a structured `plan.md` (registered as a versioned RSPL resource), broadcasts subtasks to specialized agents via the bus
- **Sub-agents** — deep researcher, browser-use agent, reporter, tool generator, deep analyzer — each retrieves prompts/tools from RSPL registry via semantic search, executes concurrently, writes to shared memory
- **Agent-as-tool composition** — sub-agents can also be wrapped behind standard RSPL tool schemas and invoked alongside conventional tools, MCP services, and [[Agent-Skills]]

Self-evolution is interleaved with bus coordination: whenever traces signal correctable failures, SEPL triggers, evolving prompts, tool source code, MCP tool configurations, skill definitions, or the plan structure itself.

## Key Results

### GAIA Test — 89.04% SOTA

| Tier | Vanilla | Evolve Tool | Improvement |
|------|---------|-------------|-------------|
| Level 1 | 91.40% | 98.92% | +8.2% |
| Level 2 | 77.36% | 85.53% | +10.6% |
| Level 3 | 61.22% | 81.63% | +33.3% |
| **Average** | **79.07%** | **89.04%** | **+12.6%** |

The hardest tier sees the largest gains — tool evolution provides the most leverage where task complexity demands complex multi-step tool chains.

### GPQA / AIME — Reasoning Benchmarks

- **Weak models gain more** (gpt-4.1: +71.4% on AIME24); strong models gain less but reliably (gemini-3-flash: +2.3–12%)
- **Combined prompt+solution evolution** consistently dominates single-strategy evolution
- Math benchmarks respond more strongly than science QA (more intermediate failure points for reflection to target)

### LeetCode — Algorithmic Coding

- Pass-rate improvements of 10.1% (Python) to 26.7% (Kotlin) across 5 languages
- Runtime efficiency improves 7.8–46.4% in compiled languages
- Compounding improvement: gap between evolving and vanilla agents widens as problems accumulate

## Relation to Existing Protocols

AGP **complements** rather than replaces connectivity protocols:

| Protocol | Scope | Gap |
|----------|-------|-----|
| **MCP** (Anthropic) | Model–tool invocation | No lifecycle, versioning, or state mutation |
| **A2A** (Google) | Agent–agent communication | No resource lifecycle or evolution |
| **AGP** (this paper) | Resource lifecycle + self-evolution | Fills the mutation management gap |

MCP and A2A handle **invocation**; AGP handles **state mutation and management**. The core insight: self-evolution is not about invocation but about controlled state change.

## Design Decisions Worth Noting

1. **Resources are passive** — no self-modification; evolution only through SEPL operators. This prevents runaway mutation and enables auditability.
2. **Contract generation** — context managers produce up-to-date capability descriptions, reducing prompt bloat and enabling systematic context engineering.
3. **Learnability mask** — not everything should evolve; the `g ∈ {0,1}` marker explicitly constrains the trainable subspace.
4. **Commit gate enforces monotonicity** — the system can only move to states that improve or preserve performance and safety. Failed updates roll back cleanly.
5. **Plan as versioned resource** — the orchestration plan itself is evolvable, not just the agent components. This means coordination structure can improve over time.

## Inbound Sources

- [[sources/autogenesis]]
