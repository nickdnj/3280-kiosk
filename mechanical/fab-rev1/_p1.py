"""
P1 face plate — single source of truth for the cut file, the stencil and the box.

Rev 2 geometry, 2026-08-29: the plate is a whole 15 x 30 inches and every feature
lands on a number you can find on a tape measure.

Rev 2b, 2026-08-30 — THE WINDOW NOW OVERLAPS THE LCD.
Until now the window was cut generous and the surplus fell on the monitor's own
black bezel: black on black, nothing shows. In practice something always shows --
a shadow line, a different sheen, a power LED, a logo. So the rule is inverted.
The window is now cut SMALLER than the lit rectangle, so the ACM masks the last
3/32" of picture on every side and the bezel never appears at all. You see
illuminated LCD through a crisp routed hole and nothing else.

That inversion has a price, and it is the one thing to understand here: the
window is now derived from ACT_W / ACT_H -- the *lit* rectangle of the monitor
you actually buy. P1 can no longer be ordered before the monitor is measured.
Set ACT_MEASURED = True only when the numbers below came off a tape.

    python3 _p1.py      # prints the layout and runs the checks
"""
import math

def _r8(v):  return round(v*8)/8
def _r16(v): return round(v*16)/16

# ── the plate ───────────────────────────────────────────────────────────────
PW, PH        = 15.000, 30.000     # 15 x 30, whole
R_OUT = R_IN  = 0.250              # 1/4 corner radius, outside and window

# ── the monitor it has to suit ──────────────────────────────────────────────
# MEASURE THESE. Power the monitor, fill the screen white, measure the lit
# rectangle with a tape -- not the advertised diagonal, not the outside of the
# casing. Everything below is derived from it. The values here are a generic
# 23.8" 16:9 panel and are NOT a release.
ACT_MEASURED   = False
ACT_W, ACT_H   = 11.667, 20.741    # LIT rectangle, portrait
BEZ_CHIN       = 0.850             # the thick edge. In PORTRAIT this is a SIDE.
BEZ_THIN       = 0.353             # the edge opposite the chin
BEZ_SIDE       = 0.350             # the two long edges -- top and bottom in portrait
MON_T          = 1.800             # thickest point, front glass to rearmost

# ── the window, derived from the lit rectangle ──────────────────────────────
OVERLAP       = 3/32               # ACM masks this much LCD on every side
WIN_W         = _r8 (ACT_W - 2*OVERLAP)    # 1/8 steps: keeps WIN_X on a 1/16 mark
WIN_H         = _r16(ACT_H - 2*OVERLAP)
WIN_X         = (PW - WIN_W) / 2
WIN_Y         = 1.500              # 1-1/2 below the top edge
OV_W          = (ACT_W - WIN_W) / 2        # overlap actually achieved, sides
OV_H          = (ACT_H - WIN_H) / 2        # ... and ends

# where the picture and the casing then land on the plate
ACT_X, ACT_Y  = WIN_X - OV_W, WIN_Y - OV_H
MON_OW        = BEZ_CHIN + ACT_W + BEZ_THIN
MON_OH        = ACT_H + 2*BEZ_SIDE
MON_TOP       = ACT_Y - BEZ_SIDE           # casing top, below the plate top
MON_BOT       = MON_TOP + MON_OH
# The picture is centred on the plate, so the CASING is not: it shifts by half
# the chin-to-thin difference. This is the number that eats the side clearance.
MON_SHIFT     = (BEZ_CHIN - BEZ_THIN) / 2

# ── the light seal ──────────────────────────────────────────────────────────
# Closed-cell black neoprene foam tape on the BACK of the ACM, around the
# window. Its only job is to kill the light leak and the shadow line. It is not
# a gasket and it does not hold anything -- the VESA rails set the monitor's
# position and the foam merely kisses the bezel.
GAP           = 0.125              # ACM back face to bezel face. Set by the rails.
SEAL_T        = 0.1875             # 3/16 uncompressed -> 33% compression at GAP
SEAL_IN       = 0.125              # inner edge, measured out from the window edge
SEAL_W        = 0.250              # 1/4 tape
SEAL_LEN      = 2*(WIN_W + WIN_H) + 4*SEAL_W      # perimeter, corners included
NO_SHROUD     = True               # decided 2026-08-30 -- see the README

# ── the buttons ─────────────────────────────────────────────────────────────
BTN_CC        = 3.500              # 3-1/2 centre to centre
BTN_Y         = 26.000             # whole, below the top edge  <-- the ADA datum
BTN_D         = 30.5 / 25.4        # 30.5 mm, set by the switch. VERIFY.
BTN_X         = [PW/2 - BTN_CC, PW/2, PW/2 + BTN_CC]      # 4.000  7.500  11.000

# ── fixings ─────────────────────────────────────────────────────────────────
EDGE          = 0.500              # 1/2 in from the edge. Was 5/8; see NOTE 1.
HOLE          = 0.1875             # 3/16 clearance for #8
RAIL_Y        = 24.000             # whole, the button rail centreline
RAIL_X        = [3.500, 7.500, 11.500]
MAT_T         = 0.118              # 3 mm ACM

# ── depth chain, from the front face of the ACM ─────────────────────────────
Z = dict(face_f=0.000, face_b=MAT_T, mon_f=MAT_T + GAP, mon_b=MAT_T + GAP + MON_T)

# ── placement on the machine ────────────────────────────────────────────────
BTN_AFF       = 38.000             # ADA 308 reach. Fixed.
KIOSK_BOT     = BTN_AFF - (PH - BTN_Y)     # 34.000 AFF, whole
KIOSK_TOP     = KIOSK_BOT + PH             # 64.000
DOOR_TOP      = 71.150
ADA_LO, ADA_HI = 15.0, 48.0

# ── derived hole lists ──────────────────────────────────────────────────────
MOUNT_Y = [EDGE + i*(PH - 2*EDGE)/4 for i in range(5)]     # 0.5 7.75 15 22.25 29.5
MOUNT   = ([(EDGE, y) for y in MOUNT_Y] + [(PW - EDGE, y) for y in MOUNT_Y]
           + [(PW/2, EDGE), (PW/2, PH - EDGE)]
           + [(x, RAIL_Y) for x in RAIL_X])
BUTTONS = [(x, BTN_Y) for x in BTN_X]


def panels(diags=(23.6, 23.8, 24.0)):
    """Lit area of any 16:9 panel sold as '24 inch', in portrait."""
    k = math.hypot(16, 9)
    return [(d, d*9/k, d*16/k) for d in diags]


if __name__ == '__main__':
    fails = []
    def ok(label, cond, detail):
        if not cond: fails.append(label)
        print(f"  {label:<46} {detail:<30} {'OK' if cond else '*** FAIL ***'}")

    print(f"""
P1 FACE PLATE   {PW} x {PH}   x {MAT_T} ACM

  lit area      {ACT_W} x {ACT_H}      {'MEASURED' if ACT_MEASURED else '*** NOMINAL -- NOT MEASURED ***'}
  window        {WIN_W} x {WIN_H}   at ({WIN_X}, {WIN_Y}) from the top-left
                overlaps the LCD by {OV_W:.4f} sides, {OV_H:.4f} ends
  light seal    {SEAL_W:g} wide x {SEAL_T:g} thick, {SEAL_IN:g} out from the window edge,
                {SEAL_LEN:.1f}" of it, compressed to {GAP:g}
  buttons       3 x {BTN_D:.4f} dia at x = {', '.join(f'{x:g}' for x in BTN_X)},
                y = {BTN_Y} below the top
  mount         {len(MOUNT)} x {HOLE} dia, {EDGE} in from the edge
  rail          y = {RAIL_Y}, x = {', '.join(f'{x:g}' for x in RAIL_X)}

  placement     bottom {KIOSK_BOT} AFF, top {KIOSK_TOP} AFF,
                buttons {BTN_AFF} AFF
""")
    win_bot = WIN_Y + WIN_H
    ok("plate is whole inches", PW == int(PW) and PH == int(PH), f"{PW:g} x {PH:g}")
    ok("button datum is whole", BTN_Y == int(BTN_Y), f"{BTN_Y:g} below the top")
    # Everything a person measures should land on a tape mark. The switch
    # cutout is the one exception -- it is metric and set by the hardware.
    layout = dict(PW=PW, PH=PH, WIN_W=WIN_W, WIN_H=WIN_H, WIN_X=WIN_X, WIN_Y=WIN_Y,
                  BTN_CC=BTN_CC, BTN_Y=BTN_Y, EDGE=EDGE, HOLE=HOLE, RAIL_Y=RAIL_Y,
                  R=R_OUT, SEAL_IN=SEAL_IN, SEAL_W=SEAL_W, SEAL_T=SEAL_T, GAP=GAP,
                  **{f'BTN_X{i}': v for i, v in enumerate(BTN_X)},
                  **{f'RAIL_X{i}': v for i, v in enumerate(RAIL_X)},
                  **{f'MOUNT_Y{i}': v for i, v in enumerate(MOUNT_Y)})
    off = {k: v for k, v in layout.items() if abs(v*16 - round(v*16)) > 1e-9}
    ok("every layout dimension is a multiple of 1/16", not off,
       f"{len(layout)} dimensions" if not off else str(off))
    ok("buttons at the ADA datum", abs(KIOSK_BOT + (PH - BTN_Y) - BTN_AFF) < 1e-9,
       f"{BTN_AFF:g}\" AFF from a {KIOSK_BOT:g}\" bottom")
    ok("within the ADA reach range", ADA_LO <= BTN_AFF <= ADA_HI,
       f"{ADA_LO:g}-{ADA_HI:g}")
    ok("kiosk top clears the door top", KIOSK_TOP <= DOOR_TOP,
       f"{KIOSK_TOP:g} <= {DOOR_TOP}")
    web = (BTN_Y - BTN_D/2) - win_bot
    ok("web between window and buttons", web > 1.0, f"{web:.3f}\"")
    ok("material below the buttons", PH - BTN_Y - BTN_D/2 > 1.0,
       f"{PH - BTN_Y - BTN_D/2:.3f}\"")
    ok("rail clears the window", RAIL_Y - win_bot > 0.5, f"{RAIL_Y - win_bot:.3f}\"")
    ok("rail clears the switch cutouts", (BTN_Y - BTN_D/2) - RAIL_Y > 0.5,
       f"{(BTN_Y - BTN_D/2) - RAIL_Y:.3f}\"")
    ok("outer button to the plate edge", min(BTN_X) - BTN_D/2 > 1.0,
       f"{min(BTN_X) - BTN_D/2:.3f}\"")
    ok("mount hole to the plate edge", EDGE - HOLE/2 > MAT_T,
       f"{EDGE - HOLE/2:.4f}\"")

    # NOTE 1: at EDGE 0.500 a 0.375 brass insert spans 0.3125-0.6875, so it sits
    # entirely inside a 3/4 board's front edge. At the old 0.625 it broke out.
    ok("insert stays inside a 3/4 board edge", EDGE + 0.375/2 <= 0.750,
       f"{EDGE + 0.375/2:.4f}\" <= 0.750")
    ok("insert stays inside a .719 board edge", EDGE + 0.375/2 <= 0.719,
       f"{EDGE + 0.375/2:.4f}\" <= 0.719")

    # ── the window against the picture ──────────────────────────────────────
    # The whole point of Rev 2b: the ACM must land ON the LCD, never on the
    # bezel. Positive overlap on all four sides, and small enough that nobody
    # notices the missing pixels.
    ok("window overlaps the LCD, sides", OV_W > 0, f"{OV_W:.4f}\"/side")
    ok("window overlaps the LCD, ends",  OV_H > 0, f"{OV_H:.4f}\"/end")
    ok("overlap inside the 1/16 - 1/8 band",
       all(0.0625 <= v <= 0.125 for v in (OV_W, OV_H)),
       f"{OV_W:.4f} / {OV_H:.4f}")
    ok("window is centred on the plate", abs(WIN_X*2 + WIN_W - PW) < 1e-9,
       f"{WIN_X:g} each side")
    # 1080 x 1920 across the lit rectangle -- how much picture the mask eats.
    px = 1080/ACT_W
    ok("masked picture under 20 px a side", max(OV_W, OV_H)*px < 20,
       f"{OV_W*px:.0f} px sides, {OV_H*px:.0f} px ends")

    # ── the light seal ──────────────────────────────────────────────────────
    # The foam sits on the back of the ACM. Anything inboard of SEAL_IN is over
    # bare LCD -- foam there presses on the glass. That is the hard rule.
    ok("foam never lands on the LCD", SEAL_IN >= max(OV_W, OV_H),
       f"{SEAL_IN:g} >= {max(OV_W, OV_H):.4f}")
    # Measured out from the window edge: the LCD ends at OV, the bezel runs on
    # to OV + its own width. The foam has to sit wholly between those two.
    bez_out = max(OV_W, OV_H) + min(BEZ_SIDE, BEZ_THIN, BEZ_CHIN)
    ok("foam lands wholly on the narrowest bezel", SEAL_IN + SEAL_W <= bez_out,
       f"foam ends {SEAL_IN + SEAL_W:.4f}, bezel ends {bez_out:.4f}")
    comp = (SEAL_T - GAP) / SEAL_T
    ok("foam compresses 20-50%", 0.20 <= comp <= 0.50, f"{comp*100:.0f}%")
    ok("no shroud", NO_SHROUD, "a seal, not a hood")

    # ── how much a different panel would cost ───────────────────────────────
    spread = [(d, (w - WIN_W)/2, (h - WIN_H)/2) for d, w, h in panels()]
    ok("every \"24 inch\" panel still overlaps",
       all(a > 0 and b > 0 for _, a, b in spread),
       "  ".join(f'{d:g}:{a:+.3f}/{b:+.3f}' for d, a, b in spread))

    ok("part inside SendCutSend 44 x 31", PW <= 31 and PH <= 44, f"{PW:g} x {PH:g}")

    import itertools
    allh = [(x, y, BTN_D/2) for x, y in BUTTONS] + [(x, y, HOLE/2) for x, y in MOUNT]
    gap = min(math.hypot(a[0]-b[0], a[1]-b[1]) - a[2] - b[2]
              for a, b in itertools.combinations(allh, 2))
    ok("closest hole-to-hole gap", gap > MAT_T, f"{gap:.3f}\"")
    wl, wr, wt, wb = WIN_X, WIN_X+WIN_W, WIN_Y, WIN_Y+WIN_H
    clash = [h for h in allh if wl-h[2] < h[0] < wr+h[2] and wt-h[2] < h[1] < wb+h[2]]
    ok("no hole intrudes on the window", not clash, f"{len(clash)} clash")

    print("\nALL CHECKS PASS" if not fails else f"\n{len(fails)} FAILED: {fails}")
    if not ACT_MEASURED:
        print("""
*** GATE — DO NOT ORDER P1 ***
    ACT_W / ACT_H are nominal. Power the monitor, fill the screen white,
    measure the lit rectangle, put it above, set ACT_MEASURED = True, re-run.
""")
    else:
        print()
