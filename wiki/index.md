---
updated: 2026-04-26
---

# Wiki Index

## Sources

- [[sources/alphaevolve-complexity-theory]] — AlphaEvolve discovers gadget reductions & Ramanujan graphs, yielding new complexity theory theorems (2025-09-29)
- [[sources/advent-of-claude-31-days]] — 31 Claude Code tips from beginner shortcuts to advanced agent patterns (2025-12-31)
- [[sources/claude-code-how-we-use-skills]] — Anthropic's internal lessons on skill categories, writing, distribution, and measurement (2026-03-17)
- [[sources/claude-code-seeing-like-an-agent]] — Tool design philosophy: AskUserQuestion, TodoWrite→Task, search evolution, progressive disclosure (2026-02-27)
- [[sources/turboquant-kv-cache-compression]] — Google TurboQuant: 6× KV cache memory reduction, 8× attention speedup, no retraining (2026-03-29)
- [[sources/googleworkspace-cli]] — Discovery-driven Rust CLI for all Google Workspace APIs; command surface generated at runtime from Google's API schema (2026-04-26)
- [[sources/claude-skills-alirezarezvani]] — 248 production-ready skills for 11 AI coding tools with Skills/Agents/Personas taxonomy and zero-dep security auditor (2026-04-26)
- [[sources/hindsight]] — Biomimetic agent memory (World/Experiences/Mental Models) with SOTA LongMemEval results; Reflect synthesizes new insights from experience (2026-04-26)
- [[sources/addyosmani-agent-skills]] — 19 lifecycle-mapped engineering skills from Addy Osmani; anti-rationalization tables and evidence-gated verification (2026-04-26)
- [[sources/graphify]] — Claude Code skill converting any folder to a knowledge graph; 71.5× token reduction via graph compression and PreToolUse hook (2026-04-26)
- [[sources/openspace]] — Self-evolving skill engine (HKUDS); FIX/DERIVED/CAPTURED mutation modes; 4.2× GDPVal improvement (2026-04-26)
- [[sources/cli-anything]] — Generates production CLI harnesses for real software (GIMP, Blender, etc.); Rendering Gap insight; CLI-Hub for autonomous install (2026-04-26)
- [[sources/openviking]] — Context database with filesystem URI paradigm (viking://); three-tier lazy loading; 96% fewer tokens vs flat RAG (2026-04-26)
- [[sources/personal-ai-infrastructure]] — Goal-oriented personal AI assistant (TELOS) layered on Claude Code; 63 skills, 21 hooks, three-tier memory with feedback loops (2026-04-26)
- [[sources/agent-governance-toolkit]] — Microsoft's runtime agent governance: <0.1ms policy eval, zero-trust identity, 4-tier privilege rings, full OWASP Agentic Top 10 coverage (2026-04-26)
- [[sources/autoresearch]] — Karpathy's proof-of-concept: AI agent runs overnight ML training experiments autonomously; human programs research strategy in program.md (2026-04-26)
- [[sources/tensorzero]] — Open-source LLMOps platform; Rust gateway, ClickHouse observability, data flywheel closing the fine-tuning loop (2026-04-26)
- [[sources/onlook]] — Visual editor for Next.js + TailwindCSS; bidirectional DOM-to-source live link; designers ship React without writing JSX (2026-04-26)
- [[sources/praisonai]] — Low-code multi-agent framework; YAML-first, fixed workflow vocabulary, doom-loop detection, MCP as tool integration layer (2026-04-26)
- [[sources/trading-agents]] — LangGraph multi-agent framework mirroring a trading firm org chart; adversarial bullish/bearish debate before portfolio decisions (2026-04-26)
- [[sources/claw-code]] — Community Rust reimplementation of Claude Code CLI; mock-service parity harness for correctness testing across the port (2026-04-26)
- [[sources/hermes-agent]] — Nous Research self-improving personal agent; closed skill-creation loop, dialectic user model via Honcho, RL trajectory generation (2026-04-26)
- [[sources/opencode]] — Open-source Claude Code alternative; client/server architecture, provider-agnostic, LSP out-of-the-box, build/plan dual-agent model (2026-04-26)
- [[sources/claude-code-repo]] — Official Anthropic Claude Code repo; plugin extensibility, multi-surface support, OS-native installer migration (2026-04-26)
- [[sources/claude-howto]] — Community 10-module progressive curriculum for Claude Code; power comes from combining features, not using them in isolation (2026-04-26)
- [[sources/claude-mem]] — Claude Code persistent memory plugin; 3-layer retrieval (search index → timeline → full fetch); ~10× token savings (2026-04-26)
- [[sources/everything-claude-code]] — Hackathon-winning harness with 47 agents, 181 skills, DRY cross-harness adapter, instinct-based learning, AgentShield security scanning (2026-04-26)
- [[sources/get-shit-done]] — Spec-driven development system; solves context rot via fresh subagent contexts, wave execution, XML task prompts, multi-layer security (2026-04-26)
- [[sources/gstack]] — Garry Tan's Claude Code skill pack; full sprint process (Think→Plan→Build→Review→Test→Ship→Reflect), real Chromium QA, /pair-agent (2026-04-26)
- [[sources/obra-superpowers]] — Spec-first workflow; brainstorming before coding, true RED-GREEN-REFACTOR TDD, two-stage spec+quality subagent review (2026-04-26)
- [[sources/oh-my-claudecode]] — Teams-first orchestration layer; staged plan→PRD→exec→verify→fix pipeline, tmux CLI workers, smart model routing, Ralph persistence mode (2026-04-26)
- [[sources/awesome-design-md]] — Curated DESIGN.md files from Vercel, Stripe, Claude, Linear; drop into any project so AI generates UI matching established design systems (2026-04-26)
- [[sources/system-prompts-leaks]] — Community archive of verbatim system prompts from ChatGPT, Claude, Gemini, Grok, Perplexity; tool-level granularity for OpenAI (2026-04-26)
- [[sources/last30days-skill]] — Claude Code skill for parallel research across 10 live sources; two-phase scoring and synthesis; progressive source unlocking (2026-04-26)

## Entities

- [[AlphaEvolve]] — Google DeepMind Gemini-powered coding agent using evolutionary code search
- [[Claude-Code]] — Anthropic's agentic coding CLI and development environment
- [[Thariq-Shihipar]] — Anthropic engineer; author of "Seeing like an Agent" and "How We Use Skills"
- [[TurboQuant]] — Google two-stage KV cache compression algorithm (PolarQuant + QJL)

## Concepts

- [[Agent-Governance]] — Runtime policy enforcement, zero-trust identity, and privilege rings for autonomous agents; OWASP Agentic Top 10
- [[Agent-Memory]] — Three architectures for agent memory: biomimetic (Hindsight), filesystem (OpenViking), self-evolving skills (OpenSpace)
- [[Agent-Native-Software]] — Making software consumable by AI agents via generated CLIs and discovery-driven command surfaces
- [[Agent-Skills]] — Packaged expertise folders for AI agents; Claude Code's primary extensibility mechanism
- [[Complexity-Theory]] — Hardness of approximation, gadget reductions, inapproximability bounds
- [[Context-Engineering]] — Deliberate design of what enters an LLM's context window; context rot, fresh subagents, structured context files
- [[Knowledge-Graph-for-Agents]] — Graph-based compression of codebases and docs; 71.5× token reduction; always-on PreToolUse hook pattern
- [[KV-Cache]] — Key-value cache bottleneck in LLM inference; primary target of efficiency research
- [[LLMOps]] — Gateway, observability, evaluation, fine-tuning, and experimentation for LLM systems; data flywheel as organizing principle
- [[Multi-Agent-Orchestration]] — Coordinating multiple agents via thin orchestrators, wave execution, staged pipelines, and quality gates
- [[Personal-AI-Stack]] — Goal-oriented personal AI infrastructure: TELOS goal files, tiered memory, hook-driven extensibility
- [[Progressive-Disclosure]] — Agent design pattern: incremental context discovery over front-loading
- [[Self-Evolving-Skills]] — Skills that mutate in response to execution outcomes (FIX/DERIVED/CAPTURED); agents learn from failure
- [[Skills-Ecosystem]] — Open standard skill libraries, marketplaces, security auditing, and cross-tool distribution
- [[Spec-Driven-Development]] — Writing full specs before code generation; brainstorming gates, PRD stages, two-stage review

## Analyses

*(none yet)*
