---
tags:
  - source
  - ai
  - theoretical-cs
  - google-deepmind
updated: 2026-04-26
---

# AI as a Research Partner: Advancing Theoretical Computer Science with AlphaEvolve

**Source:** [Google Research Blog, 2025-09-29](https://research.google/blog/ai-as-a-research-partner-advancing-theoretical-computer-science-with-alphaevolve/)
**Authors:** Ansh Nagda, Abhradeep Thakurta (Google DeepMind), Prabhakar Raghavan (Google)
**Paper:** [Reinforced Generation of Combinatorial Structures (arXiv:2509.18057)](https://arxiv.org/abs/2509.18057)

## Summary

Google DeepMind used [[AlphaEvolve]] — a Gemini-powered coding agent — to discover novel combinatorial structures in [[Complexity Theory]], producing new theorems with machine-verifiable proofs. The key methodological insight is "lifting": AI finds a better finite structure inside a proof, and existing mathematical frameworks automatically propagate that improvement into a stronger universal theorem.

## Key Results

### MAX-4-CUT inapproximability (new state of the art)
- **Previous bound:** NP-hard to approximate within 0.9883
- **New bound:** 0.987 (inapproximability lower bound tightened)
- AlphaEvolve found a gadget with 19 variables and edge weights up to 1429× the minimum — too complex to discover by hand.

### Average-case hardness / Ramanujan graphs
- Prior work found extremal Ramanujan graphs on ≤10 nodes via computer search.
- AlphaEvolve found them on up to **163 nodes**, significantly tightening lower bounds for average-case hardness of MAX-2-CUT certification.
- Combined with non-AI algorithmic progress, upper and lower bounds now agree to the third decimal place.

## Methodology: The Lifting Framework

```
AI discovers better finite structure
        ↓
Plugged into existing proof framework
        ↓
Framework "lifts" → stronger universal theorem
        ↓
Verified by brute-force algorithm (absolute correctness)
```

The crucial constraint: results must be **computationally verifiable without human involvement**. AlphaEvolve achieved a **10,000× speedup** in verification via branch-and-bound strategies, enabling exploration of far larger gadgets. Final gadgets were re-verified by the original brute-force algorithm.

## AI Modes for Mathematical Research

1. **Literature / planning / proof generation** — LLM as writing assistant (not this work)
2. **AI-derived tools finding better proof elements** — this work's category

The second mode is more rigorous because correctness is machine-checkable, not subject to hallucination.

## Implications

- AI is becoming a collaborator in mathematical *discovery*, not just exposition.
- **Verification will be the bottleneck** as AI produces more complex structures.
- AlphaEvolve's iterative code evolution (population → evaluate → LLM morphs best → repeat) is a general pattern applicable beyond math.

## Inbound sources
- [[sources/alphaevolve-complexity-theory]] ← this page
