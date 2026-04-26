---
tags:
  - concept
  - agents
  - tooling
  - cli
updated: 2026-04-26
---

# Agent-Native Software

The idea that software needs to be redesigned — or at minimum re-wrapped — for AI agent consumption, not human consumption. The gap between what agents can reason about and what they can actually operate is currently large. Closing it is an open design problem.

## The Gap

Agents reason well but can't use real professional software. The three common failure modes:

- **UI automation** — fragile, layout-dependent, breaks on version updates, produces no structured output
- **Existing APIs** — cover roughly 10% of the surface area of a professional application; the high-leverage operations (complex workflows, bulk operations, format-specific rendering) are often missing
- **LLM hallucination** — agents generate plausible-looking commands for tools that don't have a CLI at all

The result: agents are often restricted to a toy subset of the tools a human professional uses daily. A human analyst uses Excel's full solver and pivot table engine; an agent gets read/write CSV.

## Two Approaches to Wrapping

### 1. Purpose-Built Agent CLIs (CLI-Anything)

CLI-Anything's approach: take any existing software's codebase and generate a CLI wrapper that calls the real backend. No reimplementation, no replacement — the generated CLI is a thin translation layer over the existing library or service.

The generation pipeline has 7 phases:
1. Codebase analysis — understand the existing API surface
2. Command taxonomy — group operations into logical verbs and subcommands
3. Interface design — define argument shapes, flag names, help text
4. Implementation scaffolding — generate the CLI handler code
5. Integration wiring — connect handlers to the real backend calls
6. JSON output standardization — add `--json` flag to every command
7. SKILL.md generation — auto-generate the [[Agent Skills]] manifest

The `--json` flag throughout is non-negotiable for agent consumption. Agents can't parse human-readable text output reliably; structured JSON output is the interface contract.

The SKILL.md auto-generation is the other key step: it produces the [[Progressive Disclosure]] entry point that tells an agent what the CLI can do, what commands exist, and what flags are available — without requiring the agent to run `--help` on every subcommand.

### 2. Discovery-Driven CLIs (googleworkspace-cli)

A different bet: rather than generating a CLI from source code analysis, build the CLI surface dynamically from the API's own schema. For Google Workspace, this means consuming the **Google Discovery Service** — the machine-readable description of every API endpoint, parameter, and return type.

The advantage: the CLI is always synchronized with the actual API. No static command list to go stale. When Google adds a new Calendar endpoint, the CLI gains a new command automatically on next build. This is especially important for Google Workspace, where the API surface spans Docs, Sheets, Drive, Gmail, Calendar, Meet, and Admin with frequent updates.

The tradeoff: discovery-driven generation is only possible when the underlying system publishes a machine-readable schema. It doesn't generalize to arbitrary software the way CLI-Anything does.

## The Rendering Gap

One non-obvious problem with CLI wrapping of GUI applications: GUI apps apply effects **at render time**. A naive CLI wrapper that generates project files but uses a simple export path silently drops effects — the effects exist in the project data model, but the export step doesn't invoke the renderer.

Example: a video editing CLI that creates a project with color grading and transitions, then exports using a basic muxer, will produce a flat video with no effects applied. The effects are in the project file; the renderer is what bakes them in. To build a correct CLI, you must invoke the real renderer — which may be a headless mode of the GUI application itself, or a separate rendering binary.

This is a general problem: any CLI wrapping a system where processing is split between a data model and a rendering/execution step must ensure the CLI invokes the execution step, not just manipulates the data model.

## Why CLI Over GUI Automation

The case for CLI as the agent-native interface form:

| Property | CLI | GUI Automation |
|----------|-----|----------------|
| Structured output | Native (`--json`) | Requires parsing |
| Self-describing | `--help` at every level | Requires vision model |
| Composable | Pipes, scripts, skill composition | Fragile chaining |
| Deterministic | Same inputs → same outputs | Layout/state dependent |
| Agent-first | Designed for programmatic consumption | Designed for humans |

CLIs are essentially the original API — before REST, before gRPC, the CLI was how programs composed. [[Agent Skills]] extend this: a SKILL.md wrapping a CLI gives an agent both the interface and the instructions for using it correctly, as a single installable unit.

## Inbound Sources

- [[sources/cli-anything]]
- [[sources/googleworkspace-cli]]
