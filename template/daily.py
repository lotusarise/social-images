import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from la_design import *
R = os.path.dirname(os.path.abspath(__file__))
D = '26 September 2026'
S = {}

# ---------------- POST 1: current affairs carousel (7 slides) ----------------
S['eci_a1'] = page(slide(f'''{top(date=D)}
<div class="tagrow"><span class="tag">POLITY  |  GS-2</span><span class="line"></span></div>
{headline("Who can remove a", "Chief Election Commissioner?")}
<div class="rule"></div>
<div class="lead">On <b>23 September 2026</b> a two-judge Supreme Court Bench split <b class="hl">1:1</b> on sending the challenge to the <b>CEC Act, 2023</b> to a larger Bench. The matter now sits with the Chief Justice of India.</div>''',
  hero("landmark", ["scale", "users", "gavel", "vote"])) + f'''<div class="swipe">Swipe {icon("arrow-right", 30, "#D17502", 3)}</div>''', page_no='1/7')

S['eci_a2'] = page(slide(mini_top("WHY IN NEWS") + h2("Two pressures on", "one institution"),
  info("gavel", "In the Supreme Court", "On **23 September 2026**, Justices **Dipankar Datta** and **Satish Chandra Sharma** split ==1:1== on referring the challenge to the 2023 Act to a larger Bench.", True)
  + info("users", "Inside the Commission", "Reports that the two Election Commissioners recorded objections on several decisions. The ECI has said the final decisions were ==unanimous==.")), page_no='2/7')

S['eci_a3'] = page(slide(mini_top("THE CONSTITUTIONAL BASE") + h2("Article 324:", "what it actually says"),
  info("landmark", "324(1)", "Superintendence, direction and control of elections to **Parliament**, **State Legislatures** and the offices of ==President and Vice-President==.")
  + info("users", "324(2)", "A **CEC**, plus as many other ECs as the President may fix. Appointment is ==subject to any law made by Parliament==.", True)
  + info("shield", "324(5)", "The CEC's conditions of service ==cannot be varied to his disadvantage== after appointment.")), page_no='3/7')

S['eci_a4'] = page(slide(mini_top("THE KEY ASYMMETRY") + h2("One Commission,", "two levels of protection"),
  cards([("shield", "The CEC", "Removable only in the manner of a **Supreme Court judge**"),
         ("user", "The two ECs", "Removable on the ==CEC's recommendation=="),
         ("scale", "The effect", "Two of the three members hold the **weaker** tenure")])
  + info("triangle-alert", "Why this matters", "The Commission decides by **majority**. The two members who can outvote the CEC are the two with the ==thinner protection==.", True)), page_no='4/7')

S['eci_a5'] = page(slide(mini_top("THE REMOVAL ROUTE") + h2("Removing a CEC:", "five steps"),
  chain(["Notice", "Speaker admits", "Inquiry panel", "Both Houses", "President"])
  + bullets_box("gavel", "The detail", [
      "Grounds under **Article 124(4)**: ==proved misbehaviour or incapacity==",
      "Notice signed by **100 Lok Sabha** or **50 Rajya Sabha** members",
      "Three-member panel under the **Judges (Inquiry) Act, 1968**",
      "Special majority in ==both Houses, in the same session=="])), page_no='5/7')

S['eci_a6'] = page(slide(mini_top("WHO PICKS THEM") + h2("The 2023 Act", "changed the panel"),
  info("scale", "Anoop Baranwal (2023)", "A **five-judge Bench** set an interim panel: the PM, the **Leader of Opposition** in the Lok Sabha, and the ==Chief Justice of India==.")
  + info("landmark", "The 2023 Act", "Parliament replaced the CJI with a **Union Cabinet Minister** nominated by the PM. The CJI is ==no longer on the panel==.", True)
  + info("search", "The shortlist", "A **Search Committee** under the ==Cabinet Secretary== proposes a panel of five names.")), page_no='6/7')

S['eci_a7'] = page(slide(mini_top("PRELIMS POINTERS", logo=True) + h2("Facts to", "remember"),
  flash([("Article 324(1)", "ECI also conducts **President & Vice-President** elections"),
         ("Article 324(5)", "CEC removed like an **SC judge**; ECs on the CEC's recommendation"),
         ("Article 124(4)", "Ground: **proved misbehaviour or incapacity**"),
         ("Judges (Inquiry) Act, 1968", "SC judge + HC Chief Justice + **distinguished jurist**"),
         ("Term of office", "**Six years** or age **65**, whichever is earlier"),
         ("Never once used", "**No CEC** has been removed in independent India")]), fill=True), page_no='7/7')

# ---------------- POST 2: Prelims MCQ (2 slides) ----------------
Q = ["The Chief Election Commissioner is removed only on the recommendation of the Election Commission.",
     "The CEC's conditions of service cannot be varied to his disadvantage after appointment.",
     "The 2023 Act on appointments places the Chief Justice of India on the Selection Committee.",
     "The Commission conducts elections to the offices of President and Vice-President."]
S['eci_b1'] = page(slide(mini_top("PRELIMS PRACTICE  |  POLITY", logo=True) + h2("The Election", "Commission of India"),
  mcq_q(Q, "How many of the above are correct?", ["Only one", "Only two", "Only three", "All four"])),
  cta='Share your answer in comments')

S['eci_b2'] = page(slide(mini_top("ANSWER & EXPLANATION", logo=True) + '<div class="ans"><div class="a">(B)</div><div class="t">Only two statements are correct:<br>statements 2 and 4</div></div>',
  verdicts([(False, "1. Incorrect", "That is the rule for the **other ECs**. The CEC goes the ==Supreme Court judge== route — an address by both Houses."),
            (True, "2. Correct", "The proviso to **Article 324(5)** protects the CEC's service conditions after appointment."),
            (False, "3. Incorrect", "The panel is the PM, a **Union Cabinet Minister** and the LoP. The CJI sat only on the ==Anoop Baranwal== interim panel."),
            (True, "4. Correct", "**Article 324(1)** covers Parliament, State Legislatures and the ==President and Vice-President== elections.")])), page_no='2/2')

# ---------------- POST 3: Mains angle (4 slides) ----------------
S['eci_c1'] = page(slide(f'''{top(kicker_a='MAINS', kicker_b='ANGLE', date=D)}
<div class="tagrow"><span class="tag">GS-2  |  CONSTITUTIONAL BODIES</span><span class="line"></span></div>
{headline("Insulating the", "Election Commission")}
<div class="rule"></div>
<div class="lead">Independence is not one guarantee but four: <b>how members are chosen</b>, <b>how they can be removed</b>, <b>who pays</b>, and <b class="hl">who staffs them</b>. The ECI is strong on one and thin on the rest.</div>''',
  hero("scale", ["landmark", "banknote", "users", "lock"])) + f'''<div class="swipe">Swipe {icon("arrow-right", 30, "#D17502", 3)}</div>''', page_no='1/4')

S['eci_c2'] = page(slide(mini_top("WHERE THE GAPS ARE") + h2("Four tests of", "institutional autonomy"),
  cards([("users", "Appointment", "The executive holds **two of three** seats on the panel"),
         ("shield", "Tenure", "Only the CEC has ==Article 324(5)== protection"),
         ("banknote", "Finance", "ECI spending is **voted**, not charged")])
  + info("lock", "Staffing", "The ECI has **no independent secretariat** with its own cadre; officers are ==drawn from the executive==.", True)), page_no='2/4')

S['eci_c3'] = page(slide(mini_top("WHAT HAS BEEN PROPOSED") + h2("Reform ideas", "on the record"),
  bullets_box("clipboard-list", "Long-standing recommendations", [
      "**Dinesh Goswami Committee, 1990** — a balanced selection mechanism",
      "**Law Commission, 255th Report (2015)** — consensus-based appointment",
      "Extend ==Article 324(5)== removal protection to **all three** members"], True)
  + info("banknote", "Make it charged", "Put ECI expenditure on the **Consolidated Fund** as ==charged==, as for the Supreme Court, CAG and UPSC.")), page_no='3/4')

S['eci_c4'] = page(slide(mini_top("THE MAINS QUESTION", logo=True) + h2("How to", "write it"),
  bullets_box("lightbulb", "A workable structure", [
      "Define independence through **appointment, tenure, finance, staffing**",
      "Use **Article 324** and ==Anoop Baranwal (2023)== as the spine",
      "Contrast the **CEC** and the **two ECs** on removal",
      "Close on the ==Article 98 / 146== secretariat model"])
  + '<div class="mq">Q. "The Election Commission\'s independence rests on one protected office, not on a protected institution." Critically examine. <span style="color:#D17502">(15 marks)</span></div>'
  + '<div class="chips"><span class="chip">GS-2 Polity</span><span class="chip">PSIR Optional</span><span class="chip">Essay</span></div>'), page_no='4/4')

for k, v in S.items():
    open(os.path.join(R, 'html', f'{k}.html'), 'w').write(v)

# ---------------- Pinterest pin (1000x1500) ----------------
P = {}
P['eci_pin'] = page(slide(top(date=D) + '<div class="tagrow"><span class="tag">PRELIMS + MAINS  |  GS-2</span><span class="line"></span></div>'
  + headline("Election Commission:", "6 facts for UPSC"),
  flash([("Article 324(1)", "Also runs President & Vice-President elections"),
         ("Article 324(5)", "CEC removed like a Supreme Court judge"),
         ("The two ECs", "Removed on the CEC's recommendation"),
         ("Article 124(4)", "Proved misbehaviour or incapacity"),
         ("Judges (Inquiry) Act, 1968", "SC judge + HC Chief Justice + jurist"),
         ("Selection panel (2023)", "PM + Cabinet Minister + LoP")]), fill=True), W=1000, H=1500, h1=58)

# ---------------- Facebook / landscape card (1200x675) ----------------
P['eci_card'] = page(slide(mini_top("CURRENT AFFAIRS  |  GS-2", logo=True) + h2("Removing a", "Chief Election Commissioner"),
  stats([("324(5)", "The CEC goes only by the **Supreme Court judge** route"),
         ("1:1", "Supreme Court split on **23 September 2026**")])), W=1200, H=675)

for k, v in P.items():
    open(os.path.join(R, 'html', f'{k}.html'), 'w').write(v)
print('wrote', len(S) + len(P), 'slides')
