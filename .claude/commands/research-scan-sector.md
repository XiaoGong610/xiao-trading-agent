---
description: Research a market sector and identify candidate stocks
---

Research the following sector or theme and identify candidate stocks: $ARGUMENTS

The argument can be a traditional sector (e.g., "healthcare", "energy", "financials") or a cross-sector investment theme (e.g., "ai-infrastructure", "defense", "glp-1"). Themes cut across traditional sector boundaries — pull relevant stocks from wherever they sit.

Use web search to analyze the current state of this sector. Cover:

## Sector Overview
- What's driving the sector right now (macro trends, catalysts, headwinds)
- Recent performance vs. S&P 500 (outperforming, underperforming, in line?)
- Key themes (e.g., AI spend, rate sensitivity, regulatory changes)

## Top Performers
- 3-5 stocks leading the sector and why
- Recent earnings highlights from sector leaders

## Laggards / Turnaround Candidates
- 2-3 stocks underperforming that could be interesting on a pullback
- What would need to change for them to turn around

## Sector Risks
- Key risks that could hurt the sector broadly
- Upcoming events (earnings season, regulatory decisions, macro data)

## Candidate Ranking

Rank 5-10 stocks from this sector worth investigating:

| Rank | Ticker | Why Interesting | Valuation | Growth | Options Liquid? | Verdict |
|------|--------|----------------|-----------|--------|-----------------|---------|

For each candidate, briefly note:
- Valuation (cheap, fair, expensive relative to growth)
- Growth trajectory (accelerating, stable, declining)
- Whether options are liquid enough for options strategies (if relevant)
- Overall interest: Strong / Moderate / Watch Later

## Relevant ETFs

Identify ETFs that cover this sector or theme:

| ETF | Name | Thesis Match | IV / Options | Verdict |
|-----|------|-------------|-------------|---------|

For each ETF, note:
- How well it matches the sector thesis (what % is relevant vs. dead weight?)
- Whether it has liquid options (for theta gang viability)
- Whether DCA into the ETF makes more sense than picking individual stocks

## Top Picks
Highlight the top 2-3 candidates and suggest next steps:
- Run `/research-stock TICKER` for a deep-dive on fundamentals
- Run `/trade-watch TICKER` to add to watchlist for monitoring
- Run `/plan-stock TICKER` for full pre-trade analysis

Save the output to `research/sectors/$SECTOR.md` (use lowercase sector name as filename, e.g., `software.md`).
Start the entry with a date separator: `---` followed by `# Sector — SECTOR | YYYY-MM-DD`.
If the file already exists, prepend the new analysis above all previous entries (after the file title). Never remove historical entries.
