---
tags:
  - claude_code
  - multi_agent
  - orchestration
  - OSS
updated: 2026-04-26
source: https://github.com/Yeachan-Heo/oh-my-claudecode
---

# oh-my-claudecode (OMC)

A teams-first multi-agent orchestration layer for Claude Code that provides a staged pipeline (plan → PRD → execute → verify → fix loop) with zero learning curve, natural language task routing, smart model cost optimization, and optional cross-provider orchestration via Codex and Gemini CLI workers.

## Key Design Decisions / Architecture

- **Team as the canonical orchestration surface**: Since v4.1.7, "Team" replaces the legacy `swarm` keyword. The Team pipeline is explicit and staged: `team-plan → team-prd → team-exec → team-verify → team-fix (loop)`. This forces planning and product requirements to exist before execution begins, and loops on fix until verification passes — preventing silent partial completions.
- **tmux CLI workers for cross-provider orchestration**: Rather than using MCP servers to invoke Codex and Gemini (which was removed in v4.4.0), OMC spawns real `codex` / `gemini` / `claude` CLI processes in tmux panes on-demand. Workers die when their task completes, eliminating idle resource usage. This sidesteps API compatibility issues by using each tool's native CLI.
- **Smart model routing for cost optimization**: Haiku for simple tasks, Opus for complex reasoning. OMC claims 30-50% token savings from routing — routing is implemented as a first-class system concern rather than a user-managed setting.
- **Skill learning with auto-injection**: Skills are extracted from sessions with strict quality gates, stored in `.omc/skills/` (project-scoped) or `~/.omc/skills/` (user-scoped), and auto-injected into context when their trigger patterns match. Project-scope overrides user-scope, enabling both personal and team-shared patterns.
- **Persistent execution modes**: Ralph mode wraps execution in verify/fix loops until the task is truly complete — addressing the common failure mode where agents declare completion without verifying their output actually works. This is distinct from the default single-pass execution.
- **OpenClaw gateway integration**: OMC can forward Claude Code session events (session-start, stop, keyword-detector, ask-user-question, pre/post-tool-use) to an OpenClaw gateway, enabling automated response workflows and agent-to-agent coordination through webhook-style event dispatch.
- **Deep interview for requirements clarification**: `/deep-interview` uses Socratic questioning to measure clarity across weighted dimensions before any code is written, exposing hidden assumptions. This is OMC's equivalent of GSD's "discuss phase" and Superpowers' "brainstorming" skill.

## Notable Patterns

- **HUD statusline**: Real-time orchestration metrics displayed in the terminal status bar — provides visibility into what multi-agent orchestration is actually doing without requiring manual inspection.
- **`/ccg` tri-model advisor synthesis**: Routes to `/ask codex` + `/ask gemini`, then Claude synthesizes both responses — a structured way to get multi-model perspective on a single problem.
- **Rate limit wait daemon**: `omc wait --start` enables an auto-resume daemon that detects when rate limits reset and automatically continues the session, enabling true unattended long-running workflows.
- **Ralph includes ultrawork**: Activating persistence mode (ralph) automatically includes maximum parallelism (ultrawork) — the combination is the recommended default for tasks that must complete reliably.

## Concepts touched

- [[Claude Code]]
- [[Multi-Agent Orchestration]]
- [[Claude Subagents]]
- [[Claude Skills]]
- [[Claude Hooks]]
- [[Context Engineering]]
- [[Cross-Harness Compatibility]]
- [[Token Optimization]]
- [[Agentic Development]]
- [[Session Persistence]]
