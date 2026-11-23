<p align="center">
  <img src="https://akshaysinghhada.com/wp-content/uploads/2026/11/d2c-performance-marketing-claude-skills.png" alt="D2C performance marketing Claude skills for Indian brands: true ROAS, RTO, daily Meta ads report, festive planner and Hinglish hooks" width="100%">
</p>

# D2C Performance Marketing Claude Skills

**7 free Claude skills for Indian D2C performance marketers.** Built for the problems global marketing tools ignore: COD, RTO, GST, festive auctions and Hinglish creatives.

Made by **[Akshay Singh Hada](https://akshaysinghhada.com/akshay-singh-hada/)**, performance marketing manager in Jaipur with 7+ years in Meta and Google Ads for fashion jewellery D2C and B2B brands. These skills are the checks I run by hand every week, written down so Claude can run them for you.

No coding needed. No API keys. Nothing gets posted or changed in your ad account.

---

## Sound familiar?

- Meta shows **ROAS 3**. Your bank account shows a loss.
- A third of your **COD orders come back**, and the courier bills you both ways.
- Meta says **50 purchases**. Shopify says 32. Which one is real?
- **ROAS fell overnight** and the team wants to change everything at once.
- The **Diwali budget** is approved. The creatives are not tested.
- Your ad copy reads like it was **translated from English**.

Each skill below fixes one of these.

## The 7 skills

| Skill | The problem it fixes | Ask Claude something like |
|---|---|---|
| [`d2c-true-roas`](skills/d2c-true-roas/SKILL.md) | "ROAS 3 but no profit" | "AOV 999, product cost 250, COD 60%, RTO 25%. What's my break-even ROAS?" |
| [`d2c-daily-ads-report`](skills/d2c-daily-ads-report/SKILL.md) | "Which ads are burning money?" | "Here's my Meta export. What do I pause or scale today?" |
| [`d2c-roas-drop-doctor`](skills/d2c-roas-drop-doctor/SKILL.md) | "ROAS dropped and I don't know why" | "ROAS went from 3.2 to 1.8 in 5 days. What happened?" |
| [`d2c-attribution-gap`](skills/d2c-attribution-gap/SKILL.md) | "Meta and Shopify don't match" | "Meta says 64 purchases, Shopify says 41. Which is real?" |
| [`d2c-rto-reducer`](skills/d2c-rto-reducer/SKILL.md) | "COD orders keep coming back" | "COD RTO is 32%. Where do I start?" |
| [`d2c-festive-planner`](skills/d2c-festive-planner/SKILL.md) | "Festive season chaos" | "Plan Valentine's for a jewellery brand with a ₹2 lakh budget" |
| [`d2c-hinglish-hooks`](skills/d2c-hinglish-hooks/SKILL.md) | "Copy that sounds translated" | "Oxidised jhumka at ₹799. 10 Hinglish hooks and a Reel script" |

The skills work together. `d2c-true-roas` gives the break-even ROAS that the daily report, the ROAS doctor and the festive planner all use.

**Hinglish works.** Ask "Meri AOV 1,299 hai, RTO 28%, break-even ROAS kya hai?" and Claude answers in Hinglish.

## Install (pick one)

**1. Let Claude do it (Claude Code).** Paste this into Claude:

```
https://github.com/akshaysinghhada/d2c-performance-marketing-claude-skills

Install these skills, then run d2c-true-roas on the sample numbers.
```

**2. As a plugin (Claude Code):**

```
/plugin install d2c-performance-marketing --marketplace akshaysinghhada/d2c-performance-marketing-claude-skills
```

On older Claude Code versions, use two steps:

```
/plugin marketplace add akshaysinghhada/d2c-performance-marketing-claude-skills
/plugin install d2c-performance-marketing
```

**3. Manually:**

```bash
git clone https://github.com/akshaysinghhada/d2c-performance-marketing-claude-skills.git
cp -r d2c-performance-marketing-claude-skills/skills/d2c-* ~/.claude/skills/
```

**4. In the Claude app:** download a skill folder as a ZIP and upload it under Customize > Skills. Code execution must be turned on. Without it, the skills still work; Claude just does the maths in the chat instead of running the scripts.

## See it work

These are real outputs from the two scripts in this repo, using sample numbers for a ₹999 fashion jewellery order.

**`true_roas.py`: what ROAS do you actually need?**

```
TRUE ROAS - per order Meta counts as a purchase
====================================================
Meta counts revenue of                ₹999
Orders delivered                     83.0%
Orders lost to RTO                   17.0%
Returned after delivery               4.2%
GST you pay out                        ₹23
Revenue you actually keep             ₹765

Costs per order placed
  product cost (kept orders)          ₹197
  product lost (damaged units)          ₹5
  forward shipping                     ₹60
  packaging                            ₹20
  RTO shipping                         ₹10
  return pickup                         ₹3
  COD fee                              ₹16
  gateway fee (prepaid)                 ₹8
Left before ads                       ₹446

BREAK-EVEN CPA (incl. GST on ad spend):  ₹378
BREAK-EVEN ROAS (as Meta reports it):  2.65
ROAS needed for 15% profit margin:  3.56

Profit per order at the ROAS Meta shows
  ROAS 1.5  ->     -₹340  <- loss
  ROAS 2    ->     -₹144  <- loss
  ROAS 2.5  ->      -₹26  <- loss
  ROAS 3    ->       ₹53
  ROAS 3.5  ->      ₹109
  ROAS 4    ->      ₹151
  ROAS 5    ->      ₹210
  ROAS 6    ->      ₹249
```

Meta would call a 2.5 ROAS "fine". At these numbers it loses ₹26 on every order.

No Claude yet? Try the same maths in the free [browser calculator](https://akshaysinghhada.com/break-even-roas-calculator/).

**`meta_report.py`: what to do today** (on [`sample-meta-export.csv`](skills/d2c-daily-ads-report/sample-meta-export.csv))

```
Account: spend Rs 12,900 | purchases 26 | ROAS 2.08 vs break-even 2.65 -> LOSING MONEY
Break-even CPA used: Rs 389

| Verdict | Name | Spend | Purch. | ROAS | CPA | CTR | Why |
|---|---|---:|---:|---:|---:|---:|---|
| KILL | Diwali_Static_Offer | 3,100 | 4 | 1.29 | 775 | 0.85% | ROAS only 49% of break-even; frequency 4.1, check creative fatigue |
| KILL | Bridal_Set_Carousel | 2,600 | 0 | 0.00 | - | 1.35% | spent 6.7x break-even CPA with zero purchases |
| SCALE | Jhumka_UGC_Hook3 | 4,200 | 16 | 3.81 | 262 | 1.50% | ROAS 144% of break-even |
| WATCH | Earring_Price_Hook | 900 | 2 | 2.22 | 450 | 1.33% | just under break-even |
| KEEP | Oxidised_Reel_v2 | 1,800 | 4 | 2.66 | 450 | 1.39% | profitable, not enough margin or data to scale |
| TOO EARLY | New_Collection_Generic | 300 | 0 | 0.00 | - | 0.88% | not enough spend to judge yet |

KILL: 2 rows, Rs 5,700 spend
SCALE: 1 row, Rs 4,200 spend
WATCH: 1 row, Rs 900 spend
KEEP: 1 row, Rs 1,800 spend
TOO EARLY: 1 row, Rs 300 spend
```

## Safe by design

- **No API keys, no logins, no internet calls.** The two Python scripts use only the standard library and do maths on the numbers you give them. Read them; they are short.
- **Nothing changes in your ad account.** Every skill recommends. You or your agency make the change.
- **Totals only.** No skill asks for customer names, phone numbers or addresses. Under India's DPDP rules, keep personal data out of AI chats. More in my [DPDP guide for marketers](https://akshaysinghhada.com/dpdp-consent-manager-13-november-2026/).
- **No made-up numbers.** Festival dates, GST rates and RTO rates are asked for or checked, never guessed.

## Read more

- [Break even ROAS calculator for Indian D2C](https://akshaysinghhada.com/break-even-roas-calculator/), the web version of `d2c-true-roas`
- [8 best free Claude skills on GitHub for marketers](https://akshaysinghhada.com/claude-skills-for-marketers/), and how to check any skill before you install it
- [Instagram AI automation with Claude](https://akshaysinghhada.com/instagram-ai-automation-claude/), tested on real jewellery hooks
- [Claude SEO plugin guide](https://akshaysinghhada.com/claude-seo-plugin/)
- [Why Meta ROAS drops during big sale events](https://akshaysinghhada.com/meta-ads-roas-drop-big-billion-days/)
- More guides at **[akshaysinghhada.com](https://akshaysinghhada.com/)**

## Contributing

Got a D2C problem you fight every week? [Open an issue](../../issues) and describe it. The most common ones become the next skill. Pull requests are welcome; keep skills practical, India-aware and free of invented numbers.

If a skill saved you money or a late night, a ⭐ helps other marketers find it.

## Licence

[MIT](LICENSE) © 2026 Akshay Singh Hada
