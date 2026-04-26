---
title: "ultraworkers/claw-code: The repo is finally unlocked. enjoy the party! The fastest repo in history to surpass 100K stars ⭐. Join Discord: https://discord.gg/5TUQKqFWd Built in Rust using oh-my-codex."
source: "https://github.com/ultraworkers/claw-code"
author:
published:
created: 2026-04-08
description: "The repo is finally unlocked. enjoy the party! The fastest repo in history to surpass 100K stars ⭐. Join Discord: https://discord.gg/5TUQKqFWd Built in Rust using oh-my-codex. - ultraworkers/claw-code"
tags:
  - "developer tool"
  - "repository"
  - "agent system"
  - "agent harness"
---
## Claw Code

[ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) · [Usage](https://github.com/ultraworkers/claw-code/blob/main/USAGE.md) · [Rust workspace](https://github.com/ultraworkers/claw-code/blob/main/rust/README.md) · [Parity](https://github.com/ultraworkers/claw-code/blob/main/PARITY.md) · [Roadmap](https://github.com/ultraworkers/claw-code/blob/main/ROADMAP.md) · [UltraWorkers Discord](https://discord.gg/5TUQKqFWd)

[![Star history for ultraworkers/claw-code](https://camo.githubusercontent.com/33e7f5e2ecd8d13a9af64fd984b301e8070da1c8cc85c5f781ce9c9013f41bc5/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d756c747261776f726b6572732f636c61772d636f646526747970653d44617465)](https://star-history.com/#ultraworkers/claw-code&Date)

[![Claw Code](https://github.com/ultraworkers/claw-code/raw/main/assets/claw-hero.jpeg)](https://github.com/ultraworkers/claw-code/blob/main/assets/claw-hero.jpeg)

Claw Code is the public Rust implementation of the `claw` CLI agent harness. The canonical implementation lives in [`rust/`](https://github.com/ultraworkers/claw-code/blob/main/rust), and the current source of truth for this repository is **ultraworkers/claw-code**.

> [!important] Important
> Start with [`USAGE.md`](https://github.com/ultraworkers/claw-code/blob/main/USAGE.md) for build, auth, CLI, session, and parity-harness workflows. Make `claw doctor` your first health check after building, use [`rust/README.md`](https://github.com/ultraworkers/claw-code/blob/main/rust/README.md) for crate-level details, read [`PARITY.md`](https://github.com/ultraworkers/claw-code/blob/main/PARITY.md) for the current Rust-port checkpoint, and see [`docs/container.md`](https://github.com/ultraworkers/claw-code/blob/main/docs/container.md) for the container-first workflow.

## Current repository shape

- **`rust/`** — canonical Rust workspace and the `claw` CLI binary
- **`USAGE.md`** — task-oriented usage guide for the current product surface
- **`PARITY.md`** — Rust-port parity status and migration notes
- **`ROADMAP.md`** — active roadmap and cleanup backlog
- **`PHILOSOPHY.md`** — project intent and system-design framing
- **`src/` + `tests/`** — companion Python/reference workspace and audit helpers; not the primary runtime surface

## Quick start

```
cd rust
cargo build --workspace
./target/debug/claw --help
./target/debug/claw prompt "summarize this repository"
```

Authenticate with either an API key or the built-in OAuth flow:

```
export ANTHROPIC_API_KEY="sk-ant-..."
# or
cd rust
./target/debug/claw login
```

Run the workspace test suite:

```
cd rust
cargo test --workspace
```

## Documentation map

- [`USAGE.md`](https://github.com/ultraworkers/claw-code/blob/main/USAGE.md) — quick commands, auth, sessions, config, parity harness
- [`rust/README.md`](https://github.com/ultraworkers/claw-code/blob/main/rust/README.md) — crate map, CLI surface, features, workspace layout
- [`PARITY.md`](https://github.com/ultraworkers/claw-code/blob/main/PARITY.md) — parity status for the Rust port
- [`rust/MOCK_PARITY_HARNESS.md`](https://github.com/ultraworkers/claw-code/blob/main/rust/MOCK_PARITY_HARNESS.md) — deterministic mock-service harness details
- [`ROADMAP.md`](https://github.com/ultraworkers/claw-code/blob/main/ROADMAP.md) — active roadmap and open cleanup work
- [`PHILOSOPHY.md`](https://github.com/ultraworkers/claw-code/blob/main/PHILOSOPHY.md) — why the project exists and how it is operated

## Ecosystem

Claw Code is built in the open alongside the broader UltraWorkers toolchain:

- [clawhip](https://github.com/Yeachan-Heo/clawhip)
- [oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)
- [oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)
- [oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex)
- [UltraWorkers Discord](https://discord.gg/5TUQKqFWd)

## Ownership / affiliation disclaimer

- This repository does **not** claim ownership of the original Claude Code source material.
- This repository is **not affiliated with, endorsed by, or maintained by Anthropic**.