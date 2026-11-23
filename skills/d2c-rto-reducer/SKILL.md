---
name: d2c-rto-reducer
description: >-
  Build a plan to cut RTO (return to origin) and fake COD orders for an Indian
  D2C brand: where the RTO comes from, which levers to pull first (COD
  confirmation, partial COD, prepaid nudges, pincode rules, NDR follow-up,
  ad targeting) and what each is worth in rupees. Use when the user says "RTO
  bahut zyada hai", "COD orders wapas aa rahe hain", "fake orders", "reduce RTO",
  "COD band karein kya", or when RTO is the biggest leak in d2c-true-roas.
---

# d2c-rto-reducer

For COD-heavy Indian D2C brands, RTO is often the biggest profit leak, and it
hides: Meta counts the sale, the courier bills you twice, and the product comes
back weeks later. This skill finds where it comes from and fixes the cheapest
part first.

## Step 1: find where the RTO comes from

Ask for the last 60 to 90 days, as totals only:

1. RTO % for COD and for prepaid.
2. RTO % by state or by top pincodes, from the courier panel.
3. RTO % by courier partner.
4. RTO % by campaign or traffic source, if UTMs exist.
5. RTO reasons from the NDR (non-delivery report) data: customer refused, not
   reachable, wrong address, delivery attempt failed.
6. Average days from order to dispatch.

The fix depends on the reason. "Customer refused" is an intent problem.
"Not reachable" and "wrong address" are data and process problems.

## Step 2: pick levers in order of cost

| Lever | Fixes | Notes |
|---|---|---|
| Faster dispatch | Impulse buyers who change their mind | Same-day or next-day dispatch is often the cheapest win |
| COD order confirmation by WhatsApp or call before dispatch | Fake orders, wrong numbers | Ship only confirmed orders; cancel unconfirmed after a fixed window |
| Address check at checkout | Wrong or incomplete address | Pincode validation and a required landmark field |
| NDR follow-up within 24 hours | Missed deliveries | Re-attempt or reschedule before the courier marks RTO |
| Prepaid nudge | Shift buyers from COD to prepaid | Small prepaid discount or free shipping on prepaid. Price it with d2c-true-roas |
| Partial COD or COD fee | Low-intent COD orders | Small advance or fee on COD. Expect some conversion drop; measure net profit, not orders |
| Pincode and state rules | Areas with very high RTO | Prepaid-only for the worst pincodes, not a blanket COD ban |
| Courier allocation | One courier failing in one region | Route those pincodes to the better courier |
| Ad side | Audiences or creatives that bring low-intent COD buyers | Compare RTO by campaign; cut the worst, fix "too good to be true" offers |

## Step 3: put a rupee value on it

Re-run d2c-true-roas with the current RTO and with the target RTO, and show the
difference in break-even ROAS and profit per order. "Cutting COD RTO from 30% to
22% lowers your break-even ROAS from X to Y" moves a founder faster than any
percentage.

## Step 4: the plan

```
Biggest source: COD orders from <region>, reason "customer refused" (61% of RTO)
This week
1. Dispatch within 24 hours (now 3 days)
2. WhatsApp COD confirmation; cancel if unconfirmed in 24 hours
Next 2 weeks
3. Prepaid-only for the 40 worst pincodes; ₹50 prepaid discount, tested on 50% of traffic
Expected: COD RTO 30% → ~22% target; break-even ROAS 2.9 → ~2.5 (re-check after 30 days)
```

Label targets as targets. Do not promise an RTO number.

## Rules

- WhatsApp and SMS confirmations need the customer's consent and approved
  templates on the WhatsApp Business Platform. Under India's DPDP rules, use
  customer phone numbers only for the purpose they were given for.
- Do not recommend a blanket COD shutdown without the numbers. COD often brings
  orders that prepaid alone will not.
- Never ask for customer names, phone numbers or addresses. Aggregates only.
- Answer in the user's language. Hinglish if they write Hinglish.
