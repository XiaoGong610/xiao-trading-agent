---
description: Broad market overview — where is money flowing, what sectors are hot, what's next
---

Run a broad market scan to identify opportunities.

This skill takes no arguments. It provides a high-level market overview before diving into specific sectors or stocks.

Use web search to gather current market data. Cover:

## Market Pulse
- S&P 500, Nasdaq, Russell 2000 recent performance (1-week, 1-month, YTD)
- Market sentiment: fear/greed, VIX level
- Macro backdrop: Fed policy, inflation, rates, any geopolitical events affecting markets

## Sector Rotation
Where is money flowing right now? Show a sector performance table:

| Sector | YTD Performance | Trend | Notable Movers |
|--------|----------------|-------|----------------|

Identify:
- **Leading sectors** — outperforming, money flowing in
- **Lagging sectors** — underperforming, but watch for rotation opportunities
- **Turning sectors** — showing early signs of reversing (either topping out or bottoming)

## Volatility & Options Landscape
- VIX level and trend — is volatility elevated or depressed?
- Any upcoming macro events that could move markets (FOMC, jobs report, CPI, earnings season)?
- Which sectors have elevated IV right now?

## Hot Themes
- What are analysts and media talking about as the "next trade"?
- Any emerging narratives (AI infrastructure, defense, energy transition, etc.)?
- Contrarian opportunities — sectors that are hated but could be turning

## Sector Recommendations

Rank 3-5 sectors to investigate further:

| Priority | Sector | Why | Next Step |
|----------|--------|-----|-----------|
| 1 | ... | ... | `/sector-scan SECTOR` |
| 2 | ... | ... | `/sector-scan SECTOR` |
| 3 | ... | ... | `/sector-scan SECTOR` |

Be opinionated — don't just list everything. Focus on what's actionable right now. The user may pursue any strategy (buy-and-hold, DCA, theta gang, swing trading), so keep recommendations strategy-agnostic.

Save the output to `research/sectors/market-overview.md`.
Start the entry with a date separator: `---` followed by `# Market Overview | YYYY-MM-DD`.
If the file already exists, prepend the new scan above all previous entries. Never remove historical entries.
