---
title: "alirezarezvani/claude-skills"
created: 2026-04-26
updated: 2026-04-26
type: summary
tags:
  - [agent-skills, claude-code, multi-tool, orchestration, personas, python]
---

# alirezarezvani/claude-skills

One-line summary: 248 production-ready [[Agent-Skills]] across 9 domains for 11 AI coding tools, bundled with a three-tier taxonomy (Skills / Agents / Personas) and a security auditor that runs before install.

## Problem it solves

Skill collections for AI coding tools are tool-specific: a skill written for Claude Code doesn't work in Cursor, Windsurf, or Aider. Teams end up maintaining parallel copies per tool. There's also no standard model for how skills, task agents, and cognitive personas relate to each other — they collapse into a single "prompt" category, making it hard to reason about composition or reuse.

## Core architectural insight

The central contribution is a **three-tier taxonomy**:

- **Skills** — how to execute a specific operation (procedural knowledge)
- **Agents** — what task to accomplish (goal-oriented)
- **Personas** — who is thinking (cognitive style and priorities)

Most skill libraries conflate all three. Separating them enables composition: a Startup CTO persona applied to a refactoring agent using a code-review skill produces different behavior than a Growth Marketer persona applied to the same agent. Personas define the value weighting, not the procedure.

The second key decision is **zero-dependency tooling throughout**. The 332 bundled Python CLI tools use only stdlib — no pip installs. This means skills can invoke real computation (parsing, formatting, analysis) without environment setup, making them portable across any machine an agent runs on.

The **multi-tool convert script** is a practical consequence of the taxonomy: because skills are encoded in a tool-neutral intermediate form, one command transforms the entire library into Cursor, Aider, Windsurf, Kilo Code, or other native formats. The taxonomy is the portability layer.

## Key capabilities

- 248 skills across 9 domains; 5,200+ GitHub stars signals community uptake
- **POWERFUL tier**: 25 advanced skills including `agent-designer`, `rag-architect`, `mcp-server-builder`, and `skill-security-auditor`
- **skill-security-auditor**: scans any skill for command injection, prompt injection, data exfiltration, and supply-chain risks — zero dependencies, runs before install. This is notable because most skill collections have no pre-install security gate
- **Orchestration protocols**: four named patterns — Solo Sprint (single agent, one task), Domain Deep-Dive (one agent, deep vertical), Multi-Agent Handoff (sequential specialist handoff), Skill Chain (output of one skill feeds next)
- **Personas**: Startup CTO, Growth Marketer, Solo Founder — each encodes a decision framework, not just a role label

## Tradeoffs and limitations

- The taxonomy adds cognitive overhead: users must decide which tier a new prompt belongs to before contributing or composing
- 248 skills is large enough that discovery becomes a problem — without good indexing, teams gravitate toward skills they already know
- Multi-tool conversion assumes the target tools' formats are stable; a tool update can break the converter for that target
- No runtime orchestration engine is included — the Skill Chain and Multi-Agent Handoff patterns are conventions, not enforced infrastructure

## Relation to other work

The Personas concept overlaps with but is distinct from the Agents/Skills framing in [[sources/claude-code-how-we-use-skills]]. The security auditor addresses the same threat model that [[sources/googleworkspace-cli]]'s Model Armor integration targets. The orchestration protocols anticipate the kind of self-evolving skill execution that [[sources/openspace]] formalizes.

## Inbound sources

- [[sources/claude-skills-alirezarezvani]] ← this page
