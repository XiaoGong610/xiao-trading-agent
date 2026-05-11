---
description: Dashboard view of all active positions and trade history
---

Show portfolio dashboard.

**Step 1:** Run the dashboard script to generate the overview:
```bash
.venv/bin/python3 scripts/dashboard.py
```

This will:
- Print a full dashboard to the terminal (portfolio, watchlist by sector with live prices, earnings calendar, stale alerts, trade history)
- Save a markdown version to `DASHBOARD.md` in the project root (viewable in IDE)

**Step 2:** After the script runs, review the output and highlight:
- Any positions needing attention (DTE < 14, deep ITM, earnings approaching)
- Stocks near their entry targets (current price close to target = action time)
- Stale research that needs refreshing
- Upcoming earnings in the next 7 days

**Step 3:** Suggest next actions based on the dashboard:
- Which stocks to enter (at or below target)
- Which positions to review (`/trade-review TICKER`)
- Which research to refresh (`/research-stock TICKER` or `/plan-stock TICKER`)
