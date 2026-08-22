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
| Electronics | `electronics/` | v0 BOM + salvage recon list |
| Mechanical | `mechanical/` | v0 assumed dimensions + drawings + ME-1 field sheet |

Team: **Software Project Team**, provisioned by AgentArchitect (2026-08-22).

## Going to the museum or the warehouse?

Field materials, all phone-readable:

- **[Measurement field sheet](mechanical/measurement-checklist.md)** — the ME-1
  checklist. Fill the blanks on site.
- **[Salvage shopping list](electronics/salvage-recon.md)** — what to scavenge,
  with monitor acceptance criteria and the powered test to run before de-casing.
- **[Assumed dimensions + drawings](mechanical/dimensions-assumed.md)** — the
  design as currently drawn, and exactly which numbers are guesses.

> Everything mechanical is drawn against **assumed** dimensions taken from the
> concept render. Nothing has been measured. Don't cut material against it.

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
