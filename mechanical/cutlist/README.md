# Buying the box at Home Depot

> ⚠️ **Concept.** Nothing here has been cut. Prices seen at **West Long Branch,
> 2026-08-29**; confirm at the store.

**Buy one sheet, take three cuts at the desk, cut every real dimension yourself.**

```bash
python3 make-cutlist.py                 # the cut list, for 0.469 ply
python3 make-cutlist.py --ply 0.484     # after you measure the actual sheet
```

The script derives every length from the thickness you measure, runs 14 checks,
and draws [`nesting.svg`](nesting.svg).

---

## 1. Buy this

| | | |
|---|---|---|
| **½″ × 4 × 8 PureBond Birch Plywood** — model **833185** | **$59.98** | 15 in stock |
| **Poplar or red oak 1×4, 6 ft** — hardwood rack, not the pine rack | ~$15–25 | all cleats |
| Titebond II, 120 + 180 grit, #6 × 1¼ wood screws (40) | | |

**Why the full sheet and not a project panel.** The obvious buy looks like a
2×4 handy panel — we only need 5.3 sq ft. Two problems. The nest is
**0.096″ too wide for a 24″ panel** (`--panel 24 48` fails the first check), so
one won't do it. And two ProWood birch 2×4s are **$79.72** — twenty dollars more
than a full sheet of better plywood. The 4×8 is both the cheaper and the only
workable option, and it leaves a complete spare set of parts.

**The material substitution, stated plainly.** The drawings say *Baltic birch*.
This is **PureBond** — birch face veneers on a veneer core, not the void-free
all-birch 13-ply stuff, which Home Depot does not sell. For this box that is
acceptable: the loads are small, and the fastening that matters goes into
hardwood cleats, not into plywood edges. Where the drawings do call for edge
screws (P2 into P3 at the corners), **pilot every hole** — veneer core splits
where Baltic birch would not. If you want the real thing, Rockler and Woodcraft
sell 12 mm Baltic birch in 24×30 pieces; run `--ply 0.472`.

Skip the Sande and radiata pine panels. Sande is $10 less and softer with more
voids; $10 is not worth it on the one structural part of the whole kiosk.

## 2. Measure before you cut anything

**"½ inch" plywood is not 0.500″.** Home Depot's is usually 15/32 (0.469), it
varies sheet to sheet, and Columbia lists their ¼″ PureBond as an actual 0.188″
— so do not trust the label. Put calipers on the sheet in **four places**, take
the average, and feed it to the script.

Almost every length in the box moves with it. At 0.469 the cavity is
14.432 × 27.752; at a true 0.500 it is 14.370 × 27.690 — **a 1/16″ error that
would show up as a gap at the face plate.** Only P2, P10 and the depth are
thickness-independent.

One thing the thin stock quietly improves: with a 0.469 wall, **92 %** of each
threaded insert lands in the hardwood cleat instead of straddling the plywood
edge.

## 3. What to ask for at the cut desk

Their panel saw is **±1/8″**. That is fine for breaking a sheet down and
useless for a part that has to meet a $61 face plate with fixed hole positions.
So the cuts below are **breakdown only, all landing in waste** — the script
proves no part straddles one.

| | | Why |
|---|---|---|
| **1** | crosscut at **48″** | The cut that actually matters. A 4×8 of ½″ is ~48 lb and fits in nothing. Gives two 4×4 halves — one to work, one spare. |
| **2** | rip one half at **25″** | Leaves a 25 × 48 working piece holding every part, with 0.9″ of margin. |
| **3** | crosscut that piece at **29.5″** | Optional. Separates the long parts from the short ones so you aren't wrestling 48″ across a table saw. |

Three cuts is inside every store's free allowance; policies vary from a handful
to unlimited, and cuts beyond it run $0.25–0.50.

**Do not ask them to cut parts to size.** Not the 3.132″ strips, not the rear
panel. That is the whole point of the split above.

## 4. Then, on a table saw

Cut in this order. Rips before crosscuts, and **cut the sides first** so you can
measure the real cavity before committing the parts that have to fit it.

1. Rip the 25″ piece into strips: **3.132** ×3, **1.500** ×2, **4.000** ×1.
2. Crosscut **P2 side panels** to 28.690 ×2 — the only two parts that never move.
3. Dry-assemble the tube. **Measure the actual cavity.**
4. Cut **P3**, **P4**, **P9** and all cleats to what you measured, not to the
   printed number. The script's values are the prediction; the box is the truth.
5. Rip cleats from the 1×4: **0.750 square**, 12.5 ft total.

## 5. MDF for the rear panel

**It works, and for a specific reason: P4 carries no load.** The monitor hangs on
the P9 VESA rails, which land on the cavity top and bottom. P4 is a dust cover
and a service hatch, held by six thumbscrews that pass *through* it into inserts
in the cleats — no fastener ever goes into an MDF edge, which is the one thing
MDF is genuinely bad at.

What it buys: dead flat, zero voids, no seasonal movement across a 13.8″ width,
the best paint surface of any sheet good, and an **actual 0.500″** thickness
instead of plywood's nominal-but-not-really. The depth chain doesn't care —
anything up to **0.763″** clears the VESA rail:

```bash
python3 make-cutlist.py --rear 0.500     # 0.263" clearance, all checks pass
```

> ⚠️ **Only true while P9 exists.** If anyone deletes the VESA rails and bolts
> the monitor through the back — which is exactly what the shelved variant K
> does — then ten pounds of glass hangs on four M4 bolts in MDF face, and MDF is
> the wrong material for that. The script prints this warning whenever `--rear`
> is used.

**Whether to buy it is a different question from whether it works.** Taking P4
out of the nest shrinks the birch requirement to ~11.5 × 48 — a 2×4 panel — but
Home Depot's small panels are terrible value:

| | | |
|---|---|---|
| **One 4×8 PureBond, everything** | **$59.98** | $1.87/sq ft, plus a complete spare half |
| Birch 2×4 + MDF 2×4, both new | $67.34 | more money, no spare |
| Birch 2×4 + **MDF you already have** | $39.86 | saves $20, no spare |

So: **if there's ½″ MDF on the scrap rack at CDL, use it** — it's a better rear
panel than plywood and it's free. If you'd have to buy it, the 4×8 birch sheet
is cheaper per square foot than anything else in the aisle and does the whole
job. MDF's best quality is its paint surface, and P4 is the one panel nobody
ever sees.

Seal MDF on all six faces regardless. Unsealed edges drink finish and swell if
they ever meet water.

## 6. A change to record if you take it

Sheet 302 draws **P5 / P6 / P7 at 1.000″ square**. This plan uses **0.750″
throughout**, which is what a 1×4 gives you when ripped — no glue-up, no 5/4
stock, no hardwood square dowel of doubtful straightness.

It costs nothing measurable: the insert still lands 92 % in the cleat, and 0.750″
is still 0.31″ deeper than the insert needs. It changes P6 and P7 to 12.932″
long. Run `--cleat 1.000` to price the drawing exactly instead.

## 7. What Home Depot will not have

- **#8-32 brass threaded inserts for wood** (21) — Rockler or McMaster
- **#8-32 button-head pin-torx screws, black** (15) — McMaster
- **30 mm anti-vandal switches** (3) — still the gate on the face plate order
- **M4 × 12 bolts** (4) — HD carries some metric, worth a look

Sources: [PureBond ½″ 4×8](https://www.homedepot.com/p/Columbia-Forest-Products-1-2-in-x-4-ft-x-8-ft-PureBond-Birch-Plywood-833185/100020218)
