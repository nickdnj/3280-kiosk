# Buy-and-Modify vs. Fabricate — Door Enclosure

> **Decision status: OPEN, gated on C1.** Both paths are live. The measurement
> that picks between them is the same one that gates everything else — the
> closing clearance behind the cabinet's front face (ME-1 §C).
> **Do not buy anything before that number exists.**

**Reads with:** [`door-construction.md`](door-construction.md) ·
[`dimensions-assumed.md`](dimensions-assumed.md) §5 ·
[`measurement-checklist.md`](measurement-checklist.md) §C

---

## 1. The candidate category

Not digital-signage enclosures — those are built around a **cased** monitor and
run 4–8″ deep before you start, in a modern black-and-silver style that fights
the cabinet.

The right category is **shallow industrial / electrical enclosures**: nVent
Hoffman, Saginaw Control & Engineering, Rittal, Bud Industries, Hammond
Manufacturing. Single-door wall boxes, NEMA 1 or 12, sold in a wide size ladder
and finished in ANSI 61 gray — which sands and repaints to tan without argument.

What makes them interesting for us:

- A **hinged door and latch are already built in**, engineered and tested
- They ship with a **removable inner mounting panel** — exactly where an LCD,
  a controller board and a Pi want to live, and it comes out on the bench
- The body is rigid, square and already assembled
- Knockouts and gasketing are solved problems

---

## 2. The clever bit: run the box backwards

The obvious reading is "the enclosure's door becomes our door." That's wrong and
it wastes the product.

**Mount the enclosure body facing *into* the cabinet.** Then:

| Enclosure feature | Becomes |
|---|---|
| Solid back panel (now facing the visitor) | **The door face** — cut the screen window and button holes here |
| Inner mounting panel | **The LCD / controller / Pi carrier**, removable on the bench |
| Its own hinged, latched door (now facing rearward) | **Rear service access** — already hinged, already latched (MR16) |
| The body | The structural box and heatsink |

The whole enclosure then hinges on its left edge to the fixed frame. You get
MR16 service access and MR18 full enclosure for free, and the one surface you
have to modify is a **flat, solid, accessible back panel** — the easiest surface
on the whole product to work.

That's a real design, not a bodge.

---

## 3. What it does *not* save you

**The screen window.** You still have to cut a ~11.7 × 20.9″ rectangle to
±0.03″ with clean, square, deburred edges — and now you're cutting it in a
**formed box** instead of in flat sheet. That is harder, not easier: no laser
bed will take a 4″-deep box, so it becomes a jigsaw-and-file job, or it goes to
a router/mill with awkward workholding.

Avoiding that cut was the single biggest reason for outsourcing in the first
place. **Buying an enclosure does not avoid it.** It saves the forming, the box
assembly, and the hinge/latch engineering — all of which were the *easy* parts.

---

## 4. What it costs

### Depth — the gating cost

| Path | Door depth |
|---|---|
| Custom fabrication (as drawn) | **2.5″** |
| Shallowest common off-the-shelf enclosure | **~4″** |
| Typical off-the-shelf | 6–8″ |

Rule from [`dimensions-assumed.md`](dimensions-assumed.md) §5: **C1 ≥ door depth
+ 0.5″.**

| Measured C1 | What it means |
|---|---|
| **< 3.0″** | Custom fab only, and the escalation ladder applies |
| **3.0″ – 4.5″** | Custom fab only. Off-the-shelf won't close |
| **≥ 4.5″** | A 4″ enclosure fits — buy-and-modify is genuinely on the table |
| **≥ 6.5″** | The whole size ladder opens up; pick on proportions, not depth |

### Weight — disqualifying for steel

A 30 × 16 × 4″ enclosure in 16 ga steel (0.060″) has roughly 9.2 sq ft of skin at
about 2.45 lb/sq ft — **~23 lb of empty box**, before the door, mounting panel,
LCD, Pi and buttons. Call it 35–40 lb assembled.

Against a design budget of 14.5 lb and ~100 in-lb at the hinge, a steel box lands
near **250 in-lb** — cantilevered off a mount that is not allowed to put a single
hole in a museum artifact.

**Steel is out.** If this path is taken it has to be an **aluminum** enclosure
(~1/3 the weight, ~10–12 lb) — a smaller part of the catalogue and more
expensive, but the only version that's safe on a reversible mount.

Fiberglass and polycarbonate boxes are light and cheap but give up the thermal
conduction path (§5 of the build spec) and read wrong next to painted sheet
metal.

### Proportions

Standard sizes won't be 14.5 × 30. The nearest common footprints — 16 × 30,
16 × 24, 12 × 24 — change how much card cage stays visible around the door, which
is a stated design value (MR3). Not fatal, but it's a real aesthetic cost and it
has to be re-checked against the measured opening.

---

## 5. The hybrid — what I'd actually recommend if C1 allows

**Buy the box. Laser-cut only the face.**

- Buy a shallow **aluminum** enclosure for the body, hinge, latch, rear access and
  inner mounting panel
- Have **one flat part** cut — a face plate with the screen window, button holes
  and fixings — sized to the enclosure's actual back panel
- Bond or fasten the face plate over the enclosure's back panel, or replace that
  panel entirely if it's removable

This keeps the hardest operation (the window) on a laser bed where it belongs,
buys everything else off a shelf, and drops the fab package from four parts to
one flat plate — the cheapest, fastest, lowest-risk part to order.

It also survives failure gracefully: if the enclosure turns out wrong, you've
lost a box, not a design.

---

## 6. Honest summary

| | Custom fab (as drawn) | Buy + modify |
|---|---|---|
| Depth | **2.5″** | 4″ minimum |
| Weight | ~14.5 lb | ~10–12 lb alu, 35–40 lb steel ❌ |
| Proportions | Exactly as designed | Whatever the catalogue offers |
| Hinge / latch / access | Design + build it | **Already solved** |
| Screen window | **Lasered, flat, perfect** | Hand-cut in a formed box |
| Finish | Prime + tan | Prime + tan (same) |
| Thermal path | Designed in | Good, if aluminum |
| Lead time | ~1 week | Off the shelf |
| Risk concentration | The order | The window cut |

Neither is clearly better. **Custom fab wins on depth, proportions and the
quality of the hard cut. Buying wins on hinge/latch/access engineering and lead
time.** The hybrid in §5 takes the better half of each.

---

## 7. Before Wednesday

**Buy nothing.** The decision needs C1.

Useful now, costs nothing:

- [ ] Price shallow **aluminum** single-door enclosures near 14–16″ W × 24–30″ H
      × 4″ D. Note the shallowest depth anyone offers in aluminum
- [ ] Confirm whether their back panel is removable or welded — removable is
      worth a lot
- [ ] Check the secondary market; industrial enclosures turn up cheap used
- [ ] Ask CDL (question 7 of the
      [drawing package](fab/DRAWING-PACKAGE.md)) whether they'd rather cut a
      window in a box or bend a tray — their answer may decide this for us
- [ ] **Look for a suitable enclosure in the warehouse on Wednesday** — salvage
      beats buying, and an aluminum box on a shelf changes the maths

Then on Wednesday, C1 decides it. Take the §4 table with you.

---

## 8. Lead candidate — Leviton STRUCTURED MEDIA enclosure

Verified against the manufacturer spec sheet (Leviton B26 SS1431, rev. Feb 2026).
This is a **low-voltage structured-wiring can**, not a breaker panel — which
removes the weight, finish and identity problems of a load center in one move.

### The parts

| Part No. | Description | Size |
|---|---|---|
| **47605-28N** | 28″ **enclosure only** ← the one we want | **28.0″ H × 14.30″ W × 3.85″ D** |
| 47605-28W | Same can + flush-mount cover | 29.32 × 15.62 × 3.85 |
| **47605-28S** | 28″ **Premium Vented Hinged Door** | 29.32 × 15.62 × 0.25 |
| 47605-28D | 28″ Economy Hinged Door | 29.32 × 15.62 × 0.25 |
| 47605-F28 | 28″ Flush-Mount Cover (flat panel) | 29.32 × 15.62 × 0.20 |
| 47612-28B | **2″ depth extender bracket** | — |
| 5L000-L0K | Lock & key | — |

42″ versions exist (47605-42x) — too tall for us.

### Why it fits

| | Our design | 47605-28N | |
|---|---|---|---|
| Width | 14.50″ | **14.30″** | ✅ essentially exact |
| Height | 30.00″ | **28.00″** | ✅ 2″ short — absorbs into the layout |
| Depth | 2.50″ | 3.85″ | ⚠️ needs **C1 ≥ 4.35″** |
| Material | 0.080″ alu | **20-ga white powder-coated steel** | ✅ paints normally |
| Weight | ~14.5 lb | ~13.6 lb can + vented door | ✅ **on budget** |

**The face layout fits the 28″ can almost exactly.** Window 20.86 + reveal 0.60 +
button plate 4.00 = 25.46, leaving ~1.3″ top and ~1.2″ bottom margin in 28.0″.
Width: an 11.71″ window in 14.30″ leaves 1.30″ each side against the 1.40″ we drew.

### What it solves for free

- **Ventilated hinged door** (47605-28S) — MR14 + MR16 off the shelf. Leviton
  explicitly recommends it "when using active equipment inside enclosure," so
  powered gear in this box is an anticipated use, not a hack.
- **20-gauge, not breaker-panel gauge** — this is why the weight works. A load
  center of the same footprint runs ~26 lb because it has to carry bus bars.
- **White powder-coat**, not galvanised — ordinary primer adheres.
- **No electrical identity problem.** A structured-media can is a data enclosure.
  Nobody mistakes it for a live panel.
- Knockouts and self-healing grommets on top/bottom/sides for the hinge cable.
- **2″ extender bracket** if we ever need more depth; **lock and key** if the
  museum wants the rear secured.

### The catch, and the fix

The can's back panel carries a **grid of module-mounting holes**. Running the box
backwards puts that grid on the visitor-facing surface.

**Fix — and it is the §5 hybrid exactly:** laser-cut **P1 only**, resized to
14.30 × 28.0, and fasten it over the can's back. It hides the hole grid, carries
the exact window and button holes, and takes the tan finish. The fab package
drops from four parts to **one flat plate**, and P2/P4 disappear entirely.

### ⚠️ Reject the plastic ones

Legrand/On-Q's 30″ enclosures (ENP3050 and similar) are **plastic**. No thermal
conduction path for the Pi (§5 of the build spec), and they won't read right next
to painted sheet metal. Leviton's 47605/49605 series is steel — check the
material on every listing.

---

## 8. Where to browse

### What to filter on

> **Aluminium** · **14–16″ W × 24–30″ H** · **depth ≤ 4″** · hinged door ·
> removable back panel · NEMA 1 or 12 (indoor — no need to pay for 4/4X)

Depth is the filter that kills most results. Sort by it first. And **check the
material on every hit** — the catalogues are overwhelmingly steel, and steel is
disqualified on weight (§4).

### Best for filtering by actual dimensions

| Site | Why |
|---|---|
| [digikey.com](https://www.digikey.com) | Parametric search on **exact L × W × H and material** — the fastest way to find out whether a shallow aluminium box in our size even exists. Carries Hammond and Bud. |
| [mouser.com](https://www.mouser.com) | Same parametric approach, different stock |
| [mcmaster.com](https://www.mcmaster.com) | Browse by dimension, dimensioned drawings on every page, CAD downloads, ships next day |

### General industrial suppliers

| Site | Why |
|---|---|
| [automationdirect.com](https://www.automationdirect.com) | Clear specs, good prices, honest photos |
| [zoro.com](https://www.zoro.com) | Consumer-friendly front end on industrial stock |
| [grainger.com](https://www.grainger.com) | Widest catalogue, priced accordingly |

### Manufacturer catalogues — best drawings

| Site | Why |
|---|---|
| [hammfg.com](https://www.hammfg.com) | Hammond. Deep range of small/shallow boxes, aluminium options, excellent drawings |
| [hoffman.nvent.com](https://hoffman.nvent.com) | Hoffman. The industry default |
| [saginawcontrol.com](https://www.saginawcontrol.com) | Often cheaper than Hoffman for the same box |
| [budind.com](https://www.budind.com) | Bud Industries |
| [polycase.com](https://www.polycase.com) | Sells direct **and offers CNC modification of what they sell** — they could cut our window |

### A third path — custom one-off enclosure houses

Worth pricing, because budget is not a constraint (PRD §15) and these remove the
hard cut entirely:

| Site | Why |
|---|---|
| [protocase.com](https://www.protocase.com) | **Custom enclosures, quantity of one, ~2–3 day turnaround, finished and painted.** Send our drawings and get back the actual box. Removes the window-cut problem completely. |
| [frontpanelexpress.com](https://www.frontpanelexpress.com) | Machined aluminium **front panels** with cutouts and engraving, one-offs, free design software. A direct fit for the §5 hybrid — buy a box, get P1 made here. |

### Laser cutting (already in the fab package)

[sendcutsend.com](https://www.sendcutsend.com) ·
[oshcut.com](https://www.oshcut.com) · [ponoko.com](https://www.ponoko.com)

### Secondary market

eBay and industrial surplus dealers — search *"aluminum electrical enclosure
hinged"*. Industrial enclosures turn up cheap and undamaged, and it beats buying
new on the salvage-first rule. **And check the warehouse first.**
