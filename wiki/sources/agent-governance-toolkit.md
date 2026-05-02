---
title: "Agent Governance Toolkit (Microsoft)"
created: 2026-04-26
updated: 2026-04-26
type: summary
tags:
  - agent-security
  - governance
  - agentic-ai
  - owasp
  - zero-trust
  - policy-enforcement
  - microsoft
  - open-source
source: https://github.com/microsoft/agent-governance-toolkit
---

# Agent Governance Toolkit (Microsoft)

Microsoft's open-source runtime governance layer for autonomous AI agents — deterministic policy enforcement, zero-trust identity, execution sandboxing, and SRE tooling that sits between an agent framework and the actions agents actually take. Claims full coverage of all 10 OWASP Agentic Top 10 risks, verified by 9,500+ tests.

## Key Design Decisions

**Application-layer governance, not model-layer safety.** The toolkit explicitly distinguishes itself from prompt guardrails or content moderation. It governs *agent actions* (tool calls, resource access, inter-agent communication) at the application layer. Model-level safety (e.g., Azure AI Content Safety) is treated as a complementary, separate concern. This is the correct boundary: an agent can produce safe-sounding outputs and still execute dangerous operations.

**Sub-millisecond policy evaluation as a non-negotiable constraint.** The policy engine is implemented to evaluate actions in <0.1ms (p50: 0.012ms for a single rule, 72K ops/sec). This is ~10,000x faster than an LLM API call. The design explicitly treats latency overhead as a first-class constraint — governance must not be the bottleneck. This rules out approaches that require LLM calls for policy decisions.

**Four-tier privilege rings for execution.** Rather than binary allow/deny, the Agent Runtime implements a 4-tier privilege ring model with saga orchestration, termination control, and a kill switch. This mirrors OS-level privilege separation (Ring 0–3) in software, without requiring actual kernel-level enforcement. The tradeoff is explicitly acknowledged: enforcement is at the Python middleware layer, not OS level — agents and the policy engine share the same process.

**Zero-trust identity via Ed25519 + SPIFFE/SVID.** Each agent gets cryptographic credentials rather than relying on shared secrets or API keys. Trust is scored on a 0–1000 scale and gates inter-agent communication. This addresses OWASP ASI-03 (Identity & Privilege Abuse) and ASI-07 (Unsafe Inter-Agent Communication) architecturally rather than through policy alone.

**Bring-your-own policy language.** Rather than inventing a new policy DSL, the toolkit supports OPA/Rego and Cedar — both established policy languages with existing infrastructure and tooling. Three evaluation modes per backend: embedded engine, remote server, or built-in fallback with zero external dependencies. Organizations can reuse their existing policy infrastructure rather than rebuilding it for agents.

**Framework-agnostic by design.** Works with 20+ agent frameworks (LangChain, CrewAI, AutoGen, OpenAI Agents, Google ADK, Semantic Kernel, etc.) via thin adapters. Pure `pip install` with zero vendor lock-in. The architecture treats governance as a cross-cutting concern that should not require rewriting agent logic.

**MCP Security Scanner.** Built-in tooling to detect tool poisoning, typosquatting, hidden instructions, and rug-pull attacks in MCP tool definitions — a novel attack surface that emerges when agents consume external tool registries.

## OWASP Agentic Top 10 Coverage

All 10 ASI risks addressed (ASI-01 through ASI-10), including:
- ASI-01 Goal Hijacking → policy engine blocks unauthorized goal changes
- ASI-04 Uncontrolled Code Execution → 4-tier privilege rings + sandboxing
- ASI-06 Memory Poisoning → episodic memory with integrity checks
- ASI-08 Cascading Failures → circuit breakers + SLO enforcement
- ASI-10 Rogue Agents → kill switch + ring isolation + behavioral anomaly detection

## Regulatory Alignment

Maps to EU AI Act (August 2026 deadline), Colorado AI Act (June 2026), and NIST AI Agent Security RFI. Positions AGT as runtime governance evidence for regulatory audits.

## Notable Patterns

- **Agent SRE:** SLOs, error budgets, replay debugging, chaos engineering, and progressive delivery — treating agents like production services
- **Bootstrap integrity:** SHA-256 tamper detection of governance modules at startup
- **GitHub Actions integration:** governance attestation and security scanning baked into CI/CD pipelines
- Multi-language SDKs: Python, TypeScript, .NET, Rust, Go

## Concepts Touched

- [[Agent-Governance]]
- [[Agentic-AI]]
- [[Agent-Security]]
- [[OWASP-Agentic-Top-10]]
- [[Zero-Trust-Identity]]
- [[Policy-Enforcement]]
- [[Agent-SRE]]
- [[MCP-Security]]
- [[LLM-Infrastructure]]

## Inbound Sources

- `/raw/Repos/agent-governance-toolkit.md`
