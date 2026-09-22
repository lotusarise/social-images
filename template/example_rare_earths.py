import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from la_design import *
D = '22 September 2026'
S = {}

S['a1'] = page(slide(f'''{top(date=D)}
<div class="tagrow"><span class="tag">ECONOMY  |  GS-3</span><span class="line"></span></div>
{headline("India's ₹7,280-crore push for", "Rare Earth Magnets")}
<div class="rule"></div>
<div class="lead">The <b>REPM scheme</b>, cleared by the Union Cabinet on 26 Nov 2025, aims to build <b class="hl">6,000 tonnes a year</b> of magnet capacity at home, cutting reliance on China.</div>''', hero("magnet", ["car", "wind", "plane", "cpu"]))+f'''<div class="swipe">Swipe {icon("arrow-right", 30, "#D17502", 3)}</div>''', page_no='1/6')

S['a2'] = page(slide(mini_top("WHY IN NEWS") + h2("Why a coin-sized magnet", "became a strategic issue"),
  info("triangle-alert", "The trigger", "In **April 2025**, China put export licensing on **7 medium and heavy rare earths** and related magnets, hitting auto and electronics supply chains.", True)
  + info("magnet", "What are REPMs?", "**Rare Earth Permanent Magnets**: the strongest permanent magnets, made mainly from **NdFeB** or **samarium-cobalt (SmCo)**.")
  + '<div class="banner">Where they are used</div>'
  + cards([("car", "EV motors", "Traction motors in electric vehicles"), ("wind", "Wind turbines", "Direct-drive generators"), ("shield", "Defence", "Missiles, radars, aircraft")])), page_no='2/6')

S['a3'] = page(slide(mini_top("THE SCHEME AT A GLANCE") + h2("REPM scheme:", "the numbers"),
  stats([("₹7,280 cr", "Total outlay over **7 years** (2-year set-up + 5 years of incentives)", True),
        ("₹6,450 cr", "Sales-linked incentives on magnets sold"),
        ("₹750 cr", "Capital subsidy for new plants"),
        ("6,000 <small>TPA</small>", "Target integrated capacity (tonnes/year)"),
        ("5 × 1,200", "Up to 5 firms, max 1,200 TPA each, via **global bidding**")])
  + '<div class="banner or">Integrated value chain covered</div>' + chain(["Oxide", "Metal", "Alloy", "Magnet"])), page_no='3/6')

S['a4'] = page(slide(mini_top("WHERE INDIA IS EXPOSED") + h2("India's magnet", "import dependence"),
  stats([("84.8–90.4%", "China's share of India's REPM imports **by quantity** (2022-23 to 2024-25)", True),
        ("59.6–81.3%", "China's share **by value** over the same period"),
        (">85%", "Share of world rare earth magnet output made in **China**"),
        ("2×", "Expected rise in India's REPM demand **by 2030** (vs 2025)"),
        ("7.23 Mt", "Rare earth oxides in India's **13.15 Mt monazite** reserves")])
  + info("factory", "The real gap is midstream", "India mines and separates oxides (IREL), but lacks industrial-scale **metal, alloy and magnet** making.", True)), page_no='4/6')

S['a5'] = page(slide(mini_top("PRELIMS POINTERS") + h2("Facts to", "remember"),
  flash([("17 rare earths", "15 **lanthanides** + scandium + yttrium"),
        ("NdFeB (Nd₂Fe₁₄B)", "Strongest commercial permanent magnet; developed in the **early 1980s**"),
        ("Dysprosium & terbium", "Heavy rare earths added so NdFeB works at **high temperature**"),
        ("SmCo magnets", "Better heat tolerance; used in **defence & aerospace**"),
        ("Monazite", "Beach placers of **Kerala, TN, Odisha, AP**; contains thorium"),
        ("Atomic mineral", "Because of thorium; mined by **IREL** (Dept of Atomic Energy)")]), fill=True), page_no='5/6')

S["a6"] = page(slide(mini_top("MAINS ANGLE", logo=True) + h2("Challenges &", "way forward"),
  cards([("gem", "Scarce heavy REEs", "Dy and Tb are limited in Indian deposits"),
        ("atom", "Thorium rules", "Monazite processing is tightly regulated"),
        ("recycle", "No recycling", "No recovery targets for magnets in e-waste")])
  + bullets_box("lightbulb", "Way forward", ["Magnet recycling from **e-waste and EV motors**", "Overseas sourcing via the **Minerals Security Partnership**", "Align with the **National Critical Mineral Mission**"], True)
  + '<div class="mq">Q. "Critical-mineral security is now national security." Examine with reference to rare earth permanent magnets. <span style="color:#D17502">(15 marks)</span></div>'
  + '<div class="chips"><span class="chip">GS-3 Economy</span><span class="chip">GS-2 IR</span><span class="chip">Geography Optional</span></div>'), page_no='6/6')

Q = ["NdFeB magnets tolerate high temperatures better than samarium-cobalt magnets.",
     "Dysprosium and terbium are added to NdFeB magnets to improve high-temperature performance.",
     "In India, monazite is treated as an atomic mineral because it contains thorium.",
     "Scandium and yttrium are members of the lanthanide series."]
S['b1'] = page(slide(mini_top("PRELIMS PRACTICE  |  GS-3", logo=True) + h2("Rare earths &", "magnets"),
  mcq_q(Q, "How many of the above statements are correct?", ["Only one", "Only two", "Only three", "All four"])), cta='Share your answer in comments')

S['b2'] = page(slide(mini_top("ANSWER & EXPLANATION", logo=True) + '<div class="ans"><div class="a">(B)</div><div class="t">Only two statements are correct:<br>statements 2 and 3</div></div>',
  verdicts([(False, "1. Incorrect", "NdFeB is the strongest, but loses strength above ~150°C. **SmCo handles heat better.**"),
           (True, "2. Correct", "Dy and Tb raise coercivity, keeping NdFeB stable in **hot EV motors**."),
           (True, "3. Correct", "Monazite contains **thorium**, so it is an atomic mineral; mined by IREL."),
           (False, "4. Incorrect", "Rare earths = 15 lanthanides **+ Sc + Y**. Sc and Y are **not** lanthanides.")])), page_no='2/2')

for k, v in S.items():
    open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'html', f'{k}.html'), 'w').write(v)
print('ok')

# ---- Pinterest pin (1000x1500) ----
P = {}
P['pin_a'] = page(slide(top(date=D) + '<div class="tagrow"><span class="tag">PRELIMS + MAINS  |  GS-3</span><span class="line"></span></div>' + headline("Rare earth magnets:", "10 facts for UPSC"),
  flash([("₹7,280 cr", "REPM scheme, Cabinet 26 Nov 2025"), ("6,000 TPA", "Target; up to 5 firms × 1,200 TPA"),
         ("₹6,450 cr + ₹750 cr", "Sales incentives + capital subsidy"), ("84.8–90.4%", "China's share of India's REPM imports (qty)"),
         ("17 rare earths", "15 lanthanides + Sc + Y"), ("NdFeB", "Strongest; Dy/Tb added for heat"),
         ("SmCo", "Heat-tolerant; defence use"), ("Monazite", "Thorium-bearing atomic mineral; IREL")]), fill=True), W=1000, H=1500, h1=72)
# ---- X / LinkedIn card (1200x675) ----
P['x_a'] = page(slide(mini_top("CURRENT AFFAIRS  |  GS-3", logo=True) + h2("India's ₹7,280-crore", "rare earth magnet push"),
  stats([("6,000 TPA", "Target integrated capacity"), ("84.8–90.4%", "China's share of India's REPM imports (qty)")])), W=1200, H=675)
for k, v in P.items():
    open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'html', f'{k}.html'), 'w').write(v)
