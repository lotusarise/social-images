import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from la_design import *
HERE = os.path.dirname(os.path.abspath(__file__))
D = '23 September 2026'
S = {}

S['w1'] = page(slide(f'''{top(date=D)}
<div class="tagrow"><span class="tag">ENVIRONMENT  |  GS-1 &amp; GS-3</span><span class="line"></span></div>
{headline("Rivers are drying:", "the WMO water report")}
<div class="rule"></div>
<div class="lead">The <b>State of Global Water Resources 2025</b> finds <b class="hl">2025</b> among the driest years for river flow in 35 years — and northern India among the worst-hit regions.</div>''',
 hero("droplets", ["mountain", "waves", "sprout", "trending-down"])) + f'''<div class="swipe">Swipe {icon("arrow-right", 30, "#D17502", 3)}</div>''', page_no='1/5')

S['w2'] = page(slide(mini_top("WHY IN NEWS") + h2("What the WMO", "has reported"),
  info("book-open", "The report", "The **World Meteorological Organization's** annual State of Global Water Resources, now tracking **15 hydrological variables** — up from 3 at its 2021 debut.")
  + info("triangle-alert", "The headline finding", "**2025** was among the driest years for global river discharge in **35 years**, with below-normal flows across **36%** of global basin area.", True)
  + info("mountain", "Ice is going everywhere", "A **fourth consecutive year** of net ice loss across **every** major glaciated region on earth.")), page_no='2/5')

S['w3'] = page(slide(mini_top("THE NUMBERS") + h2("What 2025", "actually looked like"),
  stats([("408 Gt", "Glacier mass lost in the 2025 hydrological year (±132) — about **1.1 mm** of sea-level rise", True),
         ("1,400 Gt", "Cumulative glacier loss, **2023 to 2025**"),
         ("36%", "Of global basin area ran **below normal**"),
         ("~2 in 3", "Monitored wells outside their **historical norm**"),
         ("34–38%", "Basins in normal range, vs a **46%** long-term average")])), page_no='3/5')

S['w4'] = page(slide(mini_top("WHAT IT MEANS FOR INDIA") + h2("The Ganges-Indus", "warning"),
  info("map", "Where the stress is", "**Northern India** and the **Ganges-Indus headwaters** ran persistently below-normal on terrestrial water storage through **2021 to 2025**.")
  + info("droplets", "Groundwater", "Northern India recorded **below-normal to much-below-normal** groundwater levels, with **over-abstraction** identified as a key driver.", True)
  + info("layers", "Why headwaters matter", "Himalayan glaciers buffer dry-season flow. As they thin, the **timing** of river supply shifts, not just the volume.")), page_no='4/5')

S['w5'] = page(slide(mini_top("PRELIMS POINTERS", logo=True) + h2("Water report:", "facts to remember"),
  flash([("WMO", "UN agency, **Geneva**; 1950, from the IMO"),
         ("The report", "**State of Global Water Resources**, annual since 2021"),
         ("Gigatonne", "**1 Gt = 1 billion tonnes** of water"),
         ("Terrestrial water storage", "Soil + groundwater + snow, ice, lakes"),
         ("Trend since 2014-16", "Persistent **global decline**"),
         ("Data gap", "**Africa and Asia** remain under-monitored")]), fill=True), page_no='5/5')

for k, v in S.items():
    open(os.path.join(HERE, 'html', f'{k}.html'), 'w').write(v)

P = {}
P['pin_w'] = page(slide(top(date=D) + '<div class="tagrow"><span class="tag">ENVIRONMENT  |  GS-1 &amp; GS-3</span><span class="line"></span></div>'
  + headline("Global water report:", "8 facts for UPSC"),
  flash([("The report", "WMO **State of Global Water Resources 2025**"),
         ("River flow", "Among the **driest** years in 35"),
         ("Basins below normal", "**36%** of global basin area"),
         ("Glacier loss 2025", "**408 Gt** (±132) = ~1.1 mm sea-level rise"),
         ("Since 2023", "**1,400 Gt** of ice gone"),
         ("Glaciated regions", "**4th** straight year of net loss, all regions"),
         ("Groundwater", "**~2 in 3** wells outside historical norm"),
         ("India", "**Ganges-Indus** headwaters below normal, 2021-25")]), fill=True), W=1000, H=1500, h1=72)

P['fb_w'] = page(slide(mini_top("CURRENT AFFAIRS  |  GS-1 & GS-3", logo=True) + h2("Rivers are drying:", "the WMO water report"),
  stats([("408 Gt", "Glacier mass lost in 2025"), ("36%", "Of basins ran below normal")])), W=1200, H=675)

for k, v in P.items():
    open(os.path.join(HERE, 'html', f'{k}.html'), 'w').write(v)
print('ok')
