---
description: Check what top ThetaGang.com traders are doing on a specific ticker
---

Check what the top theta gang traders are doing on: $ARGUMENTS

Reference the leader list at `leaders.md` (in the project root) for the top 10 traders.

For the given ticker, check the following profiles and summarize any recent trades:

1. [jrue](https://thetagang.com/jrue) — #1, 5,882 trades
2. [dom747](https://thetagang.com/dom747) — #2, 3,993 trades
3. [major](https://thetagang.com/major) — #3, 3,535 trades
4. [bobthetrader](https://thetagang.com/bobthetrader) — #4, 2,576 trades
5. [Slomotion](https://thetagang.com/Slomotion) — #5, 3,001 trades
6. [gruffalo](https://thetagang.com/gruffalo) — #6, 2,347 trades
7. [epilektoi](https://thetagang.com/epilektoi) — #7, 1,992 trades
8. [Stizzle](https://thetagang.com/Stizzle) — #8, 2,073 trades
9. [simofin](https://thetagang.com/simofin) — #9, 1,568 trades
10. [Hirad](https://thetagang.com/Hirad) — #10, 1,723 trades

Try to fetch each profile page to find trades on the given ticker. If the pages don't render trade data (they use dynamic loading), then instead:

1. Direct the user to check these profiles manually on thetagang.com
2. Also check the ticker-specific community page: `thetagang.com/symbols/$ARGUMENTS`
3. Suggest filtering by: Winners, strategy type (CSP, CC), and recent trades

## What to Look For
- Are any top traders currently active on this ticker?
- What strategies are they using (CSP, CC, IC, etc.)?
- What strikes and expirations are they choosing?
- Win rate on this ticker across the community
- Any patterns: do they sell at similar delta/DTE to our rules?

## Output
Summarize findings and note any insights that should inform your own trade decision. Do NOT save to a file — this is a live lookup tool.
