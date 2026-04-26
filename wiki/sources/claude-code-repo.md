---
tags:
  - claude_code
  - agent_system
  - anthropic
  - OSS
updated: 2026-04-26
source: https://github.com/anthropics/claude-code
---

# Claude Code (Official Repo)

The official Anthropic repository for Claude Code — an agentic coding tool that operates in the terminal, understands codebases, and handles routine coding tasks, explanations, and git workflows through natural language commands.

## Key Design Decisions / Architecture

- **Terminal-native agent**: Claude Code is designed to live in the developer's terminal rather than as an IDE plugin, treating the shell as a first-class interface.
- **Multi-surface availability**: Can be used from the terminal, IDEs, and GitHub (via `@claude` mentions), with a single install covering all contexts.
- **Installation migration**: npm-based install is explicitly deprecated in favor of native OS installers (curl script on Unix, PowerShell on Windows, Homebrew cask). This signals a shift away from treating it as a Node package toward a proper system application.
- **Plugin extensibility**: The repo ships a plugins directory that allows extending Claude Code with custom commands and agents, establishing a composable architecture on top of the base tool.
- **Privacy-first data policy**: Usage feedback is collected but with explicit safeguards — limited retention, restricted session data access, and a stated policy against using feedback for model training.

## Notable Patterns

- The `@claude` GitHub integration extends agentic operation into async, event-driven contexts outside the interactive terminal.
- The transition from npm to OS-native installers mirrors how developer tools graduate from prototype to product (similar to how Homebrew is used for stable CLI tools).

## Concepts touched

- [[Claude Code]]
- [[AI Coding Agents]]
- [[Agentic Development]]
- [[MCP (Model Context Protocol)]]
- [[Claude Plugins]]
