"""
Cortex AI - Advanced Crypto Arbitrage & AI Execution Engine
Entry point for managing real-time market scanners, LLM signal filters, and trade routing.
"""

import asyncio
import logging
from scanners.arbitrage_scanner import ArbitrageScanner
from execution.ai_signal_engine import AISignalEngine
from execution.risk_manager import RiskManager
from config.settings import Config

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(message)s")

async def main():
    logging.info("Initializing Cortex AI Arbitrage Framework v2.4...")
    config = Config.load()
    
    # Initialize core modules
    scanner = ArbitrageScanner(exchanges=config.EXCHANGES, min_spread=config.MIN_SPREAD)
    ai_engine = AISignalEngine(provider=config.AI_PROVIDER, api_key=config.AI_API_KEY)
    risk_manager = RiskManager(max_position=config.MAX_POSITION, max_slippage=config.MAX_SLIPPAGED)

    logging.info(f"Execution Mode: {config.EXECUTION_MODE} | Min Spread Threshold: {config.MIN_SPREAD}%")
    logging.info(f"AI Provider: {config.AI_PROVIDER} (Active: {config.ENABLE_AI_SIGNALS})")

    while True:
        # Step 1: Scan for cross-exchange spreads
        opportunities = await scanner.scan_spreads()
        
        for opp in opportunities:
            logging.info(f"Opportunity Detected: {opp['pair']} | Buy: {opp['buy_exchange']} @ ${opp['buy_price']} -> Sell: {opp['sell_exchange']} @ ${opp['sell_price']} | Spread: {opp['spread']}%")
            
            # Step 2: Validate through AI Advisory Layer (if enabled)
            ai_verified = True
            if config.ENABLE_AI_SIGNALS:
                ai_analysis = await ai_engine.analyze_market_context(opp)
                ai_verified = ai_analysis.get("recommended", False)
                logging.info(f"AI Sentiment Score: {ai_analysis.get('score')} | Recommendation: {ai_analysis.get('reason')}")

            # Step 3: Local Risk Validation & Execution
            if ai_verified:
                can_execute = risk_manager.validate_trade(opp)
                if can_execute:
                    logging.info(f"[EXECUTION] Executing trade pair {opp['pair']} under mode {config.EXECUTION_MODE}...")
                else:
                    logging.warning("[RISK REJECT] Trade exceeded local safety thresholds.")

        await asyncio.sleep(config.SCAN_INTERVAL / 1000.0)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Cortex AI engine shut down gracefully.")
