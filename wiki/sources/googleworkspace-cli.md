---
tags: [cli, google-workspace, rust, discovery-api, agent-tools, mcp]
updated: 2026-04-26
---

# googleworkspace/cli (`gws`)

One-line summary: A Rust CLI for all Google Workspace APIs whose command surface is generated at runtime from Google's Discovery Service — never out of date, never manually maintained.

## Problem it solves

Every Google Workspace API (Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin) has its own SDK, its own auth flow, and its own CLI wrapper — or no CLI at all. Scripting across APIs means juggling libraries. AI agents that need to call Workspace APIs get no structured interface; they're left to raw HTTP or brittle shell invocations. `gws` gives agents and scripts a single, uniform, always-current CLI entry point across all Workspace surfaces.

## Core architectural insight

The defining design decision is **discovery-driven command construction**. Most CLIs are compiled with a fixed command tree. `gws` does this in two phases at runtime:

1. `argv[1]` identifies the service (e.g. `drive`, `gmail`)
2. `gws` fetches the corresponding Google Discovery Document (JSON API description), caches it for 24 hours, then builds the full `clap::Command` tree from it
3. Remaining args are re-parsed against that dynamically built tree

This means when Google adds a new API endpoint, `gws` exposes it automatically — zero code changes, zero release required. The tradeoff is that Google API changes can silently break behavior, and users depend on Google's own Discovery Service being correct. This is the inverse of the usual CLI engineering tradeoff: maximum currency at the cost of stability guarantees.

A second structural decision is the **`+` prefix for hand-crafted helper commands** (e.g., `+agenda`, `+standup-report`). Auto-generated Discovery commands handle the raw API surface; `+` commands encode higher-level workflows that compose multiple API calls. This separates "generated" from "curated" at the command-name level without collision risk.

## Key capabilities

- Covers all major Workspace APIs from a single binary
- 100+ bundled [[Agent-Skills]], one per major API plus workflow helpers
- Structured JSON output throughout; exit codes are enumerated and documented (0 = success, 1 = API error, 2 = auth error, 3 = validation, 4 = discovery, 5 = internal), making it suitable for programmatic consumption
- Auth: AES-256-GCM encrypted credentials stored in OS keyring; supports interactive OAuth, service accounts, token files, and a CI/headless export flow
- **Model Armor integration**: can scan API responses for prompt injection before they reach an agent — relevant when a Drive document or email is used as agent input
- Installable via npm, Homebrew, Nix, or pre-built binaries

## Tradeoffs and limitations

- **Not an officially supported Google product** — no SLA, may break with API changes
- Discovery-driven parsing adds cold-start latency on first use per service (mitigated by 24h cache)
- Dynamic command construction means tab-completion and man pages can't be fully pre-generated
- The generated surface reflects Google's API shape, which is often verbose and non-ergonomic; the `+` commands fill in ergonomics but don't cover every workflow

## Relation to other work

The discovery-driven approach is thematically similar to [[CLI-Anything]]'s goal of giving agents a stable CLI interface to software — but where CLI-Anything generates harnesses from codebases, `gws` generates them from API schemas. Both treat the CLI as the universal agent interface. The Model Armor integration connects to agent security concerns explored in [[sources/claude-skills-alirezarezvani]] (skill-security-auditor).

## Inbound sources

- [[sources/googleworkspace-cli]] ← this page
