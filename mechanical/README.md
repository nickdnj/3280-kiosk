# Mechanical — enclosure & mounting

The physical build: the hinged portrait display panel, the three-button control
plate, and how the whole assembly integrates with the real Concurrent 3280
cabinet so a docent can **swing the screen open to reveal the card cage behind
it**.

## Scope

- **Hinged display panel.** The portrait screen mounts on a hinge over the
  cabinet opening; opening it exposes the interior. Hinge, latch/detent, cable
  strain relief across the hinge, and safe travel/stop.
- **Button plate.** Mounting and spacing for BACK / HOME / NEXT, reachable and
  ADA-considerate, labeled to match the on-screen controls.
- **Integration with the 3280.** Brackets/adapters that attach to the original
  cabinet **without damaging the artifact** — reversible, non-destructive
  mounting is a hard requirement (this is a museum piece).
- **Thermal & access.** Ventilation for the SBC/display and service access.

## What's here now

> **Everything below is drawn against *assumed* dimensions.** The cabinet has not
> been measured yet. Do not cut material against these numbers.

- **[`dimensions-assumed.md`](dimensions-assumed.md)** — the v0 dimension set,
  where each number came from, and how confident we are in it.
- **[`measurement-checklist.md`](measurement-checklist.md)** — the ME-1 field
  sheet. Print it or open it on a phone at the museum; fill the blanks in place.
- **[`drawings/`](drawings/)** — dimensioned SVGs (render inline on GitHub):
  - [`01-cabinet-front-elevation.svg`](drawings/01-cabinet-front-elevation.svg) — door size and placement, ADA button height
  - [`02-door-assembly.svg`](drawings/02-door-assembly.svg) — every door face dimension, weight budget
  - [`03-plan-section-clearance.svg`](drawings/03-plan-section-clearance.svg) — depth budget, swing envelope, **the C1 clearance risk**
  - [`04-mount-candidates.svg`](drawings/04-mount-candidates.svg) — three no-drill mounting options
  - [`05-door-exploded.svg`](drawings/05-door-exploded.svg) — door assembly stack, depth budget, thermal path
  - [`06-option-comparison.svg`](drawings/06-option-comparison.svg) — **all four display approaches side by side**
- **[`fab/`](fab/)** — the fabrication package: order sheet, laser-cut DXFs,
  review previews, and the parametric generator that rebuilds them all from one
  PARAMS block, plus [`DRAWING-PACKAGE.md`](fab/DRAWING-PACKAGE.md) — the
  shareable version for a shop or makerspace. **Not for order until the release
  gate clears.**
- **[`cabinet-spec-oem.md`](cabinet-spec-oem.md)** — Concurrent's own published
  cabinet spec (71″ × 24″ × 34″) from the 1989 product overview on bitsavers.
- **[`me1-findings.md`](me1-findings.md)** — ⚠️ **read this first.** Site visit
  2026-08-26: the machine has two doors, not an open card cage. Changes the
  mounting design and part of the concept.
- **[`display-approach-options.md`](display-approach-options.md)** — **the
  top-level open decision.** Custom door vs. bought enclosure vs. a cased monitor
  VESA-mounted to a hinged carrier panel. Read this first.
- **[`enclosure-buy-vs-build.md`](enclosure-buy-vs-build.md)** — is there an
  off-the-shelf enclosure we could buy and modify instead? Open decision, gated
  on the measured clearance.
- **[`door-construction.md`](door-construction.md)** — ME-4 build spec: laser-cut
  5052 aluminium (outsourced), parts P1–P4, assembly stack, thermal, finish, and
  what's still blocked before anything can be ordered.

## Still to produce

- `cad/` — enclosure, hinge, bracket, and button-plate models (source + STEP).
- `drawings/` — cut files once dimensions are measured.
- `mounting.md` — how it fastens to the cabinet, reversibly, and the fit check.
- `photos/` — the ME-1 site photos.

## The one number that matters most

**C1** — the clear depth from the cabinet's front face to the frontmost thing
inside the opening. The door needs `C1 ≥ door depth + 0.5"`, and the design is
drawn at a 2.5″ door depth. If C1 measures under 3.0″, the door redesigns. Measure
it at the top, middle and bottom of the opening and design to the smallest.
