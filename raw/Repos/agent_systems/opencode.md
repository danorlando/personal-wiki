---
title: "anomalyco/opencode: The open source coding agent."
source: "https://github.com/anomalyco/opencode"
author:
published:
created: 2026-04-06
description: "The open source coding agent. Contribute to anomalyco/opencode development by creating an account on GitHub."
tags:
  - "coding_tool"
  - "OSS"
  - "repository"
  - "claude_code"
  - "agent_system"
---
[![OpenCode logo](https://github.com/anomalyco/opencode/raw/dev/packages/console/app/src/asset/logo-ornate-light.svg)](https://opencode.ai/)

The open source AI coding agent.

[English](https://github.com/anomalyco/opencode/blob/dev/README.md) | [简体中文](https://github.com/anomalyco/opencode/blob/dev/README.zh.md) | [繁體中文](https://github.com/anomalyco/opencode/blob/dev/README.zht.md) | [한국어](https://github.com/anomalyco/opencode/blob/dev/README.ko.md) | [Deutsch](https://github.com/anomalyco/opencode/blob/dev/README.de.md) | [Español](https://github.com/anomalyco/opencode/blob/dev/README.es.md) | [Français](https://github.com/anomalyco/opencode/blob/dev/README.fr.md) | [Italiano](https://github.com/anomalyco/opencode/blob/dev/README.it.md) | [Dansk](https://github.com/anomalyco/opencode/blob/dev/README.da.md) | [日本語](https://github.com/anomalyco/opencode/blob/dev/README.ja.md) | [Polski](https://github.com/anomalyco/opencode/blob/dev/README.pl.md) | [Русский](https://github.com/anomalyco/opencode/blob/dev/README.ru.md) | [Bosanski](https://github.com/anomalyco/opencode/blob/dev/README.bs.md) | [العربية](https://github.com/anomalyco/opencode/blob/dev/README.ar.md) | [Norsk](https://github.com/anomalyco/opencode/blob/dev/README.no.md) | [Português (Brasil)](https://github.com/anomalyco/opencode/blob/dev/README.br.md) | [ไทย](https://github.com/anomalyco/opencode/blob/dev/README.th.md) | [Türkçe](https://github.com/anomalyco/opencode/blob/dev/README.tr.md) | [Українська](https://github.com/anomalyco/opencode/blob/dev/README.uk.md) | [বাংলা](https://github.com/anomalyco/opencode/blob/dev/README.bn.md) | [Ελληνικά](https://github.com/anomalyco/opencode/blob/dev/README.gr.md) | [Tiếng Việt](https://github.com/anomalyco/opencode/blob/dev/README.vi.md)

[![OpenCode Terminal UI](https://github.com/anomalyco/opencode/raw/dev/packages/web/src/assets/lander/screenshot.png)](https://opencode.ai/)

---

### Installation

```
# YOLO
curl -fsSL https://opencode.ai/install | bash

# Package managers
npm i -g opencode-ai@latest        # or bun/pnpm/yarn
scoop install opencode             # Windows
choco install opencode             # Windows
brew install anomalyco/tap/opencode # macOS and Linux (recommended, always up to date)
brew install opencode              # macOS and Linux (official brew formula, updated less)
sudo pacman -S opencode            # Arch Linux (Stable)
paru -S opencode-bin               # Arch Linux (Latest from AUR)
mise use -g opencode               # Any OS
nix run nixpkgs#opencode           # or github:anomalyco/opencode for latest dev branch
```

> [!tip] Tip
> Remove versions older than 0.1.x before installing.

### Desktop App (BETA)

OpenCode is also available as a desktop application. Download directly from the [releases page](https://github.com/anomalyco/opencode/releases) or [opencode.ai/download](https://opencode.ai/download).

| Platform | Download |
| --- | --- |
| macOS (Apple Silicon) | `opencode-desktop-darwin-aarch64.dmg` |
| macOS (Intel) | `opencode-desktop-darwin-x64.dmg` |
| Windows | `opencode-desktop-windows-x64.exe` |
| Linux | `.deb`, `.rpm`, or AppImage |

```
# macOS (Homebrew)
brew install --cask opencode-desktop
# Windows (Scoop)
scoop bucket add extras; scoop install extras/opencode-desktop
```

#### Installation Directory

The install script respects the following priority order for the installation path:

1. `$OPENCODE_INSTALL_DIR` - Custom installation directory
2. `$XDG_BIN_DIR` - XDG Base Directory Specification compliant path
3. `$HOME/bin` - Standard user binary directory (if it exists or can be created)
4. `$HOME/.opencode/bin` - Default fallback
```
# Examples
OPENCODE_INSTALL_DIR=/usr/local/bin curl -fsSL https://opencode.ai/install | bash
XDG_BIN_DIR=$HOME/.local/bin curl -fsSL https://opencode.ai/install | bash
```

### Agents

OpenCode includes two built-in agents you can switch between with the `Tab` key.

- **build** - Default, full-access agent for development work
- **plan** - Read-only agent for analysis and code exploration
	- Denies file edits by default
		- Asks permission before running bash commands
		- Ideal for exploring unfamiliar codebases or planning changes

Also included is a **general** subagent for complex searches and multistep tasks. This is used internally and can be invoked using `@general` in messages.

Learn more about [agents](https://opencode.ai/docs/agents).

### Documentation

For more info on how to configure OpenCode, [**head over to our docs**](https://opencode.ai/docs).

### Contributing

If you're interested in contributing to OpenCode, please read our [contributing docs](https://github.com/anomalyco/opencode/blob/dev/CONTRIBUTING.md) before submitting a pull request.

### Building on OpenCode

If you are working on a project that's related to OpenCode and is using "opencode" as part of its name, for example "opencode-dashboard" or "opencode-mobile", please add a note to your README to clarify that it is not built by the OpenCode team and is not affiliated with us in any way.

### FAQ

#### How is this different from Claude Code?

It's very similar to Claude Code in terms of capability. Here are the key differences:

- 100% open source
- Not coupled to any provider. Although we recommend the models we provide through [OpenCode Zen](https://opencode.ai/zen), OpenCode can be used with Claude, OpenAI, Google, or even local models. As models evolve, the gaps between them will close and pricing will drop, so being provider-agnostic is important.
- Out-of-the-box LSP support
- A focus on TUI. OpenCode is built by neovim users and the creators of [terminal.shop](https://terminal.shop/); we are going to push the limits of what's possible in the terminal.
- A client/server architecture. This, for example, can allow OpenCode to run on your computer while you drive it remotely from a mobile app, meaning that the TUI frontend is just one of the possible clients.

---

**Join our community** [Discord](https://discord.gg/opencode) | [X.com](https://x.com/opencode)