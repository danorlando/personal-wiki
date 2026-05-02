---
title: "AlphaEvolve"
created: 2026-04-26
updated: 2026-04-26
type: entity
tags:
  - entity
  - google-deepmind
  - ai-tool
  - coding-agent
---

# AlphaEvolve

A Gemini-powered coding agent developed at Google DeepMind. AlphaEvolve uses an **evolutionary loop** to iteratively improve code: it starts with a population of code snippets, evaluates the structures they produce, and uses an LLM to morph the most successful snippets toward better solutions.

## Core Loop

```
Population of code snippets
    → Evaluate structures produced
    → LLM morphs best snippets
    → Repeat
```

## Notable Applications

- **Mathematical discovery:** Found gadget reductions for [[Complexity Theory]] problems that are beyond human hand-derivation in complexity. See [[sources/alphaevolve-complexity-theory]].
  - MAX-4-CUT gadget: 19 variables, edge weights up to 1429×
  - Ramanujan graphs on up to 163 nodes (prior state of art: 10 nodes)
  - Achieved **10,000× speedup** in verification via branch-and-bound strategies
- **Algorithm design** (referenced in original AlphaEvolve blog post, not detailed here)

## Key Design Choice: Verified Correctness

AlphaEvolve doesn't generate proofs — it finds **finite structures** that plug into existing mathematical frameworks. This keeps the correctness burden tractable: only the discovered structure needs verification, and that verification can be done computationally without human involvement.

## Relation to Other Work

- Follows [[FunSearch]] in applying LLM-driven search to mathematical discovery
- Complements proof assistants (Lean, Coq) by generating the structures those systems could verify

## Inbound sources
- [[sources/alphaevolve-complexity-theory]]
