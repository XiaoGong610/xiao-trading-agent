---
description: Analyze a stock's options setup for theta gang trading
---

Analyze the options setup for theta gang trading: $ARGUMENTS

This is a pure options mechanics analysis. Do NOT cover company fundamentals, growth, or earnings quality — that belongs in `/research`. Assume the user already has conviction on the stock.

**Step 1:** Run the data script to get price, technicals, and options data:
```bash
source .venv/bin/activate && python3 scripts/technicals.py $ARGUMENTS --options
```

Use the script's output for IV, price, support/resistance levels, and expiry data. Supplement with web search only for qualitative info the script can't provide.

## Options Environment
- Current stock price and recent trend (from script's `price` and `technicals`)
- IV rank and IV percentile — is premium rich right now? (from script's `options`)
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

Save the output to `watchlist/$ARGUMENTS.md` (use uppercase ticker as filename).
Start the entry with a date separator: `---` followed by `# TICKER — Theta Gang Analysis | YYYY-MM-DD`.
If the file already exists, prepend the new analysis above all previous entries (after the YAML frontmatter block). Never remove historical entries.

If creating a new file, add YAML frontmatter at the top:
```yaml
---
ticker: TICKER
status: watching
added_date: YYYY-MM-DD
sector: (infer from context)
thesis: "(one-line summary)"
entry_target: (recommended strike)
strategies: [CSP, CC]
---
```

If the file already exists and has frontmatter, do not modify the frontmatter — only prepend the new analysis entry below it.
