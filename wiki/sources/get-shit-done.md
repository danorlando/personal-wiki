---
tags:
  - claude_code
  - spec_driven_development
  - context_engineering
  - workflow_system
updated: 2026-04-26
source: https://github.com/gsd-build/get-shit-done
---

# Get Shit Done (GSD)

A meta-prompting, context engineering, and spec-driven development system for Claude Code that solves "context rot" — the quality degradation that occurs as an LLM's context window fills — by breaking work into phases executed in fresh context windows with parallel subagents.

## Key Design Decisions / Architecture

- **Context rot as the core problem**: GSD's foundational insight is that long sessions degrade quality because accumulated garbage in the context window causes the model to make increasingly poor decisions. The solution is not to manage one long session better, but to structure work so each execution unit gets a fresh 200k context.
- **Thin orchestrator + specialized subagents**: Every stage uses the same pattern — a thin orchestrator spawns specialized agents (researcher, planner, checker, executor, verifier, debugger), collects results, and routes to the next step. The orchestrator never does heavy lifting. This keeps the main context at 30-40% even through large parallel workloads.
- **Wave execution for parallelism**: Plans are grouped into dependency waves. Within a wave, plans run in parallel; waves are sequential. The key insight is that "vertical slices" (one feature end-to-end per plan) parallelize better than "horizontal layers" (all models, then all APIs), because they produce fewer file conflicts.
- **XML prompt formatting**: Every task plan uses structured XML (`<task>`, `<files>`, `<action>`, `<verify>`, `<done>`) optimized for Claude's parsing. This eliminates ambiguity and provides built-in verification criteria at the task level.
- **Context engineering as file system**: GSD maintains a structured set of context files — `PROJECT.md`, `REQUIREMENTS.md`, `ROADMAP.md`, `STATE.md`, `CONTEXT.md`, `PLAN.md`, `SUMMARY.md` — each with a specific role and size limits calibrated to where Claude's quality degrades. The file system IS the context engineering layer.
- **Multi-layer security**: Because GSD generates markdown files that become LLM system prompts, user-controlled text flowing into planning artifacts is a potential indirect prompt injection vector. GSD implements path traversal prevention, a centralized prompt injection scanner, a PreToolUse prompt guard hook, and safe JSON parsing as defense-in-depth.
- **Model profiles by role**: Planning uses Opus, execution uses Sonnet, verification uses Sonnet (balanced profile default). Budget profile drops to Sonnet/Haiku throughout. This matches [[everything-claude-code]]'s model routing philosophy — match model cost to task complexity.

## Notable Patterns

- **Discuss phase captures taste before research**: Before researching implementation approaches, GSD asks about your preferences (layout, error handling, depth) and writes them to `CONTEXT.md`. The researcher reads this file, so investigation is targeted at *your* vision rather than generic best practices.
- **Atomic git commits per task**: Every task gets its own commit immediately after completion with a structured prefix (e.g. `feat(08-02): add email confirmation flow`). This makes git bisect precise, enables surgical reverts, and gives future Claude sessions a clean history.
- **Quality gates taxonomy**: 4 canonical gate types — pre-flight, revision, escalation, abort — wired into plan-checker and verifier agents. Schema drift detection, security enforcement anchored to threat models, and scope reduction detection (prevents the planner from silently dropping requirements).
- **Workstreams for parallel milestone work**: Named workstreams allow parallel work on different aspects of the same milestone, with explicit switching and completion flows.

## Concepts touched

- [[Claude Code]]
- [[Context Engineering]]
- [[Spec-Driven Development]]
- [[Claude Subagents]]
- [[Context Rot]]
- [[Token Optimization]]
- [[Wave Execution]]
- [[Agentic Development]]
- [[Prompt Injection]]
- [[Multi-Agent Orchestration]]
