import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from la_design import *
HERE = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(HERE, 'html'), exist_ok=True)
D = '14 November 2026'
S = {}

# ============================================================
# CAROUSEL A - NITI Aayog Impact Assessment of PLI Schemes (GS-3)
# ============================================================
S['a1'] = page(slide(f'''{top(date=D)}
<div class="tagrow"><span class="tag">ECONOMY  |  GS-3</span><span class="line"></span></div>
{headline("PLI schemes at the", "halfway mark")}
<div class="rule"></div>
<div class="lead">NITI Aayog's mid-course <b>Impact Assessment of PLI Schemes</b> finds <b class="hl">76%</b> of the investment target met — but only <b class="hl">28%</b> of the jobs target.</div>''',
  hero("factory", ["smartphone", "pill", "car", "drone"])) +
  f'<div class="swipe">Swipe {icon("arrow-right", 30, "#D17502", 3)}</div>', page_no='1/6')

S['a2'] = page(slide(mini_top("WHY IN NEWS") + h2("What the report", "actually is"),
  info("landmark", "Who released it", "**NITI Aayog**, with ==IIM Ahmedabad== as knowledge partner, on **12 November 2026**.", True)
  + info("target", "What it measures", "All **14 PLI sectors** on four outcomes: **investment, production, exports and employment**.")
  + info("gauge", "The yardstick", "==50% of full-tenure targets== as a mid-course screen. Implementation is **58% complete**.")), page_no='2/6')

S['a3'] = page(slide(mini_top("THE SCORECARD") + h2("Cumulative, up to", "March 2026"),
  stats([("₹2.40 <small>lakh cr</small>", "Investment realised — **76%** of the ₹3.15 lakh crore target", True),
         ("₹22.66 <small>lakh cr</small>", "Production and sales — **64%** of target"),
         ("8.49 <small>lakh</small>", "Jobs created — only **28%** of target"),
         ("₹35,354 <small>cr</small>", "Incentives paid — **18.51%** of outlay"),
         ("₹1.91 <small>lakh cr</small>", "Approved outlay across **14 sectors**")])), page_no='3/6')

S['a4'] = page(slide(mini_top("WHAT WORKED") + h2("Sectors pulling", "their weight"),
  stats([("₹2 <small>lakh cr</small>", "Mobile phone exports in **FY2025** — a first; imports fell **77%**", True),
         ("+32.7%", "Pharma exports, **$19.46bn → $25.82bn**"),
         ("7×", "Drone turnover; **77.5%** of outlay used")])
  + info("pill", "Bulk drugs turned around", "A **₹1,930 cr deficit** in FY2021-22 became a ==₹2,280 cr surplus== by FY2024-25.")), page_no='4/6')

S['a5'] = page(slide(mini_top("WHERE IT LAGS") + h2("The gaps the", "report flags"),
  cards([("users", "Jobs", "8.49 lakh of a 30.19 lakh target"),
         ("battery", "ACC batteries", "Localisation norms, long gestation"),
         ("shirt", "Technical textiles", "Only **3.61%** of funds used")])
  + bullets_box("triangle-alert", "Structural concerns", [
      "Limited **domestic value addition**",
      "Uneven performance across sectors",
      "Frequent **policy revisions** and delays"], True)), page_no='5/6')

S['a6'] = page(slide(mini_top("MAINS ANGLE", logo=True) + h2("Way forward &", "exam angle"),
  bullets_box("lightbulb", "What NITI Aayog recommends", [
      "**Sector-specific** design, not one template",
      "Add **demand-pull**: procurement and exports",
      "Deepen **MSME** participation; harmonise data"], True)
  + '<div class="mq">Q. PLI has bought India scale, but not yet jobs or depth. Critically examine. <span style="color:#D17502">(15 marks)</span></div>'
  + '<div class="chips"><span class="chip">GS-3 Economy</span><span class="chip">GS-2 Governance</span><span class="chip">Prelims</span></div>'), page_no='6/6')

# ============================================================
# CAROUSEL B - Prelims MCQ on the PLI review
# ============================================================
Q = ["The Production Linked Incentive (PLI) schemes were launched in 2020 and currently cover 14 sectors.",
     "PLI incentives are computed on incremental sales over a base year and are released only after prescribed investment and production conditions are met.",
     "The 2026 impact assessment of the PLI schemes was prepared by the Ministry of Commerce and Industry with the World Bank as knowledge partner.",
     "By March 2026 the schemes had met a larger share of their employment target than of their investment target."]

S['b1'] = page(slide(mini_top("PRELIMS PRACTICE  |  GS-3", logo=True) + h2("PLI schemes &", "the 2026 review"),
  mcq_q(Q, "Which of the statements given above is/are correct?",
        ["1 and 2 only", "2 and 3 only", "1, 3 and 4 only", "1, 2 and 4 only"])), cta='Reply with your answer')

S['b2'] = page(slide(mini_top("ANSWER & EXPLANATION", logo=True) +
  '<div class="ans"><div class="a">(A)</div><div class="t">Only statements 1 and 2<br>are correct</div></div>',
  verdicts([(True, "1. Correct", "PLI began in **2020** under Atmanirbhar Bharat and covers **14 notified sectors**."),
            (True, "2. Correct", "Incentives ride on **incremental sales** over a base year, paid only after thresholds are met."),
            (False, "3. Incorrect", "It was **NITI Aayog**, with ==IIM Ahmedabad== as knowledge partner — not the World Bank."),
            (False, "4. Incorrect", "Reversed. Investment is at **76%** of target; employment at just **28%**.")])), page_no='2/2')

# ============================================================
# CAROUSEL C - Global Carbon Budget 2026 (GS-3 / Geography)
# ============================================================
S['c1'] = page(slide(f'''{top(date=D)}
<div class="tagrow"><span class="tag">ENVIRONMENT  |  GS-3</span><span class="line"></span></div>
{headline("Global Carbon Budget", "2026")}
<div class="rule"></div>
<div class="lead">Fossil CO₂ is projected to <b class="hl">fall 0.4%</b> to <b>38.2 billion tonnes</b> in 2026 — while India's emissions rise <b class="hl">4.4%</b>.</div>''',
  hero("thermometer", ["factory", "car", "flame", "leaf"])) +
  f'<div class="swipe">Swipe {icon("arrow-right", 30, "#D17502", 3)}</div>', page_no='1/6')

S['c2'] = page(slide(mini_top("WHY IN NEWS") + h2("What the Global", "Carbon Budget is"),
  info("globe", "The report", "The **21st annual** budget from the ==Global Carbon Project==, released as a preprint on **10 November 2026**.", True)
  + info("users", "Who built it", "Over **140 scientists** across **90+ institutions**, led from the **University of Exeter**.")
  + info("calendar", "Where it landed", "Published during ==COP31== at **Antalya, Türkiye** (9-20 November 2026).")), page_no='2/6')

S['c3'] = page(slide(mini_top("THE GLOBAL PICTURE") + h2("Four numbers that", "frame 2026"),
  stats([("38.2 <small>bn t</small>", "Fossil CO₂ in 2026 — **down 0.4%** on 2025", True),
         ("5.1 <small>bn t</small>", "Land-use change CO₂, and **rising**"),
         ("43.3 <small>bn t</small>", "Total CO₂, up from **42.8** in 2025"),
         ("427.7 <small>ppm</small>", "Atmospheric CO₂ — **54%** above pre-industrial"),
         ("150 <small>bn t</small>", "Left for **1.5°C**: under **four years**")])), page_no='3/6')

S['c4'] = page(slide(mini_top("WHO IS CUTTING, WHO IS NOT") + h2("The country", "split"),
  stats([("+4.4%", "**India** — the one large economy projected up", True),
         ("-0.9%", "**China**, though its coal use rose 0.3%"),
         ("-1.3%", "**United States**"),
         ("-1.5%", "**European Union**"),
         ("-1.9%", "**Oil** worldwide; gas -0.3%, coal **+0.6%**")])), page_no='4/6')

S['c5'] = page(slide(mini_top("WHY INDIA IS RISING") + h2("Four drivers behind", "the 4.4%"),
  cards([("thermometer", "Cooling demand", "A drier monsoon and a hotter year"),
         ("flame", "Coal-led power", "Coal still dominates generation"),
         ("car", "Road transport", "Vehicle ownership keeps climbing")])
  + info("factory", "And heavy industry", "Steel, cement and construction keep fossil demand growing; new renewables are ==not yet offsetting== that growth.", True)), page_no='5/6')

S['c6'] = page(slide(mini_top("PRELIMS POINTERS") + h2("Facts to", "remember"),
  flash([("38.2 bn t", "Fossil CO₂ in 2026, **down 0.4%**"),
         ("43.3 bn t", "Total CO₂ including land-use change"),
         ("427.7 ppm", "Atmospheric CO₂, **54%** above pre-industrial"),
         ("150 bn t", "Remaining **1.5°C** carbon budget"),
         ("Global Carbon Project", "Publishes the budget; **21st** edition"),
         ("COP31", "**Antalya, Türkiye**, 9-20 Nov 2026"),
         ("India +4.4%", "China -0.9%, US -1.3%, EU -1.5%"),
         ("Land sink", "Recovered after the **2023-24 El Niño**")]), fill=True), page_no='6/6')

for k, v in S.items():
    open(os.path.join(HERE, 'html', f'{k}.html'), 'w').write(v)

# ============================================================
# PINTEREST PINS (1000 x 1500)
# ============================================================
P = {}
P['pin_a'] = page(slide(top(date=D)
  + '<div class="tagrow"><span class="tag">PRELIMS + MAINS  |  GS-3</span><span class="line"></span></div>'
  + headline("PLI schemes:", "the 2026 scorecard"),
  flash([("₹2.40 lakh cr", "Investment realised — 76% of target"),
         ("₹22.66 lakh cr", "Production and sales — 64% of target"),
         ("8.49 lakh", "Jobs created — only 28% of target"),
         ("₹35,354 cr", "Incentives paid, 18.51% of outlay"),
         ("₹1.91 lakh cr", "Outlay across 14 sectors"),
         ("58%", "Of the implementation period elapsed"),
         ("₹2 lakh cr", "Mobile exports, FY2025 — a first"),
         ("NITI Aayog", "Report with IIM Ahmedabad, 12 Nov 2026")]), fill=True), W=1000, H=1500, h1=72)

P['pin_b'] = page(slide(mini_top("PRELIMS PRACTICE  |  GS-3", logo=True) + h2("PLI schemes &", "the 2026 review"),
  mcq_q(Q, "Which of the statements given above is/are correct?",
        ["1 and 2 only", "2 and 3 only", "1, 3 and 4 only", "1, 2 and 4 only"])), W=1000, H=1500, h1=72, cta='Answer in the description')

P['pin_c'] = page(slide(top(date=D)
  + '<div class="tagrow"><span class="tag">ENVIRONMENT  |  GS-3</span><span class="line"></span></div>'
  + headline("Global Carbon Budget", "2026: 8 facts"),
  flash([("38.2 bn t", "Fossil CO₂ in 2026, down 0.4%"),
         ("43.3 bn t", "Total CO₂ including land use"),
         ("5.1 bn t", "Land-use change CO₂, rising"),
         ("427.7 ppm", "Atmospheric CO₂, 54% above pre-industrial"),
         ("150 bn t", "Remaining 1.5°C budget — under 4 years"),
         ("India +4.4%", "China -0.9%, US -1.3%, EU -1.5%"),
         ("Global Carbon Project", "21st annual edition"),
         ("COP31", "Antalya, Türkiye, 9-20 Nov 2026")]), fill=True), W=1000, H=1500, h1=72)

# ============================================================
# FACEBOOK CARDS (1200 x 675)
# ============================================================
P['fb_a'] = page(slide(mini_top("CURRENT AFFAIRS  |  GS-3", logo=True) + h2("PLI at the halfway", "mark: 76% vs 28%"),
  stats([("₹2.40 lakh cr", "Investment — 76% of target"), ("8.49 lakh", "Jobs — 28% of target")])), W=1200, H=675)

P['fb_b'] = page(slide(mini_top("PRELIMS PRACTICE  |  GS-3", logo=True) + h2("PLI schemes &", "the 2026 review"),
  stats([("4 statements", "One answer. Options (A)-(D)"), ("GS-3", "Economy · Manufacturing")])), W=1200, H=675)

P['fb_c'] = page(slide(mini_top("CURRENT AFFAIRS  |  GS-3", logo=True) + h2("Global Carbon Budget", "2026"),
  stats([("38.2 bn t", "Fossil CO₂ in 2026, down 0.4%"), ("India +4.4%", "The one large economy rising")])), W=1200, H=675)

for k, v in P.items():
    open(os.path.join(HERE, 'html', f'{k}.html'), 'w').write(v)

print('ok', len(S) + len(P), 'slides')
