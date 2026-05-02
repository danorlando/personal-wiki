---
title: "LLMOps"
created: 2026-04-26
updated: 2026-04-26
type: concept
tags:
  - concept
  - llmops
  - observability
  - optimization
  - infrastructure
---

# LLMOps

The operational discipline for running LLM-powered systems in production — gateway routing, observability, evaluation, fine-tuning, and experimentation — with the goal of continuously improving model performance on specific tasks using real production data.

## The Data Flywheel

TensorZero's central insight is that LLMOps tools only compound value if they form a closed loop: production metrics → fine-tuning → better models → better production data → back to fine-tuning. Individual tools disconnected from this loop are insufficient. The flywheel is the architecture, not a feature ([[sources/tensorzero]]).

## Key Components

**Gateway.** A high-throughput proxy that routes LLM calls, enforces rate limits, handles failover, and collects observability data. TensorZero implements this in Rust (<1ms p99 at 10k+ QPS) to make the gateway a non-bottleneck. Exposes an OpenAI-compatible API so existing clients need only change `base_url` ([[sources/tensorzero]]).

**Structured functions and variants.** Rather than treating prompts as free-form strings, TensorZero enforces typed "functions" with schemas and "variants" (specific prompt + model combinations). This creates a typed interface between application code and LLMs, enabling systematic A/B testing and optimization ([[sources/tensorzero]]).

**Evaluation.** Two types: inference evaluations (unit tests on single calls) and workflow evaluations (integration tests on multi-step flows). LLM judges are themselves TensorZero functions, optimized using the same feedback loop as the models they evaluate ([[sources/tensorzero]]).

**Optimization techniques:**
- SFT (supervised fine-tuning) on curated production traces
- RLHF on preference feedback
- GEPA (automated prompt engineering) — generates and evaluates prompt variants programmatically
- DICL (dynamic in-context learning) — retrieves relevant examples at inference time
- Best-of-N — samples multiple completions and selects the best

**Adaptive experimentation.** Multi-armed bandits shift traffic toward better-performing variants *during* the experiment, reducing the cost of running an inferior variant to completion versus fixed A/B splits ([[sources/tensorzero]]).

## Model Routing as a Cost Lever

Multiple frameworks treat model routing as a first-class concern:
- TensorZero: typed variants route different task types to different models
- oh-my-claudecode: Haiku for simple tasks, Opus for complex reasoning (30–50% token savings claimed)
- GSD: Opus for planning, Sonnet for execution, Sonnet for verification
- PraisonAI: auto-routing selects cheapest capable model per task

The pattern: match model cost to task complexity, not task importance.

## Self-Hosted vs. Managed

TensorZero is fully self-hosted with file-based GitOps config — no required cloud dependency. Design rationale: data sovereignty, compliance, and auditability are hard constraints for industrial deployments. Commercial "Autopilot" layer sits on top for organizations that want managed optimization ([[sources/tensorzero]]).

## Relation to Other Concepts

- [[Agent-Governance]] — governance overlaps at the gateway layer (policy enforcement on LLM calls)
- [[Multi-Agent-Orchestration]] — LLMOps observability applies to multi-agent workflows, not just single calls
- [[Self-Evolving-Skills]] — the data flywheel is a form of skill/behavior evolution from production feedback

## Inbound Sources

- [[sources/tensorzero]]
