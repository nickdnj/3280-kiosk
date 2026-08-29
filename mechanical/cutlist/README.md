# The box — locked plan

> ⚠️ **Concept.** Nothing has been cut. Prices seen at Home Depot **West Long
> Branch, 2026-08-29**. Locked 2026-08-29.

**Zero rips. Nine crosscuts. Home Depot cuts the MDF.**

```bash
python3 make-cutlist.py            # the plan. 21 checks, all passing.
```

Read **[`SHOPPING.md`](SHOPPING.md)** in the store. Everything is generated from
the same geometry as the drawings, so the shopping list cannot drift from the
cut list.

---

## 1. Buy — $74.20, spares included

| | Model | Qty |
|---|---|---|
| **1×4 × 8 ft Radiata Pine Finger-Joint, PRIMED** (.719 × 3.5) | 252978 | ×2 |
| **1×3 × 8 ft Pine Finger-Joint, PRIMED** (.719 × 2.5) | 424600 | ×3 |
| **½″ × 2 × 4 MDF Project Panel** | 109097 | ×1 |
| Titebond II · 120 + 180 grit · #6 × 1¼ screws | | |

One of each board is spare. Cost is not the constraint; a second chance at any
part is worth more than $19.

**Finger-jointed, not common whitewood.** Whitewood comes bowed and knotty;
finger-jointed stock is cut from selected short pieces, which relieves the
stress that twists a board. A 28.690″ side that must sit flat against the face
plate is exactly the case that cares. It arrives primed, which we want anyway.

**These are 0.719″, not 0.750″.** Home Depot states it on the 1×3 listing.
Measure yours; `--ply` re-derives everything.

## 2. Why nothing is ripped

**The board's width becomes the box depth.** A 1×4 is 3.5″ wide, so the tube is
3.5″ deep and the sides need only crosscutting. The 1×3 supplies the button
rail, rear cleats and VESA rails at its full 2.5″ width. Nine crosscuts, all on
a mitre saw.

The cost is depth: the enclosure is **3.618″**, so the mounting adapter's share
of the ADA §307.2 4.000″ cap is **0.382″**. That is tight, and it is the one
number this plan spends to buy simplicity.

**Home Depot cuts the MDF.** The rear panel is deliberately 0.250″ undersize and
lands on a 2.500″ ledge, so their ±1/8″ cannot matter. You never handle a sheet
good.

## 3. Cut

```
1x4 x 8 ft, full 3.5" width      P2 28.690 x2    P3 13.932 x2
1x3 x 8 ft, full 2.5" width      P7 13.932 x1    P8 27.252 x2    P9 27.252 x2
1/2" MDF, cut by Home Depot      P4 13.682 x 27.002    P10 4.000 x 2.900
```

**Crosscut P2 first, dry-assemble, and measure the real cavity** before cutting
anything else. The tables are the prediction; the box is the truth.

## 4. The front cleats are gone — and that is a bug fix

Every earlier version of this design, **including the released drawing
package**, put vertical and horizontal cleats behind the face plate to receive
P1's mounting screws. Those cleats do not fit:

| | wall + cleat | clear width | vs monitor 12.870 |
|---|---|---|---|
| **Released ½″ birch + 1.000 cleat** | 1.500/side | 12.370 | **fouls by 0.250/side** |
| 0.719 pine + 0.719 cleat | 1.438/side | 12.494 | **fouls by 0.188/side** |
| **This plan, no front cleats** | 0.719/side | 13.932 | clears by 1.250/side |

The monitor is 12.870″ wide in a 15.370″ box. There is 1.250″ of margin per
side, and a wall-plus-cleat eats more than that. The top cleat fouls the
monitor's top edge by the same amount. **It was never buildable as drawn.**

The fix costs nothing: **all 15 of P1's mounting holes already land in solid
material without cleats** — ten in the side boards' front edges, two in the top
and bottom boards, three in the button rail. `make-cutlist.py` now checks this
on every run, and the check fails the released configuration.

The inserts sit 83% inside a 0.719″ edge and break out slightly on the inner
face. That is cosmetic and inside the box. **Epoxy them**; pine threads are soft.

## 5. Build

1. **Tube** — P2 sides over P3 top and bottom. Glue and screw, **pilot every
   hole**; pine end grain splits.
2. **Button rail** — P7, front-flush, centreline 23.715″ below the top edge. It
   takes the press load so the face plate can't flex under a thumb.
3. **Rear cleats** — P8 ×2, **turned 90°** so they lie 0.719″ deep and sit
   entirely behind the monitor instead of alongside it.
4. **Inserts** — 15 on P1's pattern. Epoxy.
5. **Rails** — P9 ×2 on the VESA centres.
6. Monitor, Pi tray, wiring. Switches into P1, then P1 on. Back panel last.

**23.3 lb finished.**

> ⚠️ **MDF is safe here only because P9 exists.** The monitor hangs on the VESA
> rails; P4 is a cover and no fastener enters an MDF edge.

## 6. What this supersedes in the released package

**P1 is unaffected** — its outline, window, cutouts and 15 mount holes are
independent of everything above, so the **$61.43 SendCutSend order stands.** ADA
placement is unaffected: buttons at 38.000″ AFF, kiosk bottom at 34.750″.

| Sheet | Now wrong |
|---|---|
| 102 · section | depth 3.250 → **3.618**; monitor–cleat conflict |
| 300 / 301 | P2 P3 P4 P9 P10 all resized; P4 is MDF |
| 302 · cleats | **P5 and P6 deleted**; P8 turned 90°; stock is 1× at full width |
| 400 · holes | inserts go into board edges, not cleats |
| 100 / 101 / 700 | envelope, BOM materials, inspection dimensions |

## 7. Alternatives, priced and rejected

| | | Why not |
|---|---|---|
| 1×6 frame, ripped | $52.37 | one rip per board; this plan trades $22 for zero |
| Birch ply + MDF | $67.34 | plywood edges hold screws worse than pine long grain |
| One 4×8 PureBond | $59.98 | 32 sq ft for a 5.3 sq ft job |
| Cellular PVC | $124 | ~⅓ the stiffness, 7× the thermal movement |
| IKEA IVAR | $39 | [shelved](../ikea-build/) — nothing usable directly |
| Off-the-shelf cabinet | — | shallowest is 6¾″ against a 4.000″ cap |

Explore any of them: `--allow-rip`, `--stock ply`, `--board 5.5`, `--back tacked`.
