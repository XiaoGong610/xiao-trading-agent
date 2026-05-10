# xiao-trading-agent

A personal trading research and analysis workspace powered by [Claude Code](https://claude.ai/code).

## What This Is

A set of Claude Code custom skills for stock research and trading (including stocks and options). The skills use web search to gather live market data and produce structured, opinionated analysis. The repo is organized around a trading workflow lifecycle: scan, watch, enter, manage, exit, repeat.

## Skills

### Research & Discovery
| Command | Description |
|---------|-------------|
| `/sector-scan software` | Research a sector, rank 5-10 stocks for theta gang suitability |
| `/research AAPL` | Strategy-agnostic stock fundamentals (growth, earnings, sentiment, bull/bear case) |
| `/earnings AAPL` | Latest earnings call summary and key takeaways |
| `/scanner AAPL, TSLA, NVDA` | Rank a watchlist of stocks for best theta gang setup |

### Watchlist & Pre-Trade
| Command | Description |
|---------|-------------|
| `/watch AAPL` | Add a stock to the watchlist with entry criteria |
| `/plan AAPL` | Full pre-trade pipeline — conviction, options environment, strategy, strikes, checklist |
| `/theta-gang AAPL` | Pure options environment analysis (IV rank, Greeks, premiums, go/no-go) |
| `/strike-picker AAPL CSP` | Compare multiple strike/expiry combos side by side |
| `/check-leaders AAPL` | Check what top thetagang.com traders are doing on a ticker |
| `/chart AAPL 6mo csp=185 cc=200` | Interactive price chart with theta gang overlays |

### Portfolio Management
| Command | Description |
|---------|-------------|
| `/open AAPL CSP 185P 2026-06-18 3.20` | Log a new position to the portfolio |
| `/portfolio` | Dashboard — all active positions, alerts, trade history, cumulative stats |
| `/review-position AAPL` | Review an active position — hold, add, sell, or roll? |
| `/roll AAPL 170P 2026-05-16 CSP` | Analyze whether to roll an existing position |
| `/close AAPL expired-worthless` | Close a position, calculate P&L, run trade review |

## Folder Structure

```
research/
  sectors/           # Sector-level scans (local only, gitignored)
  stocks/            # Per-stock research (local only, gitignored)
watchlist/           # Candidates being monitored (local only, gitignored)
portfolio/           # Active positions (local only, gitignored)
trades/              # Closed trade log (local only, gitignored)
charts/              # Generated HTML charts (local only, gitignored)
.claude/commands/    # Claude Code custom skills (committed)
leaders.md           # ThetaGang.com top traders reference
```

## Setup

1. Clone this repo
2. Use with [Claude Code](https://claude.ai/code) — the skills are automatically available as slash commands
3. Optional: set up the Python environment for charts — `python3 -m venv .venv && pip install yfinance plotly matplotlib pandas`

Analysis files are gitignored since they contain personal trading data.
