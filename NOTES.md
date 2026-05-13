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

### 1. Capture Current Holdings & Trades ⬆️ HIGH
Import existing portfolio positions and trade history so `/trade-portfolio` has real data. Without this, the agent can't factor in existing positions when recommending strategies.

- [ ] Build `/trade-import` skill to bulk-load positions into `portfolio/` files
- [ ] Support importing from brokerage exports (CSV) or manual entry
- [ ] Populate frontmatter with strategy, entry date, cost basis, etc.

### 2. Refine & Test Trade Skills ⬆️ HIGH (depends on #1)
The trade lifecycle skills (`trade-open`, `trade-close`, `trade-review`, `trade-portfolio`) have been built but never tested with real data.

- [ ] Test `/trade-open` — log a real position, verify frontmatter and portfolio file creation
- [ ] Test `/trade-review` — review an active position, verify technicals integration
- [ ] Test `/trade-close` — close a position, verify P&L calculation and move to `trades/`
- [ ] Test `/trade-portfolio` — dashboard with active positions, trade history, and candidates summary
- [ ] Verify index (`0-INDEX.md`) status transitions work end-to-end
- [ ] Refine skills based on real usage — same way we improved research and plan skills

### 3. Risk & Portfolio Management ⬆️ HIGH
Prevent overconcentration and size positions properly. Critical before scaling up positions.

- [ ] **Correlation analysis** — measure how correlated watching/portfolio stocks are. Flag if 80% of positions move together (e.g., all AI semis drop on one NVDA miss)
- [ ] **Allocation framework** — define max % per stock, per sector, per theme. Enforce in `/plan-stock` recommendations
- [ ] **Position sizing calculator** — Kelly criterion or fixed-risk model. Input: conviction level, volatility, portfolio size → output: how many shares/contracts
- [ ] Add a portfolio risk section to `/trade-portfolio` dashboard showing sector concentration, correlation heatmap, and allocation vs. limits

### 4. Knowledge Base 🔄 IN PROGRESS
Build a knowledge layer for smarter decision-making. Start with knowledge files, add scoring scripts later.

**Phase 1 — Knowledge files (4 done, 6 remaining):**
- [x] `knowledge/signals/rsi-guide.md`
- [x] `knowledge/signals/iv-rank-guide.md`
- [x] `knowledge/frameworks/capital-flow.md`
- [x] `knowledge/frameworks/valuation.md`
- [ ] `knowledge/sectors/semiconductors.md` — cycle dynamics, HBM/NAND drivers, key metrics
- [ ] `knowledge/sectors/energy.md` — oil price drivers, toll-model vs upstream, geopolitical risk
- [ ] `knowledge/sectors/software.md` — SaaS metrics (NRR, ARR), AI disruption vs adoption
- [ ] `knowledge/strategies/when-to-csp.md` — IV rank thresholds, delta/DTE rules, earnings avoidance
- [ ] `knowledge/strategies/when-to-dca.md` — RSI zones, volatility-based sizing, daily vs window-based
- [ ] `knowledge/strategies/when-to-leaps.md` — IV environment, delta selection, vega risk

**Phase 2 — Scoring scripts:**
- [ ] `scripts/screener.py` — composite scoring (RSI + fwd P/E + gap-to-target + IV rank)
- [ ] Wire into `/research-compare-stocks` for systematic ranking
- [ ] Backtest scoring logic against past recommendations

### 5. Macro Regime Detection ➡️ MEDIUM
Different market regimes favor different strategies. The agent should adapt.

- [ ] **Regime classification** — bull / bear / sideways / high-vol / low-vol, based on S&P trend, VIX level, yield curve, breadth
- [ ] **Strategy mapping by regime:**
  - Bull + low vol → Buy & Hold, DCA, LEAPs
  - Bull + high vol → DCA (not lump sum), CSPs at support
  - Bear → CSPs get assigned more (danger), defensive stocks, cash-heavy
  - Sideways → Theta gang shines (range-bound = premium selling paradise)
- [ ] Integrate into `/research-scan-market` — report current regime and strategy implications
- [ ] Add to knowledge base: `knowledge/frameworks/macro-regimes.md`

### 6. Market Intelligence Skills ➡️ MEDIUM
Add continuous monitoring capabilities beyond point-in-time research snapshots.

- [ ] **Whale tracking** — institutional buys/sells, 13F filings, insider transactions, unusual options activity (dark pool, large blocks)
- [ ] **Social sentiment** — monitor X (Twitter) for trending tickers and sentiment shifts, Reddit (r/wallstreetbets, r/options), StockTwits
- [ ] **News alerts** — breaking news, FDA decisions, earnings surprises, analyst upgrades/downgrades
- [ ] Consider using `/loop` for periodic monitoring

### 7. Scheduled Cloud Agents ➡️ MEDIUM
Set up Claude Code cloud triggers to run jobs on a recurring schedule.

- [ ] Daily: refresh technicals for all watching stocks
- [ ] Weekly: re-run `/research-scan-market` for sector rotation updates
- [ ] Pre-earnings: auto-flag stocks in watchlist with earnings approaching within 7 days
- [ ] Explore Claude Code `/schedule` for cron-based remote agent triggers

### 8. Multi-Timeframe Analysis ⬇️ LOW
Daily RSI tells one story; weekly/monthly tell another. Combining timeframes gives higher conviction signals.

- [ ] Add weekly and monthly RSI to dashboard alongside daily
- [ ] **Confluence signals** — daily oversold + weekly at support + monthly uptrend = highest conviction entry
- [ ] Update `scripts/dashboard.py` to fetch and display multi-timeframe RSI
- [ ] Add to knowledge base: `knowledge/signals/multi-timeframe.md`
- [ ] Consider adding weekly/monthly SMA alignment (e.g., price above monthly SMA 10 = long-term uptrend intact)

### 9. Leveraged ETF Strategy ⬇️ LOW
Evaluate leveraged single-stock ETFs as alternative to options. Examples: TSLL (2x TSLA), CONL (2x COIN), NVDL (2x NVDA).

- [ ] Research available leveraged ETFs for stocks on our watchlist
- [ ] Add leveraged ETF consideration to `/plan-stock`
- [ ] Document the tradeoffs: daily rebalancing decay, no options needed, volatility drag on long holds
- [ ] Consider as a strategy of its own (`/strategy-leveraged-etf`?) or fold into existing strategies

### 10. Tax Optimization 📅 SEASONAL
Maximize after-tax returns. Critical before year-end.

- [ ] **Wash sale tracking** — flag if you sell a stock at a loss and rebuy within 30 days
- [ ] **Tax-loss harvesting** — identify positions with unrealized losses that could offset gains
- [ ] **Short-term vs. long-term gains** — track holding periods (>1 year = favorable rate)
- [ ] **End-of-year review** — annual skill to scan portfolio for tax optimization before Dec 31
- [ ] Add to knowledge base: `knowledge/frameworks/tax-rules.md`
