#!/usr/bin/env python3
"""
Auto-generate research/stocks/0-INDEX.md from frontmatter in stock files.

Reads all .md files in research/stocks/, parses YAML frontmatter,
groups by status, flags stale research, and writes a fresh index.

Usage:
    .venv/bin/python3 scripts/update-index.py
"""

import os
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

STOCKS_DIR = Path("research/stocks")
INDEX_FILE = STOCKS_DIR / "0-INDEX.md"
STALE_DAYS = 7  # Flag research older than this


def parse_frontmatter(filepath: Path) -> dict:
    """Parse YAML frontmatter from a markdown file."""
    content = filepath.read_text(encoding="utf-8")

    # Match YAML frontmatter between --- markers
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}

    frontmatter = {}
    for line in match.group(1).strip().split('\n'):
        if ':' in line:
            key, _, value = line.partition(':')
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            # Parse lists like [dca, csp]
            if value.startswith('[') and value.endswith(']'):
                value = [v.strip().strip('"').strip("'") for v in value[1:-1].split(',')]
            frontmatter[key] = value

    return frontmatter


def find_last_update(filepath: Path) -> str | None:
    """Find the most recent analysis date from section headers."""
    content = filepath.read_text(encoding="utf-8")

    # Match patterns like: # TICKER — Analysis Type | YYYY-MM-DD
    # or: # TICKER — Analysis Type | 2026-05-10
    dates = re.findall(r'\|\s*(\d{4}-\d{2}-\d{2})', content)
    if not dates:
        # Try matching date in header like: Research | 2026-05-09
        dates = re.findall(r'(\d{4}-\d{2}-\d{2})', content[:2000])  # Check first 2000 chars

    if dates:
        # Return the most recent date
        return max(dates)
    return None


def days_since(date_str: str) -> int:
    """Calculate days between a date string and today."""
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        return (datetime.now() - date).days
    except (ValueError, TypeError):
        return 999


def generate_index():
    """Generate the 0-INDEX.md file."""
    if not STOCKS_DIR.exists():
        print(f"Error: {STOCKS_DIR} does not exist")
        sys.exit(1)

    # Collect all stock files
    stocks = []
    for filepath in sorted(STOCKS_DIR.glob("*.md")):
        if filepath.name == "0-INDEX.md":
            continue
        if filepath.name.startswith("."):
            continue

        fm = parse_frontmatter(filepath)
        if not fm.get("ticker"):
            continue

        last_update = find_last_update(filepath)
        age_days = days_since(last_update) if last_update else 999

        stocks.append({
            "file": filepath.name,
            "ticker": fm.get("ticker", filepath.stem),
            "status": fm.get("status", "unknown"),
            "sector": fm.get("sector", "Unknown"),
            "thesis": fm.get("thesis", ""),
            "entry_target": fm.get("entry_target", ""),
            "strategies": fm.get("strategies", []),
            "added_date": fm.get("added_date", ""),
            "last_update": last_update or "unknown",
            "age_days": age_days,
            "is_stale": age_days > STALE_DAYS,
        })

    # Group by status
    groups = {
        "watching": [],
        "researched": [],
        "in-portfolio": [],
        "removed": [],
        "unknown": [],
    }

    for stock in stocks:
        status = stock["status"]
        if status in groups:
            groups[status].append(stock)
        else:
            groups["unknown"].append(stock)

    # Sort each group by ticker
    for group in groups.values():
        group.sort(key=lambda s: s["ticker"])

    # Find stale stocks
    stale = [s for s in stocks if s["is_stale"] and s["status"] in ("watching", "researched")]

    # Build the index
    today = datetime.now().strftime("%Y-%m-%d")
    lines = []
    lines.append(f"# Stock Index")
    lines.append(f"")
    lines.append(f"*Auto-generated on {today} by `scripts/update-index.py`*")
    lines.append(f"")

    # Refresh alerts
    if stale:
        lines.append(f"## ⚠ Needs Refresh (>{STALE_DAYS} days old)")
        lines.append(f"")
        for s in sorted(stale, key=lambda x: x["age_days"], reverse=True):
            lines.append(f"- [{s['ticker']}]({s['file']}) — last updated **{s['last_update']}** ({s['age_days']} days ago) | {s['sector']}")
        lines.append(f"")
        lines.append(f"Run `/research-stock TICKER` or `/plan-stock TICKER` to refresh.")
        lines.append(f"")

    # Watching
    if groups["watching"]:
        lines.append(f"## Watching")
        lines.append(f"")
        lines.append(f"| Ticker | Sector | Thesis | Strategies | Last Updated |")
        lines.append(f"|--------|--------|--------|------------|-------------|")
        for s in groups["watching"]:
            strategies = ", ".join(s["strategies"]) if isinstance(s["strategies"], list) else s["strategies"]
            age_flag = " ⚠" if s["is_stale"] else ""
            lines.append(f"| [{s['ticker']}]({s['file']}) | {s['sector']} | {s['thesis']} | {strategies} | {s['last_update']}{age_flag} |")
        lines.append(f"")

    # Researched
    if groups["researched"]:
        lines.append(f"## Researched (no plan yet)")
        lines.append(f"")
        lines.append(f"| Ticker | Sector | Thesis | Last Updated |")
        lines.append(f"|--------|--------|--------|-------------|")
        for s in groups["researched"]:
            age_flag = " ⚠" if s["is_stale"] else ""
            lines.append(f"| [{s['ticker']}]({s['file']}) | {s['sector']} | {s['thesis']} | {s['last_update']}{age_flag} |")
        lines.append(f"")

    # In Portfolio
    if groups["in-portfolio"]:
        lines.append(f"## In Portfolio")
        lines.append(f"")
        lines.append(f"| Ticker | Sector | Strategies | Last Updated |")
        lines.append(f"|--------|--------|------------|-------------|")
        for s in groups["in-portfolio"]:
            strategies = ", ".join(s["strategies"]) if isinstance(s["strategies"], list) else s["strategies"]
            lines.append(f"| [{s['ticker']}]({s['file']}) | {s['sector']} | {strategies} | {s['last_update']} |")
        lines.append(f"")

    # Removed
    if groups["removed"]:
        lines.append(f"## Removed")
        lines.append(f"")
        for s in groups["removed"]:
            lines.append(f"- [{s['ticker']}]({s['file']}) — {s['thesis']}")
        lines.append(f"")

    # Stats
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"**Stats:** {len(stocks)} stocks total | {len(groups['watching'])} watching | {len(groups['in-portfolio'])} in portfolio | {len(stale)} need refresh")

    # Write
    INDEX_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Index updated: {len(stocks)} stocks, {len(stale)} stale")


if __name__ == "__main__":
    generate_index()
