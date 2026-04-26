---
tags:
  - claude_code
  - agent_harness
  - performance_optimization
  - OSS
  - hackathon_winner
updated: 2026-04-26
source: https://github.com/affaan-m/everything-claude-code
---

# everything-claude-code (ECC)

An Anthropic hackathon-winning "agent harness performance optimization system" for Claude Code — not a config pack but a complete production system of skills, instincts, memory persistence, security scanning, and cross-harness compatibility evolved from 10+ months of daily use. Currently ships 47 agents, 181 skills, and 79 legacy command shims.

## Key Design Decisions / Architecture

- **Harness-first framing**: ECC explicitly positions itself as a performance system for the *agent harness* itself, not just useful prompts. The goal is to make Claude Code reliably perform across sessions, not to add features. This includes deterministic eval scoring, observer loop prevention, and 5-layer re-entrancy guards.
- **Skills over commands**: The architectural direction is to move workflow definitions from `commands/` (slash-command shims) to `skills/` (richer, auto-invocable workflow definitions with YAML frontmatter). Legacy commands are kept for backwards compatibility but new development lands in skills first.
- **Selective install with manifest-driven pipeline**: `install-plan.js` + `install-apply.js` allow targeted component installation rather than all-or-nothing. A SQLite state store tracks what's installed to enable incremental updates.
- **Cross-harness DRY adapter pattern**: A `.cursor/hooks/adapter.js` transforms Cursor's stdin JSON to Claude Code's hook format, letting the same `scripts/hooks/*.js` implementations serve both Claude Code and Cursor without duplication. The same skills format (SKILL.md with YAML frontmatter) works across Claude Code, Codex, and OpenCode.
- **Instinct-based continuous learning**: Beyond static skills, ECC v2 implements an "instinct" system that extracts patterns from sessions with confidence scoring, allows import/export for sharing, and can cluster related instincts into skills via `/evolve`. Sessions automatically teach the system.
- **AgentShield security scanning**: A red-team/blue-team/auditor pipeline (three Opus agents) performs adversarial security analysis of Claude Code configurations, covering 5 categories with 102 static analysis rules. The `--opus` flag switches from pattern matching to adversarial reasoning.
- **Token management as first-class concern**: Explicit guidance to set `model: sonnet`, cap `MAX_THINKING_TOKENS` at 10k (vs default 31,999), and compact at 50% context rather than 95%. Also warns that each MCP tool description consumes tokens — keep under 10 MCPs and 80 tools active.
- **Hook auto-loading convention**: Claude Code v2.1+ auto-loads `hooks/hooks.json` from installed plugins by convention. Explicitly declaring it in `plugin.json` causes duplicate detection errors — a lesson the project learned through repeated fix/revert cycles.

## Notable Patterns

- **Context injection via `contexts/` directory**: Different modes (dev, review, research) have dedicated system prompt injection contexts, enabling mode-switching without editing CLAUDE.md.
- **`AGENTS.md` as universal cross-tool file**: Read natively by Claude Code, Cursor, Codex, and OpenCode — the single file that makes a repo work across all major AI coding tools.
- **Strategic compaction**: A `strategic-compact` skill suggests `/compact` at logical breakpoints (after research, after milestones) rather than auto-compacting at 95% context, trading some context for higher quality in long sessions.
- **Agent Teams cost warning**: Agent Teams (spawning multiple context windows) is expensive because each teammate's context is independent. Only use when parallelism provides clear value.

## Concepts touched

- [[Claude Code]]
- [[Claude Skills]]
- [[Claude Subagents]]
- [[Claude Hooks]]
- [[Agent Security]]
- [[Context Engineering]]
- [[Token Optimization]]
- [[Continuous Learning]]
- [[Cross-Harness Compatibility]]
- [[MCP (Model Context Protocol)]]
- [[Agentic Development]]
