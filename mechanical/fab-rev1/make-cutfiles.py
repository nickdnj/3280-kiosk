#!/usr/bin/env python3
"""
Rev 1 cut file — face plate (P1), one piece.

Emits R12 ASCII DXF (LINE / ARC / CIRCLE only — no polylines, no splines, no
text) plus an SVG preview of each part. Written for SendCutSend's ACM service:
3 mm aluminium composite, matte black both sides, CNC routed.

Every dimension traces to the shared geometry block in
../drawings/make-drawings.py and ../rev1-standalone-kiosk.md. Change it there
first, then here.

    python3 make-cutfiles.py
"""
import math, os

# ── geometry, from the Rev 1 design study ────────────────────────────────────
KW, KH        = 15.37, 28.69      # kiosk / face plate outside
SIDE, TOP     = 1.25, 1.25        # face reveal
GAP, BAND, BOT = 0.75, 4.00, 1.25 # below the monitor
MON_W, MON_H  = 12.87, 21.44      # monitor outline, cased, portrait
ACT_W, ACT_H  = 11.67, 20.74      # active area, portrait
WIN_CLR       = 0.25              # window oversize per side. Generous on purpose:
                                  # "24 inch" covers 23.6"-24.0" diagonals, and the
                                  # monitor's own black bezel (0.35" min) fills the
                                  # margin invisibly behind a black face plate.

BTN_CC        = 3.50              # button centre-to-centre
BTN_HOLE      = 30.5 / 25.4       # 30.5 mm cutout for a 30 mm anti-vandal switch

R_OUT         = 0.25              # outside corner radius
R_IN          = 0.25              # inside corner radius (clears any router bit)
H_FACE        = 3/16              # #8 clearance
EDGE_FACE     = 0.625             # hole centres, in from the edge

MAT_T         = 0.118             # 3 mm ACM

# ── derived ──────────────────────────────────────────────────────────────────
WIN_W, WIN_H  = ACT_W + 2*WIN_CLR, ACT_H + 2*WIN_CLR

# distances measured DOWN from the top of the face plate
d_mon_top     = TOP
d_win_top     = d_mon_top + (MON_H - ACT_H)/2 - WIN_CLR
d_band_top    = TOP + MON_H + GAP
d_btn_ctr     = d_band_top + BAND/2                 # the ADA datum, 38" AFF

# DXF works Y-up from the bottom-left of the part
WIN_X, WIN_Y  = (KW - WIN_W)/2, KH - d_win_top - WIN_H
BTN_Y         = KH - d_btn_ctr                      # button centreline, Y-up
RAIL_Y        = (BTN_Y + BTN_HOLE/2 + WIN_Y) / 2    # cleat row between buttons and window

# ── DXF writer ───────────────────────────────────────────────────────────────
def g(code, val):
    return f"{code}\n{val}\n"

class Dxf:
    def __init__(self):
        self.e = []
    def line(self, x1, y1, x2, y2):
        self.e.append(g(0,'LINE')+g(8,'0')+g(10,f"{x1:.5f}")+g(20,f"{y1:.5f}")+g(30,'0.0')
                      +g(11,f"{x2:.5f}")+g(21,f"{y2:.5f}")+g(31,'0.0'))
    def arc(self, cx, cy, r, a0, a1):
        self.e.append(g(0,'ARC')+g(8,'0')+g(10,f"{cx:.5f}")+g(20,f"{cy:.5f}")+g(30,'0.0')
                      +g(40,f"{r:.5f}")+g(50,f"{a0:.5f}")+g(51,f"{a1:.5f}"))
    def circle(self, cx, cy, r):
        self.e.append(g(0,'CIRCLE')+g(8,'0')+g(10,f"{cx:.5f}")+g(20,f"{cy:.5f}")+g(30,'0.0')
                      +g(40,f"{r:.5f}"))
    def rrect(self, x, y, w, h, r):
        """Closed rounded rectangle, counter-clockwise."""
        self.line(x+r,   y,     x+w-r, y)
        self.arc (x+w-r, y+r,   r, 270, 360)
        self.line(x+w,   y+r,   x+w,   y+h-r)
        self.arc (x+w-r, y+h-r, r, 0,   90)
        self.line(x+w-r, y+h,   x+r,   y+h)
        self.arc (x+r,   y+h-r, r, 90,  180)
        self.line(x,     y+h-r, x,     y+r)
        self.arc (x+r,   y+r,   r, 180, 270)
    def save(self, path):
        s  = g(0,'SECTION')+g(2,'HEADER')+g(9,'$INSUNITS')+g(70,'1')+g(0,'ENDSEC')
        s += g(0,'SECTION')+g(2,'ENTITIES')+''.join(self.e)+g(0,'ENDSEC')+g(0,'EOF')
        open(path,'w').write(s)
        return len(self.e)

# ── SVG preview ──────────────────────────────────────────────────────────────
def svg(path, w, h, shapes, holes, title, notes):
    P, S = 1.6, 24                      # padding in inches, px per inch
    W, H = (w+2*P)*S, (h+2*P+1.1)*S
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:.0f}" height="{H:.0f}" '
         f'viewBox="0 0 {w+2*P:.3f} {h+2*P+1.1:.3f}">',
         f'<rect width="100%" height="100%" fill="#F7F8F9"/>',
         f'<g transform="translate({P:.3f},{P:.3f}) scale(1,-1) translate(0,{-h:.3f})">']
    for (x,y,ww,hh,r) in shapes:
        o.append(f'<rect x="{x:.4f}" y="{y:.4f}" width="{ww:.4f}" height="{hh:.4f}" rx="{r}" '
                 f'fill="none" stroke="#0E5A6B" stroke-width="0.03"/>')
    for (cx,cy,rr) in holes:
        o.append(f'<circle cx="{cx:.4f}" cy="{cy:.4f}" r="{rr:.4f}" '
                 f'fill="none" stroke="#93331F" stroke-width="0.03"/>')
    o.append('</g>')
    o.append(f'<text x="{P:.3f}" y="{h+2*P+0.35:.3f}" font-family="monospace" '
             f'font-size="0.30" fill="#171A1C">{title}</text>')
    o.append(f'<text x="{P:.3f}" y="{h+2*P+0.85:.3f}" font-family="monospace" '
             f'font-size="0.22" fill="#697077">{notes}</text>')
    o.append('</svg>')
    open(path,'w').write('\n'.join(o))

# ── P1 · face plate, one piece ───────────────────────────────────────────────
d = Dxf()
d.rrect(0, 0, KW, KH, R_OUT)                    # outside
d.rrect(WIN_X, WIN_Y, WIN_W, WIN_H, R_IN)       # screen window

btn_holes = [(KW/2 + i*BTN_CC, BTN_Y) for i in (-1, 0, 1)]
for (x, y) in btn_holes:
    d.circle(x, y, BTN_HOLE/2)

mount = []
ys = [EDGE_FACE + i*(KH - 2*EDGE_FACE)/4 for i in range(5)]
for y in ys:
    mount += [(EDGE_FACE, y), (KW - EDGE_FACE, y)]          # side rails
mount += [(KW/2, EDGE_FACE), (KW/2, KH - EDGE_FACE)]        # top and bottom centre
mount += [(3.50, RAIL_Y), (KW/2, RAIL_Y), (KW - 3.50, RAIL_Y)]   # cleat above the buttons
for (x, y) in mount:
    d.circle(x, y, H_FACE/2)
n1 = d.save('P1-face-plate.dxf')

svg('P1-face-plate.svg', KW, KH,
    [(0, 0, KW, KH, R_OUT), (WIN_X, WIN_Y, WIN_W, WIN_H, R_IN)],
    [(x, y, BTN_HOLE/2) for x, y in btn_holes] + [(x, y, H_FACE/2) for x, y in mount],
    f'P1 FACE PLATE  {KW}" x {KH}"  x 3mm ACM  -  ONE PIECE',
    f'window {WIN_W:.3f} x {WIN_H:.3f}  |  3 x {BTN_HOLE:.4f} dia (30.5mm) at {BTN_CC}" cc  |  '
    f'{len(mount)} x {H_FACE:.4f} dia mount')

# ── checks ───────────────────────────────────────────────────────────────────
import itertools
print(f"P1 face plate, one piece   {KW} x {KH}      {n1} entities")
print(f"   screen window           {WIN_W:.3f} x {WIN_H:.3f}  at ({WIN_X:.3f}, {WIN_Y:.3f})")
print(f"   button holes            3 x {BTN_HOLE:.4f} at {BTN_CC}\" cc, y={BTN_Y:.3f}")
print(f"   mount holes             {len(mount)} x {H_FACE:.4f}")
print()

def ok(label, cond, detail):
    print(f"check  {label:<40} {detail}  {'OK' if cond else '*** FAIL ***'}")

web = WIN_Y - (BTN_Y + BTN_HOLE/2)
ok("web, window to button holes", web > 1.0, f"{web:.3f}\"")
below = BTN_Y - BTN_HOLE/2
ok("material below the button holes", below > 1.0, f"{below:.3f}\"")
ok("button datum below face plate top", abs(d_btn_ctr - 25.44) < 1e-9,
   f"{d_btn_ctr:.3f}\" (must be 25.440)")
edge = min(x - BTN_HOLE/2 for x, _ in btn_holes)
ok("outer button to plate edge", edge > 1.0, f"{edge:.3f}\"")
ok("min hole dia vs material thickness", min(H_FACE, BTN_HOLE) > MAT_T,
   f"{H_FACE:.4f}\" > {MAT_T:.3f}\"")
ok("mount hole to plate edge", EDGE_FACE - H_FACE/2 > MAT_T, f"{EDGE_FACE - H_FACE/2:.3f}\"")

allh = [(x, y, BTN_HOLE/2) for x, y in btn_holes] + [(x, y, H_FACE/2) for x, y in mount]
gap = min(math.hypot(a[0]-b[0], a[1]-b[1]) - a[2] - b[2] for a, b in itertools.combinations(allh, 2))
ok("closest hole-to-hole gap", gap > MAT_T, f"{gap:.3f}\"")

wl, wr, wb, wt = WIN_X, WIN_X+WIN_W, WIN_Y, WIN_Y+WIN_H
clash = [h for h in allh
         if wl-h[2] < h[0] < wr+h[2] and wb-h[2] < h[1] < wt+h[2]]
ok("no hole intrudes on the window", not clash, f"{len(clash)} clash")
ok("part inside SendCutSend 30 x 44", KW <= 30 and KH <= 44, f"{KW} x {KH}")

K = math.hypot(16, 9)
worst = [(d, d*9/K, d*16/K) for d in (23.6, 23.8, 24.0)]
crop = [w for w in worst if w[1] >= WIN_W or w[2] >= WIN_H]
ok("window clears every \"24 inch\" panel", not crop,
   f"23.6-24.0\" diag, min margin {min(min((WIN_W-w[1])/2, (WIN_H-w[2])/2) for w in worst):.3f}\"/side")
ok("that margin hides behind the monitor bezel", WIN_CLR < 0.35, f"{WIN_CLR:.3f}\" < 0.35\"")
