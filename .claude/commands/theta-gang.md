---
description: Analyze a stock's options setup for theta gang trading
---

Analyze the options setup for theta gang trading: $ARGUMENTS

This is a pure options mechanics analysis. Do NOT cover company fundamentals, growth, or earnings quality — that belongs in `/research`. Assume the user already has conviction on the stock.

Use web search to gather current options chain data, IV data, and key dates.

## Options Environment
- Current stock price and recent trend (5-day, 1-month)
- IV rank and IV percentile — is premium rich right now?
- Options liquidity: volume, open interest, bid-ask spreads on near-the-money strikes
- Theta decay curve: where are we on the 90→0 DTE curve?

## Key Dates (Disqualifiers)
- Next earnings date — if within 30-45 DTE window, flag as a risk or disqualifier
- Next ex-dividend date — stock typically drops by dividend amount
- Any other binary events (FDA, legal rulings, etc.)

## Recommended Trades
Suggest 1-2 setups. For each:
- **Strategy**: CSP / CC / PMCC / Iron Condor
- **Strike(s)**: specific prices with delta (target 0.20-0.30 for selling)
- **Expiration**: specific date, DTE (target 30-45 DTE sweetspot)
- **Premium**: estimated credit received per share and per contract
- **Greeks snapshot**: delta, theta ($/day earned), vega exposure, gamma risk
- **Probability of profit**
- **Max profit / Max loss / Breakeven**
- **Buying power reduction**
- **Annualized return**: if held to expiry, and if closed at 50% profit

## Risk Assessment
- Gamma risk (especially if DTE < 21)
- Vega risk (will IV likely expand or contract?)
- Assignment risk at this strike
- What would trigger a roll or early close?

## Verdict
- Go / no-go for theta gang right now
- If go: best specific trade with reasoning
- Check what other traders are doing on this ticker at [thetagang.com/symbols/$ARGUMENTS](https://thetagang.com/symbols/$ARGUMENTS) — filter by strategy type, look at winners/losers to validate your setup

Save the output to `theta-gang/$ARGUMENTS.md` (use uppercase ticker as filename).
Start the entry with a date separator: `---` followed by `# TICKER — Theta Gang Analysis | YYYY-MM-DD`.
If the file already exists, prepend the new analysis above all previous entries (after the file title). Never remove historical entries.
