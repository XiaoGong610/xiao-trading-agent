---
description: Full pre-trade analysis plan — research, strategy fit, and trade setup
---

Run a complete pre-trade analysis for: $ARGUMENTS

The argument is just a ticker (e.g., "AAPL", "TSLA").

This is the **orchestrator** — it chains together the research funnel, strategy selection, and trade setup in one shot. It pulls from existing research when available and fills gaps.

---

## Phase 1: Gather Context

**Check for existing research first:**
- Read `research/stocks/$TICKER.md` — if a recent `/research-stock` entry exists, summarize key findings. Don't redo work.
- Read `research/sectors/` — check if the stock's sector has been scanned recently for broader context.
- Read `research/sectors/market-overview.md` — pull current market pulse (sentiment, VIX, macro).

**If no existing research:** Run the research inline:
```bash
.venv/bin/python3 scripts/technicals.py $ARGUMENTS --options
```
Then use web search for qualitative info. Cover: business model, growth, earnings, sentiment (same as `/research-stock`).

**If existing research is stale (>7 days old):** Re-run the data script for fresh technicals, but reuse the qualitative research.

Summarize the conviction check:
- **Verdict:** Pass / Fail — do you have conviction?
- If Fail → stop here.

---

## Phase 2: Market Context & Timing

Use the script's `price`, `technicals`, `support`, `resistance`, and `options` data:
- Current stock price, 5-day and 1-month trend
- Technical levels: key support AND resistance
- Where is price relative to 52-week range?
- IV rank and IV percentile — is premium rich or cheap?
- Upcoming events: earnings date, ex-dividend date, binary catalysts
- Is now a good entry point, or should you wait?

---

## Phase 3: Strategy Fit

Based on conviction, market context, and the stock's profile, recommend the best strategy:

| Strategy | Best When | Skill |
|----------|-----------|-------|
| **Buy & Hold** | High-conviction compounder, long time horizon, want full upside | `/strategy-buy-and-hold` |
| **DCA** | Conviction but timing uncertain, want to average in | `/strategy-dca` |
| **LEAP Calls** | Bullish with leverage, defined risk, clear catalysts, IV is low | `/strategy-leaps` |
| **Theta Gang** | Elevated IV, range-bound or at support, happy to own shares | `/strategy-theta-gang analyze` |

Consider:
- Are US-listed options available? If not, only stock-based strategies apply (Buy & Hold, DCA).
- Does the stock's volatility suit options selling or buying?
- Is IV rich enough for theta gang, or too low (favoring LEAPs/buy & hold)?
- Is the growth profile better suited for long-term holding or income extraction?
- Does the user already own shares? (If unknown, analyze both paths)

Pick the best fit (or a combination) and explain why.

---

## Phase 4: Trade Setup

Based on the chosen strategy, provide specific execution details by running the relevant strategy skill inline:

**If Buy & Hold:** Follow `/strategy-buy-and-hold` framework:
- Entry price / target buy zone (support levels)
- Position sizing (% of portfolio, scaling plan)
- Thesis-break triggers and exit rules

**If DCA:** Follow `/strategy-dca` framework:
- Schedule (weekly, biweekly, monthly) and amount per period
- Total budget and duration
- Acceleration/pause rules

**If LEAP Calls:** Follow `/strategy-leaps` framework:
- Strike selection (deep ITM / ATM / OTM with rationale)
- Expiry (9-12+ months), premium, breakeven, delta
- Position sizing, stop loss, rolling plan

**If Theta Gang:** Follow `/strategy-theta-gang analyze` framework:
- Strategy (CSP/CC/PMCC/IC), strike, expiry, premium, Greeks
- Probability of profit, max profit/loss, annualized return
- Roll rules and management plan

---

## Phase 5: Final Checklist

- [ ] Conviction in the company? (Phase 1)
- [ ] Entry timing makes sense given technicals? (Phase 2)
- [ ] No earnings/ex-div landmines in the trade window? (Phase 2)
- [ ] Strategy matches the stock's profile? (Phase 3)
- [ ] Specific trade setup defined with entry, exit, and risk? (Phase 4)
- [ ] Position sizing appropriate for portfolio?

**Final Verdict:** Go / No-Go / Wait — with a one-line summary, recommended strategy, and next action.

If "Wait": specify what trigger or date to revisit (e.g., "Wait for post-earnings May 11, then re-run `/plan-stock`").

---

Save the output to `watchlist/$TICKER.md` (use uppercase ticker as filename).
Start the entry with a date separator: `---` followed by `# TICKER — Pre-Trade Plan | YYYY-MM-DD`.
If the file already exists, prepend the new analysis above all previous entries (after the YAML frontmatter block). Never remove historical entries.

If creating a new file, add YAML frontmatter at the top:
```yaml
---
ticker: TICKER
status: watching
added_date: YYYY-MM-DD
sector: (infer from research)
thesis: "(one-line summary of why this stock is interesting)"
entry_target: (target entry price from Phase 4)
strategies: [(recommended strategy from Phase 3)]
---
```

If the file already exists and has frontmatter, do not modify the frontmatter — only prepend the new analysis entry below it.
