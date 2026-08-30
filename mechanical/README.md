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

**Recommendation: 24″-class display, buttons at 38″ AFF. Kiosk 15″ W × 30″ H ×
3-5/8″ D, ≈ 23.8 lb — a 3 mm black ACM face on a solid-pine box with a tacked
MDF back, the face plate CNC-cut to order rather than fabricated on site.**

The plate's window is cut **3/16″ smaller than the monitor's lit rectangle**, so
the ACM masks the last 3/32″ of picture on every side and **no bezel is ever
visible**: illuminated LCD in a crisp routed opening, and nothing else. A 1/4″
black foam light seal behind the plate kills the shadow line. There is no
shroud. That decision, and what it costs, is in
[`fab-rev1/README.md`](fab-rev1/README.md).

## Scope

- **The enclosure.** Face plate, structural box, removable rear panel, internal
  frame, VESA mount, ventilation, service access.
- **The buttons.** BACK / HOME / NEXT cut straight into the face plate,
  centreline **38″ AFF — set by the ADA §308 reach range, and the datum the whole
  kiosk is placed from.** 30 mm anti-vandal switches at 3.50″ centres.
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

## Cut files — ready to order

**[`fab-rev1/`](fab-rev1/)** holds the face plate as DXF, generated and
self-checked by [`make-cutfiles.py`](fab-rev1/make-cutfiles.py) from
[`_p1.py`](fab-rev1/_p1.py): **P1**, one piece, **15 × 30″**, with the switch
cutouts routed straight in.

**[`cutlist/`](cutlist/)** turns the same module into a Home Depot buy plan and
a nine-crosscut cut list; **[`build-kit/`](build-kit/)** turns it into a
22-page wordless build cookbook. One source of truth, three outputs.

⚠️ **P1 is not releasable yet.** Two numbers gate it — the ⌀30.5 mm switch
cutout, and the monitor's measured lit rectangle. The box is gated on neither.

## Can we just buy an enclosure? — no

**[`ikea-build/`](ikea-build/)** — *shelved 2026-08-29,* kept for one finding
that keeps mattering: **no off-the-shelf shallow cabinet can work.** ADA §307.2
allows the kiosk **4.000″ of total projection**; the shallowest wall cabinets
made are 6¾″ deep, and picture frames shallow enough to pass are thin MDF that
will not carry 24 lb or hold a panel-mount switch. Too deep or too flimsy, with
nothing in between.

The directory also holds a costed IKEA-pine variant and a 15-page illustrated
assembly manual. Neither is the build route — **the box is ½″ Baltic birch per
sheets 300 / 301 / 302**.

## Still to produce

- `cad/` — enclosure and internal frame models (source + STEP).

- `mounting.md` — the reversible adapter, after the kiosk bench-tests clean.

## The sequence

1. **Choose the monitor** — buy or salvage, run the power-cut test, and check
   it against the three fit limits (chin ≤ 0.92″, long-edge bezel ≤ 0.60″, body
   ≤ 2.12″). Then measure the **lit rectangle**: that is what P1's window is cut
   from. ← *gate, and now it gates the face plate too*
2. Build the enclosure. Bench, no 3280 involved.
3. Install monitor, Pi, buttons, wiring, software.
4. Bench-test as a complete kiosk.
5. **Then** design and build the reversible mounting adapter.
6. Rev 2, if desired, revisits the replacement-door concept.
