import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from la_design import *
HERE = os.path.dirname(os.path.abspath(__file__))
D = '24 September 2026'
S = {}

# ============================ SET A - DELIMITATION ============================
S['a1'] = page(slide(f'''{top(date=D)}
<div class="tagrow"><span class="tag">POLITY  |  GS-2</span><span class="line"></span></div>
{headline("Delimitation and the", "federal balance")}
<div class="rule"></div>
<div class="lead">With <b>Census 2027</b> under way and the <b class="hl">Constitution (131st Amendment) Bill</b> defeated in April, how India reallocates Lok Sabha seats is wide open again.</div>''',
 hero("landmark", ["users", "map", "scale", "vote"])) + f'''<div class="swipe">Swipe {icon("arrow-right", 30, "#D17502", 3)}</div>''', page_no='1/6')

S['a2'] = page(slide(mini_top("WHY IN NEWS") + h2("Why the question is", "live again"),
  info("triangle-alert", "The April vote", "The **Constitution (131st Amendment) Bill, 2026** was negatived in Lok Sabha on **17 April 2026** — 298 for, 230 against of 528 voting.", True)
  + info("calendar", "Census 2027 is running", "Phase I houselisting ran **1 April to 30 September 2026**. Population enumeration follows in **February 2027**.")
  + info("scale", "What failed, and why", "A constitutional amendment needs **two-thirds of those present and voting** under Article 368. 298 of 528 was well short.")), page_no='2/6')

S['a3'] = page(slide(mini_top("THE CONSTITUTIONAL BASIS") + h2("What the Constitution", "actually says"),
  cards([("landmark", "Article 81", "Lok Sabha composition; present ceiling **550**"),
         ("scale", "Article 82", "Readjustment after **every census**"),
         ("building-2", "Article 170", "The same, for **State Assemblies**")])
  + info("gavel", "Article 329(a)", "A delimitation order **cannot be questioned in any court**. Parliament may accept it, but not modify it.", True)
  + info("users", "Articles 330 & 332", "**SC and ST reserved seats** are re-fixed at every delimitation exercise.")), page_no='3/6')

S['a4'] = page(slide(mini_top("THE LONG FREEZE") + h2("Why seats still follow", "the 1971 Census"),
  chain(["1971 Census", "42nd Amdt", "84th Amdt", "87th Amdt"])
  + stats([("1971", "The census that still fixes each state's **share** of Lok Sabha seats", True),
           ("42nd, 1976", "Froze inter-state allocation until after **2000**"),
           ("84th, 2001", "Freeze extended to the **first census after 2026**"),
           ("87th, 2003", "Within-state redrawing moved to the **2001 census**"),
           ("543 / 550", "Elected members against the **Article 81 ceiling**")])), page_no='4/6')

S['a5'] = page(slide(mini_top("THE TWO ARGUMENTS") + h2("Democratic equality vs", "federal equity"),
  info("users", "The representation case", "An MP in Uttar Pradesh or Bihar speaks for roughly **2.5 to 3 million** people; one in Tamil Nadu or Kerala for about **1.5 to 1.8 million**.")
  + info("shield", "The federal case", "States that brought fertility down early fear losing weight in Parliament for doing what national policy asked of them.", True)
  + stats([("~44 seats", "Roughly **8% of the House** is mis-allocated on one widely cited estimate", True)])), page_no='5/6')

S['a6'] = page(slide(mini_top("WAY FORWARD", logo=True) + h2("What could break", "the deadlock"),
  bullets_box("lightbulb", "Options on the table", [
      "**Expand the House** with a floor, so no state loses seats",
      "**Degressive proportionality**, as in the EU Parliament",
      "Make the **Rajya Sabha** a real federal chamber"], True)
  + info("users-round", "Linked issue", "The **106th Amendment, 2023** ties women's reservation to the delimitation that follows the census.")
  + '<div class="mq">Q. Can India reconcile democratic equality with federal equity in delimitation? Discuss. <span style="color:#D17502">(15 marks)</span></div>'
  + '<div class="chips"><span class="chip">GS-2 Polity</span><span class="chip">PSIR Optional</span><span class="chip">Prelims</span></div>'), page_no='6/6')

# ============================== SET B - MCQ ==================================
S['b1'] = page(slide(f'''{top(kicker_a='PRELIMS', kicker_b='PRACTICE', date=D)}
<div class="tagrow"><span class="tag">POLITY  |  GS-2</span><span class="line"></span></div>
{headline("Statement-based MCQ:", "Delimitation")}
<div class="rule"></div>
<div class="lead">Four statements. Two traps. One of them turns on a bill that <b class="hl">did not pass</b> this April — exactly the kind of detail UPSC likes.</div>''',
 hero("vote", ["landmark", "scale", "gavel", "users"])) + f'''<div class="swipe">Swipe {icon("arrow-right", 30, "#D17502", 3)}</div>''', page_no='1/4')

Q = ["Under Article 82, the allocation of Lok Sabha seats among the States is to be readjusted upon the completion of each census.",
     "The 84th Amendment extended the freeze on inter-State allocation of seats until the first census taken after 2026.",
     "An order of the Delimitation Commission may be challenged in a High Court but not in the Supreme Court.",
     "The maximum strength of the Lok Sabha under Article 81 was raised from 550 to 850 in 2026."]
S['b2'] = page(slide(mini_top("CONSIDER THE FOLLOWING STATEMENTS", logo=True) + h2("Delimitation in", "India"),
  mcq_q(Q, "How many of the above statements are correct?", ["Only one", "Only two", "Only three", "All four"])),
  cta='Answer on the next slide')

S['b3'] = page(slide(mini_top("ANSWER & EXPLANATION", logo=True)
  + '<div class="ans"><div class="a">(B)</div><div class="t">Only two are correct:<br>statements 1 and 2</div></div>',
  verdicts([(True, "1. Correct", "Article 82: on completion of **each census**, seats are readjusted by an authority Parliament lays down in a **Delimitation Act**."),
            (True, "2. Correct", "The **84th Amendment, 2001** pushed the freeze to the **first census after 2026**, keeping the 1971 shares."),
            (False, "3. Incorrect", "**Article 329(a)** bars **any court** from questioning a delimitation order — High Court and Supreme Court alike."),
            (False, "4. Incorrect", "The **131st Amendment Bill** proposed 850, but it was **negatived on 17 April 2026**. The ceiling is still **550**.")])), page_no='3/4')

S['b4'] = page(slide(mini_top("PRELIMS POINTERS", logo=True) + h2("Delimitation:", "facts to remember"),
  flash([("Article 82", "Readjustment after each census"),
         ("Article 329(a)", "Orders are beyond judicial review"),
         ("Four commissions", "Under the Acts of **1952, 1962, 1972, 2002**"),
         ("Plus 2020", "A separate commission for **J&K**"),
         ("Composition", "Retired SC judge (Chair), **CEC**, State EC"),
         ("106th Amdt, 2023", "Women's quota follows delimitation")]), fill=True), page_no='4/4')

# ========================= SET C - AGASTHYAMALA ==============================
S['c1'] = page(slide(f'''{top(date=D)}
<div class="tagrow"><span class="tag">ENVIRONMENT  |  GS-3</span><span class="line"></span></div>
{headline("3,261 flowering plants:", "inside Agasthyamala")}
<div class="rule"></div>
<div class="lead">A new <b>JNTBGRI</b> checklist maps the flora of the Agasthyamala Biosphere Reserve — <b class="hl">31.2%</b> of its taxa grow nowhere outside India.</div>''',
 hero("flower-2", ["mountain", "trees", "bird", "leaf"])) + f'''<div class="swipe">Swipe {icon("arrow-right", 30, "#D17502", 3)}</div>''', page_no='1/5')

S['c2'] = page(slide(mini_top("WHERE IT IS") + h2("A reserve across", "two states"),
  info("map", "Location", "Southern **Western Ghats**, spanning **Kerala** (Thiruvananthapuram, Kollam, Pathanamthitta) and **Tamil Nadu** (Tirunelveli, Kanniyakumari).")
  + stats([("3,500 sq km", "Total area of the biosphere reserve", True),
           ("1,868 m", "Agasthyarkoodam, the highest peak"),
           ("2016", "Joined UNESCO's **World Network**")])
  + info("trees", "What it contains", "Four protected areas: **Neyyar**, **Peppara** and **Shendurney** sanctuaries, and the **Kalakad-Mundanthurai Tiger Reserve**.", True)), page_no='2/5')

S['c3'] = page(slide(mini_top("THE NEW CHECKLIST") + h2("What the survey", "recorded"),
  stats([("3,261", "Flowering plant species, plus **26 subspecies** and **28 varieties**", True),
         ("31.2%", "Of the taxa are **endemic to India**"),
         ("245", "**Steno-endemic** species, found only here"),
         ("347", "Taxa **shared with Sri Lanka**"),
         ("337", "Bird species recorded in the reserve")])
  + info("sprout", "Why botanists care", "The reserve holds **wild progenitors** of pepper, cardamom and nutmeg — a living gene bank for India's spice crops.")), page_no='3/5')

S['c4'] = page(slide(mini_top("THE HUMAN STORY") + h2("The Kani model:", "biodiversity that pays"),
  info("users", "The Kani people", "Around **30,000** Kani (Kanikkar) live in and around the reserve, among the oldest forest-dwelling communities of the southern Ghats.")
  + info("leaf", "Arogyapacha", "Kani knowledge of **Trichopus zeylanicus** led to the anti-fatigue drug **Jeevani**, licensed in 1995 for a fee plus a **2% royalty**.", True)
  + info("handshake", "Why UPSC cares", "TBGRI shared **50%** of fee and royalty with the community — India's textbook **Access and Benefit-Sharing** case.")), page_no='4/5')

S['c5'] = page(slide(mini_top("PRELIMS POINTERS", logo=True) + h2("Agasthyamala:", "facts to remember"),
  flash([("Biosphere reserve", "National **2001**; UNESCO **2016**"),
         ("Western Ghats", "One of India's **4 biodiversity hotspots**"),
         ("Agasthyarkoodam", "**1,868 m**, highest peak of the reserve"),
         ("Kalakad-Mundanthurai", "Tamil Nadu's **first** tiger reserve"),
         ("Arogyapacha", "**Trichopus zeylanicus**; drug Jeevani"),
         ("ABS law", "**Biological Diversity Act, 2002**; Nagoya Protocol")]), fill=True), page_no='5/5')

for k, v in S.items():
    open(os.path.join(HERE, 'html', f'{k}.html'), 'w').write(v)

# ============================ PINTEREST PINS =================================
P = {}
P['pin_a'] = page(slide(top(date=D) + '<div class="tagrow"><span class="tag">PRELIMS + MAINS  |  GS-2</span><span class="line"></span></div>'
  + headline("Delimitation in India:", "8 facts for UPSC"),
  flash([("Article 82", "Readjust seats after **each census**"),
         ("Article 329(a)", "Orders beyond **judicial review**"),
         ("42nd Amdt, 1976", "Froze inter-state shares on **1971**"),
         ("84th Amdt, 2001", "Freeze till **first census after 2026**"),
         ("87th Amdt, 2003", "Within-state redraw on **2001 census**"),
         ("Article 81", "Ceiling **550**; 543 elected today"),
         ("131st Amdt Bill", "Proposed 850 - **negatived** 17 Apr 2026"),
         ("106th Amdt, 2023", "Women's quota **after** delimitation")]), fill=True), W=1000, H=1500, h1=72)

Q_PIN = ["Article 82 requires readjustment of Lok Sabha seats among States after each census.",
         "The 84th Amendment extended the seat freeze to the first census after 2026.",
         "A Delimitation Commission order can be challenged in a High Court.",
         "The Article 81 ceiling on Lok Sabha strength was raised to 850 in 2026."]
P['pin_b'] = page(slide(top(kicker_a='PRELIMS', kicker_b='PRACTICE', date=D)
  + headline("Delimitation MCQ:", "can you get it?"),
  mcq_q(Q_PIN, "How many of the above are correct?", ["Only one", "Only two", "Only three", "All four"])), W=1000, H=1500, h1=68)

P['pin_c'] = page(slide(top(date=D) + '<div class="tagrow"><span class="tag">ENVIRONMENT  |  GS-3</span><span class="line"></span></div>'
  + headline("Agasthyamala Reserve:", "8 facts for UPSC"),
  flash([("Where", "Kerala + Tamil Nadu, **southern Western Ghats**"),
         ("Area", "About **3,500 sq km**"),
         ("UNESCO", "World Network of Biosphere Reserves, **2016**"),
         ("Peak", "**Agasthyarkoodam**, 1,868 m"),
         ("New checklist", "**3,261** flowering plant species"),
         ("Endemism", "**31.2%** Indian endemics; 245 steno-endemic"),
         ("People", "About **30,000 Kani** live in and around it"),
         ("Case study", "**Jeevani** - India's ABS benchmark")]), fill=True), W=1000, H=1500, h1=72)

# ========================== FACEBOOK CARDS 1200x675 ==========================
P['fb_a'] = page(slide(mini_top("CURRENT AFFAIRS  |  GS-2", logo=True) + h2("Delimitation and", "the federal balance"),
  stats([("17 Apr 2026", "131st Amendment Bill negatived"), ("1971", "Census that still fixes state shares")])), W=1200, H=675)

P['fb_b'] = page(slide(mini_top("PRELIMS PRACTICE  |  GS-2", logo=True) + h2("Delimitation:", "4 statements, 2 traps"),
  stats([("Article 82", "Readjustment after each census"), ("Article 329(a)", "Beyond judicial review")])), W=1200, H=675)

P['fb_c'] = page(slide(mini_top("CURRENT AFFAIRS  |  GS-3", logo=True) + h2("Agasthyamala:", "3,261 flowering plants"),
  stats([("31.2%", "Taxa endemic to India"), ("3,500 sq km", "Across Kerala and Tamil Nadu")])), W=1200, H=675)

for k, v in P.items():
    open(os.path.join(HERE, 'html', f'{k}.html'), 'w').write(v)
print('wrote', len(S) + len(P), 'html files')
