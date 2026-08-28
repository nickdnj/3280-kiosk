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
≈ 15-3/8″ W × 28-11/16″ H × 3-1/4″ D, ≈ 23 lb.**

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
4″**. With the recommended 3 mm ACM face (§7) the enclosure is 3.25″ deep,
**leaving 0.75″ for the mounting adapter** — a plywood face instead would cut
that to 0.5″.

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
| Location | **Cut straight into the face plate**, below the monitor | ↓ |
| Surface | Flat, in the plane of the face — **not** angled | ↓ |
| Labels | Engraved / cut into the plate, not stickers | Stickers peel; this is a 10-year exhibit |

**Consider making the three tactilely distinguishable** — different cap shapes, or
a tactile mark on HOME. Not required by §309, but it costs nothing at purchase
time and it helps visitors with low vision far more than a label does.

**Why they're in the face plate, not on their own plate.** An earlier version put
them on a separate plate behind an aperture, as insurance against getting the
switch cutout wrong. **That was over-engineered.**

*Stiffness was the real cost.* Cutting both a 12.17 × 21.24 window **and** an
11.87 × 3.00 aperture out of one 3 mm sheet left a **1.35″ web** as the only
material joining the side rails below the screen. One piece leaves **2.25″ above
the buttons and 2.65″ below**. It also meant a second part on the invoice, six
more holes, a second set of cleats, and a plate to align square in an aperture.

*And the wear argument didn't hold.* Anti-vandal switches are rated for millions
of cycles, and when one fails you replace **the switch**, through the same hole.
The plate only needs replacing if the hole itself is damaged, which essentially
doesn't happen.

The insurance is better bought by **confirming the cutout before ordering** than
by designing around not knowing it.

**A cleat row sits between the window and the buttons** — three fixings onto a
plywood rail, so the panel takes the press load instead of flexing every time
somebody pushes a button. It clears the switch bodies, which stand about an inch
proud behind the plate.

**Why not angled.** An angled lower surface adds a bevelled joint, adds depth at
the bottom of the enclosure, and complicates the mount's load path. At 38″ AFF a
flat vertical face is comfortable for a standing adult. Note it as a Rev 2
option if observation says otherwise.

**No visible fasteners on the front.** The face plate is captured from behind.
Nothing on the visitor-facing surface is a screw a bored twelve-year-old can
turn.

## 6. Enclosure depth

**Target: 3.25″ with the recommended 3 mm ACM face (§7). Floor: 3.0″.
2.5″ is not realistic.** A plywood face instead makes it 3.5″.

Side-section stack, front to back:

```
  0.118"  face plate — 3 mm ACM on internal cleats
  0.10"   bezel clearance
  1.80"   monitor body at its thickest (VESA boss / driver hump)
  0.73"   air + service gap
  0.50"   rear panel
 ───────
  3.25"   finished depth      (3.50" if the face is 1/2" plywood)
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
3. **Face plate + rear panel.** A 3 mm ACM face and a 1/2″ ply rear come to 0.62″
   together; a plywood face makes it 1.0″ — **and that 3/8″ comes straight out of
   the mounting adapter's budget.**
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
| **3.25″** | **The design target**, with a 3 mm ACM face. Works at 22/24/27 with 0.7″ of service air, and leaves **0.75″ for the mount** under the 4″ cap. |
| 3.5″ | What a plywood face costs you. Still fine — the mount's budget drops to 0.5″. |
| 4.0″ | Needed for 32″, or any monitor with a rear-facing connector cluster and straight cables. **Leaves nothing for the mount.** |

---

## 7. What it's made of, and where to buy it

### First — what these materials actually are

| | | |
|---|---|---|
| **ACM** | *aluminium composite · "Dibond"* | Two thin sheets of aluminium glued either side of a plastic core — a metal sandwich about **1/8″ thick**. Stiff, dead flat, colour baked on at the factory. **Nothing to sand, nothing to paint.** Every storefront and road sign is this stuff. |
| **HPL** | *high-pressure laminate · "Formica"* | The material on a kitchen counter. **It is not a board** — it's a 1/32″ skin with no stiffness of its own, so it has to be glued onto plywood or MDF first. That is the word "bonded" doing a lot of quiet work. |
| **Compact laminate** | *solid phenolic · Trespa, Fundermax* | The same material as Formica, pressed thick enough to stand on its own (1/4″–1/2″). Restroom partitions, lab benches. Beautiful and permanent, but heavy and sold in architectural quantities. |
| **Baltic birch** | *void-free plywood* | Very good plywood — many thin layers, no hidden gaps. Machines beautifully. But it's wood: to look finished it wants sanding, sealing and spraying, and **that is where volunteer builds come unstuck.** |

### The three routes

| | **A — Plywood, cut and sprayed** | **B — Plywood box, ACM front** ✅ | **C — Modify a bought enclosure** |
|---|---|---|---|
| What you do | CNC-cut 1/2″ Baltic birch, rabbet corners, spray satin graphite | Same plywood box, but the **visible front is 3 mm black ACM**, cut to shape, screwed to internal cleats | Buy a signage or instrument housing and cut it for the panel |
| The hard part | **The finish.** Ply edges telegraph; a brushed coat reads homemade from ten feet | **There isn't one.** The face arrives already finished | **Nothing off the shelf is 15″ × 29″ × 3-1/4″ portrait** |
| Needs | CNC access *and* somewhere to spray | Ordinary woodworking — the front is cut by someone else | Luck |
| Material | ~$80–140 | ~$120–200 | $150–400 |
| Weight | ~13 lb enclosure | **~12 lb** — ACM is lighter than the ply front it replaces | 30 lb+ in steel |

**Recommend B.** The single biggest risk in a volunteer-built enclosure is the
**finish**, and B removes it from the critical path entirely: the visible surface
arrives flat and durable, and the crew builds a plywood box behind it — a thing
any woodworker gets right on the first try.

### The move that actually makes this easy — don't buy a sheet, send the file

**[SendCutSend](https://sendcutsend.com/materials/acm/) will CNC-route the face
plate out of 3 mm matte black ACM and mail it to you.** Upload the drawing file,
they cut to **±0.005″**, ships in 2–4 days. Maximum part is **30″ × 44″** — our
face plate is 15.4 × 28.7, well inside.

This takes the hardest job away from the volunteer crew: **no CNC access needed
at CDL, no 4 × 8 sheet to buy and mostly throw away, no jig for the screen
window, and the three button holes arrive cut to size.**

### One small thing that decides the material

Panel-mount buttons have a **maximum panel thickness** — model-specific, commonly
6–11 mm. **3 mm ACM clears every one of them.** A 1/2″ plywood-and-Formica face
is 12.7 mm, at or over the limit for most switches, meaning counterboring the
back of all three holes by hand.

**Two limits on ACM worth knowing:** it can't be tapped or bent, so fastening goes
through clearance holes into threaded inserts in the plywood cleats (already the
plan); and cut edges show the black plastic core — invisible on black, a visible
dark line on white, so order it **black both sides**.

### Shopping list

| Part | What to order | Where | Rough cost |
|---|---|---|---|
| Face plate | 3 mm ACM, **matte black both sides**, one piece with the button holes cut in | [SendCutSend](https://sendcutsend.com/materials/acm/) | quote on upload, qty 1 |
| Box — sides, top, bottom, rear | 1/2″ Baltic birch, ~8 sq ft | [MakerStock](https://makerstock.com/collections/baltic-birch-plywood) · [Cherokee](https://www.cherokeewood.com/store/1-2-baltic-birch-plywood-cut-to-size/) · [Jeff Mack](https://jeffmacksupply.com/en-us/products/1-2-thick-baltic-birch-select-a-size) | $40–90 |
| Buttons × 3 | 30 mm anti-vandal, momentary, stainless. **Check the datasheet for panel range including 3 mm and actuation force ≤ 5 lbf** (§309.4) | [APEM AV](https://www.apem.com/panel-switches/pushbutton-switches/av-anti-vandal-pushbutton-switches) · [RJS](https://www.rjselectronics.com/category/panel-mount/pushbutton-metal-switches/metal-pushbutton-switches-anti-vandal/) · [Adafruit](https://www.adafruit.com/category/235) | $25–40 |
| Threaded inserts | #8 for plywood, ×15 — **never screw into a plywood edge** | McMaster-Carr | ~$12 |
| Rear-panel fasteners | Quarter-turn or captive thumbscrews, ×6 | McMaster-Carr | $20–30 |

**Other ACM sources:** [Curbell Plastics](https://www.curbellplastics.com/product-category/material/aluminum-composite-material-acm/dibond-panels/) ·
[OnlineMetals](https://www.onlinemetals.com/en/buy/3mm-aluminum-composite-panel-black/pid/mp-00040256) ·
[Midwest Airbrush](https://www.midwestairbrush.com/collections/acm-aluminum-panels-black) (small pieces).
**HPL:** [Wilsonart vertical grade, black matte](https://www.amazon.com/Wilsonart-Sheet-Laminate-Vertical-Grade/dp/B01FV20Z6A) ·
[Ledgeband](https://ledgeband.com/collections/laminate-sheets).
**Compact:** [Fundermax](https://fundermax.us/product/interior-thin-laminate-panels/) ·
[Wilsonart Compact](https://www.wilsonart.com/laminate/specialty-laminate/compact).

Costs are estimates — confirm at the link. Curbell and OnlineMetals block
automated requests; they load fine in a browser.

### ✅ The cut files exist — [`../fab-rev1/`](../fab-rev1/)

**One part.** `P1-face-plate.dxf` — 15.37 × 28.69″, screen window 12.17 × 21.24,
three ⌀30.5 mm button holes at 3.50″ centres, fifteen ⌀0.1875 mounting holes.

Upload it, pick **ACM → 0.118″ (3 mm) → matte black**, quantity **1**. No
secondary services. Full ordering notes in
[`../fab-rev1/README.md`](../fab-rev1/README.md).

**The window is 0.25″ oversize per side on purpose** — "24 inch" covers
23.6″–24.0″ diagonals and this clears all of them without cropping, with the
margin falling on the monitor's own black bezel. The monitor is aligned *to the
window* on an internal VESA frame, which is why P1 is safe to cut before the
monitor arrives.

**⚠ Confirm ⌀30.5 mm against your switch's datasheet before ordering.** It's the
only dimension here tied to a part nobody owns yet, and since this is now a
one-piece part, getting it wrong means recutting the whole face.

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
  leading edge is at 34.75″ AFF, above the 27″ threshold). With the recommended
  3 mm ACM face the enclosure is 3.25″, so **the adapter's budget is 0.75″**. See §5 — whether the rule binds here is a
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
