	

**Role:** Senior Software Engineer II, Aledade
**Focus:** Generative AI infrastructure, healthcare systems integration, scalable LLM-backed services, technical leadership

---

## System Context — "What It Is"

### The product

The Medscape AI Answer Engine is a conversational AI service for Medscape clinicians. A user asks a clinical question (drug interactions, diagnostic criteria, treatment protocols, etc.) and the system returns a structured, source-grounded response — a summary, cited sources, related articles, and suggested follow-up questions — streamed back to the UI over SSE in real time.

### What this system does

It's a FastAPI + LangGraph service that takes a clinician query and runs it through a multi-subgraph pipeline:

1. **Guardrails + PII detection** — at the API layer, before anything reaches the graph.
2. **History detection subgraph** — classifies whether this turn is a new conversation, a continuation, or a reference to a prior session.
3. **Intent classification with router and planning tool**
4. **Query normalization subgraph** — normalises, translates, and context-expands the raw query into an `enhanced_query_text` that downstream nodes work against.
5. **Orchestrator subgraph** — a ReAct-style agent that reads a skills manifest (progressive disclosure), selects which skills apply, plans a retrieval strategy, executes it, and composes the final response.
6. **Streaming response** — token-level SSE with a custom structured-output parser that separates a streamed human-readable summary from structured JSON (sources, related articles, follow-ups) embedded in the same LLM response.

### Suggested 2-sentence opener

> "I designed and built a FastAPI + LangGraph conversational AI answer engine for Medscape. A clinician asks a clinical question, and the system streams back a structured, source-grounded response — classifying conversation history, cleaning the query, planning retrieval, and composing the answer through a multi-agent subgraph pipeline, with PII detection and guardrails at the API boundary for healthcare safety."

### Why this framing maps to the Aledade role

Aledade's description asks for engineers who will:

- *"Architect systems to enhance the capabilities and relevance of AI models."*
- *"Contribute to APIs and interfaces for integrating generative AI capabilities into existing healthcare systems."*
- *"Maintain the security of protected patient health information in the context of AI."*
- *"Partner, as a peer, with Engineering Managers, Product Managers, and stakeholders."*
- *"Mentor and coach more junior engineers."*
- *"Act as a trusted technical decision-maker in a team setting."*

This project is a textbook example of all of the above, and I've been the technical lead on it end-to-end.

---

## Headline — Technical Leadership on a CEO-Priority Initiative

**The single most important thing to convey in this interview.** I'm currently the technical lead and architect on the project for a 15-person team, and it is the **#1 priority for the CEO of Internet Brands**. Every architectural decision on this project goes through me.

### How I lead architectural decisions on this team

I don't hand down decisions. When we hit a new challenge, I:

1. **Work up multiple candidate solutions** with the trade-offs, pros, and cons of each.
2. **Present them to the team with a recommendation**, but frame it as a decision the group is making, not one I've already made.
3. **Facilitate the discussion** until the team naturally converges on the best option for the current constraints.

I've found this is the fastest path to real buy-in. People execute well on decisions they helped shape; they execute reluctantly on decisions they were handed. On a 15-person team with junior engineers who need to own their pieces, that distinction compounds.


### Why this matters for the Aledade role

The role description specifically calls out *"partner, as a peer, with Engineering Managers, Product Managers, and stakeholders"* and *"act as a trusted technical decision-maker."* That is the exact shape of what I do on this team every day. The engineering content below is evidence for that claim — but the claim itself is the headline.

---

## Architectural Evolution — Three Production Generations

This is the third production version of the Medscape AI Answer Engine. Framing the engineering story against the prior two versions is the strongest signal that the current architecture isn't the first thing that came to mind — it's what survived real production constraints.

| Generation | Platform | Why it was replaced |
|---|---|---|
| V1 | Microsoft Copilot | No-code platform; hit its ceiling on customisation, observability, and the kind of structured output streaming the UX required. |
| V2 | Dify | Better than Copilot for LLM workflows, but still a low-code orchestration layer. No way to cleanly implement deterministic retrieval, typed state contracts, or production-grade streaming with structured output. The V2 workflow is checked in at `docs/reference/ai_answer_engine_v1_dify_workflow.yml` as a reference implementation. |
| **V3 (current)** | FastAPI + LangGraph, engineered from scratch | Full control over graph topology, state contracts, model selection, streaming, and the seams where guardrails/PII/compliance plug in. |

### The talking point

**The ceiling that forced each migration was always the same:** the product kept demanding things the platform couldn't give us cleanly. Copilot → Dify was driven by needing better LLM workflow composition. Dify → custom service was driven by needing streaming, typed state, deterministic retrieval, and healthcare-grade safety at the API boundary. **At some point the cost of bending a no-code tool exceeds the cost of building the real thing.** Recognising that inflection point — and being the engineer the org trusts to lead the rebuild — is the move this product has made twice, and I've been the person leading the current one.

### In-system evolution (within V3)

Even within the current generation, the architecture has iterated. Two examples worth calling out:

#### 1. Orchestrator: ReAct loop → Plan-Execute (MAIAE-155)

| Phase | Architecture | Why it was replaced |
|---|---|---|
| Initial | Single ReAct loop — `orchestrator ⇄ tools ⇄ orchestrator`, LLM chose every tool call | Non-deterministic retrieval, model_rag leaking into the planning phase, and an OpenAI message-sequence constraint that made the loop fragile |
| **Current** | Split into two phases: an LLM planning node bound only to `select_skills` + `create_plan`, followed by a deterministic `execute_plan_node` that calls tools as plain Python | LLM decides *what* to retrieve once; execution is predictable, testable, and doesn't burn tokens on tool-call orchestration |

The planning LLM writes a typed `plan: list[dict]` into graph state. The executor reads it and dispatches each step. **The LLM no longer holds the wheel during execution — it holds it only during planning**, which is the right division of labour for a healthcare system where reproducibility matters.

#### 2. LLM access: module globals → Profile registry + runtime resolver

| Phase | Architecture | Why it was replaced |
|---|---|---|
| Initial | `set_llm()` wrote to module-level globals (`_llm`, `_llm_with_tools`). Nodes and tools called `get_llm()` directly, and each one imported the provider SDK the author was most familiar with. Thin, inconsistent LLM wrappers had spread across the codebase. | Three problems: (1) **DRY violation** — every tool author rolled their own wrapper with its own conventions. (2) **Shared mutable global state** — safe today but a silent concurrency bug the first time anyone adds per-request model selection. (3) **No runtime flexibility** — the orchestrator couldn't steer model choice for a downstream node. |
| **Current** | Named **profile registry** (`default`, `orchestrator_reasoning`, `retrieval_web_search`, etc.) + **role policies** (each node role has an allowlist of profiles) + a **runtime resolver** that hands the right `BaseChatModel` to the caller. The orchestrator can write `selected_profiles` into graph state to override the default for a downstream node. Deploy-time overrides come from a single `LLM_PROFILES_OVERRIDE` env var, validated at startup. | One consistent way to get a model. One place to change a model ID. Runtime steerability without mutable globals. |

**Why this is the most senior-shaped piece of work in the repo.** It solved three problems at once — DRYness for the team, concurrency-safety for the future, and runtime model selection for the orchestrator — with a single abstraction. And it's documented at `docs/llm-abstraction.md` with how-to recipes so a junior engineer can wire a new node without asking me.

---

## 1. Scalability Analysis & Self-Audit
*Maps to: "scalable and performant solutions", "trusted technical decision-maker"*

**The headline:** Wrote a standalone scalability assessment of the `/runs/stream` endpoint against a target of 200–1,000 concurrent SSE streams, naming **8 specific gaps** with severity, fix complexity, and a recommended fix order — then started executing against the list.

**Key points:**

- **Self-audit on a system I built.** The assessment (`docs/API_SCALABILITY_ASSESSMENT.md`) is honest about limits. Example finding: the `StreamingRegistry` is a module-level `dict[str, asyncio.Task]`, which silently breaks in a multi-worker deployment because stop requests routed to Worker 2 can never cancel a task registered in Worker 1. That's the kind of gap you only find by reading the code *as an attacker of your own architecture*.
- **Priority matrix, not a list.** Each finding was rated "blocking at 200?" vs. "blocking at 1,000?" vs. "fix complexity." Gave the team a clear execution order rather than "here are some concerns."
- **Actually executing.** The current branch (MAIAE-146) is the Redis-backed `RedisStreamingRegistry` that replaces the in-process `dict` — the #1 finding from the assessment. The fix works across worker processes, uses a short-TTL Redis key polled on every stream iteration, and re-enables the Redis startup check so the app fails fast if Redis is unreachable rather than silently broken at runtime.
- **Findings not yet fixed are named, not hidden.** Missing async DB connection pool, missing concurrency semaphore, polling-based disconnect detection — all called out with specific file references and proposed remediations.

**Why this matters for Aledade.** The role description calls out *"strategies that minimize risk, leaning towards observability, alerting, metrics, high test coverage."* A written scalability audit *on a system you built yourself* is the single clearest signal that you think this way.

---

## 2. Multi-Subgraph LangGraph Architecture
*Maps to: "Architect systems to enhance AI models", "making complex data sets more accessible and actionable"*

**The headline:** The system is composed of four distinct LangGraph subgraphs wired into a root graph — guardrails → history detection → cleaning → orchestrator — each owning one concern, with explicit **state projection nodes** between them to prevent token bloat.

**Key points:**

- **Subgraphs, not monolith.** Each subgraph has its own typed state (`CleaningState`, `HistoryDetectionState`, `OrchestratorState`) and its own tests. The root graph composes them via projection nodes that explicitly choose which fields flow forward, which prevents the full conversation state (especially `messages`) from echoing back into every step and bloating downstream LLM prompts. This is a subtle but important detail — see the inline comment in `app/graphs/graph.py` at the `orchestrator_projection_node`.
- **Plan-execute split in the orchestrator.** Described above — planning LLM → deterministic execution → response. The orchestrator LLM is bound only to `select_skills` + `create_plan` during planning; retrieval runs as plain Python against a typed plan.
- **Skills as progressive disclosure.** `app/skills/` holds markdown files with YAML frontmatter. At startup the system scans all skill files and reads *only the frontmatter* — that manifest gets injected into every orchestrator system prompt so the LLM knows what capabilities exist. When the orchestrator selects a skill, the full skill content is loaded into the prompt on demand. This keeps the graph topology stable regardless of how many skills exist and keeps the default prompt small.
- **Iteration counter as a safety cap.** The orchestrator loop tracks iterations in state and forces an exit to the response node at 10 — a concrete budget, not an infinite loop. Reset inside the projection node so multi-turn threads don't accumulate iterations from prior turns and hit the cap prematurely.

---

## 3. Streaming Structured Output
*Maps to: "Design and implement prompt engineering strategies", "APIs for integrating generative AI capabilities"*

**The headline:** The UI needs to show a streaming human-readable summary *and* receive structured metadata (sources, related articles, follow-up questions) from the same LLM response. Most teams solve this by making two LLM calls. I solved it with one, using a custom streaming parser and tagged output.

**Key points:**

- **Single LLM call, two output shapes.** The orchestrator prompt instructs the model to emit the summary wrapped in `@@start_summary@@ ... @@end_summary@@` tags followed by a JSON block with structured fields. `StreamStructuredOutputParser` in `app/graphs/orchestrator/structured_output.py` feeds token chunks in, emits the visible summary text as it streams, and parses the JSON block at the end.
- **Holdback buffer for tag safety.** The parser implements a holdback: if the tail of the buffer *could* be the start of `@@end_summary@@`, it holds those characters back and waits for the next chunk rather than emitting them as visible text. Prevents the UI from ever flickering a partial tag.
- **SSE event types match the UI contract.** `ping`, `metadata`, `data`, `source`, `related_articles`, `follow_up_question`, `end`, `error` — each a separate SSE event type so the frontend can bind different handlers to each. One streaming LLM response fans out into multiple typed UI events.
- **Scar tissue documented.** `_unpack_message_stream_item` in `runs.py` normalises LangGraph's nested-tuple event shape from `astream(subgraphs=True)`. That took a full debug session to figure out — it's saved in my agent memory as a lesson learned so I don't spend another afternoon on it.

---

## 4. Healthcare AI Safety — PII Detection + Guardrails
*Maps to: "Maintain the security of protected patient health information and ensure compliance with relevant regulations in the context of AI"*

**The headline:** Compliance in an AI context isn't just "route through a proxy" — it's active detection at the API boundary and alignment guardrails inside the agent loop. The plumbing (all LLM traffic routes through the internal **Athena LiteLLM proxy** rather than direct OpenAI, gateway-enforced) is the floor, not the ceiling.

**Key points:**

- **PII detection at the API layer, before the graph.** A small PII-detection language model runs as middleware on the inbound query — **44 PII classes across 17 languages.** This is the right layer: if PII is in the query, we never want it to reach the orchestrator, the LLM, the logs, or the checkpoint store. Catching it at the API boundary keeps the rest of the system free of a compliance concern.
- **Guardrails as an orchestrator-callable tool.** Rather than a blunt pre/post filter, guardrails are exposed as a tool the orchestrator can invoke to validate answer alignment before finalising a response. This is *agent-aware* safety: the orchestrator decides when to consult guardrails based on what it's been asked, rather than every response paying the guardrails cost unconditionally. Lets the system be safe *and* fast.
- **Athena proxy as the compliance plumbing.** All model traffic transits the internal approved gateway via `AthenaAdapter`. Prompts and completions do not touch the public OpenAI API directly, which is the gating condition for HIPAA-adjacent AI work at Internet Brands.
- **Env discipline.** No keys in git, profile registry validated at startup, `LLM_PROFILES_OVERRIDE` fails fast on invalid JSON or unknown profile IDs.

**This is the single talking point most aligned with Aledade's mission.** Internet Brands is consumer-facing medical media; Aledade is value-based care with direct PHI exposure. But the *shape* of the problem — build safety in at the boundary, make it composable at the agent layer, and don't trust any single control — is the same.

---

## 5. LLM Abstraction as Team Infrastructure
*Maps to: "Design and implement prompt engineering strategies", "mentor junior engineers"*

**The headline:** Replaced a growing sprawl of ad-hoc LLM wrappers with a single three-layer abstraction — profiles, role policies, runtime — documented as how-to recipes so any engineer on the team can wire a new node without asking me. This is mentoring at the codebase level.

**Key points:**

- **The problem it solved.** Before this, developers were creating thin LLM wrappers wherever they needed a model — each one with different conventions, different param handling, different ways of binding tools. New tools meant new wrappers meant new inconsistencies. A team of 15 was going to make this worse, not better.
- **Profiles as named configurations.** Immutable, validated at startup. `orchestrator_reasoning` has `reasoning_effort: medium`. `retrieval_web_search` has `supports_web_search: True`. Adding a profile is a single-file change in `app/core/llm_profiles.py`.
- **Role policies as allowlists.** Each node role (`orchestrator`, `cleaning`, `retrieval`, etc.) has a default profile and an allowlist of profiles it's allowed to use. The orchestrator can write `selected_profiles` into graph state to override the default — but only within the allowlist. This is the seam that lets the orchestrator steer model selection at runtime without opening the door to arbitrary transport payloads.
- **Runtime as the single entry point.** `runtime.get_model_for_role("orchestrator", state=state, config=config)` returns a `BaseChatModel`. Tool binding, native web search, structured output — all go through the same runtime methods. One way to do it.
- **`LLM_PROFILES_OVERRIDE` for deploy-time flexibility.** A single JSON env var lets ops swap a model ID or tune params per environment without a code change. Validated at startup; invalid values fail fast with the specific profile ID named.
- **Documented as recipes, not reference.** `docs/llm-abstraction.md` is written as "how to wire a new node," "how to add a new profile," "how to enable web search" — oriented around what a junior engineer is trying to *do*, not what the code *is*.

---

## 6. TDD + Plan-Driven Development
*Maps to: "high test coverage", "frequent releases that incrementally build value", "mentor junior engineers"*

**The headline:** Every non-trivial change on this project starts with a written plan in `docs/superpowers/plans/` that lists tasks with checkbox tracking, failing tests first, then implementation, then passing tests, with explicit commit points. I use this process myself and expect the team to follow it.

**Key points:**

- **Plans before code.** Look at `docs/superpowers/plans/2026-04-14-redis-streaming-registry.md` (the branch I'm on right now) — it has a file-map table, 4 task groups, and within each task a strict sequence: *write failing test → run test and confirm it fails → implement → run test and confirm it passes → commit*. No code gets written until the plan is reviewed.
- **Test contracts stated before implementation.** The test assertions in the plan double as the requirements spec. "Stream should emit exactly 1 data event, not ≤1, to prove the first chunk emitted and the cancellation check fired on the second" is *in the plan*, before any code exists.
- **Commits scoped to single changes.** Each task group ends with a specific commit message in a specific format (`feature/MAIAE-146: <scope>`) — a convention I enforce because it makes PR review and rollback trivial.
- **Self-review section.** Every plan ends with a spec-coverage matrix: "requirement X → task that addresses it." Forces me to verify I actually covered the spec before handing the plan to the team or to an agent.

**Why this is mentoring.** When a junior engineer asks "how should I approach this?" the answer is not a conversation — it's *"read the last three plans in `docs/superpowers/plans/`, then write one for your work."* Scales where 1:1 pairing doesn't.

---

## 7. Risk-Minimising Engineering
*Maps to: "minimize risk", "secure, maintainable, correct"*

**The headline:** Several small-but-deliberate patterns across the codebase that reduce operational risk without adding framework complexity.

**Key points:**

- **Startup checks that fail fast.** `verify_dependencies()` tests Postgres and Redis connectivity during the FastAPI lifespan. If either is unreachable, the app refuses to start rather than failing silently on the first real request. Tests monkeypatch this so they don't need live infrastructure.
- **Checkpointer compiled in the lifespan, not at import.** `conversation_graph` is `None` until `compile_graph(checkpointer, runtime=runtime)` is called from the lifespan. This was a deliberate choice to prevent the graph from being usable without persistence — a silent no-persistence deployment would be a bad day, and this makes it impossible.
- **Message content extraction is defensive.** `_extract_text_content` in `orchestrator/nodes.py` handles both `HumanMessage` objects and dicts from the LangSmith UI, both string and list-of-parts content. The comment explains *why*: "in case of any future changes or other sources of messages." Not speculative defensiveness — scoped to known alternate callers.
- **Skills cache primed at startup.** `prime_skills_cache()` runs in the lifespan so the first request pays no skill-index I/O cost. A small latency win that also means the first user after a deploy doesn't get a slower response than everyone else.
- **Projection nodes between subgraphs.** The root graph explicitly narrows what flows out of each subgraph rather than letting LangGraph's default state-merge behaviour bloat the conversation state. This was a deliberate choice after seeing token usage grow turn-over-turn in early testing.

---

## Suggested Narrative Arc (30-minute interview)

1. **Opening (2 min)** — System context: who uses it (Medscape clinicians), what it does (structured, source-grounded answers streamed over SSE), what's novel (healthcare-safety-first generative AI).
2. **Leadership framing (4 min)** — Tech lead for a 15-person team on a CEO-priority initiative. How I drive architectural decisions: multiple options with trade-offs, recommendation, facilitated discussion, paper trail in `docs/superpowers/`.
3. **The three-generation product story (3 min)** — Copilot → Dify → engineered FastAPI+LangGraph service. Each migration was driven by the prior platform hitting its ceiling on something the product needed.
4. **Architecture (6 min)** — Multi-subgraph pipeline, plan-execute orchestrator split, LLM abstraction layer, streaming structured output. Focus on decisions, not boxes-and-arrows.
5. **Scale + self-audit story (6 min)** — The scalability assessment doc, the 8 findings, the priority matrix, and the Redis streaming registry work currently in flight (MAIAE-146) as the #1 fix.
6. **Healthcare AI safety (5 min)** — PII detection at the API boundary, orchestrator-callable guardrails tool, Athena proxy as the compliance plumbing.
7. **Closing (4 min)** — How this translates to Aledade: same shape of problem (healthcare + AI + PHI), same engineering mindset (risk-minimising, test-first, documented-trade-offs, mentoring at the codebase level), different clinical context.

---

## STAR-Format Answers for Likely Questions

### ==Q: "Tell me about a time you led a significant technical decision."==

**Situation.** We were preparing to add source-citation validation to the answer engine — every URL the LLM cited in its response had to be verified against the actual retrieval results, and unverifiable citations had to be redacted before the response reached the user. Healthcare-grade hallucination defence. The naive implementation would drop a `validate_urls` tool into the existing ReAct orchestrator and trust the LLM to call it. But that would leave citation validation as an *implicit* behaviour — governed by prompt and token probabilities rather than by system structure. For a healthcare answer engine, that's the wrong layer for a safety rule to live at.

**Task.** Decide how to restructure the orchestrator so that citation validation is *structural* — impossible to skip, not conditional on the LLM doing the right thing. Lead the team to an aligned decision without declaring it myself.

**Action.** I spent a day mapping the design space, then posted three candidate architectures to the team channel with pros and cons for each and my recommendation. The framing was: *"URL validation is a rule. In LangGraph, rules belong in edges, not in token probabilities. So it should be an edge, not a tool."* That single reframing changed what we were arguing about — no longer "where do we put the tool," but "what shape of graph makes the rule unskippable."

The three options I laid out:

1. **Orchestrator-generator** — keep the ReAct loop, have `model_rag` call `validate_urls` internally before returning. *Pro:* flexible iterative retrieval. *Con:* validation is still implicit, enforced by tool internals rather than by graph topology.

2. **Planner → executor → generator** — explicit planning node writes a typed plan, executor runs it with validation as a hard-wired edge after every `model_rag` step, redacted evidence written to a dedicated `validated_context` slot. *Pro:* validation is structural, per-node model configs become easy, plans are inspectable, parallel fan-out possible. *Con:* more moving parts, plans struggle when the next step depends on the previous step's return (fixable with a re-plan edge).

3. **Executor → validator → generator with controlled re-query loop** — no upfront planner; planning collapses into the executor's first iteration. Validator is a dedicated edge that runs deterministically and writes into a `validated_evidence` state slot. *Key structural move: the executor cannot reach the generator without going through the validator, because that's the only edge out.*

My lean was #3 — most ReAC turns need one, sometimes two or three retrieval calls, so a dedicated planner wasn't justified by the observed cost curve. I posted the full analysis, named my lean explicitly, and asked the team what they thought.

**Result.** The discussion that followed produced a refinement none of the three options had: we kept the planner–executor split from option #2 (because it gave us per-node model configs and inspectable plans) but collapsed the validation step into graph topology the way option #3 prescribed. The plan that came out of it is `docs/superpowers/plans/2026-04-10-plan-execute-architecture.md`, which is now in implementation. The outcome — citation validation as a structural edge, not a tool call — is better than any of the three options I started with, because the team pressure-tested my analysis and found a combination I'd missed. That's the pattern: I bring multiple options with honest trade-offs and a named recommendation, the team engages with the actual substance, and we often end up somewhere better than any single starting option. Every significant architectural decision on this project works this way.


---

### Q: "Tell me about a time you identified a serious risk in a system you'd built."

**Situation.** The `/runs/stream` endpoint was working well in development — async-native, SSE, streaming LangGraph output token-by-token. But I was preparing to socialise a plan to move toward multi-worker deployment and higher target concurrency (200–1,000 simultaneous streams). I didn't trust the system to actually handle that yet.

**Task.** Audit my own system as if I were a reviewer who'd never seen it before, and produce a document the team could execute against.

**Action.** I read the entire request path — routes, streaming registry, startup checks, graph compilation, state management — with one question in mind: "what breaks at 200 concurrent streams that works fine at 2?" I found 8 issues. Some were hard blockers (in-process `StreamingRegistry` silently breaks across worker processes; no DB connection pool means `max_connections` exhaustion at ~100 streams; no rate limiter means OpenAI TPM exhaustion before infrastructure saturates). Others were correctness risks (graph compiled without a checkpointer guard; mutable global LLM state). I wrote it up as `docs/API_SCALABILITY_ASSESSMENT.md` with a priority matrix showing severity at 200 vs. 1,000, fix complexity, and a recommended fix order.

**Result.** The team had a concrete execution plan instead of a vague sense of "we should make it more scalable." I'm currently on the first fix — branch MAIAE-146 replaces the in-process registry with a Redis-backed `RedisStreamingRegistry` that works across worker processes and re-enables the Redis startup check so the app fails fast if Redis is down. The assessment doc is the single clearest artifact on the team that I own this system end-to-end and can see its limits. More importantly, the *habit* — audit your own systems, write it down, prioritise, execute — is now how we approach production-readiness on this project.

---

### Q: "Tell me about a time you removed complexity from a system."

**Situation.** The orchestrator originally ran as a single ReAct loop — the LLM had all tools bound to it (`model_rag`, `select_skills`), decided which to call each turn, and looped back to itself after tool execution. In practice this meant the LLM sometimes re-called retrieval "to be sure," sometimes skipped skill selection entirely, and hit an OpenAI message-sequence constraint that made the loop fragile. Retrieval behaviour was non-deterministic for a healthcare answer engine, which is exactly the wrong tool.

**Task.** Make retrieval deterministic without losing the benefit of LLM-driven reasoning about *what* to retrieve.

**Action.** I split the orchestrator into two phases. **Planning** — the LLM is bound only to `select_skills` + `create_plan`, where `create_plan` accepts a typed `list[dict]` of `{"tool": ..., "args": ...}` steps. The LLM decides what to retrieve and writes the plan to graph state. **Execution** — a new `execute_plan_node` reads the plan and calls retrieval functions directly as plain Python, bypassing the `@tool` wrapper and its `InjectedState` machinery. The LangGraph `ToolNode` still runs between the two to satisfy OpenAI's AIMessage → ToolMessage protocol, but it only handles the planning tools, which are side-effect-free. Plan doc: `docs/superpowers/plans/2026-04-10-plan-execute-architecture.md`, test-driven task-by-task.

**Result.** Retrieval is now deterministic — given the same plan, the same tools run with the same args. The LLM can't re-invoke retrieval "to be sure" because it no longer holds the wheel during execution. The OpenAI message-sequence constraint disappeared as a failure mode. And because the plan is typed and in graph state, it's inspectable in LangSmith and testable in isolation. Three problems solved with one structural change.

---

### Q: "Tell me about a time you made a codebase easier for other engineers to work with."

**Situation.** As the team grew past a handful of engineers, I noticed LLM wrappers spreading. Every new tool author was creating their own thin wrapper around `ChatOpenAI` or the Anthropic SDK, each with slightly different conventions — different param handling, different tool-binding styles, different ways of enabling web search. It was DRY-violating at the code level, but the real problem was that every new wrapper became one more thing a junior engineer had to figure out before they could add a tool. This was friction I was going to pay every time we onboarded someone.

**Task.** Collapse the sprawl into a single way to access models, without sacrificing the runtime flexibility the orchestrator needed (it had to be able to pick different models for different downstream nodes).

**Action.** Designed a three-layer abstraction: (1) a **profile registry** of immutable named model configurations (`orchestrator_reasoning`, `retrieval_web_search`, etc.); (2) **role policies** that give each node role an allowlist of profiles it may use and a default; (3) a **runtime resolver** that hands back a ready-to-use `BaseChatModel` for a given role, with tool binding, web search, and structured output all going through the same runtime methods. The orchestrator steers model selection at runtime by writing `selected_profiles` into graph state — bounded by the role's allowlist so it can't request a profile the role wasn't designed for. Deploy-time overrides go through a single `LLM_PROFILES_OVERRIDE` env var, validated at startup.

**Result.** One way to get a model. One file to change to add a profile (`app/core/llm_profiles.py`). One file to change to let a role use a new profile. One env var to swap a model in production without a code change. And — the part I care about most — `docs/llm-abstraction.md` is written as how-to recipes oriented around what an engineer is *trying to do*: wire a new node, add a profile, enable web search, use structured output. A new engineer can add a tool without asking me. That's mentoring that scales.

---

### Q: "Tell me about a time you had to balance engineering cost against product needs."

**Situation.** The UI needs to show a streaming human-readable summary as tokens arrive *and* receive structured metadata (sources, related articles, follow-up questions) from the same response. The obvious implementation is two LLM calls — one for the streaming summary, one for the structured metadata. Clean separation of concerns, but doubles the cost and the latency-to-structured-metadata for every query. The product target is answer latency, not compute cost, but at sustained volume this choice compounds.

**Task.** Get both outputs from a single LLM call without the UI ever seeing a malformed partial response.

**Action.** Designed a tagged-output protocol: the orchestrator prompt instructs the model to emit the summary wrapped in `@@start_summary@@ ... @@end_summary@@` tags followed by a JSON block. Built `StreamStructuredOutputParser` in `app/graphs/orchestrator/structured_output.py` to feed token chunks in as they stream, emit visible summary text immediately, and parse the JSON tail at the end. The parser implements a **holdback buffer** — if the tail of the current buffer could be a prefix of `@@end_summary@@` or another tag, it holds those characters back until the next chunk arrives rather than emitting them. Prevents the UI from ever flickering a partial tag. The SSE layer fans the single parsed response out into typed events — `data`, `source`, `related_articles`, `follow_up_question`, `end` — so the frontend binds different handlers to each without any knowledge of the tagged-output protocol.

**Result.** Single LLM call per turn instead of two. The tagged protocol is simple enough that prompt engineering for it takes one paragraph in the orchestrator prompt. The parser is covered by tests that feed it chunks byte-by-byte to prove tag-boundary safety under any chunk size. And the frontend contract — typed SSE events — is independent of the tagged-output protocol, so the protocol could change later without touching the UI.

---

### Q: "Tell me about a time you made a system more reliable in a subtle way."

**Situation.** The root graph wires four subgraphs (`guardrails` → `history_detection` → `clean` → `orchestrator`) sharing a single `OrchestratorState` as their type. LangGraph's default behaviour is to merge subgraph outputs back into the root state, which meant every subgraph's full output — including the growing `messages` list — was being projected back into the next subgraph's input. In early testing I noticed token usage growing turn-over-turn faster than the actual message count could explain.

**Task.** Stop the state bloat without changing the graph topology or the subgraph interfaces.

**Action.** Added explicit **projection nodes** between subgraphs in `app/graphs/graph.py`. Each projection node reads the subgraph's full output, picks out only the fields that need to flow forward, and returns that narrowed dict. The inline comment names the reason: *"we have to do this dance of projection nodes to prevent the full state (especially messages) from echoing back at each step, which would be very inefficient for the LLM to process and cause token bloat in the state history."* Also reset the orchestrator's `iterations` counter inside its projection node — otherwise multi-turn threads accumulated iterations from prior turns and hit the safety cap (10) prematurely, silently capping the agent loop on turns 2+.

**Result.** Token usage per turn stopped growing in the conversation-state dimension. The safety cap now fires on actual runaway loops, not on multi-turn conversations. And because the projection nodes are named and commented, the next engineer who touches this subgraph boundary will understand *why* the dance exists rather than "simplifying" it.

---

## Quick-Reference Talking Points

*(No production numbers yet — performance analysis and load testing are scoped as the next major workstream after the scalability fixes land.)*

| Item | Value |
|---|---|
| Team size | 15 engineers |
| Organisational priority | #1 CEO priority for Internet Brands |
| Product generation | 3rd (Copilot → Dify → current FastAPI + LangGraph) |
| Target concurrency | 200–1,000 simultaneous SSE streams |
| Subgraph count | 4 (guardrails, history detection, cleaning, orchestrator) |
| Scalability findings in self-audit | 8, prioritised by severity + fix complexity |
| PII detection classes | 44 across 17 languages |
| Compliance plumbing | All LLM traffic through internal Athena LiteLLM proxy |
| Max ReAct iterations (safety cap) | 10 |
| LLM access pattern | Profile registry + role policies + runtime resolver |
