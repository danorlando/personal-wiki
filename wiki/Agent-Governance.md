---
tags:
  - concept
  - security
  - governance
  - agentic-ai
  - policy-enforcement
updated: 2026-04-26
---

# Agent Governance

Runtime enforcement of policy, identity, and safety constraints on autonomous AI agents — sitting between agent frameworks and the actions agents actually take. Distinct from model-level safety (content moderation, prompt guardrails) which governs outputs; agent governance governs *actions* (tool calls, resource access, inter-agent communication).

## The Boundary That Matters

An agent can produce safe-sounding outputs and still execute dangerous operations. Model-level safety catches the former; agent governance is needed for the latter. This is the architectural argument for a separate governance layer rather than relying on system prompts and guardrails ([[sources/agent-governance-toolkit]]).

## Key Mechanisms

**Deterministic policy evaluation.** Policy decisions must not require LLM calls — Microsoft's Agent Governance Toolkit evaluates policies in <0.1ms (p50: 0.012ms, 72K ops/sec). This is ~10,000× faster than an LLM call, making governance a non-bottleneck even at scale ([[sources/agent-governance-toolkit]]).

**Zero-trust cryptographic identity.** Each agent gets Ed25519 credentials (SPIFFE/SVID) with a trust score (0–1000) that gates inter-agent communication. Eliminates shared secrets and API key reuse across agent boundaries ([[sources/agent-governance-toolkit]]).

**Privilege rings.** A 4-tier privilege ring model (analogous to OS Ring 0–3) gates execution with saga orchestration, termination control, and a kill switch — rather than binary allow/deny ([[sources/agent-governance-toolkit]]).

**Bring-your-own policy language.** OPA/Rego and Cedar are supported — reuse existing policy infrastructure rather than rebuilding it for agents. Three evaluation modes: embedded engine, remote server, or built-in fallback with zero external dependencies ([[sources/agent-governance-toolkit]]).

**MCP Security.** Novel attack surface: agents consuming external tool registries can be victims of tool poisoning, typosquatting, hidden instructions, and rug-pull attacks. Built-in MCP Security Scanner detects these in tool definitions before execution ([[sources/agent-governance-toolkit]]).

**Agent SRE.** Treating agents like production services: SLOs, error budgets, chaos engineering, replay debugging, and progressive delivery. Circuit breakers + SLO enforcement address cascading failures (OWASP ASI-08) ([[sources/agent-governance-toolkit]]).

## OWASP Agentic Top 10

The industry risk taxonomy for agentic systems (ASI-01 through ASI-10), covering:
- ASI-01 Goal Hijacking
- ASI-03 Identity & Privilege Abuse
- ASI-04 Uncontrolled Code Execution
- ASI-06 Memory Poisoning
- ASI-07 Unsafe Inter-Agent Communication
- ASI-08 Cascading Failures
- ASI-10 Rogue Agents

Regulatory alignment: EU AI Act (Aug 2026), Colorado AI Act (Jun 2026), NIST AI Agent Security RFI.

## Relation to Other Concepts

- [[Multi-Agent-Orchestration]] — governance sits above orchestration, enforcing policy across all agents
- [[Agent-Memory]] — memory poisoning (ASI-06) requires integrity checks on episodic memory
- [[Progressive-Disclosure]] — governance can gate context disclosure at privilege ring boundaries

## Inbound Sources

- [[sources/agent-governance-toolkit]]
- [[sources/personal-ai-infrastructure]] (security hooks without `--dangerously-skip-permissions`)
