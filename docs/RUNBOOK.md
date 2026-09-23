# Daily social automation runbook

## Where this runs

The working checkout on the Mac is `/Users/arvind/Social Media Marketing`.
The folder name contains spaces, so quote it in every shell command. The
scripts themselves resolve their own repo root, so they work from any path.

The daily routine is bound to this Mac. A device-bound routine only runs
while the Claude desktop app is open; if it is closed at the scheduled time
it runs on next launch.

IMPORTANT (verified 23 Sept 2026): a routine's shell on this Mac is NOT
macOS. It is an isolated Linux sandbox with the connected folder mounted at
$HOME/mnt/Social Media Marketing. Consequences:

- `~/.ssh` does not exist there and github.com does not resolve over SSH, so
  an `git@github.com:` remote can never authenticate. The remote is HTTPS
  with a fine-grained PAT (Contents: read/write on this repo only) stored in
  this checkout's `.git/config`. Rotate it before it expires; `.git/config`
  is local and never pushed.
- Author identity is not inherited, so it is set repo-locally
  (`git config user.name/user.email`). Do not remove it.
- The sandbox reaches the network through a proxy that allow-lists hosts.
  github.com, raw.githubusercontent.com and api.github.com work. Typefully's
  media host does not - see below.

## Accounts in play

| Thing                | Value                                               |
| -------------------- | --------------------------------------------------- |
| Metricool brand      | `LotusArise`, blogId `4860368`                       |
| Metricool timezone   | `Asia/Kolkata`                                       |
| Metricool networks   | Instagram `lotus_arise`, Facebook, Threads, Pinterest `lotusarise` (board "UPSC Exam", boardId `706431960239283710`), Google Business Profile |
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
   - Text-led posts (X, LinkedIn, Bluesky, Substack) -> Typefully.
     Typefully has its own media store: `create_media_upload` returns a
     presigned S3 URL, `PUT` the raw bytes with no extra headers, then attach
     the returned `media_id`. Typefully posts do **not** need this repo.
     BUT (verified 23 Sept 2026) `typefully-user-uploads.s3.amazonaws.com`
     returns `403 from proxy after CONNECT` in BOTH the cloud environment and
     this Mac's routine sandbox, so the upload cannot be done from a routine
     at all. Publish X and LinkedIn with the article link instead and let the
     link preview supply the picture. The earlier claim that "the upload works
     normally when the routine runs on the Mac" is wrong.
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
  On this Mac that means the PAT in `.git/config` has expired or been revoked:
  create a new fine-grained token and re-run
  `git remote set-url origin "https://<TOKEN>@github.com/lotusarise/social-images.git"`.

- **Stale `.git/refs/.../*.lock`.** The sandbox cannot delete files unless the
  user has granted delete permission for the folder in that session, so a
  crashed git run can leave a lock behind and the next push logs
  `cannot lock ref`. Ask for delete permission and `rm` the `.lock` file.

- **Cloud session can clone but not push (seen 23 Sept 2026).** The repo is
  public, so a claude.ai/code session clones it anonymously and renders every
  slide correctly — then the push fails and the images have no public URL, so
  Instagram and Pinterest are dropped while the run otherwise looks healthy.
  The Claude GitHub App already has write access to this repo; the missing
  piece is that the git proxy only injects a credential for repositories in
  that session's authorised set, and it says so verbatim:
  "lotusarise/social-images is not in this session's authorized repository
  set". A cloud routine therefore needs the repo added as one of its sources
  when it is created. The Mac routine does not - it uses the PAT above.
- **No browser in the Mac routine sandbox (seen 23 Sept 2026).** `render.js`
  finds neither `/opt/pw-browsers` nor a macOS Chrome, because the routine
  shell is a Linux sandbox with no browser installed, and `npx playwright
  install` fails: `cdn.playwright.dev` returns
  `403 Connection blocked by network allowlist`. Workaround used: stage
  `la_design.py`, the day's script, `render.js`, `package.json` and
  `assets/logo.png` into the cloud container, `npm i` there (the npm registry
  is allowed), and run the SAME `daily.py` + `render.js` against the
  container's `/opt/pw-browsers/chromium-*/chrome-linux/chrome`. Then commit
  the PNGs back to `template/out/` and run `publish.sh` on the Mac as usual.
  The HTML embeds fonts by absolute path, so regenerate it in the container -
  copying the Mac's HTML across will lose the fonts.

- **URL pushed but 404 for a few seconds.** Expected; `publish.sh` polls for up
  to 120s before giving up.
- **Google Drive upload truncated.** A partial file uploads "successfully" and
  then serves a corrupt image. Match the byte count against the original.
- **Filenames with spaces or non-ASCII.** `publish.sh` rewrites names to
  `[A-Za-z0-9_-]` so the raw URL never needs escaping.
