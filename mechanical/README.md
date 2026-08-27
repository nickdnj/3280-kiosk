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

> **Measured 2026-08-26.** Cabinet dimensions are real; the door aperture is
> derived from a uniform frame offset. **C1 — the closing clearance — is still
> unmeasured**, and it is the last gate before anything gets built.

### Start here
- **[`me1-findings.md`](me1-findings.md)** — the site visit. **The machine has two
  doors, not an open card cage.** This changed the design.
- **[`monitor-selection.md`](monitor-selection.md)** — **27″ IPS 1440p**, validated
  against the measured cabinet. 24″ is undersized.
- **[`drawings/`](drawings/)** — the full set, all rebuilt to measured geometry
  from one shared block in [`make-drawings.py`](drawings/make-drawings.py).

### Reference — what the machine actually is
- **[`cabinet-spec-oem.md`](cabinet-spec-oem.md)** — Concurrent's published spec:
  **71″ × 24″ × 34″**, and the internal stack.
- **[`cabinet-drawings-3230.md`](cabinet-drawings-3230.md)** — Perkin-Elmer's
  mechanical drawings for the sibling 3230: **19″ EIA rack confirmed**, door part
  numbers, and the factory paint spec (**P.E. #464 textured**).
- **[`photos/`](photos/)** — site photographs.

### Open decisions
- **[`display-approach-options.md`](display-approach-options.md)** — cased monitor
  on a hinged carrier panel (Option C) is the recommendation.
- Recessed vs. proud — see [drawing 06](drawings/06-recessed-vs-proud.svg). This
  one is for the docents, not the engineers.

### Field materials
- **[`measurement-checklist.md`](measurement-checklist.md)** — the ME-1 field
  sheet. **C1 and the door height are what's left.**

### Superseded — kept for provenance, don't build from these
- [`dimensions-assumed.md`](dimensions-assumed.md) — the pre-measurement guesses.
- [`door-construction.md`](door-construction.md), [`fab/`](fab/) — the de-cased-panel
  fabrication route, obsolete now that we're keeping the monitor whole.
- [`enclosure-buy-vs-build.md`](enclosure-buy-vs-build.md) — moot: the cabinet
  supplies the enclosure.
- [`drawings/superseded/`](drawings/superseded/).

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
