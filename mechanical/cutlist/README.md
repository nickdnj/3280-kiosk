# The box — locked plan

> ⚠️ **Concept.** Nothing has been cut. Prices seen at Home Depot **West Long
> Branch, 2026-08-29**. Locked 2026-08-29.

**A solid pine frame, a tacked-on MDF back, and the ACM face plate already on
order. $52.37 of material, 24.2 lb finished.**

```bash
python3 make-cutlist.py            # the plan. 20 checks, all passing.
```

Everything below is generated from the same geometry as the drawings, so the
shopping list cannot drift from the cut list. Read
**[`SHOPPING.md`](SHOPPING.md)** in the store; **[`nesting.svg`](nesting.svg)**
is the MDF panel layout.

---

## 1. Buy

| | Model | |
|---|---|---|
| **1×6 × 8 ft Radiata Pine Finger-Joint, PRIMED** | 280552 | $16.37 |
| **1×3 × 8 ft Pine Finger-Joint, PRIMED** | 424600 | $8.52 |
| **½″ × 2 × 4 MDF Project Panel** | 109097 | $27.48 |
| Titebond II · 120 + 180 grit · #6 × 1¼ screws (40) | | ~$20 |
| | | **$52.37** in stock |

**No cut desk.** Everything fits in a car, and their panel saw is ±1/8″ against
a face plate whose hole pattern is already fixed at ±0.005″.

**Finger-jointed, not common whitewood.** Whitewood 1×6 is $2 cheaper and comes
bowed and knotty. Finger-jointed stock is cut from selected short pieces, which
relieves the internal stress that twists a board — and a 28.690″ side panel that
must sit flat against P1 is exactly the case that cares. Primed is a bonus; the
box gets painted anyway.

**These boards are 0.719″, not 0.750″.** Home Depot states it on the 1×3 listing
and the 1×6×12 confirms it as 23/32. Measure yours in four places and re-run
with `--ply` / `--cleat` if it differs. The cavity, every cleat and the depth
chain all move with it.

## 2. Cut

**One 1×6 carries the tube, every cleat and the tray.**

```
BOARD A   1x6 x 8 ft
  1. crosscut 4" off one end        -> P10 tray 4.000 x 2.900
  2. rip the remaining 92" to 2.719 -> P2 28.690 x2 + P3 13.932 x2   (85" of 92")
  3. rip the 2.656" offcut into 3 x 0.719 cleat strips
                                    -> P5 P6 P7                      (92" of 276")

BOARD B   1x3 x 8 ft
     rip 2.5 -> 1.500               -> P9 VESA rails x2              (55" of 96")

MDF       1/2" 2x4 panel            -> P4 rear panel 15.370 x 28.690
```

| Part | | Size | Qty |
|---|---|---|---|
| P2 | side panel | 2.719 × 28.690 | ×2 |
| P3 | top / bottom | 2.719 × 13.932 | ×2 |
| P4 | rear panel, **MDF** | 15.370 × 28.690 × 0.500 | ×1 |
| P5 | front cleat, vertical | 0.719 sq × 27.252 | ×2 |
| P6 | front cleat, horizontal | 0.719 sq × 12.494 | ×2 |
| P7 | button rail | 0.719 sq × 12.494 | ×1 |
| P9 | VESA rail | 1.500 × 27.252 | ×2 |
| P10 | Pi tray | 4.000 × 2.900 | ×1 |

**Cut P2 first, then measure the real cavity** and cut P3, P9, P4 and the cleats
to what you measured. The table is the prediction; the box is the truth.

## 3. Build

1. **Tube** — P2 sides, P3 top and bottom. Glue and screw, pilot every hole.
2. **Front cleats** — P5, P6 glued to the inner faces, **flush with the front**.
   That gives a continuous 1.438″ landing band, so P1's mount holes at 0.625″
   sit in solid material with meat all round.
3. **Button rail** — P7, front-flush, centreline 23.715″ below the top edge.
   It takes the press load so the face plate can't flex under a thumb.
4. **Inserts** — 15 in the front plane on P1's pattern, plus 6 in the rear edges
   for the back panel. **Epoxy them**; pine threads are soft.
5. **Rails** — P9 ×2 on the VESA centres, spanning the cavity.
6. **Monitor** onto the rails. **Pi tray** into the lower cavity.
7. **Face plate** — switches into P1 first, wire them, then P1 onto the cleats.
8. **Back** — P4 tacked on last, into the rear-edge inserts.

## 4. Why the back is tacked on, not inset

It deletes P8 entirely (cleat stock 146″ → 92″), lets the tube be only as deep
as what lives inside it (3.132 → 2.719), gives the panel four-sided support
instead of two cleats, and clears a 0.018″ depth conflict that an inset ½″ back
could not.

**It is not free.** The enclosure grows to **3.337″**, so the mounting adapter's
share of the ADA §307.2 4.000″ cap goes 0.750″ → **0.663″**.

> ⚠️ **MDF is safe here only because P9 exists.** The monitor hangs on the VESA
> rails; P4 is a cover, and no fastener enters an MDF edge. Delete the rails and
> bolt the monitor through the back — as the shelved variant K does — and ten
> pounds of glass sits on four M4 bolts in MDF face. Don't.

## 5. What this supersedes in the released drawing package

The face plate is **unaffected** — P1's outline, window, switch cutouts and
15 mount holes are independent of box depth, so the **$61.43 SendCutSend order
stands as-is.** ADA placement is unaffected too: buttons at 38.000″ AFF, kiosk
bottom at 34.750″, both driven by P1's geometry and the 28.690″ height.

These sheets now describe the old ½″ Baltic birch, inset-back box and must be
regenerated before anyone builds from them:

| Sheet | What changed |
|---|---|
| 102 section A-A | depth chain 3.250 → **3.337**; rear panel tacked |
| 300 / 301 | P2 P3 P4 P9 P10 dimensions; P4 is MDF and full-footprint |
| 302 cleats | cleats 1.000 sq → **0.719 sq**; **P8 deleted** |
| 400 holes | 6 rear inserts move to the tube's rear edges |
| 100 / 101 / 700 | envelope depth, BOM materials, inspection dimensions |

## 6. Alternatives, priced and rejected

| | | Why not |
|---|---|---|
| Birch ply 2×4 + MDF 2×4 | $67.34 | works; $15 more, and plywood edges hold screws worse than pine long grain |
| One 4×8 PureBond birch | $59.98 | best $/sq ft and a full spare set, but 32 sq ft for a 5.3 sq ft job |
| Cellular PVC | $124 sheet | ~1/3 the stiffness, 7× the thermal movement, solves rot we don't have |
| IKEA IVAR pine | $39 | [shelved](../ikea-build/) — nothing usable directly |
| Any off-the-shelf cabinet | — | shallowest is 6¾″ deep against a 4.000″ cap |

Explore any of them: `--stock ply`, `--board 3.5`, `--back inset`, `--ply 0.469`.
