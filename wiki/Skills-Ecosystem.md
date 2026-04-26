---
tags:
  - concept
  - skills
  - ecosystem
  - extensibility
updated: 2026-04-26
---

# Skills Ecosystem

The emerging ecosystem of skill libraries, marketplaces, and standards for agent extensibility. As [[Agent Skills]] become a stable interface format, the ecosystem around them — who publishes skills, how they're distributed, how they're secured — is beginning to take shape.

## The Open Standard

[[Agent Skills]] are platform-agnostic. The same skill folder format works across Claude Code, OpenAI Codex CLI, Gemini CLI, Cursor, and other agent runtimes that have adopted or are adopting the convention. This matters because it means a skill built for one runtime is in principle portable to others — the format is the standard, not the vendor.

The practical implication: skill authors aren't writing for a single platform. Community investment in a skill library compounds across the ecosystem rather than being locked to one vendor's user base.

## Key Players

### alirezarezvani/claude-skills — 248 skills across 9 domains

The largest community library currently tracked. Notable for:

- **Taxonomy beyond skills**: distinguishes Skills (task instructions), Agents (autonomous multi-step), and Personas (behavioral modes). Skills tell the agent how to do a task; Agents tell it how to orchestrate a workflow; Personas shift its baseline behavior.
- **skill-security-auditor** — a meta-skill that scans other skills for security risks (see Security section below). This is a significant contribution: security tooling for the skills ecosystem itself.
- **multi-tool convert script** — batch-converts skills between formats, enabling migration across runtimes

### addyosmani/agent-skills — 19 engineering skills with lifecycle mapping

Smaller but opinionated. Notable for:

- **Lifecycle mapping**: skills are explicitly tagged to phases of software delivery (Define → Design → Build → Test → Ship). This makes it possible to compose a workflow by assembling phase-appropriate skills rather than picking skills by name.
- **Anti-rationalization tables**: for each skill, documents failure modes where an agent might claim success without actually validating. The verification-first philosophy is baked into the skill format, not left to the user to enforce.
- **Verification-first**: skills include explicit verification steps that must pass before the skill declares completion. This directly addresses the problem of agents that produce plausible-looking output without checking it.

### googleworkspace-cli — 100+ bundled skills

The googleworkspace-cli (see [[Agent-Native-Software]]) ships with a skill library bundled alongside the CLI itself — one skill per major API surface plus workflow helpers that compose across APIs. This is a distribution model: the skills and the tool they operate come as a unit, so installation is a single step.

### graphify — installs as a skill, always-on via hook

Graphify takes a different approach to distribution: it installs itself not just as a callable skill but as a **PreToolUse hook** on Glob and Grep operations. This makes it always-on — every time the agent would search the codebase, the hook surfaces `GRAPH_REPORT.md` first. See [[Knowledge-Graph-for-Agents]] for the mechanics.

The hook pattern is architecturally significant: it's the difference between a skill the agent chooses to invoke and a skill that's always in the loop. PreToolUse hooks are a form of mandatory middleware.

### OpenSpace — cloud community for skill sharing

OpenSpace adds a cloud layer: [[Self-Evolving-Skills]] that an agent has evolved locally can be uploaded to a shared community repository, where other agents (or users) can download and install them. This closes the loop between local execution and global skill improvement.

The community model raises coordination questions that aren't fully solved: if agent A evolves a skill based on its environment and agent B installs it, does it work in B's environment? OpenSpace sidesteps this somewhat because evolved skills focus on execution reliability (tool-specific patterns, error recovery) rather than environment-specific configuration.

## Security: Skills Are Executable Code

The most important thing to understand about skills: they are not documentation. They are instructions executed by a capable agent with access to tools, files, and network. A malicious or compromised skill can:

- Inject commands into subsequent agent actions (prompt injection)
- Exfiltrate data through tool calls
- Install supply-chain payloads via scripts bundled in the skill folder
- Escalate permissions by manipulating the agent's reasoning about what's allowed

The **skill-security-auditor** from alirezarezvani/claude-skills addresses this directly. It's a meta-skill that runs static analysis over other skills, checking for:
- Command injection patterns in script files
- Prompt injection patterns in SKILL.md instructions
- Data exfiltration signatures in tool usage patterns
- Supply-chain risks in bundled dependencies

Running a security auditor before installing community skills is the equivalent of running `npm audit` before installing packages. The analogy to npm is apt: the skills ecosystem is at approximately the same maturity level npm was in 2012 — rapidly growing, broadly useful, and without robust security infrastructure yet.

## Distribution Models

| Model | Example | Tradeoff |
|-------|---------|----------|
| In-repo (`.claude/skills/`) | Most project-specific skills | High trust, low discoverability |
| GitHub repo | alirezarezvani, addyosmani | Discoverable, manual install |
| Bundled with tool | googleworkspace-cli | Zero-friction install, one vendor |
| Hook-installed | graphify | Always-on, invasive |
| Cloud community | OpenSpace | Cross-agent sharing, trust questions |

## Composability

Skills can reference other skills by name — a skill's instructions can say "use the code-review skill" and the agent will invoke it if installed. Dependency management isn't natively built into the format: there's no `package.json`-style manifest declaring skill dependencies, and no install-time resolution. The agent handles it at runtime — if the referenced skill isn't installed, the agent either fails gracefully or improvises.

This is a gap the ecosystem will need to close as skills become more compositional. The addyosmani lifecycle-mapping approach hints at one direction: skills composed by workflow stage rather than by explicit dependency.

## Inbound Sources

- [[sources/claude-skills-alirezarezvani]]
- [[sources/addyosmani-agent-skills]]
- [[sources/googleworkspace-cli]]
- [[sources/graphify]]
- [[sources/openspace]]
