---
tags:
  - concept
  - multi-agent
  - orchestration
  - agentic-ai
updated: 2026-04-26
---

# Multi-Agent Orchestration

The design patterns and infrastructure for coordinating multiple AI agents — dividing work, managing dependencies, routing tasks, and synthesizing results — so the system as a whole achieves goals no single agent context window could handle.

## Core Patterns

**Thin orchestrator + specialist subagents.** The orchestrator holds only routing logic; it spawns specialists (researcher, planner, executor, verifier) and never does heavy lifting itself. This keeps the orchestrator's context at 30–40% even through large parallel workloads ([[sources/get-shit-done]]).

**Wave execution.** Plans are grouped into dependency waves — within a wave, agents run in parallel; waves are sequential. "Vertical slices" (one feature end-to-end per agent) parallelize better than "horizontal layers" (all models first, then all APIs) because they produce fewer file conflicts ([[sources/get-shit-done]]).

**Fixed workflow vocabulary.** Rather than letting users wire arbitrary DAGs, PraisonAI exposes a constrained primitive set: `route()`, `parallel()`, `loop()`, `repeat()`. Constraining the design space makes workflows predictable and introspectable ([[sources/praisonai]]).

**Staged pipelines with quality gates.** oh-my-claudecode enforces `plan → PRD → exec → verify → fix (loop)` as a fixed sequence, preventing silent partial completions. The fix loop runs until verification passes — not until the agent declares itself done ([[sources/oh-my-claudecode]]).

**Role decomposition mirroring real organizations.** TradingAgents maps specialist analyst roles (fundamentals, sentiment, technicals, macro) to separate agents, then adds an adversarial bullish/bearish researcher debate before a trader + risk team gatekeeper. The org chart is the architecture ([[sources/trading-agents]]).

**Cross-provider CLI workers.** oh-my-claudecode spawns real `codex`/`gemini`/`claude` CLI processes in tmux panes rather than using API adapters — sidesteps compatibility issues by using each tool's native interface ([[sources/oh-my-claudecode]]).

## Failure Modes Addressed

- **Context rot:** long sessions degrade quality → fresh subagent contexts per task unit ([[sources/get-shit-done]])
- **Silent partial completion:** agents declare done without verifying → verify/fix loops until passing ([[sources/oh-my-claudecode]])
- **Doom loops:** agents get stuck → auto-recovery detection ([[sources/praisonai]])
- **Cascading failures:** one agent failure propagates → circuit breakers + saga orchestration ([[sources/agent-governance-toolkit]])

## Relation to Other Concepts

- [[Context-Engineering]] — orchestration is one technique within context engineering
- [[Agent-Governance]] — governance sits above orchestration, enforcing policy across all agents
- [[Agent-Skills]] — skills are the units of capability that orchestrators compose
- [[Self-Evolving-Skills]] — skills improve from orchestration execution traces

## Inbound Sources

- [[sources/get-shit-done]]
- [[sources/oh-my-claudecode]]
- [[sources/praisonai]]
- [[sources/trading-agents]]
- [[sources/hermes-agent]]
- [[sources/gstack]]
