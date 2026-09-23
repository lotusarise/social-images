#!/usr/bin/env bash
# preflight.sh - Check that this machine/session can actually use the host.
#
# Usage:  scripts/preflight.sh
#
# Run this FIRST in the daily task. It answers the one question that broke
# every previous attempt: "can I push right now?" - and it answers it without
# leaving anything behind in the repo history.

set -uo pipefail

REPO_SLUG="lotusarise/social-images"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

status=0
say() { printf '%-28s %s\n' "$1" "$2"; }

# 1. Can we see github at all?
if curl -sf -o /dev/null --max-time 15 https://api.github.com; then
  say "github api" "reachable"
else
  say "github api" "UNREACHABLE"
  status=1
fi

# 2. Does the repo exist?
vis="$(curl -s --max-time 15 "https://api.github.com/repos/${REPO_SLUG}" \
       | awk -F'"' '/"private"/{print; exit}')"
if [ -n "$vis" ]; then
  say "repo ${REPO_SLUG}" "found"
else
  say "repo ${REPO_SLUG}" "NOT FOUND"
  status=1
fi

# 3. Is a remote configured?
if git remote get-url origin >/dev/null 2>&1; then
  say "git remote" "$(git remote get-url origin | sed -E 's#//[^@]*@#//***@#')"
else
  say "git remote" "NOT CONFIGURED"
  status=1
fi

# 4. The real test: can we push? Push the current commit to a scratch ref and
#    delete it again. This exercises credentials and network egress without
#    adding a commit or a branch anyone will see.
probe_ref="refs/heads/_preflight-$(date +%s)"
if GIT_TERMINAL_PROMPT=0 git push -q origin "HEAD:${probe_ref}" 2>/dev/null; then
  say "push access" "GRANTED"
  if GIT_TERMINAL_PROMPT=0 git push -q origin --delete "${probe_ref}" 2>/dev/null; then
    say "cleanup" "probe ref removed"
  else
    say "cleanup" "WARNING: could not delete ${probe_ref}"
  fi
else
  say "push access" "DENIED (no credentials or egress blocked)"
  status=1
fi

echo
if [ $status -eq 0 ]; then
  echo "preflight: OK - GitHub can be used as the image host."
else
  echo "preflight: FAILED - fall back to another host (see docs/RUNBOOK.md)."
fi
exit $status
