---
name: d2c-true-roas
description: >-
  Work out the real profit per order and the break-even ROAS for an Indian D2C
  brand after COD, RTO, returns, GST, shipping, COD fees and gateway fees. Use
  when the user asks "what ROAS do I need", "am I making money at this ROAS",
  "break-even ROAS", "true ROAS", "real profit", "Meta says ROAS 3 but no profit",
  "kitne ROAS pe profit hoga", or before any budget or scaling decision.
---

# d2c-true-roas

Meta counts a purchase the moment an order is placed. A COD order that comes
back undelivered, a return, GST and the courier bill all happen later, and Meta
never sees them. So a "good" ROAS for one brand is a loss for another. This
skill finds the ROAS that actually breaks even for this brand.

## The tool

```bash
python3 true_roas.py --aov 999 --product-cost 250 --shipping 60 --packaging 20 \
  --cod-share 60 --rto-cod 25 --rto-prepaid 5 --cod-fee 35 --cod-fee-pct 2 \
  --gateway 2 --returns 5 --return-shipping 70 --damage 10 --gst 3 --ad-gst 18 \
  --margin-goal 15
```

All percentages are plain numbers (25 means 25%). Add `--json` for raw numbers.
If you cannot run Python (for example in a chat without code execution), do the
same maths by hand using the formulas at the bottom and show your working.

## Step 1: collect the inputs

Ask for these in one message, not one by one. Use the user's own numbers from
the last 30 to 60 days. Never invent a number. If they do not know one, use the
fallback in brackets and label it clearly as an assumption in the output.

| Input | Flag | Where they find it | Fallback |
|---|---|---|---|
| Average order value incl. GST | `--aov` | Shopify or Meta: value ÷ purchases | none, must ask |
| Product cost per order | `--product-cost` | Landed cost incl. inward freight | none, must ask |
| Forward shipping per order | `--shipping` | Shiprocket or courier invoice | ask |
| Packaging per order | `--packaging` | Box, pouch, tape, inserts | 0 |
| COD share of orders | `--cod-share` | Shopify payment method report | ask |
| RTO % on COD orders | `--rto-cod` | Courier panel, last 60 days | ask |
| RTO % on prepaid orders | `--rto-prepaid` | Courier panel | 0 |
| RTO charge per order | `--rto-shipping` | Courier rate card | same as shipping |
| COD fee | `--cod-fee`, `--cod-fee-pct` | Courier rate card ("₹X or Y%, whichever is higher") | ask |
| Gateway fee on prepaid | `--gateway` | Razorpay, Cashfree etc. | 2 |
| Returns after delivery | `--returns` | Returns or exchange report | 0 |
| Reverse pickup cost | `--return-shipping` | Courier rate card | 0 |
| Unsellable returned units | `--damage` | Warehouse | 0 |
| GST in selling price | `--gst` | Their CA or invoice | ask |
| GST on ad spend not claimed | `--ad-gst` | Meta invoices carry 18% GST. If they claim input tax credit, use 0 | 18 |
| Profit goal | `--margin-goal` | Their target margin on kept revenue | skip |

GST rates depend on the product category and change from time to time. Do not
guess a rate. Ask, or tell the user to confirm with their CA.

## Step 2: run it and read the result

The output has three numbers that matter:

1. **Left before ads**: contribution per order placed, after every cost except ads.
   If this is negative, stop. No ROAS can fix it. The problem is price, product
   cost, shipping or RTO, and the user needs to hear that plainly.
2. **Break-even CPA**: the most they can pay per Meta-counted purchase.
3. **Break-even ROAS**: the ROAS Meta must show for zero profit. This is the
   number every other skill in this pack uses.

## Step 3: tell them what it means

Write the answer for a founder, not an analyst:

- One line: "At your numbers, Meta needs to show ROAS X just to break even."
- The profit table at 2, 3 and 4 ROAS in rupees per order.
- The single biggest leak in their cost stack, and its rupee impact. RTO is
  usually the first suspect for COD-heavy brands. Show what happens if RTO drops
  by 5 points by re-running with the new value.
- If `--margin-goal` was given, the ROAS needed for that margin.

Round to whole rupees and one decimal of ROAS. If the user writes in Hinglish,
answer in Hinglish.

## Rules

- Break-even ROAS is per brand and per period. Re-run it whenever price, COD
  share or RTO changes, and before every festive season.
- Meta-reported ROAS already includes orders that will later be RTO'd or
  returned. That is why the break-even comes out higher than the simple
  "1 ÷ margin" number. Explain this if they push back.
- Do not mix this with attribution problems. If Meta's purchase count does not
  match Shopify, use the d2c-attribution-gap skill first, then come back.
- Never ask for customer names, phone numbers or order-level personal data. You
  only need totals.

## Formulas (per order placed)

```
delivered      = COD% × (1 − RTO_cod) + prepaid% × (1 − RTO_prepaid)
kept           = delivered × (1 − returns%)
net revenue    = AOV × kept ÷ (1 + GST%)
costs          = product × kept + product × damage% × (RTO + returned)
                 + shipping + packaging + RTO charge × RTO
                 + reverse pickup × returned
                 + max(COD flat, COD% × AOV) × COD delivered
                 + gateway% × AOV × prepaid%
contribution   = net revenue − costs
break-even CPA = contribution ÷ (1 + ad GST%)
break-even ROAS= AOV ÷ break-even CPA
```
