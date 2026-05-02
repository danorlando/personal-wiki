---
title: "Diversity Collapse in Multi-Agent LLM Systems"
created: 2026-04-26
updated: 2026-04-26
type: summary
tags:
  - multi-agent
  - diversity
  - llm
  - ideation
source: https://arxiv.org/abs/2604.18005
---

# Diversity Collapse in Multi-Agent LLM Systems

**Authors:** Nuo Chen, Xueyi Zhang, Yicheng Tong, Qingyun Zou, Yufei He, Yuzhe Yang, Qian Wang, Bingsheng He (NUS, CUHK-Shenzhen)

**Core question:** When and why does multi-agent collaboration actually expand the solution space rather than reaching premature consensus?

## Key Findings

The paper evaluates over 10,000 research proposals across 20 topics, dissecting diversity at three hierarchical levels:

### 1. Model Level: Compute Efficiency Paradox
Stronger, highly aligned models yield **diminishing marginal diversity** despite higher per-sample quality. Scaling compute ≠ scaling information gain. More resources produce redundant outputs converging on shared priors.

### 2. Cognition Level: Authority-Driven Suppression
Authority-driven dynamics (senior/expert agents dominating) **suppress semantic diversity** compared to junior-dominated groups. The False Consensus Trap: agents become overconfident in biased priors, reinforcing shared assumptions.

### 3. System Level: Topology and Scaling
- Group-size scaling yields **diminishing returns** on diversity
- Dense communication topologies **accelerate premature convergence**
- Sparser topologies preserve independence longer

## Structural Coupling

The paper characterizes diversity collapse as emerging from **structural coupling** — a process where interaction inadvertently contracts agent exploration. The collapse arises primarily from the **interaction structure** rather than inherent model insufficiency.

This is a critical distinction: the problem isn't that models lack diverse ideas internally, but that multi-agent interaction structures cause agents to reinforce each other's biases and converge prematurely.

## Design Principles

The paper proposes counter-strategies:
- **Explorer role:** Inject high-variance, novel ideas to push toward the innovation frontier
- **Leader role:** Ensure quality and feasibility to prevent logical collapse
- **Judge role:** Use rigorous evaluation to sustain constructive conflict
- Preserve **independence and disagreement** when designing MAS for creative tasks

## Implications

For [[Multi-Agent-Orchestration]], this means:
- More agents ≠ more diversity (often the opposite)
- Communication topology is a first-order design choice
- Role heterogeneity matters more than agent count
- Diversity-preserving mechanisms must be intentional, not emergent

## Inbound Sources

- [[sources/diversity-collapse-mas|Diversity Collapse in Multi-Agent LLM Systems]] (Chen et al., 2026)

## Outbound Links

- [[Multi-Agent-Orchestration]] — topology and role design
- [[Agent-Governance]] — governance of multi-agent interaction structures
