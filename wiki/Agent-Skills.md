---
title: "Agent Skills"
created: 2026-04-26
updated: 2026-05-02
type: concept
tags:
  - concept
  - claude-code
  - extensibility
---

# Agent Skills

Packaged units of expertise for AI agents. In [[Claude Code]], a skill is a **folder** (not just a markdown file) containing instructions, scripts, assets, data, and optional configuration. Skills can be installed, shared, and composed.

## Structure

```
my-skill/
  SKILL.md          # Instructions for Claude; frontmatter with config/hooks
  references/       # API docs, usage examples, etc.
  assets/           # Templates, static data
  scripts/          # Helper scripts Claude can call or compose
  config.json       # Setup data (e.g., Slack channel to post to)
```

## Why Folders Matter

The filesystem itself is a form of **[[Progressive Disclosure]]**: Claude reads `SKILL.md`, which tells it what other files exist, and Claude fetches them when needed. This avoids front-loading all context at session start.

## The 9 Skill Categories (per Anthropic internal usage)

1. **Library & API Reference** — correct usage of internal/external libraries
2. **Product Verification** — test flows with Playwright, tmux, assertions
3. **Data Fetching & Analysis** — connect to data/monitoring stacks
4. **Business Process & Team Automation** — one-command repetitive workflows
5. **Code Scaffolding & Templates** — boilerplate with org-specific conventions
6. **Code Quality & Review** — style enforcement, adversarial review
7. **CI/CD & Deployment** — build, test, rollout, rollback
8. **Runbooks** — symptom → investigation → structured report
9. **Infrastructure Operations** — maintenance with guardrails

## Writing Good Skills

- **Gotchas section** is the highest-signal content — populate from real Claude failures
- **Description field is for the model** — write it as a trigger condition, not a summary
- **Don't state the obvious** — Claude already knows general coding; focus on org-specific corrections
- **Avoid railroading** — give information, preserve flexibility to adapt
- **On-demand hooks** — skills can register session-scoped hooks that aren't always on

## Distribution

- In-repo (`.claude/skills/`) — simple but adds context overhead
- Plugin marketplace — installable on demand; scales better for large orgs

## Open Standard

Agent Skills are an open standard; they work across any tool that supports them, not just Claude Code.

## Cross-Tool Portability

Skills work across Claude Code, Cursor, Codex, Gemini CLI, and other harnesses that support the SKILL.md format. everything-claude-code implements a DRY adapter pattern that maps skill invocations to the native interface of each harness — a single skill library deployed across all tools ([[sources/everything-claude-code]]).

oh-my-claudecode adds project-scope and user-scope skill storage (`.omc/skills/` vs `~/.omc/skills/`) with project-scope overriding user-scope — enabling both personal and team-shared patterns from the same install ([[sources/oh-my-claudecode]]).

## Self-Improving Skills

Hermes Agent and OpenSpace both implement closed learning loops that generate new skills from execution traces — an agent completes a task, the system analyzes the trace, and a new or updated skill is created. This is a distinct architectural pattern from skills-as-static-packages. See [[Self-Evolving-Skills]] ([[sources/hermes-agent]], [[sources/openspace]]).

Autogenesis takes this further: under its [[Agent-Protocol]] (AGP), skills are one of five RSPL resource types that can evolve. The SEPL operator algebra (Reflect → Select → Improve → Evaluate → Commit) treats skills as first-class, versioned resources with auditable lineage and rollback — a generalization from skill-only evolution to full-stack [[Self-Evolving-Agents]] ([[sources/autogenesis]]).

## Skills and Agent Judgment

The [[sources/two-agents-one-prompt|Two agents, one prompt]] comparison shows how skill quality affects agent output beyond task completion. Claude Code's ability to detect data leakage, handle class imbalance, and produce professional documentation may reflect deeper skill-level knowledge embedded in its training and tool surface. This connects to the broader question in [[Agent-Benchmarking]]: how do we measure whether an agent's skills produce *good* outcomes, not just *completed* outcomes?

## Inbound sources
- [[sources/claude-code-how-we-use-skills]]
- [[sources/advent-of-claude-31-days]]
- [[sources/claude-code-seeing-like-an-agent]]
- [[sources/claude-skills-alirezarezvani]]
- [[sources/addyosmani-agent-skills]]
- [[sources/everything-claude-code]]
- [[sources/gstack]]
- [[sources/obra-superpowers]]
- [[sources/oh-my-claudecode]]
- [[sources/hermes-agent]]
- [[sources/last30days-skill]]
- [[sources/two-agents-one-prompt]]
- [[sources/autogenesis]]
