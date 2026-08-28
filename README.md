# 3280 Kiosk

An interactive exhibit kiosk for the Vintage Computer Federation museum's
**Concurrent 3280**. A portrait display in a self-contained enclosure, mounted on
the front of the machine's closed factory door. Driven by **three physical
buttons only: BACK / HOME / NEXT. No touchscreen.**

**Rev 1 is a standalone product.** The kiosk is built, wired and bench-tested on
a table before it ever touches the 3280; the reversible mounting adapter is a
separate subsystem designed after that. The machine is not opened, not drilled,
not modified. → **[Rev 1 design study](mechanical/rev1-standalone-kiosk.md)** ·
**[interactive version](mechanical/rev1-design-study.html)**

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
| Electronics | `electronics/` | v0 BOM + salvage recon list |
| Mechanical | `mechanical/` | **Rev 1 standalone-kiosk design study** (24″ display, ~15.4 × 28.7 × 3.5″) |

Team: **Software Project Team**, provisioned by AgentArchitect (2026-08-22).

## Going to the museum or the warehouse?

Field materials, all phone-readable:

- **[Measurement field sheet](mechanical/measurement-checklist.md)** — the ME-1
  checklist. Fill the blanks on site.
- **[Salvage shopping list](electronics/salvage-recon.md)** — what to scavenge,
  with monitor acceptance criteria and the powered test to run before de-casing.
- **[Rev 1 design study](mechanical/rev1-standalone-kiosk.md)** — the current
  mechanical design, drawn against measured cabinet dimensions.

> The cabinet is measured (71 × 24 × 34, box 67-7/8″). Monitor outlines, weights
> and thicknesses in the design study are **estimates from typical current
> product**, not measured units — confirm against the actual monitor before
> cutting anything.

## Planning docs

`docs/00-project-brief.md` → `01-prd.md` → `02-architecture.md` →
`03-ux.md` → `04-dev-plan.md`. Work is tracked as
[GitHub issues](https://github.com/nickdnj/3280-kiosk/issues) across five
milestones.

## Start

```bash
claude
```

New here? Read `docs/00-project-brief.md`. The PRD → architecture → UX → dev-plan
flow is complete; work is now execution against the issue list.

## Run the app locally

```bash
cd src/kiosk-app
python3 build-app.py          # rebuild index.html from assets/
open index.html               # or serve the folder
```
