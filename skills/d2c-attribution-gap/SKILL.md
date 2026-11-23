---
name: d2c-attribution-gap
description: >-
  Explain and reconcile the gap between Meta Ads purchases and real Shopify or
  WooCommerce orders for a D2C brand, then give the user one number to trust.
  Use when the user says "Meta says 50 sales, Shopify shows 30", "numbers match
  nahi ho rahe", "Meta over-reporting", "which ROAS is real", "attribution", or
  when a report's verdicts look too good to be true.
---

# d2c-attribution-gap

Meta and your store count different things, on different dates, with different
rules. A gap is normal. A gap you cannot explain is a problem, because every
ROAS decision sits on top of it.

## Step 1: line up the same period

Ask for:

- **Meta:** purchases and purchase value for a fixed date range, and the
  attribution setting (Ads Manager → Columns → Attribution setting). Most
  accounts use 7-day click and 1-day view.
- **Store:** orders and revenue for the same range, split by status (paid,
  pending COD, cancelled, RTO, returned) and, if they use UTMs, by source.
- **Time zones:** the ad account's time zone and the store's time zone.

## Step 2: walk the usual causes in order

| # | Cause | How to check | What to do |
|---|---|---|---|
| 1 | Different time zones | Ad account settings vs store settings | Compare whole weeks, or fix one to match |
| 2 | Different date logic | Ads Manager reports by the date of the click or view by default. The store reports by order date | Compare 7- or 14-day windows, not single days |
| 3 | View-through purchases | Compare the "7-day click" column alone with the full setting | Judge creatives on click-only when the gap is large |
| 4 | Cancelled, RTO and returned orders | Store order status | Meta still counts them. Use d2c-true-roas, which prices this in |
| 5 | Double counting | Events Manager: is Purchase firing from both browser and Conversions API without matching event IDs? Does it fire on thank-you page reloads? | Fix deduplication (same event name and event ID) |
| 6 | Third-party checkout | Is a checkout app (COD or one-click checkout) firing its own Purchase event as well as the store's? | Keep one source of Purchase |
| 7 | Other channels claim the same order | Google, email, WhatsApp and influencer UTMs on the same orders | Accept overlap; judge the business on blended numbers |
| 8 | Missing purchases | Store orders far ABOVE Meta: pixel broken, consent blocking, domain change | Fix tracking before optimising anything |

## Step 3: give them one number to trust

Platform ROAS is for comparing ads with each other. For the business, use
**MER** (marketing efficiency ratio):

```
MER = total store revenue (delivered orders) ÷ total ad spend (all platforms)
```

Show a small table: Meta-reported revenue, store revenue, delivered revenue,
and the ratio between Meta and delivered. If Meta reports ₹1.5 lakh and only
₹1 lakh is delivered, the ratio is 1.5. Divide Meta ROAS by that ratio for a
realistic read, and say clearly that this is an estimate.

## Step 4: write it up

```
Gap: Meta 52 purchases, store 41 orders, 33 delivered (same 14 days, IST)
Explained: ~6 from view-through, ~5 cancelled or RTO, 0 from time zone
Unexplained: ~8 → check Purchase deduplication in Events Manager
Trust: MER 2.4 on delivered revenue. Meta ROAS ÷ 1.6 for a realistic view.
```

## Rules

- Never call Meta "fake" or "lying". Attribution is a model; explain the model.
- If the gap cannot be explained with the data given, say what data would
  close it. Do not invent a split.
- Only totals and statuses are needed. Never ask for customer names, phone
  numbers or addresses.
- Answer in the user's language. Hinglish if they write Hinglish.
