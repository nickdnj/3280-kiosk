#!/usr/bin/env python3
"""
Rev 1 cut files — face plate (P1) and button plate (P2).

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
APER_W, APER_H = 11.87, 3.00      # button aperture in the FACE plate
LIP           = 0.75              # button plate overlap behind that aperture

R_OUT         = 0.25              # outside corner radius
R_IN          = 0.25              # inside corner radius (clears any router bit)
H_FACE        = 3/16              # #8 clearance, face plate
H_BTN         = 3/16              # #8 clearance, button plate
EDGE_FACE     = 0.625             # hole centres, in from the face plate edge
EDGE_BTN      = 0.375             # hole centres, in from the button plate edge

MAT_T         = 0.118             # 3 mm ACM

# ── derived ──────────────────────────────────────────────────────────────────
WIN_W, WIN_H  = ACT_W + 2*WIN_CLR, ACT_H + 2*WIN_CLR
BP_W, BP_H    = APER_W + 2*LIP, APER_H + 2*LIP     # button plate outside

# distances measured DOWN from the top of the face plate
d_mon_top     = TOP
d_win_top     = d_mon_top + (MON_H - ACT_H)/2 - WIN_CLR
d_band_top    = TOP + MON_H + GAP
d_btn_ctr     = d_band_top + BAND/2                 # the ADA datum, 38" AFF
d_aper_top    = d_btn_ctr - APER_H/2

# DXF works Y-up from the bottom-left of each part
WIN_X, WIN_Y   = (KW - WIN_W)/2,  KH - d_win_top  - WIN_H
APER_X, APER_Y = (KW - APER_W)/2, KH - d_aper_top - APER_H

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

# ── P1 · face plate ──────────────────────────────────────────────────────────
d = Dxf()
d.rrect(0, 0, KW, KH, R_OUT)                 # outside
d.rrect(WIN_X,  WIN_Y,  WIN_W,  WIN_H,  R_IN)   # screen window
d.rrect(APER_X, APER_Y, APER_W, APER_H, R_IN)   # button aperture

face_holes = []
ys = [EDGE_FACE + i*(KH - 2*EDGE_FACE)/4 for i in range(5)]
for y in ys:
    face_holes += [(EDGE_FACE, y), (KW - EDGE_FACE, y)]
face_holes += [(KW/2, EDGE_FACE), (KW/2, KH - EDGE_FACE)]
for (x,y) in face_holes:
    d.circle(x, y, H_FACE/2)
n1 = d.save('P1-face-plate.dxf')

svg('P1-face-plate.svg', KW, KH,
    [(0,0,KW,KH,R_OUT),(WIN_X,WIN_Y,WIN_W,WIN_H,R_IN),(APER_X,APER_Y,APER_W,APER_H,R_IN)],
    [(x,y,H_FACE/2) for x,y in face_holes],
    f'P1 FACE PLATE  {KW}" x {KH}"  x 3mm ACM',
    f'window {WIN_W:.3f} x {WIN_H:.3f}  |  button aperture {APER_W} x {APER_H}  |  '
    f'{len(face_holes)} x {H_FACE:.4f} dia')

# ── P2 · button plate ────────────────────────────────────────────────────────
d = Dxf()
d.rrect(0, 0, BP_W, BP_H, R_OUT)
btn_holes = [(BP_W/2 + i*BTN_CC, BP_H/2) for i in (-1,0,1)]
for (x,y) in btn_holes:
    d.circle(x, y, BTN_HOLE/2)
bp_mount = [(EDGE_BTN, EDGE_BTN), (BP_W/2, EDGE_BTN), (BP_W-EDGE_BTN, EDGE_BTN),
            (EDGE_BTN, BP_H-EDGE_BTN), (BP_W/2, BP_H-EDGE_BTN), (BP_W-EDGE_BTN, BP_H-EDGE_BTN)]
for (x,y) in bp_mount:
    d.circle(x, y, H_BTN/2)
n2 = d.save('P2-button-plate.dxf')

svg('P2-button-plate.svg', BP_W, BP_H, [(0,0,BP_W,BP_H,R_OUT)],
    [(x,y,BTN_HOLE/2) for x,y in btn_holes] + [(x,y,H_BTN/2) for x,y in bp_mount],
    f'P2 BUTTON PLATE  {BP_W}" x {BP_H}"  x 3mm ACM',
    f'3 x {BTN_HOLE:.4f} dia (30.5mm) at {BTN_CC}" cc  |  {len(bp_mount)} x {H_BTN:.4f} dia mount')

# ── checks ───────────────────────────────────────────────────────────────────
print(f"P1 face plate    {KW} x {KH}      {n1:3d} entities")
print(f"   window        {WIN_W:.3f} x {WIN_H:.3f}  at ({WIN_X:.3f}, {WIN_Y:.3f})")
print(f"   btn aperture  {APER_W} x {APER_H}      at ({APER_X:.3f}, {APER_Y:.3f})")
print(f"   mount holes   {len(face_holes)} x {H_FACE:.4f}")
print(f"P2 button plate  {BP_W} x {BP_H}      {n2:3d} entities")
print(f"   button holes  3 x {BTN_HOLE:.4f} at {BTN_CC}\" cc, y={BP_H/2}")
print(f"   mount holes   {len(bp_mount)} x {H_BTN:.4f}")
print()
web = WIN_Y - (APER_Y + APER_H)
print(f"check  web between window and aperture   {web:.3f}\"")
print(f"check  button datum below face plate top {d_btn_ctr:.3f}\"  (must be 25.440)")
print(f"check  min feature spacing vs 3mm ACM    {min(EDGE_BTN-H_BTN/2, EDGE_FACE-H_FACE/2):.3f}\" "
      f"> {MAT_T:.3f}\"  {'OK' if min(EDGE_BTN-H_BTN/2, EDGE_FACE-H_FACE/2) > MAT_T else 'FAIL'}")
print(f"check  min hole dia vs material thickness {min(H_FACE,H_BTN):.4f}\" > {MAT_T:.3f}\"  "
      f"{'OK' if min(H_FACE,H_BTN) > MAT_T else 'FAIL'}")
bx = BP_W/2 + BTN_CC + BTN_HOLE/2
print(f"check  outer button edge inside aperture  {bx-LIP:.3f}\" < {APER_W:.3f}\"  "
      f"{'OK' if bx-LIP < APER_W else 'FAIL'}")
print(f"check  P2 fits enclosure cavity (14.37\")  {BP_W:.3f}\"  "
      f"{'OK' if BP_W < 14.37 else 'FAIL'}")
print(f"check  both parts inside SendCutSend 30x44  "
      f"{'OK' if max(KW,KH,BP_W,BP_H) <= 44 and max(min(KW,KH),min(BP_W,BP_H)) <= 30 else 'FAIL'}")
