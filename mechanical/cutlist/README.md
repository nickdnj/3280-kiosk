# The box — 15 × 30, whole numbers

> ⚠️ **Concept.** Nothing cut. Prices seen at Home Depot **West Long Branch,
> 2026-08-29**.

**Zero rips. Nine crosscuts. Every dimension a multiple of ¼″.**

```bash
python3 make-cutlist.py            # 23 checks, all passing
```

The box reads its geometry from **[`../fab-rev1/_p1.py`](../fab-rev1/_p1.py)** —
the same module the DXF and the print stencil are generated from. There is one
source of truth now; the box cannot disagree with the face plate.

---

## 1. Buy — $68.86, spares included

| | Model | Qty |
|---|---|---|
| **1×4 × 8 ft Kiln-Dried Whitewood** (actual .750 × 3.5) | 914681 | ×2 |
| **1×3 × 8 ft Kiln-Dried Whitewood** (actual .750 × 2.5) | 914649 | ×3 |
| **½″ × 2 × 4 MDF Project Panel** | 109097 | ×1 |
| Titebond II · 120 + 180 grit · #6 × 1¼ screws | | |

**Whitewood, because it is a true ¾″.** That is what makes the cut list land on
halves and quarters — a 0.719″ finger-jointed board gives a 13.562″ cavity
instead of 13.500″. The trade is straightness: whitewood arrives knottier and
more bowed, so **sight down every board in the rack** and reject the bent ones.
If you would rather have the straighter stock, `--ply 0.719` re-derives
everything for finger-jointed primed pine.

## 2. Cut — nothing is ripped

The board's **width becomes the box depth**. A 1×4 is 3.5″ wide, so the tube is
3.5″ deep by crosscut alone; the 1×3 gives the button rail, rear cleats and VESA
rails at its full 2.5″ width.

```
1x4, full 3.5" width     P2  3-1/2 x 30       x2
                         P3  3-1/2 x 13-1/2   x2
1x3, full 2.5" width     P7  13-1/2           x1
                         P8  28-1/2           x2
                         P9  28-1/2           x2
MDF, cut by Home Depot   P4  13-1/4 x 28-1/4
                         P10 4 x 3
```

**Home Depot cuts the MDF.** The rear panel is deliberately ¼″ undersize and
lands on a 2½″ ledge, so their ±1/8″ cannot matter. You never handle a sheet
good.

**Crosscut P2 first, dry-assemble, and measure the real cavity** before cutting
anything else.

## 3. The one number that got tighter

Rounding the plate from 15.370″ to 15.000″ took **0.185″ per side** out of the
monitor's clearance. The cavity is now 13.500″ against a 12.870″ monitor —
**0.315″ per side**, and against the widest thing sold as "24 inch" (a true 24.0″
diagonal) **0.267″ per side.** Both positive, both checked on every run.

But `MON_OW` is an estimate until you own the monitor. **Measure the actual
panel before cutting P3.** This is the margin the rounding spent.

## 4. Build

1. **Tube** — P2 sides over P3 top and bottom. Glue and screw, **pilot every
   hole**; pine end grain splits.
2. **Button rail** — P7, front-flush, centreline **24″** below the top edge.
   It takes the press load so the face plate can't flex under a thumb.
3. **Rear cleats** — P8 ×2, **turned 90°** so they lie ¾″ deep and sit entirely
   behind the monitor rather than alongside it.
4. **Inserts** — 15 on P1's pattern, **½″ in from the edge**. At the old 5/8″
   a 0.375″ insert broke out of a ¾″ board edge; at ½″ it spans 0.3125–0.6875
   and sits entirely inside. **Epoxy them.**
5. **Rails** — P9 ×2 on the VESA centres. Monitor, Pi tray, wiring.
6. Switches into P1, then P1 on, then the back panel.

**23.8 lb.** Enclosure **3.618″** deep, leaving the mounting adapter **0.382″**
of the ADA §307.2 4.000″ cap.

> ⚠️ **MDF is safe only because P9 exists.** The monitor hangs on the VESA rails;
> P4 is a cover and no fastener enters an MDF edge.

## 5. No front cleats — that was a bug fix

Every earlier version, **including the released drawing package**, put cleats
behind the face plate to receive P1's screws. They never fitted: the released
½″ wall plus 1.000″ cleat eats 1.500″ per side, and the monitor only has 1.250″
of margin. It fouled by 0.250″ per side, and the top cleat fouled the monitor's
top edge by the same.

All 15 of P1's holes already land in solid material without them — ten in the
side boards' front edges, two in the top and bottom boards, three in the button
rail. P5 and P6 are deleted. There is a permanent check that passes this plan
and **fails the released configuration**.

## 6. What this supersedes

The whole released drawing package is now stale — the envelope itself moved.

| | was | now |
|---|---|---|
| Plate | 15.370 × 28.690 | **15 × 30** |
| Window | 12.170 × 21.240 | **12¼ × 21¼** |
| Button datum below top | 25.440 | **26** |
| Kiosk bottom AFF | 34.750 | **34** |
| Mount holes in from edge | 0.625 | **0.500** |
| Enclosure depth | 3.250 | **3.618** |
| Front cleats P5 P6 | 1.000 sq | **deleted** |

Buttons stay at **38″ AFF** — that never moves, it is the ADA datum everything
else is placed from.

**The SendCutSend quote must be redone.** $61.43 was for 441 sq in; this is 450.

## 7. Alternatives

`--allow-rip`, `--stock ply`, `--board 5.5`, `--back tacked`, `--ply 0.719`.
