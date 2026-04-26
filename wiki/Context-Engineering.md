---
tags:
  - concept
  - context-management
  - agentic-ai
  - claude-code
updated: 2026-04-26
---

# Context Engineering

The deliberate design of what information enters an LLM's context window, when it enters, how it's structured, and how it's refreshed — treating the context window as a resource to be managed rather than a buffer to be filled.

## Context Rot

The foundational problem: as a context window fills with accumulated conversation, prior tool outputs, and intermediate state, model decision quality degrades even within the nominal context limit. The model doesn't "forget" — it attends to everything, including noise. Context rot is the dominant failure mode in long agentic sessions ([[sources/get-shit-done]]).

The solution is architectural: structure work so each execution unit gets a fresh context rather than managing one long session better.

## Key Techniques

**Fresh subagent contexts per task.** Each meaningful unit of work (a plan, a verification pass, a debugging session) is executed in a new subagent with only the relevant context injected — not the full conversation history. GSD targets 30–40% context usage in the orchestrator even through large parallel workloads ([[sources/get-shit-done]]).

**Structured context files.** GSD maintains a set of typed context files (`PROJECT.md`, `REQUIREMENTS.md`, `ROADMAP.md`, `STATE.md`, `CONTEXT.md`, `PLAN.md`, `SUMMARY.md`), each with a specific role and calibrated size limits. The file system *is* the context engineering layer — persistent state lives in files, not conversation history ([[sources/get-shit-done]]).

**Tiered retrieval.** Rather than injecting all memory upfront, retrieve progressively: search index → timeline → full fetch. claude-mem achieves ~10× token savings versus naive full-context injection using a 3-layer retrieval pattern ([[sources/claude-mem]]). See also [[Progressive-Disclosure]].

**Skill auto-injection on trigger.** oh-my-claudecode stores skills with trigger patterns and auto-injects them when patterns match — relevant context arrives exactly when needed, not always ([[sources/oh-my-claudecode]]).

**Capture preferences before research.** GSD's "discuss phase" captures layout, error-handling, and depth preferences into `CONTEXT.md` before research begins — so the researcher investigates *your* vision rather than generic best practices ([[sources/get-shit-done]]).

## XML Prompt Structure

GSD formats task plans as structured XML (`<task>`, `<files>`, `<action>`, `<verify>`, `<done>`) optimized for Claude's parsing. Structured formats eliminate ambiguity and embed verification criteria at the task level — reducing the chance that an agent misunderstands its scope ([[sources/get-shit-done]]).

## Security Dimension

When user-controlled text flows through planning artifacts into LLM system prompts, context engineering creates a prompt injection attack surface. GSD implements path traversal prevention, a centralized prompt injection scanner, a `PreToolUse` prompt guard hook, and safe JSON parsing as defense-in-depth ([[sources/get-shit-done]]).

## Relation to Other Concepts

- [[Progressive-Disclosure]] — tiered retrieval is one form of progressive disclosure applied to memory
- [[Multi-Agent-Orchestration]] — fresh subagent contexts are an orchestration pattern driven by context rot
- [[Agent-Memory]] — memory systems solve context rot by externalizing state
- [[Agent-Skills]] — skills are pre-packaged context that arrives on demand

## Inbound Sources

- [[sources/get-shit-done]]
- [[sources/claude-mem]]
- [[sources/oh-my-claudecode]]
- [[sources/everything-claude-code]]
