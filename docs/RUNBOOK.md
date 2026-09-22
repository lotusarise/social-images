# Daily social automation runbook

## Accounts in play

| Thing                | Value                                               |
| -------------------- | --------------------------------------------------- |
| Metricool brand      | `LotusArise`, blogId `4860368`                       |
| Metricool timezone   | `Asia/Kolkata`                                       |
| Metricool networks   | Instagram `lotus_arise`, Facebook, Threads, Pinterest `lotusarise`, Google Business Profile |
| Typefully social set | `334144` (`Lotus_Arise_1`)                           |
| Image host           | this repo, `lotusarise/social-images`                |

## Order of operations

1. **Preflight the host.** `scripts/preflight.sh`. If this fails, GitHub is not
   usable from the current session and you should go to the fallback order
   below *before* generating anything.
2. **Generate the day's images** with the approved design system in
   `template/` — never with an ad-hoc renderer. Write a Python script modelled
   on `template/example_rare_earths.py`, then:

       cd template && python3 <your_script>.py && node render.js out html/*.html

   `render.js` prints `<png> overflow <px>` per slide and **exits 2 if any
   slide overflowed**. Treat a non-zero exit as a hard stop: fix the copy and
   re-render. Never publish a slide that overflowed.

   First-time setup on a machine, per `template/README.md`:

       cd template && npm i && mkdir -p assets html out
       curl -sSL -o assets/logo.png https://lotusarise.com/wp-content/uploads/brand/lotusarise-ias-logo.png

   Note: `playwright-core` bundles no browser. `render.js` looks for the
   Linux `/opt/pw-browsers` build first, then falls back to the Google Chrome
   installed on this Mac. If neither exists, run `npx playwright install`.
3. **Publish and verify.** `scripts/publish.sh --json <files...>`. Use only the
   URLs it returns. If it exits non-zero, treat the GitHub host as unavailable.
4. **Schedule the posts.**
   - Image posts (Instagram, Pinterest, Facebook) -> Metricool
     `createScheduledPost`, `blogId: "4860368"`, `media: [<verified urls>]`,
     `publicationDate.timezone: "Asia/Kolkata"`.
     Pinterest also requires `pinterestData.boardId` and `pinTitle`.
     Instagram requires at least one image.
   - Text-led posts (X, LinkedIn, Bluesky, Threads, Substack) -> Typefully.
     Typefully has its own media store: `create_media_upload` returns a
     presigned S3 URL, `PUT` the raw bytes with no extra headers, then attach
     the returned `media_id`. Typefully posts do **not** need this repo.
5. **Re-verify before the post goes live.** `scripts/verify.sh <urls...>`.

## Host fallback order

Use the first one that works. Never skip the verification step, whichever host
you land on.

1. **This repo** (`scripts/publish.sh`). Preferred: public, permanent, free,
   and the URL is checked before use.
2. **Typefully media upload** (`create_media_upload` + `PUT`). Works for
   Typefully-delivered networks only — Metricool cannot read those media ids.
3. **Google Drive.** Metricool can ingest a Drive link, but only if Google
   Drive is linked inside the Metricool account, and the upload must be
   byte-for-byte complete. Slowest and the most failure-prone of the three.

If all three fail: **skip Instagram and Pinterest entirely** and publish
text-only on the networks that allow it. Do not publish an image post with an
unverified URL. Report which host failed and the exact error.

## Failure modes seen before

- **`git push` rejected / no credentials.** The session has no write access to
  the repo. `preflight.sh` catches this in seconds instead of at posting time.
- **URL pushed but 404 for a few seconds.** Expected; `publish.sh` polls for up
  to 120s before giving up.
- **Google Drive upload truncated.** A partial file uploads "successfully" and
  then serves a corrupt image. Match the byte count against the original.
- **Filenames with spaces or non-ASCII.** `publish.sh` rewrites names to
  `[A-Za-z0-9_-]` so the raw URL never needs escaping.
