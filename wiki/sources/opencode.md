---
title: "OpenCode"
created: 2026-04-26
updated: 2026-04-26
type: summary
tags:
  - agent_systems
  - coding_agent
  - cli_tool
  - oss
  - tui
  - provider_agnostic
source: https://github.com/anomalyco/opencode
---

# OpenCode

An open-source AI coding agent built as a direct, provider-agnostic alternative to Claude Code — emphasizing a client/server architecture, a terminal-first UX philosophy, and out-of-the-box LSP support as the key differentiators from its proprietary counterpart.

## Key design decisions / architecture

**Client/server split as the fundamental architecture.** The most architecturally significant decision in OpenCode is decoupling the agent backend (which does the work) from the frontend client (the TUI). This means OpenCode can run on a remote machine while a user drives it from a mobile app — the TUI is explicitly described as "just one of the possible clients." Claude Code ties the agent to the terminal session; OpenCode's architecture makes remote and headless operation a first-class case.

**Provider agnosticism as a long-term strategic bet.** OpenCode explicitly distances itself from any single LLM provider. It supports Claude, OpenAI, Google, and local models, with `OpenCode Zen` as its own recommended inference offering. The README's rationale is stated directly: "As models evolve, the gaps between them will close and pricing will drop, so being provider-agnostic is important." This is a defensible position — a coding agent that works with the best available model at any time is more durable than one tied to a single provider's roadmap.

**LSP support out of the box.** Language Server Protocol integration is highlighted as a differentiator unavailable in Claude Code. LSP gives the agent structured access to language semantics (go-to-definition, diagnostics, symbol resolution) rather than treating code as plain text. This can improve edit quality for refactoring and cross-file changes without additional model capability.

**TUI as a product focus, not a convenience.** OpenCode is built by neovim users and the creators of `terminal.shop`. The README frames TUI quality as a core commitment: "we are going to push the limits of what's possible in the terminal." This is not about matching Claude Code's terminal UX — it's about exceeding it for users who live in the terminal.

**Two built-in agents with different permission models.** The `build` agent has full access for development work; the `plan` agent is read-only (denies file edits by default, asks permission before bash commands). Switching between them with `Tab` is designed for cognitive mode-switching — "think before you act" is enforced by tool permissions, not user discipline. A `@general` subagent handles complex searches and multistep tasks internally.

**Distribution breadth as adoption strategy.** OpenCode installs via npm/bun/pnpm/yarn, Homebrew, Scoop, Chocolatey, Pacman, AUR, Nix, and `mise`. A desktop app (macOS, Windows, Linux) is in beta. The breadth of distribution channels suggests a deliberate effort to lower the friction of trying it relative to Claude Code, which requires an npm install from a specific source.

## Notable patterns and concepts

- **`build` vs. `plan` agent modes:** Permission-level separation between "full access for coding" and "read-only for exploration" — enforced at the tool layer, not via prompting.
- **`@general` subagent:** An internal delegation target for complex multistep tasks within a session.
- **OpenCode Zen:** The team's own model inference offering, positioned as the recommended backend despite provider agnosticism.
- **Desktop app beta:** A GUI client built alongside the TUI, consistent with the client/server architecture where different frontend surfaces are first-class.
- **Terminal.shop lineage:** The team's prior work on `terminal.shop` (a commerce experience in the terminal) signals genuine TUI craft, not just a thin wrapper.

## Concepts touched

- [[CLI-Agent-Tools]]
- [[Client-Server-Agent-Architecture]]
- [[Language-Server-Protocol-in-Coding-Agents]]
- [[Provider-Agnostic-LLM-Applications]]
- [[Agent-Permission-Models]]
- [[Claude-Code-Ecosystem]]
- [[TUI-Design-for-Developer-Tools]]

## Inbound sources

- `/Users/dan.orlando/Code/my_apps/personal_wiki/raw/Repos/agent_systems/opencode.md`
