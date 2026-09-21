# Ingestion Progress

Tracks how much of `raw/parsed/timeline.jsonl` (the merged Twitter + Mastodon
chronological archive) has been processed into the two wikis. This is the
resume point — always check here before starting an ingest session.

Regenerate the timeline with `python3 tools/build_timeline.py` if the raw
archives change; it will not affect this table.

Default batch = 1 calendar year. Dense years (2000+ posts) may be split into
quarters at ingest time — split rows here if you do.

| Range | Posts | Status | Wikis touched | Batch pages |
|---|---|---|---|---|
| 2010 | 224 | done (2026-09-21) | testing | [[testing/batches/2010]] |
| 2011 | 602 | done (2026-09-21) | testing, personal | [[testing/batches/2011]], [[personal/batches/2011]] |
| 2012 | 639 | done (2026-09-21) | testing, personal | [[testing/batches/2012]], [[personal/batches/2012]] |
| 2013 | 945 | done (2026-09-21) | testing, personal | [[testing/batches/2013]], [[personal/batches/2013]] |
| 2014 | 1540 | done (2026-09-21) | testing, personal | [[testing/batches/2014]], [[personal/batches/2014]] |
| 2015-Q1 | 491 | done (2026-09-21) | testing, personal | [[testing/batches/2015-q1]], [[personal/batches/2015-q1]] |
| 2015-Q2 | 646 | done (2026-09-21) | testing, personal | [[testing/batches/2015-q2]], [[personal/batches/2015-q2]] |
| 2015-Q3 | 979 | done (2026-09-21) | testing, personal | [[testing/batches/2015-q3]], [[personal/batches/2015-q3]] |
| 2015-Q4 | 725 | not started | | |
| 2016 | 4169 | not started | | |
| 2017 | 2845 | not started | | |
| 2018 | 4403 | not started | | |
| 2019 | 4363 | not started | | |
| 2020 | 4487 | not started | | |
| 2021 | 3575 | not started | | |
| 2022 | 3211 | not started | | |
| 2023 | 1293 | not started | | |
| 2024 | 1240 | not started | | |
| 2025 | 1044 | not started | | |
| 2026 (partial, through Aug) | 690 | not started | | |

Total posts: 38,111 (33,551 tweets, 2010-05-13–2022-10-29; 4,935 toots, 2022-11-08–2026-08-28).
