#!/usr/bin/env python3
"""Merge the Twitter and Mastodon archives into one chronological JSONL timeline.

Reads:
  raw/archives/twitter/data/tweets.js
  raw/archives/mastodon/<date>_outbox.json   (picks the newest by filename)

Writes:
  raw/parsed/timeline.jsonl   -- one JSON object per line, oldest first

This is a derived/regenerable artifact. It never touches the original
archive files. Re-run any time the raw archives are updated.
"""
import glob
import html
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TWEETS_JS = ROOT / "raw/archives/twitter/data/tweets.js"
MASTODON_GLOB = str(ROOT / "raw/archives/mastodon/*_outbox.json")
OUT_PATH = ROOT / "raw/parsed/timeline.jsonl"

TAG_RE = re.compile(r"<[^>]+>")


def strip_html(text: str) -> str:
    text = re.sub(r"<br\s*/?>", "\n", text)
    text = re.sub(r"</p><p>", "\n\n", text)
    text = TAG_RE.sub("", text)
    return html.unescape(text).strip()


def load_tweets():
    raw = TWEETS_JS.read_text(encoding="utf-8")
    raw = raw.split("=", 1)[1]
    data = json.loads(raw)
    out = []
    for wrapper in data:
        t = wrapper["tweet"]
        dt = datetime.strptime(t["created_at"], "%a %b %d %H:%M:%S %z %Y").astimezone(timezone.utc)
        out.append({
            "date": dt.isoformat(),
            "platform": "twitter",
            "id": t["id_str"],
            "url": f"https://twitter.com/maaretp/status/{t['id_str']}",
            "text": t["full_text"],
            "is_retweet": bool(t.get("retweeted") or t.get("full_text", "").startswith("RT @")),
            "is_reply": bool(t.get("in_reply_to_screen_name")),
            "in_reply_to": t.get("in_reply_to_screen_name"),
        })
    return out


def load_mastodon():
    files = sorted(glob.glob(MASTODON_GLOB))
    if not files:
        return []
    path = Path(files[-1])
    data = json.loads(path.read_text(encoding="utf-8"))
    out = []
    for item in data.get("orderedItems", []):
        if item.get("type") != "Create":
            continue
        obj = item.get("object", {})
        if obj.get("type") != "Note":
            continue
        dt = datetime.fromisoformat(obj["published"].replace("Z", "+00:00"))
        out.append({
            "date": dt.isoformat(),
            "platform": "mastodon",
            "id": obj["id"].rsplit("/", 1)[-1],
            "url": obj.get("url", obj["id"]),
            "text": strip_html(obj.get("content", "")),
            "is_retweet": False,
            "is_reply": bool(obj.get("inReplyTo")),
            "in_reply_to": obj.get("inReplyTo"),
        })
    return out


def main():
    posts = load_tweets() + load_mastodon()
    posts.sort(key=lambda p: p["date"])

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUT_PATH.open("w", encoding="utf-8") as f:
        for p in posts:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")

    by_year = {}
    for p in posts:
        y = p["date"][:4]
        by_year[y] = by_year.get(y, 0) + 1

    print(f"Wrote {len(posts)} posts to {OUT_PATH.relative_to(ROOT)}")
    print(f"Range: {posts[0]['date']} .. {posts[-1]['date']}")
    for y in sorted(by_year):
        print(f"  {y}: {by_year[y]}")


if __name__ == "__main__":
    main()
