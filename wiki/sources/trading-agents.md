---
tags:
  - agent_systems
  - multi_agent
  - financial_ai
  - trading
  - langgraph
  - research_framework
updated: 2026-04-26
source: https://github.com/TauricResearch/TradingAgents
---

# TradingAgents

A multi-agent LLM framework that mirrors the structure of a real-world trading firm — decomposing a trading decision into specialized analyst, researcher, trader, risk manager, and portfolio manager roles that debate and synthesize before any order is placed.

## Key design decisions / architecture

**Role decomposition mirrors institutional finance.** The core insight is that trading firms already decompose decision-making into specialized roles with structured information flows between them. TradingAgents makes this the architecture: four analysts (fundamentals, sentiment, news, technical) feed a bullish/bearish researcher debate, which feeds a trader report, which feeds a risk team, which feeds a portfolio manager who makes the final approval/rejection. Each hand-off is explicit, not implicit.

**Structured debate as risk control.** The most non-obvious design choice is the researcher tier: bullish and bearish researchers receive the same analyst inputs and argue opposing cases before the trader synthesizes them. The number of debate rounds is configurable (`max_debate_rounds`). This is not just rhetorical framing — it forces the system to surface counter-arguments before committing capital, functioning as an adversarial check.

**Portfolio manager as gatekeeper.** The final approval step is architecturally separate from the trader's recommendation. Even if the trader proposes a trade, the portfolio manager can reject it based on risk assessment. This mirrors how institutional desks operate and prevents the trader agent from being the single point of failure.

**Two-tier LLM assignment.** The framework distinguishes between `deep_think_llm` (complex reasoning tasks — researcher debate, risk evaluation) and `quick_think_llm` (faster, cheaper tasks — data retrieval, formatting). This cost/capability tiering is explicit in the config rather than ad hoc.

**LangGraph as the execution substrate.** The agent graph is implemented in LangGraph, giving each node a defined state schema and making the flow inspectable and modifiable. The `TradingAgentsGraph.propagate(ticker, date)` interface is deliberately simple — complexity is inside the graph, not in the caller.

**Backtesting with date fidelity.** The framework is designed for research, with backtesting support and careful attention to not leaking future data into past decision points — a subtle but critical correctness requirement for financial AI systems.

**Provider-agnostic from the start.** Multi-LLM support (OpenAI, Google, Anthropic, xAI, OpenRouter, Ollama) is not an afterthought. The v0.2.x release cycle has tracked each major frontier model family release (GPT-5.4, Gemini 3.1, Claude 4.6, Grok 4.x), suggesting the authors treat model portability as a first-class concern.

**Research-oriented, not production trading.** The README is explicit: this is a research framework, not financial advice. The "simulated exchange" in the risk layer reinforces that the output of the pipeline is a decision signal, not a live order.

## Notable patterns and concepts

- **Analyst → Researcher debate → Trader → Risk → Portfolio Manager pipeline:** Strict role separation with explicit hand-offs between each tier.
- **Configurable debate rounds:** `max_debate_rounds` lets users tune how long the adversarial researcher debate runs before synthesis.
- **Five-tier rating scale:** v0.2.2 introduced a structured output format for analyst ratings.
- **Alpha Vantage integration:** Financial data is fetched via Alpha Vantage API; the framework is data-source aware, not just model-aware.
- **Trading-R1 companion work:** A separate technical report (`arxiv:2509.11420`) covers RL-trained trading models from the same research group.

## Concepts touched

- [[Multi-Agent-Orchestration]]
- [[Financial-AI-Agents]]
- [[Adversarial-Debate-in-LLM-Systems]]
- [[LangGraph]]
- [[Agent-Role-Decomposition]]
- [[LLM-Cost-Optimization]]
- [[Backtesting-AI-Agents]]

## Inbound sources

- `/Users/dan.orlando/Code/my_apps/personal_wiki/raw/Repos/agent_systems/TradingAgents.md`
