---
tags:
  - entity
  - tool
  - anthropic
  - developer-tools
updated: 2026-04-26
---

# Claude Code

Anthropic's AI-powered coding CLI and agentic development environment. Claude Code provides an interactive agent loop with file editing, bash execution, web search, and an extensible tool surface. It runs in the terminal, as a desktop app, a web app (claude.ai/code), and via IDE extensions.

## Architecture

Claude Code's action space is built around Tool Calling in the Claude API. Key design principles (from [[Thariq Shihipar]]'s writings):

- **Tools should be shaped to model abilities**, not force patterns onto the model
- **[[Progressive Disclosure]]** over front-loading all context
- **[[Agent Skills]]** as the primary extensibility mechanism
- As models improve, previously useful tools can become constraints

## Key Features

### Context & Memory
- `CLAUDE.md` — project-level instructions Claude writes and reads
- `.claude/rules/` — modular topic-specific rule files with optional path-scoped frontmatter
- `@mention` — instant context injection for files, directories, MCP servers
- `/context` — token consumption breakdown

### Session Management
- `--continue` / `--resume` — persist and restore sessions (up to `cleanupPeriodDays`, default 30)
- `/rename` — named sessions
- `--teleport` — pull web/mobile sessions to local terminal
- `/export` — conversation to markdown

### Thinking & Planning
- `ultrathink` keyword — up to 32k internal reasoning tokens
- **[[Plan Mode]]** (`Shift+Tab ×2`) — read/analyze/plan without editing; requires approval
- Extended thinking (API) — configurable via `budget_tokens`

### Extensibility
- **[[Agent Skills]]** — packaged folders of instructions + scripts + assets
- **Hooks** — shell commands at lifecycle events (`PreToolUse`, `PostToolUse`, `PermissionRequest`, etc.)
- **Plugins** — bundle commands/agents/skills/hooks/MCPs into one installable unit
- **[[Claude Agent SDK]]** — same loop/tools/context as Claude Code, usable programmatically
- **[[LSP Integration]]** — IDE-level diagnostics, references, hover info in real time
- **MCP servers** — Model Context Protocol for external tool integrations

### Permissions & Safety
- `/sandbox` — define permission boundaries with wildcard syntax
- `--dangerously-skip-permissions` — YOLO mode for isolated environments
- Hooks as deterministic guardrails over probabilistic AI

### Automation
- `-p "prompt"` — headless mode for CI/CD pipelines
- Slash commands from markdown files: any `.md` → `/command $ARGUMENTS`

## Tool Evolution (per internal Anthropic experience)

| Tool | Replaced by | Reason |
|---|---|---|
| RAG vector DB | Grep tool | Claude can build its own context; active > passive |
| `TodoWrite` | Task tool | Tasks support subagent coordination and dependencies |
| Inline docs in system prompt | [[Claude Code]] Guide subagent | Avoids context rot; [[Progressive Disclosure]] |
| ExitPlanTool question param | `AskUserQuestion` tool | Dedicated tool works better; Claude likes calling it |

## Inbound sources
- [[sources/advent-of-claude-31-days]]
- [[sources/claude-code-how-we-use-skills]]
- [[sources/claude-code-seeing-like-an-agent]]
- [[sources/claude-code-repo]]
- [[sources/claude-howto]]
- [[sources/claude-mem]]
- [[sources/everything-claude-code]]
- [[sources/get-shit-done]]
- [[sources/gstack]]
- [[sources/obra-superpowers]]
- [[sources/oh-my-claudecode]]
- [[sources/personal-ai-infrastructure]]
- [[sources/claw-code]]
- [[sources/opencode]]
- [[sources/awesome-design-md]]
- [[sources/last30days-skill]]
