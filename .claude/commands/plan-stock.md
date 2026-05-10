---
description: Full pre-trade analysis plan — research, strategy fit, and trade setup
---

Run a complete pre-trade analysis for: $ARGUMENTS

The argument is just a ticker (e.g., "AAPL", "TSLA").

This is the **orchestrator** — it chains together the research funnel, strategy selection, and trade setup in one shot. It pulls from existing research when available and fills gaps.

---

## Phase 1: Research

**Check for existing research:**
- Read `research/stocks/$TICKER.md` — if a recent `/research-stock` entry exists (<7 days old), summarize key findings and move to Phase 2.
- Read `research/sectors/` — check if the stock's sector has been scanned recently for broader context.

**If no existing research, or research is stale (>7 days old):** Run `/research-stock $TICKER` first. This will:
- Run `technicals.py` for quantitative data
- Web search for qualitative info (business model, earnings, sentiment)
- Save full output to `research/stocks/$TICKER.md`
- Include a Strategy Fit recommendation

Wait for the research to complete before proceeding.

**Conviction check** — based on the research output:
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

## Phase 3: Run Strategy Analysis

Run the applicable strategy skills to get concrete trade setups. Which skills to run depends on what's available:

**Always run:**
- `/strategy-buy-and-hold $TICKER`
- `/strategy-dca $TICKER`

**Run if US-listed options are available AND the user is not restricted from trading options on this stock:**
- `/strategy-theta-gang analyze $TICKER`
- `/strategy-leaps $TICKER`

**Trading restrictions check:** If the user has restrictions on this stock (check memory — e.g., trading windows, no options), skip restricted strategies and note the constraint.

Each skill will produce its own detailed analysis (entry, sizing, exit rules, risk management). Collect all outputs before proceeding to Phase 4.

---

## Phase 4: Compare & Recommend

With all strategy outputs in hand, compare them and pick the best fit:

| Factor | Consider |
|--------|----------|
| Valuation | Stretched → favors DCA over lump sum. Fair/cheap → Buy & Hold viable |
| IV environment | High IV → theta gang. Low IV → LEAPs or Buy & Hold |
| Timing | At support → Buy & Hold. Uncertain → DCA. Pre-earnings → Wait |
| Options liquidity | Illiquid or unavailable → stock-based strategies only |
| Growth profile | Compounder → Buy & Hold/DCA. Range-bound → Theta Gang |
| User's position | Already owns shares? → CC or add via DCA. No position → CSP or Buy & Hold |

**Recommendation:** Pick the best strategy (or combination) with clear reasoning. Reference the specific trade setup from the winning strategy skill's output.

---

## Phase 5: Final Checklist

- [ ] Conviction in the company? (Phase 1)
- [ ] Entry timing makes sense given technicals? (Phase 2)
- [ ] Strategy skills have been run and outputs collected? (Phase 3)
- [ ] Best strategy selected with clear reasoning? (Phase 4)
- [ ] No earnings/ex-div landmines in the trade window? (Phase 2)
- [ ] Specific trade setup defined with entry, exit, and risk? (Phase 3-4)
- [ ] Position sizing appropriate for portfolio?

**Final Verdict:** Go / No-Go / Wait — with a one-line summary, recommended strategy, and next action.

If "Wait": specify what trigger or date to revisit (e.g., "Wait for post-earnings May 11, then re-run `/plan-stock`").

---

Save the output to `research/stocks/$TICKER.md` (use uppercase ticker as filename).
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

If the file already exists and has frontmatter:
- If status is `researched`, update it to `watching` (plan promotes to watchlist)
- Update `entry_target` and `strategies` based on Phase 4 results
- Prepend the new analysis entry below the frontmatter

**Update `research/stocks/0-INDEX.md`** — move the ticker to the `Watching` section if not already there.
