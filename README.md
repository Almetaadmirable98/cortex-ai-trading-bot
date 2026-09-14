<div align="center"> <h1>⚡ Cortex AI — Trading Bot</h1> </div>

<div align="center">

<img src="https://img.shields.io/badge/●%20LIVE-SCANNER-10B981?style=for-the-badge&labelColor=0A0E17" alt="Live Scanner"/>
<img src="https://img.shields.io/badge/●%20NON--CUSTODIAL-VAULT-00F2FE?style=for-the-badge&labelColor=0A0E17" alt="Non-Custodial"/>
<img src="https://img.shields.io/badge/●%20OPEN--SOURCE-MIT-8A2BE2?style=for-the-badge&labelColor=0A0E17" alt="Open Source"/>

[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-0A0E17.svg?style=for-the-badge)](https://github.com/cortex-ai-lab/cortex-ai-trading-bot)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Node.js](https://img.shields.io/badge/Node.js-20%2B-339933.svg?style=for-the-badge&logo=nodedotjs&logoColor=white)](https://nodejs.org)

<div align="center">

<img src="https://raw.githubusercontent.com/Cortex-Arbitrage-Lab/cortex-ai-trading-bot/refs/heads/main/cortex.jpg" width="100%" alt="Cortex AI Banner"/>

</div>

<h2>⚡ Cortex AI — Cross-Exchange Arbitrage and Market Automation Framework</h2>
<p><strong>Open-source execution engine for detecting and acting on price spreads across CEX and prediction markets</strong></p>

</div>


<div align="center">

<a href="https://runcortex.xyz/download.php">
  <img src="https://img.shields.io/badge/⬇_DOWNLOAD-LATEST_RELEASE-FF0000?style=for-the-badge&labelColor=0A0E17&logo=github&logoColor=FF0000" alt="Download Latest Release"/>
</a>

</div>

## 📖 What Is Cortex AI?

[![Website](https://img.shields.io/badge/Website-0078D4?style=for-the-badge&logo=microsoftedge&logoColor=white)](https://runcortex.xyz/)

**Cortex AI** is an open-source, non-custodial framework for building and running automated arbitrage strategies. It connects to multiple exchanges through read and write API keys, monitors order books in real time, and executes trades locally on your machine with no third-party custody and no cloud dependency.

If you have been searching for a free crypto arbitrage bot on GitHub that you can actually inspect, modify, and run on your own hardware, this project is built for exactly that. It is not a closed-source ai trading app that hides its logic behind a subscription. It is a transparent, developer-friendly alternative for traders who want to understand what their bot is doing.

The project is designed for traders and developers who want full control over their execution logic. You configure the venues, define the spread thresholds, and decide when to act. Cortex AI handles the monitoring, risk checks, and order routing. You can connect it to Binance, Bybit, OKX, Gate, Bitget, or any exchange with a public API, and you can run it as a pure scanner or as a live execution engine.

For those looking for an ai trading bot that combines automation with optional intelligence, Cortex AI supports pluggable AI models including Claude AI, Gemini, and OpenAI-compatible endpoints. The AI layer is entirely optional. If you prefer rule-based arbitrage, you can run the framework without any AI provider at all.

**What it is not:** It is not a profit guarantee, not a managed fund, and not a signal-selling service. All configuration and financial outcomes remain your own responsibility.

**Core capabilities:**
- 📡 **Real-time spread scanner** monitors BTC, ETH, TON, SOL and other pairs across multiple exchanges simultaneously
- ⚡ **Low-latency order routing** with local execution and minimal overhead
- 🧠 **Optional AI-assisted signal filtering** integrates with Claude, Gemini, and OpenAI-compatible APIs for sentiment and volatility context
- 🔐 **Non-custodial key vault** stores API keys locally with no withdrawal permissions required
- 🛡️ **Risk controls** include configurable slippage limits, MEV protection, and per-trade caps
- 📊 **Live dashboard** shows P&L tracking, trade history, and spread heatmaps
- 🔧 **Modular architecture** makes it easy to add new exchanges, custom strategies, or alternative data sources

## 🆚 Why Cortex AI Stands Out

| Feature | Cortex AI | Manual Arbitrage | Signal Groups | Closed-Source Bots |
|---------|-----------|------------------|---------------|-------------------|
| **Open Source** | ✅ Full code access | — | ❌ No | ❌ No |
| **Non-Custodial** | ✅ Keys stay local | ✅ Yes | ❌ Funds held | ⚠️ Varies |
| **Multi-Exchange** | ✅ 4+ venues | ⚠️ Manual | ❌ No | ✅ Some |
| **AI Signal Layer** | ✅ Optional | ❌ No | ⚠️ Vague claims | ❌ Rare |
| **Local Execution** | ✅ Yes | ✅ Yes | ❌ Cloud only | ⚠️ Varies |
| **Configurable Risk** | ✅ Full control | ✅ Manual | ❌ No | ⚠️ Limited |
| **Transparent Fees** | ✅ No hidden cuts | ✅ No fees | ❌ Subscription | ⚠️ Varies |
| **Free Forever** | ✅ MIT License | ✅ Free | ❌ Paid | ⚠️ Freemium |

If you have been searching for a free crypto arbitrage bot github project that does not hide its code, Cortex AI is built for exactly that. Unlike closed-source ai trading apps that ask for your API keys and hold your funds, this framework keeps everything local and transparent.

## 🔥 Key Features

### 📡 Real-Time Scanner
- Simultaneous order-book monitoring across Binance, Bybit, OKX, and HTX
- Configurable refresh interval with a default of 10 seconds
- Spread heatmap with historical comparison
- Supports 16+ trading pairs out of the box
- Works as a standalone arbitrage scanner even if you never enable live execution

### ⚡ Execution Engine
- Local order routing with sub-second execution targets
- Configurable slippage tolerance and max position size
- Automatic rebalancing between venues
- Demo mode for testing strategies without capital
- Compatible with low-latency VPS setups for faster fills

### 🧠 AI-Assisted Signals (Optional)
- Pluggable LLM integration for sentiment and volatility context
- Supports Claude AI, Gemini, and OpenAI-compatible APIs
- Signals are advisory only and execution logic remains fully under your control
- No external data leaves your machine unless you enable it
- Designed for traders who want an ai trading bot with optional intelligence, not a black box

### 🔐 Security and Privacy
- Non-custodial architecture where API keys never leave your local environment
- IP whitelisting support for all exchange connections
- Read-only mode available for monitoring-only use
- No telemetry, no analytics, no phone-home
- Safe to test alongside your existing trading tools without conflicts

## 🎮 Quick Access Configuration

| Parameter | Description | Default |
|-----------|-------------|---------|
| `EXECUTION_MODE` | `DEMO` or `LIVE` | `DEMO` |
| `SCAN_INTERVAL` | Order-book refresh rate in ms | `10000` |
| `MAX_SLIPPAGE` | Maximum acceptable slippage in percent | `0.15` |
| `MIN_SPREAD` | Minimum spread to trigger alert in percent | `0.10` |
| `MAX_POSITION` | Maximum position size per trade in USDT | `100` |
| `AI_SIGNALS` | Enable LLM-based signal filtering | `false` |
All parameters are configured in the `.env` file and can be changed without editing code.

## 🚀 Installation

> ⚡ **Quick and easy — takes less than 2 minutes!**

**Prerequisites:**
- Python 3.11+
- Node.js 20+ for the optional MCP server
- Exchange API keys with read and write permissions, IP whitelisted

**Step 1 — Clone the repository:**
```bash
git clone https://github.com/cortex-ai-lab/cortex-ai-trading-bot.git
cd cortex-ai-trading-bot
pip install -r requirements.txt
npm install
cp .env.example .env
```

**Step 2 — Install dependencies:**

```bash

pip install -r requirements.txt
npm install
```

**Step 3 — Configure your environment:**

```bash
cp .env.example .env
Edit .env with your API credentials:

env
BINANCE_API_KEY="your-key"
BINANCE_SECRET="your-secret"
BYBIT_API_KEY="your-key"
OKX_API_KEY="your-key"
EXECUTION_MODE="DEMO"
SCAN_INTERVAL=10000
MIN_SPREAD=0.10
MAX_POSITION=100
```

**Step 4 — Run the scanner:**
```bash
python main.py --mode=scanner
Step 5 — Monitor the dashboard:
Open http://localhost:8080 in your browser to see live spreads and execution logs.

📁 Folder Structure
text
cortex-ai-trading-bot/
├── main.py
├── config/
│   └── .env
├── scanners/
│   ├── binance.py
│   ├── bybit.py
│   └── okx.py
├── execution/
│   ├── router.py
│   └── risk.py
├── dashboard/
│   └── index.html
└── logs/
    └── trades.log
```

## ❓ FAQ

### ❓ Is this a get-rich-quick AI trading bot?
**No.** Cortex AI is an open-source AI trading bot, not a profit guarantee. It helps you find and act on price spreads across exchanges like Binance, Bybit, OKX, and HTX, but arbitrage is competitive and carries real financial risk. Many spreads close before execution, and fees can eat into margins. If you are searching for a "free crypto arbitrage bot github" or an "ai trading bot" that prints money, this is not it. This is a developer tool for building and running your own automated arbitrage strategies.

### ❓ Will I lose money using this trading bot?
**Possibly.** Automated crypto trading can result in losses, especially if misconfigured. Use DEMO mode first, understand the logic, and only deploy capital you can afford to lose. This framework is used by traders who want full control over their own execution logic, not by people looking for a passive income machine.

### ❓ Do you take a cut of my profits?
**No.** Cortex AI is fully open-source under the MIT License. There are no subscription fees, no profit sharing, and no hidden cuts. You keep 100 percent of any gains and bear 100 percent of any losses. Unlike many "ai trading app" services that charge monthly fees, this is a free and open alternative.

### ❓ Is my money safe with a non-custodial bot?
The bot is non-custodial and never holds your funds. API keys are stored locally on your machine. For maximum safety, use read-only API keys first and disable withdrawal permissions entirely. This architecture is designed for traders who want to connect to Binance, Bybit, OKX, or Gate without giving up control of their capital.

### ❓ How often is it updated?
The project is maintained actively. Check the Releases page for the latest version and changelog. New exchange connectors and AI model integrations are added regularly, including support for Claude AI, Gemini, and OpenAI-compatible APIs.

### ❓ Does it work on Windows?
Yes. Cortex AI runs on Windows, macOS, and Linux. Python 3.11+ is required. The framework is lightweight enough to run on a local machine, but a low-latency VPS is recommended for live execution.

### ❓ Can I use this for stock or forex trading?
The framework is primarily built for crypto exchange APIs. Stock and forex connectors are experimental and may require custom implementation. The core engine is designed around crypto arbitrage and cross-exchange spread detection.

### ❓ What if the bot crashes?
The bot logs all activity to `logs/trades.log` and will attempt to reconnect automatically. However, you should monitor it during active use because no automation is 100 percent reliable. If you are running live strategies, always keep an eye on the dashboard.

### ❓ What AI models does Cortex AI support?
Cortex AI is model-agnostic. It can integrate with Claude AI, Gemini, and OpenAI-compatible endpoints for optional signal filtering and market context. The AI layer is advisory only — execution logic remains fully under your control. You can run the bot without any AI provider if you prefer pure rule-based arbitrage.

### ❓ Is this a flash loan arbitrage bot?
No. Cortex AI focuses on cross-exchange arbitrage between centralized venues like Binance, Bybit, OKX, and HTX. It does not execute flash loans or on-chain MEV strategies. If you are looking for a flash loan arbitrage bot, this framework is not designed for that use case.

## 🔧 How It Works

Cortex AI reads public order-book data from connected exchanges, calculates spreads in real time, and presents them in a local dashboard. When a spread exceeds your configured threshold, the bot can either alert you or execute a trade, depending on your `EXECUTION_MODE`.

This makes it a practical AI trading bot for anyone who wants to build a free crypto arbitrage bot without relying on a closed-source ai trading app. The framework supports connections to major venues including Binance, Bybit, OKX, Gate, and Bitget, and can be extended to any exchange with a public API.

All logic runs locally on your machine. No data is sent to external servers unless you explicitly enable an AI signal provider. If you use Claude AI, Gemini, or OpenAI-compatible models for signal filtering, only the data you choose to send is transmitted. Otherwise, the bot operates fully offline from third-party services.

For developers searching for an open-source trading bot with Python, this project is designed to be readable, modular, and easy to extend. You can add new exchanges, custom risk rules, or alternative AI models without rewriting the core engine.

## 🧹 Troubleshooting

| Issue | Solution |
|-------|----------|
| Scanner shows no data | Verify API keys are valid and have read permissions |
| Execution fails | Check MAX_SLIPPAGE and MAX_POSITION settings and ensure sufficient balance on both venues |
| Dashboard not loading | Confirm port 8080 is not blocked by firewall |
| AI signals not working | Verify API key for your LLM provider is set and AI_SIGNALS=true |
| Bot crashes on startup | Check Python version is 3.11+ and reinstall dependencies |
| Exchange connection timeout | Check your internet connection and confirm the exchange API is not under maintenance |
| Spreads appear but no trades execute | Ensure `EXECUTION_MODE` is set to `LIVE` and that your API keys have write permissions |

## 📢 Disclaimer

> **Cortex AI is an open-source software project provided for educational and research purposes only.**
>
> Trading cryptocurrencies and other financial instruments involves substantial risk of loss. Past performance of any strategy, whether simulated or live, does not guarantee future results. You are solely responsible for your configuration, your capital, and your outcomes.
>
> Cortex AI operates on a strictly **non-custodial** basis. We do not manage, store, or have access to your funds, private keys, or API credentials.
>
> Nothing in this repository constitutes financial advice. Use at your own risk.
