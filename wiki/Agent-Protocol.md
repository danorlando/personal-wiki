---
title: "Agent Protocol"
created: 2026-05-02
updated: 2026-05-02
type: concept
tags:
  - concept
  - agent_system
  - orchestration
  - governance
---

# Agent Protocol

Standardized interfaces that govern how agents interact — with tools, with each other, and with their own internal resources. Protocols enable interoperability, but each addresses a different layer of the agent stack.

## The Three Protocol Layers

| Protocol | Layer | Scope | Key Abstraction |
|----------|-------|-------|-----------------|
| **MCP** (Anthropic) | Connectivity | Model–tool invocation | Tool schema + context server |
| **A2A** (Google) | Connectivity | Agent–agent communication | Agent card + message passing |
| **AGP** (Autogenesis) | Evolution | Resource lifecycle + self-modification | Versioned resources + operator algebra |

MCP and A2A handle **invocation** — how to call a tool, how to send a message. AGP handles **mutation** — how to safely change the resources that agents depend on. The gap between connectivity and evolution is where most current systems break down: without lifecycle management, version tracking, and safe update interfaces, self-modifying agents risk irrecoverable errors and opaque state changes.

## Why Protocol-Level Matters

Ad hoc self-evolution leads to monolithic architectures, brittle glue code, and untraceable modifications. A protocol standardizes:

1. **Resource representation** — what exists and how it's described (RSPL's five entity types)
2. **Mutation interface** — how changes are proposed, evaluated, and committed (SEPL's operator algebra)
3. **Safety guarantees** — rollback, lineage, monotonic improvement

The same optimization algorithm (TextGrad, GRPO, Reinforce++, reflection) can then operate on any protocol-registered resource through a uniform interface — the protocol makes evolution composable.

## The Complementarity Insight

These protocols are **complementary**, not competing:

- **MCP** connects agents to tools — "what can I call?"
- **A2A** connects agents to agents — "who can I talk to?"
- **AGP** connects agents to their own evolution — "how do I safely improve?"

An agent system could use all three: MCP for tool invocation, A2A for multi-agent coordination, and AGP for self-evolution. Each protocol owns a distinct concern.

## Relation to Other Concepts

- [[Self-Evolving-Agents]] — the primary use case for evolution protocols; AGP is the protocol-level foundation
- [[Multi-Agent-Orchestration]] — protocols enable orchestration at scale; A2A standardizes agent communication, AGP makes orchestrated resources evolvable
- [[Agent-Governance]] — governance constrains what protocols allow; the AGP commit gate is a protocol-level governance mechanism
- [[Agent-Skills]] — skills are one resource type managed by AGP; MCP tools are another; both become first-class, versioned, evolvable entities under the protocol
- [[Context-Engineering]] — protocol-level resource contracts (e.g., skills.md descriptions) enable systematic context engineering via controlled prompt injection

## Inbound Sources

- [[sources/autogenesis]]
