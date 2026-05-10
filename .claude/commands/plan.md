---
description: Full pre-trade analysis plan — research, strategy fit, and trade setup
---

Run a complete pre-trade analysis for: $ARGUMENTS

The argument is just a ticker (e.g., "AAPL", "TSLA").

This chains together research → strategy selection → trade setup in one shot. Work through each phase sequentially.

**Step 1:** Run the data script upfront to get price, technicals, fundamentals, and options data:
```bash
source .venv/bin/activate && python3 scripts/technicals.py $ARGUMENTS --options
```

Use this data throughout all phases below. Supplement with web search for qualitative info (news, analyst opinions, earnings details) that the script can't provide.

---

## Phase 1: Conviction Check

Use the fundamentals from the script output + web search to assess:
- What the company does, market cap, sector
- Revenue/earnings growth trend (accelerating, stable, declining?)
- Balance sheet: healthy or overleveraged?
- Recent news: anything alarming?
- Analyst consensus: broadly bullish, neutral, or bearish?

**Verdict:** Pass / Fail — do you have conviction in this company?

If Fail → stop here.

---

## Phase 2: Market Context

Use the script's `price`, `technicals`, `support`, `resistance`, and `options` data:
- Current stock price, 5-day and 1-month trend
- Technical levels: key support AND resistance
- Where is price relative to 52-week range?
- IV rank and IV percentile — is premium rich or cheap?
- Upcoming events: earnings date, ex-dividend date, binary catalysts

---

## Phase 3: Strategy Fit

Based on conviction, market context, and the stock's profile, recommend the best strategy:

| Strategy | Best When |
|----------|-----------|
| **Buy & Hold** | High-conviction compounder, long time horizon, want full upside |
| **DCA** | Conviction is there but timing is uncertain, want to average in |
| **LEAP Calls** | Bullish with leverage, defined risk, stock has clear catalysts ahead |
| **Theta Gang (CSP)** | Bullish, want to enter at a discount, IV is elevated, stock at support |
| **Theta Gang (CC)** | Own shares, want income, stock near resistance or range-bound |
| **Theta Gang (PMCC)** | Bullish long-term, low IV, want leverage + income, less capital than CC |
| **Theta Gang (Iron Condor)** | Neutral/range-bound, want to collect premium from both sides |

Pick the best fit (or a combination) and explain why. Consider:
- Does the stock's volatility suit options selling or buying?
- Is IV rich enough for theta gang, or too low (favoring LEAPs/buy & hold)?
- Is the growth profile better suited for long-term holding or income extraction?
- Does the user already own shares? (If unknown, analyze both paths)

---

## Phase 4: Trade Setup

Based on the chosen strategy, provide specific execution details:

**If Buy & Hold:**
- Entry price / target buy zone (support levels)
- Position sizing suggestion
- What would change the thesis (stop-loss level or thesis-break triggers)

**If DCA:**
- Suggested schedule (weekly, biweekly, monthly)
- Per-period amount or share count
- How long to DCA (until position is full-sized)
- Price level where you'd accelerate or pause

**If LEAP Calls:**
- Strike: ATM for balanced, deep ITM (delta 0.70-0.80) for stock replacement
- Expiry: 9-12+ months out
- Premium cost and max risk
- Breakeven at expiry
- Delta, theta decay rate
- Exit plan: target profit %, stop-loss level

**If Theta Gang:**
- Refer user to `/theta-gang analyze $TICKER` for detailed options setup
- Quick summary: suggested strategy (CSP/CC/PMCC/IC), approximate strike zone, target DTE

---

## Phase 5: Final Checklist

- [ ] Conviction in the company? (Phase 1)
- [ ] Entry timing makes sense given technicals? (Phase 2)
- [ ] No earnings/ex-div landmines in the trade window? (Phase 2)
- [ ] Strategy matches the stock's profile? (Phase 3)
- [ ] Specific trade setup defined with entry, exit, and risk? (Phase 4)
- [ ] Position sizing appropriate for portfolio?

**Final Verdict:** Go / No-Go with a one-line summary and the recommended strategy.

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
