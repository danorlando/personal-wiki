---
title: "TurboQuant"
created: 2026-04-26
updated: 2026-04-26
type: entity
tags:
  - entity
  - google
  - llm-efficiency
  - algorithm
---

# TurboQuant

A [[KV Cache]] compression algorithm from Google (2026) that reduces LLM inference memory by 6× and speeds up attention by up to 8× — without requiring model retraining.

## Algorithm

TurboQuant is a two-stage pipeline applied to KV cache vectors:

### Stage 1: PolarQuant
Converts vectors from Cartesian → polar coordinates (radius + angles).
- Compresses multi-directional information into a compact form
- Reduces repeated normalization overhead

### Stage 2: Quantized Johnson-Lindenstrauss (QJL)
A classical dimensionality-reduction technique adapted for 1-bit quantization.
- Reduces each element to a single sign bit (positive/negative)
- Corrects residual errors left by PolarQuant
- Preserves key relationships in attention score computation

## Results (reported)

| Metric | Result |
|---|---|
| Memory reduction | 6× |
| Attention speedup | Up to 8× (vs. fp32) |
| Min precision without retraining | 3-bit |

## Design Principle

Separating compression into two stages — coarse polar compression + fine-grained 1-bit correction — is analogous to how audio codecs use transform coding + residual coding. The coarse stage does most of the work cheaply; the fine-grained stage corrects the errors it introduces.

## Limitations

- Results are benchmark-specific (long-context benchmarks, open models)
- Real-world variability in workloads may produce different outcomes
- Jevons paradox risk: freed memory may enable larger models rather than cost reduction

## Inbound sources
- [[sources/turboquant-kv-cache-compression]]
