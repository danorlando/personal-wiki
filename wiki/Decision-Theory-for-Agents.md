---
title: "Decision Theory for Agents"
created: 2026-05-02
updated: 2026-05-02
type: concept
tags:
  - concept
  - decision-theory
  - agentic-ai
  - bayesian-inference
  - utility-theory
  - value-of-information
---

# Decision Theory for Agents

The application of normative decision theory — Bayesian decision theory, expected utility, value of information — to the problem of how agentic AI systems should select actions under uncertainty. This is the theoretical foundation underlying principled agent orchestration.

## From Prediction to Decision

LLMs are predictive models: they estimate distributions over sequences. Agentic AI systems are *decision makers*: they select and execute actions in an environment. The shift from prediction to decision changes the evaluation target from likelihood/correctness to utility/consequence. An agentic system that produces plausible outputs but makes poor decisions (wrong tool, too many calls, unsafe action) fails at the task that matters.

## Core Framework: Bayesian Decision Theory

1. **Belief state:** A posterior distribution over task-relevant latent variables, updated as evidence arrives
2. **Utility function:** Costs and benefits associated with actions and outcomes — potentially context-dependent, nonlinear, and themselves uncertain
3. **Decision rule:** Select the action that maximizes posterior expected utility, integrating over uncertainty in both the task state and the utility specification
4. **Value of information (VoI):** The expected reduction in posterior expected loss from acquiring additional evidence; additional queries are warranted only when VoI exceeds their cost

## Why Decision Theory Matters for Agents

Agent orchestration involves decisions that are:
- **Sequential:** Call agent A, observe output, decide whether to call agent B
- **Cost-aware:** Each agent call has latency, monetary cost, and risk
- **Uncertainty-laden:** Agent outputs are noisy observations about latent task variables
- **Asymmetric:** Wrong stops are more costly than extra queries (or vice versa, depending on context)
- **Composable:** Multiple agents may need to be orchestrated, with dependencies

These properties map directly onto the structure that decision theory formalizes. Prompting heuristics and fixed workflows can work for simple cases, but decision theory provides the normative framework for principled behavior as complexity grows.

## Alternative Approaches and Their Limits

- **RL/policy gradient methods** — Optimize expected return without explicit belief states; struggle with abstention, escalation, and cost-utility coupling
- **Robust control** — Worst-case guarantees; conservative and doesn't naturally support information gathering
- **Bandit formulations** — Confidence bounds and exploration bonuses; partial overlap with Bayesian control but lack explicit utility coupling
- **Heuristic orchestration** — Chain-of-thought, fixed workflows; sufficient for short-horizon, low-stakes settings; no principled basis for stopping/routing under uncertainty

## Practical Implications

- **Stopping rules** become value-of-information calculations rather than fixed thresholds
- **Routing** becomes posterior-predictive success probability comparison rather than heuristic matching
- **Budget allocation** becomes expected utility maximization under resource constraints
- **Abstention/escalation** becomes the optimal action when no agent's expected utility exceeds a safety threshold

## Relation to Other Concepts

- [[Bayesian-Agent-Control]] — The specific architectural pattern of applying Bayesian decision theory at the agent control layer
- [[Agent-Governance]] — Governance constrains the action space; decision theory selects within it
- [[Multi-Agent-Orchestration]] — Decision theory provides the normative basis for orchestration decisions (routing, stopping, composition)
- [[Adaptive-RAG]] — Adaptive retrieval timing and routing are instances of the broader decision-theoretic framework

## Inbound Sources

- [[sources/bayes-consistent-decisions]]
