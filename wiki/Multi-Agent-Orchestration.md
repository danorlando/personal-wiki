---
title: "Multi-Agent Orchestration"
created: 2026-04-26
updated: 2026-05-02
type: concept
tags:
  - concept
  - multi-agent
  - orchestration
  - agentic-ai
  - agent-security
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

## Principled Orchestration via Bayesian Control

Current orchestration patterns (thin orchestrator, wave execution, staged pipelines) are effective but heuristic — they lack a normative basis for *when* to stop, *which* agent to route to, and *how much* budget to allocate. Bayesian control ([[Bayesian-Agent-Control]]) provides this foundation: the orchestrator maintains posterior beliefs over task-relevant latent variables and selects actions by maximizing posterior expected utility. This yields value-of-information stopping rules (stop when another agent call's expected benefit falls below cost), posterior-predictive routing (route to the agent with highest expected success probability given the current belief state), and utility-aware budget allocation. The LLMs remain non-Bayesian predictors; the Bayesian structure lives entirely in the orchestrator ([[Decision-Theory-for-Agents]], [[sources/bayes-consistent-decisions]]).

Three concrete patterns where Bayesian control upgrades heuristic orchestration:
- **Stopping:** Replace fixed iteration limits with VoI-based stopping — continue querying agents only while the expected reduction in posterior expected loss exceeds the call cost
- **Routing:** Replace heuristic agent selection with Thompson sampling over agent competence profiles — routing improves across tasks as outcomes accumulate
- **Budget allocation:** Replace fixed compute budgets with utility-maximizing allocation under uncertainty — spend more when the posterior is diffuse and stakes are high

## Relation to Other Concepts

- [[Context-Engineering]] — orchestration is one technique within context engineering
- [[Agent-Governance]] — governance sits above orchestration, enforcing policy across all agents
- [[Agent-Skills]] — skills are the units of capability that orchestrators compose
- [[Self-Evolving-Skills]] — skills improve from orchestration execution traces
- [[Bayesian-Agent-Control]] — Bayesian control provides a principled (normative) approach to orchestration decisions under uncertainty
- [[Decision-Theory-for-Agents]] — the decision-theoretic framework underlying principled orchestration
- [[Agent-Traps]] — Systemic Traps specifically target orchestrated multi-agent systems (sub-agent spawning, compositional fragments, congestion, cascades)
- [[Agent-Security]] — orchestration creates new attack surfaces that security must address

## Systemic Traps in Orchestrated Systems

The DeepMind Agent Traps framework identifies **Systemic Traps** as a distinct attack class targeting multi-agent dynamics. These are particularly relevant to orchestrated systems:

- **Sub-agent Spawning Traps** exploit the orchestrator's ability to instantiate sub-agents — adversarial content can hijack control flow to route execution through attacker-controlled agents (58–90% attack success rate depending on orchestrator)
- **Compositional Fragment Traps** partition malicious payloads across multiple data sources that reconstitute when collaborative architectures aggregate inputs — each fragment is individually benign and passes safety filters
- **Congestion Traps** broadcast signals that synchronise homogeneous agents into exhaustive demand for limited resources
- **Interdependence Cascades** perturb fragile equilibria to trigger self-amplifying failure loops (flash crash dynamics) — the system's own interdependent logic propagates the attack
- **Sybil Attacks** fabricate pseudonymous agent identities to disproportionately influence collective decision-making

- [[Self-Evolving-Skills]] — skills improve from orchestration execution traces
- [[Self-Evolving-Agents]] — Autogenesis generalizes self-evolution beyond skills to the full agent stack
- [[Agent-Protocol]] — protocol-level standardization (AGP) makes orchestration resources versioned and evolvable

## Inbound Sources

- [[sources/get-shit-done]]
- [[sources/oh-my-claudecode]]
- [[sources/praisonai]]
- [[sources/trading-agents]]
- [[sources/hermes-agent]]
- [[sources/gstack]]
- [[sources/autogenesis]]
- [[sources/bayes-consistent-decisions]]
- [[sources/ai-agent-traps]]
