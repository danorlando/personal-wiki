---
title: "Stateless Decision Memory for Enterprise AI Agents"
created: 2026-04-26
updated: 2026-04-26
type: summary
tags:
  - research_paper
  - agent_system
  - memory
  - architecture
  - governance
sources:
  - raw/research_papers/Stateless Decision Memory for Enterprise AI Agents.md
source: https://arxiv.org/html/2604.20158v1
---

# Stateless Decision Memory for Enterprise AI Agents

**Author:** Vasundra Srinivasan (2026)

## Core Argument

Enterprise deployment of regulated decision agents (underwriting, claims adjudication, clinical review) overwhelmingly uses RAG pipelines despite a decade of more sophisticated stateful memory architectures. This gap exists because regulated deployment requires four **systems properties** that the research evaluation has underweighted — and stateful memory violates them by construction.

## The Four Enterprise Properties

1. **Deterministic replay** — a denied applicant must be re-scored and produce the same decision; the memory view M(E,T,B) must be reproducible from the same inputs
2. **Auditable rationale** — reasoning chains must map back to specific events; regulators and courts must be able to inspect the provenance
3. **Multi-tenant isolation** — tenant i's decision depends only on tenant i's events; shared mutable state creates leakage surfaces
4. **Statelessness for horizontal scale** — thousands of concurrent decisions with no per-request affinity; no bottleneck on shared mutable memory

RAG satisfies these as a side-effect of architectural simplicity. Stateful memory (MemGPT, H-MEM, GAM, A-Mem, etc.) violates at least one by construction because path-dependent state is the load-bearing difficulty.

## Deterministic Projection Memory (DPM)

DPM is the paper's proposed architecture — see [[Deterministic-Projection-Memory]] for the full concept page.

**Two components:**
1. **Append-only event log** — immutable, arrival-order, never edited or summarized. The single durable representation of the trajectory.
2. **Task-conditioned projection** π(E,T,B)→M — one LLM call at decision time at temperature zero, producing a structured memory view (facts / reasoning / compliance notes) within budget.

The consolidation operator U is the identity. Memory doesn't exist as a runtime object until π is applied. This is a direct application of [[Event-Sourcing]] to agent memory.

## Key Results

**Decision quality** (10 regulated cases, 3 budgets, 4 alignment axes — FRP/RCS/EDA/CRR):

| Budget | DPM vs Summ-only |
|--------|-----------------|
| Loose (2× compression) | No significant difference on any axis |
| Moderate (5×) | No significant difference on any axis |
| Tight (20×) | DPM strictly better: FRP +0.52 (h=1.17, p=0.001), RCS +0.53 (h=1.13, p=0.003) |

**The mechanism:** Incremental summarization is lossy per step, and loss compounds across 82–96 events. At generous budgets the loss rounds to zero; at tight budgets, discarded anchors accumulate. DPM never consolidates, so no compounding.

**Cost and latency:** DPM is 7–15× faster than Summ-only because it makes 1 LLM call instead of N (82–96). At tight budget: 59.8s vs 440.3s wall time; $0.014 vs $0.165 per run.

**Determinism study** (10 replays per case at temperature zero): Both architectures inherit residual API-level nondeterminism from the Anthropic API, but the asymmetry is structural — DPM exposes one nondeterministic call, Summ-only exposes N compounding calls. Byte-exact replay requires pairing DPM with a deterministic inference backend.

## TAMS Heuristic

**Task-Adaptive Memory Selection** — a practitioner decision rule:

1. If deployment requires deterministic replay, audit-ready rationale, or multi-tenant isolation → **use DPM**
2. Else if compression ratio (trajectory/budget) exceeds ~10× → **use DPM**
3. Else → either architecture is acceptable; choose by operational preference

## Failure Analysis of Stateful Memory

Five concrete failure modes under enterprise operating conditions:
- **State drift under concurrency** — parallel tool calls make merge semantics non-associative/non-commutative
- **Replay complexity compounding with trajectory length** — probability of byte-identical replay falls exponentially with n
- **Cross-tenant leakage in shared caches** — imperfect cache keying creates leakage surfaces
- **Audit surface area** — DPM: 2 LLM calls to audit; Summ-only: 83–97 calls (scales linearly with trajectory)
- **Retrofitting cost** — each fix is real engineering cost and latent bug source; compounds with architectural sophistication

## Limitations

- Temperature-zero is not byte-deterministic against the live Anthropic API
- Single-call projection has a context-window ceiling (~10⁶ tokens); hierarchical projection is future work
- TAMS derived from 2 domains, 1 model family, 10 cases per cell — re-derive for materially different regimes
- Comparison is DPM vs Summ-only only; retrieval and schema-anchored architectures dominated in companion paper

## Connections

- [[Deterministic-Projection-Memory]] — the core architecture introduced by this paper
- [[Agent-Memory]] — where DPM sits among memory architectures for agents
- [[Agent-Governance]] — enterprise properties overlap heavily with governance requirements
- [[Event-Sourcing]] — the distributed systems pattern DPM applies to agent memory
