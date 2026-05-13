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

### Knowledge Base — Hybrid Approach (2026-05-12)
Build a knowledge layer so the agent makes better decisions over time. Two components:

**1. Knowledge files** (start here) — human-readable reference docs that skills can consult:
```
knowledge/
  sectors/              — sector-specific logic (what metrics matter, cycle dynamics)
  strategies/           — when to use each strategy, edge cases, rules of thumb
  frameworks/           — reusable mental models (AI capital flow, valuation benchmarks)
  signals/              — how to interpret RSI, IV rank, P/E in different contexts
```

**2. Scoring scripts** (build later) — systematic ranking of stocks by composite signals:
- `scripts/screener.py` — input tickers, output ranked list by composite score
- Rules codified in Python, not prompt-dependent
- Consistent, fast, no token cost

**Why hybrid:** Knowledge files handle nuance and context (when does low P/E NOT mean cheap?). Scripts handle systematic scoring (rank 42 stocks). Skills reference both.

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

### 6. Knowledge Base
Build a knowledge layer for smarter decision-making. Start with knowledge files, add scoring scripts later.

**Phase 1 — Knowledge files:**
- [ ] `knowledge/sectors/semiconductors.md` — cycle dynamics, HBM/NAND drivers, key metrics, valuation benchmarks
- [ ] `knowledge/sectors/energy.md` — oil price drivers, toll-model vs upstream, geopolitical risk framework
- [ ] `knowledge/sectors/software.md` — SaaS metrics (NRR, ARR), AI disruption vs AI adoption framework
- [ ] `knowledge/strategies/when-to-csp.md` — IV rank thresholds, delta/DTE rules, earnings avoidance, capital requirements
- [ ] `knowledge/strategies/when-to-dca.md` — RSI zones, volatility-based sizing, daily vs window-based
- [ ] `knowledge/strategies/when-to-leaps.md` — IV environment, delta selection, vega risk
- [ ] `knowledge/frameworks/capital-flow.md` — AI bottleneck progression, 5 tracks, how to position ahead
- [ ] `knowledge/frameworks/valuation.md` — P/E benchmarks by sector, what "cheap" means in context
- [ ] `knowledge/signals/rsi-guide.md` — context-dependent interpretation, sector differences
- [ ] `knowledge/signals/iv-rank-guide.md` — when to sell vs buy premium, thresholds

**Phase 2 — Scoring scripts:**
- [ ] `scripts/screener.py` — composite scoring (RSI + fwd P/E + gap-to-target + IV rank)
- [ ] Wire into `/research-compare-stocks` for systematic ranking
- [ ] Backtest scoring logic against past recommendations
