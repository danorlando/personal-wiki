---
title: "Bayesian Agent Control"
created: 2026-05-02
updated: 2026-05-02
type: concept
tags:
  - concept
  - bayesian-inference
  - agentic-ai
  - orchestration
  - uncertainty-quantification
  - decision-theory
---

# Bayesian Agent Control

Placing Bayesian reasoning at the **control layer** of agentic AI systems — the orchestrator that selects, composes, and terminates LLM/tool calls — rather than inside the LLMs themselves. The LLMs remain black-box predictors; the Bayesian structure lives in the system that decides *when*, *which*, and *how many* agents to invoke.

## The Key Insight

Token-level uncertainty and task-level uncertainty are different things. An LLM can be confident in its token distribution while the system is deeply uncertain about the task-level variable that drives action selection (and vice versa). This "syntactic vs. semantic uncertainty" gap means you can't reliably use LLM output probabilities as belief states for control. Instead, maintain an explicit belief state over **decision-relevant latent variables** — task outcomes, hypothesis truth, agent competence — and update it from calibrated observation models.

## What the Controller Does

1. **Maintains belief states** over task-relevant latent variables (not LLM parameters)
2. **Updates beliefs** from agent outputs and human feedback via observation models
3. **Selects actions** by maximizing posterior expected utility or comparing value of information (VoI) against cost

## Properties of a Well-Designed Bayesian Controller

- **Utility-aware:** Costs and utilities are latent variables with priors, updated from feedback
- **Low overhead:** Negligible latency and memory relative to model inference
- **Bounded memory:** Belief state as approximately sufficient statistic of interaction history (Bayesian distillation), not growing context
- **Multi-agent & human-in-the-loop:** Feedback and inter-agent communication become probabilistic observations
- **Modality-agnostic:** Any agent that provides probabilistic beliefs about task-level events fits the framework

## Three Design Patterns

1. **Within-task stopping** — Infer a latent task outcome (e.g., code passes tests) from sequential agent calls; stop when posterior exceeds threshold or VoI falls below cost
2. **Hypothesis deliberation** — Maintain posterior over hypotheses; treat each agent's contribution as evidence; decide whether to solicit more opinions
3. **Cross-task routing** — Maintain posterior over agent competence profiles; Thompson sampling or Bayesian bandit policies improve routing over time

## Why Not Bayesian LLMs?

Parameter posteriors in overparameterized models are often uninformative (cold posterior effect, permutation symmetry, functional diversity collapse). Pre-trained LLMs violate exchangeability and martingale constraints. Approximate inference in BNNs breaks sequential updating. These problems don't go away — but they're sidestepped by locating Bayesian structure at the control layer, where latent variables are low-dimensional and decision-relevant.

## Relation to Other Concepts

- [[Decision-Theory-for-Agents]] — Bayesian control is the application of Bayesian decision theory to agentic orchestration
- [[Agent-Governance]] — Governance enforces *what actions are permitted*; Bayesian control decides *which permitted action is optimal under uncertainty*
- [[Multi-Agent-Orchestration]] — Bayesian control provides a principled alternative to heuristic orchestration, especially for routing, stopping, and budget allocation
- [[Deterministic-Projection-Memory]] — DPM's belief-state-as-sufficient-statistic aligns with the Bayesian distillation property; both compress interaction history into a compact decision-relevant state

## Inbound Sources

- [[sources/bayes-consistent-decisions]]
