# social-images

Public image host for LotusArise social posts.

Metricool will only attach an image it can fetch from a public URL. This repo
is that URL. Images live under `images/<YYYY-MM-DD>/` and are served straight
from GitHub's CDN:

```
https://raw.githubusercontent.com/lotusarise/social-images/<commit-sha>/images/2026-09-22/example.png
```

GitHub serves these with `content-type: image/png` and
`access-control-allow-origin: *`, which is everything Metricool needs. No web
server, no Google Drive sharing settings, no expiring links.

### Why the commit SHA and not `main`

`raw.githubusercontent.com` sends `cache-control: max-age=300`. A branch URL
can therefore serve a stale response for up to five minutes — this was
observed for real while setting this repo up, with `/main/README.md` still
returning the old 30-byte placeholder while the git tree already held the
2178-byte file. Worse, a 404 fetched before an image existed can be cached
the same way, which would make `publish.sh` time out on an image that
pushed perfectly well.

A SHA-pinned path has never been requested before and its content can never
change, so it is immune to both. `publish.sh` emits these automatically.

## Scripts

| Script                 | What it does                                                            |
| ---------------------- | ----------------------------------------------------------------------- |
| `scripts/preflight.sh` | Checks push access **before** the day's work starts. Run this first.     |
| `scripts/publish.sh`   | Copies images in, commits, pushes, and returns **verified** URLs.        |
| `scripts/verify.sh`    | Re-checks that given URLs are live images. The last gate before posting. |

### Typical use

```bash
scripts/preflight.sh || echo "GitHub host unavailable today"
scripts/publish.sh --json out/carousel-1.png out/carousel-2.png
```

`publish.sh` prints only URLs it has confirmed are serving real image bytes,
and exits non-zero if any image could not be verified. That exit code is the
signal to fall back to another host rather than publishing a broken post.

## Why verification matters

A successful `git push` does not mean the file is being served yet, and a URL
that 404s is worse than having no URL: the scheduler would hand it to Metricool
and the post would go out with a missing image. Every URL this repo emits has
been fetched and checked for a `200` plus an `image/*` content type.

## Layout

```
images/<YYYY-MM-DD>/<name>.<ext>   day-stamped image files
scripts/                           preflight, publish, verify
docs/RUNBOOK.md                    the daily automation, host fallback order
```

## Housekeeping

Images accumulate. They are small, but if the repo ever gets unwieldy, delete
old `images/<date>/` folders — nothing references them after the post is
published.
