#!/usr/bin/env bash
# publish.sh - Host images on GitHub and return verified public URLs.
#
# Usage:  scripts/publish.sh [--json] [--date YYYY-MM-DD] <image> [<image>...]
#
# Copies each image into images/<date>/, commits, pushes, then polls the
# raw.githubusercontent.com URL until it actually serves the bytes. Only URLs
# confirmed live are printed. Exit code is non-zero if any image fails to
# become reachable, so the caller can fall back to another host instead of
# handing a broken link to Metricool.

set -euo pipefail

REPO_SLUG="lotusarise/social-images"
BRANCH="main"
RAW_BASE="https://raw.githubusercontent.com/${REPO_SLUG}/${BRANCH}"
VERIFY_TIMEOUT=120   # seconds to wait for a URL to go live
VERIFY_INTERVAL=3

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

OUTPUT_JSON=0
DATE_DIR="$(date +%F)"
FILES=()

while [ $# -gt 0 ]; do
  case "$1" in
    --json) OUTPUT_JSON=1; shift ;;
    --date) DATE_DIR="$2"; shift 2 ;;
    -h|--help) sed -n '2,11p' "$0"; exit 0 ;;
    -*) echo "publish.sh: unknown option $1" >&2; exit 2 ;;
    *) FILES+=("$1"); shift ;;
  esac
done

if [ ${#FILES[@]} -eq 0 ]; then
  echo "publish.sh: no image files given" >&2
  exit 2
fi

log() { echo "[publish] $*" >&2; }

# --- 1. Validate inputs before touching git -------------------------------
for f in "${FILES[@]}"; do
  [ -f "$f" ] || { echo "publish.sh: not a file: $f" >&2; exit 1; }
  [ -s "$f" ] || { echo "publish.sh: file is empty: $f" >&2; exit 1; }
  lower="$(printf '%s' "$f" | tr 'A-Z' 'a-z')"
  case "$lower" in
    *.png|*.jpg|*.jpeg|*.webp|*.gif) ;;
    *) echo "publish.sh: unsupported extension: $f" >&2; exit 1 ;;
  esac
done

DEST_DIR="images/${DATE_DIR}"
mkdir -p "$DEST_DIR"

# --- 2. Copy in with collision-safe, URL-safe names -----------------------
REL_PATHS=()
for f in "${FILES[@]}"; do
  base="$(basename "$f")"
  ext="$(printf '%s' "${base##*.}" | tr 'A-Z' 'a-z')"
  stem="${base%.*}"
  stem="$(printf '%s' "$stem" | tr ' ' '-' | tr -cd 'A-Za-z0-9_-')"
  [ -n "$stem" ] || stem="image"
  candidate="${DEST_DIR}/${stem}.${ext}"
  n=1
  while [ -e "$candidate" ] && ! cmp -s "$f" "$candidate"; do
    candidate="${DEST_DIR}/${stem}-${n}.${ext}"
    n=$((n+1))
  done
  cp -f "$f" "$candidate"
  REL_PATHS+=("$candidate")
  log "staged $candidate ($(wc -c < "$candidate" | tr -d ' ') bytes)"
done

# --- 3. Commit and push ---------------------------------------------------
git add -- "${REL_PATHS[@]}"
if git diff --cached --quiet; then
  log "no new content to commit (images already present)"
else
  git commit -qm "images: ${DATE_DIR} (${#REL_PATHS[@]} file(s))"
  log "committed"
fi

if ! GIT_TERMINAL_PROMPT=0 git push -q origin "HEAD:${BRANCH}"; then
  echo "publish.sh: git push failed - images are NOT publicly reachable" >&2
  exit 3
fi
log "pushed to ${REPO_SLUG}@${BRANCH}"

# --- 4. Verify each URL is genuinely live before handing it out -----------
LIVE_URLS=()
FAILED=0
for rel in "${REL_PATHS[@]}"; do
  url="${RAW_BASE}/${rel}"
  deadline=$(( $(date +%s) + VERIFY_TIMEOUT ))
  ok=0
  code=""
  ctype=""
  while [ "$(date +%s)" -lt "$deadline" ]; do
    probe="$(curl -sIL --max-time 20 "$url" \
      | awk 'BEGIN{IGNORECASE=1} /^HTTP/{c=$2} /^content-type:/{t=$2} END{print c, t}')" || probe=""
    code="$(printf '%s' "$probe" | awk '{print $1}')"
    ctype="$(printf '%s' "$probe" | awk '{print $2}')"
    case "$code:$ctype" in
      200:image/*) ok=1; break ;;
    esac
    sleep "$VERIFY_INTERVAL"
  done
  if [ $ok -eq 1 ]; then
    log "live: $url"
    LIVE_URLS+=("$url")
  else
    log "FAILED to verify: $url (last status=${code:-none} type=${ctype:-none})"
    FAILED=1
  fi
done

# --- 5. Emit ---------------------------------------------------------------
if [ $OUTPUT_JSON -eq 1 ]; then
  ok_flag=false
  [ $FAILED -eq 0 ] && ok_flag=true
  printf '{"date":"%s","ok":%s,"urls":[' "$DATE_DIR" "$ok_flag"
  for i in "${!LIVE_URLS[@]}"; do
    [ "$i" -gt 0 ] && printf ','
    printf '"%s"' "${LIVE_URLS[$i]}"
  done
  printf ']}\n'
else
  [ ${#LIVE_URLS[@]} -gt 0 ] && printf '%s\n' "${LIVE_URLS[@]}"
fi

exit $FAILED
