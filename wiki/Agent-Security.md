---
title: "Agent Security"
created: 2026-04-26
updated: 2026-04-26
type: concept
tags:
  - concept
  - agent-security
  - safety
  - adversarial-ml
  - governance
sources:
  - raw/research_papers/AI_Agent_Traps.pdf
  - raw/Repos/agent-governance-toolkit.md
---

# Agent Security

The discipline of protecting autonomous AI agents from adversarial manipulation, unauthorised access, and exploitation — encompassing the full attack surface from model-level vulnerabilities through environment-level traps to systemic multi-agent failures.

## The Environment-Level Threat

Agent security extends beyond traditional model safety (content moderation, prompt guardrails, jailbreak prevention). The DeepMind Agent Traps framework demonstrates that the **information environment itself** is an attack surface: adversarial content embedded in web pages, documents, and APIs can weaponise an agent's own capabilities against it. This is fundamentally different from adversarial ML attacks that perturb model inputs — the agent's autonomy and tool access are the vulnerability ([[Agent-Traps]]).

## Layered Defence Model

**Model-level safety** — content moderation, prompt guardrails, Constitutional AI, adversarial training. Necessary but insufficient: an agent can produce safe-sounding outputs and still execute dangerous operations.

**Application-level governance** — deterministic policy enforcement (<0.1ms), zero-trust cryptographic identity, privilege rings, circuit breakers. Sits between the agent framework and actual actions ([[Agent-Governance]]).

**Ecosystem-level interventions** — web standards for AI-consumable content, domain reputation systems, mandatory provenance citations for synthesised information, NIST AI RMF alignment.

**Legal & ethical frameworks** — distinguishing passive adversarial examples from active traps, addressing the "Accountability Gap" (liability between agent operator, model provider, domain owner).

## Key Attack Surfaces

| Surface | OWASP Mapping | Agent Trap Class |
|---------|--------------|-----------------|
| Goal hijacking | ASI-01 | Content Injection, Behavioural Control |
| Memory poisoning | ASI-06 | Cognitive State |
| Unsafe inter-agent communication | ASI-07 | Systemic (Sub-agent Spawning, Sybil) |
| Cascading failures | ASI-08 | Systemic (Interdependence Cascades) |
| Rogue agents | ASI-10 | Behavioural Control (Sub-agent Spawning) |
| Human manipulation | — | Human-in-the-Loop |

## Critical Gaps

- **Benchmarking deficit**: most Agent Trap categories lack standardised benchmarks (WASP, AgentDojo, InjecAgent are early but incomplete)
- **Attribution**: tracing a compromised agent's output back to the specific trap is forensically difficult
- **Arms race**: attackers continuously adapt to evade new defences
- **Homogeneity risk**: correlated model architectures create systemic fragility

## Relation to Other Concepts

- [[Agent-Traps]] — the primary threat class that defines the agent security problem at the environment level
- [[Agent-Governance]] — runtime enforcement layer that blocks trap-induced behaviours at the action boundary
- [[Multi-Agent-Orchestration]] — orchestration patterns create new attack surfaces (sub-agent spawning, compositional fragments) that security must address
- [[Agent-Memory]] — memory architectures are a primary target of Cognitive State Traps; integrity checks are essential

## Inbound Sources

- [[sources/ai-agent-traps]]
- [[sources/agent-governance-toolkit]]
