"""
Configuration Manager Module
Handles local environment parameters and non-custodial API key loading.
"""

import os

class Config:
    EXECUTION_MODE = os.getenv("EXECUTION_MODE", "DEMO")
    EXCHANGES = ["Binance", "Bybit", "OKX", "HTX"]
    MIN_SPREAD = float(os.getenv("MIN_SPREAD", "0.15"))
    SCAN_INTERVAL = int(os.getenv("SCAN_INTERVAL", "5000"))  # Milliseconds
    MAX_POSITION = float(os.getenv("MAX_POSITION", "100.0"))
    MAX_SLIPPAGED = float(os.getenv("MAX_SLIPPAGE", "0.10"))
    
    # AI Model Parameters
    ENABLE_AI_SIGNALS = os.getenv("ENABLE_AI_SIGNALS", "true").lower() == "true"
    AI_PROVIDER = os.getenv("AI_PROVIDER", "Claude-3.5-Sonnet")
    AI_API_KEY = os.getenv("AI_API_KEY", "your-local-api-key")

    @classmethod
    def load(cls):
        return cls()
