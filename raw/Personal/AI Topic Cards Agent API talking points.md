## System Context — "What It Is"

### The upstream system

An ML service generates **personalized topic recommendations** for each user, ranked from a combination of:

- User profile data (specialty, experience level, role)
- Lead concepts (clinical areas they've engaged with)
- Claims data (what they actually see in practice)
- Recent browsing history and usage of other AI features
- Specialty-level priors

The output of that system is, for each user, an ordered list of _topics_ — each with a set of source articles that justify why the topic is relevant to this person.

### What this system does

**The Topic Cards Agent API is the content generation layer that sits downstream of that recommender.** For each `(user, topic, source articles)` tuple:

1. **Pulls the topic, its source articles, and the full personalization payload** from the upstream system's database.
2. **Generates a personalized topic card** — a structured summary of the source material, tailored to that specific user's specialty, experience level, and preferences.
3. **Evaluates quality with a multi-metric pipeline** (faithfulness, relevance, coherence, fluency, usefulness, structural checks) and iteratively refines until it meets a quality bar.
4. **Persists the completion, metrics, and review data** so the upstream system and downstream analytics can close the loop.

**The headline:** the ML system decides _what_ each user should see; this system decides _how_ to present it. Ranking is useless if the content itself is generic, inaccurate, or pitched at the wrong level — this layer is what makes personalization actually felt by the end user.

### Suggested 2-sentence opener

> "I designed and built a generative AI service that sits downstream of an ML recommender. The recommender decides which clinical topics are most relevant to each user based on their specialty, claims, browsing, and lead concepts — my service takes each recommended topic plus its source articles and generates a personalized, clinically accurate summary tailored to that specific user, with a multi-agent evaluation loop ensuring the output meets a quality bar before it's persisted."


---

  

## Architectural Evolution — Iteration as Senior-Level Signal

One of the strongest artifacts in this repo is `modules/routing/archives/`, which preserves two prior generations of both the orchestrator and the evaluation pipeline, each with header comments explaining what failed and why. **This is worth calling out explicitly in the interview** — it demonstrates that the current design isn't the first thing that came to mind, it's the survivor of measured iteration.

### Orchestrator evolution
  
| Version          | Architecture                                                                                                                        | Why it was replaced                                                                                         |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| V1               | Three independent agents (summarization, evaluation, workflow-manager) communicating via subagents-as-tools; 2+ LLM calls per agent | Highly variable runtime, SLA violations, opaque debugging, non-deterministic workflow                       |
| V2               | Single orchestrator extending ADK's `BaseAgent` with direct Python function calls                                                   | `BaseAgent` extension pattern explicitly discouraged by ADK docs; ADK-native primitives make it unnecessary |
| **V3 (current)** | ADK-native `SequentialAgent → LoopAgent(Evaluator, Refiner)` with `escalate=True` exit                                              | Officially supported, deterministic, predictable runtime, agent hierarchy *is* the control flow             |

### Evaluation pipeline evolution

| Version          | Architecture                                                                                | LLM calls / eval            | Why it was replaced                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------- | --------------------------- | --------------------------------------------------------------------------------------------------- |
|                  |                                                                                             |                             |                                                                                                     |
| V1               | LlmAgent with 6 individual metric tools; agent reasons about which to call                  | 7–10+                       | Agent sometimes re-called metrics "to be sure"; 200+ line prompt to govern behavior; 15–25s runtime |
| V2               | Single `run_evaluation_pipeline` tool (parallel Python) + `FinalDecisionAgent` for approval | 1–2                         | Decision agent added an unnecessary LLM call; JSON parsing added another failure surface            |
| **V3 (current)** | Parallel Python metric execution + deterministic `calculate_approval()`                     | 0 (for the decision itself) | Debuggable, predictable, ~38% cost savings from early exit on gating failure                        |

**The talking point:** senior engineering is not about arriving at clever architectures on the first try — it's about measuring what you have, identifying the specific failure mode, and iterating. The archives document that process in a way that's reviewable by anyone who joins the team.

---
## 1. Multi-Agent LLM System Architecture

*Maps to: "Architect systems to enhance AI models"*

**The headline:** Designed a production medical-summarization system on Google's Asterix ADK using a `SequentialAgent → LoopAgent(Evaluator, Refiner)` pattern that produces clinically accurate topic cards through iterative self-correction — arrived at after two prior architectures were tried, measured, and replaced.

**Key points:**
- **Arrived at the current design through two prior iterations, both archived in the repo with lessons-learned headers.** V1 used independent multi-agent orchestration with subagents-as-tools, which produced high runtime variability and made SLA compliance impossible. V2 consolidated into a pipeline but extended `BaseAgent` in a way ADK explicitly discourages. Current production uses ADK's native `SequentialAgent + LoopAgent` pattern — officially supported, deterministic, and the agent hierarchy is the control flow.
- **Deterministic control flow over agent autonomy.** Deliberately chose ADK's built-in loop primitive with an `escalate=True` exit signal rather than letting an LLM decide when to stop. Non-deterministic agents are the wrong tool for a healthcare pipeline where reproducibility matters.
- **State-based parameter passing .** Removed dynamic model-router agents and switched tools to read inputs from `tool_context.state` instead of the LLM passing parameters through function calls. Result: ~1–2s latency saved per request, lower token usage, more deterministic behavior.
- **Personalized vs. cold-start modes** with mutual exclusivity validation — the system routes on `global_user_id` vs. `homepage_id` to serve either individually tailored content or specialty-level baseline content for new users where the upstream recommender has no signal.

---

  

## 2. Prompt Engineering & Evaluation as Infrastructure

*Maps to: "Design and implement prompt engineering strategies"*

**The headline:** Treated evaluation as a first-class subsystem, not an afterthought, using DeepEval with a **two-phase gating/quality pipeline** that achieves ~38% cost savings through early exit — again arrived at by eliminating LLM calls from earlier agentic designs.

**Key points:**

- **Three-generation evolution archived in the repo.** V1 was a fully agentic evaluator where an LLM decided which metrics to call, sometimes re-calling the same metric if it "felt uncertain" — 7–10+ LLM calls per evaluation, 200+ line instruction prompt, non-deterministic execution time. V2 consolidated to a single pipeline tool with a `FinalDecisionAgent` that made approval decisions via LLM reasoning — better, but the decision LLM call was still an unnecessary cost. The current design runs metrics as parallel Python functions and replaces the decision agent with a deterministic `calculate_approval()` function. **1–2 LLM calls per evaluation, predictable runtime, easier to debug.**

- **Gating metrics run first** (faithfulness, relevance) — if factual accuracy fails, the pipeline short-circuits before spending money on quality metrics. This is the ~38% cost savings.

- **Weighted scoring** (usefulness 0.40, fluency 0.30, coherence 0.30) with a configurable `eval_cutoff` threshold of 0.65 that encodes the quality bar as data, not code.

- **Adaptive refinement model selection:** when a rejection is a *content-integrity* failure (hallucination/faithfulness), the refiner swaps in GPT-5.1; when it's a *structural* failure (word count, paragraph formatting), GPT-4o-mini suffices. Routes compute where it actually improves outcomes — a cost-for-quality decision made per-failure-mode, not per-request.

---

## 3. Defensive Correctness — Two-Stage JSON Recovery

*Maps to: "secure, maintainable, correct"*

**The headline:** LLM output is structurally unreliable. Built a two-stage validation recovery pattern so a malformed JSON response doesn't burn an entire workflow iteration.

**Key points:**

- **Stage 1 — `json-repair`:** deterministic, no API cost, handles the common failure modes (trailing commas, unescaped quotes).

- **Stage 2 — LLM feedback loop:** up to 2 retries with formatted Pydantic validation errors fed back into the prompt so the model can correct itself.

- Capped at 2 retries because "diminishing returns, wasted API calls" — a concrete budget, not an infinite loop.

This directly mirrors Aledade's "minimize risk, high test coverage" language.

---

## 4. Scalability & Throughput Design

*Maps to: "scalable and performant solutions"*

**The headline:** Authored a throughput analysis report and PRD proposing a **Celery + Redis** migration, and — critically — pushed back on the naive 1:1 GUID-to-worker design.

  

**Key points:**

  

- **Identified the wrong default.** Celery's prefork model creates a ~100–200MB OS process per task. For an I/O-bound async workload (LLM calls + DB), that's wasted isolation.

- **Counter-design:** each worker processes a *chunk* of GUIDs inside a single event loop with `asyncio.gather`. Result: 10 workers hit the 6-hour SLO for 10k GUIDs/week where the original design needed 30+ — **~65% infrastructure reduction** for the same throughput.

- **Production targets:** 150k GUIDs initial rollout (~1M topics), 70k topics/week sustained, ~9 LLM calls/topic, ~29 calls/sec. Sized the system against those numbers, not against vibes.

  

---

  

## 5. Technical Decision-Maker / Mentoring Artifacts

*Maps to: "trusted technical decision-maker", "mentor junior engineers"*

  

**The headline:** Every non-obvious choice is documented with a *why*, not just a *what*. `docs/` contains PRDs, design docs, and an architecture review — artifacts a junior engineer can read to understand not just the code but the reasoning behind it.

  

**Examples:**

  

- **Model selection rationale:** GPT-5-mini for summarization (validated by user testing against IB GPT prototypes), GPT-4o-mini for evaluation (narrow, well-defined tasks where cost/latency win), GPT-5.1 for content-integrity refinement (where the extra capability actually moves the needle).

- **CLAUDE.md "Do Not" list** — encodes past mistakes (e.g., dual-write anti-pattern to `tool_context.state` + `session.state`, deprecated `workflow_orchestrator.py`) as enforceable rules for future contributors.

- **Known issues documented honestly** — e.g., batch head-of-line blocking when 1 of N topics requires refinement. Name the problem and propose the solution (queue-based dynamic batching) rather than hiding it.

  

---

  

## 6. Healthcare Compliance Awareness

*Maps to: "Maintain the security of protected patient health information"*

  

**The headline:** All LLM traffic is routed through the internal **Athena API Proxy** rather than calling OpenAI directly. That's the compliance boundary — prompts and completions transit an approved internal gateway, not the public API, which matters enormously in a HIPAA context.

  

Combined with `.env` discipline (no keys in git, separate dev/prod keys enforced in CLAUDE.md), this is the kind of plumbing-level security posture Aledade's description calls out explicitly.

  

---

  

## Suggested Narrative Arc (30-minute interview)

  

1. **Opening (2 min)** — System context: upstream ML recommender → this system generates the content → persisted for user consumption and analytics.

2. **Architectural evolution (5 min)** — Briefly describe the V1 → V2 → V3 journey for both the orchestrator and evaluation pipeline. This is the single strongest signal of senior judgment — lean into it.

3. **Architecture (6 min)** — ADK orchestrator pattern, why deterministic control flow, state-based parameter passing.

4. **Quality/cost engineering (6 min)** — Two-phase evaluation, early exit, adaptive refinement model selection, JSON validation recovery.

5. **Scale story (7 min)** — Throughput analysis, Celery PRD, the 30→10 worker insight.

6. **Closing (4 min)** — How this translates to healthcare AI at Aledade: compliance via proxy, observability via structured logging, mentoring via documented tradeoffs and archived reference implementations.

  

---

  

## STAR-Format Answers for Likely Questions

  

### Q: "Tell me about a hard technical decision you made."

*Best answer: the Celery batched-worker redesign — it's a decision where you pushed back on an existing design.*

  

**Situation.** The team had drafted a PRD to move batch topic card generation from synchronous HTTP (with client-side `asyncio.Semaphore` concurrency) to a Celery + Redis task queue. The goal was fault tolerance, job visibility, and backpressure for a weekly workload of 10,000 GUIDs (~70,000 topics) that needed to finish in under 6 hours, with an initial rollout of 150,000 GUIDs (~1M topics).

**Task.** Review the design and validate whether the proposed architecture would actually hit the throughput target within a reasonable infrastructure budget. The initial PRD mapped one GUID to one Celery task, 1:1.

**Action.** I ran a throughput analysis against the real workload characteristics. Two things jumped out: (1) the orchestrator was already fully async and I/O-bound — each workflow spends its time waiting on LLM API responses and DB queries, not consuming CPU; (2) Celery's default prefork model allocates a ~100–200MB OS process per task. Mapping 1 GUID to 1 process wasted that isolation because the event loop inside each worker would be idle most of the time. I proposed a counter-design where each Celery task processes a *chunk* of GUIDs concurrently within a single event loop using `asyncio.gather`, preserving Celery's fault-tolerance and visibility benefits but matching the work unit to how the code actually spends its time. I wrote up the analysis as a standalone throughput report with the math (~29 LLM calls/sec sustained, 1000 PG connections available, Enterprise Tier 5 OpenAI limits) so the tradeoffs were reviewable.

  
**Result.** The batched design hit the 6-hour SLO with 10 workers instead of 30+ — roughly a 65% reduction in container count and memory footprint for the same throughput. More importantly, the decision was documented with reasoning that a future engineer (or me, six months from now) can re-derive rather than having to take on faith.


---

### Q: "Tell me about a time you had to balance cost, quality, and latency."

*Best answer: adaptive refinement model selection.*

**Situation.** In homepage (cold-start) mode, when a generated topic card failed evaluation, the refinement step regenerated it using the same model as the initial pass (`gpt-5-mini`). This was suboptimal in two directions at once — sometimes we needed a stronger model to actually fix the problem, and sometimes we were overpaying to fix something trivial.

**Task.** Route the refinement model to the failure mode, without adding complexity to the agent hierarchy or sacrificing the determinism of the ADK loop pattern.

**Action.** I classified failures into two categories based on which evaluation metric tripped. *Content-integrity* failures (faithfulness, hallucination, source presence) mean the content itself is factually unreliable — those need `gpt-5.1` because the extra capability materially improves the retry's success rate. *Structural* failures (article_structure, word count, short paragraphs) are formatting corrections that `gpt-4o-mini` handles reliably at a fraction of the cost. I implemented this as a state-driven override: the evaluation pipeline writes `summarization_model` to `tool_context.state` before the refinement agent runs, and the existing `generate_summary_with_pipeline` tool already reads the model from state at runtime. Zero changes to the agent hierarchy, zero new ADK primitives.

**Result.** The system now spends the stronger model's budget only on retries that actually need it. Scoped the feature to homepage mode specifically — user-mode content is individually tailored and the existing single-model approach is sufficient, so expanding the feature there would be added complexity without a proportional quality gain. Documented the rationale in the design doc so the scoping decision is defensible, not arbitrary.

  

---

  

### Q: "Tell me about a time you made a system more reliable."

*Best answer: two-stage JSON validation recovery.*

**Situation.** The system depends on the LLM emitting structured JSON that conforms to a Pydantic schema. In practice, models occasionally emit malformed JSON (trailing commas, unescaped quotes, truncated output) or schema-valid JSON with missing/invalid fields. Each failure was burning an entire refinement iteration — a full regeneration costing ~9 LLM calls for what was really just a syntax problem.

**Task.** Recover from output-format failures without losing an iteration of the expensive evaluation/refinement loop, and without building an unbounded retry loop.

**Action.** Built a two-stage recovery pattern inside `generate_summary_with_pipeline`. **Stage 1** runs the output through the `json-repair` library — deterministic, no API cost, and handles the overwhelming majority of syntax-level failures (trailing commas, missing brackets). **Stage 2** only kicks in if repair fails or the JSON parses but fails Pydantic validation: format the validation errors into a feedback message, append it to the instruction, and retry the generation. Capped retries at 2 because the cost curve flattens quickly — three attempts at syntax recovery is diminishing returns on wasted API calls.

**Result.** The common failure modes — the ones that used to burn a full iteration — now recover with no API cost via `json-repair`. The harder structural failures get at most two self-corrections with specific, actionable feedback rather than a silent re-roll. The retry budget is explicit and documented in CLAUDE.md's "Do Not" list (`max_validation_retries >3` is called out as an anti-pattern) so a future engineer doesn't quietly turn the knob up and wonder why costs spiked.


---

  

### Q: "Tell me about a time you mentored another engineer or influenced team practices."

*Best answer: the CLAUDE.md "Do Not" list as codified lessons learned.*

  

**Situation.** As the system evolved through several architectural shifts (the old `workflow_orchestrator.py` → ADK-based `orchestrator.py`, dynamic model-router removal, state-based parameter passing), the codebase accumulated patterns that looked plausible but were actively harmful — e.g., writing state to both `tool_context.state` and `session.state` (the ADK dual-write anti-pattern), or adding custom loop logic instead of using ADK's `LoopAgent` with `escalate`. Each of those mistakes had cost me real debugging time, and anyone new to the codebase — human or AI coding assistant — was likely to repeat them.

  

**Task.** Make those lessons enforceable so future contributors don't re-learn them the hard way.

  

**Action.** Built CLAUDE.md as a living instruction file with an explicit "Do Not ⛔" section organized by domain (Architecture, Evaluation, Validation, Environment, Dependencies). Each rule states the prohibition and the reason — e.g., "Do not write to both `tool_context.state` AND `session.state` (ADK anti-pattern)" — so a reader can judge edge cases rather than blindly following. Paired that with a "Common Tasks" section pointing at the canonical place to read before touching each subsystem (adding a metric, debugging evaluation, modifying workflow logic) and a "Known Issues" section that names problems honestly rather than hiding them.

  

**Result.** The document is now the first thing anyone — teammate or AI assistant — reads when they touch the repo. Architectural decisions that used to live in Slack threads or in my head are checked-in artifacts that survive context compression, team turnover, and the next person who thinks "surely I can just write to session state directly." It's mentoring at the codebase level rather than the 1:1 level, which scales where pairing doesn't.

  

---

  

### Q: "Tell me about a time you had to rethink an architecture that wasn't working."

*Best answer: the orchestrator evolution — V1 multi-agent → V2 BaseAgent pipeline → current ADK-native SequentialAgent + LoopAgent.*

**Situation.** The original orchestrator coordinated three independent agents (summarization, evaluation, workflow-manager) that communicated through subagents-as-tools. Each agent frequently made 2+ LLM calls to complete its task, and the overall workflow had high runtime variability — sometimes a few minutes, sometimes much longer — which made SLA compliance impossible and debugging a nightmare. Non-determinism was baked into the architecture, not introduced by prompts.

**Task.** Reduce runtime variability to something predictable enough to meet SLAs, without sacrificing the quality that the iterative refinement loop provided.

**Action.** I tackled this in two phases rather than one big rewrite. **V2** consolidated the multi-agent logic into a single orchestrator that extended ADK's `BaseAgent` and called Python functions directly instead of going through LLM-driven tool orchestration for every step. That eliminated most of the redundant LLM calls and gave me determinism — but I hit a wall when I realized the `BaseAgent` extension pattern is explicitly discouraged by ADK documentation. Extending it means taking on maintenance of orchestration mechanics that the framework already provides. **V3 (current)** switched to ADK's native `SequentialAgent + LoopAgent` pattern: `SequentialAgent(InitialSummaryAgent, LoopAgent(EvaluationAgent, RefinementAgent))`, with loop exit controlled by `tool_context.actions.escalate = True`. The agent hierarchy *is* the control flow — no custom logic, no BaseAgent workaround.

**Result.** Runtime is now predictable and within SLA. Code surface area dropped significantly — the current `orchestrator.py` is a fraction of the size of the archived V1. But the more valuable outcome is the paper trail: both prior versions are archived in `modules/routing/archives/` with headers documenting what failed and why, so the next engineer who's tempted to add "just one more agent" has a concrete record of why that approach was abandoned.

  
---

  

### Q: "Tell me about a time you removed complexity from a system."

*Best answer: the evaluation pipeline V1 → V2 → current evolution.*

  
**Situation.** The original evaluation agent was a fully agentic design — an LlmAgent with 6 individual metric tools (faithfulness, hallucination, relevance, coherence, fluency, usefulness) that used natural-language reasoning to decide which metrics to call and when. In practice, this meant 7–10+ LLM calls per evaluation just for tool orchestration, a 200+ line instruction prompt to keep the agent behaving, and — worst of all — the agent would sometimes re-call the same metric if it "felt uncertain" about the result. Evaluation time was non-deterministic and costs were unpredictable.

  
**Task.** Reduce evaluation cost and latency without losing the quality signal that the multi-metric approach provided.

  

**Action.** Again split into two phases. **V2** consolidated the 6 metric tools into a single `run_evaluation_pipeline` tool that executed all metrics as parallel Python functions (no LLM orchestration) and implemented early-exit: if gating metrics failed, skip the quality metrics entirely. The agent wrapper shrank from 200+ lines to ~100 and dropped to 1–2 LLM calls. **V3 (current)** went further — the V2 agent still made the approval decision via LLM reasoning and JSON output, which was another LLM call and another parsing surface. I replaced it with a deterministic `calculate_approval()` Python function that makes approval decisions based on gating results, word count, and per-metric thresholds. The agent wrapper now exists almost entirely to satisfy ADK's pattern expectations; the real work is in deterministic code.

  

**Result.** ~38% cost savings on rejected summaries from early exit alone. Evaluation runtime went from 15–25s (V1 sequential metric calls) to 6–10s (parallel + early exit). Total token usage dropped from ~15–20K per evaluation to ~5–8K. But the win I care about most is *debuggability* — when evaluation produces a surprising result now, I read three Python functions and a results dict, not a 200-line prompt and a tool-call trace. The comment in the archive says it plainly: "This may be revisited post-MVP if more nuanced approval decisions are needed." That's a scoping decision, not a refusal — if the product ever needs weighted overrides or margin tolerance, the V2 `FinalDecisionAgent` is right there as a reference.

  

---

  

### Q: "Tell me about a time you had to integrate with an existing system."

*Best answer: the upstream recommender integration and mode-based routing.*

  

**Situation.** This service is the content generation layer downstream of an ML recommender. The recommender ranks topics per user using profile data, lead concepts, claims data, and browsing history; this service has to pull each recommended topic and its source articles, generate a personalized summary, and persist the result back into the shared database in a format the frontend can consume. Upstream contract: two different identifier types (`global_user_id` for personalized mode, `homepage_id` for cold-start) and an articles array for direct input / testing. Each mode has different personalization semantics.

  

**Task.** Support all three modes without ambiguity, without forking the pipeline, and without leaking mode-specific logic into every agent.

  

**Action.** Enforced mutual exclusivity at the request level — a `WorkflowRequest` must specify exactly one of `global_user_id`, `homepage_id`, or `articles`; validation rejects requests that set more than one. Mode gets resolved once at the entry point into an `is_homepage_mode` state flag, and downstream agents read from state rather than branching on request shape. The frontend needs a complex nested JSON structure (title, CTA, paragraphs with inline citations, enriched references) that would be fragile to ask the LLM to emit directly, so I added a post-generation `schema_transform` layer — the LLM emits a simpler `LlmTopicCard` schema, and a deterministic transform enriches it into `FrontendTopicCard` using article metadata from the database.

  

**Result.** Adding cold-start mode (MTOPICS-154) was a localized change — request validation, mode detection, and the adaptive refinement feature I mentioned — without touching the summarization agents themselves. The schema transform layer means frontend format changes don't require prompt changes, and prompt changes don't risk breaking the frontend contract. Two independent concerns, two independent change surfaces.

  

---

  

## Quick-Reference Numbers

  

| Metric | Value |

|---|---|

| Weekly production target | 10,000 GUIDs / ~70,000 topics in < 6 hours |

| Initial rollout | 150,000 GUIDs / ~1M topics |

| Avg LLM calls per topic | ~9 (weighted avg across approve/refine/gate-fail paths) |

| Avg topic processing time | ~90 seconds |

| Early-exit cost savings | ~38% |

| Worker reduction (Celery redesign) | 30+ → 10 (~65% infra savings) |

| Evaluation threshold | 0.65 weighted score, 0.5 per-metric floor |

| Word count window | 250–450 words |

| Metric weights | usefulness 0.40, fluency 0.30, coherence 0.30 |