import yfinance as yf
import pandas as pd
import numpy as np

# 1. Pick a stock (e.g., Apple or even Palantir )
ticker = "PLTR"
data = yf.download(ticker, start="2025-01-01", end="2026-05-01")

#2. Calculate Daily Returns (Algebra)
data["Daily_Return"] = data["Close"].pct_change()

#3. Calculate volatility