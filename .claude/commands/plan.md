---
description: Full pre-trade analysis plan for a theta gang candidate
---

Run a complete theta gang pre-trade analysis for: $ARGUMENTS

The argument is just a ticker (e.g., "AAPL", "TSLA").

This chains together the full workflow in one shot. Work through each phase sequentially.
Always analyze BOTH the CSP path (don't own shares) and CC path (own shares) so the user can decide based on their current position.

---

## Phase 1: Conviction Check

Use web search to quickly assess:
- What the company does, market cap, sector
- Revenue/earnings growth trend (accelerating, stable, declining?)
- Balance sheet: healthy or overleveraged?
- Recent news: anything alarming?
- Analyst consensus: broadly bullish, neutral, or bearish?

**Two-way verdict:**
- **For CSP:** Would you be comfortable owning 100 shares at a ~10-15% discount?
- **For CC:** Is this a stock worth continuing to hold? Any reason to exit outright instead?

**Verdict:** Pass / Fail (may pass for one path but not the other)

If Fail on both → stop here.

---

## Phase 2: Options Environment

Is this a good theta gang setup *right now*?

Use web search to gather options data:
- Current stock price, 5-day and 1-month trend
- IV rank and IV percentile — is premium rich?
- Options liquidity: volume, open interest, bid-ask spreads
- **Earnings date**: if within 30-45 DTE → disqualifier unless intentionally playing IV crush
- **Ex-dividend date**: if within window, flag the expected price drop
- Technical levels: key support AND resistance levels

**CSP lens:**
- Entry timing: is stock pulling back (ideal) or breaking out (sell at breakout level)?
- Support levels: where would you want to be assigned?

**CC lens:**
- Entry timing: is stock rallying into resistance (ideal for CC) or pulling back (less premium)?
- Resistance levels: where would you be comfortable letting shares get called away?

**Verdict:** Pass / Fail — is the options environment favorable?

If Fail → stop here. Explain why and when to revisit.

---

## Phase 3: Strategy Recommendations

Analyze BOTH paths:

### Path A: Don't Own Shares

| Condition | Strategy |
|-----------|----------|
| Bullish, want to enter at a discount | CSP |
| Bullish long-term, low IV, less capital | PMCC |
| Neutral/range-bound | Iron Condor |

Pick the best fit for this path and explain why.

### Path B: Own 100+ Shares

| Condition | Strategy |
|-----------|----------|
| Slightly bullish/neutral, want income | CC |
| Bullish long-term, want income on both sides | CC + CSP (wheel) |
| Neutral, want max income | CC with more aggressive (closer to ATM) strike |

Pick the best fit for this path and explain why.

---

## Phase 4: Strike & Expiry Recommendations

### Path A: CSP Recommendation

- **Strike**: at or below support, delta 0.20-0.30, a price you'd happily own at
- **Expiration**: specific date, DTE (30-45 sweetspot)
- **Premium**: estimated credit per share and per contract
- **Greeks**: delta, theta ($/day), vega, gamma
- **Probability of profit**
- **Max profit / Max loss / Breakeven**
- **Buying power reduction**
- **Annualized return**: at full profit and at 50% early close

Plus 1 alternative (different strike or expiry).

### Path B: CC Recommendation

- **Strike**: above cost basis (note: ask user for cost basis or assume current price), at resistance / take-profit level, delta 0.20-0.30
- **Expiration**: specific date, DTE (30-45 sweetspot)
- **Premium**: estimated credit per share and per contract
- **Greeks**: delta, theta ($/day), vega, gamma
- **Probability of profit** (that shares are NOT called away)
- **Max profit**: premium + (strike - cost basis) × 100
- **Downside protection**: cost basis minus premium collected
- **Annualized return**: at full profit and at 50% early close

Plus 1 alternative (different strike or expiry).

---

## Phase 5: Final Checklist

**Common checks:**
- [ ] Conviction in the company? (Phase 1)
- [ ] IV rank justifies selling premium? (Phase 2)
- [ ] No earnings/ex-div landmines in the window? (Phase 2)
- [ ] DTE in 30-45 day sweetspot? (Phase 4)
- [ ] Delta 0.20-0.30? (Phase 4)
- [ ] Options are liquid (tight bid-ask)? (Phase 2)
- [ ] Plan for management: close at 50% profit, roll rules clear? (Standing rule)

**Path A (CSP) checks:**
- [ ] Strike is at a price you'd be happy to own at?
- [ ] Enough buying power for assignment (~100 × strike)?

**Path B (CC) checks:**
- [ ] Strike is above your cost basis?
- [ ] Strike is at a price you'd be happy to sell at?
- [ ] Comfortable with capped upside if stock rallies past strike?

**Final Verdict for each path:** Go / No-Go with a one-line summary.

**Community check:**
Before pulling the trigger, check what other traders are doing on this ticker at [thetagang.com/symbols/$TICKER](https://thetagang.com/symbols/$TICKER). Filter by strategy type and look at winners/losers to validate your setup.

---

Save the output to `theta-gang/$TICKER.md` (use uppercase ticker as filename).
Start the entry with a date separator: `---` followed by `# TICKER — Pre-Trade Plan | YYYY-MM-DD`.
If the file already exists, prepend the new analysis above all previous entries (after the file title). Never remove historical entries.
