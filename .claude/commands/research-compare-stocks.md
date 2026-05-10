---
description: Compare researched stocks head-to-head and pick the best trading opportunity
---

Compare these stocks and rank them for the best trading opportunity: $ARGUMENTS

The argument is a comma-separated list of tickers (e.g., "AAPL, TSLA, NVDA, AMZN, MSFT"). These should already be researched individually via `/research-stock` — this skill does the head-to-head comparison to decide which one to trade.

**Step 1:** Read the existing research files for each ticker from `research/stocks/TICKER.md`. If a research file is missing for any ticker, flag it and suggest running `/research-stock TICKER` first.

**Step 2:** Synthesize the research into a comparative analysis. Focus on the differences that matter for deciding which stock to trade *now*.

## Comparison Criteria

For each stock, compare:
1. **Conviction** — how strong is the bull case? Any thesis-breaking risks?
2. **Timing** — is the entry point attractive right now? Near support or overextended?
3. **Growth vs. Valuation** — who has the best growth-to-valuation ratio?
4. **Risk Profile** — upcoming earnings, binary events, sector headwinds
5. **Strategy Fit** — which strategy suits each stock and how actionable is it?

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
