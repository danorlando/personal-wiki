

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

### How I lead architectural decisions on this team

I don't hand down decisions. When we hit a new challenge, I:

1. **Work up multiple candidate solutions** with the trade-offs, pros, and cons of each.
2. **Present them to the team with a recommendation**, but frame it as a decision the group is making, not one I've already made.
3. **Facilitate the discussion** until the team naturally converges on the best option for the current constraints.

I've found this is the fastest path to real buy-in. People execute well on decisions they helped shape; they execute reluctantly on decisions they were handed. On a 15-person team with junior engineers who need to own their pieces, that distinction compounds.


### Why this matters for the Aledade role

The role description specifically calls out *"partner, as a peer, with Engineering Managers, Product Managers, and stakeholders"* and *"act as a trusted technical decision-maker."* That is the exact shape of what I do on this team every day. The engineering content below is evidence for that claim — but the claim itself is the headline.

---

### Q: "Tell me about a time you had to rethink an architecture that wasn't working."

*Best answer: the orchestrator evolution — V1 multi-agent → V2 BaseAgent pipeline → current ADK-native SequentialAgent + LoopAgent.*

**Situation.** The original orchestrator coordinated three independent agents (summarization, evaluation, workflow-manager) that communicated through subagents-as-tools. Each agent frequently made 2+ LLM calls to complete its task, and the overall workflow had high runtime variability — sometimes a few minutes, sometimes much longer — which made SLA compliance impossible and debugging a nightmare. Non-determinism was baked into the architecture, not introduced by prompts.

**Task.** Reduce runtime variability to something predictable enough to meet SLAs, without sacrificing the quality that the iterative refinement loop provided.

**Action.** I tackled this in two phases rather than one big rewrite. **V2** consolidated the multi-agent logic into a single orchestrator that extended ADK's `BaseAgent` and called Python functions directly instead of going through LLM-driven tool orchestration for every step. That eliminated most of the redundant LLM calls and gave me determinism — but I hit a wall when I realized the `BaseAgent` extension pattern is explicitly discouraged by ADK documentation. Extending it means taking on maintenance of orchestration mechanics that the framework already provides. **V3 (current)** switched to ADK's native `SequentialAgent + LoopAgent` pattern: `SequentialAgent(InitialSummaryAgent, LoopAgent(EvaluationAgent, RefinementAgent))`, with loop exit controlled by `tool_context.actions.escalate = True`. The agent hierarchy *is* the control flow — no custom logic, no BaseAgent workaround.

**Result.** Runtime is now predictable and within SLA. Code surface area dropped significantly — the current `orchestrator.py` is a fraction of the size of the archived V1. But the more valuable outcome is the paper trail: both prior versions are archived in `modules/routing/archives/` with headers documenting what failed and why, so the next engineer who's tempted to add "just one more agent" has a concrete record of why that approach was abandoned.

---
### Q: "Tell me about a time you had to balance cost, quality, and latency."

*Best answer: adaptive refinement model selection.*

**Situation.** In homepage (cold-start) mode, when a generated topic card failed evaluation, the refinement step regenerated it using the same model as the initial pass (`gpt-5-mini`). This was suboptimal in two directions at once — sometimes we needed a stronger model to actually fix the problem, and sometimes we were overpaying to fix something trivial.

**Task.** Route the refinement model to the failure mode, without adding complexity to the agent hierarchy or sacrificing the determinism of the ADK loop pattern.

**Action.** I classified failures into two categories based on which evaluation metric tripped. *Content-integrity* failures (faithfulness, hallucination, source presence) mean the content itself is factually unreliable — those need `gpt-5.1` because the extra capability materially improves the retry's success rate. *Structural* failures (article_structure, word count, short paragraphs) are formatting corrections that `gpt-4o-mini` handles reliably at a fraction of the cost. I implemented this as a state-driven override: the evaluation pipeline writes `summarization_model` to `tool_context.state` before the refinement agent runs, and the existing `generate_summary_with_pipeline` tool already reads the model from state at runtime. Zero changes to the agent hierarchy, zero new ADK primitives.

**Result.** The system now spends the stronger model's budget only on retries that actually need it. Scoped the feature to homepage mode specifically — user-mode content is individually tailored and the existing single-model approach is sufficient, so expanding the feature there would be added complexity without a proportional quality gain. Documented the rationale in the design doc so the scoping decision is defensible, not arbitrary.


