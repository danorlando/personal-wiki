---
title: "OpenSpace (HKUDS)"
created: 2026-04-26
updated: 2026-04-26
type: summary
tags:
  - [agent-skills, self-evolving, mcp, benchmark, hkuds, skill-evolution]
---

# OpenSpace (HKUDS)

One-line summary: A self-evolving skill engine that plugs into any agent as an MCP server and continuously repairs, derives, and captures skills from live execution — so agents learn from experience instead of repeating failures.

## Problem it solves

Current agent skill systems are static. A skill works at deploy time and silently degrades as the world changes — APIs update, file formats shift, tool behavior diverges. Failures repeat across sessions because there's no feedback loop from execution back to skill content. Worse, knowledge is trapped per-agent: if one agent's execution discovers a better approach, every other agent starts from zero. The thesis is that **agents never learn from experience**, and OpenSpace is a direct architectural response to that.

## Core architectural insight

The core idea is that **skill mutation is a first-class operation**, triggered automatically from three independent signals:

- **Post-execution analysis**: after every task, OpenSpace examines what worked and what failed
- **Tool degradation detection**: monitors for tools behaving unexpectedly (wrong output format, timeouts, schema changes)
- **Metric monitor**: tracks performance signals over time; triggers evolution when metrics degrade

Three mutation modes handle different cases:
- **FIX**: repair a broken skill in-place — same interface, corrected implementation
- **DERIVED**: create an enhanced version alongside the original — preserves backward compatibility while adding capability
- **CAPTURED**: extract a novel pattern from a successful execution that wasn't in any existing skill — new skill from scratch

The CAPTURED mode is the most architecturally interesting: it means skills can grow from zero. OpenSpace doesn't require a human to identify patterns worth codifying; a particularly effective execution sequence becomes a skill automatically.

The **GDPVal benchmark** result reveals where evolution actually helps: of 165 auto-evolved skills, 44 address file format I/O and 29 address execution recovery — not domain knowledge. The dominant failure modes agents hit in production are tool reliability and format negotiation, not reasoning. Skills that patch these plumbing problems are where the 4.2× income improvement and 46% token reduction come from.

The **cloud community** extends learning across agent boundaries: one agent's CAPTURED or FIX skill can be shared to a community pool that all connected agents draw from. This is collective intelligence at the skill level.

Integration is deliberately lightweight: OpenSpace installs as an MCP server (stdio/SSE/streamable HTTP) and adds two host skills to the agent (`delegate-task`, `skill-discovery`). No agent rewrite required.

## Key capabilities

- GDPVal benchmark: 4.2× higher income, 46% fewer tokens vs baseline on 50 professional real-world tasks (payroll calculators, tax returns, legal memos)
- 165 skills auto-evolved in benchmark runs — empirical evidence that FIX and CAPTURED fire frequently in real workloads
- "My Daily Monitor" showcase: 60+ skills evolved from scratch to build a live dashboard, zero human code written
- Cloud community: cross-agent skill sharing
- Communication gateway: WhatsApp and Feishu adapters for external message I/O

## Tradeoffs and limitations

- Auto-evolution is only as good as its trigger signals — a skill that degrades gracefully (wrong output, no error) may not trigger FIX; silent failures are the hardest case
- CAPTURED mode has no human review gate by default — a misleading execution that happened to succeed can produce a bad skill
- Cloud community skill sharing introduces a trust problem: a malicious or buggy shared skill can propagate to all connected agents (comparable to the supply-chain risk flagged in [[sources/claude-skills-alirezarezvani]])
- No discussion of skill versioning or rollback if a FIX worsens behavior — the mutation is persistent
- GDPVal is a benchmark from the same lab (HKUDS) that built OpenSpace; external reproduction has not been confirmed

## Relation to other work

OpenSpace's Reflect-equivalent (CAPTURED from successful execution) parallels [[sources/hindsight]]'s Reflect operation — both synthesize new knowledge from accumulated experience, but Hindsight targets memory entries while OpenSpace targets executable skills. The cloud community sharing model is the distributed version of what [[sources/claude-skills-alirezarezvani]] does with its convert script. The MCP integration pattern is identical to [[sources/cli-anything]]'s CLI-Hub approach. Both repos are from HKUDS, suggesting a shared research program around agent capability infrastructure.

## Inbound sources

- [[sources/openspace]] ← this page
