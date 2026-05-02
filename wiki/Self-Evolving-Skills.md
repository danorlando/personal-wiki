---
title: "Self-Evolving Skills"
created: 2026-04-26
updated: 2026-05-02
type: concept
tags:
  - concept
  - agents
  - skills
  - self-improvement
---

# Self-Evolving Skills

The idea that [[Agent Skills]] can improve themselves without human intervention, triggered by execution outcomes. OpenSpace's implementation is the most detailed example in the wild.

## The Problem

Skills degrade silently. A skill written against one version of a tool breaks when the tool updates — and the agent keeps trying, keeps failing, and the failures don't propagate back into the skill definition. Separately, when an agent succeeds at something novel, that success disappears into conversation history rather than being encoded for reuse. Humans have to notice both problems and fix them manually.

Self-evolving skills are an attempt to close this loop: the system that executes skills also updates them. This is a pattern shared with [[Self-Evolving-Agents]] more broadly — Autogenesis generalizes it from skills to the full agent stack (prompts, tools, environments, memory) via an [[Agent-Protocol]].

## Three Evolution Modes

OpenSpace defines three distinct ways a skill can change:

**FIX** — repairs a broken or outdated skill in-place. The skill identity is preserved; only the implementation changes. This is triggered when a skill fails consistently — tool API changes, environment drift, deprecated flags. The same skill, new version.

**DERIVED** — creates an enhanced or specialized version from a parent skill. The parent remains unchanged; the derived skill lives in a new directory and coexists alongside it. This is how a general-purpose skill becomes a domain-specialized one: the parent handles the 80%, the derived skill handles a specific variant with additional context or constraints baked in.

**CAPTURED** — extracts novel reusable patterns from successful executions where no parent skill exists. The agent did something useful ad hoc; the system notices and packages it as a skill for future reuse. No parent, no predecessor — this is the "discovered skill" mode.

## Three Independent Triggers

Evolution doesn't only happen after a task completes. OpenSpace runs three independent monitors:

1. **Post-execution analysis** — after every task, examine the execution trace for patterns worth capturing or problems worth fixing
2. **Tool degradation detection** — monitor tool call success rates across sessions; when a tool's reliability drops, trigger FIX evaluation on skills that use it
3. **Metric monitor** — watch outcome metrics (task completion rate, retry counts, error types) and trigger evolution when thresholds are crossed

The three triggers are independent. Tool degradation can fire between tasks. Metric monitors can fire across a time window without a specific triggering execution.

## What Actually Gets Evolved: The GDPVal Findings

The GDPVal benchmark (OpenSpace's evaluation framework) produced a counterintuitive result: when left to evolve freely, the system does not primarily learn domain knowledge. Of 165 auto-evolved skills:

- **44 skills** — file format I/O (PDF extraction edge cases, CSV parsing quirks, encoding handling)
- **29 skills** — execution recovery (how to handle Python environment failures, retry strategies, subprocess errors)
- Remaining skills — distributed across tool-specific reliability, API error handling, environment setup

The agent isn't learning "how to do payroll" or "how to analyze financial statements." It's learning "how to reliably run Python in this environment" and "how to handle PDF extraction when the file is malformed." The knowledge that accretes is about **execution reliability**, not domain competence.

This is consistent with the broader [[Agent-Memory]] insight that what you store reflects a theory of what agents need. OpenSpace's bet is that execution reliability is the bottleneck — and the empirical data from GDPVal supports it.

## Safeguards

Autonomous skill modification is high-stakes — a corrupted skill propagates errors to every subsequent execution. OpenSpace includes:

- **Confirmation gates** — human-in-the-loop approval before a skill replaces its predecessor in the active library
- **Anti-loop guards** — prevent a skill from triggering its own evolution repeatedly (evolution cycles)
- **Safety checks** — scan evolved skills for prompt injection patterns, data exfiltration risks, and supply-chain-style attacks before acceptance
- **Validation before replacement** — derived/fixed skills are tested before the predecessor is superseded; the predecessor is retained until validation passes

## Relation to Other Concepts

Self-evolving skills are one of three memory architectural patterns in [[Agent-Memory]]. Where Hindsight stores Mental Models as data and OpenViking stores tiered abstractions in a navigable hierarchy, OpenSpace stores execution patterns as executable code. The "learn by doing" framing is distinct: the stored artifact can be run, not just read.

The skill format itself follows [[Agent Skills]] conventions. The evolution mechanism is what's novel — standard skills are static; evolved skills carry a lineage (predecessor links, evolution type, triggering event).

Self-evolving skills are a **specialization** of the broader [[Self-Evolving-Agents]] concept: they evolve one resource type (skills) while [[sources/autogenesis|Autogenesis]] generalizes the pattern to prompts, tools, environments, and memory via an [[Agent-Protocol]]. The [[Agent-Protocol]] layer makes skill evolution composable with other resource evolution — a skill update can trigger a prompt update, and both are governed by the same commit gate.

## Inbound Sources

- [[sources/openspace]]
- [[sources/autogenesis]]
