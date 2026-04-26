---
title: "tensorzero/tensorzero: TensorZero is an open-source LLMOps platform that unifies an LLM gateway, observability, evaluation, optimization, and experimentation."
source: https://github.com/tensorzero/tensorzero
author:
published:
created: 2026-04-06
description: TensorZero is an open-source LLMOps platform that unifies an LLM gateway, observability, evaluation, optimization, and experimentation. - tensorzero/tensorzero
tags:
  - OSS
  - repository
  - readme
  - github
---
![TensorZero Logo](https://github.com/user-attachments/assets/9d0a93c6-7685-4e57-9737-7cbeb338a218)

## TensorZero

![GitHub Trending - #1 Repository Of The Day](https://camo.githubusercontent.com/87d5893d1cf54a24538828d062b22e20b5b2d53309a609d948b1940245d86fa8/68747470733a2f2f7777772e74656e736f727a65726f2e636f6d2f6769746875622d7472656e64696e672d62616467652e737667)

**TensorZero is an open-source LLMOps platform that unifies:**

- **Gateway:** access every LLM provider through a unified API, built for performance (<1ms p99 latency)
- **Observability:** store inferences and feedback in your database, available programmatically or in the UI
- **Evaluation:** benchmark individual inferences or end-to-end workflows using heuristics, LLM judges, etc.
- **Optimization:** collect metrics and human feedback to optimize prompts, models, and inference strategies
- **Experimentation:** ship with confidence with built-in A/B testing, routing, fallbacks, retries, etc.

You can take what you need, adopt incrementally, and complement with other tools. It plays nicely with the **OpenAI SDK**, **OpenTelemetry**, and **every major LLM provider**.

TensorZero is used by companies ranging from frontier AI startups to the Fortune 10 and fuels ~1% of global LLM API spend today.

  

**[Website](https://www.tensorzero.com/)** · **[Docs](https://www.tensorzero.com/docs)** · · **[Slack](https://www.tensorzero.com/slack)** · **[Discord](https://www.tensorzero.com/discord)**  
  
**[Quick Start (5min)](https://www.tensorzero.com/docs/quickstart)** · **[Deployment Guide](https://www.tensorzero.com/docs/deployment/tensorzero-gateway)** · **[API Reference](https://www.tensorzero.com/docs/gateway/api-reference)** · **[Configuration Reference](https://www.tensorzero.com/docs/gateway/configuration-reference)**

## Demo

tensorzero-demo.mp4<video src="https://github.com/user-attachments/assets/04a8466e-27d8-4189-b305-e7cecb6881ee" controls="controls"></video>

## Features

> [!note] Note
> ### 🆕 TensorZero Autopilot
> 
> TensorZero Autopilot is an **automated AI engineer** powered by TensorZero that analyzes LLM observability data, sets up evals, optimizes prompts and models, and runs A/B tests.
> 
> It **dramatically improves the performance of LLM agents** across diverse tasks:
> 
> [![Bar chart showing baseline vs. optimized scores across diverse LLM tasks](https://private-user-images.githubusercontent.com/1275491/568594816-aa474fe3-b55a-48aa-9f0d-e7c2f8e32ccd.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzU1MTQyNDYsIm5iZiI6MTc3NTUxMzk0NiwicGF0aCI6Ii8xMjc1NDkxLzU2ODU5NDgxNi1hYTQ3NGZlMy1iNTVhLTQ4YWEtOWYwZC1lN2MyZjhlMzJjY2QucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDQwNiUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA0MDZUMjIxOTA2WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9NmRjODQxZDFiMzBjNzQ0ZjIzOWFkZjJjMzAwODYwMjg1ZTNjMTg5YTBiY2YzZjhkNGIyMTk4ZTQxNjcyMWJlZiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.mmNfEbIy3cldeD2bX2e0em_SvzgRSIouuBo_u8e3Sx8)](https://private-user-images.githubusercontent.com/1275491/568594816-aa474fe3-b55a-48aa-9f0d-e7c2f8e32ccd.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzU1MTQyNDYsIm5iZiI6MTc3NTUxMzk0NiwicGF0aCI6Ii8xMjc1NDkxLzU2ODU5NDgxNi1hYTQ3NGZlMy1iNTVhLTQ4YWEtOWYwZC1lN2MyZjhlMzJjY2QucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDQwNiUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA0MDZUMjIxOTA2WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9NmRjODQxZDFiMzBjNzQ0ZjIzOWFkZjJjMzAwODYwMjg1ZTNjMTg5YTBiY2YzZjhkNGIyMTk4ZTQxNjcyMWJlZiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.mmNfEbIy3cldeD2bX2e0em_SvzgRSIouuBo_u8e3Sx8)  
> 
> **[Learn more →](https://www.tensorzero.com/blog/automated-ai-engineer/)**    **[Schedule a demo →](https://www.tensorzero.com/schedule-demo)**

### 🌐 LLM Gateway

> **Integrate with TensorZero once and access every major LLM provider.**

- **[Call any LLM](https://www.tensorzero.com/docs/gateway/call-any-llm)** (API or self-hosted) through a single unified API
- Infer with **[tool use](https://www.tensorzero.com/docs/gateway/guides/tool-use)**, **[structured outputs (JSON)](https://www.tensorzero.com/docs/gateway/generate-structured-outputs)**, **[batch](https://www.tensorzero.com/docs/gateway/guides/batch-inference)**, **[embeddings](https://www.tensorzero.com/docs/gateway/generate-embeddings)**, **[multimodal (images, files)](https://www.tensorzero.com/docs/gateway/call-llms-with-image-and-file-inputs)**, **[caching](https://www.tensorzero.com/docs/gateway/guides/inference-caching)**, etc.
- **[Create prompt templates and schemas](https://www.tensorzero.com/docs/gateway/create-a-prompt-template)** to enforce a structured interface between your application and the LLMs
- Satisfy extreme throughput and latency needs, thanks to 🦀 Rust: **[<1ms p99 latency overhead at 10k+ QPS](https://www.tensorzero.com/docs/gateway/benchmarks)**
- **[Ensure high availability](https://www.tensorzero.com/docs/gateway/guides/retries-fallbacks)** with routing, retries, fallbacks, load balancing, granular timeouts, etc.
- **[Track usage and cost](https://www.tensorzero.com/docs/operations/track-usage-and-cost)** and **[enforce custom rate limits](https://www.tensorzero.com/docs/operations/enforce-custom-rate-limits)** with granular scopes (e.g. tags)
- **[Set up auth for TensorZero](https://www.tensorzero.com/docs/operations/set-up-auth-for-tensorzero)** to allow clients to access models without sharing provider API keys

#### Supported Model Providers

**[Anthropic](https://www.tensorzero.com/docs/gateway/guides/providers/anthropic)**, **[AWS Bedrock](https://www.tensorzero.com/docs/gateway/guides/providers/aws-bedrock)**, **[AWS SageMaker](https://www.tensorzero.com/docs/gateway/guides/providers/aws-sagemaker)**, **[Azure](https://www.tensorzero.com/docs/gateway/guides/providers/azure)**, **[DeepSeek](https://www.tensorzero.com/docs/gateway/guides/providers/deepseek)**, **[Fireworks](https://www.tensorzero.com/docs/gateway/guides/providers/fireworks)**, **[GCP Vertex AI Anthropic](https://www.tensorzero.com/docs/gateway/guides/providers/gcp-vertex-ai-anthropic)**, **[GCP Vertex AI Gemini](https://www.tensorzero.com/docs/gateway/guides/providers/gcp-vertex-ai-gemini)**, **[Google AI Studio (Gemini API)](https://www.tensorzero.com/docs/gateway/guides/providers/google-ai-studio-gemini)**, **[Groq](https://www.tensorzero.com/docs/gateway/guides/providers/groq)**, **[Hyperbolic](https://www.tensorzero.com/docs/gateway/guides/providers/hyperbolic)**, **[Mistral](https://www.tensorzero.com/docs/gateway/guides/providers/mistral)**, **[OpenAI](https://www.tensorzero.com/docs/gateway/guides/providers/openai)**, **[OpenRouter](https://www.tensorzero.com/docs/gateway/guides/providers/openrouter)**, **[SGLang](https://www.tensorzero.com/docs/gateway/guides/providers/sglang)**, **[TGI](https://www.tensorzero.com/docs/gateway/guides/providers/tgi)**, **[Together AI](https://www.tensorzero.com/docs/gateway/guides/providers/together)**, **[vLLM](https://www.tensorzero.com/docs/gateway/guides/providers/vllm)**, and **[xAI (Grok)](https://www.tensorzero.com/docs/gateway/guides/providers/xai)**.

Need something else? TensorZero also supports **[any OpenAI-compatible API (e.g. Ollama)](https://www.tensorzero.com/docs/gateway/guides/providers/openai-compatible)**.

#### Usage Example

You can use TensorZero with any OpenAI SDK (Python, Node, Go, etc.) or OpenAI-compatible client.

1. **[Deploy the TensorZero Gateway](https://www.tensorzero.com/docs/deployment/tensorzero-gateway)** (one Docker container).
2. Update the `base_url` and `model` in your OpenAI-compatible client.
3. Run inference:
```
from openai import OpenAI

# Point the client to the TensorZero Gateway
client = OpenAI(base_url="http://localhost:3000/openai/v1", api_key="not-used")

response = client.chat.completions.create(
    # Call any model provider (or TensorZero function)
    model="tensorzero::model_name::anthropic::claude-sonnet-4-6",
    messages=[
        {
            "role": "user",
            "content": "Share a fun fact about TensorZero.",
        }
    ],
)
```

See **[Quick Start](https://www.tensorzero.com/docs/quickstart)** for more information.

### 🔍 LLM Observability

> **Zoom in to debug individual API calls, or zoom out to monitor metrics across models and prompts over time — all using the open-source TensorZero UI.**

- Store inferences and **[feedback (metrics, human edits, etc.)](https://www.tensorzero.com/docs/gateway/guides/metrics-feedback)** in your own database
- Dive into individual inferences or high-level aggregate patterns using the TensorZero UI or programmatically
- **[Build datasets](https://www.tensorzero.com/docs/gateway/api-reference/datasets-datapoints)** for optimization, evaluation, and other workflows
- Replay historical inferences with new prompts, models, inference strategies, etc.
- **[Export OpenTelemetry traces (OTLP)](https://www.tensorzero.com/docs/operations/export-opentelemetry-traces)** and **[export Prometheus metrics](https://www.tensorzero.com/docs/operations/export-prometheus-metrics)** to your favorite application observability tools
- Soon: AI-assisted debugging and root cause analysis; AI-assisted data labeling

### 📈 LLM Optimization

> **Send production metrics and human feedback to easily optimize your prompts, models, and inference strategies — using the UI or programmatically.**

- Optimize your models with **[supervised fine-tuning](https://www.tensorzero.com/docs/optimization/supervised-fine-tuning-sft)**, RLHF, and other techniques
- Optimize your prompts with automated prompt engineering algorithms like **[GEPA](https://www.tensorzero.com/docs/optimization/gepa)**
- Optimize your **[inference strategy](https://www.tensorzero.com/docs/gateway/guides/inference-time-optimizations)** with **[dynamic in-context learning](https://www.tensorzero.com/docs/optimization/dynamic-in-context-learning-dicl)**, best/mixture-of-N sampling, etc.
- Enable a feedback loop for your LLMs: a data & learning flywheel turning production data into smarter, faster, and cheaper models
- Soon: synthetic data generation

### 📊 LLM Evaluation

> **Compare prompts, models, and inference strategies using evaluations powered by heuristics and LLM judges.**

- **[Evaluate individual inferences](https://www.tensorzero.com/docs/evaluations/inference-evaluations/tutorial)** with *inference evaluations* powered by heuristics or LLM judges (≈ unit tests for LLMs)
- **[Evaluate end-to-end workflows](https://www.tensorzero.com/docs/evaluations/workflow-evaluations/tutorial)** with *workflow evaluations* with complete flexibility (≈ integration tests for LLMs)
- Optimize LLM judges just like any other TensorZero function to align them to human preferences
- Soon: more built-in evaluators; headless evaluations

| **Evaluation » UI** | **Evaluation » CLI** |
| --- | --- |
| [![](https://private-user-images.githubusercontent.com/1275491/432117870-f4bf54e3-1b63-46c8-be12-2eaabf615699.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzU1MTQyNDYsIm5iZiI6MTc3NTUxMzk0NiwicGF0aCI6Ii8xMjc1NDkxLzQzMjExNzg3MC1mNGJmNTRlMy0xYjYzLTQ2YzgtYmUxMi0yZWFhYmY2MTU2OTkucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDQwNiUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA0MDZUMjIxOTA2WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9NTNhMmVlNTgxZDFlNzgyYWU0MDYxZjgzZWM5NDdjNjJjOGM1MDIzOWVmMDYyMjU4ZmE3NGI4NTVlMmIwZWZiNSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.OaOIzPaj_q1mldilnxJmN2PhDUDGwL4X85-ml-V75vc)](https://private-user-images.githubusercontent.com/1275491/432117870-f4bf54e3-1b63-46c8-be12-2eaabf615699.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzU1MTQyNDYsIm5iZiI6MTc3NTUxMzk0NiwicGF0aCI6Ii8xMjc1NDkxLzQzMjExNzg3MC1mNGJmNTRlMy0xYjYzLTQ2YzgtYmUxMi0yZWFhYmY2MTU2OTkucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDQwNiUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA0MDZUMjIxOTA2WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9NTNhMmVlNTgxZDFlNzgyYWU0MDYxZjgzZWM5NDdjNjJjOGM1MDIzOWVmMDYyMjU4ZmE3NGI4NTVlMmIwZWZiNSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.OaOIzPaj_q1mldilnxJmN2PhDUDGwL4X85-ml-V75vc) | ``` docker compose run --rm evaluations \   --evaluation-name extract_data \   --dataset-name hard_test_cases \   --variant-name gpt_4o \   --concurrency 5 ```  ``` Run ID: 01961de9-c8a4-7c60-ab8d-15491a9708e4 Number of datapoints: 100 ██████████████████████████████████████ 100/100 exact_match: 0.83 ± 0.03 (n=100) semantic_match: 0.98 ± 0.01 (n=100) item_count: 7.15 ± 0.39 (n=100) ``` |

### 🧪 LLM Experimentation

> **Ship with confidence with built-in A/B testing, routing, fallbacks, retries, etc.**

- **[Run adaptive A/B tests](https://www.tensorzero.com/docs/experimentation/run-adaptive-ab-tests)** to ship with confidence and identify the best prompts and models for your use cases.
- Enforce principled experiments in complex workflows, including support for multi-turn LLM systems, sequential testing, and more.

### & more!

> **Build with an open-source stack well-suited for prototypes but designed from the ground up to support the most complex LLM applications and deployments.**

- Build simple applications or massive deployments with GitOps-friendly orchestration
- **[Extend TensorZero](https://www.tensorzero.com/docs/operations/extend-tensorzero)** with built-in escape hatches, programmatic-first usage, direct database access, and more
- Integrate with third-party tools: specialized observability and evaluations, model providers, agent orchestration frameworks, etc.
- Iterate quickly by experimenting with prompts interactively using the Playground UI

## Frequently Asked Questions

**How is TensorZero different from other LLM frameworks?**

1. TensorZero enables you to optimize complex LLM applications based on production metrics and human feedback.
2. TensorZero supports the needs of industrial-grade LLM applications: low latency, high throughput, type safety, self-hosted, GitOps, customizability, etc.
3. TensorZero unifies the entire LLMOps stack, creating compounding benefits. For example, LLM evaluations can be used for fine-tuning models alongside AI judges.

**Can I use TensorZero with \_\_\_?**

Yes. Every major programming language is supported. It plays nicely with the **OpenAI SDK**, **OpenTelemetry**, and **every major LLM provider**.

**Is TensorZero production-ready?**

Yes. TensorZero is used by companies ranging from frontier AI startups to the Fortune 10 and powers ~1% of the global LLM API spend today.

Here's a case study: **[Automating Code Changelogs at a Large Bank with LLMs](https://www.tensorzero.com/blog/case-study-automating-code-changelogs-at-a-large-bank-with-llms)**

**How much does TensorZero cost?**

TensorZero (LLMOps platform) is 100% self-hosted and open-source.

TensorZero Autopilot (automated AI engineer) is a complementary paid product powered by TensorZero.

**Who is building TensorZero?**

Our technical team includes a former Rust compiler maintainer, machine learning researchers (Stanford, CMU, Oxford, Columbia) with thousands of citations, and the chief product officer of a decacorn startup. We're backed by the same investors as leading open-source projects (e.g. ClickHouse, CockroachDB) and AI labs (e.g. OpenAI, Anthropic). See our **[$7.3M seed round announcement](https://www.tensorzero.com/blog/tensorzero-raises-7-3m-seed-round-to-build-an-open-source-stack-for-industrial-grade-llm-applications/)** and **[coverage from VentureBeat](https://venturebeat.com/ai/tensorzero-nabs-7-3m-seed-to-solve-the-messy-world-of-enterprise-llm-development/)**. We're **[hiring in NYC](https://www.tensorzero.com/jobs)**.

**How do I get started?**

You can adopt TensorZero incrementally. Our **[Quick Start](https://www.tensorzero.com/docs/quickstart)** goes from a vanilla OpenAI wrapper to a production-ready LLM application with observability and fine-tuning in just 5 minutes.

## Get Started

**Start building today.** The **[Quick Start](https://www.tensorzero.com/docs/quickstart)** shows it's easy to set up an LLM application with TensorZero.

**Questions?** Ask us on **[Slack](https://www.tensorzero.com/slack)** or **[Discord](https://www.tensorzero.com/discord)**.

**Using TensorZero at work?** Email us at **[hello@tensorzero.com](mailto:hello@tensorzero.com)** to set up a Slack or Teams channel with your team (free).

## Examples

We are working on a series of **complete runnable examples** illustrating TensorZero's data & learning flywheel.

> **[Optimizing Data Extraction (NER) with TensorZero](https://github.com/tensorzero/tensorzero/tree/main/examples/data-extraction-ner)**
> 
> This example shows how to use TensorZero to optimize a data extraction pipeline. We demonstrate techniques like fine-tuning and dynamic in-context learning (DICL). In the end, an optimized GPT-4o Mini model outperforms GPT-4o on this task — at a fraction of the cost and latency — using a small amount of training data.

> **[Agentic RAG — Multi-Hop Question Answering with LLMs](https://github.com/tensorzero/tensorzero/tree/main/examples/rag-retrieval-augmented-generation/simple-agentic-rag/)**
> 
> This example shows how to build a multi-hop retrieval agent using TensorZero. The agent iteratively searches Wikipedia to gather information, and decides when it has enough context to answer a complex question.

> **[Writing Haikus to Satisfy a Judge with Hidden Preferences](https://github.com/tensorzero/tensorzero/tree/main/examples/haiku-hidden-preferences)**
> 
> This example fine-tunes GPT-4o Mini to generate haikus tailored to a specific taste. You'll see TensorZero's "data flywheel in a box" in action: better variants leads to better data, and better data leads to better variants. You'll see progress by fine-tuning the LLM multiple times.

> **[Image Data Extraction — Multimodal (Vision) Fine-tuning](https://github.com/tensorzero/tensorzero/tree/main/examples/multimodal-vision-finetuning)**
> 
> This example shows how to fine-tune multimodal models (VLMs) like GPT-4o to improve their performance on vision-language tasks. Specifically, we'll build a system that categorizes document images (screenshots of computer science research papers).

> **[Improving LLM Chess Ability with Best-of-N Sampling](https://github.com/tensorzero/tensorzero/tree/main/examples/chess-puzzles/)**
> 
> This example showcases how best-of-N sampling can significantly enhance an LLM's chess-playing abilities by selecting the most promising moves from multiple generated options.

## Blog Posts

We write about LLM engineering on the **[TensorZero Blog](https://www.tensorzero.com/blog)**. Here are some of our favorite posts:

- **[Bandits in your LLM Gateway: Improve LLM Applications Faster with Adaptive Experimentation (A/B Testing)](https://www.tensorzero.com/blog/bandits-in-your-llm-gateway/)**
- **[Is OpenAI's Reinforcement Fine-Tuning (RFT) Worth It?](https://www.tensorzero.com/blog/is-openai-reinforcement-fine-tuning-rft-worth-it/)**
- **[Distillation with Programmatic Data Curation: Smarter LLMs, 5-30x Cheaper Inference](https://www.tensorzero.com/blog/distillation-programmatic-data-curation-smarter-llms-5-30x-cheaper-inference/)**
- **[From NER to Agents: Does Automated Prompt Engineering Scale to Complex Tasks?](https://www.tensorzero.com/blog/from-ner-to-agents-does-automated-prompt-engineering-scale-to-complex-tasks/)**