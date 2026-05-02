---
title: "Agent Memory"
created: 2026-04-26
updated: 2026-05-02
type: concept
tags:
  - concept
  - agents
  - memory
  - architecture
---

# Agent Memory

Most agent memory systems treat memory as **recall** — the agent asks a question, retrieves relevant chunks, and uses them. The emerging alternative treats memory as **learning** — building structured understanding that changes how the agent reasons, not just what it can look up. The distinction matters more than it first appears: recall gives you a better-equipped amnesiac; learning gives you an agent that compounds.

## The Recall vs. Learn Distinction

Recall-based memory answers the question "what have I seen before that's similar to this?" It's retrieval over a corpus. The agent's behavior doesn't change — only the context it has access to changes.

Learning-based memory answers "what do I understand now that I didn't before?" The agent's stored models of the world update. Future behavior differs not because context is richer, but because the agent carries different priors.

In practice, pure learning is hard to implement cleanly in LLM agents. The most interesting systems combine both: they store structured artifacts that encode learned abstractions, but retrieve them situationally. The critical variable is **what you choose to store** — and that choice reflects a theory of what agents need to know.

## Three Architectural Approaches

### 1. Biomimetic (Hindsight)

Hindsight organizes memory into three stores that mirror how humans are thought to encode knowledge:

- **World Facts** — factual knowledge about the environment, people, tools, and context
- **Experiences** — episodic records of what happened, what was tried, what worked
- **Mental Models** — higher-order abstractions: patterns the agent has generalized from experiences

The three corresponding operations are **Retain** (write to memory), **Recall** (retrieve from memory), and **Reflect** (synthesize experiences into mental models). Reflect is the key step — it's what converts episodic history into transferable understanding.

Recall uses **four parallel retrieval strategies** merged via reciprocal rank fusion:
1. Semantic similarity (embedding-based)
2. Keyword search
3. Graph traversal (entity relationships)
4. Temporal ordering (recency)

Running all four in parallel and fusing the results hedges against any single retrieval method's blind spots. Semantic search misses exact-match queries; keyword search misses paraphrases; graph traversal finds structured relationships that neither captures.

### 2. Filesystem Paradigm (OpenViking)

OpenViking takes a deterministic, hierarchical approach rather than a probabilistic one. Memory is organized as a filesystem with `viking://` URIs, tiered into three levels:

- **L0** — immediately loaded at session start (critical priors, current task state)
- **L1** — loaded on demand by the agent (domain knowledge, tool guides)
- **L2** — loaded recursively when a directory is traversed (supporting detail, archives)

The agent can navigate this structure explicitly: it knows where things live, can write new nodes, and can traverse directories to pull in subtrees. This makes memory **observable** — the agent (and the user) can inspect the memory structure as a filesystem, not as an opaque vector index. The trajectory of memory updates is auditable.

The bet here is that determinism beats stochasticity for agent reliability. An agent that always loads L0 on start, and explicitly navigates to what it needs, is more predictable than one that hopes semantic search surfaces the right chunks.

### 3. Self-Evolving Skills (OpenSpace)

OpenSpace takes a different angle: rather than storing memories as data, it encodes them as **executable skills** that capture successful execution patterns. When an agent completes a task, the system analyzes the execution trace and decides whether to create or update a skill.

Memory in this framing is "how to reliably do this class of task in this environment" — not episodic history. See [[Self-Evolving-Skills]] for the full mechanics.

## What You Store Is the Design Decision

The four approaches differ most sharply in their theory of what's worth encoding:

|| System | Stored unit | Theory |
|--------|-------------|--------|
| Hindsight | Mental Models (abstractions over experiences) | Agents need generalizable patterns, not raw history |
| OpenViking | Tiered abstractions in a navigable hierarchy | Agents need structured, deterministic context |
| OpenSpace | Executable skills (patterns as runnable code) | Agents need reliable execution, not just knowledge |
| DPM | Immutable event log + projection | Regulated agents need replay/audit/isolation/scale by construction |

All four reject naive "store everything, retrieve by similarity" approaches. They're all bets that the stored representation — not just the retrieval mechanism — is the leverage point.

### 4. Deterministic Projection (DPM)

DPM takes the most radical stateless position: **memory does not exist as a runtime object at all** until decision time. The trajectory is stored as an immutable append-only event log, and a single task-conditioned projection at temperature zero produces the memory view. This is [[Event-Sourcing]] applied to agent memory.

The tradeoff is explicit: DPM gives up the ability for an agent to deliberate by editing its own memory mid-trajectory. In exchange, it satisfies four enterprise properties by construction — deterministic replay, auditable rationale, multi-tenant isolation, and statelessness for horizontal scale — that stateful architectures can only achieve through costly retrofits.

Empirically, DPM matches summarization-based memory at generous budgets and strictly outperforms it at tight budgets (20× compression), because incremental summarization's per-step losses compound across the trajectory while DPM's single projection sees the full log. See [[Deterministic-Projection-Memory]] for the full architecture and results.

|| System | Stored unit | Theory |
|--------|-------------|--------|
| Hindsight | Mental Models (abstractions over experiences) | Agents need generalizable patterns, not raw history |
| OpenViking | Tiered abstractions in a navigable hierarchy | Agents need structured, deterministic context |
| OpenSpace | Executable skills (patterns as runnable code) | Agents need reliable execution, not just knowledge |
| DPM | Immutable event log + projection | Regulated agents need replay/audit/isolation/scale by construction |

## Session Persistence (Personal Stack Pattern)

claude-mem adds a practical fourth pattern: Claude Code session memory via lifecycle hooks. Observations from each session are captured via `PostToolUse`/`Stop` hooks and injected back into future sessions using a 3-layer retrieval pattern (search index → timeline → full fetch). Claims ~10× token savings versus naive full-context injection. This is simpler than the three architectures above — no World/Experience/Mental-Model split, no filesystem URI scheme, no skill generation — but sufficient for the personal-assistant use case ([[sources/claude-mem]]).

PAI's three-tier hot/warm/cold memory feeds a continuous feedback loop — ratings, sentiment, and success/failure signals from each interaction improve future behavior. The explicit design goal is that the system's performance on *your* tasks improves over time ([[sources/personal-ai-infrastructure]]).

## Inbound Sources

- [[sources/hindsight]]
- [[sources/openviking]]
- [[sources/openspace]]
- [[sources/claude-mem]]
- [[sources/personal-ai-infrastructure]]
- [[sources/stateless-decision-memory]]
