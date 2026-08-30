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
import argparse, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'fab-rev1'))
import _p1 as P1                      # the face plate is the single source of truth

ap = argparse.ArgumentParser()
ap.add_argument('--ply',   type=float, default=0.750, help='MEASURED box stock thickness')
ap.add_argument('--cleat', type=float, default=0.750, help='cleat stock, square')
ap.add_argument('--back', choices=['inset', 'tacked'], default='tacked',
                help='inset = P4 drops into the cavity on rear cleats; '
                     'tacked = P4 screws onto the back of the tube')
ap.add_argument('--air', type=float, default=0.100, help='air behind the VESA rail')
ap.add_argument('--allow-rip', dest='allow_rip', action='store_true',
                help='allow ripping (the earlier plans). Default is crosscuts only: '
                     'board WIDTH becomes the box depth and nothing is ripped.')
ap.add_argument('--cleatboard', type=float, default=2.5,
                help='actual width of the cleat/rail stock (1x3 = 2.5, 1x2 = 1.5)')
ap.add_argument('--board', type=float, default=3.5,
                help='ACTUAL width of the 1x stock: 3.5 for 1x4, 5.5 for 1x6')
ap.add_argument('--stock', choices=['solid', 'ply'], default='solid',
                help='solid 1x lumber (the plan) or a plywood sheet (the alternative)')
ap.add_argument('--rear', type=float, default=0.500,
                help='rear panel thickness if it is a different sheet (e.g. 0.500 MDF)')
ap.add_argument('--kerf',  type=float, default=0.125, help='table saw kerf')
ap.add_argument('--panel', type=float, nargs=2, default=[24.0, 48.0],
                metavar=('W', 'L'), help='sheet bought')
ap.add_argument('--rip',   type=float, default=None,
                help='Home Depot rip line (default: derived from the nest)')
a = ap.parse_args()

# ── all of this comes from the face plate. Change ../fab-rev1/_p1.py. ───────
OA_W, OA_H = P1.PW, P1.PH              # 15 x 30, whole
OA_D    = 3.250                        # recomputed from the stock in --norip
T_ACM   = P1.MAT_T
TUBE_D  = OA_D - T_ACM
EDGE    = P1.EDGE                      # P1 mount holes, 1/2 in from the edge
INSERT  = 0.375                        # #8-32 brass insert, outside diameter
MON_OW, MON_OH, MON_T = P1.MON_OW, P1.MON_OH, P1.MON_T
MON_TOP = P1.MON_TOP
Z_GAP   = P1.GAP                # ACM back face to the bezel face. Set in _p1.
# The window is centred on the plate and the PICTURE is centred on the
# window, so the CASING is not centred: it shifts toward the chin side.
MON_L   = P1.ACT_X - P1.BEZ_CHIN               # casing left edge, chin left
MON_SHIFT = P1.MON_SHIFT
VESA_W  = 1.500
TRAY    = (4.000, 3.000)               # rounded with the rest
REAR_CL = 0.250                        # rear panel clearance; Home Depot cuts it

BUY_PLY = [
 ('ProWood 1/2 in. x 2 ft. x 4 ft. Birch Plywood Project Panel', '154153', 39.86, 1,
  'P2 P3 P9 P10 -- the box'),
 ('ProWood 1/2 in. x 2 ft. x 4 ft. MDF Project Panel',           '109097', 27.48, 1,
  'P4 -- the rear cover'),
 ('Poplar or red oak 1x4, 8 ft (hardwood rack)',                 '--',      0.00, 1,
  'P5 P6 P7 P8 -- 12.5 ft of cleat'),
 ('Titebond II, 120 + 180 grit, #6 x 1-1/4 wood screws (40)',     '--',      0.00, 1,
  'assembly'),
]
BUY_SOLID = [
 ('1x4 x 8 ft Kiln-Dried Whitewood Common (actual .750 x 3.5)',   '914681',  9.53, 2,
  'P2 P3 -- the tube, at full width. 1 needed, 1 spare. SIGHT DOWN EACH BOARD'),
 ('1x3 x 8 ft Kiln-Dried Whitewood Common (actual .750 x 2.5)',   '914649',  7.44, 3,
  'P7 P8 P9 -- at full width. 2 needed, 1 spare'),
 ('ProWood 1/2 in. x 2 ft. x 4 ft. MDF Project Panel',           '109097', 27.48, 1,
  'P4 rear cover' ),
 ('Titebond II, 120 + 180 grit, #6 x 1-1/4 wood screws (40)',     '--',      0.00, 1,
  'assembly'),
]

BW = a.board                              # 1x4 = 3.5 actual, 1x6 = 5.5
BUY = BUY_SOLID if (a.stock == 'solid') else BUY_PLY
T, C, K = a.ply, a.cleat, a.kerf
CW = a.cleatboard        # cleat stock width, used as-is
T4 = a.rear if a.rear else T          # P4 need not match the box

# ── everything else follows from T ──────────────────────────────────────────
NORIP = not a.allow_rip
NO_FRONT_CLEATS = False
if NORIP:
    REAR_CL = 0.250                     # deliberately loose: Home Depot cuts it
    # No board is ever ripped. The 1x4's 3.5" WIDTH becomes the tube depth,
    # and the cleats/rails are 1x stock used at full width. The back must be
    # inset -- tacked on it would put the enclosure past the ADA 4.000" cap
    # on its own, before any mounting adapter.
    TUBE_D = a.board
    OA_D   = T_ACM + TUBE_D
    C      = T                      # a cleat intrudes by its board THICKNESS
    a.back = 'inset'
    NO_FRONT_CLEATS = True          # see the monitor-clearance check below

TACK = a.back == 'tacked'
if TACK:
    # A tacked back screws onto the tube's rear edges, so the tube only has to
    # be as deep as what lives inside it, and the depth budget is recomputed.
    TUBE_D = Z_GAP + MON_T + T + a.air
    OA_D   = T_ACM + TUBE_D + T4

CAV_W, CAV_H = OA_W - 2*T, OA_H - 2*T
REAR_W, REAR_H = ((OA_W, OA_H) if TACK else (CAV_W - REAR_CL, CAV_H - REAR_CL))
CLH = CAV_W - 2*C                       # verticals intrude by C, not by their width

PLY = [   # name, w, l, qty
    ('P2  SIDE PANEL',        TUBE_D, OA_H,   2),
    ('P3  TOP / BOTTOM',      TUBE_D, CAV_W,  2),
    ('P4  REAR PANEL',        REAR_W, REAR_H, 1),
    ('P10 PI TRAY',           TRAY[0], TRAY[1], 1),
]
if not NORIP:
    PLY.insert(3, ('P9  VESA RAIL', VESA_W, CAV_H, 2))
CLEATS = ([('P7  BUTTON RAIL', CAV_W, 1)] if NO_FRONT_CLEATS else [
    ('P5  FRONT CLEAT, VERT', CAV_H, 2),
    ('P6  FRONT CLEAT, HORIZ', CLH,  2),
    ('P7  BUTTON RAIL',       CLH,   1),
])
if not TACK:                               # a tacked back screws to the tube edges
    CLEATS.append(('P8  REAR CLEAT, VERT', CAV_H, 2))
if NORIP:
    CLEATS.append(('P9  VESA RAIL',        CAV_H, 2))

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

if NORIP:
    BL = 96.0
    tube_run = 2*OA_H + 2*CAV_W
    nboards  = math.ceil(cl_total / (BL - 2)) + 1     # +1 spare; cost is not the constraint
    print(f"""CROSSCUT-ONLY PLAN   zero rips

  1x4 x 8 ft  (actual {T:.3f} x {a.board})   -- the tube, at full width
      P2 {OA_H:.3f} x2  +  P3 {CAV_W:.3f} x2        {tube_run:.0f}" of {BL:.0f}"

  1x2 x 8 ft  (actual {T:.3f} x {CW})   x{nboards}  -- at full width, no rip
      {chr(10) + "      " if False else ""}{"   ".join(n.split()[0] + " " + format(l, ".3f") + " x" + str(q) for n, l, q in CLEATS)}
                                            {cl_total:.0f}" of {nboards*(BL-2):.0f}"

  1/2" MDF 2x4     -- P4 {REAR_W:.3f} x {REAR_H:.3f}  +  P10 {TRAY[0]:.3f} x {TRAY[1]:.3f}

  {4 + sum(q for _, _, q in CLEATS)} crosscuts in wood. No rips, no front cleats.
  A mitre saw does all of it. HOME DEPOT CUTS THE MDF -- the rear panel is
  deliberately {REAR_CL:.3f}" undersize, so their +/- 1/8" cannot matter.
""")

elif a.stock == 'solid':
    BL = 96.0                                # 8 ft
    tube = 2*OA_H + 2*CAV_W
    rails = 2*CAV_H
    nA = int((BW - TUBE_D - K) // (C + K))      # cleat strips beside the tube strip
    P10CUT = math.ceil(TRAY[1] + 0.2) if TRAY[0] <= BW else 0.0
    solo = nA*(BL - P10CUT) >= cl_total and 2*OA_H + 2*CAV_W + 3*K <= BL - P10CUT
    print(f"""BOARD PLAN   1x{4 if BW < 4.5 else 6}, actual {BW}" x {BL:.0f}", {T:.3f}" thick

  BOARD A   1x{4 if BW < 4.5 else 6} x 8 ft
    1. crosscut {P10CUT:.0f}" off one end   -> P10 tray {TRAY[0]:.3f} x {TRAY[1]:.3f}
    2. rip the remaining {BL-P10CUT:.0f}" to {TUBE_D:.3f}"
         -> P2 {OA_H:.3f} x2  +  P3 {CAV_W:.3f} x2      ({2*OA_H + 2*CAV_W:.0f}" of {BL-P10CUT:.0f}")
    3. rip the {BW - TUBE_D - K:.3f}" offcut into {nA} x {C:.3f}" cleat strips
         -> {' '.join(n.split()[0] for n, _, _ in CLEATS)}   ({cl_total:.0f}" of {nA*(BL-P10CUT):.0f}")

  BOARD B   1x2 x 8 ft -- already {VESA_W:.3f}" wide, no rip
         -> P9 x2   ({2*CAV_H:.0f}" of {BL:.0f}")

  {'One 1x6 covers the tube, every cleat and the tray.' if solo else
   'Board A cannot carry the cleats -- take them off a second wide board.'}
""")
D_PINE, D_MDF, D_ACM = 0.0162, 0.0278, 0.0080     # lb/in^3, lb/in^2 for 3 mm ACM
w_box  = (2*TUBE_D*OA_H + 2*TUBE_D*CAV_W)*T + cl_total*C*C + TRAY[0]*TRAY[1]*T
w_box += 0.0 if NORIP else 2*VESA_W*CAV_H*T
W_PINE = w_box * D_PINE
W_BACK = REAR_W*REAR_H*T4 * (D_MDF if a.rear else D_PINE)
W_FACE = OA_W*OA_H*D_ACM
W_ALL  = W_PINE + W_BACK + W_FACE + 9.0 + 1.0      # monitor + Pi/PSU/wiring
print(f"WEIGHT   pine {W_PINE:.1f} + back {W_BACK:.1f} + face {W_FACE:.1f} "
      f"+ monitor 9.0 + electronics 1.0 = {W_ALL:.1f} lb\n")

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
in_cleat = (min(T + C, EDGE + INSERT/2) - max(T, EDGE - INSERT/2)) / INSERT
if a.stock == 'solid':
    # A 1x board's front edge is SIDE grain -- the drill axis crosses the grain,
    # which holds an insert well. Plywood's edge is between plies and does not.
    ok("insert lands in side grain, backed by the cleat",
       EDGE - INSERT/2 > 0 and EDGE + INSERT/2 <= T + C,
       f"{max(0.0, in_cleat)*100:.0f}% in cleat, rest in solid edge")
else:
    ok("insert sits mostly in the cleat, not the ply edge", in_cleat > 0.5,
       f"{in_cleat*100:.0f}% in cleat")
rail_back = T_ACM + Z_GAP + MON_T + (T if NORIP else T)
air = (OA_D - T4) - rail_back
ADAPTER = 4.000 - OA_D                        # ADA 307.2 caps total projection
ok("depth chain still closes", air > (a.air*0.99 if TACK else 0.15),
   f"{air:.3f}\" between the VESA rail and a {T4:.3f}\" back")
ok("rear panel thickness is free to differ", T4 <= OA_D - rail_back,
   f"{T4:.3f}\" vs {OA_D - rail_back:.3f}\" available")
if air < (a.air*0.99 if TACK else 0.15):
    print(f"""
  >> DEPTH CONFLICT, {abs(air):.3f}\"
     {T_ACM:.3f} face + {Z_GAP:.3f} gap + {MON_T:.3f} monitor + {T:.3f} rail + {T4:.3f} back
     = {T_ACM + Z_GAP + MON_T + T + T4:.3f}\" against a {OA_D:.3f}\" envelope.
     Do NOT resolve this on paper. MON_T is an ESTIMATE until you own the
     monitor, and it is the largest number in the stack. Cut the tube and the
     cleats now; set the rear cleat position -- and therefore where the rails
     land -- once you can measure the real panel. If it still overruns then,
     the envelope may go to {T_ACM + Z_GAP + MON_T + T + T4:.3f}\": ADA 307.2 caps total
     projection at 4.000\", so the adapter budget goes 0.750 -> {4.0 - (T_ACM + Z_GAP + MON_T + T + T4):.3f}\".
""")
ok("enclosure leaves the adapter a budget", ADAPTER > 0.35,
   f"{OA_D:.3f}\" deep, {ADAPTER:.3f}\" of the 4.000 ADA cap left")
ok("a one-person lift onto the bench", W_ALL < 35, f"{W_ALL:.1f} lb")
if NORIP:
    ok("nothing is ripped", True, f"tube depth = the {a.board}\" board width")
    internal = Z_GAP + MON_T + T + T4
    ok("monitor + rail + inset back fit the tube", internal <= TUBE_D,
       f"{internal:.3f}\" in {TUBE_D:.3f}\"")
    ok("one 1x4 x 8 ft yields the whole tube", 2*OA_H + 2*CAV_W <= 94.0,
       f"{2*OA_H + 2*CAV_W:.0f}\" of 94\"")
    # Front cleats lie 0.719 into the cavity x 1.500 deep. REAR cleats turn 90
    # degrees -- 1.500 into the cavity x 0.719 deep -- so they sit entirely
    # behind the monitor instead of running alongside it.
    ok("rear cleat, turned 90, clears the monitor",
       (OA_D - T4 - T) > (T_ACM + Z_GAP + MON_T),
       f"cleat front {OA_D - T4 - T:.3f}\" vs monitor back {T_ACM + Z_GAP + MON_T:.3f}\"")
    ok("rear panel still lands on the ledge",
       CW - REAR_CL/2 - 0.125 > 0.75,
       f"{CW - REAR_CL/2 - 0.125:.3f}\" of ledge at Home Depot's worst cut")
front_in = 0.0 if NO_FRONT_CLEATS else T + C
# Measure from where the casing ACTUALLY sits, not from the centreline.
_tight = min(MON_L - front_in - T, (OA_W - front_in - T) - (MON_L + MON_OW))
ok("monitor clears the FRONT CLEATS, not just the cavity",
   _tight > 0.03 and (MON_TOP - T - front_in) > 0.10,
   f"{_tight:+.3f}\" on the chin side, "
   f"{MON_TOP - T - front_in:+.3f}\" at the top")
ok("every P1 hole lands in a board edge or the rail",
   EDGE + INSERT/2 <= T + (C if not NO_FRONT_CLEATS else 0) + 0.10,
   "15 of 15" if NO_FRONT_CLEATS else "via cleats")
# Rounding the plate 15.370 -> 15.000 took 0.185"/side out of this margin.
# MON_OW is an ESTIMATE; a true 24.0" panel is wider than the 23.8" we drew.
# The cavity's real limit is not a panel WIDTH -- it is how thick a chin the
# cavity can swallow once the picture is centred. That is the number to take
# shopping, and it shrinks as the panel gets wider.
budget = [(d, (CAV_W - w)/2) for d, w, _ in P1.panels()]
ok("every \"24 inch\" panel leaves a usable chin budget",
   all(b > 0.60 for _, b in budget),
   "  ".join(f'{d:g}:{b:.3f}' for d, b in budget))
ok("monitor clears the cavity, off-centre and all",
   min(MON_L - T, (OA_W - T) - (MON_L + MON_OW)) > 0.03,
   f"{min(MON_L - T, (OA_W - T) - (MON_L + MON_OW)):.4f}\"/side, "
   f"{MON_SHIFT:.3f}\" off centre")
# The chin is the number that decides whether a given monitor fits at all.
ok("chin inside the buy limit", P1.BEZ_CHIN <= (CAV_W - P1.ACT_W)/2,
   f"{P1.BEZ_CHIN:.3f}\" <= {(CAV_W - P1.ACT_W)/2:.3f}\" max")
ok("cleat deep enough for the insert", C >= 0.44 + 0.10, f"{C:.3f}\"")
ok("horizontal cleats have positive length", CLH > 6.0, f"{CLH:.3f}\"")
if a.stock == 'solid' and not NORIP:
    ok("board A yields tube + cleats + P10", 
       2*OA_H + 2*CAV_W + 3*K <= BL - P10CUT and nA*(BL - P10CUT) >= cl_total,
       f"tube {2*OA_H + 2*CAV_W:.0f}\", cleats {cl_total:.0f}\"/{nA*(BL-P10CUT):.0f}\", "
       f"P10 off the first {P10CUT:.0f}\"")
    nstrip = int((BW - VESA_W - K) // (C + K))
    ok("board B rips to a rail strip plus cleat strips",
       nstrip >= 2, f"1 x {VESA_W:.3f} + {nstrip} x {C:.3f} from {BW}\"")
    print(f"  {'board A offcut -> cleats?':<46} "
          f"{(str(nA) + ' strip(s), ' + str(int(nA*BL)) + chr(34)) if nA*BL >= cl_total else 'no, too narrow -- use board B'}")
    ok("board B yields the rails and every cleat",
       2*CAV_H <= BL and cl_total <= nstrip*BL,
       f"rails {2*CAV_H:.0f}\"/{BL:.0f}, cleats {cl_total:.0f}\"/{nstrip*BL:.0f}")
else:
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
if a.stock == 'solid':
    ok("P10 has a source", TRAY[0] <= BW or TRAY[0] <= PW,
       f"{TRAY[0]:.3f}\" -> {'board' if TRAY[0] <= BW else 'MDF panel'}")
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
L = []
def w(x=''): L.append(x)

w("# Shopping list — 3280 kiosk box")
w()
w("> Generated by `make-cutlist.py`. Prices seen at Home Depot West Long Branch,")
w(f"> 2026-08-29. Assumes the boards measure **{T:.3f}\"** and the MDF **{T4:.3f}\"** —")
w("> *measure before cutting.*")
w()
w("## Buy")
w()
w("| Item | Model | Qty | Price |")
w("|---|---|---|---|")
for name, model, usd, qty, use in BUY:
    price = f"${usd*qty:.2f}" if usd else "~$20"
    w(f"| {name}<br>*{use}* | {model} | ×{qty} | {price} |")
w(f"| | | | **${tot:.2f}** |")
w()
if NORIP:
    w("**Zero rips.** Every board is used at its full width, so the only wood cuts are")
    w(f"**{4 + sum(q for _, _, q in CLEATS)} crosscuts** — a mitre saw does all of it.")
    w()
    w("**Home Depot cuts the MDF.** The rear panel is deliberately "
      f"{REAR_CL:.3f}\" undersize and")
    w(f"lands on a {CW:.3f}\" ledge, so their ±1/8\" cannot matter. Ask for:")
    w()
    w(f"- **P4 rear panel — {REAR_W:.3f} × {REAR_H:.3f}**")
    w(f"- **P10 Pi tray — {TRAY[0]:.3f} × {TRAY[1]:.3f}**")
w()
w("## Measure first")
w()
w("Calipers in four places on a board. If it differs, re-run:")
w()
w("```bash")
w("python3 make-cutlist.py --ply <board> --rear <mdf>")
w("```")
w()
w(f"## Cut — 1x4, at full width ({a.board}\")")
w()
w("| Part | Width | Length | Qty |")
w("|---|---|---|---|")
for n, ww_, l, q in PLY:
    if n.startswith(('P4', 'P10')):
        continue
    w(f"| {n} | {ww_:.3f} | {l:.3f} | ×{q} |")
w()
w(f"## Cut — 1x3, at full width ({CW}\")")
w()
w("| Part | Length | Qty |")
w("|---|---|---|")
for n, l, q in CLEATS:
    w(f"| {n} | {l:.3f} | ×{q} |")
w()
w("## From the MDF — Home Depot cuts these")
w()
w("| Part | Size |")
w("|---|---|")
w(f"| P4  REAR PANEL | {REAR_W:.3f} × {REAR_H:.3f} |")
w(f"| P10 PI TRAY | {TRAY[0]:.3f} × {TRAY[1]:.3f} |")
w()
w("## Order of operations")
w()
w(f"1. Crosscut **P2 ×2 to {OA_H:.3f}** — the only parts whose size never moves.")
w("2. Dry-assemble with P3 and **measure the real cavity.**")
w("3. Cut P3, P7, P8, P9 to what you measured, not to the tables above.")
w("4. Glue and screw the tube. **Pilot every hole** — pine end grain splits.")
w(f"5. P7 button rail, front-flush, centreline {P1.RAIL_Y:g}\" below the top edge.")
w("6. P8 rear cleats, **turned 90°** so they sit behind the monitor.")
w("7. Threaded inserts — 15 on P1's pattern. **Epoxy them.**")
w("8. P9 rails, monitor, Pi tray. **Then the foam seal onto the back of P1**,")
w("   then P1, then the back panel.")
w()
w("## Not at Home Depot")
w()
w("- #8-32 brass threaded inserts for wood (15) — Rockler / McMaster")
w("- #8-32 button-head pin-torx screws, black (15) — McMaster")
w("- **30 mm anti-vandal switches (3)** — one of two gates on the face plate order")
w("- **Foam tape, BLACK closed-cell neoprene or EPDM, 1/4\" wide × 3/16\" thick**")
w(f"  — the light seal behind P1; {P1.SEAL_LEN:.0f}\" used, so a 10 ft roll is plenty.")
w("  Check the weatherstripping aisle first. It must be black, closed-cell, and")
w("  **no wider than 1/4\"** — wider tape runs off the bezel and onto the glass.")
w()
w("## Before you buy the monitor")
w()
w("Three numbers decide whether a monitor fits this box at all. The picture is")
w("centred on the plate, so the CASING is not — it shifts toward its thick edge.")
w()
w("| | limit |")
w("|---|---|")
w(f"| thick bezel — the \"chin\", a SIDE edge in portrait | **≤ {(CAV_W - P1.ACT_W)/2:.2f}\"** |")
w(f"| bezel on the long edges — top and bottom in portrait | **≤ {(P1.RAIL_Y - CW/2) - P1.ACT_Y - P1.ACT_H:.2f}\"** |")
w(f"| body thickness at its deepest | **≤ {OA_D - T4 - T - T_ACM - Z_GAP:.2f}\"** |")
w()
w("Plus: matte screen, VESA 100, and it must power itself back up after a mains")
w("cut. Then measure the **lit rectangle** — that is what P1's window is cut from.")
w()
open('SHOPPING.md', 'w').write('\n'.join(L))

print(f"\n  nesting.svg + SHOPPING.md written   (panels ${tot:.2f})")
print("\nALL CHECKS PASS\n" if not fails else f"\n{len(fails)} FAILED: {fails}\n")
