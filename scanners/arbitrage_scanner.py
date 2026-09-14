"""
Arbitrage Scanner Module
Aggregates order books across multiple CEX platforms and detects bid-ask price disparities.
"""

import asyncio
import random

class ArbitrageScanner:
    def __init__(self, exchanges: list, min_spread: float):
        self.exchanges = exchanges
        self.min_spread = min_spread

    async def fetch_order_book(self, exchange: str, symbol: str):
        """Simulates fetching real-time L2 order book data via REST / WebSocket."""
        base_price = 64000.0 if symbol == "BTC/USDT" else 3400.0
        variation = random.uniform(-15.0, 15.0)
        bid = base_price + variation
        ask = bid + random.uniform(0.5, 3.0)
        return {"exchange": exchange, "symbol": symbol, "bid": bid, "ask": ask}

    async def scan_spreads(self):
        """Calculates potential cross-exchange arbitrage opportunities."""
        pairs = ["BTC/USDT", "ETH/USDT", "SOL/USDT"]
        opportunities = []

        for pair in pairs:
            books = await asyncio.gather(*[self.fetch_order_book(ex, pair) for ex in self.exchanges])
            
            # Find best buy (lowest ask) and best sell (highest bid)
            best_buy = min(books, key=lambda x: x["ask"])
            best_sell = max(books, key=lambda x: x["bid"])

            if best_buy["exchange"] != best_sell["exchange"]:
                spread = ((best_sell["bid"] - best_buy["ask"]) / best_buy["ask"]) * 100
                if spread >= self.min_spread:
                    opportunities.append({
                        "pair": pair,
                        "buy_exchange": best_buy["exchange"],
                        "buy_price": round(best_buy["ask"], 2),
                        "sell_exchange": best_sell["exchange"],
                        "sell_price": round(best_sell["bid"], 2),
                        "spread": round(spread, 3)
                    })
        return opportunities
