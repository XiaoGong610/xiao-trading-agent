---
description: Scan a watchlist of stocks and rank them for theta gang trading
---

Scan and rank these stocks for theta gang opportunities: $ARGUMENTS

The argument is a comma-separated list of tickers (e.g., "AAPL, TSLA, NVDA, AMZN, MSFT")

**Step 1:** Run the data script for each ticker to get structured market data:
```bash
source .venv/bin/activate && for ticker in TICKER1 TICKER2 ...; do echo "=== $ticker ===" && python3 scripts/technicals.py $ticker --options; done
```
(Replace the ticker list with the actual tickers from the arguments.)

Use the script's output for programmatic comparison across all tickers. Supplement with web search for earnings dates and qualitative context the script can't provide.

## Screening Criteria

For each stock, evaluate:
1. **IV Rank / IV Percentile** — higher = richer premiums (but check why IV is elevated)
2. **Options Liquidity** — volume, open interest, bid-ask spreads (wide spreads = bad fills)
3. **Underlying Stability** — beta, recent drawdown, is it range-bound or trending?
4. **Upcoming Events** — earnings date, ex-dividend date within 30-45 days? (disqualifier)
5. **Premium Available** — what can you actually collect at delta 0.20-0.30, 30-45 DTE?

## Ranking Table

| Rank | Ticker | Price | IV Rank | IV %ile | Next Earnings | Next Ex-Div | Beta | CSP Premium (30-45 DTE, ~0.25 delta) | Annualized Return | Verdict |

## Top Picks

For the top 2-3 candidates:
- Why they stand out
- Suggested strategy (CSP, CC, PMCC, or IC) and why
- Quick strike/expiry suggestion

## Disqualified Stocks
- Which stocks to skip right now and why (earnings too close, IV too low, too volatile, etc.)

Do NOT save output to a file — this is a live analysis tool for decision-making.
