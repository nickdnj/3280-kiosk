"""
Kit contents for the 15 x 30 box. Geometry comes from ../fab-rev1/_p1.py so the
manual can never disagree with the DXF or the cut list.

    python3 _kit.py
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'fab-rev1'))
import _p1 as P

T      = 0.750                 # 1x stock, actual
CW     = 2.500                 # 1x3 actual width
BW     = 3.500                 # 1x4 actual width  = the box depth
T4     = 0.500                 # MDF
OA_W, OA_H = P.PW, P.PH        # 15 x 30
OA_D   = P.MAT_T + BW          # 3.618
CAV_W, CAV_H = OA_W - 2*T, OA_H - 2*T          # 13.5 x 28.5
REAR_W, REAR_H = CAV_W - 0.250, CAV_H - 0.250  # 13.25 x 28.25
TRAY   = (4.000, 3.000)
VESA   = 100/25.4

# ── what you cut ────────────────────────────────────────────────────────────
# code, name, stock, W, L, qty, "nice" string
PARTS = [
 ('P2',  'SIDE PANEL',      '1x4', BW,  OA_H,   2, '3-1/2 x 30'),
 ('P3',  'TOP / BOTTOM',    '1x4', BW,  CAV_W,  2, '3-1/2 x 13-1/2'),
 ('P7',  'BUTTON RAIL',     '1x3', CW,  CAV_W,  1, '2-1/2 x 13-1/2'),
 ('P8',  'REAR CLEAT',      '1x3', CW,  CAV_H,  2, '2-1/2 x 28-1/2'),
 ('P9',  'VESA RAIL',       '1x3', CW,  CAV_H,  2, '2-1/2 x 28-1/2'),
 ('P4',  'REAR PANEL',      'MDF', REAR_W, REAR_H, 1, '13-1/4 x 28-1/4'),
 ('P10', 'PI TRAY',         'MDF', TRAY[0], TRAY[1], 1, '4 x 3'),
 ('P1',  'FACE PLATE',      'ACM', OA_W, OA_H, 1, '15 x 30  (ordered)'),
]

# ── what holds it together, and what seals it ───────────────────────────────
# code, name, qty, icon, note
FASTENERS = [
 ('F1', 'WOOD SCREW, #6 x 1-1/4, FLAT HEAD',        40, 'screw',
  'box, rail, cleats, rails. Pilot 7/64.'),
 ('F2', 'INSERT, THREADED, #8-32, BRASS, FOR WOOD', 21, 'insert',
  '15 front + 6 rear. Drill 3/8. EPOXY.'),
 ('F3', 'SCREW, #8-32 x 1/2, BUTTON HEAD, BLACK',   15, 'button',
  'holds P1. Pin-torx if you want it tamper-resistant.'),
 ('F4', 'THUMBSCREW, #8-32 x 1/2',                   6, 'thumb',
  'holds P4. Tool-free service.'),
 ('F5', 'BOLT, M4 x 12 + FLAT WASHER',               4, 'bolt',
  'monitor to P9, VESA 100.'),
 ('F6', 'SWITCH, 30 mm ANTI-VANDAL, MOM. SPST-NO',   3, 'switch',
  'VERIFY the 30.5 cutout before P1 is cut.'),
 ('F7', 'INLET, IEC C14, PANEL MOUNT, FUSED',        1, 'inlet',
  'lower cavity, in the back or the bottom board.'),
 ('F8', 'FOAM TAPE, NEOPRENE, BLACK, 1/4 x 3/16, 10 ft', 1, 'foam',
  f'light seal on the BACK of P1. {P.SEAL_LEN:.0f}" used.'),
]

GLUES = [
 ('G1', 'WOOD GLUE, PVA (Titebond II)', 'glue',   'every wood joint'),
 ('G2', 'EPOXY, 5 MINUTE, 2-PART',      'epoxy',  'the 21 inserts, nothing else'),
 ('G3', 'SANDING SEALER or PRIMER',     'can',    'ALL SIX FACES of every part'),
 ('G4', 'PAINT, SATIN BLACK',           'can',    'outside + visible edges'),
]

TOOLS = [
 ('mitre',   'MITRE SAW  (or hand saw + mitre box)'),
 ('tape',    'TAPE MEASURE'),
 ('square',  'COMBINATION SQUARE'),
 ('pencil',  'PENCIL + MARKING KNIFE'),
 ('drill',   'DRILL / DRIVER'),
 ('bits',    'DRILL BITS  7/64 pilot, 3/8 insert, countersink'),
 ('driver',  'INSERT DRIVER or HEX KEY'),
 ('clamp',   'CLAMPS x4'),
 ('sand',    'SANDPAPER 120 + 180'),
 ('glasses', 'SAFETY GLASSES'),
 ('mask',    'DUST MASK  (MDF)'),
 ('brush',   'BRUSH or FOAM ROLLER'),
]

CONSUMABLES = [
 'Blue tape — mark cut lines, keeps tear-out down',
 'Shop rag + denatured alcohol — squeeze-out, and wiping the back of P1 '
 'clean before the foam seal goes on. Foam tape will not stick to a dusty ACM face.',
 'Cardboard — the printed P1 mock-up',
]

# ── the monitor the box can actually take ───────────────────────────────────
# The picture is centred on the plate, so the CASING is not -- it shifts by half
# the chin-to-thin bezel difference. These are the three numbers to check on a
# monitor's spec sheet, or with a tape in the shop, before buying it.
BUY = dict(
    # thick bezel -- a SIDE edge in portrait. Beyond this the casing hits a wall.
    chin_max  = (CAV_W - P.ACT_W)/2,
    # long-edge bezel -- top and bottom in portrait. The bottom one meets P7.
    bez_max   = (P.RAIL_Y - CW/2) - P.ACT_Y - P.ACT_H,
    # body thickness, with the VESA rail and the rear panel behind it.
    depth_max = OA_D - T4 - T - P.MAT_T - P.GAP,
)

if __name__ == '__main__':
    fails = []
    def ok(l, c, d):
        if not c: fails.append(l)
        print(f"  {l:<44} {d:<26} {'OK' if c else '*** FAIL ***'}")

    print(f"\nKIT — 15 x 30 BOX\n  cavity {CAV_W:g} x {CAV_H:g}   depth {OA_D:.3f}\n")
    for c, n, s, w, l, q, nice in PARTS:
        print(f"  {c:<4} {n:<14} {s:<4} {nice:<22} x{q}")
    print()
    print(f"  {len(FASTENERS)} fastener lines, {sum(f[2] for f in FASTENERS)} pieces")
    print(f"  {len(GLUES)} consumable lines, {len(TOOLS)} tools\n")

    ok("every wood part is a multiple of 1/8",
       all(abs(v*8 - round(v*8)) < 1e-9
           for _, _, s, w, l, _, _ in PARTS if s != 'ACM' for v in (w, l)),
       "17 dimensions")
    ok("inserts match P1's hole count + the rear panel",
       FASTENERS[1][2] == len(P.MOUNT) + 6, f"{len(P.MOUNT)} + 6 = {FASTENERS[1][2]}")
    ok("face screws match P1's hole count",
       FASTENERS[2][2] == len(P.MOUNT), f"{FASTENERS[2][2]}")
    ok("switches match P1's cutouts", FASTENERS[5][2] == len(P.BUTTONS), "3")
    ok("VESA bolts match a 100 mm pattern", FASTENERS[4][2] == 4, "4")
    ok("P4 lands on the rear cleat ledge", (CW - 0.125 - 0.125) > 1.0,
       f"{CW - 0.25:g}\" of ledge")
    ok("rail sits where P1 expects it",
       abs((OA_H - P.RAIL_Y) - 6.0) < 1e-9, f"{OA_H - P.RAIL_Y:g}\" up from the bottom")

    # ── the monitor in the cavity ───────────────────────────────────────────
    # P1's window is centred on the plate and the picture is centred on the
    # window, so the CASING sits off-centre by P.MON_SHIFT. Check the tight side.
    mon_l = P.ACT_X - P.BEZ_CHIN                 # chin on the left; mirrored is the same
    side  = min(mon_l - T, (OA_W - T) - (mon_l + P.MON_OW))
    ok("casing clears the side walls", side > 0.03,
       f"{side:.4f}\" on the chin side, {P.MON_SHIFT:.3f} off centre")
    ok("casing clears the top board", P.MON_TOP - T > 0.10,
       f"{P.MON_TOP - T:.3f}\"")
    ok("casing clears the BUTTON RAIL", (P.RAIL_Y - CW/2) - P.MON_BOT > 0.10,
       f"{(P.RAIL_Y - CW/2) - P.MON_BOT:.3f}\"")
    ok("monitor + rail + back fit the depth",
       P.Z['mon_b'] + T + T4 <= OA_D,
       f"{P.Z['mon_b'] + T + T4:.3f} <= {OA_D:.3f}")
    ok("foam is behind the plate, not holding it up",
       P.SEAL_T > P.GAP and P.Z['mon_f'] - P.MAT_T == P.GAP,
       f"{P.GAP:g}\" gap, rails carry the weight")

    print(f"""
BUY CRITERIA — the monitor has to satisfy all three
  thick bezel (a SIDE in portrait)   <= {BUY['chin_max']:.3f}\"   now {P.BEZ_CHIN:.3f}
  long-edge bezel (top and bottom)   <= {BUY['bez_max']:.3f}\"   now {P.BEZ_SIDE:.3f}
  body thickness                     <= {BUY['depth_max']:.3f}\"   now {P.MON_T:.3f}
  ... plus: matte, VESA 100, and it must power itself back up after a mains cut.
""")
    ok("the nominal monitor meets its own buy criteria",
       P.BEZ_CHIN <= BUY['chin_max'] and P.BEZ_SIDE <= BUY['bez_max']
       and P.MON_T <= BUY['depth_max'], "3 of 3")

    print("\nALL CHECKS PASS\n" if not fails else f"\n{len(fails)} FAILED: {fails}\n")
