#!/usr/bin/env python3
"""Daily Meta Ads verdicts for D2C: SCALE, KEEP, WATCH, KILL, TOO EARLY.

Export a report from Meta Ads Manager as CSV (campaign, ad set or ad level,
with Amount spent, Purchases and Purchases conversion value columns) and run:

  python3 meta_report.py export.csv --be-roas 2.65

Get --be-roas from the d2c-true-roas skill. Without it, every "good ROAS"
call is a guess, because a 2.5 ROAS is profit for one brand and a loss for
another once COD, RTO and GST are counted.

No internet calls. No dependencies. Python 3.8+.
"""
import argparse
import csv
import io
import sys

ORDER = ["KILL", "SCALE", "WATCH", "KEEP", "TOO EARLY"]


def num(v):
    if v is None:
        return 0.0
    s = str(v).replace(",", "").replace("₹", "").replace("INR", "").replace("%", "").strip()
    if s in ("", "-", "—"):
        return 0.0
    try:
        return float(s)
    except ValueError:
        return 0.0


def find(headers, *candidates, contains=None, exclude=()):
    low = {h.lower().strip(): h for h in headers}
    for c in candidates:
        if c in low:
            return low[c]
    if contains:
        for k, h in low.items():
            if all(x in k for x in contains) and not any(e in k for e in exclude):
                return h
    return None


def load(path):
    raw = open(path, "rb").read().decode("utf-8-sig", errors="replace")
    rows = list(csv.DictReader(io.StringIO(raw)))
    if not rows:
        sys.exit("The CSV is empty.")
    h = list(rows[0].keys())
    cols = {
        "name": find(h, "ad name", "ad set name", "campaign name"),
        "spend": find(h, contains=("amount spent",)),
        "purchases": find(h, "purchases", "website purchases", "meta purchases"),
        "value": find(h, "purchases conversion value", "website purchases conversion value",
                      "purchase conversion value", contains=("conversion value",), exclude=("cost",)),
        "impressions": find(h, "impressions"),
        "clicks": find(h, "link clicks"),
        "frequency": find(h, "frequency"),
    }
    if not cols["purchases"]:
        res, ind = find(h, "results"), find(h, "result indicator")
        if res and ind and any("purchase" in (r.get(ind) or "").lower() for r in rows):
            cols["purchases"] = res
    missing = [k for k in ("name", "spend", "purchases", "value") if not cols[k]]
    if missing:
        sys.exit("Could not find these columns: " + ", ".join(missing)
                 + "\nColumns in your file: " + ", ".join(h)
                 + "\nAdd Amount spent, Purchases and Purchases conversion value in Ads Manager, then export again.")
    data = []
    for r in rows:
        name = (r.get(cols["name"]) or "").strip()
        if not name:
            continue  # Meta adds a blank-name total row
        g = lambda k: num(r.get(cols[k])) if cols[k] else 0.0
        data.append({"name": name, "spend": g("spend"), "purchases": g("purchases"), "value": g("value"),
                     "impressions": g("impressions"), "clicks": g("clicks"), "frequency": g("frequency")})
    return data, cols


def verdict(row, be_roas, be_cpa, a):
    s, p, v = row["spend"], row["purchases"], row["value"]
    roas = v / s if s else 0.0
    if s < a.min_spend * be_cpa and p < a.min_purchases:
        return "TOO EARLY", "not enough spend to judge yet"
    if p == 0:
        if s >= a.kill_spend * be_cpa:
            return "KILL", f"spent {s/be_cpa:.1f}x break-even CPA with zero purchases"
        return "WATCH", "no purchase yet"
    if roas >= be_roas * a.scale_buffer and p >= a.min_purchases:
        return "SCALE", f"ROAS {roas/be_roas:.0%} of break-even"
    if roas >= be_roas:
        return "KEEP", "profitable, not enough margin or data to scale"
    if roas >= be_roas * a.watch_floor:
        return "WATCH", "just under break-even"
    if s >= a.kill_spend * be_cpa:
        return "KILL", f"ROAS only {roas/be_roas:.0%} of break-even"
    return "WATCH", "below break-even, small spend so far"


def main(argv=None):
    ap = argparse.ArgumentParser(description="Turn a Meta Ads CSV export into SCALE/KEEP/WATCH/KILL verdicts.")
    ap.add_argument("csv")
    ap.add_argument("--be-roas", type=float, required=True, help="break-even ROAS from true_roas.py")
    ap.add_argument("--be-cpa", type=float, help="break-even CPA in Rs (default: account AOV / break-even ROAS)")
    ap.add_argument("--min-purchases", type=int, default=3, help="purchases needed before SCALE (default 3)")
    ap.add_argument("--min-spend", type=float, default=1.0, help="judge only after this many x break-even CPA spent (default 1)")
    ap.add_argument("--kill-spend", type=float, default=2.0, help="KILL after this many x break-even CPA with no profit (default 2)")
    ap.add_argument("--scale-buffer", type=float, default=1.3, help="SCALE when ROAS is this many x break-even (default 1.3)")
    ap.add_argument("--watch-floor", type=float, default=0.7, help="below this x break-even, losers get KILL (default 0.7)")
    ap.add_argument("--fatigue-freq", type=float, default=3.5, help="flag frequency at or above this (default 3.5)")
    a = ap.parse_args(argv)

    data, cols = load(a.csv)
    tot_s = sum(r["spend"] for r in data)
    tot_p = sum(r["purchases"] for r in data)
    tot_v = sum(r["value"] for r in data)
    if a.be_cpa:
        be_cpa = a.be_cpa
    elif tot_p:
        be_cpa = (tot_v / tot_p) / a.be_roas
    else:
        sys.exit("No purchases in this file, so break-even CPA cannot be worked out. Pass --be-cpa.")

    for r in data:
        r["verdict"], r["why"] = verdict(r, a.be_roas, be_cpa, a)
        r["roas"] = r["value"] / r["spend"] if r["spend"] else 0.0
        r["cpa"] = r["spend"] / r["purchases"] if r["purchases"] else None
        r["ctr"] = r["clicks"] / r["impressions"] * 100 if r["impressions"] else None
        if cols["frequency"] and r["frequency"] >= a.fatigue_freq:
            r["why"] += f"; frequency {r['frequency']:.1f}, check creative fatigue"
    data.sort(key=lambda r: (ORDER.index(r["verdict"]), -r["spend"]))

    acct_roas = tot_v / tot_s if tot_s else 0
    print(f"Account: spend Rs {tot_s:,.0f} | purchases {tot_p:,.0f} | ROAS {acct_roas:.2f} "
          f"vs break-even {a.be_roas:.2f} -> {'PROFITABLE' if acct_roas >= a.be_roas else 'LOSING MONEY'}")
    print(f"Break-even CPA used: Rs {be_cpa:,.0f}\n")
    print("| Verdict | Name | Spend | Purch. | ROAS | CPA | CTR | Why |")
    print("|---|---|---:|---:|---:|---:|---:|---|")
    for r in data:
        cpa = f"{r['cpa']:,.0f}" if r["cpa"] else "-"
        ctr = f"{r['ctr']:.2f}%" if r["ctr"] is not None else "-"
        print(f"| {r['verdict']} | {r['name']} | {r['spend']:,.0f} | {r['purchases']:g} | {r['roas']:.2f} | {cpa} | {ctr} | {r['why']} |")
    print()
    for v in ORDER:
        rows = [r for r in data if r["verdict"] == v]
        if rows:
            print(f"{v}: {len(rows)} {'row' if len(rows) == 1 else 'rows'}, Rs {sum(r['spend'] for r in rows):,.0f} spend")


if __name__ == "__main__":
    sys.exit(main())
