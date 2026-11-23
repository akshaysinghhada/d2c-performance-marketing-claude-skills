---
name: d2c-roas-drop-doctor
description: >-
  Diagnose why ROAS dropped for a D2C brand's Meta ads by splitting ROAS into
  CPM, CTR, conversion rate and AOV, finding which one moved, and ranking the
  likely causes with a 48-hour action plan. Use when the user says "ROAS gir
  gaya", "ROAS dropped", "sales down", "ads stopped working", "CPM badh gaya",
  "kal tak sab theek tha", or panics after a bad few days.
---

# d2c-roas-drop-doctor

When ROAS falls, most teams start changing everything at once. That resets
learning, muddies the data and usually makes it worse. This skill finds what
actually moved before anyone touches a campaign.

## The one formula

```
ROAS = (CTR × CVR × AOV × 1000) ÷ CPM
```

- CTR = link clicks ÷ impressions
- CVR = purchases ÷ link clicks
- AOV = purchase value ÷ purchases
- CPM = cost per 1,000 impressions

ROAS can only fall if CPM went up, or CTR, CVR or AOV went down. Find which one,
and you know where to look. Do the maths in front of the user so they can see it.

## Step 1: get comparable data

Ask for two equal windows: the bad period (for example, the last 7 days) and a
normal period before it (the 7 or 14 days before). Account level first, then the
top 3 campaigns by spend. Same columns: Amount spent, Impressions, CPM, Link
clicks, CTR (link), Purchases, Purchases conversion value.

Also ask, in the same message:

1. What changed in the account? Budgets, new campaigns, paused ads, new
   creatives, audience or bid edits, and on which date.
2. What changed on the website? Price, discount, shipping fee, COD on or off,
   theme or app updates, checkout app, payment gateway.
3. What do Shopify orders say for the same two windows? Up, flat or down?
4. Stock: are the best sellers or popular sizes out of stock?

## Step 2: find the factor that moved

Make a small table: each factor, both windows, % change. Then follow the
biggest mover.

| Factor moved | Likely causes to check |
|---|---|
| **CPM up** | Festive and sale-season auctions (big sale events, Diwali, wedding season), a narrower audience, many ads competing, low quality ranking in Ads Manager's relevance diagnostics |
| **CTR down** | Creative fatigue (frequency climbing while CTR slides over several days), an offer that is no longer new, a placement mix shift to Audience Network or Reels without native creative |
| **CVR down** | Site or checkout problem first: slow pages, broken payment gateway, COD switched off, new shipping fee, price change, out-of-stock sizes. Then intent: post-festive slump, traffic from a broad or cold audience |
| **AOV down** | Discount depth changed, bundle or free-gift offer removed, cheaper product getting the spend |
| **Purchases fell but Shopify orders did not** | Not a sales problem. Tracking broke: pixel or Conversions API, deduplication, a new checkout app or domain. Check Events Manager before touching ads |

## Step 3: check for a learning reset

Big edits put ad sets back into learning: budget jumps, bid or targeting
changes, new creatives, changing the optimisation event, or pausing for a week
or more. Meta needs roughly 50 optimisation events in a week to exit learning.
If the drop started the day after a big edit, that is suspect number one.

## Step 4: give the verdict

```
What moved: CVR fell 38% (2.1% → 1.3%). CPM and CTR are flat.
Most likely: checkout problem. COD was switched off on <date>, the day the drop began.
Also possible: <second cause, with evidence>
Ruled out: creative fatigue (CTR steady), auction pressure (CPM flat)

Next 48 hours
1. <single most important fix>
2. <check that confirms or rules out cause two>
3. Leave budgets and audiences alone until 1 and 2 are done.
```

Rank causes by evidence, not by how common they are. If the data cannot
separate two causes, say so and name the one check that would.

## Rules

- Never recommend more than one major campaign change at a time. You cannot
  learn from five changes made on the same day.
- Do not blame "the algorithm" or "Meta is down" without evidence.
- If ROAS fell but the brand is still above break-even (see d2c-true-roas),
  say so. Calm is a valid recommendation.
- Answer in the user's language. Hinglish if they write Hinglish.
- Never ask for customer-level data.
