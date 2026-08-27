# Perkin-Elmer Cabinet Drawings — Model 3230 (sibling machine)

**Source:** Perkin-Elmer, *Model 3230 Processor Installation and Maintenance
Manual*, **47-004 R21 (1982)**, Chapter 3 "Mechanical Configuration", figures
3-1 through 3-5 (book pages 3-1 … 3-7).
[bitsavers](https://bitsavers.org/pdf/interdata/32bit/3230/47-004R21_3230_Maint_1982.pdf)
· [OCR text](https://archive.org/stream/bitsavers_interdata30Maint1982_46790039/47-004R21_3230_Maint_1982_djvu.txt)

> ⚠️ **This is the 3230, not the 3280.** The 3230 is a **56″ rack**; our machine
> is a **71″ cabinet** ([`cabinet-spec-oem.md`](cabinet-spec-oem.md)). Same
> manufacturer, same era, same design language — but three years earlier and a
> different size class. Treat everything here as **strong evidence about the
> family**, and confirm anything load-bearing against the real machine.

Chapter 3 opens: *"Figures 3-1 through 3-4 illustrate the mechanical components
of a typical Perkin-Elmer digital system. Dimensions and mounting information are
provided for the system cabinet, chassis support rails, side skins, and doors."*
This is the closest thing to a cabinet spec that exists in the archive.

---

## 1. The finding that matters most

### It's a 19-inch EIA rack

Figure 3-1, *Basic Rack Structure*:

> **PANEL SPACE 1292 mm (50.87″) × 482.6 mm (19″)**
> **711.2 mm (28″) UPRIGHT TO UPRIGHT**

**482.6 mm is exactly 19.00″ — standard EIA-310 panel width.** 50.87″ of panel
space is ~29U.

**This revives mount candidate A.** If the 3280 carries the same rack standard
— and there is no reason for Concurrent to have abandoned it between 1982 and
1985 — then our fixed frame can be an **off-the-shelf 19″ rack panel** bolted to
the existing uprights. Standards-based, no drilling, fully reversible.

**Confirm on the machine:** put a rack screw against an upright and see if it
threads. That single test, already item B4 on the
[field sheet](measurement-checklist.md), now has a documented expectation behind it.

---

## 2. The doors — Figure 3-4, "Doors and Latches"

| Property | Value |
|---|---|
| **Full door** part no. | **13.045 F01** — *"use for all front & rear door covers when peripheral cutouts are not req'd"* |
| **Height** | **54.32″ (1380 mm)** |
| **Width** | **24.3″ (617 mm)** |
| Mag-tape variant | 13.045 F02, with a cutout; 2″ (51 mm) band above it |
| Latching | **Spring latch ×2 per door**, at the top; #6-32 × 3/8″ PHPS, #6 split + #6 flat, 2 per latch |
| Sealing | **Adhesive-backed foam rubber seal/gasket, all around, inside the rib** |
| Construction | Louvered panel with a perimeter rib frame — **vertical louvers** |

> *"The front and rear doors are released by depressing the two spring latches at
> the top. The same door is used for all configurations with appropriate cutouts."*

### Two things worth sitting with

**The 3230 door is a lift-off cover, not a hinged door.** Latches at the top,
pilot holes and adjustment screws at the bottom (Figure 3-1). **Your photos show
the 3280's outer door on hinges** — so the 3280 changed, or has both. Either way:
*a door designed to come off is the most reversible mounting point imaginable.*
Removing it and hanging our panel in its place touches nothing structural.

**The door is 24.3″ wide on a 24″ cabinet** — it overlaps the frame by ~0.15″
per side, as a cover door should. Your tape read of ~23–24″ across the outer door
is consistent.

**Door height does not transfer.** 54.32″ suits a 56″ rack. The 3280's 71″
cabinet needs a taller door, a stacked pair, or a door plus filler panels. Your
[`me1-vertical-48.jpg`](photos/me1-vertical-48.jpg) reading of ~48″ may well be
the real 3280 door or aperture — **that's one of the three numbers to confirm.**

---

## 3. Paint and materials — Figure 3-1 note block

> **MATL: CRS .104 THK (STRUCTURE)**
> **SIDE SKINS CRS .047 THK**
> **PAINT: P.E. #464 TEXTURED**

**"P.E. #464 textured" is the factory paint specification.** That is a real lead
for MR13 (colour match). It won't be a currently available product, but it is a
named reference a paint shop can work from, and it confirms the finish is
**textured**, not smooth — which matters more than the hue for making a new panel
look like it belongs. A smooth tan panel next to textured tan will read wrong even
at a perfect colour match.

Structure is **cold-rolled steel 0.104″** (≈12 ga); skins **0.047″** (≈18 ga).

---

## 4. Cooling — §3.2 and Figure 3-5

- Blower package at the **bottom**, **450 CFM @ 0″ H₂O**, 230 V AC
- Air drawn from the bottom of the rack (room ambient or raised floor)
- Distributed by an **internal plenum along the RIGHT side of the cabinet opening,
  viewed from the front**
- The plenum has **five removable covers**, stacked vertically
- **Two cover types: solid and perforated.** Solid where there is no card file;
  perforated where there is an operating card file. *"In the Model 3230,
  perforated covers are factory installed."*
- Washable filter in the blower base, reachable from the front once the cover door
  is off

**This may re-read your photos.** The rainbow zinc-plated perforated panels could
be **plenum covers** rather than a second door — though the piano-hinged panel you
photographed looks larger than a side plenum cover, and the diamond-mesh EMI
gasket visible on the frame in
[`me1-opening-width-tape.jpg`](photos/me1-opening-width-tape.jpg) suggests the
3280 added a proper **EMI screen door** for FCC compliance, which the 1982 machine
would not have needed. Worth resolving on the machine.

---

## 5. Internal zones — Figure 3-2

Rear view, top to bottom: **203 mm (8″)** · **908 mm (35.75″)** · **178 mm (7″)**
— totalling 50.75″, matching the 50.87″ panel space.

Front view names: consolette (top), power subsystem control panel, support rails
for all chassis, plenum air system down the right, AC distribution panel, blower
assembly at the bottom.

Compare with the 3280's stack in [`cabinet-spec-oem.md`](cabinet-spec-oem.md) §2 —
power/fan on top, chassis in the middle, fan at the bottom. Same idea, taller box.

---

## 6. Referenced drawings we do *not* have

The manual cites drawings by number that would settle everything:

| Drawing | What it is |
|---|---|
| **01-142F01** | *"For further details of the Model 3230 system cabinet, refer to 01-142F01 included in this manual"* — the cabinet detail drawing |
| **01-142R02C03** | Assembly Drawings, System Cabinet |
| 13.045 F01 / F02 | The door part numbers |

`01-142F01` is the one to want. It is listed as *included in this manual*, so it
may be among the fold-outs in the 621-page scan — worth a targeted look if door
geometry becomes the blocker.

---

## 7. What this changes for us

| | Before | Now |
|---|---|---|
| Mount candidate A (19″ rack) | Speculative | **Documented for the family** — confirm with a rack screw |
| Paint match (MR13) | "match the tan somehow" | Named spec **P.E. #464 textured** — and texture matters |
| Door removal | Assumed reversible | **Doors are designed to come off** — latches, pilot holes, adjustment screws |
| Door size | Unknown | 3230 is 54.32 × 24.3; the 3280's is one of your three unconfirmed readings |
| Perforated panel | "inner door" | Possibly plenum covers, possibly an EMI door — resolve on the machine |

**Still not answered: C1.** No drawing in this manual gives outer-door-plane to
inner-panel clearance. It stays a tape measurement.

---

*Recorded 2026-08-27 from the 1982 Perkin-Elmer manual. Sibling-model evidence —
the machine in the warehouse remains the authority.*
