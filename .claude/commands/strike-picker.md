---
description: Compare strike/expiry combos for a theta gang trade
---

Analyze strike and expiry options for: $ARGUMENTS

The argument format is: TICKER STRATEGY (e.g., "AAPL CSP", "TSLA CC", "NVDA PMCC", "AMZN IC")

**Step 1:** Run the data script to get real options chain data:
```bash
source .venv/bin/activate && python3 scripts/technicals.py $TICKER --options
```
(Extract the ticker from the arguments.)

Use the script's output for price, support/resistance, IV, and options chain data. Supplement with web search only if needed.

## Current Setup
- Stock price, 52-week range, recent trend
- IV rank / IV percentile
- Next earnings date and ex-dividend date (flag if within the trade window)

## Strike/Expiry Comparison Table

Build a comparison table with 3-5 candidates. Follow these rules:
- **CSP**: delta 0.20-0.30, strike at support levels or a price you'd be happy owning
- **CC**: strike above cost basis, at resistance / take-profit level
- **PMCC**: long leg delta 0.80-0.90 (far out expiry), short leg delta 0.20-0.30 (30-45 DTE)
- **Iron Condor**: sell both sides at ~16 delta, buy wings further out

For each candidate, include:
| Strike | Expiry (DTE) | Delta | Premium | PoP | Max Profit | Max Loss | Breakeven | Annualized Return |

## Theta Decay Analysis
- How much theta ($/day) does each candidate earn?
- Is the DTE in the 30-45 day sweetspot?
- Gamma risk assessment — any candidates too close to expiry?

## Recommendation
- Which specific strike/expiry combo offers the best risk/reward?
- Why this one over the others?

Do NOT save output to a file — this is a live analysis tool for decision-making.
