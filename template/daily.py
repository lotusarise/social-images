import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from la_design import *
D = '25 September 2026'
HTML = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'html')
S = {}

# ============ POST 1 : CURRENT AFFAIRS CAROUSEL (a1-a6) ============
S['a1'] = page(slide(f'''{top(date=D)}
<div class="tagrow"><span class="tag">INTERNATIONAL RELATIONS  |  GS-2</span><span class="line"></span></div>
{headline("A new security order", "for the Arctic")}
<div class="rule"></div>
<div class="lead">On <b>22 September 2026</b> the <b>US, Denmark and Greenland</b> signed a pact rewriting the <b class="hl">1951 Defense of Greenland Agreement</b>.</div>''',
  hero("snowflake", ["ship", "plane", "radar", "shield"])) +
  f'''<div class="swipe">Swipe {icon("arrow-right", 30, "#D17502", 3)}</div>''', page_no='1/6')

S['a2'] = page(slide(mini_top("WHY IN NEWS") + h2("What exactly", "was signed"),
  info("signature", "The signing", "Done at **New York** on 22 September 2026, on the sidelines of the **81st UN General Assembly**.")
  + info("file-text", "What it amends", "The **Agreement of 27 April 1951** on the defense of Greenland, as amended by the ==2004 Igaliku Agreement==.")
  + info("landmark", "Not yet in force", "It takes effect only after **parliamentary procedures** in Denmark and Greenland are completed.", True)), page_no='2/6')

S['a3'] = page(slide(mini_top("THE CORE PROVISIONS") + h2("What the agreement", "actually allows"),
  cards([("radar", "Pituffik", "Modernise and expand the only active US base"),
         ("map-pin", "Narsarsuaq", "New defence area in the south"),
         ("anchor", "Mestersvig", "New defence area on the east coast")])
  + bullets_box("plane", "Access rights", ["US aircraft may **fly over and land in any territory**, including territorial waters",
                                            "US public vessels gain **undersea access**"], True)), page_no='3/6')

S['a4'] = page(slide(mini_top("THE STRATEGIC LOCK") + h2("The clauses that", "matter most"),
  info("ban", "No non-NATO forces", "**No non-NATO state** may build military installations or keep a persistent military presence.", True)
  + info("lock", "Investment screening", "Non-NATO, non-EU investors barred from control over ==critical infrastructure and resource extraction==.")
  + info("flag", "If Greenland goes independent", "It must **remain in NATO** and assume every obligation. The pact has **no end date**.")), page_no='4/6')

S['a5'] = page(slide(mini_top("WHY GREENLAND") + h2("Why this island,", "and why now"),
  stats([("2,166,086 km²", "World's **largest island**; about ==80%== under ice", True),
         ("~56,500", "Population; capital **Nuuk**"),
         ("GIUK gap", "Greenland–Iceland–UK **submarine chokepoint**"),
         ("Pituffik", "US **missile early-warning** and space surveillance"),
         ("Article 21", "Self-Government Act **no. 473 of 2009** sets the independence route")])), page_no='5/6')

S['a6'] = page(slide(mini_top("PRELIMS POINTERS", logo=True) + h2("Facts to", "remember"),
  flash([("Arctic Council", "**Ottawa Declaration, 19 Sept 1996**; a forum, not a treaty body"),
         ("8 members", "Canada, Denmark, Finland, Iceland, Norway, Russia, Sweden, USA"),
         ("Military security", "**Expressly outside** the Council's mandate"),
         ("India", "**Observer since 2013**, Kiruna Ministerial"),
         ("Svalbard Treaty", "Paris, **9 February 1920**; India an original signatory"),
         ("Himadri", "India's Arctic station, **Ny-Ålesund, 1 July 2008**")]), fill=True), page_no='6/6')

# ============ POST 2 : PRELIMS MCQ (b1-b2) ============
Q = ["The Arctic Council was established by the Ottawa Declaration of 1996 and its mandate excludes military security.",
     "India has been an Observer in the Arctic Council since 2013.",
     "India became a party to the Svalbard Treaty only after releasing its Arctic Policy in 2022.",
     "Under the 2026 US–Denmark–Greenland agreement, an independent Greenland must remain in NATO."]
S['b1'] = page(slide(mini_top("PRELIMS PRACTICE  |  GS-2", logo=True) + h2("The Arctic", "& India"),
  mcq_q(Q, "How many of the above statements are correct?", ["Only one", "Only two", "Only three", "All four"])),
  cta='Share your answer in comments')

S['b2'] = page(slide(mini_top("ANSWER & EXPLANATION", logo=True) +
  '<div class="ans"><div class="a">(C)</div><div class="t">Only three are correct:<br>statements 1, 2 and 4</div></div>',
  verdicts([(True, "1. Correct", "Signed **19 September 1996**. The Council is a forum, and military security sits **outside** its mandate."),
            (True, "2. Correct", "India became an Observer at the **Kiruna Ministerial, 2013**."),
            (False, "3. Incorrect", "India signed the Svalbard Treaty in **1920** — a century before the 2022 Arctic Policy."),
            (True, "4. Correct", "The agreement requires an independent Greenland to **stay in NATO** and assume all obligations.")])), page_no='2/2')

# ============ POST 3 : MAINS ANGLE (c1-c5) ============
S['c1'] = page(slide(f'''{top(kicker_a='MAINS', kicker_b='ANGLE', date=D)}
<div class="tagrow"><span class="tag">GS-2  |  INTERNATIONAL RELATIONS</span><span class="line"></span></div>
{headline("India and the", "militarised Arctic")}
<div class="rule"></div>
<div class="lead">The Arctic's reputation as a zone of <b>exceptional cooperation</b> is thinning. India's stake there is <b class="hl">older than most people assume</b>.</div>''',
  hero("globe", ["microscope", "ship", "thermometer", "scale"])) +
  f'''<div class="swipe">Swipe {icon("arrow-right", 30, "#D17502", 3)}</div>''', page_no='1/5')

S['c2'] = page(slide(mini_top("THE FOOTPRINT") + h2("India in the Arctic,", "by the dates"),
  stats([("1920", "India signed the **Svalbard Treaty** at Paris", True),
         ("2013", "**Observer**, Arctic Council"),
         ("1 July 2008", "**Himadri** station, Ny-Ålesund"),
         ("17 Mar 2022", "India's **Arctic Policy**, six pillars"),
         ("NCPOR, Goa", "Nodal body, **Ministry of Earth Sciences**")])), page_no='2/5')

S['c3'] = page(slide(mini_top("WHY IT MATTERS") + h2("Why a tropical country", "watches the Arctic"),
  info("thermometer", "Climate", "Arctic warming is tied to shifts in the **monsoon** and the Himalaya — the ==Third Pole== link.")
  + info("ship", "Connectivity", "Shorter northern shipping routes and the **Chennai–Vladivostok** Eastern Maritime Corridor.")
  + info("lock", "Securitisation", "The 2026 pact screens **non-NATO, non-EU investment** out of resources and infrastructure.", True)), page_no='3/5')

S['c4'] = page(slide(mini_top("CHALLENGES & WAY FORWARD") + h2("The balance", "India must strike"),
  bullets_box("triangle-alert", "Challenges", ["Observers have **no vote** in the Arctic Council",
                                                "Arctic security is being settled **outside** the Council",
                                                "Russia ties versus Western partnerships"])
  + bullets_box("lightbulb", "Way forward", ["Deepen **science diplomacy** through Himadri and NCPOR",
                                              "Build **polar research capacity**",
                                              "Press for a stronger voice for **Observers**"], True)), page_no='4/5')

S['c5'] = page(slide(mini_top("MAINS PRACTICE", logo=True) + h2("Answer", "this"),
  '<div class="mq">Q. "The Arctic is no longer a zone of exceptional cooperation." Examine the implications of Arctic militarisation for India\'s scientific, economic and strategic interests. <span style="color:#D17502">(15 marks)</span></div>'
  + bullets_box("scale", "Structure it like this", ["Intro: **Arctic exceptionalism** and why it is fading",
                                                     "Body 1: India's **legal and scientific** stake",
                                                     "Body 2: **Economic** stake — routes, minerals",
                                                     "Body 3: The **strategic** squeeze on non-Arctic states",
                                                     "Conclusion: science diplomacy + **multi-alignment**"], True)
  + '<div class="chips"><span class="chip">GS-2 IR</span><span class="chip">GS-1 Geography</span><span class="chip">PSIR Optional</span></div>'), page_no='5/5')

for k, v in S.items():
    open(os.path.join(HTML, f'{k}.html'), 'w').write(v)

# ============ PINTEREST PINS (1000x1500) ============
P = {}
P['pin_a'] = page(slide(top(date=D) + '<div class="tagrow"><span class="tag">PRELIMS + MAINS  |  GS-2</span><span class="line"></span></div>'
  + headline("The Arctic pact:", "8 facts for UPSC"),
  flash([("22 Sept 2026", "US–Denmark–Greenland pact signed"),
         ("Amends", "1951 Defense of Greenland Agreement"),
         ("Pituffik", "Modernised and expanded"),
         ("Two new areas", "Narsarsuaq and Mestersvig"),
         ("Non-NATO forces", "Bases and persistent presence barred"),
         ("If independent", "Greenland stays in NATO"),
         ("Arctic Council", "Ottawa Declaration, 1996"),
         ("India", "Observer 2013; Svalbard 1920")]), fill=True), W=1000, H=1500, h1=72)

P['pin_b'] = page(slide(top(date=D) + '<div class="tagrow"><span class="tag">PRELIMS PRACTICE  |  GS-2</span><span class="line"></span></div>'
  + headline("Arctic & India:", "MCQ pointers"),
  flash([("Arctic Council", "A forum, not a treaty-based organisation"),
         ("Founded", "Ottawa Declaration, 19 September 1996"),
         ("Members", "8 Arctic states; 6 Permanent Participants"),
         ("Mandate", "Military security expressly excluded"),
         ("India", "Observer since the Kiruna Ministerial, 2013"),
         ("Svalbard Treaty", "Paris, 9 February 1920"),
         ("Himadri", "Ny-Ålesund, inaugurated 1 July 2008"),
         ("Arctic Policy", "Released 17 March 2022")]), fill=True), W=1000, H=1500, h1=72)

P['pin_c'] = page(slide(top(kicker_a='MAINS', kicker_b='ANGLE', date=D) + '<div class="tagrow"><span class="tag">GS-2  |  IR</span><span class="line"></span></div>'
  + headline("India in the Arctic:", "the Mains angle"),
  flash([("1920", "Svalbard Treaty signed at Paris"),
         ("2008", "Himadri station, Ny-Ålesund"),
         ("2013", "Arctic Council Observer"),
         ("2022", "India's Arctic Policy, six pillars"),
         ("NCPOR, Goa", "Nodal body under Ministry of Earth Sciences"),
         ("Climate", "Arctic warming and the monsoon"),
         ("Routes", "Chennai–Vladivostok corridor"),
         ("The squeeze", "Security settled outside the Arctic Council")]), fill=True), W=1000, H=1500, h1=72)

# ============ FACEBOOK / LINK CARDS (1200x675) ============
P['fb_a'] = page(slide(mini_top("CURRENT AFFAIRS  |  GS-2", logo=True) + h2("A new security order", "for the Arctic"),
  stats([("22 Sept 2026", "US–Denmark–Greenland pact signed"), ("1951", "The agreement it amends")])), W=1200, H=675)

P['fb_b'] = page(slide(mini_top("PRELIMS PRACTICE  |  GS-2", logo=True) + h2("The Arctic", "& India"),
  stats([("1996", "Arctic Council, Ottawa Declaration"), ("1920", "India signed the Svalbard Treaty")])), W=1200, H=675)

P['fb_c'] = page(slide(mini_top("MAINS ANGLE  |  GS-2", logo=True) + h2("India and the", "militarised Arctic")
  , stats([("2013", "Arctic Council Observer"), ("2022", "India's Arctic Policy")])), W=1200, H=675)

for k, v in P.items():
    open(os.path.join(HTML, f'{k}.html'), 'w').write(v)
print('built', len(S) + len(P), 'slides')
