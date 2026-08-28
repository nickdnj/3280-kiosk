# Rev 1 — Standalone Kiosk

**The kiosk is now its own product.** A self-contained enclosure holding the
display, the Pi, the power and the three buttons — built, wired and bench-tested
on a table, then hung on the front of the 3280's closed factory door by a
mounting adapter designed *later*, as a separate subsystem.

The 3280 is not modified. It is not opened. It is not part of the build.

> **Interactive design study:** [`rev1-design-study.html`](rev1-design-study.html)
> — front elevation with a live size switcher, kiosk front view, side section,
> and the comparison tables below.

**Recommendation up front: 24″-class display (23.8″ actual), finished kiosk
≈ 15-3/8″ W × 28-11/16″ H × 3-1/2″ D, ≈ 23 lb.**

---

## 1. Why the pivot

Everything in `mechanical/` before this document designed a **replacement door**:
our panel hung on the 3280's original hinges, sized to the cabinet aperture,
gated on an unmeasured closing clearance (C1).

That design has four problems Rev 1 doesn't:

| Integrated door | Standalone kiosk |
|---|---|
| Can't be tested until it's on the machine | Bench-testable start to finish |
| Blocked on C1, still unmeasured | C1 is irrelevant |
| Reuses original hinges — load on an artifact | Load path is a designed, reversible adapter |
| Failure means the machine has no door | Failure means a box comes off the wall |

The old work is not wrong and is not deleted. It is **superseded for Rev 1** and
is a live candidate for Rev 2.

## 2. What Rev 1 keeps from the measured work

Only the **external** dimensions matter now:

| | | Provenance |
|---|---|---|
| Cabinet overall | 71″ H × 24″ W × 34″ D | OEM 50-045R00 |
| Cabinet box, less feet | 67-7/8″ | measured, ME-1 |
| Feet | 3-1/8″ | derived (71 − 67.875) |
| Outer door | ≈ 24.3″ W × 68.2″ H, ≈ 3″–71″ AFF | 3230 drawing + derived |
| Factory paint | P.E. #464 textured | 3230 drawing |

**Everything internal is out of scope** — the aperture, the inner perforated
panel, the card cage, the rack rails, C1. The kiosk sits on a flat ≈24″-wide
door face and never learns what's behind it.

**The kiosk should not be 24.3″ wide.** It is an interpretation device added to a
historic machine, and it should read that way. Subordinate, not flush.

---

## 3. Monitor size study

16:9, run portrait. Nominal sizes are marketing; the table uses **actual**
diagonals (a "24-inch" panel is 23.8″).

Bezel allowance: +0.35″ on three sides, +0.85″ chin — typical of a current thin-
bezel monitor. Face-plate reveal: 1.25″ all round. Button band: 0.75″ gap +
4.00″ band + 1.25″ bottom border.

### Screen geometry

| | **22″** | **24″** ✅ | **27″** | **32″** |
|---|---|---|---|---|
| Actual diagonal | 21.5″ | **23.8″** | 27.0″ | 31.5″ |
| Landscape active | 18.74 × 10.54 | **20.74 × 11.67** | 23.53 × 13.24 | 27.45 × 15.44 |
| Portrait active (W × H) | 10.54 × 18.74 | **11.67 × 20.74** | 13.24 × 23.53 | 15.44 × 27.45 |
| Portrait outline, cased | 11.74 × 19.44 | **12.87 × 21.44** | 14.44 × 24.23 | 16.64 × 28.15 |

### Resulting kiosk

| | **22″** | **24″** ✅ | **27″** | **32″** |
|---|---|---|---|---|
| Finished kiosk W × H | 14.24 × 26.69 | **15.37 × 28.69** | 16.94 × 31.48 | 19.14 × 35.40 |
| Share of 24.3″ door width | 59% | **63%** | 70% | 79% |
| Share of 71″ cabinet height | 38% | **40%** | 44% | 50% |
| Kiosk top, buttons at 40″ AFF | 63.4″ | **65.4″** | 68.2″ | **72.2″ ✗** |
| Screen centre | 52.5″ AFF | **53.5″ AFF** | 54.9″ AFF | 56.8″ AFF |
| Est. total weight | ~20 lb | **~23 lb** | ~27 lb | ~34 lb |
| Min. enclosure depth | 2.7″ | **2.9″** | 3.1″ | 3.4″ |
| Pixel density (1080 px across) | 102 ppi | **93 ppi** | 82 ppi | 70 ppi |
| Panel tech at this size | IPS | **IPS** | IPS | **often VA** |

**The 32″ is the only one with a hard geometric problem.** At a comfortable 40″
button height its top lands at 72.2″ — an inch above the door. It only fits if
the buttons drop to ~38″ AFF, and it then covers half the machine's face.

### Readability check

The governing constraint is cap height, not resolution. Comfortable reading at
6 ft wants roughly **0.35″ cap height** — about a 0.5″ em.

On the 24″ (20.74″ tall across 1920 px) that's a **46 px** body size, giving
~47 characters per line at 1080 px wide. That is a good measure for the 3–5
bullets the content bar allows. The 22″ lands at ~42 characters — workable, but
it starts to constrain the writing.

**Resolution is not a differentiator.** All four are legible at 3–6 ft; a 1080p
24″ at 93 ppi is crisp at arm's length and dead sharp at exhibit distance. Don't
pay for 1440p unless it's what the salvage pile offers.

---

## 4. Recommendation — 24″

**Proportion is the deciding argument.** At 15.4″ wide the kiosk is 63% of the
door — clearly an added object, clearly not trying to be the machine. The 27″ at
70% and the 32″ at 79% start to read as a monitor wearing a cabinet, which is
exactly the impression a museum exhibit should not give.

**Weight is the second argument, and it may be the more important one.** The
mounting adapter is undesigned and unconstrained. It has to carry the kiosk off
a hollow sheet-metal door **without a single fastener into the artifact**.
23 lb of strap-and-bracket load is a solvable problem. 34 lb is where you start
having to transfer load to the cabinet frame, and the mount stops being simple.

**Availability.** 24″ 1080p IPS is the highest-volume monitor ever made. It's
the most likely thing in the warehouse, the cheapest thing to buy, and the
easiest thing for a docent to replace in 2033 without calling anyone.

**Depth.** 2.9″ minimum vs. 3.1″ for the 27″ — small, but it compounds with the
mount, and every eighth of an inch the kiosk stands off the machine is visible.

### If a 27″ falls out of the salvage pile

Take it. It is not a bad answer — it's a *slightly worse* answer, and the
enclosure design is parametric enough that switching costs one face plate. The
27″ upgrades the screen centre to a slightly better 54.9″ and buys real estate
for images. Just budget the extra 4 lb into the mount.

**22″ is the fallback if the mount turns out to be harder than expected.**
20 lb is genuinely easy to hang.

**32″ is out.** Height failure at a comfortable button position, the weight, and
the VA-panel risk — visitors approach an exhibit from the side, and a VA panel
at 45° looks bad in exactly that situation.

### Two go/no-go criteria carried over

1. **It must power itself back on after a mains cut.** The exhibit is on an AC
   timer (EL-4). Many monitors return to standby and need a button press —
   that's a black screen every morning. Test before committing: switched strip,
   kill power, restore, confirm it comes back with no input.
2. **Matte only.** Overhead lights and daylight; glossy panels mirror them.

---

## 5. Button layout

Three controls, no touchscreen: **BACK · HOME · NEXT**.

```
        ┌──────────── 15.37" ────────────┐
        │                                │
        │   ( BACK )  ( HOME )  ( NEXT ) │  ← 4.00" band
        │      └────3.50"────┘           │
        └────────────────────────────────┘
                  buttons at 40" AFF
```

| Decision | Call | Why |
|---|---|---|
| Switch | 30 mm anti-vandal stainless, momentary, 30.5 mm hole | Big public target, industrial durability, ~$10, standard hole means any replacement fits |
| Spacing | 3.50″ centre-to-centre, 7.00″ overall span | Room for a legible engraved label under each; far enough apart that a mis-press is a mis-press, not a fat finger |
| Height | Centreline **40″ AFF** | Mid-band of the 15″–48″ ADA reach range, natural for a standing adult, still reachable seated |
| Location | **Separate removable button plate**, below the monitor | ↓ |
| Surface | Flat, in the plane of the face — **not** angled | ↓ |
| Labels | Engraved / cut into the plate, not stickers | Stickers peel; this is a 10-year exhibit |

**Why a separate plate.** The buttons are the highest-wear part of the whole
exhibit and the only part a visitor touches. A separate plate means: switch
tolerance is decoupled from the big expensive face plate; the whole control
assembly can be built and tested on the bench with a jumper to the Pi; and if
the switch style changes you recut a $15 plate instead of the face.

**Why not angled.** An angled lower surface adds a bevelled joint, adds depth at
the bottom of the enclosure, and complicates the mount's load path. At 40″ AFF a
flat vertical face is comfortable for a standing adult. Note it as a Rev 2
option if observation says otherwise.

**No visible fasteners on the front.** The button plate is captured from behind.
Nothing on the visitor-facing surface is a screw a bored twelve-year-old can
turn.

---

## 6. Enclosure depth

**Target: 3.5″. Floor: 3.0″. 2.5″ is not realistic.**

Side-section stack, front to back:

```
  0.50"   face plate (1/2" ply, or 1/8" ACM on a 3/8" sub-frame)
  0.10"   bezel clearance
  1.80"   monitor body at its thickest (VESA boss / driver hump)
  0.60"   air + service gap
  0.50"   rear panel
 ───────
  3.50"   finished depth
```

### What actually forces the depth

1. **The monitor's thickest point — 1.6″ to 2.3″.** Non-negotiable, and the only
   real number in the stack. This is why the enclosure gets deeper with screen
   size even though the panel itself doesn't.
2. **Cable bend at the monitor's connectors — 0.75″ to 1.75″.** This is the one
   you can design away, and it's the difference between 3.5″ and 4.5″. Route the
   HDMI and DC leads **downward into the button bay** instead of straight back,
   and use right-angle plugs. The button bay has 4″ of free depth in a 5″-tall
   band and nothing in it but the Pi.
3. **Face plate + rear panel — 1.0″ combined.** Reducible to ~0.4″ with ACM, at
   the cost of stiffness.
4. **The mounting adapter**, TBD, adds to the *stand-off*, not the enclosure.

### What does NOT force the depth

**The Raspberry Pi.** A Pi 4 is 0.65″ tall. It does not live behind the monitor —
it lives in the button bay below it, on a slide-out tray, where there is 4″ of
depth doing nothing. Anyone who designs this enclosure around fitting a Pi behind
the panel will build it an inch too deep.

**The monitor stays cased.** De-casing buys ~1.2″ of depth and costs the panel's
EMI shielding, its thermal design, its warranty, its power board's enclosure, and
any hope of a volunteer replacing it. Not worth it. This reverses the earlier
de-cased-panel route in [`door-construction.md`](door-construction.md).

| Depth | Verdict |
|---|---|
| 2.5″ | **No.** Requires a sub-1.4″ monitor, a 1/8″ face, and zero service gap. |
| 3.0″ | Achievable at 22–24″ with a slim monitor, right-angle cables, down-routing. No margin. |
| **3.5″** | **The design target.** Works at 22/24/27 with a normal monitor and 0.6″ of service air. |
| 4.0″ | Needed for 32″, or for any monitor with a rear-facing connector cluster and straight cables. |

---

## 7. Construction approaches

| | **A — CNC Baltic birch** | **B — Ply box + applied face** ✅ | **C — Modified commercial** |
|---|---|---|---|
| What it is | 1/2″ Baltic birch, CNC-cut, rabbeted, sprayed satin graphite | 3/8–1/2″ ply structural box, face plate in ACM or HPL, bonded | Digital-signage / instrument enclosure, cut for the panel |
| Fabrication | Moderate — CNC + a spray setup. **The finish is the hard part.** | Moderate — two stages, but each is easy. Face plate CNC's flat, box is simple joinery | Low *if* something fits; high if not |
| Material cost | $80–140 | $120–200 | $150–400 |
| Weight (24″) | ~13 lb enclosure | ~15 lb enclosure | 30 lb+ in steel; light in ABS |
| Finish quality | Good sprayed, poor brushed. Ply edges telegraph | **Best.** Factory-flat laminate, no spray booth, no grain to fill | Factory |
| Serviceability | Excellent — but **use threaded inserts**, not screws into ply edge | Excellent, same caveat. Face is bonded, so button work goes through the back | Usually good |
| Museum read | Honest, repairable, slightly craft | **Purpose-built exhibit component** | Risks reading as generic industrial kit |

**Recommend B.** The single biggest risk in a volunteer-built enclosure is the
**finish** — a well-built box with a brushed-lacquer face still looks homemade,
and that is the exact failure mode the brief names. Approach B removes the finish
from the critical path entirely: the visible surface arrives already flat and
already durable, and the volunteers build a plywood box behind it, which is a
thing any woodworker can do well on the first try.

**A is the fallback** if nobody at CDL can source or bond sheet facing. It's a
good enclosure — it just puts the project's appearance on the line at the spray
stage.

**C fails on aspect ratio.** Nothing off the shelf is 15″ × 29″ × 3.5″ portrait.
Everything close is either a landscape signage housing or a deep NEMA box. Worth
ten minutes of searching, not worth designing around.

---

## 8. Serviceability

Everything must be replaceable by a museum volunteer with a screwdriver.

| Part | How it comes out |
|---|---|
| **Rear panel** | Captive thumbscrews or 1/4-turn fasteners into threaded inserts. No loose hardware to drop inside a museum artifact. |
| **Monitor** | On a VESA 100 plate bolted to the internal frame. Rear panel off → four bolts → monitor out backwards. **The face plate never comes off.** |
| **Raspberry Pi** | Slide-out tray in the button bay. Unplug two, slide out. |
| **Buttons** | Button plate is captured from behind. Rear panel off → plate drops in. Switches are standard 30.5 mm hole. |
| **Power** | One appliance inlet at the bottom rear. One cord leaves the kiosk. |

**The rule:** nothing that fails routinely should require touching the face plate
or the mount. The kiosk should never have to come off the 3280 for service.

---

## 9. Attachment interface — deliberately not designed

The rear of the enclosure carries a flat, unobstructed **mounting interface
zone**, marked on the drawings as:

> **REVERSIBLE 3280 MOUNTING ADAPTER — DESIGN TBD**

Constraints it will have to satisfy, recorded now so the enclosure doesn't
foreclose them:

- **Reversible, non-destructive, removable, visually discreet** (MR2). No holes,
  no cuts, no permanent modification to the door or the cabinet.
- Must carry ~23 lb in shear plus the moment from a ~1.75″ centre-of-mass
  stand-off, with a safety factor for someone leaning on it.
- Candidates, unevaluated: edge brackets hooking the door's return flange;
  compression straps around the cabinet; a full-door backing plate captured at
  top and bottom; clamps on the door's existing hardware.
- Anything that loads the original **hinges** needs to be checked against them.

**Deliberately deferred.** The enclosure's job is to have a flat back and a known
weight. That is enough for the adapter to be designed against later, and
designing it now would be guessing.

---

## 10. Sequence

1. **Choose the monitor** — buy or salvage, run the power-cut test. ← *gate*
2. **Build the enclosure** — bench, no 3280 involved.
3. **Install** monitor, Pi, buttons, wiring, software.
4. **Bench-test as a complete kiosk** — run it for a week on a table.
5. **Then** design and build the reversible mounting adapter.
6. **Rev 2**, if desired, revisits the replacement-door concept.

Steps 1–4 have no dependency on the 3280 at all. **C1 no longer gates anything**,
and neither does the door height, the aperture, or the inner panel.

---

*Recorded 2026-08-28. Supersedes for Rev 1: the 27″ call in
[`monitor-selection.md`](monitor-selection.md), the hinged-carrier route in
[`display-approach-options.md`](display-approach-options.md), the de-cased-panel
route in [`door-construction.md`](door-construction.md) and [`fab/`](fab/), and
drawings 01–06 in [`drawings/`](drawings/). Those describe the Rev 2 concept.*
