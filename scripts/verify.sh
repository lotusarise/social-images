#!/usr/bin/env bash
# verify.sh - Confirm image URLs are publicly fetchable before posting them.
#
# Usage:  scripts/verify.sh <url> [<url>...]
#
# Prints one line per URL and exits non-zero if ANY url is not a live image.
# Run this immediately before handing URLs to Metricool: it is the last gate
# between a broken link and a published post with a missing image.

set -uo pipefail

FAILED=0

if [ $# -eq 0 ]; then
  echo "verify.sh: no URLs given" >&2
  exit 2
fi

for url in "$@"; do
  headers="$(curl -sIL --max-time 25 "$url" 2>/dev/null)" || headers=""
  code="$(printf '%s' "$headers"  | awk 'BEGIN{IGNORECASE=1} /^HTTP/{c=$2} END{print c}')"
  ctype="$(printf '%s' "$headers" | awk 'BEGIN{IGNORECASE=1} /^content-type:/{t=$2} END{print t}')"
  size="$(printf '%s' "$headers"  | awk 'BEGIN{IGNORECASE=1} /^content-length:/{s=$2} END{print s}')"

  case "$code:$ctype" in
    200:image/*)
      printf 'OK    %s  (%s, %s bytes)\n' "$url" "$ctype" "${size:-unknown}"
      ;;
    *)
      printf 'BAD   %s  (status=%s type=%s)\n' "$url" "${code:-none}" "${ctype:-none}"
      FAILED=1
      ;;
  esac
done

exit $FAILED
