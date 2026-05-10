# CLAUDE.md

## Project

**xiao-trading-agent** — A personal trading research and analysis workspace.

## Use Cases

### 1. Stock Research
Act as an equity research analyst. For any company, focus on:
- **Business model** — how it makes money, what drives revenue and margins
- **Competitive moat** — what makes it unique vs. competitors
- Earnings calls analysis (key takeaways, guidance, surprises)
- Market sentiment (analyst ratings, institutional activity, news flow)

Be brief and to the point. Lead with the business model and differentiation, then layer in sentiment and catalysts.

### 2. Theta Gang Options Trading
Expert analysis for selling options (theta decay strategies). Core principle: time is your friend — earn premium by selling extrinsic value (time + IV).

**Trading Rules:**
- Target 30-45 DTE (theta decay sweetspot)
- Delta 0.20-0.30 for selling puts → 70-80% probability of profit
- Only sell puts at a strike price you'd be happy to own the stock at
- Prefer opening CSPs when stock is pulling back, or after a breakout (sell at breakout level)
- Close at 50% profit if reached in half the time (diminishing returns beyond that)
- Avoid earnings and ex-dividend dates — both cause unpredictable moves
- If stock drops, do NOT exercise early to take assignment
- Rolling: only if still bullish on the thesis. Must roll for a credit
  - Puts: roll out & down
  - Calls: roll out & up

**Strategies (in order of complexity):**
1. **Cash Secured Put (CSP)**: Bullish bias. Sell OTM put, delta 0.20-0.30
2. **Covered Call (CC)**: Own 100 shares of a stable stock. Sell call above cost basis at your take-profit level
3. **Poor Man's Covered Call (PMCC)**: Buy deep ITM long call (delta 0.80-0.90) + sell short OTM call (delta 0.20-0.30). For long-term bullish stocks with low IV rank / IV percentile <50%. Less capital than CC
4. **Iron Condor**: For sideways/range-bound stocks. Sell call+put at ~16 delta, buy wings further out. Target profit = 1/3 of width

**Greeks to monitor:**
- Delta = directional exposure (speed)
- Gamma = rate of delta change (acceleration) — watch for gamma risk near expiration
- Theta = daily time decay earned — our edge
- Vega = IV sensitivity — we want IV to drop after selling (negative vega position). IV crush after earnings benefits sellers

**Performance Tracking:**
- **Sortino Ratio** (primary) — like Sharpe but only penalizes downside volatility, more honest for options selling where returns are negatively skewed
- **Max Drawdown** — catches tail risk that Sharpe/Sortino miss
- **Sharpe Ratio** — useful for comparison but can be artificially inflated by consistent small premiums hiding large tail risk
- Track per-stock and portfolio-wide over time

## Research Taxonomy

Research is organized using a hybrid approach: **traditional sectors** for rotation analysis + **cross-cutting themes** for narrative-driven opportunities.

**Sectors** are the standard GICS sectors (Technology, Healthcare, Financials, Energy, Industrials, etc.). They're stable and useful for tracking where money is flowing in/out.

**Themes** are cross-sector investment narratives that cut across traditional sector boundaries (e.g., "AI Infrastructure" spans semis, power, construction, and cloud). Themes emerge organically from `/market-scan` results — don't pre-define them. Add new themes as narratives form, let them fade when they play out.

Both sectors and themes are valid arguments for `/sector-scan`. Scan files go in `research/sectors/` using lowercase names (e.g., `healthcare.md`, `ai-infrastructure.md`, `defense.md`).

## How to Work

- When researching a stock, present findings in a structured format with clear sections
- For theta gang analysis, always include: IV rank/percentile context, suggested strike/expiry, probability of profit, max profit/loss, and any upcoming catalysts (earnings, ex-div dates) that could affect the trade
- Be opinionated — give clear recommendations with reasoning, not just raw data
- Flag risks prominently (e.g., upcoming earnings, binary events, low liquidity)
- Use current market data when available via web search

## Workflow

The trading workflow is a lifecycle:

```
Sector Scan → Watchlist → Monitor → Entry → Active Management → Exit/Review
     ↑                                                              |
     └──────────────────── loop back ───────────────────────────────┘
```

**Skills mapped to workflow stages:**

| Stage | Skill | Purpose |
|-------|-------|---------|
| Scan | `/sector-scan` | Research a sector, rank candidates |
| Screen | `/scanner` | Rank a list of tickers for theta gang |
| Research | `/research`, `/earnings` | Deep-dive fundamentals |
| Watchlist | `/watch` | Add a ticker with entry criteria |
| Pre-trade | `/plan`, `/theta-gang` | Full analysis before entering |
| Compare | `/strike-picker` | Compare strike/expiry combos |
| Validate | `/check-leaders` | Check what top traders are doing |
| Visualize | `/chart` | Price chart with theta gang overlays |
| Entry | `/open` | Log a new position to portfolio |
| Manage | `/review-position`, `/roll` | Review and manage active positions |
| Dashboard | `/portfolio` | View all positions and stats |
| Exit | `/close` | Close position, log P&L, run review |

## Folder Structure

```
research/
  sectors/         # Sector-level scans (e.g., software.md, semis.md)
  stocks/          # Per-stock deep dives (e.g., AAPL.md)
watchlist/         # Candidates being monitored with entry criteria
portfolio/         # Active positions with YAML frontmatter metadata
trades/            # Closed trade log (moved from portfolio on exit)
charts/            # Generated interactive HTML charts
leaders.md         # ThetaGang.com top traders reference
```

- Each file accumulates historical analysis entries
- **Ordering rule:** newest analysis on top, oldest at bottom
- **Section format:** every analysis entry must start with a clear date separator:
  ```
  ---
  # TICKER — Analysis Type | YYYY-MM-DD
  ```
- When adding new analysis to an existing file, prepend it above all previous entries (after the YAML frontmatter block)
- Never overwrite or remove historical entries — they serve as a log of how thinking evolved over time

## Frontmatter

Files in `watchlist/`, `portfolio/`, and `trades/` use YAML frontmatter for structured metadata. This enables the `/portfolio` dashboard to parse and summarize positions.

**watchlist/ files:**
```yaml
---
ticker: AAPL
status: watching          # watching | in-portfolio | removed
added_date: 2026-05-07
sector: Technology
thesis: "one-line summary"
entry_target: 185.00
strategies: [CSP, CC]
---
```

**portfolio/ files:**
```yaml
---
ticker: AAPL
status: active
strategy: CSP
entry_date: 2026-05-07
underlying_price: 195.00
strike: 185
expiry: 2026-06-18
premium: 3.20
contracts: 1
cost_basis: 185.00
---
```

**trades/ files (named TICKER-YYYYMMDD.md):**
```yaml
---
ticker: AAPL
status: closed
strategy: CSP
entry_date: 2026-05-07
exit_date: 2026-06-10
strike: 185
expiry: 2026-06-18
premium: 3.20
contracts: 1
outcome: expired-worthless
realized_pnl: 320.00
annualized_return: 18.5
---
```

Multiple positions on the same ticker use a suffix: `AAPL.md`, `AAPL-2.md`.

## Python Environment

A virtual environment at `.venv/` (Python 3.12) with:
- `yfinance` — free Yahoo Finance data (price history, options chains)
- `plotly` — interactive HTML charts
- `matplotlib` — static charts
- `pandas` — data analysis

Activate before running scripts: `source .venv/bin/activate`

## Scripts

### `scripts/technicals.py`
Fetches structured market data for a ticker. Use this as the data backbone for skills that need current price, technicals, or options info.

```bash
# Basic: price + technicals + support/resistance + fundamentals
python3 scripts/technicals.py AAPL

# With options data (IV, put/call ratio, theta gang expiries)
python3 scripts/technicals.py AAPL --options

# Custom history period
python3 scripts/technicals.py AAPL --period 1y
```

Returns JSON with: `price`, `technicals` (RSI, MACD, SMAs, BBands, ATR), `trend`, `support`, `resistance`, `volume_profile_hvn`, `fundamentals`, and optionally `options`.

## Future Extensions

This project may expand to additional trading strategies and tooling over time.
