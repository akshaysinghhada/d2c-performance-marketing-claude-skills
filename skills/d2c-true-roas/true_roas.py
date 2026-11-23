#!/usr/bin/env python3
"""True ROAS calculator for Indian D2C brands.

Meta shows you revenue on every purchase it counts. Your bank account sees
something else: COD orders that come back (RTO), customer returns, GST,
courier and COD fees, payment gateway fees and product cost. This script turns
your real numbers into the one figure that matters before you touch a budget:
the break-even ROAS, as Meta reports ROAS.

No internet calls. No dependencies. Python 3.8+.

Example:
  python3 true_roas.py --aov 999 --product-cost 250 --shipping 60 \
      --cod-share 60 --rto-cod 25 --rto-prepaid 5 --cod-fee 35 \
      --gateway 2 --returns 5 --return-shipping 70 --gst 3 --ad-gst 18

All percentages are written as plain numbers: 25 means 25%.
"""
import argparse
import json
import math
import sys


def inr(x):
    """Format a number the Indian way: 1,23,456."""
    neg = x < 0
    x = abs(round(x))
    s = str(int(x))
    if len(s) > 3:
        head, tail = s[:-3], s[-3:]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:])
            head = head[:-2]
        if head:
            parts.insert(0, head)
        s = ",".join(parts) + "," + tail
    return ("-₹" if neg else "₹") + s


def compute(a):
    p = lambda v: v / 100.0
    aov, cost = a.aov, a.product_cost
    cod = p(a.cod_share)
    pre = 1 - cod
    rto_cod, rto_pre = p(a.rto_cod), p(a.rto_prepaid)
    cod_delivered = cod * (1 - rto_cod)
    delivered = cod_delivered + pre * (1 - rto_pre)
    rto = 1 - delivered
    returned = delivered * p(a.returns)
    kept = delivered - returned

    gross_kept = aov * kept
    net_revenue = gross_kept / (1 + p(a.gst))
    gst_paid = gross_kept - net_revenue
    rto_ship = a.rto_shipping if a.rto_shipping is not None else a.shipping

    costs = {
        "product cost (kept orders)": cost * kept,
        "product lost (damaged units)": cost * p(a.damage) * (rto + returned),
        "forward shipping": a.shipping,
        "packaging": a.packaging,
        "RTO shipping": rto_ship * rto,
        "return pickup": a.return_shipping * returned,
        "COD fee": max(a.cod_fee, p(a.cod_fee_pct) * aov) * cod_delivered,
        "gateway fee (prepaid)": p(a.gateway) * aov * pre,
    }
    total_cost = sum(costs.values())
    contribution = net_revenue - total_cost
    ad_mult = 1 + p(a.ad_gst)
    be_cpa = contribution / ad_mult
    be_roas = aov / be_cpa if be_cpa > 0 else math.inf

    def profit_at(roas):
        return contribution - (aov / roas) * ad_mult

    table = [(r, profit_at(r)) for r in (1.5, 2, 2.5, 3, 3.5, 4, 5, 6)]

    goal_roas = None
    if a.margin_goal is not None:
        room = contribution - p(a.margin_goal) * net_revenue
        goal_roas = aov * ad_mult / room if room > 0 else math.inf

    return {
        "per_order_placed": {
            "aov_meta_sees": aov,
            "delivered_share": delivered,
            "rto_share": rto,
            "returned_share": returned,
            "kept_share": kept,
            "gst_paid": gst_paid,
            "net_revenue": net_revenue,
            "costs": costs,
            "contribution_before_ads": contribution,
        },
        "break_even_cpa": be_cpa,
        "break_even_roas": be_roas,
        "goal_roas": goal_roas,
        "profit_table": table,
    }


def report(a, r):
    o = r["per_order_placed"]
    out = []
    out.append("TRUE ROAS - per order Meta counts as a purchase")
    out.append("=" * 52)
    out.append(f"{'Meta counts revenue of':<32}{inr(o['aov_meta_sees']):>10}")
    out.append(f"{'Orders delivered':<32}{o['delivered_share']*100:>9.1f}%")
    out.append(f"{'Orders lost to RTO':<32}{o['rto_share']*100:>9.1f}%")
    out.append(f"{'Returned after delivery':<32}{o['returned_share']*100:>9.1f}%")
    out.append(f"{'GST you pay out':<32}{inr(o['gst_paid']):>10}")
    out.append(f"{'Revenue you actually keep':<32}{inr(o['net_revenue']):>10}")
    out.append("")
    out.append("Costs per order placed")
    for k, v in o["costs"].items():
        if v:
            out.append(f"  {k:<30}{inr(v):>10}")
    out.append(f"{'Left before ads':<32}{inr(o['contribution_before_ads']):>10}")
    out.append("")
    if r["break_even_cpa"] <= 0:
        out.append("VERDICT: you lose money on every order BEFORE ads.")
        out.append("Fix price, product cost, shipping or RTO first. No ROAS can save this.")
        return "\n".join(out)
    tag = " (incl. GST on ad spend)" if a.ad_gst else ""
    out.append(f"BREAK-EVEN CPA{tag}:  {inr(r['break_even_cpa'])}")
    out.append(f"BREAK-EVEN ROAS (as Meta reports it):  {r['break_even_roas']:.2f}")
    if r["goal_roas"] is not None:
        g = r["goal_roas"]
        g_txt = "not reachable" if math.isinf(g) else f"{g:.2f}"
        out.append(f"ROAS needed for {a.margin_goal:g}% profit margin:  {g_txt}")
    out.append("")
    out.append("Profit per order at the ROAS Meta shows")
    for roas, prof in r["profit_table"]:
        mark = "  <- loss" if prof < 0 else ""
        out.append(f"  ROAS {roas:<4g} -> {inr(prof):>9}{mark}")
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Break-even ROAS for Indian D2C after COD, RTO, returns, GST and fees. Percentages as plain numbers (25 = 25%).")
    ap.add_argument("--aov", type=float, required=True, help="average order value Meta records, incl. GST (Rs)")
    ap.add_argument("--product-cost", type=float, required=True, help="landed product cost per order (Rs)")
    ap.add_argument("--shipping", type=float, default=0, help="forward shipping per shipped order (Rs)")
    ap.add_argument("--packaging", type=float, default=0, help="packaging per order (Rs)")
    ap.add_argument("--cod-share", type=float, default=0, help="%% of orders that are COD")
    ap.add_argument("--rto-cod", type=float, default=0, help="%% of COD orders that come back undelivered")
    ap.add_argument("--rto-prepaid", type=float, default=0, help="%% of prepaid orders that come back undelivered")
    ap.add_argument("--rto-shipping", type=float, default=None, help="RTO charge per returned order (Rs, default = --shipping)")
    ap.add_argument("--cod-fee", type=float, default=0, help="flat COD fee per delivered COD order (Rs)")
    ap.add_argument("--cod-fee-pct", type=float, default=0, help="COD fee as %% of order value (the higher of flat and %% is used)")
    ap.add_argument("--gateway", type=float, default=0, help="payment gateway fee on prepaid orders, %%")
    ap.add_argument("--returns", type=float, default=0, help="%% of delivered orders refunded after delivery")
    ap.add_argument("--return-shipping", type=float, default=0, help="reverse pickup cost per return (Rs)")
    ap.add_argument("--damage", type=float, default=0, help="%% of RTO/returned units you cannot resell")
    ap.add_argument("--gst", type=float, default=0, help="GST %% included in your selling price")
    ap.add_argument("--ad-gst", type=float, default=0, help="GST %% on ad spend you cannot claim back (18 if no input credit)")
    ap.add_argument("--margin-goal", type=float, default=None, help="profit goal as %% of kept revenue, e.g. 15")
    ap.add_argument("--json", action="store_true", help="print raw numbers as JSON")
    a = ap.parse_args(argv)

    for name in ("cod_share", "rto_cod", "rto_prepaid", "returns", "damage"):
        v = getattr(a, name)
        if not 0 <= v <= 100:
            ap.error(f"--{name.replace('_', '-')} must be between 0 and 100")
    if a.aov <= 0:
        ap.error("--aov must be more than 0")

    r = compute(a)
    if a.json:
        clean = json.loads(json.dumps(r, default=str).replace("Infinity", "null"))
        print(json.dumps(clean, indent=2))
    else:
        print(report(a, r))


if __name__ == "__main__":
    sys.exit(main())
