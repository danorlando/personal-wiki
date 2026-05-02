---
title: "Agent Traps"
created: 2026-04-26
updated: 2026-04-26
type: concept
tags:
  - concept
  - agent-security
  - adversarial-ml
  - safety
  - governance
sources:
  - raw/research_papers/AI_Agent_Traps.pdf
---

# Agent Traps

Adversarial content embedded within a web page or digital resource, engineered specifically to misdirect or exploit an interacting AI agent. The defining insight from the Franklin et al. (DeepMind) framework: **traps alter the environment, not the model** — they weaponise the agent's own capabilities (instruction-following, tool-chaining, goal-prioritisation) against it. Not model-specific.

## How Traps Differ from Traditional Attacks

Traditional adversarial ML perturbs model inputs. Prompt injection attacks the model directly. Agent traps are distinct: they embed malicious context in the *environment* that the agent navigates — websites, documents, APIs, emails — and the agent processes this content during normal operation. The trap doesn't need to modify the model; it weaponises the agent's autonomy and access.

## Six-Class Taxonomy

Traps are categorised by which component of the agent's operational cycle they target:

1. **Content Injection** (Perception) — exploiting machine-vs-human parsing divergence via CSS obfuscation, dynamic cloaking, steganography, syntactic masking
2. **Semantic Manipulation** (Reasoning) — corrupting reasoning through biased framing, oversight evasion, persona hyperstition
3. **Cognitive State** (Memory/Learning) — corrupting persistent knowledge via RAG poisoning, latent memory poisoning, contextual learning traps
4. **Behavioural Control** (Action) — hijacking instruction-following for embedded jailbreaks, data exfiltration, sub-agent spawning
5. **Systemic** (Multi-Agent Dynamics) — weaponising aggregate behaviour via congestion, cascades, tacit collusion, compositional fragments, Sybil attacks
6. **Human-in-the-Loop** (Cognitive Biases) — attacking the human overseer via automation bias, approval fatigue, social engineering

## Why Agent Traps Are Hard to Defend Against

- **Subtle**: indistinguishable from benign persuasive language; downstream effects manifest long after initial interaction
- **Persistent**: memory and knowledge attacks endure across sessions and users
- **Composable**: multiple trap types can be chained (e.g., jailbreak → exfiltration → sub-agent spawning)
- **Systemic**: homogeneity of model ecosystem amplifies correlated failures
- **Attribution gap**: tracing compromised output back to specific trap is forensically difficult

## Relation to Other Concepts

- [[Agent-Security]] — traps are the primary threat class that agent security must address
- [[Agent-Governance]] — governance layers provide runtime enforcement to detect and block trap-induced behaviours (e.g., OWASP ASI-01 Goal Hijacking maps to Content Injection and Behavioural Control)
- [[Multi-Agent-Orchestration]] — Systemic Traps specifically target orchestrated multi-agent systems via congestion, cascades, and sub-agent spawning
- [[Agent-Memory]] — Cognitive State Traps directly target the memory architectures described in Agent-Memory

## Inbound Sources

- [[sources/ai-agent-traps]]
