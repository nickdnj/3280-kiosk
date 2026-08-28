"""
Geometry for the IKEA-sourced box — variant K of the Rev 1 kiosk.

The released envelope does not move.  P1 (the ACM face plate), the ADA
placement maths, sheet 100 and the 0.750" mounting-adapter budget all key off
15.370 x 28.690 x 3.250, so variant K changes only what is INSIDE the box.

What changes: Baltic birch 1/2" becomes IKEA IVAR solid pine 3/4".
Everything below is derived from that one substitution.  Run this file to
check it:  python3 _geom_k.py
"""

# ── the released envelope, unchanged ─────────────────────────────────────────
OA_W, OA_H, OA_D = 15.370, 28.690, 3.250
T_ACM            = 0.118                # P1, 3 mm ACM
TUBE_D           = OA_D - T_ACM         # 3.132

# ── the substitution ─────────────────────────────────────────────────────────
T                = 0.750                # IVAR shelf, solid pine, measured 3/4"
CLEAT            = 0.750                # ripped square from the same stock

# ── the box ──────────────────────────────────────────────────────────────────
CAV_W            = OA_W - 2*T           # 13.870
CAV_H            = OA_H - 2*T           # 27.190

SIDE_D, SIDE_H   = TUBE_D, OA_H         # K2   3.132 x 28.690
TOPB_D, TOPB_L   = TUBE_D, CAV_W        # K3   3.132 x 13.870

# rear panel: cross-grain gets double clearance, pine moves across the grain
REAR_W           = CAV_W - 0.200        # 13.670   (0.100 per side, across grain)
REAR_H           = CAV_H - 0.100        # 27.090   (0.050 per side, along grain)

# ── cleats ───────────────────────────────────────────────────────────────────
# Front cleats glue to the INNER FACE of each panel, flush with the front, so
# the front plane presents a continuous 1.500" landing band: panel edge
# 0.000-0.750, cleat 0.750-1.500.  P1's mount holes sit at 0.625 from the
# outside, inside that band with material all round.
CLV_L            = CAV_H                # K5   27.190  front vertical
CLH_L            = OA_W - 2*(T+CLEAT)   # K6   12.370  front horizontal
RAIL_L           = CLH_L                # K7   12.370  button rail
RCV_L            = CAV_H                # K8   27.190  rear vertical
RCH_L            = CLH_L                # K9   12.370  rear horizontal

TRAY_W, TRAY_D   = 4.000, 2.900         # K10  Pi tray
VESA_HALF        = 100/25.4/2           # 1.969, VESA 100 bolt circle

# ── depth chain, from the front face ─────────────────────────────────────────
# The 1/2" VESA rails of the birch build are gone.  The monitor bolts straight
# through the 3/4" rear panel on 12 mm M4 standoffs, which is both stiffer and
# one part fewer -- and it makes the rear panel a lift-out service module.
STANDOFF         = 12/25.4              # 0.472, nearest stock size to 0.482
Z = dict(face_f=0.000, face_b=T_ACM,
         mon_f=0.218,  mon_b=2.018,
         rear_f=OA_D-T, rear_b=OA_D)    # 2.500 / 3.250
AIR              = Z['rear_f'] - Z['mon_b']    # 0.482 cable gap
SHIM             = AIR - STANDOFF              # 0.010, shim to suit

# ── P1 interface, copied from ../fab-rev1/make-cutfiles.py ───────────────────
EDGE_FACE        = 0.625                # mount hole centres, in from the edge
H_FACE           = 3/16
RAIL_TOP         = 23.715               # button rail centreline below the top
WIN_TOP          = 1.350
MON_TOP, MON_OW, MON_OH, MON_T = 1.250, 12.870, 21.440, 1.800
BTN_TOP, BTN_CC, BTN_DIA = 25.440, 3.500, 30.5/25.4
KIOSK_BOT        = 34.750               # AFF, set by ADA reach -- see sheet 100

# ── IKEA stock ───────────────────────────────────────────────────────────────
# Verified on ikea.com/us 2026-08-28.
SHELF_A = dict(art='IVAR shelf 83x30', sku='303.181.63',
               L=32.625, W=11.75, T=0.750, usd=12.00, qty=2)
SHELF_C = dict(art='IVAR shelf 83x50', sku='803.181.65',
               L=32.625, W=19.625, T=0.750, usd=15.00, qty=1)
KERF    = 0.125                          # a normal 1/8" table-saw blade

PARTS = [
 ('K2','SIDE PANEL',            2, f'{SIDE_D:.3f} x {SIDE_H:.3f} x {T:.3f}', 'A'),
 ('K3','TOP / BOTTOM PANEL',    2, f'{TOPB_D:.3f} x {TOPB_L:.3f} x {T:.3f}', 'A'),
 ('K4','REAR PANEL',            1, f'{REAR_W:.3f} x {REAR_H:.3f} x {T:.3f}', 'C'),
 ('K5','FRONT CLEAT, VERTICAL', 2, f'{CLEAT:.3f} sq x {CLV_L:.3f}',          'B'),
 ('K6','FRONT CLEAT, HORIZ.',   2, f'{CLEAT:.3f} sq x {CLH_L:.3f}',          'B'),
 ('K7','BUTTON RAIL',           1, f'{CLEAT:.3f} sq x {RAIL_L:.3f}',         'B'),
 ('K8','REAR CLEAT, VERTICAL',  2, f'{CLEAT:.3f} sq x {RCV_L:.3f}',          'B'),
 ('K9','REAR CLEAT, HORIZ.',    2, f'{CLEAT:.3f} sq x {RCH_L:.3f}',          'B'),
 ('K10','PI TRAY',              1, f'{TRAY_W:.3f} x {TRAY_D:.3f} x {T:.3f}', 'B'),
]

HARDWARE = [
 ('H1','INSERT, THREADED, #8-32, FOR WOOD',        21,'brass, epoxy into softwood'),
 ('H2','SCREW, #8-32 x 1/2, BUTTON HEAD, BLACK',   15,'holds P1 to the cleats'),
 ('H3','THUMBSCREW / QUARTER-TURN, #8-32',          6,'holds K4, tool-free'),
 ('H4','BOLT, M4 x 12 + WASHER',                    4,'through K4 into the standoff'),
 ('H5','STANDOFF, M4 M-F, 12 mm, NYLON',            4,'sets the 0.482 cable gap'),
 ('H6','SWITCH, 30 mm ANTI-VANDAL, MOM. SPST-NO',   3,'30.5 cutout -- verify first'),
 ('H7','INLET, IEC C14, PANEL MOUNT, FUSED',        1,'in the lower cavity'),
 ('H8','SCREW, WOOD, #6 x 1-1/4',                  40,'box and cleats'),
 ('H9','GLUE, PVA, YELLOW',                         1,'every cleat, every corner'),
]

DENSITY_PINE = 0.0162      # lb/in^3, dry eastern white / scots pine
DENSITY_ACM  = 0.0080      # lb/in^2 of 3 mm sheet


def volume():
    v  = 2 * SIDE_D * SIDE_H * T
    v += 2 * TOPB_D * TOPB_L * T
    v += REAR_W * REAR_H * T
    v += (2*CLV_L + 2*CLH_L + RAIL_L + 2*RCV_L + 2*RCH_L) * CLEAT * CLEAT
    v += TRAY_W * TRAY_D * T
    return v


def weight():
    pine = volume() * DENSITY_PINE
    acm  = OA_W * OA_H * DENSITY_ACM
    return dict(pine=pine, acm=acm, monitor=9.0, electronics=1.0,
                hardware=1.0, total=pine + acm + 11.0)


if __name__ == '__main__':
    fails = []
    def ok(label, cond, detail):
        if not cond: fails.append(label)
        print(f"  {label:<44} {detail:<28} {'OK' if cond else '*** FAIL ***'}")

    print(f"\nVARIANT K -- IKEA IVAR SOLID PINE {T}\"\n")
    print(f"  envelope        {OA_W} x {OA_H} x {OA_D}")
    print(f"  cavity          {CAV_W:.3f} x {CAV_H:.3f}")
    print(f"  depth chain     " + "  ".join(f"{k}={v:.3f}" for k, v in Z.items()))
    print()

    ok("envelope unchanged from the released package",
       (OA_W, OA_H, OA_D) == (15.370, 28.690, 3.250), f"{OA_W} x {OA_H} x {OA_D}")
    ok("P1 mount hole lands in solid material",
       EDGE_FACE + H_FACE/2 < T + CLEAT and EDGE_FACE - H_FACE/2 > 0,
       f"0.625 in a 0-{T+CLEAT:.3f} band")
    ok("monitor fits the cavity, width",
       CAV_W - MON_OW > 0.5, f"{(CAV_W-MON_OW)/2:.3f}\"/side")
    ok("monitor fits the cavity, height",
       CAV_H - MON_OH > 4.0, f"{CAV_H-MON_OH:.3f}\" spare")
    pi_room = CAV_H - (MON_TOP - T) - MON_OH
    ok("clear cavity below the monitor for the Pi",
       pi_room > 4.0, f"{pi_room:.3f}\" tall x {CAV_W:.3f}\"")
    ok("depth chain closes on the envelope",
       abs(Z['rear_b'] - OA_D) < 1e-9, f"{Z['rear_b']:.3f} = {OA_D}")
    ok("cable gap behind the monitor", AIR > 0.4, f"{AIR:.3f}\"")
    ok("standoff is a stock size, shim takes the rest",
       0 <= SHIM < 0.03, f"12 mm + {SHIM:.3f}\" shim")
    ok("button rail clears the monitor",
       (RAIL_TOP - CLEAT/2) - (MON_TOP + MON_OH) > 0.25,
       f"{(RAIL_TOP-CLEAT/2)-(MON_TOP+MON_OH):.3f}\"")
    ok("button rail clears the switch cutouts",
       (BTN_TOP - BTN_DIA/2) - (RAIL_TOP + CLEAT/2) > 0.25,
       f"{(BTN_TOP-BTN_DIA/2)-(RAIL_TOP+CLEAT/2):.3f}\"")
    ok("horizontal cleats span between the verticals",
       abs(CLH_L - (CAV_W - 2*CLEAT)) < 1e-9, f"{CLH_L:.3f}\"")

    # cut plan: does the stock cover it?
    a_rips = int((SHELF_A['W'] + KERF) // (SIDE_D + KERF))
    ok("shelf A yields the four tube pieces",
       a_rips >= 3 and 2*TOPB_L + KERF <= SHELF_A['L'] and SIDE_H <= SHELF_A['L'],
       f"{a_rips} rips x {SHELF_A['L']}\"")
    cleat_need = 2*CLV_L + 2*CLH_L + RAIL_L + 2*RCV_L + 2*RCH_L
    b_len  = SHELF_A['L'] - TRAY_W - KERF
    b_rips = int((SHELF_A['W'] + KERF) // (CLEAT + KERF))
    ok("shelf B yields every cleat",
       b_rips * b_len >= cleat_need and RCV_L <= b_len,
       f"{b_rips} x {b_len:.3f}\" = {b_rips*b_len:.0f}\" vs {cleat_need:.0f}\" needed")
    ok("shelf C yields the rear panel",
       REAR_H <= SHELF_C['L'] and REAR_W <= SHELF_C['W'],
       f"{REAR_W:.3f} x {REAR_H:.3f} from {SHELF_C['W']} x {SHELF_C['L']}")

    w = weight()
    ok("finished weight is a one-person lift off the bench",
       w['total'] < 30, f"{w['total']:.1f} lb")
    cost = SHELF_A['usd']*SHELF_A['qty'] + SHELF_C['usd']*SHELF_C['qty']
    print(f"\n  IKEA material   ${cost:.2f}   "
          f"({SHELF_A['qty']} x {SHELF_A['art']}, {SHELF_C['qty']} x {SHELF_C['art']})")
    print(f"  pine {w['pine']:.1f} lb + ACM {w['acm']:.1f} lb + monitor/electronics 11 lb "
          f"= {w['total']:.1f} lb\n")
    print("ALL CHECKS PASS\n" if not fails else f"{len(fails)} FAILED: {fails}\n")
