---
title: "obra/superpowers"
created: 2026-04-26
updated: 2026-04-26
type: summary
tags:
  - claude_code
  - claude_plugins
  - workflow_system
  - TDD
  - subagent_development
source: https://github.com/obra/superpowers
---

# obra/superpowers

A complete software development workflow for AI coding agents, built on composable "skills" and CLAUDE.md instructions, centered on spec-first development, true red/green TDD, and subagent-driven implementation with two-stage code review at each task.

## Key Design Decisions / Architecture

- **Skills as mandatory workflows, not suggestions**: The core design decision is that the agent checks for relevant skills before any task and the skills trigger automatically. The system actively prevents the agent from jumping straight into code — it forces a brainstorming/spec phase first. This is enforced through instruction design rather than external tooling.
- **Spec-first, chunked validation**: The brainstorming skill teases out a spec through Socratic conversation, then presents it "in chunks short enough to actually read and digest" — an explicit acknowledgment that LLMs produce specs humans don't actually review when shown all at once. Chunked validation is the UX design for spec approval.
- **Subagent-driven development with two-stage review**: Each task is dispatched to a fresh subagent, and every subagent's work is reviewed twice — first for spec compliance (did it do what was asked?) and then for code quality (is it good code?). This separates correctness from quality concerns and prevents the common failure where spec drift isn't caught until integration.
- **Implementation plans calibrated for "poor taste, no judgement"**: Plans are written explicitly to be followable by "an enthusiastic junior engineer with poor taste, no judgement, no project context, and an aversion to testing." This framing pushes plan authors to make every step unambiguous and include test criteria — because the agent executing it will take shortcuts if given the chance.
- **True RED-GREEN-REFACTOR TDD**: The TDD skill enforces watching the test fail (RED) before writing implementation code, and watching it pass (GREEN) before refactoring. The skill explicitly deletes code written before tests, enforcing the discipline mechanically rather than aspirationally.
- **Git worktrees for isolation**: Each feature starts in an isolated workspace on a new branch, with the project setup verified and a clean test baseline confirmed before any implementation begins. This makes parallel development safe.
- **Available in official Claude plugin marketplace**: Superpowers is listed at `claude.com/plugins/superpowers` — a signal that this workflow is considered production-ready and broadly applicable.

## Notable Patterns

- **Writing-skills skill**: The repo includes a meta-skill for creating new skills, with a testing methodology — the system is designed to be extended and teaches contributors how to extend it correctly.
- **`finishing-a-development-branch` as explicit decision point**: When implementation is complete, the agent presents options (merge to main, open PR, keep branch, discard) rather than automatically merging. This preserves human decision-making at integration boundaries.
- **Systematic debugging with evidence requirement**: The debugging skill follows a 4-phase root cause process and requires evidence before proposing fixes — "no fixes without investigation" is the Iron Law.

## Concepts touched

- [[Claude Code]]
- [[Claude Plugins]]
- [[Claude Skills]]
- [[Claude Subagents]]
- [[Test-Driven Development]]
- [[Spec-Driven Development]]
- [[Agentic Development]]
- [[Multi-Agent Orchestration]]
- [[Git Worktrees]]
