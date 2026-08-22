# 3280 Kiosk

An interactive exhibit kiosk built into the Vintage Computer Federation museum's
**Concurrent 3280**. A portrait display mounted on a hinge over the card cage —
swing it open and the real hardware is behind it. Driven by **three physical
buttons only: BACK / HOME / NEXT. No touchscreen.**

> ⚠️ **This is a concept — our guiding light, not a shipped product.** Everything
> here describes where we're driving to. The on-screen app is a *concept-review
> build* (cabinet imagery is AI concept art); the hardware folders are still
> empty. Treat every artifact as "the target," not "the deliverable," until the
> team says otherwise.

This repo spans three disciplines:

| Area | Path | Status |
|---|---|---|
| On-screen app | `src/kiosk-app/` | Concept build — clickable, imagery is concept art |
| Button/kiosk controller | `src/controller/` | Concept / placeholder |
| Electronics | `electronics/` | Concept / placeholder |
| Mechanical | `mechanical/` | Concept / placeholder |

Team: **Software Project Team**, provisioned by AgentArchitect (2026-08-22).

## Start

```bash
claude
```

New here? Read `docs/00-project-brief.md`, then say **"let's write the PRD"** —
the team runs requirements → architecture → UX → dev plan → build.

## Run the app locally

```bash
cd src/kiosk-app
python3 build-app.py          # rebuild index.html from assets/
open index.html               # or serve the folder
```
