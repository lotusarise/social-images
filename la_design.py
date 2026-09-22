"""LotusArise social-card design system (HTML/CSS -> PNG via headless Chromium).
Original layout language: bold two-tone headline, topic tag, date badge, icon cards,
info boxes, lettered MCQ option bars, answer-verdict rows. Brand: blue #015289, orange #D17502.
"""
import os, re, html, base64

ROOT = os.path.dirname(os.path.abspath(__file__))
NM = os.path.join(ROOT, 'node_modules')
ICON_DIR = os.path.join(NM, 'lucide-static', 'icons')
LOGO = os.path.join(ROOT, 'assets', 'logo.png')

BLUE = '#015289'; NAVY = '#0A2A4A'; ORANGE = '#D17502'; GOLD = '#F2A33A'
PAPER = '#FAF6EF'; SKY = '#EAF3FA'; INK = '#1B2430'; MUTED = '#4A5563'

def font_face():
    """Use fontsource CSS (has unicode-range per subset) with absolute file URLs."""
    out = []
    for pkg, weights in [('poppins', [400, 500, 600, 700, 800, 900]), ('inter', [400, 500, 600, 700, 800])]:
        for w in weights:
            css = open(os.path.join(NM, '@fontsource', pkg, f'{w}.css')).read()
            css = css.replace('url(./files/', 'url(file://' + os.path.join(NM, '@fontsource', pkg, 'files') + '/')
            out.append(css)
    return '\n'.join(out)

def icon(name, size=56, color='currentColor', stroke=2):
    svg = open(os.path.join(ICON_DIR, name + '.svg')).read()
    svg = re.sub(r'<!--.*?-->', '', svg, flags=re.S)
    svg = re.sub(r'(?<![-\w])width="\d+"', f'width="{size}"', svg, count=1)
    svg = re.sub(r'(?<![-\w])height="\d+"', f'height="{size}"', svg, count=1)
    svg = svg.replace('stroke="currentColor"', f'stroke="{color}"').replace('stroke-width="2"', f'stroke-width="{stroke}"')
    return svg

def logo_img(width):
    b = base64.b64encode(open(LOGO, 'rb').read()).decode()
    return f'<img src="data:image/png;base64,{b}" style="width:{width}px;height:auto;display:block">'

def rich(t):
    """**bold** -> navy bold ; ==hl== -> orange bold"""
    t = html.escape(t).replace('&#x27;', '’')
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'==(.+?)==', r'<b class="hl">\1</b>', t)
    return t

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:%(W)dpx;height:%(H)dpx}
body{font-family:'Poppins','Inter',sans-serif;color:%(INK)s;background:%(PAPER)s;position:relative;overflow:hidden}
b{font-weight:700;color:%(NAVY)s} b.hl{color:%(ORANGE)s}
.bg-dots{position:absolute;right:-40px;top:-40px;width:420px;height:420px;
  background-image:radial-gradient(%(BLUE)s22 2.2px,transparent 2.4px);background-size:22px 22px;
  -webkit-mask-image:radial-gradient(circle at 70%% 30%%,#000 30%%,transparent 70%%)}
.bg-dots.bl{left:-60px;right:auto;top:auto;bottom:40px;width:360px;height:360px;
  background-image:radial-gradient(%(ORANGE)s26 2.2px,transparent 2.4px)}
.swoosh{position:absolute;left:0;right:0;bottom:0;height:128px;background:%(NAVY)s;
  clip-path:polygon(0 22%%,100%% 0,100%% 100%%,0 100%%)}
.swoosh:before{content:'';position:absolute;left:0;right:0;top:0;height:14px;background:%(ORANGE)s;
  clip-path:polygon(0 100%%,100%% 0,100%% 100%%,0 100%%)}
.frame{position:absolute;inset:26px;border:2px solid %(BLUE)s33;border-radius:6px;pointer-events:none}
.frame:before,.frame:after{content:'';position:absolute;width:14px;height:14px;border-radius:50%%;background:%(ORANGE)s}
.frame:before{left:-8px;top:-8px}.frame:after{right:-8px;bottom:-8px}
.wrap{position:absolute;inset:58px 62px 160px 62px;display:flex;flex-direction:column}
.hd{display:flex;flex-direction:column}
.hd .top{margin-bottom:26px}
.bd{flex:1;display:flex;flex-direction:column;justify-content:center;gap:22px;margin-top:22px}
.bd > .banner{margin:0;align-self:flex-start}
.bd > .info{margin-top:0}
.bd > .chain{margin-top:-6px}
.bd.fill{justify-content:stretch}
.bd.fill > .flash{flex:1;grid-auto-rows:1fr}
.bd.fill > .fc{display:flex;flex-direction:column;justify-content:center}
.fc{display:flex;flex-direction:column;justify-content:center}
.bd .mq,.bd .chips{margin-top:0}
.bd .opts{margin-top:0}
.top{display:flex;justify-content:space-between;align-items:center;margin-bottom:34px}
.logo{background:#fff;border-radius:18px;padding:14px 22px;box-shadow:0 6px 18px #01528918}
.datebox{text-align:right}
.datebox .k{font-weight:900;font-size:40px;line-height:.95;color:%(NAVY)s;letter-spacing:-1px}
.datebox .k span{color:%(ORANGE)s}
.datebox .d{display:inline-block;margin-top:10px;background:%(NAVY)s;color:#fff;font-weight:600;font-size:24px;padding:7px 18px;border-radius:10px}
.tagrow{display:flex;align-items:center;gap:16px;margin-bottom:20px}
.tag{background:%(ORANGE)s;color:#fff;font-weight:700;font-size:26px;letter-spacing:1.5px;padding:8px 20px;border-radius:6px;white-space:nowrap}
.tagrow .line{flex:1;height:3px;background:%(ORANGE)s}
h1{font-weight:800;font-size:%(H1)dpx;line-height:1.06;letter-spacing:-1.5px;color:%(NAVY)s}
h1 .o{color:%(ORANGE)s}
.rule{width:140px;height:7px;background:%(ORANGE)s;border-radius:4px;margin:24px 0 26px}
.lead{font-size:34px;line-height:1.42;color:%(INK)s;font-weight:500}
h2{font-weight:800;font-size:60px;line-height:1.08;color:%(NAVY)s;letter-spacing:-1px}
h2 .o{color:%(ORANGE)s}
.banner{display:inline-block;background:%(NAVY)s;color:#fff;font-weight:700;font-size:30px;padding:10px 26px;border-radius:12px;margin:26px 0 18px}
.banner.or{background:%(ORANGE)s}
.info{display:flex;gap:28px;align-items:center;background:%(SKY)s;border:2px solid %(BLUE)s33;border-radius:22px;padding:26px 30px;margin-top:22px}
.circ{flex:none;width:118px;height:118px;border-radius:50%%;background:%(NAVY)s;display:flex;align-items:center;justify-content:center;color:#fff}
.circ.or{background:%(ORANGE)s}
.info .t{font-weight:800;font-size:34px;color:%(NAVY)s;margin-bottom:6px}
.info .b{font-size:29px;line-height:1.42}
.cards{display:flex;gap:0;margin-top:8px}
.card{flex:1;padding:6px 22px;border-left:2px dashed %(BLUE)s55;text-align:left}
.card:first-child{border-left:none;padding-left:0}
.card .ic{width:98px;height:98px;border-radius:50%%;display:flex;align-items:center;justify-content:center;color:#fff;margin-bottom:14px}
.card .h{font-weight:800;font-size:31px;color:%(NAVY)s;line-height:1.15;margin-bottom:8px}
.card .b{font-size:26px;line-height:1.38;color:%(MUTED)s}
.stats{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:6px}
.stat{background:#fff;border-radius:20px;padding:24px 26px;border:2px solid %(BLUE)s22;box-shadow:0 6px 16px #01528912;position:relative;overflow:hidden}
.stat:before{content:'';position:absolute;left:0;top:0;bottom:0;width:10px;background:%(ORANGE)s}
.stat .n{font-weight:900;font-size:60px;line-height:1;color:%(NAVY)s;letter-spacing:-1.5px}
.stat .n small{font-size:30px;font-weight:800;letter-spacing:0}
.stat .l{font-size:25px;line-height:1.3;color:%(MUTED)s;margin-top:10px;font-weight:500}
.stat.big{grid-column:span 2;background:%(NAVY)s;border:none}
.stat.big .n{color:#fff;font-size:88px}.stat.big .l{color:#D6E4F0;font-size:28px}.stat.big b{color:#F2A33A}
.stat.big:before{background:%(GOLD)s}
.chain{display:flex;align-items:center;gap:0;margin-top:22px}
.chain .s{flex:1;background:%(BLUE)s;color:#fff;font-weight:700;font-size:25px;text-align:center;padding:20px 8px 20px 26px;
  clip-path:polygon(0 0,88%% 0,100%% 50%%,88%% 100%%,0 100%%,12%% 50%%)}
.chain .s:first-child{clip-path:polygon(0 0,88%% 0,100%% 50%%,88%% 100%%,0 100%%);padding-left:12px}
.chain .s:nth-child(2){background:#1668A3}.chain .s:nth-child(3){background:#2B7FB8}.chain .s:last-child{background:%(ORANGE)s}
.flash{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:6px}
.fc{background:#fff;border-radius:18px;padding:26px 26px;border-top:8px solid %(BLUE)s;box-shadow:0 5px 14px #01528914}
.fc:nth-child(even){border-top-color:%(ORANGE)s}
.fc .k{font-weight:800;font-size:30px;color:%(NAVY)s;margin-bottom:6px}
.fc .v{font-size:26px;line-height:1.38;color:%(MUTED)s}
.qbox{background:#fff;border:3px solid %(BLUE)s;border-radius:26px;padding:30px 34px;margin-top:0;box-shadow:0 8px 22px #0152891a}
.qbox .st{font-size:29px;line-height:1.38;margin-bottom:12px;display:flex;gap:14px}
.qbox .st .num{flex:none;width:40px;height:40px;border-radius:50%%;background:%(NAVY)s;color:#fff;font-weight:700;font-size:22px;display:flex;align-items:center;justify-content:center;margin-top:1px}
.qbox .ask{font-weight:800;font-size:28px;color:%(NAVY)s;margin-top:6px}
.opts{margin-top:0;display:flex;flex-direction:column;gap:16px}
.opt{display:flex;align-items:stretch;height:74px;filter:drop-shadow(0 5px 8px #0A2A4A22)}
.opt .L{width:86px;background:%(ORANGE)s;color:#fff;font-weight:900;font-size:42px;display:flex;align-items:center;justify-content:center;border-radius:14px 0 0 14px}
.opt .T{flex:1;background:#fff;display:flex;align-items:center;padding:0 28px;font-weight:700;font-size:31px;color:%(NAVY)s;border-radius:0 14px 14px 0}
.cta{position:absolute;left:50%%;transform:translateX(-50%%);bottom:24px;background:%(ORANGE)s;color:#fff;font-weight:700;font-size:32px;padding:14px 46px;border-radius:40px;white-space:nowrap;z-index:5;box-shadow:0 6px 16px #0006}
.foot{position:absolute;left:62px;right:62px;bottom:0;height:100px;display:flex;justify-content:space-between;align-items:center;color:#fff;font-weight:600;font-size:24px;z-index:5}
.foot .url{display:flex;align-items:center;gap:12px;font-size:26px;letter-spacing:.3px}
.foot .pg{background:%(ORANGE)s;color:#fff;font-weight:800;font-size:28px;padding:6px 18px;border-radius:12px}
.verdict{display:flex;gap:22px;align-items:flex-start;background:#fff;border-radius:18px;padding:24px 26px;margin-bottom:0;box-shadow:0 5px 14px #01528912}
.verdict .v{flex:none;width:64px;height:64px;border-radius:14px;display:flex;align-items:center;justify-content:center;color:#fff}
.verdict .v.ok{background:#1F8A4C}.verdict .v.no{background:#C0392B}
.verdict .h{font-weight:800;font-size:30px;color:%(NAVY)s;margin-bottom:4px}
.verdict .b{font-size:27px;line-height:1.38;color:%(MUTED)s}
.ans{display:flex;align-items:center;gap:24px;background:%(NAVY)s;color:#fff;border-radius:22px;padding:22px 30px;margin:0}
.ans .a{font-weight:900;font-size:64px;color:%(GOLD)s}
.ans .t{font-weight:700;font-size:30px;line-height:1.25}
.chips{display:flex;flex-wrap:wrap;gap:12px;margin-top:14px}
.chip{background:#fff;border:2px solid %(BLUE)s55;color:%(NAVY)s;font-weight:700;font-size:25px;padding:8px 18px;border-radius:30px}
.mq{background:#FFF4E3;border-left:10px solid %(ORANGE)s;border-radius:0 18px 18px 0;padding:26px 30px;font-size:30px;line-height:1.4;font-weight:600;color:%(NAVY)s;margin-top:18px}
.hero{display:flex;align-items:center;justify-content:center;margin-top:34px;position:relative;height:330px}
.hero .ring{position:absolute;width:320px;height:320px;border-radius:50%%;border:3px dashed %(BLUE)s55}
.hero .core{width:210px;height:210px;border-radius:50%%;background:%(NAVY)s;display:flex;align-items:center;justify-content:center;color:#fff;box-shadow:0 14px 30px #0A2A4A44}
.hero .sat{position:absolute;left:calc(50%% - 48px);top:calc(50%% - 48px);width:96px;height:96px;border-radius:50%%;display:flex;align-items:center;justify-content:center;color:#fff;box-shadow:0 8px 16px #0003}
.swipe{position:absolute;right:62px;bottom:166px;font-weight:700;font-size:26px;color:%(ORANGE)s;display:flex;align-items:center;gap:8px}
"""

def page(body, W=1080, H=1350, h1=76, footer=True, page_no=None, cta=None, handle=None):
    css = CSS % dict(W=W, H=H, INK=INK, PAPER=PAPER, NAVY=NAVY, ORANGE=ORANGE, BLUE=BLUE, SKY=SKY, MUTED=MUTED, GOLD=GOLD, H1=h1)
    foot = ''
    if cta:
        foot = f'<div class="swoosh"></div><div class="cta">{html.escape(cta)}</div>'
    elif footer:
        pg = f'<span class="pg">{page_no}</span>' if page_no else '<span></span>'
        foot = f'<div class="swoosh"></div><div class="foot"><span class="url">{icon("globe", 30, "#F2A33A", 2.4)}<span>www.lotusarise.com</span></span>{pg}</div>'
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{font_face()}{css}</style></head>
<body><div class="bg-dots"></div><div class="bg-dots bl"></div><div class="frame"></div>{body}{foot}</body></html>"""

def top(kicker_a='CURRENT', kicker_b='AFFAIRS', date=None, logo_w=300):
    d = f'<div class="d">{html.escape(date)}</div>' if date else ''
    return f"""<div class="top"><div class="logo">{logo_img(logo_w)}</div>
<div class="datebox"><div class="k">{kicker_a}<br><span>{kicker_b}</span></div>{d}</div></div>"""

def mini_top(label, logo=False):
    lg = f'<div class="logo" style="padding:10px 16px">{logo_img(220)}</div>' if logo else ''
    return f'<div class="top" style="margin-bottom:22px"><div class="tagrow" style="flex:1;margin:0"><span class="tag">{html.escape(label)}</span><span class="line"></span></div>{lg}</div>'

def headline(a, b=''):
    return f'<h1>{rich(a)}{" <span class=o>"+rich(b)+"</span>" if b else ""}</h1>'

def h2(a, b=''):
    return f'<h2>{rich(a)}{" <span class=o>"+rich(b)+"</span>" if b else ""}</h2>'

def info(icon_name, title, body, orange=False):
    return f"""<div class="info"><div class="circ{' or' if orange else ''}">{icon(icon_name, 60, '#fff')}</div>
<div><div class="t">{rich(title)}</div><div class="b">{rich(body)}</div></div></div>"""

def cards(items):
    cols = [NAVY, ORANGE, BLUE, '#1F8A4C']
    out = []
    for i, (ic, h, b) in enumerate(items):
        out.append(f'<div class="card"><div class="ic" style="background:{cols[i % 4]}">{icon(ic, 50, "#fff")}</div>'
                   f'<div class="h">{rich(h)}</div><div class="b">{rich(b)}</div></div>')
    return '<div class="cards">' + ''.join(out) + '</div>'

def stats(items):
    out = []
    for it in items:
        n, l = it[0], it[1]
        big = len(it) > 2 and it[2]
        out.append(f'<div class="stat{" big" if big else ""}"><div class="n">{n}</div><div class="l">{rich(l)}</div></div>')
    return '<div class="stats">' + ''.join(out) + '</div>'

def chain(steps):
    return '<div class="chain">' + ''.join(f'<div class="s">{html.escape(s)}</div>' for s in steps) + '</div>'

def flash(items):
    return '<div class="flash">' + ''.join(f'<div class="fc"><div class="k">{rich(k)}</div><div class="v">{rich(v)}</div></div>' for k, v in items) + '</div>'

def mcq_q(statements, ask, options):
    st = ''.join(f'<div class="st"><span class="num">{i+1}</span><span>{rich(s)}</span></div>' for i, s in enumerate(statements))
    op = ''.join(f'<div class="opt"><div class="L">{L}</div><div class="T">{rich(t)}</div></div>' for L, t in zip('ABCD', options))
    return f'<div class="qbox">{st}<div class="ask">{rich(ask)}</div></div><div class="opts">{op}</div>'

def verdicts(items):
    out = []
    for ok, h, b in items:
        out.append(f'<div class="verdict"><div class="v {"ok" if ok else "no"}">{icon("check" if ok else "x", 40, "#fff", 3)}</div>'
                   f'<div><div class="h">{rich(h)}</div><div class="b">{rich(b)}</div></div></div>')
    return ''.join(out)

def hero(center_icon, sats):
    pos = [(-250, -70), (250, -70), (-190, 120), (190, 120)]
    cols = [ORANGE, BLUE, '#1F8A4C', GOLD]
    s = ''.join(f'<div class="sat" style="background:{cols[i]};transform:translate({pos[i][0]}px,{pos[i][1]}px)">{icon(n, 46, "#fff")}</div>' for i, n in enumerate(sats))
    return f'<div class="hero"><div class="ring"></div><div class="core">{icon(center_icon, 110, "#fff", 1.8)}</div>{s}</div>'

def slide(head, body, fill=False):
    return f'<div class="wrap"><div class="hd">{head}</div><div class="bd{" fill" if fill else ""}">{body}</div></div>'

def bullets_box(icon_name, title, items, orange=False):
    li = ''.join(f'<div style="display:flex;gap:12px;margin-top:8px"><span style="color:#D17502;font-weight:900">▸</span><span>{rich(x)}</span></div>' for x in items)
    return f"""<div class="info" style="align-items:flex-start"><div class="circ{' or' if orange else ''}">{icon(icon_name, 60, '#fff')}</div>
<div><div class="t">{rich(title)}</div><div class="b">{li}</div></div></div>"""
