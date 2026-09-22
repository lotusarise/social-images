#!/usr/bin/env bash
# pick-content.sh - Choose a lotusarise.com article to promote today.
#
# Usage:
#   scripts/pick-content.sh              # pick one, print JSON
#   scripts/pick-content.sh --mark URL   # record URL as posted
#
# Reads the public sitemap rather than /feed/ (the feed returns 403 to
# non-browser clients) and skips anything already in state/posted-log.txt,
# so the rotation does not repeat until the whole pool is used.
#
# Prints: {"url":"...","title":"...","description":"..."}

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG="${REPO_ROOT}/state/posted-log.txt"
mkdir -p "${REPO_ROOT}/state"
touch "$LOG"

if [ "${1:-}" = "--mark" ]; then
  [ -n "${2:-}" ] || { echo "pick-content.sh: --mark needs a URL" >&2; exit 2; }
  echo "$2" >> "$LOG"
  echo "marked: $2" >&2
  exit 0
fi

LOG="$LOG" python3 <<'PY'
import os, re, sys, json, random, html, subprocess

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0 Safari/537.36")
INDEX = "https://lotusarise.com/sitemap_index.xml"

def get(url, timeout=30):
    # curl, not urllib: the system python on macOS ships without a CA bundle,
    # so urllib raises CERTIFICATE_VERIFY_FAILED on any https URL here.
    # A browser UA is required too - lotusarise.com serves 403 to default
    # agents (its /feed/ refuses them outright).
    out = subprocess.run(
        ["curl", "-sL", "--max-time", str(timeout), "-A", UA, url],
        capture_output=True)
    if out.returncode != 0:
        raise RuntimeError(f"curl exit {out.returncode}")
    return out.stdout.decode("utf-8", "replace")

def die(msg):
    print(f"pick-content.sh: {msg}", file=sys.stderr)
    sys.exit(1)

# 1. Which sitemaps hold articles? Only post-* and premium-* are editorial;
#    product/page/quiz sitemaps are not things to promote as reading.
try:
    idx = get(INDEX)
except Exception as e:
    die(f"could not fetch sitemap index: {e}")

maps = [m for m in re.findall(r"<loc>(.*?)</loc>", idx)
        if re.search(r"/(post|premium)-sitemap", m)]
if not maps:
    die("no post sitemaps found in index")

# 2. Gather candidate article URLs.
urls = []
for m in maps:
    try:
        urls += re.findall(r"<loc>(https://lotusarise\.com/[^<]+)</loc>", get(m))
    except Exception:
        continue          # one bad sitemap should not sink the run

urls = [u for u in dict.fromkeys(urls) if u.rstrip("/") != "https://lotusarise.com"]
if not urls:
    die("no article URLs found")

# 3. Drop anything already posted. If the pool is exhausted, start over
#    rather than failing - the library is evergreen and worth recycling.
posted = set()
logp = os.environ["LOG"]
if os.path.exists(logp):
    posted = {l.strip() for l in open(logp) if l.strip()}

pool = [u for u in urls if u not in posted]
recycled = False
if not pool:
    pool, recycled = urls, True

# 4. Pick one that actually resolves and has usable metadata. Try a few, so
#    a single dead or metadata-less page does not abort the morning run.
random.shuffle(pool)

def meta(doc, prop):
    pat = (r'<meta[^>]+(?:property|name)=["\']' + prop +
           r'["\'][^>]+content=["\'](.*?)["\']')
    m = re.search(pat, doc, re.S | re.I)
    if not m:
        pat2 = (r'<meta[^>]+content=["\'](.*?)["\'][^>]+(?:property|name)=["\']'
                + prop + r'["\']')
        m = re.search(pat2, doc, re.S | re.I)
    return html.unescape(m.group(1)).strip() if m else ""

for cand in pool[:8]:
    try:
        doc = get(cand)
    except Exception:
        continue
    title = meta(doc, "og:title") or meta(doc, "title")
    if not title:
        m = re.search(r"<title>(.*?)</title>", doc, re.S | re.I)
        title = html.unescape(m.group(1)).strip() if m else ""
    desc = meta(doc, "og:description") or meta(doc, "description")
    if not title:
        continue
    # Trim the site suffix editors leave on og:title.
    title = re.sub(r"\s*[-|–]\s*(UPSC|LotusArise).*$", "", title).strip()
    print(json.dumps({
        "url": cand,
        "title": title,
        "description": desc,
        "recycled": recycled,
        "pool_size": len(pool),
    }))
    sys.exit(0)

die("no candidate article returned usable metadata")
PY
