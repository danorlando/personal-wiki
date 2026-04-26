---
tags:
  - agent_systems
  - self_improving_agent
  - memory
  - skills
  - nous_research
  - messaging_gateway
  - rl_training
updated: 2026-04-26
source: https://github.com/NousResearch/hermes-agent
---

# Hermes Agent

Nous Research's self-improving personal AI agent — distinguished by a closed learning loop that creates, stores, and autonomously improves procedural skills from experience, combined with a multi-platform messaging gateway that lets the agent run on remote infrastructure while being driven from any device.

## Key design decisions / architecture

**The learning loop is the thesis.** Most agents have memory; Hermes has a skill-creation pipeline. After completing complex tasks, the agent autonomously generates reusable "skills" — structured procedural knowledge — stores them, and improves them during subsequent use. The agent also nudges itself to persist knowledge (rather than forgetting it at session end), and uses FTS5 full-text search with LLM summarization across past sessions for cross-session recall. This is a qualitatively different architecture from conversation-scoped agents.

**Skills as an open standard.** Skills are compatible with the `agentskills.io` open standard, meaning Hermes-generated skills can in principle be shared across agent ecosystems, not just reused internally. This is a deliberate interoperability bet — treating skills like shareable modules rather than private model weights.

**Dialectic user modeling via Honcho.** Hermes integrates [Honcho](https://github.com/plastic-labs/honcho) for user modeling — building a persistent, deepening model of who the user is across sessions. This goes beyond memory (what happened) to modeling (who the user is). The term "dialectic" suggests the model is updated through structured interaction, not just passive observation.

**Infrastructure-agnostic compute.** Six terminal backends are supported: local, Docker, SSH, Daytona, Singularity, and Modal. The Daytona and Modal backends offer serverless persistence — the agent environment hibernates when idle and wakes on demand, costing nearly nothing between sessions. The design explicitly decouples the agent's runtime environment from the user's local machine, enabling a $5 VPS or a GPU cluster with equal ease.

**Messaging gateway as the primary UX surface.** Hermes treats Telegram/Discord/Slack/WhatsApp/Signal/Email as first-class deployment targets, not secondary integrations. A single `hermes gateway` process handles routing across all platforms, with cross-platform conversation continuity (voice memo transcription included). The CLI TUI is one client among many.

**Subagent delegation and RPC tools.** Hermes can spawn isolated subagents for parallel workstreams, and supports Python scripts that call tools via RPC — collapsing multi-step pipelines into "zero-context-cost turns." This is a cost-control mechanism: offloading work to subagents or scripts avoids bloating the main agent's context window.

**RL training pipeline built in.** The repo includes Atropos RL environment integration (`tinker-atropos` submodule) and batch trajectory generation for training tool-calling models. This positions Hermes not just as a user-facing agent but as a data generation and RL training platform — Nous Research's research agenda leaks through.

**OpenClaw migration path.** Hermes explicitly supports migrating settings, memories, skills, and API keys from OpenClaw (`hermes claw migrate`). This signals Hermes is positioning as a successor in the community-built agent harness space.

**Provider-agnostic model selection.** `hermes model` switches LLM provider (Nous Portal, OpenRouter 200+ models, z.ai/GLM, Kimi, MiniMax, OpenAI, or custom endpoints) with no code changes. Model lock-in is treated as a first-class risk to avoid.

## Notable patterns and concepts

- **Skills system:** Skills are procedural memory — reusable, improvable, shareable via `agentskills.io`. The `/skills` command and `/<skill-name>` invocation make skills feel like slash commands.
- **Cron scheduler with platform delivery:** Scheduled tasks deliver results to any configured messaging platform — daily reports, nightly backups, weekly audits in natural language.
- **MCP integration:** Any MCP server extends the tool surface without code changes.
- **Context files:** Project-level context files shape every conversation in that directory (similar to CLAUDE.md).
- **SOUL.md persona file:** A persona definition file (migrated from OpenClaw) configures the agent's personality and behavior defaults.

## Concepts touched

- [[Self-Improving-Agents]]
- [[Agent-Memory-and-RAG]]
- [[Agent-Skills-and-Procedural-Memory]]
- [[Messaging-Gateway-Architecture]]
- [[User-Modeling-in-AI-Agents]]
- [[Serverless-Agent-Deployment]]
- [[Agent-Scheduling-and-Automation]]
- [[RL-Training-from-Agent-Trajectories]]
- [[Model-Context-Protocol]]
- [[Claude-Code-Ecosystem]]

## Inbound sources

- `/Users/dan.orlando/Code/my_apps/personal_wiki/raw/Repos/agent_systems/hermes-agent.md`
