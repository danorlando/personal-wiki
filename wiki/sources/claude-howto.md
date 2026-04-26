---
tags:
  - claude_code
  - learning_guide
  - agent_dev
  - OSS
updated: 2026-04-26
source: https://github.com/luongnv89/claude-howto
---

# claude-howto

A community-built, structured learning guide for Claude Code that provides visual tutorials, production-ready copy-paste templates, and a progressive 10-module curriculum for going from beginner to power user.

## Key Design Decisions / Architecture

- **Problem framing**: Official docs describe features in isolation; this guide's core insight is that Claude Code's power comes from *combining* features (slash commands + memory + hooks + subagents) into workflows. The guide is organized around that combination, not individual features.
- **Progressive learning path with self-assessment**: Rather than a flat reference, the curriculum is sequenced so each module builds on the last, with `/lesson-quiz` and `/self-assessment` slash commands that let learners identify gaps and get a personalized roadmap — the guide is itself delivered through Claude Code.
- **Feature taxonomy**: The guide draws a sharp distinction between invocation mechanisms: manual (`/cmd` slash commands), auto-loaded (memory/CLAUDE.md), event-triggered (hooks), auto-delegated (subagents), and auto-queried (MCP). This framing makes it clear when to reach for each mechanism.
- **Checkpoints as safety net**: The guide gives first-class treatment to the checkpoint/rewind system as a "safe experimentation" primitive, not just an error-recovery tool — encouraging users to explore multiple implementation approaches from a single state.
- **Hook taxonomy**: Documents 4 hook categories covering 25 distinct events (Tool, Session, Task, and Lifecycle hooks), which is significantly more granular than most community documentation.

## Notable Patterns

- **Feature comparison table**: Explicit table mapping each feature to its invocation style, persistence scope, and best use case — a useful reference for choosing the right tool.
- **Workflow composition examples**: Concrete multi-feature pipeline examples (code review = slash command + subagents + memory + MCP; DevOps deploy = plugins + MCP + hooks) that show the "what can you build" answer concretely.
- **EPUB generation**: The guide can be compiled to an offline ebook via `uv run scripts/build_epub.py` — treating documentation as a distributable artifact.

## Concepts touched

- [[Claude Code]]
- [[Claude Hooks]]
- [[Claude Subagents]]
- [[Claude Memory (CLAUDE.md)]]
- [[MCP (Model Context Protocol)]]
- [[Claude Plugins]]
- [[Claude Skills]]
- [[Agentic Development]]
