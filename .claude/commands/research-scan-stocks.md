---
description: Scan a list of stocks and rank them for the best trading opportunities
---

Scan and rank these stocks for trading opportunities: $ARGUMENTS

The argument is a comma-separated list of tickers (e.g., "AAPL, TSLA, NVDA, AMZN, MSFT")

**Step 1:** Run the data script for each ticker to get structured market data:
```bash
source .venv/bin/activate && for ticker in TICKER1 TICKER2 ...; do echo "=== $ticker ===" && python3 scripts/technicals.py $ticker --options; done
```
(Replace the ticker list with the actual tickers from the arguments.)

Use the script's output for programmatic comparison across all tickers. Supplement with web search for earnings dates and qualitative context the script can't provide.

## Screening Criteria

For each stock, evaluate:
1. **Trend & Technicals** — RSI, MACD, SMA alignment. Trending up, down, or sideways?
2. **Support & Resistance** — where is price relative to key levels? Near support (buy zone) or resistance?
3. **IV Rank / IV Percentile** — is premium rich (favors selling) or cheap (favors buying)?
4. **Options Liquidity** — volume, open interest, bid-ask spreads (wide spreads = bad fills)
5. **Upcoming Events** — earnings date, ex-dividend date within 30-45 days?
6. **Fundamentals** — P/E, revenue growth, margins — quick health check

## Ranking Table

| Rank | Ticker | Price | Trend | IV Rank | IV %ile | Next Earnings | Beta | Best Strategy | Verdict |

## Strategy Fit (per stock)

For each stock, recommend the best strategy:
- **Buy & Hold** — strong compounder, trending up, just accumulate
- **DCA** — conviction but uncertain timing
- **LEAP Calls** — bullish with catalyst ahead, want leverage
- **Theta Gang** — elevated IV, range-bound or at support, premium is rich

## Top Picks

For the top 2-3 candidates:
- Why they stand out
- Recommended strategy and why
- Quick entry suggestion (price level, strike, or DCA schedule)

## Skip For Now
- Which stocks to avoid right now and why (earnings too close, IV too low, overextended, thesis unclear, etc.)

Do NOT save output to a file — this is a live analysis tool for decision-making.
