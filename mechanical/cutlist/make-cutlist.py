#!/usr/bin/env python3
"""
Home Depot buy plan and cut list for the Rev 1 box.

Nominal "1/2 inch" plywood is not 0.500. Home Depot's is usually 15/32 (0.469),
and it varies sheet to sheet -- so almost every length in the box is derived
from the thickness you actually measure, not from a drawing number.

    python3 make-cutlist.py                # assume 0.469, the usual case
    python3 make-cutlist.py --ply 0.500    # true 1/2, e.g. real Baltic birch
    python3 make-cutlist.py --ply 0.472    # 12 mm

Emits the cut list, the checks, and nesting.svg.
"""
import argparse, math

ap = argparse.ArgumentParser()
ap.add_argument('--ply',   type=float, default=0.469, help='MEASURED panel thickness')
ap.add_argument('--cleat', type=float, default=0.750, help='cleat stock, square')
ap.add_argument('--rear', type=float, default=None,
                help='rear panel thickness if it is a different sheet (e.g. 0.500 MDF)')
ap.add_argument('--kerf',  type=float, default=0.125, help='table saw kerf')
ap.add_argument('--panel', type=float, nargs=2, default=[24.0, 48.0],
                metavar=('W', 'L'), help='sheet bought')
ap.add_argument('--rip',   type=float, default=None,
                help='Home Depot rip line (default: derived from the nest)')
a = ap.parse_args()

# ── fixed by the released package — do not derive these ─────────────────────
OA_W, OA_H, OA_D = 15.370, 28.690, 3.250
T_ACM   = 0.118
TUBE_D  = OA_D - T_ACM                 # 3.132, the box depth behind the face
EDGE    = 0.625                        # P1 mount holes, in from the edge
INSERT  = 0.375                        # #8-32 brass insert, outside diameter
MON_OW, MON_OH, MON_T = 12.870, 21.440, 1.800
VESA_W  = 1.500
TRAY    = (4.000, 2.900)
REAR_CL = 0.100                        # rear panel clearance, total across each axis

BUY = [
 ('ProWood 1/2 in. x 2 ft. x 4 ft. Birch Plywood Project Panel', '154153', 39.86, 1,
  'P2 P3 P9 P10 -- the box'),
 ('ProWood 1/2 in. x 2 ft. x 4 ft. MDF Project Panel',           '109097', 27.48, 1,
  'P4 -- the rear cover'),
 ('Poplar or red oak 1x4, 8 ft (hardwood rack)',                 '--',      0.00, 1,
  'P5 P6 P7 P8 -- 12.5 ft of cleat'),
 ('Titebond II, 120 + 180 grit, #6 x 1-1/4 wood screws (40)',     '--',      0.00, 1,
  'assembly'),
]

T, C, K = a.ply, a.cleat, a.kerf
T4 = a.rear if a.rear else T          # P4 need not match the box

# ── everything else follows from T ──────────────────────────────────────────
CAV_W, CAV_H = OA_W - 2*T, OA_H - 2*T
REAR_W, REAR_H = CAV_W - REAR_CL, CAV_H - REAR_CL
CLH = CAV_W - 2*C                       # horizontal cleats span between verticals

PLY = [   # name, w, l, qty
    ('P2  SIDE PANEL',        TUBE_D, OA_H,   2),
    ('P3  TOP / BOTTOM',      TUBE_D, CAV_W,  2),
    ('P4  REAR PANEL',        REAR_W, REAR_H, 1),
    ('P9  VESA RAIL',         VESA_W, CAV_H,  2),
    ('P10 PI TRAY',           TRAY[0], TRAY[1], 1),
]
CLEATS = [
    ('P5  FRONT CLEAT, VERT', CAV_H, 2),
    ('P6  FRONT CLEAT, HORIZ', CLH,  2),
    ('P7  BUTTON RAIL',       CLH,   1),
    ('P8  REAR CLEAT, VERT',  CAV_H, 2),
]

# ── nesting: band 1 holds everything 27"+ long, band 2 the short parts ───────
PW, PL = a.panel
band1 = [('P2', TUBE_D, OA_H), ('P2', TUBE_D, OA_H),
         ('P9', VESA_W, CAV_H), ('P9', VESA_W, CAV_H)]
if not a.rear:
    band1.append(('P4', REAR_W, REAR_H))
band2 = [('P3', TUBE_D, CAV_W), ('P3', TUBE_D, CAV_W), ('P10', TRAY[0], TRAY[1])]

b1_w = sum(p[1] for p in band1) + K*(len(band1) - 1)
b2_w = sum(p[1] for p in band2) + K*(len(band2) - 1)
b1_l = max(p[2] for p in band1)
b2_l = max(p[2] for p in band2)
CROSS = math.ceil((b1_l + K + 0.4) * 2) / 2      # HD crosscut, rounded up to 1/2"
if a.rip is None:                               # 0.9" of margin on the panel saw
    a.rip = math.ceil((max(b1_w, b2_w) + 0.9) * 2) / 2

# ── report ──────────────────────────────────────────────────────────────────
print(f"""
MEASURED PLY {T:.3f}"   CLEAT {C:.3f}" sq   KERF {K:.3f}"
cavity {CAV_W:.3f} x {CAV_H:.3f}
""")
print(f"PLYWOOD  ({T:.3f}\")             width      length     qty"
      + (f"        <- P4 is {T4:.3f}\" from a separate sheet" if a.rear else ""))
for n, w, l, q in PLY:
    print(f"  {n:<24} {w:7.3f}    {l:7.3f}    x{q}")
print(f"\nCLEATS  {C:.3f}\" square hardwood         length     qty")
for n, l, q in CLEATS:
    print(f"  {n:<24}            {l:7.3f}    x{q}")
cl_total = sum(l*q for _, l, q in CLEATS)
print(f"  {'':24}            {cl_total:7.1f}\"   total  ({cl_total/12:.1f} ft)")

HALVE = PL/2 if PL > 60 else None
PROJECT_PANEL = PW <= 24.5 and PL <= 48.5
print("HOME DEPOT CUT DESK")
if PROJECT_PANEL:
    print("  None. Two 2x4 project panels fit in a car and on a table saw.")
    print("  Every cut below is yours, which is the point -- their panel saw is +/- 1/8\"")
    print("  and the face plate's hole pattern is already fixed.")
else:
    n = 0
if HALVE and not PROJECT_PANEL:
        n += 1
        print(f"  {n}. CROSSCUT at {HALVE:.0f}\"  -> two {PW:.0f} x {HALVE:.0f} halves.")
        print(f"     A 4x8 of 1/2\" is ~48 lb and fits nothing. This is the cut that")
        print(f"     matters; the second half is a complete spare set of parts.")
if not PROJECT_PANEL:
    n += 1
    print(f"  {n}. RIP at {a.rip:.1f}\" down one half -> {a.rip:.1f} x {HALVE or PL:.0f} working piece")
    n += 1
    print(f"  {n}. CROSSCUT that piece at {CROSS:.1f}\"   (optional)")
    print("\n  Every cut above lands in waste. Every finished dimension is yours.\n")
if a.rear:
    print(f"""  !! P4 IS A COVER, NOT A STRUCTURE -- the monitor hangs on the P9 VESA
     rails, which is the ONLY reason a {T4:.3f}" MDF back is safe here. If anyone
     ever deletes P9 and bolts the monitor through P4, this stops being true.
""")

fails = []
def ok(label, cond, detail):
    if not cond: fails.append(label)
    print(f"  {label:<46} {detail:<26} {'OK' if cond else '*** FAIL ***'}")

print("CHECKS")
ok("band 1 fits the ripped piece", b1_w + K <= a.rip,
   f"{b1_w:.3f}\" in {a.rip:.1f}\"")
ok("band 2 fits the ripped piece", b2_w + K <= a.rip,
   f"{b2_w:.3f}\" in {a.rip:.1f}\"")
HALF = PL/2 if PL > 60 else PL
ok("both bands fit the working half", CROSS + K + b2_l <= HALF,
   f"{CROSS + K + b2_l:.3f}\" in {HALF:.0f}\"")
ok("HD crosscut lands clear of band 1", CROSS > b1_l + K,
   f"{CROSS:.1f}\" > {b1_l + K:.3f}\"")
ok("band 2 still fits after the crosscut", HALF - CROSS - K >= b2_l,
   f"{HALF - CROSS - K:.3f}\" >= {b2_l:.3f}\"")
ok("P1 mount hole lands in wall + cleat", EDGE + INSERT/2 <= T + C,
   f"{EDGE + INSERT/2:.3f}\" in {T + C:.3f}\"")
ok("insert sits mostly in the cleat, not the ply edge",
   (min(T + C, EDGE + INSERT/2) - max(T, EDGE - INSERT/2)) / INSERT > 0.5,
   f"{(min(T+C, EDGE+INSERT/2) - max(T, EDGE-INSERT/2))/INSERT*100:.0f}% in cleat")
rail_back = T_ACM + 0.100 + MON_T + T          # back face of the P9 VESA rail
air = (OA_D - T4) - rail_back
ok("depth chain still closes", air > 0.15,
   f"{air:.3f}\" between the VESA rail and a {T4:.3f}\" back")
ok("rear panel thickness is free to differ", T4 < OA_D - rail_back,
   f"{T4:.3f}\" < {OA_D - rail_back:.3f}\" max")
ok("monitor clears the cavity", CAV_W - MON_OW > 0.5, f"{(CAV_W-MON_OW)/2:.3f}\"/side")
ok("cleat deep enough for the insert", C >= 0.44 + 0.10, f"{C:.3f}\"")
ok("horizontal cleats have positive length", CLH > 6.0, f"{CLH:.3f}\"")
ok("one poplar 1x4 x 6ft yields every cleat", 4 * 72 >= cl_total,
   f"288\" available, {cl_total:.0f}\" needed")

nest = ([(x0, 0.0, w, l) for x0, (_, w, l) in
         zip([sum(p[1] for p in band1[:i]) + K*i for i in range(len(band1))], band1)]
      + [(x0, CROSS + K, w, l) for x0, (_, w, l) in
         zip([sum(p[1] for p in band2[:i]) + K*i for i in range(len(band2))], band2)])
crossed = [p for p in nest if p[0] < a.rip < p[0] + p[2] or p[1] < CROSS < p[1] + p[3]]
ok("no part straddles a Home Depot cut", not crossed, f"{len(crossed)} straddling")
if a.rear:
    ok("P4 fits the second panel", REAR_W <= PW and REAR_H <= PL,
       f"{REAR_W:.3f} x {REAR_H:.3f} in {PW:.0f} x {PL:.0f}")
ok("every part inside the sheet",
   all(p[0] + p[2] <= a.rip and p[1] + p[3] <= HALF for p in nest),
   f"{len(nest)} parts")

# ── nesting diagram ─────────────────────────────────────────────────────────
S, M, GAP = 0.135, 0.50, 0.55
sheets = 2 if a.rear else 1
DL = HALF if HALVE else PL
W = M*2 + sheets*PW*S + (GAP if sheets > 1 else 0)
H = DL*S + 2*M + 0.45
o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}in" height="{H}in" '
     f'viewBox="0 0 {W:.3f} {H:.3f}"><rect width="100%" height="100%" fill="#FFFFFF"/>']

def sheet(ox, label):
    o.append(f'<rect x="{ox:.3f}" y="{M:.3f}" width="{PW*S:.3f}" height="{DL*S:.3f}" '
             f'fill="#F4F5F6" stroke="#111" stroke-width="0.020"/>')
    o.append(f'<text x="{ox:.3f}" y="{M-0.12:.3f}" font-size="0.135" '
             f'font-family="Helvetica,Arial" font-weight="bold" fill="#111">{label}</text>')

def put(ox, x, y, w, l, lab):
    o.append(f'<rect x="{ox+x*S:.3f}" y="{M+y*S:.3f}" width="{w*S:.3f}" height="{l*S:.3f}" '
             f'fill="#FFFFFF" stroke="#111" stroke-width="0.013"/>')
    o.append(f'<text x="{ox+(x+w/2)*S:.3f}" y="{M+(y+l/2)*S+0.045:.3f}" font-size="0.115" '
             f'font-family="Helvetica,Arial" text-anchor="middle" fill="#111">{lab}</text>')

o1 = M
sheet(o1, f'BIRCH  {PW:.0f} x {DL:.0f} x {T:.3f}')
x = 0.0
for lab, w, l in band1:
    put(o1, x, 0.0, w, l, lab); x += w + K
x = 0.0
for lab, w, l in band2:
    put(o1, x, CROSS + K, w, l, lab); x += w + K
if not PROJECT_PANEL:
    o.append(f'<line x1="{o1+a.rip*S:.3f}" y1="{M:.3f}" x2="{o1+a.rip*S:.3f}" '
             f'y2="{M+DL*S:.3f}" stroke="#B3261E" stroke-width="0.024" '
             f'stroke-dasharray="0.12 0.07"/>')

if a.rear:
    o2 = M + PW*S + GAP
    sheet(o2, f'MDF  {PW:.0f} x {DL:.0f} x {T4:.3f}')
    put(o2, 0.0, 0.0, REAR_W, REAR_H, 'P4')

o.append(f'<text x="{M:.3f}" y="{H-0.14:.3f}" font-size="0.125" '
         f'font-family="Helvetica,Arial" fill="#111">'
         f'grain / face runs top-to-bottom  |  no Home Depot cuts  |  '
         f'all dimensions on a table saw</text>')
o.append('</svg>')
open('nesting.svg', 'w').write('\n'.join(o))

# ── store card ──────────────────────────────────────────────────────────────
tot = sum(p[2]*p[3] for p in BUY)
md = [f"""# Shopping list — 3280 kiosk box

> Generated by `make-cutlist.py`. Prices seen at West Long Branch 2026-08-29.
> Assumes birch measures **{T:.3f}"** and MDF **{T4:.3f}"** — *measure before cutting.*

## Buy
""", "| Item | Model | Price |", "|---|---|---|"]
for name, model, usd, qty, use in BUY:
    price = f"${usd:.2f}" if usd else "~$20"
    md.append(f"| {name}<br>*{use}* | {model} | {price} |")
md += [f"| | **panels** | **${tot:.2f}** |", "",
       "**No cut desk.** Both panels fit in a car. Their saw is ±1/8\" and the face",
       "plate's hole pattern is already fixed, so every dimension below is yours.",
       "",
       f"The birch nest uses {max(b1_w, b2_w):.1f}\" of the panel's {PW:.0f}\", leaving a "
       f"{PW - max(b1_w, b2_w) - K:.1f} x {PL:.0f}\" strip —",
       "enough for a **complete second set of box parts** if you spoil one. There is no",
       "spare P4; a second rear panel would need another MDF sheet.",
       "",
       "Check the birch panel's cut edges in the store and pick one without voids —",
       "the box corners take edge screws.",
       "", "## Measure first", "",
       f'Calipers in four places on each panel. Re-run with what you find:', "",
       "```bash", "python3 make-cutlist.py --panel 24 48 \\",
       f"        --ply <birch> --rear <mdf>", "```", "",
       "Only P2, P10 and the depth are thickness-independent. Everything else moves.",
       "", f"## Cut list — birch panel ({T:.3f}\")", "",
       "| Part | Width | Length | Qty |", "|---|---|---|---|"]
for n, w, l, q in PLY:
    if n.startswith('P4'): continue
    md.append(f"| {n} | {w:.3f} | {l:.3f} | ×{q} |")
md += ["", f"## Cut list — MDF panel ({T4:.3f}\")", "",
       "| Part | Width | Length | Qty |", "|---|---|---|---|",
       f"| P4  REAR PANEL | {REAR_W:.3f} | {REAR_H:.3f} | ×1 |", "",
       f"## Cut list — cleats, {C:.3f}\" square, from the 1x4", "",
       "| Part | Length | Qty |", "|---|---|---|"]
for n, l, q in CLEATS:
    md.append(f"| {n} | {l:.3f} | ×{q} |")
md += [f"| | **{cl_total:.1f}\" total** | |", "",
       "## Order of operations", "",
       "1. Rip the birch: **3.132** ×3, **1.500** ×2, **4.000** ×1.",
       "2. Crosscut **P2** ×2 to **28.690** — the only parts that never move.",
       "3. Dry-assemble the tube. **Measure the real cavity.**",
       "4. Cut P3, P9, P4 and the cleats to what you measured, not to this table.",
       "5. Rip cleats from the 1x4 at 0.750 square.",
       "", "## Not at Home Depot", "",
       "- #8-32 brass threaded inserts for wood (21) — Rockler / McMaster",
       "- #8-32 button-head pin-torx screws, black (15) — McMaster",
       "- **30 mm anti-vandal switches (3)** — still the gate on the face plate order",
       ""]
open('SHOPPING.md', 'w').write('\n'.join(md))
print(f"\n  nesting.svg + SHOPPING.md written   (panels ${tot:.2f})")
print("\nALL CHECKS PASS\n" if not fails else f"\n{len(fails)} FAILED: {fails}\n")
