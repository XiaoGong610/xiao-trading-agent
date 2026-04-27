---
description: Analyze whether to roll an existing theta gang position
---

Analyze rolling options for: $ARGUMENTS

The argument format is: TICKER CURRENT_STRIKE CURRENT_EXPIRY STRATEGY
(e.g., "AAPL 170P 2026-05-16 CSP" or "TSLA 280C 2026-05-09 CC")

Use web search to get current stock price and options chain data.

## Current Position Status
- Current stock price vs. your strike
- How far ITM/OTM is the position?
- Days to expiry remaining
- Current P&L estimate (premium collected vs. current cost to close)

## Should You Roll?

First, check the prerequisites:
1. **Do you still have conviction in the underlying?** Rolling only makes sense if you're still bullish (for CSP) or still want to hold (for CC). If not → close the position and take the loss.
2. **Can you roll for a net credit?** If you can't get a credit, rolling just digs a deeper hole.

## Rolling Options

Compare 2-3 rolling alternatives:

| Roll Type | New Strike | New Expiry | Cost to Close Current | New Premium | Net Credit/Debit | New Breakeven | New PoP |

Rolling types to consider:
- **Roll out**: same strike, later expiry (more time = more premium)
- **Roll out & down** (for puts): later expiry + lower strike — reduces assignment risk
- **Roll out & up** (for calls): later expiry + higher strike — gives more room

## Alternatives to Rolling
- Close the position entirely (realize the loss/gain)
- Let it expire / take assignment (if you're happy owning at this price)
- Do nothing and wait (if still OTM with time left)

## Recommendation
- Clear roll / don't roll decision with reasoning
- If roll: specify exact new strike, expiry, and expected net credit

Do NOT save output to a file — this is a live analysis tool for decision-making.
