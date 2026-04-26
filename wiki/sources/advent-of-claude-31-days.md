---
tags:
  - source
  - claude-code
  - tools
  - developer-experience
updated: 2026-04-26
---

# Advent of Claude: 31 Days of Claude Code

**Source:** [adocomplete.com, 2025-12-31](https://adocomplete.com/advent-of-claude-2025/)
**Author:** adocomplete (@adocomplete on X)

## Summary

A compiled guide of 31 Claude Code tips organized from beginner essentials to advanced patterns. Covers keyboard shortcuts, session management, productivity features, permissions, CI/CD automation, and the emerging ecosystem of agents, skills, and plugins.

## Feature Reference

### Getting Started
| Feature | How |
|---|---|
| Project onboarding | `/init` — Claude reads codebase, writes `CLAUDE.md` |
| Modular rules | `.claude/rules/*.md` with optional YAML `paths:` frontmatter |
| Memory updates | Tell Claude: "Update Claude.md: always use bun" |
| Context injection | `@file`, `@directory`, `@mcp:server` mentions |

### Essential Shortcuts
| Shortcut | Effect |
|---|---|
| `!command` | Execute bash instantly, inject output to context |
| `Esc Esc` | Rewind conversation and/or code changes |
| `Ctrl+R` | Reverse history search |
| `Ctrl+S` | Stash draft prompt |
| `Shift+Tab ×2` | Toggle [[Plan Mode]] |
| `Tab` / `Enter` | Accept prompt suggestion |

### Session Management
| Command | Effect |
|---|---|
| `claude --continue` | Resume last session |
| `claude --resume` | Pick any past session |
| `/rename <name>` | Name current session |
| `claude --teleport <id>` | Pull web session to terminal |
| `/export` | Dump full conversation to markdown |

### Productivity
- `/vim` — full vim-mode prompt editing
- `/statusline` — configurable status bar (branch, model, tokens, context %)
- `/context` — breakdown of token consumption
- `/stats` — usage dashboard and streaks
- `/usage` / `/extra-usage` — rate limit visibility and top-up

### Thinking & Planning
- **`ultrathink` keyword** — triggers up to 32k internal reasoning tokens (overridden by `MAX_THINKING_TOKENS` if set)
- **[[Plan Mode]]** (`Shift+Tab ×2`) — read/analyze/plan without editing; approve before executing
- **Extended thinking (API)** — `thinking: { type: "enabled", budget_tokens: N }`

### Permissions & Safety
- `/sandbox` — define boundaries once; wildcard syntax (`mcp__server__*`)
- `--dangerously-skip-permissions` — YOLO mode (use in isolated environments)
- **[[Claude Code Hooks]]** — `PreToolUse`, `PostToolUse`, `PermissionRequest`, `Notification`, `SubagentStart/Stop`

### Automation & CI/CD
- `-p "prompt"` — headless/print mode for scripting and pipelines
- Slash commands — any `.md` file becomes a reusable `/command $ARGUMENTS`

### Browser Integration
- Chrome extension ([claude.ai/chrome](https://claude.ai/chrome)) — navigate, click, read console errors, inspect DOM, screenshot

### Advanced: Agents & Extensibility
- **[[Subagents]]** — each gets 200k context, runs in parallel, merges back
- **[[Agent Skills]]** — packaged instructions+assets, open standard, reusable across tools
- **Plugins** — bundle commands/agents/skills/hooks/MCPs into one installable unit (`/plugin install`)
- **[[LSP Integration]]** — IDE-level diagnostics, go-to-definition, hover info in real time
- **[[Claude Agent SDK]]** — same loop/tools/context as Claude Code, usable in ≥10 lines of TypeScript

## Key Quotes
> "The developers who get the most out of Claude Code aren't the ones who type 'do everything for me.' They're the ones who've learned when to use Plan mode, how to structure their prompts, when to invoke ultrathink, and how to set up hooks that catch mistakes before they happen."

## Inbound sources
- [[sources/advent-of-claude-31-days]] ← this page
