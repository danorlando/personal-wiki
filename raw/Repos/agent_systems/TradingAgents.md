---
title: "TauricResearch/TradingAgents: TradingAgents: Multi-Agents LLM Financial Trading Framework"
source: "https://github.com/TauricResearch/TradingAgents"
author:
published:
created: 2026-04-06
description: "TradingAgents: Multi-Agents LLM Financial Trading Framework - TauricResearch/TradingAgents"
tags:
  - "agent_system"
  - "repository"
  - "OSS"
---
[![](https://github.com/TauricResearch/TradingAgents/raw/main/assets/TauricResearch.png)](https://github.com/TauricResearch/TradingAgents/blob/main/assets/TauricResearch.png)

[Deutsch](https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=de) | [Español](https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=es) | [français](https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=fr) | [日本語](https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=ja) | [한국어](https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=ko) | [Português](https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=pt) | [Русский](https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=ru) | [中文](https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=zh)

---

## TradingAgents: Multi-Agents LLM Financial Trading Framework

## News

- \[2026-03\] **TradingAgents v0.2.3** released with multi-language support, GPT-5.4 family models, unified model catalog, backtesting date fidelity, and proxy support.
- \[2026-03\] **TradingAgents v0.2.2** released with GPT-5.4/Gemini 3.1/Claude 4.6 model coverage, five-tier rating scale, OpenAI Responses API, Anthropic effort control, and cross-platform stability.
- \[2026-02\] **TradingAgents v0.2.0** released with multi-provider LLM support (GPT-5.x, Gemini 3.x, Claude 4.x, Grok 4.x) and improved system architecture.
- \[2026-01\] **Trading-R1** [Technical Report](https://arxiv.org/abs/2509.11420) released, with [Terminal](https://github.com/TauricResearch/Trading-R1) expected to land soon.

[![TradingAgents Star History](https://camo.githubusercontent.com/977dce33ad723ac2a00a5ab33d59268885c735d2204e9db43d4d6a179e7e652f/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d54617572696352657365617263682f54726164696e674167656e747326747970653d44617465)](https://www.star-history.com/#TauricResearch/TradingAgents&Date)

> 🎉 **TradingAgents** officially released! We have received numerous inquiries about the work, and we would like to express our thanks for the enthusiasm in our community.
> 
> So we decided to fully open-source the framework. Looking forward to building impactful projects with you!

🚀 [TradingAgents](#tradingagents-framework) | ⚡ [Installation & CLI](#installation-and-cli) | 🎬 [Demo](https://www.youtube.com/watch?v=90gr5lwjIho) | 📦 [Package Usage](#tradingagents-package) | 🤝 [Contributing](#contributing) | 📄 [Citation](#citation)

## TradingAgents Framework

TradingAgents is a multi-agent trading framework that mirrors the dynamics of real-world trading firms. By deploying specialized LLM-powered agents: from fundamental analysts, sentiment experts, and technical analysts, to trader, risk management team, the platform collaboratively evaluates market conditions and informs trading decisions. Moreover, these agents engage in dynamic discussions to pinpoint the optimal strategy.

[![](https://github.com/TauricResearch/TradingAgents/raw/main/assets/schema.png)](https://github.com/TauricResearch/TradingAgents/blob/main/assets/schema.png)

> TradingAgents framework is designed for research purposes. Trading performance may vary based on many factors, including the chosen backbone language models, model temperature, trading periods, the quality of data, and other non-deterministic factors. [It is not intended as financial, investment, or trading advice.](https://tauric.ai/disclaimer/)

Our framework decomposes complex trading tasks into specialized roles. This ensures the system achieves a robust, scalable approach to market analysis and decision-making.

### Analyst Team

- Fundamentals Analyst: Evaluates company financials and performance metrics, identifying intrinsic values and potential red flags.
- Sentiment Analyst: Analyzes social media and public sentiment using sentiment scoring algorithms to gauge short-term market mood.
- News Analyst: Monitors global news and macroeconomic indicators, interpreting the impact of events on market conditions.
- Technical Analyst: Utilizes technical indicators (like MACD and RSI) to detect trading patterns and forecast price movements.

[![](https://github.com/TauricResearch/TradingAgents/raw/main/assets/analyst.png)](https://github.com/TauricResearch/TradingAgents/blob/main/assets/analyst.png)

### Researcher Team

- Comprises both bullish and bearish researchers who critically assess the insights provided by the Analyst Team. Through structured debates, they balance potential gains against inherent risks.

[![](https://github.com/TauricResearch/TradingAgents/raw/main/assets/researcher.png)](https://github.com/TauricResearch/TradingAgents/blob/main/assets/researcher.png)

### Trader Agent

- Composes reports from the analysts and researchers to make informed trading decisions. It determines the timing and magnitude of trades based on comprehensive market insights.

[![](https://github.com/TauricResearch/TradingAgents/raw/main/assets/trader.png)](https://github.com/TauricResearch/TradingAgents/blob/main/assets/trader.png)

### Risk Management and Portfolio Manager

- Continuously evaluates portfolio risk by assessing market volatility, liquidity, and other risk factors. The risk management team evaluates and adjusts trading strategies, providing assessment reports to the Portfolio Manager for final decision.
- The Portfolio Manager approves/rejects the transaction proposal. If approved, the order will be sent to the simulated exchange and executed.

[![](https://github.com/TauricResearch/TradingAgents/raw/main/assets/risk.png)](https://github.com/TauricResearch/TradingAgents/blob/main/assets/risk.png)

## Installation and CLI

### Installation

Clone TradingAgents:

```
git clone https://github.com/TauricResearch/TradingAgents.git
cd TradingAgents
```

Create a virtual environment in any of your favorite environment managers:

```
conda create -n tradingagents python=3.13
conda activate tradingagents
```

Install the package and its dependencies:

```
pip install .
```

### Docker

Alternatively, run with Docker:

```
cp .env.example .env  # add your API keys
docker compose run --rm tradingagents
```

For local models with Ollama:

```
docker compose --profile ollama run --rm tradingagents-ollama
```

### Required APIs

TradingAgents supports multiple LLM providers. Set the API key for your chosen provider:

```
export OPENAI_API_KEY=...          # OpenAI (GPT)
export GOOGLE_API_KEY=...          # Google (Gemini)
export ANTHROPIC_API_KEY=...       # Anthropic (Claude)
export XAI_API_KEY=...             # xAI (Grok)
export OPENROUTER_API_KEY=...      # OpenRouter
export ALPHA_VANTAGE_API_KEY=...   # Alpha Vantage
```

For local models, configure Ollama with `llm_provider: "ollama"` in your config.

Alternatively, copy `.env.example` to `.env` and fill in your keys:

```
cp .env.example .env
```

### CLI Usage

Launch the interactive CLI:

```
tradingagents          # installed command
python -m cli.main     # alternative: run directly from source
```

You will see a screen where you can select your desired tickers, analysis date, LLM provider, research depth, and more.

[![](https://github.com/TauricResearch/TradingAgents/raw/main/assets/cli/cli_init.png)](https://github.com/TauricResearch/TradingAgents/blob/main/assets/cli/cli_init.png)

An interface will appear showing results as they load, letting you track the agent's progress as it runs.

[![](https://github.com/TauricResearch/TradingAgents/raw/main/assets/cli/cli_news.png)](https://github.com/TauricResearch/TradingAgents/blob/main/assets/cli/cli_news.png)

[![](https://github.com/TauricResearch/TradingAgents/raw/main/assets/cli/cli_transaction.png)](https://github.com/TauricResearch/TradingAgents/blob/main/assets/cli/cli_transaction.png)

## TradingAgents Package

### Implementation Details

We built TradingAgents with LangGraph to ensure flexibility and modularity. The framework supports multiple LLM providers: OpenAI, Google, Anthropic, xAI, OpenRouter, and Ollama.

### Python Usage

To use TradingAgents inside your code, you can import the `tradingagents` module and initialize a `TradingAgentsGraph()` object. The `.propagate()` function will return a decision. You can run `main.py`, here's also a quick example:

```
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

ta = TradingAgentsGraph(debug=True, config=DEFAULT_CONFIG.copy())

# forward propagate
_, decision = ta.propagate("NVDA", "2026-01-15")
print(decision)
```

You can also adjust the default configuration to set your own choice of LLMs, debate rounds, etc.

```
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "openai"        # openai, google, anthropic, xai, openrouter, ollama
config["deep_think_llm"] = "gpt-5.4"     # Model for complex reasoning
config["quick_think_llm"] = "gpt-5.4-mini" # Model for quick tasks
config["max_debate_rounds"] = 2

ta = TradingAgentsGraph(debug=True, config=config)
_, decision = ta.propagate("NVDA", "2026-01-15")
print(decision)
```

See `tradingagents/default_config.py` for all configuration options.

## Contributing

We welcome contributions from the community! Whether it's fixing a bug, improving documentation, or suggesting a new feature, your input helps make this project better. If you are interested in this line of research, please consider joining our open-source financial AI research community [Tauric Research](https://tauric.ai/).

## Citation

Please reference our work if you find *TradingAgents* provides you with some help:)

```
@misc{xiao2025tradingagentsmultiagentsllmfinancial,
      title={TradingAgents: Multi-Agents LLM Financial Trading Framework}, 
      author={Yijia Xiao and Edward Sun and Di Luo and Wei Wang},
      year={2025},
      eprint={2412.20138},
      archivePrefix={arXiv},
      primaryClass={q-fin.TR},
      url={https://arxiv.org/abs/2412.20138}, 
}
```