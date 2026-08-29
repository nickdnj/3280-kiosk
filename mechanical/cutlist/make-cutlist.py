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
ap.add_argument('--kerf',  type=float, default=0.125, help='table saw kerf')
ap.add_argument('--panel', type=float, nargs=2, default=[48.0, 96.0],
                metavar=('W', 'L'), help='sheet bought')
ap.add_argument('--rip',   type=float, default=25.0, help='Home Depot rip line')
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

T, C, K = a.ply, a.cleat, a.kerf

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
         ('P9', VESA_W, CAV_H), ('P9', VESA_W, CAV_H),
         ('P4', REAR_W, REAR_H)]
band2 = [('P3', TUBE_D, CAV_W), ('P3', TUBE_D, CAV_W), ('P10', TRAY[0], TRAY[1])]

b1_w = sum(p[1] for p in band1) + K*(len(band1) - 1)
b2_w = sum(p[1] for p in band2) + K*(len(band2) - 1)
b1_l = max(p[2] for p in band1)
b2_l = max(p[2] for p in band2)
CROSS = math.ceil((b1_l + K + 0.4) * 2) / 2      # HD crosscut, rounded up to 1/2"

# ── report ──────────────────────────────────────────────────────────────────
print(f"""
MEASURED PLY {T:.3f}"   CLEAT {C:.3f}" sq   KERF {K:.3f}"
cavity {CAV_W:.3f} x {CAV_H:.3f}
""")
print("PLYWOOD                     width      length     qty")
for n, w, l, q in PLY:
    print(f"  {n:<24} {w:7.3f}    {l:7.3f}    x{q}")
print(f"\nCLEATS  {C:.3f}\" square hardwood         length     qty")
for n, l, q in CLEATS:
    print(f"  {n:<24}            {l:7.3f}    x{q}")
cl_total = sum(l*q for _, l, q in CLEATS)
print(f"  {'':24}            {cl_total:7.1f}\"   total  ({cl_total/12:.1f} ft)")

HALVE = PL/2 if PL > 60 else None
print("HOME DEPOT CUT DESK")
n = 0
if HALVE:
    n += 1
    print(f"  {n}. CROSSCUT at {HALVE:.0f}\"  -> two {PW:.0f} x {HALVE:.0f} halves.")
    print(f"     A 4x8 of 1/2\" is ~48 lb and fits nothing. This is the cut that")
    print(f"     matters; the second half is a complete spare set of parts.")
n += 1
print(f"  {n}. RIP at {a.rip:.1f}\" down one half -> {a.rip:.1f} x {HALVE or PL:.0f} working piece")
n += 1
print(f"  {n}. CROSSCUT that piece at {CROSS:.1f}\"   (optional -- separates the long")
print(f"     parts from the short ones, saves you wrestling 48\" on the saw)")
print(f"""
  Nothing else. Their panel saw is +/- 1/8" and every cut above lands in waste.
  Every finished dimension is cut on a table saw, by you.
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
air = OA_D - T_ACM - 0.100 - MON_T - 2*T
ok("depth chain still closes", air > 0.15, f"{air:.3f}\" air behind the monitor")
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
ok("every part inside the sheet",
   all(p[0] + p[2] <= a.rip and p[1] + p[3] <= HALF for p in nest),
   f"{len(nest)} parts")

# ── nesting diagram ─────────────────────────────────────────────────────────
S, M = 0.155, 0.55
DL = HALF
W, H = PW*S + 2*M, DL*S + 2*M + 0.5
o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}in" height="{H}in" '
     f'viewBox="0 0 {W:.3f} {H:.3f}"><rect width="100%" height="100%" fill="#FFFFFF"/>',
     f'<rect x="{M}" y="{M}" width="{PW*S:.3f}" height="{DL*S:.3f}" '
     f'fill="#F4F5F6" stroke="#111" stroke-width="0.022"/>']

def put(x, y, w, l, lab):
    o.append(f'<rect x="{M+x*S:.3f}" y="{M+y*S:.3f}" width="{w*S:.3f}" height="{l*S:.3f}" '
             f'fill="#FFFFFF" stroke="#111" stroke-width="0.014"/>')
    o.append(f'<text x="{M+(x+w/2)*S:.3f}" y="{M+(y+l/2)*S+0.05:.3f}" font-size="0.13" '
             f'font-family="Helvetica,Arial" text-anchor="middle" fill="#111">{lab}</text>')

x = 0.0
for lab, w, l in band1:
    put(x, 0.0, w, l, lab); x += w + K
x = 0.0
for lab, w, l in band2:
    put(x, CROSS + K, w, l, lab); x += w + K
for pos, lbl in ((a.rip, f'HD rip {a.rip:.1f}"'), ):
    o.append(f'<line x1="{M+pos*S:.3f}" y1="{M:.3f}" x2="{M+pos*S:.3f}" '
             f'y2="{M+DL*S:.3f}" stroke="#B3261E" stroke-width="0.028" '
             f'stroke-dasharray="0.14 0.08"/>')
    o.append(f'<text x="{M+pos*S+0.09:.3f}" y="{M+0.30:.3f}" font-size="0.14" '
             f'font-family="Helvetica,Arial" fill="#B3261E">{lbl}</text>')
o.append(f'<line x1="{M:.3f}" y1="{M+CROSS*S:.3f}" x2="{M+a.rip*S:.3f}" '
         f'y2="{M+CROSS*S:.3f}" stroke="#B3261E" stroke-width="0.028" '
         f'stroke-dasharray="0.14 0.08"/>')
o.append(f'<text x="{M+a.rip*S+0.09:.3f}" y="{M+CROSS*S-0.07:.3f}" font-size="0.14" '
         f'font-family="Helvetica,Arial" fill="#B3261E">HD crosscut {CROSS:.1f}"</text>')
o.append(f'<text x="{M:.3f}" y="{H-0.18:.3f}" font-size="0.145" '
         f'font-family="Helvetica,Arial" fill="#111">'
         f'working half: {PW:.0f} x {DL:.0f} x {T:.3f} PureBond birch  |  red = Home Depot  |  '
         f'everything else on a table saw</text>')
o.append('</svg>')
open('nesting.svg', 'w').write('\n'.join(o))
print(f"\n  nesting.svg written")
print("\nALL CHECKS PASS\n" if not fails else f"\n{len(fails)} FAILED: {fails}\n")
