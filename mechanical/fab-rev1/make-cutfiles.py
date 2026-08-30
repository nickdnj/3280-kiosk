#!/usr/bin/env python3
"""
Rev 2 cut file — P1 face plate, one piece, 15 x 30.

Emits R12 ASCII DXF (LINE / ARC / CIRCLE only — no polylines, no splines, no
text) plus an SVG preview. Written for SendCutSend's ACM service: 3 mm
aluminium composite, matte black both sides, CNC routed.

All geometry comes from _p1.py. Change it there, never here.

    python3 make-cutfiles.py
"""
import _p1 as P

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

def svg(path, shapes, holes, title, notes):
    w, h = P.PW, P.PH
    PAD, S = 1.6, 22
    W, H = (w+2*PAD)*S, (h+2*PAD+1.1)*S
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:.0f}" height="{H:.0f}" '
         f'viewBox="0 0 {w+2*PAD:.3f} {h+2*PAD+1.1:.3f}">',
         '<rect width="100%" height="100%" fill="#F7F8F9"/>',
         f'<g transform="translate({PAD:.3f},{PAD:.3f}) scale(1,-1) translate(0,{-h:.3f})">']
    for (x, y, ww, hh, r) in shapes:
        o.append(f'<rect x="{x:.4f}" y="{y:.4f}" width="{ww:.4f}" height="{hh:.4f}" rx="{r}" '
                 f'fill="none" stroke="#0E5A6B" stroke-width="0.03"/>')
    for (cx, cy, rr) in holes:
        o.append(f'<circle cx="{cx:.4f}" cy="{cy:.4f}" r="{rr:.4f}" '
                 f'fill="none" stroke="#93331F" stroke-width="0.03"/>')
    o.append('</g>')
    o.append(f'<text x="{PAD:.3f}" y="{h+2*PAD+0.35:.3f}" font-family="monospace" '
             f'font-size="0.30" fill="#171A1C">{title}</text>')
    o.append(f'<text x="{PAD:.3f}" y="{h+2*PAD+0.85:.3f}" font-family="monospace" '
             f'font-size="0.22" fill="#697077">{notes}</text>')
    o.append('</svg>')
    open(path, 'w').write('\n'.join(o))

# ── build it. DXF is Y-up from the bottom-left; _p1 measures from the top. ──
d = Dxf()
d.rrect(0, 0, P.PW, P.PH, P.R_OUT)
win_y = P.PH - P.WIN_Y - P.WIN_H
d.rrect(P.WIN_X, win_y, P.WIN_W, P.WIN_H, P.R_IN)
for x, y in P.BUTTONS:
    d.circle(x, P.PH - y, P.BTN_D/2)
for x, y in P.MOUNT:
    d.circle(x, P.PH - y, P.HOLE/2)
n = d.save('P1-face-plate.dxf')

svg('P1-face-plate.svg',
    [(0, 0, P.PW, P.PH, P.R_OUT), (P.WIN_X, win_y, P.WIN_W, P.WIN_H, P.R_IN)],
    [(x, P.PH - y, P.BTN_D/2) for x, y in P.BUTTONS]
    + [(x, P.PH - y, P.HOLE/2) for x, y in P.MOUNT],
    f'P1 FACE PLATE  {P.PW:g}" x {P.PH:g}"  x 3mm ACM  -  ONE PIECE',
    f'window {P.WIN_W:g} x {P.WIN_H:g}  |  3 x {P.BTN_D:.4f} dia at {P.BTN_CC:g}" cc  |  '
    f'{len(P.MOUNT)} x {P.HOLE:g} dia mount  |  '
    + ('lit area MEASURED' if P.ACT_MEASURED else 'NOT FOR RELEASE - LIT AREA NOT MEASURED'))

print(f"P1 face plate   {P.PW:g} x {P.PH:g}      {n} entities")
print(f"   window       {P.WIN_W:g} x {P.WIN_H:g}  at ({P.WIN_X:g}, {win_y:g}) Y-up")
print(f"   buttons      3 x {P.BTN_D:.4f} at y={P.PH - P.BTN_Y:g} Y-up")
print(f"   mount        {len(P.MOUNT)} x {P.HOLE:g}")
print("\nGeometry and checks live in _p1.py — run it to verify.")
if not P.ACT_MEASURED:
    print("""
  ##################################################################
  #  NOT FOR RELEASE.  The window is derived from the monitor's    #
  #  LIT rectangle and that has not been measured yet, so this     #
  #  DXF is a mock-up file only.  Measure, set ACT_MEASURED in     #
  #  _p1.py, re-run, THEN upload.                                  #
  ##################################################################
""")
