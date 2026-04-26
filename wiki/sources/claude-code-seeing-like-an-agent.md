---
tags:
  - source
  - claude-code
  - agent-design
  - anthropic
updated: 2026-04-26
---

# Lessons from Building Claude Code: Seeing like an Agent

**Source:** [X/@trq212, 2026-02-27](https://x.com/trq212/status/2027463795355095314)
**Author:** [[Thariq Shihipar]] (@trq212) — Anthropic

## Summary

A behind-the-scenes account of how the Claude Code team designs tools for Claude — and how the right approach requires "seeing like an agent": understanding the model's native capabilities and designing the tool surface to match them, not to force a pattern onto the model.

## Core Framework: Tools Shaped to Model Abilities

> "You want to give [the agent] tools that are shaped to its own abilities."

The math problem analogy: paper < calculator < computer. The right tool depends on your skill set. Same for LLMs — the right tool surface depends on *Claude's* actual capabilities, which you discover by paying careful attention to outputs.

## Case Study 1: AskUserQuestion Tool

**Goal:** improve Claude's elicitation (ability to ask structured questions)

| Attempt | Approach | Problem |
|---|---|---|
| #1 | Added question array to `ExitPlanTool` | Claude confused — simultaneous plan + questions conflicted |
| #2 | Modified output format (markdown bullet questions) | Output not reliable; Claude appended extra text, changed formats |
| #3 | Dedicated `AskUserQuestion` tool | ✅ Works: structured output, modal UI, blocks agent loop for response |

The tool worked because Claude *likes calling it* — the best tool design is invisible friction.

Key insight: **composability matters** — the tool can be called from the Agent SDK and referenced from skills.

## Case Study 2: TodoWrite → Task Tool

**Problem evolution:**
1. Early Claude needed `TodoWrite` to stay on track; system reminders every 5 turns helped
2. Improved Claude found reminders *limiting* — made it feel stuck to the original list
3. Opus 4.5 got better at subagents — `TodoWrite` didn't support cross-agent coordination

**Solution:** Replaced `TodoWrite` with the `Task` tool:
- Tasks have **dependencies**
- Tasks **share updates across subagents**
- Tasks can be **altered and deleted** by the model

> "As model capabilities increase, the tools your models once needed might now be constraining them."

## Case Study 3: Search Interface Evolution

| Era | Approach | Limitation |
|---|---|---|
| Launch | RAG vector database | Indexing/setup required; Claude was *given* context passively |
| After Grep tool | Claude searches codebase itself | Claude actively builds its own context |
| Agent Skills | [[Progressive Disclosure]] | Multi-layer nested search; Claude reads files that point to more files |

The progression: Claude went from passive context recipient → active context builder → multi-hop explorer.

## Case Study 4: Claude Code Guide Subagent

**Problem:** Claude didn't know how to answer questions about itself (how to add MCP, what a slash command does)

**Options considered:**
- Add to system prompt → context rot, interferes with coding focus
- Load docs link → Claude over-fetches context

**Solution:** A specialized [[Subagents|subagent]] prompted when you ask Claude about itself, with optimized search instructions for the docs.

Pattern: **Add to action space without adding a tool** via subagent delegation + [[Progressive Disclosure]].

## Core Principle: This Is an Art

There are no rigid rules. Tool design depends on:
- The specific model (capabilities differ)
- The agent's goal
- The operating environment

"Experiment often, read your outputs, try new things. See like an agent."

## Inbound sources
- [[sources/claude-code-seeing-like-an-agent]] ← this page
