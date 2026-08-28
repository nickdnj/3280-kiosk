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

**Placement: buttons at 38″ AFF — and the buttons are the datum.** ADA reach sets
the button height; the button height sets where the kiosk sits; everything else
follows. Kiosk bottom 34.75″, top 63.44″, screen centre 51.5″, 7.71″ of headroom
under the door. See §5.

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
| Kiosk top, buttons at 38″ AFF | 61.4″ | **63.4″** | 66.2″ | 70.2″ |
| Headroom under the 71.15″ door top | 9.71″ | **7.71″** | 4.92″ | **1.00″** |
| Highest button the geometry allows | 47.7″ | **45.7″** | 42.9″ | **39.0″** |
| Screen centre | 50.5″ AFF | **51.5″ AFF** | 52.9″ AFF | 54.8″ AFF |
| Est. total weight | ~20 lb | **~23 lb** | ~27 lb | ~34 lb |
| Min. enclosure depth | 2.7″ | **2.9″** | 3.1″ | 3.4″ |
| Pixel density (1080 px across) | 102 ppi | **93 ppi** | 82 ppi | 70 ppi |
| Panel tech at this size | IPS | **IPS** | IPS | **often VA** |

**No size has a hard geometric problem.** With the buttons at a properly-chosen
38″ (§5) all four fit the door. What separates them is how much placement freedom
each one leaves: the 22″ and 24″ can put the buttons anywhere in the comfortable
34–44″ band, the 27″ loses the top inch of it, and the **32″ loses half of it**
and keeps only an inch of headroom — inside normal build tolerance.

*Earlier drafts of this study called the 32″ a geometric failure. That was an
artefact of an arbitrary 40″ button height, not a property of the machine.*

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

**32″ is out — but not on geometry.** It fits with an inch to spare. It goes on
weight (~34 lb against a mount that has no fasteners into the artifact), on
proportion (79% of the door), on the VA-panel risk — visitors approach an exhibit
from the side, and a VA panel at 45° looks bad in exactly that situation — and on
the placement freedom it costs.

### Two go/no-go criteria carried over

1. **It must power itself back on after a mains cut.** The exhibit is on an AC
   timer (EL-4). Many monitors return to standby and need a button press —
   that's a black screen every morning. Test before committing: switched strip,
   kill power, restore, confirm it comes back with no input.
2. **Matte only.** Overhead lights and daylight; glossy panels mirror them.

---

## 5. Button placement — ADA drives the geometry

Three controls, no touchscreen: **BACK · HOME · NEXT**. They are the **datum**:
where a visitor's hand goes decides where the kiosk sits, and everything above it
follows.

### The rule

**ADA 2010 §308 puts operable parts between 15″ and 48″ above the finished
floor.** Unobstructed forward reach and unobstructed side reach give the same 48″
maximum, so the approach doesn't change the number. The 3280's face is flat and
floor-standing with no knee clearance underneath, so a visitor in a wheelchair
makes a parallel approach and reaches sideways — still 48″.

| Provision | Requirement | Where it lands here |
|---|---|---|
| §308.2.1 / §308.3.1 unobstructed reach | 15″ min, 48″ max AFF | Sets the legal window for the button centreline |
| §309.4 operable parts | one hand; no tight grasping, pinching or twisting; **≤ 5 lbf** | A 30 mm anti-vandal momentary switch is typically well under 1 lbf — **check the actuation force on the spec sheet**, some heavy industrial switches are stiff |
| §305 clear floor space | 30″ × 48″ at the control | **A museum floor requirement, not an enclosure one.** Confirm the approach is kept clear when the exhibit is sited |
| §307.2 protruding objects | leading edge above 27″ → **4″ max** projection | Constrains the mount — see below |

**48″ is a ceiling, not a target.** Designing at the maximum satisfies the letter
of the standard and serves tall standing adults. It fails seated visitors and
children, who are the people the reach range exists for.

### Rev 1 target — 38″ AFF

- **10″ below the ADA maximum.** That margin absorbs mount tolerance, floor
  variation, and the fact that nobody has built this yet.
- **At or just above elbow height for a shorter standing adult**, and a natural
  reach-down for a taller one.
- **Comfortably inside a seated visitor's reach**, and reachable by a child of
  about eight.

**It improves the screen, too.** Buttons at 38″ put the 24″ screen centre at
**51.5″**. Adult seated eye height is roughly 47–51″, so the screen is very nearly
centred on a seated visitor, while a standing adult looks down about 11° — normal
reading posture. *The ADA-driven placement is better for everyone than the 40″
this study first drew.*

### The placement math

The button centreline sits **3.25″** above the bottom of the enclosure
(1.25″ bottom border + half the 4.00″ band), and the door face runs from about
3″ to **71.15″** AFF. For a button height `B` and a kiosk height `KH`:

```
kiosk bottom = B − 3.25″
kiosk top    = B + KH − 3.25″  ≤  71.15″
             →  B ≤ 74.40″ − KH
```

| | **22″** | **24″** ✅ | **27″** | **32″** |
|---|---|---|---|---|
| Kiosk height | 26.69″ | **28.69″** | 31.48″ | 35.40″ |
| Highest button the geometry allows | 47.7″ | **45.7″** | 42.9″ | 39.0″ |
| Legal button window | 15–47.7″ | **15–45.7″** | 15–42.9″ | 15–39.0″ |
| Of the 34–44″ comfort band | all | **all** | 34–42.9″ | **34–39.0″** |
| Headroom at 38″ buttons | 9.71″ | **7.71″** | 4.92″ | **1.00″** |

### ⚠ What it costs the mount

With the buttons at 38″ the kiosk's bottom edge sits at **34.75″ AFF** — above
the 27″ threshold — so **§307.2 caps the projection into a circulation path at
4″**. The enclosure is 3.5″ deep. **That leaves half an inch for the mounting
adapter.**

**Worth asking, not worth assuming.** §307.2 exists to stop someone with a cane
walking into an object their sweep misses. The 3280 is floor-standing and
cane-detectable, and a visitor is stopped by the cabinet before the kiosk is in
reach — so the hazard the rule targets may not apply here. **That is the museum's
accessibility coordinator's call, not ours.** Design the adapter to 4″ total, and
ask.

### Hardware and layout

```
        ┌──────────── 15.37" ────────────┐
        │                                │
        │   ( BACK )  ( HOME )  ( NEXT ) │  ← 4.00" band
        │      └────3.50"────┘           │
        └────────────────────────────────┘
                 centreline 38" AFF
```

| Decision | Call | Why |
|---|---|---|
| Switch | 30 mm anti-vandal stainless, momentary, 30.5 mm hole | Big public target, industrial durability, ~$10, standard hole means any replacement fits. **Verify ≤ 5 lbf** per §309.4 |
| Spacing | 3.50″ centre-to-centre, 7.18″ overall span | Room for a legible engraved label under each; far enough apart that a mis-press is a mis-press, not a fat finger |
| Height | Centreline **38″ AFF** | See above |
| Location | **Separate removable button plate**, below the monitor | ↓ |
| Surface | Flat, in the plane of the face — **not** angled | ↓ |
| Labels | Engraved / cut into the plate, not stickers | Stickers peel; this is a 10-year exhibit |

**Consider making the three tactilely distinguishable** — different cap shapes, or
a tactile mark on HOME. Not required by §309, but it costs nothing at purchase
time and it helps visitors with low vision far more than a label does.

**Why a separate plate.** The buttons are the highest-wear part of the whole
exhibit and the only part a visitor touches. A separate plate means: switch
tolerance is decoupled from the big expensive face plate; the whole control
assembly can be built and tested on the bench with a jumper to the Pi; and if
the switch style changes you recut a $15 plate instead of the face.

**Why not angled.** An angled lower surface adds a bevelled joint, adds depth at
the bottom of the enclosure, and complicates the mount's load path. At 38″ AFF a
flat vertical face is comfortable for a standing adult. Note it as a Rev 2
option if observation says otherwise.

**No visible fasteners on the front.** The button plate is captured from behind.
Nothing on the visitor-facing surface is a screw a bored twelve-year-old can
turn.

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
- **Total projection from the door face should be ≤ 4″** (ADA §307.2 — the kiosk's
  leading edge is at 34.75″ AFF, above the 27″ threshold). The enclosure is 3.5″,
  so **the adapter's budget is 0.5″**. See §5 — whether the rule binds here is a
  question for the museum's accessibility coordinator, but design to it and ask.
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
