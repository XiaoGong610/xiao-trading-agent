#!/usr/bin/env python3
"""
Trading dashboard — overview of watchlist, portfolio, earnings calendar, and action items.

Reads research/stocks/, portfolio/, trades/ and outputs a clean summary.

Usage:
    .venv/bin/python3 scripts/dashboard.py
    .venv/bin/python3 scripts/dashboard.py --json    # JSON output
"""

import json
import os
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

try:
    import yfinance as yf
    HAS_YFINANCE = True
except ImportError:
    HAS_YFINANCE = False

STOCKS_DIR = Path("research/stocks")
PORTFOLIO_DIR = Path("portfolio")
TRADES_DIR = Path("trades")
STALE_DAYS = 7


def parse_frontmatter(filepath: Path) -> dict:
    """Parse YAML frontmatter from a markdown file."""
    content = filepath.read_text(encoding="utf-8")
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}

    frontmatter = {}
    for line in match.group(1).strip().split('\n'):
        if ':' in line:
            key, _, value = line.partition(':')
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if value.startswith('[') and value.endswith(']'):
                value = [v.strip().strip('"').strip("'") for v in value[1:-1].split(',')]
            frontmatter[key] = value

    return frontmatter


def find_last_update(filepath: Path) -> str | None:
    """Find the most recent analysis date."""
    content = filepath.read_text(encoding="utf-8")
    dates = re.findall(r'\|\s*(\d{4}-\d{2}-\d{2})', content)
    if not dates:
        dates = re.findall(r'(\d{4}-\d{2}-\d{2})', content[:2000])
    return max(dates) if dates else None


def find_earnings_date(filepath: Path) -> str | None:
    """Try to find earnings date mentioned in the file."""
    content = filepath.read_text(encoding="utf-8")
    # Look for patterns like: Earnings **May 27** or earnings: May 11 or Next earnings: Jun 3
    patterns = [
        r'[Ee]arnings\s*(?:\*\*)?(?:date)?:?\s*(?:\*\*)?\s*((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s+\d{1,2}(?:[-–]\d{1,2})?(?:,?\s*\d{4})?)',
        r'[Nn]ext\s+earnings[:\s]+(?:\*\*)?((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s+\d{1,2}(?:[-–]\d{1,2})?(?:,?\s*\d{4})?)',
    ]
    for pattern in patterns:
        match = re.search(pattern, content)
        if match:
            return match.group(1).strip('*')
    return None


def days_since(date_str: str) -> int:
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        return (datetime.now() - date).days
    except (ValueError, TypeError):
        return 999


def compute_rsi(closes, period=14):
    """Compute RSI from a series of closing prices."""
    if len(closes) < period + 1:
        return None
    deltas = [closes[i] - closes[i-1] for i in range(1, len(closes))]
    gains = [d if d > 0 else 0 for d in deltas]
    losses = [-d if d < 0 else 0 for d in deltas]

    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period

    for i in range(period, len(gains)):
        avg_gain = (avg_gain * (period - 1) + gains[i]) / period
        avg_loss = (avg_loss * (period - 1) + losses[i]) / period

    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return round(100 - (100 / (1 + rs)), 1)


def get_market_data(tickers: list[str]) -> tuple[dict, dict]:
    """Fetch current prices and RSI for a list of tickers."""
    prices = {}
    rsi_values = {}

    if not HAS_YFINANCE or not tickers:
        return prices, rsi_values

    try:
        # Filter out non-US tickers
        us_tickers = [t for t in tickers if not any(c in t for c in ['.', '/', 'IBDNF'])]
        if us_tickers:
            data = yf.download(us_tickers, period="1mo", progress=False)
            if len(us_tickers) == 1:
                try:
                    closes = data['Close'].dropna().tolist()
                    if closes:
                        prices[us_tickers[0]] = round(float(closes[-1]), 2)
                        rsi = compute_rsi(closes)
                        if rsi is not None:
                            rsi_values[us_tickers[0]] = rsi
                except (KeyError, IndexError):
                    pass
            else:
                for ticker in us_tickers:
                    try:
                        closes = data['Close'][ticker].dropna().tolist()
                        if closes:
                            prices[ticker] = round(float(closes[-1]), 2)
                            rsi = compute_rsi(closes)
                            if rsi is not None:
                                rsi_values[ticker] = rsi
                    except (KeyError, IndexError):
                        pass
    except Exception:
        pass

    return prices, rsi_values


def load_stocks() -> list[dict]:
    """Load all stock files with metadata."""
    stocks = []
    if not STOCKS_DIR.exists():
        return stocks

    for filepath in sorted(STOCKS_DIR.glob("*.md")):
        if filepath.name == "0-INDEX.md" or filepath.name.startswith("."):
            continue

        fm = parse_frontmatter(filepath)
        if not fm.get("ticker"):
            continue

        last_update = find_last_update(filepath)
        earnings = find_earnings_date(filepath)

        stocks.append({
            "ticker": fm.get("ticker", filepath.stem),
            "status": fm.get("status", "unknown"),
            "sector": fm.get("sector", "Unknown"),
            "thesis": fm.get("thesis", ""),
            "entry_target": fm.get("entry_target", ""),
            "strategies": fm.get("strategies", []),
            "last_update": last_update or "unknown",
            "age_days": days_since(last_update) if last_update else 999,
            "earnings_date": earnings,
        })

    return stocks


def load_portfolio() -> list[dict]:
    """Load active portfolio positions."""
    positions = []
    if not PORTFOLIO_DIR.exists():
        return positions

    for filepath in sorted(PORTFOLIO_DIR.glob("*.md")):
        if filepath.name.startswith("."):
            continue
        fm = parse_frontmatter(filepath)
        if fm:
            positions.append(fm)

    return positions


def load_trades() -> list[dict]:
    """Load closed trades."""
    trades = []
    if not TRADES_DIR.exists():
        return trades

    for filepath in sorted(TRADES_DIR.glob("*.md")):
        if filepath.name.startswith("."):
            continue
        fm = parse_frontmatter(filepath)
        if fm:
            trades.append(fm)

    return trades


def rsi_label(rsi_val):
    """Return a human-readable RSI label."""
    if rsi_val is None:
        return ""
    if rsi_val < 30:
        return f"{rsi_val} OVERSOLD"
    elif rsi_val > 70:
        return f"{rsi_val} OVERBOUGHT"
    return f"{rsi_val}"


def print_dashboard(stocks, portfolio, trades, prices, rsi_values=None):
    """Print the dashboard to stdout."""
    today = datetime.now().strftime("%Y-%m-%d")

    print("=" * 70)
    print(f"  TRADING DASHBOARD — {today}")
    print("=" * 70)

    # Portfolio
    print(f"\n📊 PORTFOLIO ({len(portfolio)} positions)")
    print("-" * 50)
    if portfolio:
        for p in portfolio:
            ticker = p.get('ticker', '?')
            strategy = p.get('strategy', '?')
            entry = p.get('entry_date', '?')
            print(f"  {ticker:8s} | {strategy:15s} | entered {entry}")
    else:
        print("  (no active positions)")

    # Watchlist by sector
    watching = [s for s in stocks if s["status"] == "watching"]
    print(f"\n👀 WATCHING ({len(watching)} stocks)")
    print("-" * 50)

    sectors = {}
    for s in watching:
        sector = s["sector"]
        if sector not in sectors:
            sectors[sector] = []
        sectors[sector].append(s)

    if rsi_values is None:
        rsi_values = {}

    for sector in sorted(sectors.keys()):
        print(f"\n  [{sector}]")
        for s in sectors[sector]:
            ticker = s["ticker"]
            price_str = f"${prices[ticker]:.2f}" if ticker in prices else "     "
            target = s["entry_target"]
            target_str = f"target ${target}" if target else ""
            strategies = ", ".join(s["strategies"]) if isinstance(s["strategies"], list) else s["strategies"]
            rsi = rsi_values.get(ticker)
            rsi_str = f"RSI {rsi_label(rsi)}" if rsi else ""
            stale_flag = " ⚠ STALE" if s["age_days"] > STALE_DAYS else ""
            print(f"    {ticker:8s} {price_str:>10s} | {rsi_str:20s} | {strategies:20s} | {target_str:15s} | updated {s['last_update']}{stale_flag}")

    # Earnings calendar
    print(f"\n📅 UPCOMING EARNINGS")
    print("-" * 50)
    earnings_stocks = [(s["ticker"], s["earnings_date"]) for s in watching if s.get("earnings_date")]
    if earnings_stocks:
        for ticker, date in sorted(earnings_stocks, key=lambda x: x[1]):
            print(f"  {ticker:8s} | {date}")
    else:
        print("  (no earnings dates found — run /plan-stock to populate)")

    # Stale research
    stale = [s for s in watching if s["age_days"] > STALE_DAYS]
    if stale:
        print(f"\n⚠ NEEDS REFRESH (>{STALE_DAYS} days old)")
        print("-" * 50)
        for s in sorted(stale, key=lambda x: x["age_days"], reverse=True):
            print(f"  {s['ticker']:8s} | last updated {s['last_update']} ({s['age_days']} days ago)")

    # Trade history
    print(f"\n📈 TRADE HISTORY ({len(trades)} closed)")
    print("-" * 50)
    if trades:
        total_pnl = 0
        wins = 0
        for t in trades:
            pnl = float(t.get('realized_pnl', 0))
            total_pnl += pnl
            if pnl > 0:
                wins += 1
            print(f"  {t.get('ticker', '?'):8s} | {t.get('strategy', '?'):10s} | P&L: ${pnl:>8.2f} | {t.get('outcome', '?')}")
        win_rate = (wins / len(trades) * 100) if trades else 0
        print(f"\n  Total P&L: ${total_pnl:.2f} | Win rate: {win_rate:.0f}%")
    else:
        print("  (no closed trades yet)")

    # Summary stats
    print(f"\n{'=' * 70}")
    print(f"  {len(watching)} watching | {len(portfolio)} in portfolio | {len(trades)} closed | {len(stale)} stale")
    print(f"{'=' * 70}")


DASHBOARD_FILE = Path("research/stocks/1-DASHBOARD.md")


def generate_markdown(stocks, portfolio, trades, prices, rsi_values=None) -> str:
    """Generate a markdown version of the dashboard for file output."""
    today = datetime.now().strftime("%Y-%m-%d")
    lines = []

    lines.append(f"# Trading Dashboard")
    lines.append(f"")
    lines.append(f"*Auto-generated on {today} by `scripts/dashboard.py`*")
    lines.append(f"")

    # Portfolio
    lines.append(f"## Portfolio ({len(portfolio)} positions)")
    lines.append(f"")
    if portfolio:
        lines.append(f"| Ticker | Strategy | Entry Date |")
        lines.append(f"|--------|----------|------------|")
        for p in portfolio:
            lines.append(f"| {p.get('ticker', '?')} | {p.get('strategy', '?')} | {p.get('entry_date', '?')} |")
    else:
        lines.append(f"(no active positions)")
    lines.append(f"")

    # Watchlist by sector
    watching = [s for s in stocks if s["status"] == "watching"]
    lines.append(f"## Watching ({len(watching)} stocks)")
    lines.append(f"")

    sectors = {}
    for s in watching:
        sector = s["sector"]
        if sector not in sectors:
            sectors[sector] = []
        sectors[sector].append(s)

    if rsi_values is None:
        rsi_values = {}

    for sector in sorted(sectors.keys()):
        lines.append(f"### {sector}")
        lines.append(f"")
        lines.append(f"| Ticker | Price | RSI | Target | Gap | Strategies | Last Updated |")
        lines.append(f"|--------|-------|-----|--------|-----|------------|-------------|")
        for s in sectors[sector]:
            ticker = s["ticker"]
            price = prices.get(ticker)
            price_str = f"${price:.2f}" if price else "—"
            rsi = rsi_values.get(ticker)
            rsi_str = f"**{rsi}** 🔻" if rsi and rsi < 30 else f"**{rsi}** 🔺" if rsi and rsi > 70 else f"{rsi}" if rsi else "—"
            target = s["entry_target"]
            target_str = f"${target}" if target else "—"
            if price and target:
                try:
                    target_val = float(target)
                    gap_pct = ((price - target_val) / price) * 100
                    gap_str = f"{gap_pct:+.1f}%" if gap_pct != 0 else "at target"
                except (ValueError, ZeroDivisionError):
                    gap_str = "—"
            else:
                gap_str = "—"
            strategies = ", ".join(s["strategies"]) if isinstance(s["strategies"], list) else s["strategies"]
            stale_flag = " ⚠" if s["age_days"] > STALE_DAYS else ""
            lines.append(f"| [{ticker}]({s['ticker']}.md) | {price_str} | {rsi_str} | {target_str} | {gap_str} | {strategies} | {s['last_update']}{stale_flag} |")
        lines.append(f"")

    # Earnings calendar — sorted by date, future only
    lines.append(f"## Upcoming Earnings")
    lines.append(f"")
    earnings_stocks = [(s["ticker"], s["earnings_date"]) for s in watching if s.get("earnings_date")]
    if earnings_stocks:
        # Sort roughly by month
        month_order = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
                       "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}

        def sort_key(item):
            date_str = item[1]
            for month, num in month_order.items():
                if month in date_str:
                    return num
            return 99

        sorted_earnings = sorted(earnings_stocks, key=sort_key)

        lines.append(f"| Ticker | Earnings Date |")
        lines.append(f"|--------|--------------|")
        for ticker, date in sorted_earnings:
            lines.append(f"| {ticker} | {date} |")
    else:
        lines.append(f"(no earnings dates found)")
    lines.append(f"")

    # Stale research
    stale = [s for s in watching if s["age_days"] > STALE_DAYS]
    if stale:
        lines.append(f"## Needs Refresh (>{STALE_DAYS} days old)")
        lines.append(f"")
        for s in sorted(stale, key=lambda x: x["age_days"], reverse=True):
            lines.append(f"- **{s['ticker']}** — last updated {s['last_update']} ({s['age_days']} days ago)")
        lines.append(f"")

    # Trade history
    lines.append(f"## Trade History ({len(trades)} closed)")
    lines.append(f"")
    if trades:
        lines.append(f"| Ticker | Strategy | P&L | Outcome |")
        lines.append(f"|--------|----------|-----|---------|")
        total_pnl = 0
        wins = 0
        for t in trades:
            pnl = float(t.get('realized_pnl', 0))
            total_pnl += pnl
            if pnl > 0:
                wins += 1
            lines.append(f"| {t.get('ticker', '?')} | {t.get('strategy', '?')} | ${pnl:.2f} | {t.get('outcome', '?')} |")
        win_rate = (wins / len(trades) * 100) if trades else 0
        lines.append(f"")
        lines.append(f"**Total P&L:** ${total_pnl:.2f} | **Win rate:** {win_rate:.0f}%")
    else:
        lines.append(f"(no closed trades yet)")
    lines.append(f"")

    # Summary
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"**{len(watching)}** watching | **{len(portfolio)}** in portfolio | **{len(trades)}** closed | **{len(stale)}** stale")

    return "\n".join(lines) + "\n"


def main():
    json_mode = "--json" in sys.argv

    stocks = load_stocks()
    portfolio = load_portfolio()
    trades = load_trades()

    # Get current prices and RSI for watching stocks
    watching_tickers = [s["ticker"] for s in stocks if s["status"] == "watching"]
    if json_mode:
        prices, rsi_values = {}, {}
    else:
        prices, rsi_values = get_market_data(watching_tickers)

    if json_mode:
        output = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "stocks": stocks,
            "portfolio": portfolio,
            "trades": trades,
        }
        print(json.dumps(output, indent=2))
    else:
        # Print to terminal
        print_dashboard(stocks, portfolio, trades, prices, rsi_values)

        # Save to DASHBOARD.md
        md = generate_markdown(stocks, portfolio, trades, prices, rsi_values)
        DASHBOARD_FILE.write_text(md, encoding="utf-8")
        print(f"\nSaved to {DASHBOARD_FILE}")


if __name__ == "__main__":
    main()
