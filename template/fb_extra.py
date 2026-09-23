import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from la_design import *
HERE = os.path.dirname(os.path.abspath(__file__))
P = {}
P['fb_d'] = page(slide(mini_top("PRELIMS PRACTICE  |  GS-2", logo=True) + h2("Article 368:", "how an amendment fails"),
  stats([("Two-thirds", "Of members present and voting"), ("298 / 528", "The 131st Amendment Bill, 17 Apr 2026")])), W=1200, H=675)
for k, v in P.items():
    open(os.path.join(HERE, 'html', f'{k}.html'), 'w').write(v)
print('ok')
