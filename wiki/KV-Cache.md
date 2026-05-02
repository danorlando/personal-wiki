---
title: "KV Cache (Key-Value Cache)"
created: 2026-04-26
updated: 2026-04-26
type: concept
tags:
  - concept
  - llm-internals
  - efficiency
---

# KV Cache (Key-Value Cache)

The primary memory bottleneck in large language model inference. The KV cache stores intermediate **key** and **value** vectors computed during attention — a "high-speed digital cheat sheet" that avoids recomputing attention over prior tokens on each generation step.

## Why It Matters

In autoregressive generation, the model processes all prior tokens at each step. Without caching, this is O(n²) compute. The KV cache reduces this to O(n) by storing the key/value projections from prior layers and reusing them.

**The cost:** high-dimensional vectors for every token in every layer across every head consume substantial GPU memory. As context lengths grow (128k, 1M tokens), the KV cache can dominate VRAM usage.

## Compression Approaches

### Quantization
Reduce numerical precision of stored vectors (float32 → int8 → int4 → 1-bit). Standard approach, but risks quality degradation or requires correction overhead.

### [[TurboQuant]] (Google, 2026)
Two-stage approach:
1. **PolarQuant** — polar coordinate transform (radius + angles) reduces dimensionality
2. **QJL** — 1-bit quantization with attention-score correction

Achieves 6× memory reduction and 8× attention speedup without retraining.

### Other Approaches (not in wiki yet)
- **Sliding window attention** — discard old cache entries
- **PagedAttention** (vLLM) — virtual memory management for KV cache
- **MLA** (DeepSeek) — Multi-head Latent Attention compresses KV into lower-rank latent space

## Strategic Importance

KV cache efficiency directly affects:
- Inference cost per token
- Maximum context length feasible on given hardware
- Deployment on resource-constrained devices
- Latency (memory bandwidth is often the bottleneck, not compute)

## Inbound sources
- [[sources/turboquant-kv-cache-compression]]
