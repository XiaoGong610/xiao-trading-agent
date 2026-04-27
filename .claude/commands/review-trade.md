---
description: Log and review a closed theta gang trade
---

Review this closed trade: $ARGUMENTS

The argument format is: TICKER STRATEGY STRIKE EXPIRY PREMIUM_COLLECTED OUTCOME
(e.g., "AAPL CSP 170P 2026-04-18 2.50 expired-worthless" or "TSLA CC 280C 2026-04-11 5.00 assigned")

## Trade Summary
- Strategy, strike, expiry, DTE at open
- Premium collected (per share and total for 1 contract)
- Outcome: expired worthless / closed early / assigned / rolled

## Performance Analysis
- Actual return vs. max possible return
- Holding period (actual days held vs. original DTE)
- Was it closed at ~50% profit in half the time? (per the rule)
- Annualized return achieved

## Risk-Adjusted Metrics
Using all completed trades on this stock (from `theta-gang/$TICKER.md`), calculate running metrics:
- **Sortino Ratio**: (avg return - risk-free rate) / downside deviation. Only penalizes negative returns — our primary metric since theta gang returns are negatively skewed (many small wins, rare big losses)
- **Sharpe Ratio**: (avg return - risk-free rate) / std deviation of all returns. Use as a secondary reference — note that it can look artificially high for premium-selling strategies
- **Max Drawdown**: largest peak-to-trough loss across all trades on this stock
- **Win Rate**: % of trades that were profitable
- Use the current 10-year Treasury yield as the risk-free rate (look up via web search)
- If this is the first trade on the stock, just report the single-trade return and note that ratios will become meaningful after 5+ trades

## What Went Right
- Was the entry timing good? (dip, breakout, etc.)
- Was the delta/strike selection appropriate?
- Did theta and vega work in your favor?

## What Could Improve
- Would a different strike have been better in hindsight?
- Was the DTE optimal?
- Any signals you missed (earnings, dividend, IV crush/expansion)?

## Lessons
- 1-3 actionable takeaways for future trades on this stock

Save the output to `theta-gang/$TICKER.md` (use uppercase ticker as filename).
Start the entry with a date separator: `---` followed by `# TICKER — Trade Review | YYYY-MM-DD`.
If the file already exists, prepend the new review above all previous entries (after the file title). Never remove historical entries.
