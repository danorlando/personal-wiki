---
tags:
  - concept
  - theoretical-cs
  - mathematics
updated: 2026-04-26
---

# Complexity Theory

The subfield of theoretical computer science concerned with classifying problems by the computational resources required to solve them — particularly time and space — and understanding the limits of efficient computation.

## Key Concepts (as they appear in the wiki)

### NP-Hardness
A problem is NP-hard if every problem in NP can be reduced to it in polynomial time. NP-hard problems are not expected to have efficient exact algorithms.

### Approximation Algorithms
For NP-hard optimization problems, approximation algorithms find solutions guaranteed to be within a factor of the optimum efficiently. The key question: what is the **approximation limit** (inapproximability bound)?

### Inapproximability
Proving that it is NP-hard to approximate a problem within a certain factor. Tight inapproximability results tell us the *best possible* approximation algorithms can achieve.

### Gadget Reductions
A technique for proving hardness: map a known hard problem to a target problem using a small local "gadget" — a template that converts each piece of the source into a piece of the target. Optimal gadgets are typically found by hand; [[AlphaEvolve]] can now find more complex gadgets automatically.

## Problems in the Wiki

### MAX-k-CUT
Given a graph, partition nodes into k sets to maximize edges crossing between sets. NP-hard for k ≥ 2.
- **MAX-4-CUT inapproximability:** [[AlphaEvolve]] improved the bound from 0.9883 to **0.987**.

### Ramanujan Graphs
Deterministic graphs that spectrally resemble sparse random graphs. Their existence implies hardness of certifying properties of random graphs.
- AlphaEvolve found Ramanujan graphs on up to **163 nodes** (prior: 10 nodes), tightening average-case hardness bounds.

## The Lifting Technique

A proof strategy used with [[AlphaEvolve]]: AI finds a better **finite structure** (gadget, graph) that plugs into an existing proof framework. The framework "lifts" the improvement into a stronger universal theorem. The finite structure is machine-verifiable; the framework handles the universality.

## Inbound sources
- [[sources/alphaevolve-complexity-theory]]
