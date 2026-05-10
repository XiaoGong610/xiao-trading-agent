---
description: Dollar Cost Averaging strategy — schedule, sizing, and tracking
---

DCA strategy analysis for: $ARGUMENTS

The argument format is: TICKER [TOTAL_BUDGET]
- TICKER: stock symbol (e.g., "AAPL")
- TOTAL_BUDGET: optional — total amount to invest (e.g., "AAPL 10000")

Assume the user already has conviction from `/research-stock` or `/plan-stock`. This skill focuses on building a DCA plan: schedule, amounts, and guardrails.

**Step 1:** Run the data script:
```bash
.venv/bin/python3 scripts/technicals.py $ARGUMENTS
```
(Extract the ticker from the arguments.)

Use the script's output for price, volatility, and support/resistance. Supplement with web search for upcoming catalysts.

## Stock Profile for DCA

- Current price and 52-week range
- Average daily/weekly volatility (ATR) — helps set expectations for price swings between buys
- Upcoming events: earnings dates, ex-div dates in the DCA window
- Is the stock in an uptrend, downtrend, or range? (DCA works in all, but sets expectations)

## DCA Plan

- **Schedule**: weekly, biweekly, or monthly — recommend based on stock volatility and budget
  - Higher volatility → more frequent buys (capture more dips)
  - Lower volatility → less frequent is fine
- **Amount per period**: fixed dollar amount (e.g., $500/week)
- **Total budget**: if provided, calculate how many periods to reach full position
- **Number of shares per buy**: at current price, how many shares per period
- **Duration**: how long to DCA (e.g., 3 months, 6 months)
- **Target position size**: total shares/dollars when complete

## Acceleration & Pause Rules

- **Accelerate buys if**: stock drops X% below average cost (buy more on dips)
- **Pause buys if**: thesis-breaking news, earnings miss, or stock drops below a key support level that changes the outlook
- **Stop entirely if**: thesis breaks — specific triggers

## Example Schedule

Show a sample schedule with dates and expected buys:

| Date | Amount | Est. Shares | Running Total | Running Cost Basis |
|------|--------|-------------|---------------|-------------------|

(Use the DCA schedule and current price to project the first 4-6 buys.)

## Tracking

- Track average cost basis as buys accumulate
- Review thesis at each earnings report
- Reassess DCA plan if stock moves ±20% from starting price

Save the output to `watchlist/$TICKER.md` (use uppercase ticker as filename).
Start the entry with: `---` followed by `# TICKER — DCA Plan | YYYY-MM-DD`.
If the file already exists, prepend above previous entries (after YAML frontmatter). Never remove historical entries.

If creating a new file, add YAML frontmatter:
```yaml
---
ticker: TICKER
status: watching
added_date: YYYY-MM-DD
sector: (infer from research)
thesis: "(one-line summary)"
entry_target: (current price — DCA starts at market)
strategies: [dca]
---
```
