---
description: Dashboard view of all active positions and trade history
---

Show portfolio dashboard.

This skill takes no arguments. It reads all files in `portfolio/` and `trades/` to produce a summary.

## Active Positions

Read all `portfolio/*.md` files. Parse the YAML frontmatter from each file. Display a summary table:

| Ticker | Strategy | Strike | Expiry | DTE | Premium | Contracts | Entry Date | Notes |
|--------|----------|--------|--------|-----|---------|-----------|------------|-------|

For each position, also check (using web search or yfinance):
- Current stock price vs. strike (how far ITM/OTM)
- Estimated current P&L (if possible to estimate)

### Alerts
Flag any positions that need attention:
- **DTE < 14** — approaching expiration, consider closing or rolling
- **Deep ITM** — assignment risk, consider rolling
- **Earnings approaching** — check if earnings falls within remaining DTE
- **At 50% profit** — consider closing early per trading rules

## Capital Summary
- Total buying power deployed (sum of strike × 100 × contracts for CSPs, or share value for CCs)
- Number of active positions

## Trade History (from trades/)

If `trades/` has files, parse frontmatter and show:

| Ticker | Strategy | Entry | Exit | Days | P&L | Return | Outcome |
|--------|----------|-------|------|------|-----|--------|---------|

### Cumulative Stats
- Total realized P&L
- Win rate
- Average hold time
- Average annualized return
- Sortino Ratio (if enough trades)
- Max Drawdown

If no trades yet, note this and skip the section.

## Candidates Summary

If `research/stocks/` has files, show a brief summary of stocks being researched/monitored:

| Ticker | Status | Thesis | Entry Target | Added |
|--------|--------|--------|-------------|-------|

Do NOT save output to a file — this is a live dashboard view.
