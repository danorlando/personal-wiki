---
title: "gstack"
created: 2026-04-26
updated: 2026-04-26
type: summary
tags:
  - claude_code
  - virtual_team
  - workflow_system
  - OSS
source: https://github.com/garrytan/gstack
---

# gstack

Garry Tan's (Y Combinator CEO) personal open-source Claude Code skill stack, framing Claude Code as a virtual engineering team with 23+ specialist roles — CEO, Eng Manager, Designer, QA Lead, Security Officer, Release Engineer — structured as a complete sprint process from ideation to production deployment.

## Key Design Decisions / Architecture

- **Sprint as the organizing metaphor**: gstack is explicitly a *process*, not a collection of tools. Skills are sequenced to mirror a product sprint — Think → Plan → Build → Review → Test → Ship → Reflect — and each skill writes outputs that the next skill reads. `/office-hours` writes a design doc that `/plan-ceo-review` reads; `/plan-eng-review` writes a test plan that `/qa` picks up. This eliminates the context-loss that happens when tools are used ad-hoc.
- **Role specialization reduces cognitive load**: Rather than prompting Claude with "do a thorough review," gstack encodes what each specialist role actually does. The `senior designer` rates design dimensions 0-10 and explains what a 10 looks like. The `Staff Engineer` finds bugs that pass CI. This specificity produces better outputs than generic instructions.
- **Real browser as a force multiplier**: `/qa` gives Claude a real Chromium browser (via Playwright), enabling it to actually navigate the app, find bugs, fix them, and generate regression tests. This shifted the author's parallel sprint count from 6 to 12 workers, because Claude could self-verify rather than requiring human validation of each visual change.
- **`/design-shotgun` → `/design-html` pipeline**: Design exploration and implementation are separated. `/design-shotgun` generates 4-6 AI mockup variants with taste memory, iterates visually until the user approves. `/design-html` converts the approved mockup to production HTML using Pretext for proper computed text layout (reflows on resize, dynamic heights). The output is shippable, not a demo.
- **Cross-agent coordination via `/pair-agent`**: Two agents from different vendors (e.g., Claude Code + Codex) can share a real browser through a session token exchange mechanism with scoped tokens, tab isolation, rate limiting, and activity attribution. This is described as the first agent-to-agent browser coordination with real security.
- **Auto-update with throttling**: gstack auto-checks for updates at session start (throttled to once/hour, network-failure-safe, silent). This treats a skill pack as a live product that developers should always be running at latest, without manual update friction.
- **Multi-AI second opinion via `/codex`**: Gets an independent review from OpenAI's Codex CLI in three modes — standard review, adversarial challenge (actively tries to break the code), and open consultation. When both `/review` (Claude) and `/codex` (OpenAI) have reviewed, cross-model analysis shows which findings overlap vs. which are unique to each model.

## Notable Patterns

- **Voice-friendly trigger phrases**: Skills are designed to activate on natural speech ("run a security check", "test the website") rather than requiring exact slash command names, enabling voice input workflows.
- **`/investigate` auto-freeze**: The debugging skill automatically activates `/freeze` (edit lock) on the module being investigated, preventing Claude from "fixing" unrelated code while debugging.
- **Review routing by audience**: The guide distinguishes `/plan-design-review` (for end users) vs `/plan-devex-review` (for developers/API consumers) vs `/plan-eng-review` (for architecture) — different specialists for different success criteria.
- **`/document-release` auto-invoked by `/ship`**: Documentation is kept current automatically rather than as a separate step, eliminating README drift.

## Concepts touched

- [[Claude Code]]
- [[Claude Skills]]
- [[Virtual Engineering Team]]
- [[Agentic Development]]
- [[Multi-Agent Orchestration]]
- [[Agent Security]]
- [[Design Systems]]
- [[Test-Driven Development]]
- [[Cross-Harness Compatibility]]
