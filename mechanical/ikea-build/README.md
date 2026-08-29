# Variant K — building the kiosk box out of IKEA

> ## 🗄 SHELVED 2026-08-29
> **Not the build route.** The kiosk box is built per the released package —
> ½″ Baltic birch, sheets [300 / 301 / 302](../dwg/). Variant K is kept for the
> finding in §1, which is the part that outlives it.
>
> **Why it was shelved:** the idea was only worth having if IKEA sold something
> we could use *directly*. It doesn't — §1 below is the proof — and once it
> reduced to "buy pine and cut it yourself," IKEA stopped being special. A
> quarter sheet of Baltic birch is better material than knotty IVAR pine, and
> §4 already conceded that. The $39 was never the point.
>
> **What to take from it:** §1 generalises past IKEA. *No* off-the-shelf shallow
> cabinet can work, whoever makes it, because ADA §307.2 allows the kiosk
> 4.000″ of total projection and the shallowest wall cabinets on the market are
> 6¾″ deep. When someone suggests buying an enclosure — and someone will —
> that is the number that settles it.
>
> ⚠️ **Concept.** Nothing here was cut or built.

**The short answer: you cannot buy the kiosk at IKEA, but you can buy the wood
there for $39, and one $12 shelf makes the entire box.**

Two deliverables:

| | |
|---|---|
| **[`3280-K-assembly-manual.pdf`](3280-K-assembly-manual.pdf)** | 15-page IKEA-style manual — shopping, cut plans, hardware, six assembly steps. Print it. |
| **[`_geom_k.py`](_geom_k.py)** | the geometry, with 16 self-checks. `python3 _geom_k.py` |

Everything except **P1, the face plate** — which is CNC-routed by SendCutSend
from 3 mm ACM, exactly as [`../fab-rev1/`](../fab-rev1/) already specifies.

---

## 1. Why no IKEA product can *be* the enclosure

I checked this before designing around it, because if a $60 cabinet worked, the
whole cut plan below would be wasted effort. It doesn't, and the reason is a
single number.

**ADA §307.2 caps the kiosk at 4.000″ of projection.** Its leading edge lands at
34.75″ AFF, above the 27″ threshold where the protruding-objects rule starts
applying. The enclosure takes 3.250″ and the mounting adapter gets the remaining
0.750″. That budget is what kills every candidate:

| | Depth | |
|---|---|---|
| **Our budget** | **3.250″** | |
| ENHET wall cabinet — IKEA's shallowest | 6¾″ | 2× over. Blows §307.2 on its own. |
| BESTÅ frame | 15″ | not close |
| RÖDALM / former RIBBA frames | ~2″ | too *shallow* for a 1.8″ monitor, and it's thin MDF — it will not carry 24 lb or hold a panel-mount switch |

Cabinets are too deep, frames are too shallow, and nothing sits in between. It
is not a near miss.

## 2. What IKEA *is* good for

**IVAR shelves are solid pine, ¾″ thick, untreated, and cheap.** That is real
material — not particleboard, not veneered MDF — and IKEA is one of the few
places that sells it in small flat pieces instead of 8-foot boards.

| Buy | Size | Price | For |
|---|---|---|---|
| **2 × [IVAR shelf 83×30](https://www.ikea.com/us/en/p/ivar-shelf-pine-30318163/)** (303.181.63) | 32⅝ × 11¾ × ¾″ | $12.00 ea | shelf A → the box tube · shelf B → every cleat + the Pi tray |
| **1 × [IVAR shelf 83×50](https://www.ikea.com/us/en/p/ivar-shelf-pine-80318165/)** (803.181.65) | 32⅝ × 19⅝ × ¾″ | $15.00 | shelf C → the rear panel |
| 1 × [FIXA / TRIXIG stick-on floor protectors](https://www.ikea.com/us/en/p/fixa-stick-on-floor-protectors-set-of-20-gray-00431151/) | 1⅝″ hex felt, ×20 | ~$5 | soft, non-marring bumpers on the kiosk's back — see §6 |
| | | **$39** | wood only |

Prices seen on ikea.com/us, 2026-08-28, both shelves on sale. IKEA does not cut
material for you — assume you are ripping it yourself.

**One 83×30 shelf makes the whole four-sided box.** Rip it into three 3.132″
strips: two become the full-height sides, the third yields both the top and the
bottom with 4.9″ to spare. That is a genuinely tidy result and it is why this
variant is worth writing down.

## 3. What changes, and what deliberately doesn't

Baltic birch ½″ becomes IKEA pine ¾″. **The envelope does not move** —
15.370 × 28.690 × 3.250″. P1, the ADA placement maths, sheet 100 and the
adapter's 0.750″ budget all key off those numbers, so changing them would
invalidate the released drawing package. Variant K changes only what is inside.

Three consequences fall out of the extra ¼″ of wall:

**The face plate still lands on solid wood.** P1's mount holes sit 0.625″ in from
the edge. A ¾″ wall plus a ¾″ cleat glued flush behind it presents a continuous
1.500″ landing band, so every insert has material all round it. No hole moves.

**The VESA rails are gone.** They no longer fit the depth chain, so the monitor
bolts straight through the ¾″ rear panel on 12 mm M4 standoffs. That is stiffer
than two ½″ rails, it is one part fewer, and it turns the rear panel into a
**lift-out service module** — undo six thumbscrews and the monitor, the Pi and
the tray all come out together on the bench.

The trade: you can no longer reach behind the monitor without unbolting it, and
the panel is heavy and awkward while it is loose. That is a two-person job, and
it is why the manual opens with the two-people page.

```
0.000  P1, 3 mm ACM
0.118  ─ 0.100 bezel clearance
0.218  monitor front
2.018  monitor back
       ─ 0.482 cable gap  (12 mm standoff + 0.010 shim)
2.500  rear panel front
3.250  rear panel back = back of the box
```

**Weight is a wash.** 24 lb finished, against ~23 lb for the birch build — pine
is lighter per cubic inch, and we use more of it.

## 4. The two honest downsides

**Solid softwood moves with humidity; plywood barely does.** The rear panel is
the piece at risk — 13.7″ across the grain, in a building that is not climate
controlled. Mitigations, all of them in the drawings: cut it with the **grain
running the long way** (manual page 6), it is edge-glued stock rather than a
single board, it gets 0.100″ of clearance per side across the grain against
0.050″ along, and it is sealed on all six faces. If this still worries you, buy
that one piece as ½″ Baltic birch and leave the rest IKEA — nothing else in the
design changes.

**Pine is soft, and IVAR is knotty.** Threaded inserts hold less well in
softwood edge grain than in birch ply, so **epoxy them in** rather than trusting
the threads. Lay the cuts out to keep knots away from the 21 insert positions —
the cut plan leaves enough spare material to choose.

## 5. Sequence

1. Buy the three shelves. Check each one for cup and twist **in the store** —
   sight down the length. Reject bowed ones.
2. Cut per manual pages 5–6.
3. Assemble per manual pages 9–14.
4. Bench-test the whole kiosk. No 3280 involved.
5. **Then** design the mounting adapter. Still undesigned, still has 0.750″.

## 6. About the felt pads

They go on the **kiosk's** back, never on the machine, as the soft interface
between our enclosure and the 3280's original textured paint. They are a
suggestion for the adapter designer, not a decision — the interface material is
that subsystem's call, and long-term contact with an artifact's finish deserves
the museum's opinion before anything is stuck down.

## 7. Files

```
_geom_k.py        geometry + 16 self-checks
_draw.py          line-art primitives (isometric, IKEA man, bubbles)
make-manual.py    generates the 15 pages; refuses to pass if anything falls off a page
make-pdf.sh       build + verify the PDF is 15 Letter pages
manual/*.svg      the pages
```

Change a dimension in `_geom_k.py`, run `./make-pdf.sh`, and the manual redraws.
