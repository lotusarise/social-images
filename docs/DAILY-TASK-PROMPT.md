# Daily task — setup and prompt

Create a scheduled task (routine) with:

- **Schedule:** `0 6 * * *` (6:00 AM, Asia/Kolkata — cron runs in local time)
- **Title:** LotusArise daily social post (6 AM)
- **Notify on completion:** on

Paste everything below the line as the task prompt.

**If the routine runs in the cloud (claude.ai/code)** — which is where it runs
today — it must have `lotusarise/social-images` selected as its repository,
**and the Claude GitHub App must have write access to that repo**
(github.com/settings/installations → Configure → Repository access).

Read access is not enough and fails in a way that looks like success: the repo
is public, so a cloud session clones it and renders every slide perfectly,
then cannot push, so the images have no public URL and Instagram and Pinterest
are dropped. That is exactly what happened on 23 Sept 2026.

**If the routine runs on the Mac instead**, it uses the SSH key in `~/.ssh`
and needs no GitHub App. Note that a local routine only runs while the Claude
desktop app is open; if it is closed at 6 AM the task runs on next launch.

---

Publish the LotusArise daily social post promoting an article from lotusarise.com.

Work in this session's checkout of `lotusarise/social-images`. Every command
below is relative to the repo root, so it works whether that checkout is
`~/social-images` on the Mac or a cloud workspace — never hardcode a path.
Read `docs/RUNBOOK.md` and `template/README.md` before doing anything;
`template/README.md` is the owner-approved brand spec and its rules are not
negotiable.

IMPORTANT CONTEXT: posts go out auto-published to live public accounts. The
user chose this over hold-for-review. The verification steps below are the
only thing between a broken post and the public. Never publish an image URL
you have not verified, and never publish a slide that overflowed.

## Step 1 — Sync and preflight

    cd "$(git rev-parse --show-toplevel)"
    git pull --rebase
    ./scripts/preflight.sh

If preflight fails, GitHub cannot host images today. Go to Step 7.

## Step 2 — Pick today's article

    ./scripts/pick-content.sh

Prints `{"url","title","description","recycled","pool_size"}`. It reads the
public sitemap (the site's /feed/ returns 403 to non-browser clients) and
skips anything in `state/posted-log.txt`, so it will not repeat until the
~5400-article pool is exhausted. Retry once on failure, then go to Step 7.

Read the article itself before writing slides. Do not invent facts, figures
or dates — everything on a slide must come from the article.

## Step 3 — Build the slides with the approved template

One-time setup, if `template/node_modules` is missing:

    cd template && npm i && mkdir -p assets html out
    curl -sSL -o assets/logo.png https://lotusarise.com/wp-content/uploads/brand/lotusarise-ias-logo.png

Write `template/daily.py` modelled on `template/example_rare_earths.py`. Build:

- **An Instagram carousel**, 3–5 slides at the default 1080x1350:
  cover slide using `top(date=...)` + `headline(navy, orange)` + a `lead`,
  then inner slides using `mini_top(...)` + `h2(...)` with `info`,
  `bullets_box`, `cards`, `stats` or `chain` bodies. Number them with
  `page_no='1/N'`.
- **One X / LinkedIn card** at `W=1200, H=675`.

Respect the approved rules in `template/README.md`: max ~40 words of body per
slide, one idea per slide, body text never below 22px, official logo only
(never redrawn or recoloured), footer is globe + www.lotusarise.com only.
Inline `**bold**` renders navy bold and `==highlight==` renders orange bold.

Then render:

    cd "$(git rev-parse --show-toplevel)/template"
    python3 daily.py && node render.js out html/*.html

`render.js` prints `<png> overflow <px>` per slide and **exits 2 if any slide
overflowed**. A non-zero exit is a hard stop: shorten the copy on the named
slide and re-render until every slide reports `overflow 0`. Do not proceed
with an overflowing slide.

## Step 4 — Host the images and get VERIFIED urls

    cd "$(git rev-parse --show-toplevel)"
    ./scripts/publish.sh --json template/out/<slide>.png [more...]

Pass the carousel slides in reading order. This commits, pushes, then polls
each raw URL until it serves real image bytes, printing
`{"date","ok","urls":[...]}` with the URLs in the same order.

If `ok` is false or the exit code is non-zero, the URLs are NOT safe to use.
Go to Step 7.

URLs are pinned to the commit SHA deliberately: raw.githubusercontent.com
caches for 300s, so a branch URL can serve stale content or a stale 404.

## Step 5 — Write the copy

- Lead with the specific insight or question the article answers, not "New
  blog post!". An aspirant should want to read it from the first line.
- Plain, confident language. No hype, at most one emoji.
- Always include the article URL from Step 2.
- Instagram/Facebook: 3–6 short lines, then 5–8 relevant hashtags
  (#UPSC #IAS #UPSCPreparation plus subject-specific ones).
- X: under 270 characters including the link, 1–2 hashtags maximum.
- LinkedIn: 3–4 sentences, professional register, no hashtag block.

## Step 6 — Publish

Use only the verified urls from Step 4.

Metricool (Instagram + Facebook) via `createScheduledPost`:

- `blogId: "4860368"`
- `providers: [{"network":"instagram"},{"network":"facebook"},{"network":"threads"}]`
- `media: [<verified urls, carousel order>]`
- `autoPublish: true`, `draft: false`
- `publicationDate: {dateTime: "<today>T09:30:00", timezone: "Asia/Kolkata"}`
  Optionally call `getBestTimeToPostByNetwork` and use that instead; fall
  back to 09:30 if it returns nothing usable.
- `instagramData: {"type":"POST"}`, `facebookData: {"type":"POST"}`,
  `threadsData: {"allowedCountryCodes": []}`
- Instagram requires at least one image — never send an empty media list.

Threads (`lotus_arise`) is connected to this Metricool brand and must be
included. It was dropped from an earlier version of this prompt by mistake.

Typefully (X + LinkedIn), `social_set_id` 334144:

X and LinkedIn are **not** connected to Metricool — only Facebook, Instagram,
Threads, Pinterest and Google Business are — so Typefully is the only route to
them. There is no Metricool fallback for these two.

- Upload the 1200x675 card with `create_media_upload`, PUT the raw bytes to
  the presigned URL with no extra headers (`curl -T`), then attach the
  returned `media_id`. Typefully cannot read Metricool's media or vice versa.
- Schedule it to publish this morning, not saved as a draft.

**Known limitation in cloud runs:** `typefully-user-uploads.s3.amazonaws.com`
is blocked by the network proxy at the CONNECT stage in the claude.ai/code
cloud environment, so the PUT fails and X/LinkedIn land text-only there. This
is independent of GitHub access — fixing repo permissions does not fix it.
The upload works normally when the routine runs on the Mac. If the PUT fails,
say so explicitly in the report; do not describe the post as having an image.

Pinterest is deliberately excluded: Metricool needs a numeric board ID and
the board has never been confirmed, so including it would fail the whole
request and take Instagram and Facebook down with it. The template can build
a 1000x1500 pin (`W=1000, H=1500`) the moment a board name is supplied.

## Step 7 — Degraded mode (only if Step 1, 2, 3 or 4 failed)

Do not post an image you could not verify, or a slide that overflowed.

But do NOT drop images everywhere just because GitHub is unavailable.
**Typefully hosts its own media and does not depend on this repo at all**, so
X and LinkedIn keep their image even when hosting has failed:

- **X + LinkedIn — still with the image.** Upload the rendered 1200x675 card
  through Typefully's `create_media_upload` exactly as in Step 6. This path
  never touches GitHub. Only fall back to text-only if Step 3 failed and
  there is no rendered card at all.
- **Instagram — skip entirely.** It cannot post without an image, and
  Metricool can only take a public URL, which is precisely what failed.
- **Facebook — text-only** via Metricool with an empty media list.
- State clearly which step failed and the exact error.

A GitHub outage should therefore cost you Instagram, not the whole day.

## Step 8 — Record and report

    ./scripts/pick-content.sh --mark "<article url>"
    cd "$(git rev-parse --show-toplevel)"
    git add state/posted-log.txt && git commit -q -m "state: posted $(date +%F)" && git push -q

Report briefly:

- Which article was promoted, and its URL
- How many slides, and the verified image URLs used
- Which networks published, and which were skipped and why
- Whether the rotation recycled (`"recycled": true` = pool restarted)
- Anything that failed, with the real error text. Do not report success for
  a step that did not succeed.
