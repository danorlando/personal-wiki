---
title: "autoresearch (Karpathy)"
created: 2026-04-26
updated: 2026-04-26
type: summary
tags:
  - autonomous-research
  - agentic-ai
  - ml-training
  - karpathy
  - llm-training
  - self-modifying-systems
source: https://github.com/karpathy/autoresearch
---

# autoresearch (Karpathy)

Andrej Karpathy's proof-of-concept for fully autonomous ML research: give an AI agent a single-GPU LLM training setup and let it run experiments overnight, modifying training code, measuring results, and iterating — all without human involvement. The human programs the *research org* (via `program.md`), not the experiments themselves.

## Key Design Decisions

**The human codes the research organization, not the experiments.** The central inversion: instead of writing Python to run experiments, you write `program.md` — a Markdown file that defines how the agent should operate as a research organization. The agent reads this and runs the actual experiments. This reframes the human's job from "researcher who runs code" to "meta-researcher who programs research strategy."

**Fixed 5-minute wall-clock time budget per experiment.** All experiments run for exactly 5 minutes regardless of what the agent changes (model size, batch size, architecture, etc.). This makes experiments directly comparable across runs — a necessary condition for fair evaluation when the agent can modify the very things that affect compute requirements. The tradeoff: results are platform-specific and non-reproducible across different hardware.

**Single file the agent can modify.** The agent only edits `train.py`. Everything else (`prepare.py`, tokenizer, data loading, evaluation) is fixed. This constrains the search space to what matters — model architecture, optimizer, hyperparameters, training loop — while keeping diffs reviewable and preventing the agent from escaping into irrelevant parts of the codebase.

**val_bpb as the universal metric.** Validation bits-per-byte is vocab-size-independent, meaning the agent can change the tokenizer or vocabulary size and results still compare fairly. This metric choice is what makes fair comparison possible across architectural changes, not just hyperparameter tweaks.

**Self-contained, no distributed training.** Deliberate minimalism: one GPU, one file, one metric, no external dependencies beyond PyTorch. The goal is accessibility and reproducibility of the *research loop itself*, not maximum performance. More complex setups would make it harder to verify whether the agent is actually improving the model or gaming the infrastructure.

**program.md as the compounding artifact.** The human iterates on `program.md` over time to find the "research org code" that achieves fastest progress — the research strategy itself becomes the thing that compounds and improves, not just the model. This is Karpathy's version of the meta-learning loop applied to research organizations.

## What the Agent Actually Does

Each iteration:
1. Reads `program.md` for context and strategy
2. Modifies `train.py` (architecture, optimizer, hyperparameters — anything is fair game)
3. Trains for exactly 5 minutes
4. Evaluates val_bpb
5. Keeps the change if it improved, reverts if not
6. Logs the experiment and repeats

~12 experiments/hour, ~100 experiments overnight.

## Notable Patterns

- **Karpathy's framing:** "You are programming the research org, not the experiments" — a clean conceptual separation between meta-level (strategy) and object-level (experiments)
- Built on `nanochat` — Karpathy's single-GPU GPT implementation — as the training substrate
- Uses `uv` for dependency management, keeping setup minimal
- Karpathy explicitly notes the repo is intentionally minimal and does not plan to add CPU/MPS support himself; the simplicity is the point
- Requires a single NVIDIA GPU (tested on H100) — not designed for consumer hardware, though forks exist for smaller setups

## Concepts Touched

- [[Autonomous-Research]]
- [[Agentic-AI]]
- [[Self-Modifying-Systems]]
- [[LLM-Training]]
- [[Meta-Learning]]
- [[Experimental-Loops]]
- [[AI-Research-Automation]]

## Inbound Sources

- `/raw/Repos/autoresearch.md`
