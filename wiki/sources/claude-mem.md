---
title: "claude-mem"
created: 2026-04-26
updated: 2026-04-26
type: summary
tags:
  - claude_code
  - memory
  - persistence
  - agent_infrastructure
source: https://github.com/thedotmack/claude-mem
---

# claude-mem

A Claude Code plugin that automatically captures tool usage observations during coding sessions, compresses them with AI, and injects relevant context back into future sessions — solving the problem of Claude losing knowledge about a project when a session ends.

## Key Design Decisions / Architecture

- **Automatic capture via lifecycle hooks**: claude-mem hooks into 5 Claude Code lifecycle events (SessionStart, UserPromptSubmit, PostToolUse, Stop, SessionEnd) to capture observations without any user intervention. The core insight is that the rich event stream Claude Code already emits is sufficient raw material for building persistent memory.
- **Progressive disclosure retrieval**: The MCP search interface enforces a 3-layer workflow — first get a compact index (50-100 tokens/result), then get timeline context around interesting results, then fetch full details for filtered IDs only. This achieves ~10x token savings versus naive "fetch everything" retrieval.
- **Hybrid search architecture**: Combines SQLite with FTS5 for keyword search and a Chroma vector database for semantic search — using both to handle queries that need either exact term matching or semantic similarity.
- **Worker service + web viewer**: A persistent HTTP worker (managed by Bun, port 37777) handles all database operations and exposes a web UI for real-time memory streaming, plus 10 search endpoints. This keeps heavy work off Claude's context thread.
- **Privacy controls**: Users can wrap content in `<private>` tags to exclude it from storage, addressing the concern that an automatically-capturing memory system could store sensitive information.
- **Endless Mode (beta)**: A "biomimetic memory architecture" for extended sessions — signals ongoing architectural experimentation beyond simple append-and-summarize.

## Notable Patterns

- **Install-time hook registration**: `npx claude-mem install` handles hook registration and worker service setup as a single command. The npm package alone (without the installer) only installs the SDK/library, not the live system — an important distinction for correct setup.
- **Citation system**: Each observation gets an ID that can be referenced via the web viewer API, creating a traceable audit trail of past Claude actions.
- **3-layer search pattern**: `search → timeline → get_observations` is a reusable retrieval pattern applicable beyond this tool — filter before fetching to avoid token waste.

## Concepts touched

- [[Claude Code]]
- [[Claude Memory (CLAUDE.md)]]
- [[Claude Hooks]]
- [[Context Engineering]]
- [[MCP (Model Context Protocol)]]
- [[Agentic Development]]
- [[Session Persistence]]
- [[Progressive Disclosure]]
