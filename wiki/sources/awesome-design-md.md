---
title: "awesome design md"
created: 2026-04-26
updated: 2026-04-26
type: summary
tags:
  - repository
  - developer_tool
  - prompts
  - design
  - agent_prompting
source: https://github.com/VoltAgent/awesome-design-md
---

A curated collection of `DESIGN.md` files extracted from real, popular websites — ready to drop into any project so AI coding agents can generate UI that matches established design systems without Figma exports, JSON schemas, or special tooling.

## Key Design Decisions

**The core insight: markdown is the LLM-native design format.** The project is built around Google Stitch's `DESIGN.md` concept, which bets that a plain-text design system document is both sufficient and optimal for AI agents. The format mirrors the role `AGENTS.md` plays for build instructions, but for visual identity instead. Because LLMs already excel at parsing markdown, there is no parse layer, no intermediate representation, and no tooling dependency — the file is the interface.

**Extraction over generation.** Rather than having users describe their desired style abstractly, this repo provides pre-extracted design tokens from real, recognizable sites (Vercel, Linear, Stripe, Claude, etc.). The curation act is the value: someone has already reverse-engineered the CSS, named the semantic roles, and formatted them into the standard structure. Users get institutional design quality for free.

**Standardized 9-section format.** Every `DESIGN.md` follows the same schema: Visual Theme, Color Palette with semantic names and hex values, Typography hierarchy, Component stylings with states, Layout principles, Depth/elevation/shadow system, Do's and Don'ts guardrails, Responsive behavior, and an Agent Prompt Guide with copy-ready prompts. This consistency means an agent that knows how to read one file knows how to read all of them.

**Companion preview artifacts.** Each entry ships with `preview.html` and `preview-dark.html` — visual catalogs showing color swatches, type scale, buttons, and cards. These serve double duty: humans can verify accuracy before committing to a style, and they provide a ground truth for the extracted tokens.

**Tradeoff: fidelity vs. liveness.** The files are extracted snapshots, not live mirrors. A site that updates its design system will not automatically update its `DESIGN.md`. The repo depends on community PRs to stay current, which creates a maintenance debt proportional to how actively a site iterates on its visual identity.

## Notable Patterns

- Semantic color naming (e.g., "warm terracotta accent" for Claude, "signature purple gradients" for Stripe) is prioritized over raw hex values alone — giving agents both the token and the intent.
- Coverage spans AI tools, dev platforms, infrastructure, fintech, enterprise consumer brands, and luxury automotive — a deliberately broad set that demonstrates the format applies across industries, not just developer tooling.
- The `Agent Prompt Guide` section within each file is a meta-layer: prompts designed to instruct agents on how to use the file, creating a self-contained briefing document.
- The repo is linked to [VoltAgent](https://github.com/VoltAgent/voltagent), an AI agent framework, suggesting `DESIGN.md` is part of a broader agent-first development workflow.

## Concepts touched

- [[Agent-Skills]] — DESIGN.md files function as a specialized skill/context file for design agents, analogous to SKILL.md for behavioral skills
- [[Claude-Code]] — directly applicable as a drop-in context file for coding agent workflows
- [[Agent-Native-Software]] — illustrates the pattern of plain-text configuration files designed for agent consumption rather than human tooling
- [[Progressive-Disclosure]] — the companion preview HTML files serve as the human-readable layer over the machine-readable DESIGN.md
