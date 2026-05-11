# Project Notes

A living document for brainstorming, discussions, decisions, and TODOs.

---

## Decisions Made

### Skill Naming Convention (2026-05-09)
- `research-*` — research skills
- `strategy-*` — strategy-specific skills
- `trade-*` — portfolio/trade management
- `plan-*` — orchestrator skills
- `util-*` — utility tools

### Research Funnel (2026-05-09)
Cost-aware top-down funnel:
1. `/research-scan-market` (cheap) → many sectors
2. `/research-scan-sector` (moderate) → 5-10 candidates per sector
3. `/research-stock` (moderate) → deep-dive on candidates worth investigating
4. `/research-compare-stocks` (cheap) → narrow to top 2-3
5. `/plan-stock` (expensive) → only run on stocks you're seriously considering

### Folder Structure (2026-05-10)
- `research/stocks/` — one file per stock, accumulates research + plans
- `research/sectors/` — sector scans
- `research/comparisons/` — head-to-head comparisons
- `portfolio/` — active positions
- `trades/` — closed trade log
- Status lifecycle: `researched → watching → in-portfolio → removed`
- `0-INDEX.md` groups stocks by actionability (Ready / Wait / Watching / Not Planned)

### Multi-Strategy Framework (2026-05-09)
Four strategies: Buy & Hold, DCA, LEAP Calls, Theta Gang. Research recommends strategy fit. Plan runs all applicable strategy skills and compares.

### DCA Preference (2026-05-10)
- Daily DCA by default
- Three approaches: Static Recurring, Limit Buys at Support, Hybrid Zone-Based
- For restricted stocks: plan per trading window, not per day

### AI Capital Flow Framework (2026-05-10)
Bottleneck progression: GPU → HBM → Cluster Scaling → Optical → next
Five tracks: Memory, I/O Interconnect, Optical, Power/Cooling, Custom ASIC
Key insight: "Don't chase hot spots — position ahead of the bottleneck shift."

---

## Discussions & Ideas

### ETF vs. Individual Stocks (2026-05-10)
- `/research-scan-sector` includes relevant ETFs
- `/research-compare-stocks` includes ETF alternative analysis
- ETFs win when: can't pick a winner, want diversification, limited capital
- Individual stocks win when: high conviction, want theta gang (need higher IV), ETF dilutes thesis

### Comparison Grouping (2026-05-10)
Comparisons can be within-sector or cross-sector. Saved to `research/comparisons/` with flexible naming.

---

## TODOs

### 1. Capture Current Holdings & Trades
Import existing portfolio positions and trade history so `/trade-portfolio` has real data. Without this, the agent can't factor in existing positions when recommending strategies.

- [ ] Build `/trade-import` skill to bulk-load positions into `portfolio/` files
- [ ] Support importing from brokerage exports (CSV) or manual entry
- [ ] Populate frontmatter with strategy, entry date, cost basis, etc.

### 2. Refine & Test Trade Skills
The trade lifecycle skills (`trade-open`, `trade-close`, `trade-review`, `trade-portfolio`) have been built but never tested with real data. Depends on #1 — need real positions first, then run through the full lifecycle.

- [ ] Test `/trade-open` — log a real position, verify frontmatter and portfolio file creation
- [ ] Test `/trade-review` — review an active position, verify technicals integration
- [ ] Test `/trade-close` — close a position, verify P&L calculation and move to `trades/`
- [ ] Test `/trade-portfolio` — dashboard with active positions, trade history, and candidates summary
- [ ] Verify index (`0-INDEX.md`) status transitions work end-to-end
- [ ] Refine skills based on real usage — same way we improved research and plan skills

### 3. Market Intelligence Skills
Add continuous monitoring capabilities beyond point-in-time research snapshots.

- [ ] **Whale tracking** — institutional buys/sells, 13F filings, insider transactions, unusual options activity (dark pool, large blocks)
- [ ] **Social sentiment** — monitor X (Twitter) for trending tickers and sentiment shifts, Reddit (r/wallstreetbets, r/options), StockTwits
- [ ] **News alerts** — breaking news, FDA decisions, earnings surprises, analyst upgrades/downgrades
- [ ] Consider using `/loop` for periodic monitoring

### 4. Scheduled Cloud Agents
Set up Claude Code cloud triggers to run jobs on a recurring schedule — so research and monitoring happen automatically without manual invocation.

- [ ] Daily: refresh technicals for all watching stocks
- [ ] Weekly: re-run `/research-scan-market` for sector rotation updates
- [ ] Pre-earnings: auto-flag stocks in watchlist with earnings approaching within 7 days
- [ ] Explore Claude Code `/schedule` for cron-based remote agent triggers

### 5. Leveraged ETF Strategy
When considering strategies, also evaluate leveraged single-stock ETFs as an alternative to options for gaining leveraged exposure. Examples: TSLL (2x TSLA), CONL (2x COIN), NVDL (2x NVDA), etc.

- [ ] Research available leveraged ETFs for stocks on our watchlist
- [ ] Add leveraged ETF consideration to `/plan-stock` — when recommending LEAPs or Buy & Hold, compare with the leveraged ETF alternative
- [ ] Document the tradeoffs: daily rebalancing decay, no options needed, simpler execution, but volatility drag on long holds
- [ ] Add to `/strategy-buy-and-hold` and `/strategy-dca` — "would a leveraged ETF be more capital-efficient here?"
- [ ] Consider as a strategy of its own (`/strategy-leveraged-etf`?) or fold into existing strategies
