# Mechanical — enclosure & mounting

**Rev 1: the kiosk is a self-contained product.** An enclosure holding the
display, the Pi, the power and the three buttons — built, wired and bench-tested
on a table, then hung on the front of the 3280's **closed factory door** by a
mounting adapter designed later, as a separate subsystem.

The 3280 is not opened, not drilled, not modified.

## Start here

- **[`rev1-standalone-kiosk.md`](rev1-standalone-kiosk.md)** — the Rev 1 design
  study. Monitor sizing, buttons, depth, construction, serviceability, and the
  recommendation.
- **[`rev1-design-study.html`](rev1-design-study.html)** — the same study as an
  **interactive review tool**. Front elevation with a live 22/24/27/32 size
  switcher, kiosk front view, button plate, side section, rear. Open it locally
  (`open mechanical/rev1-design-study.html`) or use the published link in the
  project README.

**Recommendation: 24″-class display. Kiosk ≈ 15-3/8″ W × 28-11/16″ H × 3-1/2″ D,
≈ 23 lb.**

## Scope

- **The enclosure.** Face plate, structural box, removable rear panel, internal
  frame, VESA mount, ventilation, service access.
- **The button plate.** BACK / HOME / NEXT on a separate removable plate,
  centreline 38″ AFF, 30 mm anti-vandal switches at 3.50″ centres.
- **The mounting adapter.** *Deliberately deferred.* The enclosure carries a flat
  rear interface zone and a known weight; that's all the adapter needs to inherit.
  It must be **reversible, non-destructive, removable and visually discreet** —
  this is a museum artifact, and that is a hard requirement.

## Reference — what the machine actually is

Only the **external** dimensions matter for Rev 1.

| | | Provenance |
|---|---|---|
| Cabinet overall | 71″ H × 24″ W × 34″ D | OEM 50-045R00 |
| Cabinet box, less feet | 67-7/8″ | measured, ME-1 |
| Feet | 3-1/8″ | derived |
| Outer door | ≈ 24.3″ W × 68.2″ H, ≈ 3″–71″ AFF | 3230 drawing + derived |
| Factory paint | P.E. #464 textured | 3230 drawing |

- **[`me1-findings.md`](me1-findings.md)** — the site visit. The machine has
  **two doors, not an open card cage**. Still the governing field record.
- **[`cabinet-spec-oem.md`](cabinet-spec-oem.md)** — Concurrent's published spec.
- **[`cabinet-drawings-3230.md`](cabinet-drawings-3230.md)** — Perkin-Elmer's
  mechanical drawings for the sibling 3230.
- **[`photos/`](photos/)** — site photographs.
- **[`measurement-checklist.md`](measurement-checklist.md)** — the ME-1 field
  sheet. Mostly satisfied; **C1 no longer gates anything** under Rev 1.

## Superseded for Rev 1 — kept for provenance, live again for Rev 2

Everything below designs the kiosk as a **replacement door** integrated into the
cabinet aperture. That concept is not dead — it is deferred to Rev 2 — but
nothing in Rev 1 should be built from it.

- [`monitor-selection.md`](monitor-selection.md) — the 27″ call. *Its go/no-go
  monitor criteria still apply.*
- [`display-approach-options.md`](display-approach-options.md) — hinged carrier panel.
- [`door-construction.md`](door-construction.md), [`fab/`](fab/) — the
  de-cased-panel fabrication route. **Rev 1 keeps the monitor cased.**
- [`dimensions-assumed.md`](dimensions-assumed.md),
  [`enclosure-buy-vs-build.md`](enclosure-buy-vs-build.md).
- [`drawings/`](drawings/) sheets 01–06, and [`drawings/superseded/`](drawings/superseded/).

## Still to produce

- `cad/` — enclosure, internal frame and button-plate models (source + STEP).
- Cut files for the chosen construction route, once a monitor is in hand.
- `mounting.md` — the reversible adapter, after the kiosk bench-tests clean.

## The sequence

1. **Choose the monitor** — buy or salvage, run the power-cut test. ← *gate*
2. Build the enclosure. Bench, no 3280 involved.
3. Install monitor, Pi, buttons, wiring, software.
4. Bench-test as a complete kiosk.
5. **Then** design and build the reversible mounting adapter.
6. Rev 2, if desired, revisits the replacement-door concept.
