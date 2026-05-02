---
title: "Two agents, one prompt"
created: 2026-04-26
updated: 2026-04-26
type: summary
tags:
  - agent_system
  - comparison
  - fine-tuning
  - benchmark
  - developer-tools
sources:
  - raw/Articles/Two agents, one prompt.md
---

# Two agents, one prompt

Daniel van Strien gave two coding agents the same one-line prompt — fine-tune a classifier on `biglam/on_the_books` via `hf jobs` and push to the Hub — and compared what each *chose* to do beyond producing working weights.

## The Setup

- **Claude Code** on Opus 4.7
- **Pi** running on Kimi K2.6 (open weights, via API)
- Same prompt, parallel runs, ~13 minutes each
- Task: binary classifier for Jim Crow laws from UNC Libraries' *On the Books* dataset

## Headline Results

| | Claude Code | Pi+Kimi |
|---|---|---|
| Base model | ModernBERT-base (8K context) | RoBERTa-base |
| F1 (jim_crow) | 0.962 | 0.947 |
| Accuracy | 0.978 | not reported |
| Class imbalance | inverse-frequency weighted loss | not addressed |
| Model card | full (use, limits, ethics, hparams, citation) | auto-generated Trainer placeholder |
| Domain tags | 7 | 0 |

## The Interesting Differences

The F1 gap (~1.5pp) is real but small. The striking differences are in judgment and professional thoroughness:

- **Base model choice.** Claude picked ModernBERT — the obvious 2025 choice for legal text with its 8K context window. Pi+Kimi went with RoBERTa-base. Both work; only one is a current decision.
- **Data leakage detection.** The dataset's `source` field is 100% positive for `paschal` and 92% positive for `murray`. Claude noticed this in the dataset card and explicitly excluded `source`. Pi+Kimi didn't mention it.
- **Class imbalance handling.** ~29% positive class. Claude added inverse-frequency class weights. Pi+Kimi used default cross-entropy.
- **Documentation quality.** Claude wrote a full model card with intended use, limitations, OCR-noise caveats, ethical framing, full hyperparameters, per-epoch metrics, and citation. Pi+Kimi shipped the auto-generated `Trainer` template.
- **Discoverability.** Claude added 7 domain tags (`legal`, `glam`, `jim-crow`, etc.). Pi+Kimi added zero. One model is findable by an archivist; the other isn't.

## Key Takeaways

- **Judgment > metrics.** When agents produce similar performance numbers, the real differentiator is what they decide to do beyond the minimum: data leakage awareness, class imbalance handling, documentation, discoverability.
- **Agents + hf jobs lower the barrier.** Domain experts without ML expertise or local GPUs can now produce trained models. The bottleneck is shifting from infrastructure to data quality and domain expertise.
- **Datasets remain the biggest gap.** Agents still struggle with domain-specific data from scratch, but with domain expert hand-holding, the full pipeline (unlabeled → labeled → trained model) is achievable.
- **This is not a benchmark.** N=1, single dataset, single run. The value is in the qualitative comparison of agent decision-making, not the quantitative metrics.

## Relevance to Wiki Concepts

- See [[Agent-Benchmarking]] for the broader challenge of evaluating agents beyond task completion
- See [[Claude-Code]] for the tool that produced the more thorough output
- See [[Agent-Skills]] for how packaged expertise affects agent judgment

## Source

- Article: [Two agents, one prompt](https://danielvanstrien.xyz/posts/2026/agent-race/) by Daniel van Strien
- Claude's model: [davanstrien/jim-crow-laws-claude-code](https://huggingface.co/davanstrien/jim-crow-laws-claude-code)
- Pi+Kimi's model: [davanstrien/jim-crow-laws-pi-kimi](https://huggingface.co/davanstrien/jim-crow-laws-pi-kimi)
- Agent traces: [davanstrien/agent-race-traces](https://huggingface.co/datasets/davanstrien/agent-race-traces)
