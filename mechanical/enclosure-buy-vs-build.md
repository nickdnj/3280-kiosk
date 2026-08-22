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
