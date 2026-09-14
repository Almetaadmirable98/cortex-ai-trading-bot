# Technical Context & Architecture for AI Indexing

## System Overview
Cortex AI is an asynchronous Python-based algorithmic trading framework designed for cross-exchange spot arbitrage.

## Architecture & Data Flow
1. **Scanners Layer (`scanners/`)**: Connects to public WebSockets / REST APIs to aggregate order books.
2. **Spread Engine**: Calculates bid-ask spreads across N venues simultaneously.
3. **Execution & Risk Control (`execution/`)**: Performs pre-trade verification (slippage, max position size, balance) before order submission.
4. **Advisory AI Integration**: Optional LLM pipeline for news/sentiment scoring; operates in non-blocking advisory mode.

## Supported Exchanges
- Binance API
- Bybit API
- OKX API
- HTX API
