import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from la_design import *

D = '27 September 2026'
HERE = os.path.dirname(os.path.abspath(__file__))
S = {}

# ============ CAROUSEL A - in-depth current affairs (7 slides) ============
S['a1'] = page(slide(f'''{top(date=D)}
<div class="tagrow"><span class="tag">GEOGRAPHY  |  GS-1 &middot; GS-2</span><span class="line"></span></div>
{headline("30 river links, one", "federal knot")}
<div class="rule"></div>
<div class="lead">Linking the <b>Brahmaputra to the Godavari and Cauvery</b> was pitched at the <b class="hl">31st Southern Zonal Council</b> (Mahabalipuram, 20 Aug 2026). The plan is <b>46 years old</b> — and still mostly on paper.</div>''',
  hero("waves", ["mountain", "droplets", "landmark", "sprout"]))
  + f'''<div class="swipe">Swipe {icon("arrow-right", 30, "#D17502", 3)}</div>''', page_no='1/7')

S['a2'] = page(slide(mini_top("WHERE IT CAME UP") + h2("The forum, and the", "body it is not"),
  info("landmark", "Zonal Councils", "Five of them, under **Part III (ss. 15-22) of the States Reorganisation Act, 1956** — so ==statutory==, not constitutional.")
  + info("users", "Who sits on one", "Chairman: the **Union Home Minister**. Vice-Chairman: a member-State **Chief Minister, by yearly rotation**. Advisory only.", True)
  + info("scale", "The standing trap", "The ==Article 263== body is the **Inter-State Council**. Zonal Councils have no constitutional source at all.")), page_no='2/7')

S['a3'] = page(slide(mini_top("THE PLAN ON PAPER") + h2("National Perspective", "Plan, 1980"),
  stats([("30 links", "Identified in the NPP: **16 Peninsular** + **14 Himalayan**", True),
         ("1982", "**NWDA** set up as a registered society to study them"),
         ("24", "Feasibility reports completed so far"),
         ("8", "Detailed Project Reports completed"),
         ("2014", "**Special Committee on ILR**, after the Supreme Court's 2012 direction")])), page_no='3/7')

S['a4'] = page(slide(mini_top("THE ONE THAT MOVED") + h2("Ken-Betwa Link:", "the flagship"),
  stats([("Rs 44,605 cr", "Cleared by the Union Cabinet on **8 Dec 2021** — the ==first major centrally driven river link==", True),
         ("10.62 lakh ha", "Annual irrigation: **8.11 lakh** MP + **2.51 lakh** UP"),
         ("62 lakh", "People to get drinking water (**194 MCM**)"),
         ("130 MW", "**103 MW hydro** + 27 MW solar"),
         ("8 years", "Timeline; **Daudhan Dam** on the Ken, Bundelkhand")])), page_no='4/7')

S['a5'] = page(slide(mini_top("WHY IT MOVES SLOWLY") + h2("The constitutional", "knot"),
  info("droplets", "Entry 17, State List", "**Water** — supplies, irrigation, canals, storage, water power — is a ==State== subject.")
  + info("landmark", "Entry 56, Union List", "**Inter-State rivers** are Union — but ==only to the extent Parliament declares by law==.", True)
  + info("gavel", "Article 262", "Parliament may bar **the Supreme Court and every other court** from an inter-State water dispute.")), page_no='5/7')

S['a6'] = page(slide(mini_top("CHALLENGES & WAY FORWARD") + h2("Four objections,", "one rethink"),
  cards([("leaf", "Ecology", "Sediment, wetlands, aquatic life; Panna Tiger Reserve submergence"),
         ("users", "Displacement", "Land acquisition and tribal resettlement in Bundelkhand"),
         ("cloud-rain", "Climate", "Which basin is truly 'surplus' is no longer a stable fact")])
  + bullets_box("lightbulb", "The cheaper half of the answer",
      ["**Micro-irrigation** and crop change before new canals",
       "**Watershed management** and groundwater recharge",
       "A ==single standing tribunal== instead of ad hoc ones"], True)), page_no='6/7')

S['a7'] = page(slide(mini_top("PRELIMS POINTERS", logo=True) + h2("Facts to", "remember"),
  flash([("NPP, 1980", "30 links: **16 Peninsular**, **14 Himalayan**"),
         ("NWDA, 1982", "Registered society; now under **Jal Shakti**"),
         ("Entry 17 / Entry 56", "Water = **State** List; inter-State rivers = **Union**"),
         ("Article 262", "Parliament may oust **every court's** jurisdiction"),
         ("ISRWD Act, 1956", "Tribunal in **1 year**; award in **3**, +2 more"),
         ("Zonal Councils", "**Five**; SRA 1956 — statutory and advisory"),
         ("Ken-Betwa", "**Daudhan Dam**; Cabinet **8 Dec 2021**"),
         ("Godavari-Cauvery", "Via Krishna and Pennar to the **Grand Anicut**")]), fill=True), page_no='7/7')

# ============ CAROUSEL B - Prelims MCQ (2 slides) ============
Q = ["The National Water Development Agency, which studies river-link proposals, was set up as a registered society in 1982.",
     "Zonal Councils are constitutional bodies constituted under Article 263 of the Constitution.",
     "Article 262 permits Parliament to provide that neither the Supreme Court nor any other court shall exercise jurisdiction in an inter-State river water dispute.",
     "Water is a subject of the Union List, while the regulation of inter-State rivers falls in the State List."]

S['b1'] = page(slide(mini_top("PRELIMS PRACTICE  |  GS-2", logo=True) + h2("Rivers and the", "Constitution"),
  mcq_q(Q, "How many of the above statements are correct?", ["Only one", "Only two", "Only three", "All four"])),
  cta='Answer in the next slide')

S['b2'] = page(slide(mini_top("ANSWER & EXPLANATION", logo=True)
  + '<div class="ans"><div class="a">(B)</div><div class="t">Only two are correct:<br>statements 1 and 3</div></div>',
  verdicts([(True, "1. Correct", "**NWDA, 1982** — a registered society under the then Ministry of Irrigation; today under **Jal Shakti**."),
            (False, "2. Incorrect", "Zonal Councils are ==statutory==: **Part III, States Reorganisation Act, 1956**. Article 263 is the **Inter-State Council**."),
            (True, "3. Correct", "Article 262 lets Parliament oust the jurisdiction of ==every court, the Supreme Court included==."),
            (False, "4. Incorrect", "Reversed. **Water is Entry 17, State List**; ==inter-State rivers is Entry 56, Union List==.")])), page_no='2/2')

# ============ CAROUSEL C - Mains angle (4 slides) ============
S['c1'] = page(slide(f'''{top(kicker_a='MAINS', kicker_b='ANGLE', date=D)}
<div class="tagrow"><span class="tag">GS-2 FEDERALISM  |  GS-1 GEOGRAPHY</span><span class="line"></span></div>
{headline("Why 30 river links became", "a federalism question")}
<div class="rule"></div>
<div class="lead">Most answers treat interlinking as an engineering problem. The marks sit in the <b class="hl">constitutional design</b>: water is a State subject the Union may regulate only as far as Parliament declares.</div>''',
  hero("git-branch", ["scale", "gavel", "handshake", "droplets"])), page_no='1/4')

S['c2'] = page(slide(mini_top("THE FRAME") + h2("Three questions,", "in this order"),
  cards([("scale", "Who owns it?", "Entry 17 State List, read with Entry 56 Union List"),
         ("gavel", "Who decides?", "Article 262 and the tribunals under the ISRWD Act, 1956"),
         ("handshake", "Who agrees?", "Zonal and Inter-State Councils — advisory, never binding")])
  + info("triangle-alert", "Where it breaks", "Adjudication is binding; **consent is not procurable**. An award can be won and still go unimplemented.", True)), page_no='2/4')

S['c3'] = page(slide(mini_top("ANSWER STRUCTURE") + h2("Five points that", "carry marks"),
  bullets_box("list", "Build it like this",
    ["**Hydrology**: 'surplus' basins are a ==1980 assumption==, not a climate-era fact",
     "**Constitution**: Entry 17 against Entry 56; Article 262 ousts the courts",
     "**Institutions**: the coordination bodies only advise, they cannot bind",
     "**Evidence**: Ken-Betwa cleared 2021 — ==one of 30 links in 46 years==",
     "**Alternative**: demand-side efficiency before inter-basin transfer"])), page_no='3/4')

S['c4'] = page(slide(mini_top("PROBABLE QUESTION", logo=True) + h2("Write this one", "this week"),
  '<div class="mq">Q. "India\'s river-interlinking programme is constrained less by hydrology than by the federal design of water governance." Critically examine. <span style="color:#D17502">(15 marks)</span></div>'
  + info("quote", "A line to open with", "Water is **Entry 17 of the State List** — but only ==to the extent== Entry 56 permits Parliament to step in.")
  + '<div class="chips"><span class="chip">GS-2 Federalism</span><span class="chip">GS-1 Geography</span><span class="chip">GS-3 Environment</span><span class="chip">Geography Optional</span></div>'), page_no='4/4')

for k, v in S.items():
    open(os.path.join(HERE, 'html', f'{k}.html'), 'w').write(v)

# ============ PINTEREST PINS (1000x1500) ============
P = {}
P['pin_a'] = page(slide(top(date=D)
  + '<div class="tagrow"><span class="tag">PRELIMS + MAINS  |  GS-1 &middot; GS-2</span><span class="line"></span></div>'
  + headline("River interlinking:", "8 facts for UPSC"),
  flash([("NPP, 1980", "30 links: 16 Peninsular, 14 Himalayan"),
         ("NWDA, 1982", "Registered society; now under Jal Shakti"),
         ("Entry 17 / 56", "Water = State List; inter-State rivers = Union"),
         ("Article 262", "Parliament may oust every court's jurisdiction"),
         ("ISRWD Act, 1956", "Tribunal in 1 year; award in 3, +2 more"),
         ("Zonal Councils", "Five; SRA 1956 - statutory, advisory"),
         ("Ken-Betwa", "Rs 44,605 cr; Cabinet 8 Dec 2021; Daudhan Dam"),
         ("10.62 lakh ha", "Ken-Betwa annual irrigation; 62 lakh get water")]), fill=True),
  W=1000, H=1500, h1=72)

P['pin_b'] = page(slide(top(kicker_a='PRELIMS', kicker_b='PRACTICE', date=D)
  + '<div class="tagrow"><span class="tag">GS-2  |  POLITY + GEOGRAPHY</span><span class="line"></span></div>'
  + headline("Rivers and the Constitution:", "two classic traps"),
  flash([("Trap 1", "Zonal Councils are statutory - SRA 1956, Part III"),
         ("Article 263", "That is the Inter-State Council, a different body"),
         ("Trap 2", "Water is Entry 17 of the STATE List"),
         ("Entry 56", "Inter-State rivers: Union, as Parliament declares"),
         ("Article 262", "Parliament may bar the SC and all other courts"),
         ("NWDA", "1982, registered society under Jal Shakti today"),
         ("Answer", "Only two statements are correct: 1 and 3"),
         ("ISRWD Act, 1956", "Tribunal in 1 year; award in 3, +2 more")]), fill=True),
  W=1000, H=1500, h1=68)

P['pin_c'] = page(slide(top(kicker_a='MAINS', kicker_b='ANGLE', date=D)
  + '<div class="tagrow"><span class="tag">GS-2 FEDERALISM  |  15 MARKS</span><span class="line"></span></div>'
  + headline("River interlinking as a", "federalism question"),
  bullets_box("list", "Five points that carry marks",
    ["**Hydrology**: 'surplus' basins are a ==1980 assumption==",
     "**Constitution**: Entry 17 against Entry 56; Art 262 ousts courts",
     "**Institutions**: coordination bodies advise, never bind",
     "**Evidence**: ==one of 30 links cleared in 46 years==",
     "**Alternative**: demand-side efficiency first"])
  + '<div class="mq">Q. "Constrained less by hydrology than by the federal design of water governance." Critically examine. <span style="color:#D17502">(15 marks)</span></div>'),
  W=1000, H=1500, h1=68)

# ============ FACEBOOK / LINK CARD (1200x675) ============
P['fb_a'] = page(slide(mini_top("CURRENT AFFAIRS  |  GS-1 · GS-2", logo=True) + h2("30 river links,", "one federal knot"),
  stats([("30", "NPP 1980: **16 Peninsular** + 14 Himalayan"),
         ("Rs 44,605 cr", "Ken-Betwa, cleared **8 Dec 2021**")])), W=1200, H=675)

for k, v in P.items():
    open(os.path.join(HERE, 'html', f'{k}.html'), 'w').write(v)
print('wrote', len(S) + len(P), 'html files')
