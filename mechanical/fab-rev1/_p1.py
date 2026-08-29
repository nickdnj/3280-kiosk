"""
P1 face plate — single source of truth for the cut file, the stencil and the box.

Rev 2 geometry, 2026-08-29: the plate is rounded to a whole 15 x 30 inches and
every feature lands on a number you can find on a tape measure. Nothing here is
decimal for its own sake -- the only irrational number left is the switch
cutout, which is metric and set by the hardware.

    python3 _p1.py      # prints the layout and runs the checks
"""
import math

# ── the plate ───────────────────────────────────────────────────────────────
PW, PH        = 15.000, 30.000     # 15 x 30, whole
R_OUT = R_IN  = 0.250              # 1/4 corner radius, outside and window

# ── the window ──────────────────────────────────────────────────────────────
WIN_W, WIN_H  = 12.250, 21.250     # 12-1/4 x 21-1/4
WIN_X         = (PW - WIN_W) / 2   # 1.375  = 1-3/8
WIN_Y         = 1.500              # 1-1/2 below the top edge

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

# ── placement on the machine ────────────────────────────────────────────────
BTN_AFF       = 38.000             # ADA 308 reach. Fixed.
KIOSK_BOT     = BTN_AFF - (PH - BTN_Y)     # 34.000 AFF, whole
KIOSK_TOP     = KIOSK_BOT + PH             # 64.000
DOOR_TOP      = 71.150
ADA_LO, ADA_HI = 15.0, 48.0

# ── the monitor it has to suit ──────────────────────────────────────────────
MON_OW, MON_OH = 12.870, 21.440    # cased outline, nominal 23.8" panel
ACT_W, ACT_H   = 11.670, 20.740    # active area, same panel
MON_T          = 1.800
MON_TOP        = WIN_Y - (MON_OH - WIN_H)/2        # outline below the plate top

# ── derived hole lists ──────────────────────────────────────────────────────
MOUNT_Y = [EDGE + i*(PH - 2*EDGE)/4 for i in range(5)]     # 0.5 7.75 15 22.25 29.5
MOUNT   = ([(EDGE, y) for y in MOUNT_Y] + [(PW - EDGE, y) for y in MOUNT_Y]
           + [(PW/2, EDGE), (PW/2, PH - EDGE)]
           + [(x, RAIL_Y) for x in RAIL_X])
BUTTONS = [(x, BTN_Y) for x in BTN_X]


def panels(diags=(23.6, 23.8, 24.0)):
    """Active area of any 16:9 panel sold as '24 inch', in portrait."""
    k = math.hypot(16, 9)
    return [(d, d*9/k, d*16/k) for d in diags]


if __name__ == '__main__':
    fails = []
    def ok(label, cond, detail):
        if not cond: fails.append(label)
        print(f"  {label:<46} {detail:<30} {'OK' if cond else '*** FAIL ***'}")

    print(f"""
P1 FACE PLATE   {PW} x {PH}   x {MAT_T} ACM

  window        {WIN_W} x {WIN_H}   at ({WIN_X}, {WIN_Y}) from the top-left
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
                  R=R_OUT, **{f'BTN_X{i}': v for i, v in enumerate(BTN_X)},
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

    worst = panels()
    crop = [p for p in worst if p[1] >= WIN_W or p[2] >= WIN_H]
    ok("window clears every \"24 inch\" panel", not crop,
       f"min margin {min(min((WIN_W-p[1])/2, (WIN_H-p[2])/2) for p in worst):.3f}\"/side")
    ok("margin hides behind the bezel, sides",
       (WIN_W - ACT_W)/2 < (MON_OW - ACT_W)/2,
       f"{(WIN_W-ACT_W)/2:.3f} < {(MON_OW-ACT_W)/2:.3f}")
    ok("margin hides behind the bezel, ends",
       (WIN_H - ACT_H)/2 < (MON_OH - ACT_H)/2,
       f"{(WIN_H-ACT_H)/2:.3f} < {(MON_OH-ACT_H)/2:.3f}")
    ok("part inside SendCutSend 44 x 31", PW <= 31 and PH <= 44, f"{PW:g} x {PH:g}")

    import itertools
    allh = [(x, y, BTN_D/2) for x, y in BUTTONS] + [(x, y, HOLE/2) for x, y in MOUNT]
    gap = min(math.hypot(a[0]-b[0], a[1]-b[1]) - a[2] - b[2]
              for a, b in itertools.combinations(allh, 2))
    ok("closest hole-to-hole gap", gap > MAT_T, f"{gap:.3f}\"")
    wl, wr, wt, wb = WIN_X, WIN_X+WIN_W, WIN_Y, WIN_Y+WIN_H
    clash = [h for h in allh if wl-h[2] < h[0] < wr+h[2] and wt-h[2] < h[1] < wb+h[2]]
    ok("no hole intrudes on the window", not clash, f"{len(clash)} clash")

    print("\nALL CHECKS PASS\n" if not fails else f"\n{len(fails)} FAILED: {fails}\n")
