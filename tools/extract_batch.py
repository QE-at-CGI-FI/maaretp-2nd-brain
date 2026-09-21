#!/usr/bin/env python3
"""Pull one date-range slice out of raw/parsed/timeline.jsonl for reading.

Usage:
  tools/extract_batch.py 2010          # whole year
  tools/extract_batch.py 2010 2011     # year range, inclusive
  tools/extract_batch.py 2016-Q1       # a quarter
  tools/extract_batch.py --skip-retweets 2016-Q1

Prints plain-text posts (date, platform, url, text) to stdout, oldest first.
Pipe to a file if you want to keep the slice around during a session.
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TIMELINE = ROOT / "raw/parsed/timeline.jsonl"


def parse_range(args):
    if len(args) == 1 and re.fullmatch(r"\d{4}-Q[1-4]", args[0]):
        year, q = args[0].split("-Q")
        q = int(q)
        start_month = (q - 1) * 3 + 1
        end_month = start_month + 2
        start = f"{year}-{start_month:02d}-01"
        end = f"{year}-{end_month:02d}-31"
        return start, end
    if len(args) == 1:
        return f"{args[0]}-01-01", f"{args[0]}-12-31"
    return f"{args[0]}-01-01", f"{args[1]}-12-31"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("range", nargs="+", help="e.g. 2010 | 2010 2011 | 2016-Q1")
    ap.add_argument("--skip-retweets", action="store_true")
    ap.add_argument("--skip-replies", action="store_true")
    args = ap.parse_args()

    start, end = parse_range(args.range)

    if not TIMELINE.exists():
        raise SystemExit("raw/parsed/timeline.jsonl not found — run tools/build_timeline.py first")

    count = 0
    with TIMELINE.open(encoding="utf-8") as f:
        for line in f:
            p = json.loads(line)
            d = p["date"][:10]
            if not (start <= d <= end):
                continue
            if args.skip_retweets and p["is_retweet"]:
                continue
            if args.skip_replies and p["is_reply"]:
                continue
            count += 1
            print(f"--- {p['date']} [{p['platform']}] {p['url']}")
            print(p["text"])
            print()

    print(f"# {count} posts in range {start}..{end}", flush=True)


if __name__ == "__main__":
    main()
