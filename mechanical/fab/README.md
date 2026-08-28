# Fabrication Package — Door Assembly (ME-4)

> ## ⛔ SUPERSEDED FOR REV 1
> The kiosk is no longer a replacement door integrated into the cabinet. It is a
> **self-contained enclosure surface-mounted on the closed factory door** — see
> [`../rev1-standalone-kiosk.md`](../rev1-standalone-kiosk.md) and the
> [interactive design study](../rev1-design-study.html).
> This document describes the **Rev 2** concept and is kept for provenance.
> Don't build from it.

> ## ⚠ NOT FOR ORDER YET
> Every dimension here derives from **assumed** numbers
> ([`../dimensions-assumed.md`](../dimensions-assumed.md)). The cabinet has not
> been measured and the panel has not been salvaged. This package exists so the
> design can be quoted, reviewed and sanity-checked now — **release to the shop
> only after the §6 gate clears.**

**Method:** [`../door-construction.md`](../door-construction.md) ·
**Generator:** [`generate.py`](generate.py)

> 📄 **Sharing this with a shop or a makerspace?** Send them
> **[`DRAWING-PACKAGE.md`](DRAWING-PACKAGE.md)** — the same drawings wrapped in
> project context, with the ask and the capability questions up front.

---

## 1. Order sheet

| Part | Description | Material | Thick | Qty | Operations | Finish |
|---|---|---|---|---|---|---|
| **P1** | Door face | 5052-H32 | 0.080″ | 1 | Laser cut, flat | **Raw + deburr** — painted locally |
| **P2** | Rear shroud | 5052-H32 | 0.063″ | 1 | Laser cut + **4 bends**, 90° | **Raw + deburr** — painted locally |
| **P3** | Button plate | 5052-H32 | 0.080″ | 1 | Laser cut, flat | **Black anodised** |
| **P4** | Panel retention bracket | 5052-H32 | 0.063″ | 4 | Laser cut + **1 bend**, 90° | Raw + deburr |

**On every part: deburr all edges.** This is a public exhibit — MR15.

**Do not powder coat P1, P2 or P4.** The tan is colour-matched to a 1980s
minicomputer cabinet and no standard powder palette will hit it. They get
self-etching primer and a matched topcoat locally.

### Blank sizes (for quoting / nesting)

| Part | Flat blank | Formed |
|---|---|---|
| P1 | 14.500 × 30.000 | flat |
| P2 | **19.077 × 34.577** | 14.50 × 30.00 outside × 2.40 deep tray |
| P3 | 12.800 × 4.000 | flat |
| P4 | 1.239 × 3.000 | 0.75 × 0.60 legs × 3.00 long |

---

## 2. Files

| Part | DXF (for the shop) | Drawing sheet |
|---|---|---|
| P1 | [`P1-face.dxf`](P1-face.dxf) | [`P1-face.svg`](P1-face.svg) |
| P2 | [`P2-shroud-flat.dxf`](P2-shroud-flat.dxf) | [`P2-shroud-flat.svg`](P2-shroud-flat.svg) |
| P3 | [`P3-button-plate.dxf`](P3-button-plate.dxf) | [`P3-button-plate.svg`](P3-button-plate.svg) |
| P4 | [`P4-panel-bracket.dxf`](P4-panel-bracket.dxf) | [`P4-panel-bracket.svg`](P4-panel-bracket.svg) |

DXF is **R12 ASCII, units = inches**, two layers: `CUT` and `BEND`. Closed
contours, no duplicate or overlapping geometry, no text or dimensions in the cut
data.

The drawing sheets carry a datum, overall dimensions, a **full feature schedule
with X/Y coordinates for every hole**, notes and a title block — enough to lay
the part out by hand on a mill or a drill press, not just to feed a laser. They
are for humans; **the DXF is what a machine gets.**

---

## 3. Part notes

### P1 — door face
- Screen window is cut **0.06″ under the active area overall** (0.03″/side) so
  the painted bezel covers the panel's edge transition and any backlight leak.
- Five **1.250″** button clearance holes — larger than P3's 1.125″, so P3 alone
  locates the buttons and the two plates can't fight each other.
- **No hinge holes.** The hinge lands on P2's left wall, so the visible tan face
  carries no fasteners at all.
- The satin-black bezel field and the CONCURRENT badge are **paint and an applied
  plate** — not cut features. Two M3 holes locate the badge.

### P2 — rear shroud
- Flat blank is a cross/plus: centre panel with four walls, **corners removed
  square** for bend relief. Corners close on assembly with cut aluminium angle.
- **Bend deduction used: 0.1115″/bend** (t 0.063, IR 0.063, K 0.42, 90°).
  **Shop: verify against your own bend table and regenerate the flat if it
  differs** — the formed dimensions in §1 are what must be correct, not my flat.
- Vent field: 6 × 10 slots of 1.60 × 0.20, two fields. **38.4 sq in = 8.8%** of
  the rear face. Webs 0.47″ horizontal, 0.55″ vertical. Lower field is intake,
  upper is exhaust.

### P3 — button plate
- Five 1.125″ holes at **2.719″ pitch** — 28.5 mm mounting hole for a 30 mm
  arcade body. Middle three are BACK / HOME / NEXT; outer two get blanking plugs
  (ER3 / SW-C3).
- 0.40″ of material between hole edge and plate edge.
- Mounts on the **front** of P1; the buttons pass through both plates and clamp
  them together. Four M3 fixings sit in the gaps between buttons.

### P4 — panel retention bracket
- **The slots are deliberate.** The salvaged panel's real outline is the largest
  unknown in this design; these brackets absorb the variation.
- The lip clamps the panel's **chassis edge on foam**. Never screw into a panel.

---

## 4. Regenerating with real numbers

Everything is parametric. Edit the `PARAMS` block at the top of
[`generate.py`](generate.py) and re-run:

```bash
cd mechanical/fab
python3 generate.py
```

The values most likely to change after ME-1 and EL-5:

| Param | Now | Set from |
|---|---|---|
| `active_w` / `active_h` | 11.77 / 20.92 | The real salvaged panel |
| `door_depth` / `wall_h` | 2.50 / 2.40 | C1, measured (ME-1 §C) |
| `door_w` / `door_h` | 14.50 / 30.00 | Panel outline + measured opening |
| `btn_hole_d` | 1.125 | Whatever buttons are actually salvaged |

No CAD seat needed, and the diff shows exactly what moved.

---

## 5. Shop candidates

SendCutSend · OSH Cut · Ponoko. All cut 5052, bend, deburr and anodise.
Typical turnaround ~1 week. Expect roughly **$60–150** for this package.

Laser tolerance is about ±0.005″ — an order of magnitude tighter than anything
else in this build. **The uncertainty is the salvaged panel, not the
fabrication.** That is why P4 has slots and the panel is clamped on foam rather
than dropped into a tight pocket.

---

## 6. Release gate

Do not send these files until **all** of the following are true:

- [ ] **ME-1 complete** — C1 measured at top/middle/bottom, smallest ≥ door depth + 0.5″
- [ ] **Opening measured** — confirms `door_w` / `door_h` still fit with viewing margin
- [ ] **Panel salvaged, powered-tested and de-cased** — real outline, thickness, controller footprint
- [ ] **Buttons in hand** — confirms `btn_hole_d` and body depth
- [ ] **`generate.py` PARAMS updated** and re-run against those measurements
- [ ] **Full-size cardboard mock-up held in the opening** — proportions, ADA reach,
      sightlines, swing clearance all confirmed *before* metal is cut
- [ ] Previews re-reviewed after regeneration

The cardboard step is the cheapest insurance in the project. An hour of
cardboard catches every proportion mistake that would otherwise arrive as
finished, painted aluminium.
