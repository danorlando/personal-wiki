---
tags:
  - llmops
  - observability
  - llm-gateway
  - fine-tuning
  - experimentation
  - optimization
  - open-source
  - rust
updated: 2026-04-26
source: https://github.com/tensorzero/tensorzero
---

# TensorZero

An open-source LLMOps platform that unifies gateway, observability, evaluation, optimization, and experimentation into a single system, with a data flywheel at its core. In production at companies ranging from AI startups to Fortune 10, fueling ~1% of global LLM API spend.

## Key Design Decisions

**The data flywheel as the organizing principle.** TensorZero's central insight is that LLMOps tools are only useful if they compound: production metrics feed fine-tuning, fine-tuned models generate better data, better data improves future variants. The entire platform is structured around closing this loop — gateway → observability → evaluation → optimization → better models → back to gateway. Individual tools that don't connect to the loop are treated as insufficient.

**Rust gateway for <1ms p99 latency overhead.** The gateway is implemented in Rust specifically to make governance overhead negligible at scale — <1ms p99 at 10k+ QPS. This is a deliberate language choice driven by the constraint that the gateway must not become a bottleneck even for latency-sensitive workloads. Everything else (optimization, evaluation) is Python-adjacent, but the hot path is Rust.

**OpenAI SDK compatibility as the adoption strategy.** Rather than requiring SDK migration, TensorZero exposes an OpenAI-compatible API. Migration is: update `base_url` and `model` in your existing client. This removes the biggest friction point in LLMOps adoption — teams don't have to rewrite their inference code to get observability and optimization.

**Functions and variants as first-class concepts.** Instead of treating prompts as free-form strings, TensorZero enforces structured "functions" with typed schemas and "variants" (specific prompt + model combinations). This creates a typed interface between application code and LLMs, enabling systematic A/B testing, evaluation, and optimization across variants. Prompt engineering becomes an engineering discipline with measurable outcomes.

**Optimization as a feedback loop, not a one-time step.** TensorZero supports multiple optimization techniques (SFT, RLHF, GEPA for prompts, dynamic in-context learning) but the key design choice is that these consume *production data with feedback signals*, not curated offline datasets. The system is designed to continuously improve from real usage, not from periodic offline tuning cycles.

**Adaptive A/B testing (bandits) over fixed experiments.** Rather than running fixed A/B splits, TensorZero supports adaptive experimentation (multi-armed bandits) that shifts traffic toward better-performing variants during the experiment itself. This reduces the cost of experimentation — you don't lose as much value running an inferior variant to completion.

**Self-hosted, open-source, GitOps-friendly.** The platform is entirely self-hosted with no required cloud dependency. Configuration is file-based and version-controllable. This is a deliberate choice to serve industrial-grade deployments where data sovereignty, compliance, and auditability are constraints — and to avoid the lock-in that comes with managed LLMOps SaaS.

**TensorZero Autopilot as a paid layer on top.** The open-source platform handles the data collection infrastructure; Autopilot is a paid "automated AI engineer" that analyzes the observability data, sets up evals, and runs the optimization loop autonomously. Clean separation between the open-source plumbing and the commercial intelligence layer.

## Architecture Snapshot

- **Gateway:** single Docker container, Rust, OpenAI-compatible API
- **Storage:** ClickHouse for inferences and feedback (user's own database)
- **Evaluation:** inference evaluations (unit tests) + workflow evaluations (integration tests); LLM judges optimized to align with human preferences
- **Optimization:** SFT, GEPA (automated prompt engineering), DICL (dynamic in-context learning), best-of-N
- **Observability:** OpenTelemetry OTLP export, Prometheus metrics, TensorZero UI

## Notable Patterns

- Fine-tuning a small model (GPT-4o Mini) to outperform a large model (GPT-4o) on specific tasks using TensorZero's data pipeline — cost reduction without capability loss
- LLM judges are themselves TensorZero functions, optimized using the same feedback loop as the production models they evaluate
- OpenTelemetry integration means TensorZero observability data flows into existing application observability stacks (Datadog, Grafana, etc.)

## Concepts Touched

- [[LLMOps]]
- [[LLM-Observability]]
- [[LLM-Gateway]]
- [[Fine-Tuning]]
- [[Prompt-Optimization]]
- [[Experimentation-and-AB-Testing]]
- [[Data-Flywheel]]
- [[LLM-Evaluation]]
- [[LLM-Infrastructure]]

## Inbound Sources

- `/raw/Repos/tensorzero.md`
