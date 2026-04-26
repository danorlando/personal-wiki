---
tags:
  - concept
  - claude-code
  - agent-design
updated: 2026-04-26
---

# Progressive Disclosure

A design pattern for managing context in AI agents: instead of providing all context upfront, structure information so the agent **incrementally discovers relevant context through exploration**.

## Origin in Claude Code

Originally formalized when [[Agent Skills]] were introduced. Claude reads a skill's root file, which references other files, which Claude fetches on demand. This enables nested, multi-hop search without bloating the initial context.

> "Over the course of a year Claude went from not really being able to build its own context, to being able to do nested search across several layers of files to find the exact context it needed." — [[Thariq Shihipar]]

## Mechanism

```
Claude reads SKILL.md
    → "See references/api.md for full function signatures"
    → Claude fetches references/api.md when relevant
    → "See examples/auth-flow.md for edge cases"
    → Claude fetches only when needed
```

Contrast with front-loading: putting everything in the system prompt causes **context rot** and interferes with the agent's primary task.

## Applications

| Context | Use of Progressive Disclosure |
|---|---|
| Agent Skills | Filesystem references inside skill folders |
| Claude Code Guide subagent | Subagent with optimized doc search, called only when asked about Claude Code itself |
| Codebase search | Grep tool lets Claude build its own context rather than receiving RAG results passively |

## Key Insight: Active vs. Passive Context

Early Claude Code used RAG: context was *given* to Claude. Progressive disclosure flips this — Claude *seeks* the context it needs. As models improve, active context-building outperforms passive delivery because the model can refine and iterate on its search.

## Inbound sources
- [[sources/claude-code-seeing-like-an-agent]]
- [[sources/claude-code-how-we-use-skills]]
