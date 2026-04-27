---
description: Deep-dive research on a stock
---

Research the stock: $ARGUMENTS

This is a strategy-agnostic fundamentals and sentiment analysis. Focus on whether this is a good company to have conviction in — the user may use the research to inform any strategy (DCA, theta gang, buy-and-hold, etc.). Do NOT cover options-specific analysis (IV, Greeks, strikes, premiums).

Use web search to gather current information. Cover the following sections:

## Company Overview
- What the company does, sector, market cap
- Key products/services and revenue breakdown

## Growth & Financials
- Revenue and earnings growth (recent quarters + YoY)
- Margins (gross, operating, net) and trends
- Balance sheet health (debt, cash position)
- Free cash flow

## Recent Earnings
- Last earnings call highlights (beat/miss, guidance, key quotes from management)
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

Save the output to `research/$ARGUMENTS.md` (use uppercase ticker as filename).
Start the entry with a date separator: `---` followed by `# TICKER — Research | YYYY-MM-DD`.
If the file already exists, prepend the new analysis above all previous entries (after the file title). Never remove historical entries.
