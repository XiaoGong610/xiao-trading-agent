---
description: Deep-dive research on a stock
---

Research the stock: $ARGUMENTS

This is a strategy-agnostic fundamentals and sentiment analysis. Focus on whether this is a good company to have conviction in — the user may use the research to inform any strategy (DCA, theta gang, buy-and-hold, etc.). Do NOT cover options-specific analysis (IV, Greeks, strikes, premiums).

**Step 1:** Run the data script to get current price, technicals, and fundamentals:
```bash
.venv/bin/python3 scripts/technicals.py $ARGUMENTS
```

**Step 2:** Use web search to gather qualitative information (news, earnings, analyst opinions).

Combine both sources to cover the following sections:

## Company Overview
- What the company does, sector, market cap
- Key products/services and revenue breakdown

## Growth & Financials
- Revenue and earnings growth (recent quarters + YoY)
- Margins (gross, operating, net) and trends
- Balance sheet health (debt, cash position)
- Free cash flow

## Recent Earnings
- Revenue: actual vs. estimate, YoY growth
- EPS: actual vs. estimate, YoY growth
- Management commentary: tone, strategic priorities, key quotes
- Guidance: next quarter and full year vs. consensus (raised, maintained, lowered?)
- Analyst Q&A highlights: toughest questions, any evasiveness or surprising candor
- Market reaction: stock move after earnings, analyst rating/target changes
- Next earnings date

## Market Sentiment
- Analyst consensus (buy/hold/sell breakdown, average price target)
- Institutional activity (any notable buys/sells)
- Recent news or catalysts

## Risks
- Key risks to the thesis
- Upcoming binary events

## Summary
- Bull case vs. bear case (1-2 sentences each)
- Overall take: bullish, neutral, or bearish — with reasoning

## Strategy Fit
Based on the stock's volatility, IV environment, growth profile, and price action, recommend which trading strategy fits best:
- **Buy & Hold** — long-term compounder, just accumulate shares
- **DCA** — conviction is there but timing is uncertain
- **LEAP Calls** — bullish with leverage, defined risk
- **Theta Gang** — rich premiums, range-bound or slight bullish bias
Pick one (or a combination) and explain why it suits this stock right now.

Save the output to `research/stocks/$ARGUMENTS.md` (use uppercase ticker as filename).
Start the entry with a date separator: `---` followed by `# TICKER — Research | YYYY-MM-DD`.
If the file already exists, prepend the new analysis above all previous entries (after the YAML frontmatter block). Never remove historical entries.

If creating a new file, add YAML frontmatter at the top:
```yaml
---
ticker: TICKER
status: researched
added_date: YYYY-MM-DD
sector: (infer from research)
thesis: "(one-line summary)"
---
```

**Update index & dashboard:**
```bash
.venv/bin/python3 scripts/update-index.py && .venv/bin/python3 scripts/dashboard.py
```
