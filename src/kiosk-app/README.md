# Kiosk App — on-screen UI

The portrait touch-free display software for the Concurrent 3280 exhibit kiosk.
Operated by **three physical buttons only** (BACK / HOME / NEXT) — there is no
touchscreen. A docent (or visitor) steps through a short deck of screens: the
machine's story, what it did, and a look inside the real card cage.

## What's here

- `index.html` — the built, fully self-contained app (all images inlined as
  base64 data URIs). This is the file the kiosk actually loads. ~4.8 MB.
- `build-app.py` — the builder. Reads the raw assets under `assets/`, inlines
  them, and writes `index.html` by token replacement. **Edit content here and
  rebuild — do not hand-edit `index.html`.**
- `assets/` — source images (renders, poster art, montage photos, logos) at
  web resolution, before inlining.

## Build

```bash
cd src/kiosk-app
python3 build-app.py      # regenerates index.html from assets/ + the CARDS deck
```

## Origin

Started life as a shareable **concept-review Artifact** (published to
claude.ai/code) so the docent team — led by Rick Lewis — could react to the
idea before any hardware existed. Rick's review shaped the current content spec:
cut copy to ~30%, 3–5 short bullets per screen, a strong graphic, big
sans-serif type readable at 3–6 ft, and technical facts contextualized for a
general audience. See `docs/` for the full brief.

## Next (for the software team)

- Decouple content from the single HTML blob (data file + template) so non-devs
  can edit screens.
- Kiosk hardening: fullscreen, no cursor, no scrollbars, disable gestures/context
  menu, auto-restart on crash, attract-loop / idle reset to HOME.
- Wire the on-screen nav to real GPIO buttons via `../controller/`.
- Optional anonymous usage tracking (Rick's ask) — which screens get viewed.
