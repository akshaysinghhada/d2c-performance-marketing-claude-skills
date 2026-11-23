---
name: d2c-festive-planner
description: >-
  Plan an Indian D2C brand's festive or wedding-season Meta and Google campaign:
  the dates, the build-up, budget phasing by week, creative and offer calendar,
  stock and shipping cut-offs, and the post-festive plan. Use when the user says
  "Diwali campaign plan", "festive season", "shaadi season", "Valentine's plan",
  "Rakhi campaign", "sale plan", "kitna budget kab lagana hai", or is preparing
  for any peak period.
---

# d2c-festive-planner

Most festive campaigns fail in the 3 weeks before the festival, not on the day.
Creatives are not tested, the auction gets expensive, stock runs short, and the
last delivery date passes while ads are still running. This skill plans
backwards from the date that matters.

## Step 1: confirm the dates

Festival dates move every year with the Hindu calendar, and wedding muhurat
dates differ by region. **Never use a date from memory.** Confirm each date with
a web search or ask the user, and write the source next to it.

Peaks most Indian D2C brands plan around (check which apply):

| Window | Moments |
|---|---|
| Jan to Feb | Wedding season, Republic Day sales, Valentine's Day (14 Feb) |
| Mar to May | Holi, Eid, Akshaya Tritiya, wedding season, summer sales |
| Jun to Jul | End-of-season sales, monsoon |
| Aug | Raksha Bandhan, Independence Day sales |
| Sep to Oct | Big marketplace sale events, Navratri, Durga Puja |
| Oct to Nov | Karwa Chauth, Dhanteras, Diwali, Bhai Dooj |
| Nov to Feb | Wedding season (gaps between muhurat periods) |
| Dec to Jan | Christmas, New Year, end-of-season sales |

Ask: which 1 or 2 moments matter most for this brand's category, and what is
the target (revenue, orders, or new customers)?

## Step 2: work backwards

For each moment, set these dates:

1. **Last order date for on-time delivery** = festival date − courier transit
   time − dispatch time − 1 buffer day. Ask for their real transit times.
2. **Peak spend window** = the 7 to 10 days before the last order date.
3. **Creative testing window** = 2 to 3 weeks before the peak, on a small
   budget, so winners are ready before the auction gets expensive.
4. **Retargeting and last-chance window** = the final 3 to 4 days.
5. **Post-festive window** = 1 to 2 weeks after, for retention and reviews.

## Step 3: budget phasing

Start from the total festive budget and the break-even ROAS from d2c-true-roas.
A starting template to adjust, not a rule:

| Phase | Share of budget | Goal |
|---|---|---|
| Test (weeks −5 to −3) | 10–15% | Find 2 or 3 winning creatives and the offer |
| Build (weeks −3 to −2) | 20–25% | Grow warm audiences: video viewers, engagers, site visitors |
| Peak (last 7–10 days) | 45–55% | Spend behind proven winners |
| Last chance (final 3–4 days) | 10–15% | Retargeting, urgency, gifting angles |
| Post-festive | 5% | Repeat purchase, reviews, UGC collection |

Warn the user that CPMs usually rise during festive and big-sale weeks as more
advertisers compete. Plan for a higher CPM in the peak, and check the plan still
clears break-even ROAS at that CPM.

## Step 4: offer and creative calendar

For each phase, one line on: the offer, the angle, the formats and who makes
them. Angles that work in Indian festive seasons: gifting ("for her", "for
bhai"), the occasion look, price anchors ("under ₹999"), and delivery promises
("order by <date>, get it before Diwali"). Use d2c-hinglish-hooks for the copy.

## Step 5: operations checklist

- Stock for the top 10 SKUs, based on last year's festive sales or the current
  run rate × expected lift. Ask, do not assume.
- Courier capacity and pickup schedule confirmed for peak days.
- COD confirmation and RTO rules from d2c-rto-reducer switched on before the
  peak, when fake COD orders tend to rise.
- Site speed checked, payment gateway tested, offer codes tested.
- Daily report (d2c-daily-ads-report) running from the first test day.

## Output

A one-page plan: the dates table with sources, the week-by-week budget in
rupees, the offer and creative calendar, the operations checklist with owners,
and three risks with what to do if they happen. Round budgets to the nearest
₹1,000. Answer in the user's language; Hinglish if they write Hinglish.
