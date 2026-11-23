---
name: d2c-daily-ads-report
description: >-
  Turn a Meta Ads Manager export into a daily report for a D2C brand that says
  which ads to SCALE, KEEP, WATCH or KILL against the brand's real break-even
  ROAS, plus a short summary the founder can read in a minute. Use when the user
  pastes or uploads a Meta ads CSV, says "daily report", "aaj ki report",
  "kaunse ads chal rahe hain", "which ads are burning money", or asks what to
  pause or scale today.
---

# d2c-daily-ads-report

Most daily reports list numbers. This one makes a call on every row, against
the one threshold that matters: the brand's break-even ROAS after COD, RTO and
GST. A 2.5 ROAS ad is a winner for one brand and a money pit for another.

## Step 1: get the break-even ROAS

If the user already knows it, use it. If not, run the d2c-true-roas skill first.
Do not use a generic "ROAS 3 is good" rule. If they refuse to give cost data,
ask for their best guess and mark every verdict as provisional.

## Step 2: get the export

Tell them exactly how, once:

1. Ads Manager → Ads tab → choose the date range (yesterday, or last 7 days for a
   steadier read).
2. Columns: Amount spent, Impressions, Frequency, Link clicks, Purchases,
   Purchases conversion value. Ad-level is best; ad set level works.
3. Reports → Export table data → CSV.

## Step 3: run the tool

```bash
python3 meta_report.py export.csv --be-roas 2.65
```

Useful flags: `--be-cpa` (rupees, if AOV varies a lot), `--min-purchases 3`,
`--kill-spend 2` (kill after 2× break-even CPA with no profit),
`--scale-buffer 1.3`, `--fatigue-freq 3.5`. Try it on `sample-meta-export.csv`.
Without Python, apply the same rules by hand:

| Verdict | Rule (defaults) |
|---|---|
| TOO EARLY | Spent less than 1× break-even CPA and under 3 purchases |
| KILL | No purchase after 2× break-even CPA, or ROAS under 70% of break-even after 2× CPA spend |
| WATCH | Below break-even but small spend, or 70–100% of break-even |
| KEEP | At or above break-even, but under 130% or under 3 purchases |
| SCALE | ROAS at least 130% of break-even with 3+ purchases |

These thresholds are starting points, not laws. Change them to match the
brand's appetite for risk, and say which ones you used.

## Step 4: write the report

Keep it short. The founder reads the top; the media buyer reads the table.

```
<Date> | Spend ₹X | ROAS Y vs break-even Z | <PROFITABLE / LOSING MONEY>

Do today
1. Pause: <names>. Saves about ₹X a day.
2. Scale: <name> by 20% (next increase after 48 to 72 hours if it holds).
3. Fix: <name> has frequency 4.1 and falling CTR. New creative, same angle.

Watch
- <names and the one thing to check tomorrow>

<the table from the tool>
```

Write in the user's language. If they write Hinglish, the summary is Hinglish,
the table stays as is.

## Judgment the script cannot make

- **Learning phase.** Meta needs roughly 50 optimisation events in a week to
  exit learning, and big edits restart it. Do not recommend killing an ad set
  that is three days old and still learning unless it is clearly bleeding.
- **One day is noise.** For KILL calls on decent spend, check the last 7 days
  too. One bad Sunday is not a trend.
- **Meta's purchases are not your orders.** If Shopify shows far fewer orders
  than Meta, the verdicts are too generous. Run d2c-attribution-gap.
- **Scaling.** Many buyers raise budgets about 20% at a time to avoid shocking
  delivery. It is a rule of thumb, not a Meta rule. Say so.
- **Never change anything yourself.** This skill recommends. The user or their
  agency makes the change in Ads Manager.
- Never ask for customer-level data. Campaign totals are enough.
