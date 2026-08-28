#!/usr/bin/env python3
"""
Rev 1 manufacturing drawing package — 12 sheets, B size (17 x 11), third angle.

    python3 make-package.py

Every dimension comes from _geom.py, which mirrors ../fab-rev1/make-cutfiles.py.
Change geometry there, re-run both.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _sheet import *
import _geom as G

OUT = os.path.dirname(os.path.abspath(__file__))
N = len(G.SHEETS)
def sheet(num, scale, mat, fin):
    i = [k for k, _ in enumerate(G.SHEETS) if G.SHEETS[k][0] == num][0]
    s = Sheet(num, G.SHEETS[i][1], scale, mat, fin, i+1, N)
    s.frame(); s.title_block()
    return s
def done(s, num):
    s.save(os.path.join(OUT, f'{num}.svg'))
    return num

# ═══ 000 · COVER ════════════════════════════════════════════════════════════
s = sheet('000', 'NONE', 'SEE BOM', 'SEE NOTES')
s.text(.7, 1.25, 'CONCURRENT 3280 EXHIBIT KIOSK', T_TITLE*1.5, INK, bold=True, mono=False)
s.text(.7, 1.75, 'REV 1 · STANDALONE ENCLOSURE · MANUFACTURING PACKAGE', T_HEAD, ACC,
       mono=False, bold=True)
s.line(.7, 2.0, 10.2, 2.0, W_VIS, INK)
s.text(.7, 2.35, 'DRAWING INDEX', .115, THIN, bold=True, ls=.02)
for k, (num, _short, title) in enumerate(G.SHEETS):
    y = 2.65 + k*.245
    s.text(.75, y, num, .105, ACC, bold=True)
    s.text(1.35, y, title, .105, INK)
    s.line(.7, y+.075, 6.6, y+.075, W_XTHIN, '#DDDDDD')
s.text(7.1, 2.35, 'GENERAL NOTES', .115, THIN, bold=True, ls=.02)
NOTES = [
 '1.  ALL DIMENSIONS IN INCHES UNLESS NOTED. THIRD ANGLE PROJECTION.',
 '2.  DATUM -A- IS THE FRONT FACE OF P1. DATUM -B- IS THE TOP EDGE OF P1.',
 '3.  CRITICAL: BUTTON CENTRELINE 25.440 BELOW DATUM -B-. WITH THE KIOSK BOTTOM',
 '     AT 34.750 AFF THIS PLACES THE CONTROLS AT 38.000 AFF, INSIDE THE ADA 2010',
 '     §308 REACH RANGE OF 15.000 TO 48.000. DO NOT CHANGE WITHOUT RE-DERIVING.',
 '4.  P1 IS CNC ROUTED FROM 3 mm ACM. IT CANNOT BE BENT, TAPPED, COUNTERSUNK',
 '     OR POWDER COATED. ALL FIXING IS THROUGH CLEARANCE HOLES INTO ITEM 11.',
 '5.  NEVER DRIVE A SCREW INTO A PLYWOOD EDGE. USE ITEM 11 THROUGHOUT.',
 '6.  MONITOR IS ALIGNED TO THE P1 WINDOW, NOT THE REVERSE. THE WINDOW IS 0.250',
 '     OVERSIZE PER SIDE ON THE NOMINAL 23.8" ACTIVE AREA AND CLEARS EVERY PANEL',
 '     SOLD AS "24 INCH" (23.6 TO 24.0 DIAGONAL). SHIM P9 IN DEPTH TO SUIT.',
 '7.  P1 FIXINGS (ITEM 12) ARE VISIBLE ON THE FRONT FACE. BLACK HEAD ON A BLACK',
 '     PANEL, TREATED AS AN INSTRUMENT-PANEL DETAIL. PIN-TORX SPECIFIED SO THEY',
 '     CANNOT BE CASUALLY REMOVED BY THE PUBLIC. ALTERNATE: BOND P1 WITH VHB',
 '     STRUCTURAL TAPE AND OMIT ITEMS 11/12 AT THE PERIMETER — NOT REVERSIBLE.',
 '8.  ⌀1.2008 (30.5 mm) BUTTON CUTOUT IS NOMINAL FOR A 30 mm ANTI-VANDAL SWITCH.',
 '     VERIFY AGAINST THE DATASHEET OF THE SWITCH ACTUALLY PURCHASED BEFORE',
 '     RELEASING SHEET 200. CONFIRM PANEL RANGE INCLUDES 3 mm AND ACTUATION',
 '     FORCE ≤ 5 lbf PER ADA §309.4.',
 '9.  NO TEXT IS CUT INTO P1. BACK / HOME / NEXT LEGENDS ARE APPLIED VINYL,',
 '     APPLIED AFTER ASSEMBLY. SEE SHEET 600.',
 '10. THE KIOSK MOUNTS TO THE CLOSED FACTORY DOOR OF THE CONCURRENT 3280. THE',
 '     MOUNTING ADAPTER IS A SEPARATE SUBSYSTEM, NOT IN THIS PACKAGE. TOTAL',
 '     PROJECTION FROM THE DOOR FACE TO REMAIN ≤ 4.000 PER ADA §307.2, LEAVING',
 '     0.750 FOR THE ADAPTER. NO FASTENER MAY ENTER THE HISTORIC CABINET.',
]
for k, ln in enumerate(NOTES):
    s.text(7.1, 2.65 + k*.185, ln, .092, INK)
s.rect(7.05, 8.05, 9.0, .95, W_VIS, FLAG, '#FFFFFF')
s.text(7.2, 8.35, 'CONCEPT PACKAGE — NOT RELEASED FOR PRODUCTION', .135, FLAG, bold=True)
s.text(7.2, 8.60, 'The Concurrent 3280 is a museum artifact. All mounting must be reversible,', .095, INK)
s.text(7.2, 8.80, 'non-destructive and removable. Nothing in this package fastens to the machine.', .095, INK)
s.default_tol(.7, 9.05)
done(s, '000')

# ═══ 100 · GENERAL ARRANGEMENT ══════════════════════════════════════════════
s = sheet('100', '1:4', 'ASSEMBLY', '—')
K = .25
fv = View(s, 1.35, 8.35, K)                       # front elevation
def outline_front(v, hidden=False):
    s.rect(v.x(0), v.y(G.OA_H), v.d(G.OA_W), v.d(G.OA_H), W_VIS, INK, '#FFFFFF', r=v.d(G.R_OUT))
    s.rect(v.x(G.WIN_X), v.y(G.OA_H-G.WIN_TOP), v.d(G.WIN_W), v.d(G.WIN_H),
           W_VIS, INK, '#F2F4F5', r=v.d(G.R_IN))
    for i in (-1, 0, 1):
        cx, cy = v.x(G.OA_W/2 + i*G.BTN_CC), v.y(G.OA_H - G.BTN_TOP)
        s.circ(cx, cy, v.d(G.BTN_DIA/2), W_VIS, INK, '#FFFFFF')
        s.centre(cx, cy, v.d(G.BTN_DIA/2))
outline_front(fv)
s.text(fv.x(G.OA_W/2), fv.y(-1.0), 'FRONT', T_LBL, INK, 'middle', bold=True)
s.dim_h(fv.y(G.OA_H)-.55, fv.x(0), fv.x(G.OA_W), '15.370', ext_from=fv.y(G.OA_H))
s.dim_v(fv.x(0)-.55, fv.y(0), fv.y(G.OA_H), '28.690', ext_from=fv.x(0))
s.dim_h(fv.y(G.OA_H-G.BTN_TOP)+1.15, fv.x(G.OA_W/2-G.BTN_CC), fv.x(G.OA_W/2), '3.500')
s.dim_v(fv.x(G.OA_W)+.42, fv.y(G.OA_H), fv.y(G.OA_H-G.BTN_TOP), '25.440', left=False,
        ext_from=fv.x(G.OA_W))
s.dim_v(fv.x(G.OA_W)+1.00, fv.y(G.OA_H), fv.y(G.OA_H-G.WIN_TOP), '1.350', left=False)
s.leader(fv.x(G.WIN_X+G.WIN_W), fv.y(G.OA_H-G.WIN_TOP-G.WIN_H/2), fv.x(G.OA_W)+1.60,
         fv.y(G.OA_H-G.WIN_TOP-G.WIN_H/2), 'WINDOW 12.170 x 21.240')

sv = View(s, 6.55, 8.35, K)                       # right side
s.rect(sv.x(0), sv.y(G.OA_H), sv.d(G.OA_D), sv.d(G.OA_H), W_VIS, INK, '#FFFFFF')
s.rect(sv.x(0), sv.y(G.OA_H), sv.d(G.T_ACM), sv.d(G.OA_H), W_VIS, INK, '#DDE3E6')
s.rect(sv.x(G.Z['rear_f']), sv.y(G.OA_H-G.T_PLY), sv.d(G.T_PLY), sv.d(G.OA_H-2*G.T_PLY),
       W_HID, INK, 'none', dash='.06 .04')
s.text(sv.x(G.OA_D/2), sv.y(-1.0), 'RIGHT SIDE', T_LBL, INK, 'middle', bold=True)
s.dim_h(sv.y(G.OA_H)-.55, sv.x(0), sv.x(G.OA_D), '3.250', ext_from=sv.y(G.OA_H))
s.line(sv.x(-.4), sv.y(G.OA_H-G.BTN_TOP), sv.x(G.OA_D+.4), sv.y(G.OA_H-G.BTN_TOP),
       W_CEN, FLAG, dash='.14 .06 .03 .06')
s.text(sv.x(G.OA_D)+.55, sv.y(G.OA_H-G.BTN_TOP), 'BUTTON DATUM', .095, FLAG, mid=True)
s.text(sv.x(G.OA_D)+.55, sv.y(G.OA_H-G.BTN_TOP)+.17, '38.000 AFF INSTALLED', .085, FLAG, mid=True)

tv = View(s, 1.35, 10.05, K)                      # top view
s.rect(tv.x(0), tv.y(G.OA_D), tv.d(G.OA_W), tv.d(G.OA_D), W_VIS, INK, '#FFFFFF')
s.rect(tv.x(0), tv.y(G.OA_D), tv.d(G.OA_W), tv.d(G.T_ACM), W_VIS, INK, '#DDE3E6')
for x in (G.T_PLY, G.OA_W-G.T_PLY):
    s.line(tv.x(x), tv.y(G.OA_D-G.T_ACM), tv.x(x), tv.y(0), W_HID, INK, dash='.06 .04')
s.text(tv.x(G.OA_W/2), tv.y(-.35), 'TOP', T_LBL, INK, 'middle', bold=True)

# installed context
iv = View(s, 12.05, 8.35, .085)
s.rect(iv.x(0), iv.y(71.0), iv.d(24.0), iv.d(71.0-3.125), W_XTHIN, GREY, '#F3F1EC')
s.rect(iv.x(1.2), iv.y(3.125), iv.d(21.6), iv.d(3.125), W_XTHIN, GREY, '#EDEAE3')
kx = iv.x(12.0 - G.OA_W/2)
s.rect(kx, iv.y(G.KIOSK_TOP), iv.d(G.OA_W), iv.d(G.OA_H), W_VIS, INK, '#FFFFFF')
s.rect(iv.x(-3), iv.y(G.ADA_HI), iv.d(30), iv.d(G.ADA_HI-G.ADA_LO), W_XTHIN, ACC, 'none',
       dash='.08 .05')
for a, t in ((G.ADA_HI, 'ADA MAX 48.000'), (G.ADA_LO, 'ADA MIN 15.000')):
    s.text(iv.x(-3), iv.y(a)-.06, t, .085, ACC)
s.line(iv.x(-3), iv.y(G.BTN_AFF), iv.x(27), iv.y(G.BTN_AFF), W_CEN, FLAG, dash='.14 .06 .03 .06')
s.text(iv.x(27)+.06, iv.y(G.BTN_AFF), 'BUTTONS 38.000 AFF', .09, FLAG, mid=True)
s.text(iv.x(12), iv.y(-4.5), 'INSTALLED CONTEXT — REFERENCE ONLY', .095, THIN, 'middle')
s.text(iv.x(12), iv.y(-7.0), 'CONCURRENT 3280, DOOR CLOSED', .085, GREY, 'middle')
s.dim_v(iv.x(-6.2), iv.y(0), iv.y(71.0), '71.000 REF', ext_from=iv.x(0))
s.default_tol(.7, 9.05)
done(s, '100')
print('sheets 000, 100')

# ═══ 101 · EXPLODED + BOM ═══════════════════════════════════════════════════
s = sheet('101', 'NTS', 'ASSEMBLY', '—')
E = View(s, 1.0, 8.15, .215)
stack = [
  (G.T_ACM, 'P1  FACE PLATE',        1, '#DDE3E6', G.OA_H,   0.0),
  (G.CL,    'P5 / P6 / P7  CLEATS',  5, '#EFE7D8', G.CAV_H,  G.T_PLY),
  (G.MON_T, 'E3  MONITOR',          20, '#F2F4F5', G.MON_OH, G.MON_TOP),
  (G.T_PLY, 'P9  VESA RAIL',         9, '#EFE7D8', G.CAV_H,  G.T_PLY),
  (G.RC,    'P8  REAR CLEAT',        8, '#EFE7D8', G.CAV_H,  G.T_PLY),
  (G.T_PLY, 'P4  REAR PANEL',        4, '#EFE7D8', G.REAR_H, G.T_PLY+.05),
]
PITCH = 1.22
for k, (thk, lbl, item, fill, hh, ytop) in enumerate(stack):
    x0 = 1.05 + k*PITCH
    w  = max(.10, E.d(thk*1.8))
    y0 = E.y(G.OA_H - ytop); h = E.d(hh)
    s.rect(x0, y0, w, h, W_VIS, INK, fill)
    ly = E.y(-1.0) - (k % 2)*.24
    s.line(x0 + w/2, E.y(0), x0 + w/2, ly - .10, W_XTHIN, GREY)
    s.text(x0 + w/2, ly, lbl, .082, INK, 'middle')
    s.balloon(x0 + w/2, y0 + h*.28, item, x0 + w/2, E.y(G.OA_H + 1.7))
s.line(.85, E.y(G.OA_H), 1.05 + 5*1.22 + .45, E.y(G.OA_H), W_PHAN, GREY, dash='.16 .05 .04 .05')
s.line(.85, E.y(0), 1.05 + 5*1.22 + .45, E.y(0), W_PHAN, GREY, dash='.16 .05 .04 .05')
s.text(.85, E.y(G.OA_H) - .18, 'P2 / P3  BOX TUBE  —  SECTION ON SHEET 102', .085, GREY)
s.text(.85, E.y(-2.6), 'EXPLODED ALONG THE DEPTH AXIS — VIEWED FROM THE RIGHT', .095, THIN)
s.text(.85, E.y(-3.7), 'SPACING IN Z IS NOT TO SCALE', .085, GREY)

bx, by = 8.55, 1.05
s.text(bx, by - .10, 'BILL OF MATERIALS', .115, THIN, bold=True, ls=.02)
for cx, h in [(0,'ITEM'),(.45,'PART'),(1.20,'DESCRIPTION'),(5.35,'QTY'),(5.85,'MATERIAL'),(7.55,'DWG')]:
    s.text(bx + cx + .06, by + .165, h, .078, THIN, bold=True, ls=.012)
s.rect(bx, by, 7.95, .24, W_HID, INK, 'none')
for k, (n, pn, desc, qty, mat, size, dwg) in enumerate(G.BOM):
    y = by + .24 + k*.205
    if k % 2:
        s.rect(bx, y, 7.95, .205, 0, 'none', '#F5F7F8')
    s.text(bx + .06, y + .145, str(n), .085, INK)
    s.text(bx + .51, y + .145, pn, .085, ACC, bold=True)
    s.text(bx + 1.26, y + .145, desc[:60], .082, INK)
    s.text(bx + 5.41, y + .145, str(qty), .085, INK)
    s.text(bx + 5.91, y + .145, mat[:24], .075, INK)
    s.text(bx + 7.61, y + .145, dwg, .085, ACC)
    s.line(bx, y + .205, bx + 7.95, y + .205, W_XTHIN, '#DDDDDD')
s.rect(bx, by, 7.95, .24 + len(G.BOM)*.205, W_HID, INK)
done(s, '101')

# ═══ 102 · SECTION A-A, ROTATED ════════════════════════════════════════════
# The assembly is 28.690 tall by 3.250 deep. Drawn upright it is a 9:1 sliver
# that cannot be lettered, so the section is rotated 90 deg CW — a standard
# convention — putting height across the sheet and depth up it.
s = sheet('102', '1:2.6  ROTATED 90° CW', 'ASSEMBLY', '—')
KS, OX, OY = .38, 1.05, 3.05
hx = lambda ytop: OX + ytop*KS          # distance below the top of the kiosk
zy = lambda z:    OY + z*KS             # depth behind datum -A-
dd = lambda v:    v*KS
def blk(ytop, h, z0, z1, fill, lw=W_VIS, dash=None):
    s.rect(hx(ytop), zy(z0), dd(h), dd(z1-z0), lw, INK, fill, dash=dash)
s.rect(hx(0), zy(0), dd(G.OA_H), dd(G.OA_D), W_PHAN, GREY, 'none', dash='.16 .05 .04 .05')
blk(0, G.OA_H, 0, G.T_ACM, '#C9D2D6')                                   # P1
s.hatch(hx(0), zy(0), dd(G.OA_H), dd(G.T_ACM), .042, THIN)
blk(0, G.T_PLY, 0, G.OA_D, '#E6DCC6'); blk(G.OA_H-G.T_PLY, G.T_PLY, 0, G.OA_D, '#E6DCC6')
for yy in (0, G.OA_H-G.T_PLY):
    s.hatch(hx(yy), zy(0), dd(G.T_PLY), dd(G.OA_D), .05, THIN)
blk(G.T_PLY, G.CL, G.T_ACM, G.T_ACM+G.CL, '#E6DCC6')                    # P6 top
blk(G.OA_H-G.T_PLY-G.CL, G.CL, G.T_ACM, G.T_ACM+G.CL, '#E6DCC6')        # P6 bottom
blk(G.RAIL_TOP-G.CL/2, G.CL, G.T_ACM, G.T_ACM+G.CL, '#E6DCC6')          # P7
blk(G.MON_TOP, G.MON_OH, G.Z['mon_f'], G.Z['mon_b'], '#F2F4F5')         # E3
blk(G.T_PLY, G.CAV_H, G.Z['vr_f'], G.Z['vr_b'], '#E6DCC6', lw=W_HID, dash='.05 .04')
blk(G.T_PLY+.05, G.REAR_H, G.Z['rear_f'], G.Z['rear_b'], '#E6DCC6')     # P4
s.hatch(hx(G.T_PLY+.05), zy(G.Z['rear_f']), dd(G.REAR_H), dd(G.T_PLY), .05, THIN)
blk(24.6, G.T_PLY, G.T_ACM, G.T_ACM+G.TRAY_D, '#E6DCC6')                # P10
s.text(hx(G.OA_H/2), zy(G.OA_D)+.95, 'SECTION A-A — ROTATED 90° CW', T_LBL, INK, 'middle', bold=True)
s.text(hx(0), zy(0)-.55, 'TOP OF KIOSK  ▸', .09, THIN)
s.text(hx(G.OA_H), zy(0)-.55, '◂  BOTTOM', .09, THIN, 'end')
s.text(hx(-.55), zy(0), 'FRONT', .085, THIN, 'end', mid=True)
s.text(hx(-.55), zy(G.OA_D), 'REAR', .085, THIN, 'end', mid=True)
s.dim_h(zy(0)-.30, hx(0), hx(G.OA_H), '28.690', ext_from=zy(0))
s.dim_v(hx(G.OA_H)+.42, zy(0), zy(G.OA_D), '3.250', left=False, ext_from=hx(G.OA_H))
s.dim_h(zy(G.OA_D)+.42, hx(0), hx(G.BTN_TOP), '25.440  BUTTON DATUM', above=False,
        ext_from=zy(G.OA_D))
s.dim_h(zy(G.OA_D)+.85, hx(0), hx(G.RAIL_TOP), '23.715  P7 CENTRELINE', above=False)
lab = [(1.2, G.T_ACM/2, 'P1  3 mm ACM'),
       (G.T_PLY+G.CL/2, G.T_ACM+G.CL/2, 'P6'),
       (G.RAIL_TOP, G.T_ACM+G.CL/2, 'P7  BUTTON RAIL'),
       (11.9, (G.Z['mon_f']+G.Z['mon_b'])/2, 'E3  MONITOR — 1.800 AT THICKEST'),
       (19.5, (G.Z['vr_f']+G.Z['vr_b'])/2, 'P9  VESA RAIL'),
       (16.0, (G.Z['rear_f']+G.Z['rear_b'])/2, 'P4  REAR PANEL'),
       (24.85, G.T_ACM+G.TRAY_D/2, 'P10  PI TRAY'),
       (G.OA_H-G.T_PLY/2, G.OA_D/2, 'P3')]
for k, (yy, zz, txt_) in enumerate(lab):
    ty = zy(G.OA_D) + 1.55 + (k % 4)*.30
    s.leader(hx(yy), zy(zz), hx(yy), ty, txt_, 'middle' if False else 'start')
# depth chain, drawn vertically at the left
cxx = hx(G.OA_H) + 1.05
chain = [(0,'0.000'),(G.T_ACM,'0.118'),(G.Z['mon_f'],'0.218'),(G.Z['mon_b'],'2.018'),
         (G.Z['rear_f'],'2.750'),(G.Z['rear_b'],'3.250')]
for i2 in range(len(chain)-1):
    s.dim_v(cxx + i2*.34, zy(chain[i2][0]), zy(chain[i2+1][0]), f'{chain[i2+1][0]-chain[i2][0]:.3f}')
s.text(cxx - .15, zy(G.OA_D)+.30, 'DEPTH CHAIN FROM DATUM -A-', .09, ACC, bold=True)
s.rect(1.05, 6.15, 7.3, 1.75, W_HID, FLAG, '#FFFFFF')
s.text(1.17, 6.43, 'SERVICE AIR 0.732', .115, FLAG, bold=True)
for k, ln in enumerate([
  'Between the monitor at its thickest and the rear panel.',
  'Route HDMI and DC downward into the Pi bay using right-angle',
  'plugs. A straight plug needs 1.750 behind the connector and',
  'will not fit. This is what forces the enclosure depth — not the Pi.']):
    s.text(1.17, 6.70+k*.20, ln, .090, INK)
s.rect(8.75, 6.15, 7.7, 1.75, W_HID, ACC, '#FFFFFF')
s.text(8.87, 6.43, 'WHY 3.250 AND NOT MORE', .115, ACC, bold=True)
for k, ln in enumerate([
  'ADA §307.2 caps a projection into a circulation path at 4.000',
  'when its leading edge is above 27.000. The kiosk bottom sits at',
  '34.750 AFF, so the rule applies. Enclosure 3.250 leaves 0.750',
  'for the mounting adapter — see sheet 000 note 10.']):
    s.text(8.87, 6.70+k*.20, ln, .090, INK)
s.default_tol(1.05, 8.20)
done(s, '102')
# ═══ 200 · P1 FACE PLATE ════════════════════════════════════════════════════
s = sheet('200', '1:4', 'ACM 3 mm (0.118)', 'MATTE BLACK, 2 SIDES')
V = View(s, 2.60, 8.55, .25); X, Y, D = V.x, V.y, V.d
yt = lambda top: Y(G.OA_H - top)                      # below datum -B-
s.rect(X(0), Y(G.OA_H), D(G.OA_W), D(G.OA_H), W_VIS, INK, '#FFFFFF', r=D(G.R_OUT))
s.rect(X(G.WIN_X), yt(G.WIN_TOP), D(G.WIN_W), D(G.WIN_H), W_VIS, INK, '#FFFFFF', r=D(G.R_IN))
s.line(X(G.OA_W/2), Y(G.OA_H)-.22, X(G.OA_W/2), Y(0)+.22, W_CEN, GREY, dash='.14 .06 .03 .06')
for cx, ct in [(G.OA_W/2 + i*G.BTN_CC, G.BTN_TOP) for i in (-1, 0, 1)]:
    s.circ(X(cx), yt(ct), D(G.BTN_DIA/2), W_VIS, INK, '#FFFFFF')
    s.centre(X(cx), yt(ct), D(G.BTN_DIA/2))
mount = []
for i in range(5):
    ytop = G.EDGE + i*(G.OA_H - 2*G.EDGE)/4
    mount += [(G.EDGE, ytop), (G.OA_W-G.EDGE, ytop)]
mount += [(G.OA_W/2, G.EDGE), (G.OA_W/2, G.OA_H-G.EDGE),
          (3.500, G.RAIL_TOP), (G.OA_W/2, G.RAIL_TOP), (G.OA_W-3.500, G.RAIL_TOP)]
for cx, ct in mount:
    s.circ(X(cx), yt(ct), D(G.HOLE/2), W_VIS, INK, '#FFFFFF')
    s.centre(X(cx), yt(ct), D(G.HOLE/2))
s.dim_h(Y(G.OA_H)-.40, X(0), X(G.OA_W), '15.370', ext_from=Y(G.OA_H))
s.dim_h(Y(G.OA_H)-.80, X(G.WIN_X), X(G.WIN_X+G.WIN_W), '12.170')
s.dim_v(X(0)-.40, Y(0), Y(G.OA_H), '28.690', ext_from=X(0))
s.dim_v(X(0)-.80, yt(G.WIN_TOP), yt(G.WIN_TOP+G.WIN_H), '21.240')
s.dim_v(X(0)-1.20, Y(G.OA_H), yt(G.WIN_TOP), '1.350')
s.dim_v(X(G.OA_W)+.40, Y(G.OA_H), yt(G.BTN_TOP), '25.440', left=False, ext_from=X(G.OA_W))
s.dim_v(X(G.OA_W)+.85, Y(G.OA_H), yt(G.RAIL_TOP), '23.715', left=False)
s.dim_h(Y(0)+.40, X(G.OA_W/2-G.BTN_CC), X(G.OA_W/2), '3.500', above=False)
s.dim_h(Y(0)+.78, X(0), X(G.EDGE), '0.625', above=False)
s.dim_h(Y(0)+1.16, X(0), X(3.500), '3.500 TO C1', above=False)
s.dim_h(Y(0)+1.54, X(0), X(G.WIN_X), '1.600', above=False)
s.leader(X(G.OA_W/2+G.BTN_CC)+D(G.BTN_DIA/2), yt(G.BTN_TOP), X(G.OA_W)+1.80, yt(G.BTN_TOP),
         '3 x ⌀1.2008 (30.5 mm)   NOTE 8')
s.leader(X(G.OA_W-G.EDGE), yt(G.EDGE+2*(G.OA_H-2*G.EDGE)/4), X(G.OA_W)+1.80,
         yt(G.EDGE+2*(G.OA_H-2*G.EDGE)/4), '15 x ⌀0.1875 THRU')
s.leader(X(G.OA_W)-D(G.R_OUT)*.3, Y(G.OA_H)+D(G.R_OUT)*.3, X(G.OA_W)+1.80, yt(2.2),
         'R0.250 TYP, OUTSIDE PROFILE')
s.leader(X(G.WIN_X+G.WIN_W)-D(G.R_IN)*.3, yt(G.WIN_TOP)+D(G.R_IN)*.3, X(G.OA_W)+1.80, yt(5.2),
         'R0.250 TYP, WINDOW')
s.text(X(G.OA_W/2), Y(0)+1.90, 'P1  FACE PLATE — FRONT', T_LBL, INK, 'middle', bold=True)
s.text(X(G.OA_W/2), Y(0)+2.10, 'ONE PIECE. NO SEPARATE BUTTON PLATE.', .09, THIN, 'middle')
dx, dy = X(G.OA_W)+.14, Y(G.OA_H)
s.rect(dx, dy-.11, .22, .22, W_VIS, INK, '#FFFFFF')
s.text(dx+.11, dy, 'B', .105, INK, 'middle', bold=True, mid=True)
s.rect(X(0)-.36, Y(0)+.02, .22, .22, W_VIS, INK, '#FFFFFF')
s.text(X(0)-.25, Y(0)+.13, 'A', .105, INK, 'middle', bold=True, mid=True)

hx, hy = 10.75, 1.00
s.text(hx, hy-.10, 'FEATURE SCHEDULE', .115, THIN, bold=True, ls=.02)
rows = [('A','⌀1.2008','3','BUTTON, 30 mm ANTI-VANDAL','H5'),
        ('B','⌀0.1875','12','PERIMETER FIXING INTO P5 / P6','H1/H2'),
        ('C','⌀0.1875','3','CLEAT ROW INTO P7 BUTTON RAIL','H1/H2'),
        ('D','12.170 x 21.240','1','SCREEN WINDOW, R0.250','—'),
        ('E','15.370 x 28.690','1','OUTSIDE PROFILE, R0.250','—')]
s.rect(hx, hy, 5.70, .24, W_HID, INK)
for cx, h in [(0,'ID'),(.40,'SIZE'),(2.00,'QTY'),(2.50,'FUNCTION'),(5.05,'ITEM')]:
    s.text(hx+cx+.06, hy+.165, h, .078, THIN, bold=True, ls=.012)
for k, r in enumerate(rows):
    y = hy+.24+k*.24
    if k % 2: s.rect(hx, y, 5.70, .24, 0, 'none', '#F5F7F8')
    for cx, val, col in ((.06, r[0], ACC), (.46, r[1], INK), (2.06, r[2], INK),
                         (2.56, r[3], INK), (5.11, r[4], INK)):
        s.text(hx+cx, y+.165, val, .088, col, bold=(col is ACC))
    s.line(hx, y+.24, hx+5.70, y+.24, W_XTHIN, '#DDDDDD')
s.rect(hx, hy, 5.70, .24+len(rows)*.24, W_HID, INK)
s.rect(hx, 3.05, 5.70, 1.72, W_HID, FLAG, '#FFFFFF')
s.text(hx+.12, 3.33, 'BEFORE RELEASING THIS SHEET', .11, FLAG, bold=True)
for k, ln in enumerate([
  'Verify ⌀1.2008 against the datasheet of the switch actually',
  'purchased. This is a one-piece part — a wrong cutout means',
  'recutting the whole face.',
  'Also confirm: panel range includes 3 mm, and actuation force',
  '≤ 5 lbf per ADA §309.4.']):
    s.text(hx+.12, 3.58+k*.20, ln, .090, INK)
s.rect(hx, 5.05, 5.70, 1.35, W_HID, ACC, '#FFFFFF')
s.text(hx+.12, 5.33, 'SUPPLY', .11, ACC, bold=True)
for k, ln in enumerate([
  'CNC routed. A laser will melt the polyethylene core.',
  'DXF: ../fab-rev1/P1-face-plate.dxf — R12, LINE / ARC / CIRCLE.',
  'Supplier tolerance ±0.005 is acceptable throughout.']):
    s.text(hx+.12, 5.58+k*.20, ln, .090, INK)
s.default_tol(.70, 9.05)
done(s, '200')
print('sheet 200')

# ── helper: simple rectangular part with dims ───────────────────────────────
def part(s, ox, oy, k, w, h, pn, name, mat, dims=True, holes=(), slots=(), note=None):
    V = View(s, ox, oy, k); X, Y, D = V.x, V.y, V.d
    s.rect(X(0), Y(h), D(w), D(h), W_VIS, INK, '#FFFFFF')
    for cx, cy, dia in holes:
        s.circ(X(cx), Y(h-cy), D(dia/2), W_VIS, INK, '#FFFFFF'); s.centre(X(cx), Y(h-cy), D(dia/2))
    for cx, cy, sw, sh in slots:
        s.rect(X(cx-sw/2), Y(h-cy+sh/2), D(sw), D(sh), W_VIS, INK, '#FFFFFF', r=D(sw/2))
        s.centre(X(cx), Y(h-cy), D(sw/2))
    if dims:
        s.dim_h(Y(h)-.34, X(0), X(w), f'{w:.3f}', ext_from=Y(h))
        s.dim_v(X(0)-.34, Y(0), Y(h), f'{h:.3f}', ext_from=X(0))
    s.text(X(w/2), Y(0)+.32, f'{pn}   {name}', .105, INK, 'middle', bold=True)
    s.text(X(w/2), Y(0)+.50, mat, .088, THIN, 'middle')
    if note:
        s.text(X(w/2), Y(0)+.68, note, .085, FLAG, 'middle')
    return V

# ═══ 300 · P2 / P3 BOX PANELS ═══════════════════════════════════════════════
s = sheet('300', '1:4', 'BALTIC BIRCH 1/2 (0.500)', 'SEALED, SATIN BLACK INSIDE')
part(s, 1.30, 8.55, .25, G.SIDE_D, G.SIDE_H, 'P2', 'SIDE PANEL   QTY 2', 'BALTIC BIRCH 1/2"')
part(s, 3.20, 8.55, .25, G.TOPB_D, G.TOPB_L, 'P3', 'TOP / BOTTOM   QTY 2', 'BALTIC BIRCH 1/2"')
s.text(1.35, 1.05, 'BOX ASSEMBLY — PLAN', .115, THIN, bold=True, ls=.02)
PV = View(s, 5.55, 3.35, .36)
s.rect(PV.x(0), PV.y(G.OA_D), PV.d(G.OA_W), PV.d(G.OA_D), W_HID, GREY, 'none', dash='.10 .05')
s.rect(PV.x(0), PV.y(G.OA_D), PV.d(G.T_PLY), PV.d(G.TUBE_D), W_VIS, INK, '#EFE7D8')
s.rect(PV.x(G.OA_W-G.T_PLY), PV.y(G.OA_D), PV.d(G.T_PLY), PV.d(G.TUBE_D), W_VIS, INK, '#EFE7D8')
s.rect(PV.x(G.T_PLY), PV.y(G.OA_D), PV.d(G.CAV_W), PV.d(G.T_ACM), W_VIS, INK, '#C9D2D6')
s.rect(PV.x(G.T_PLY), PV.y(G.OA_D-G.T_ACM), PV.d(G.CL), PV.d(G.CL), W_VIS, INK, '#E6DCC6')
s.rect(PV.x(G.OA_W-G.T_PLY-G.CL), PV.y(G.OA_D-G.T_ACM), PV.d(G.CL), PV.d(G.CL), W_VIS, INK, '#E6DCC6')
s.rect(PV.x(G.T_PLY), PV.y(G.OA_D-G.Z['rear_f']), PV.d(G.RC), PV.d(G.RC), W_VIS, INK, '#E6DCC6')
s.rect(PV.x(G.OA_W-G.T_PLY-G.RC), PV.y(G.OA_D-G.Z['rear_f']), PV.d(G.RC), PV.d(G.RC), W_VIS, INK, '#E6DCC6')
s.rect(PV.x(G.T_PLY+.05), PV.y(G.OA_D-G.Z['rear_f']), PV.d(G.REAR_W), PV.d(G.T_PLY), W_VIS, INK, '#EFE7D8')
for vx in G.VR_X:
    s.rect(PV.x(vx-G.VR_W/2), PV.y(G.OA_D-G.Z['vr_f']), PV.d(G.VR_W), PV.d(G.T_PLY), W_VIS, INK, '#E6DCC6')
s.dim_h(PV.y(G.OA_D)-.34, PV.x(0), PV.x(G.OA_W), '15.370 OVERALL', ext_from=PV.y(G.OA_D))
s.dim_h(PV.y(G.OA_D)-.75, PV.x(G.T_PLY), PV.x(G.OA_W-G.T_PLY), '14.370 CAVITY')
s.dim_v(PV.x(G.OA_W)+.40, PV.y(G.OA_D), PV.y(0), '3.250', left=False, ext_from=PV.x(G.OA_W))
for lab, xx, yy in [('P1', G.OA_W/2, G.OA_D-G.T_ACM/2), ('P2', G.T_PLY/2, G.OA_D/2),
                    ('P5', G.T_PLY+G.CL/2, G.OA_D-G.T_ACM-G.CL/2),
                    ('P8', G.T_PLY+G.RC/2, G.OA_D-G.Z['rear_f']-G.RC/2),
                    ('P9', G.VR_X[0], G.OA_D-G.Z['vr_f']-G.T_PLY/2),
                    ('P4', G.OA_W/2, G.OA_D-G.Z['rear_f']-G.T_PLY/2)]:
    s.text(PV.x(xx), PV.y(yy), lab, .09, ACC, 'middle', bold=True, mid=True)
s.text(PV.x(G.OA_W/2), PV.y(-1.0), 'HORIZONTAL SECTION THROUGH THE MONITOR ZONE — SCALE 1:2.6',
       .095, THIN, 'middle')
s.rect(11.0, 6.10, 5.45, 2.30, W_HID, INK, '#FFFFFF')
s.text(11.12, 6.38, 'BOX CONSTRUCTION', .11, INK, bold=True)
for k, ln in enumerate([
 'P2 SIDES RUN FULL HEIGHT 28.690 AND CAPTURE P3.',
 'P3 TOP AND BOTTOM ARE 14.370 BETWEEN THE SIDES.',
 'GLUE AND SCREW WITH ITEM 17, #6 x 1-1/4, 4 PER JOINT,',
 'PILOT DRILLED. CLAMP SQUARE — DIAGONALS WITHIN 0.06.',
 'CLEATS P5/P6 GLUE FLUSH WITH THE FRONT EDGE.',
 'REAR CLEATS P8 SET BACK 0.750 FROM THE REAR EDGE SO',
 'P4 FINISHES FLUSH.',
 'SEAL AND PAINT ALL INTERNAL SURFACES SATIN BLACK',
 'BEFORE ASSEMBLY — REFLECTIONS SHOW THROUGH THE WINDOW.',
 'GRAIN DIRECTION: LONG AXIS OF EACH PART.']):
    s.text(11.12, 6.62+k*.175, ln, .086, INK)
s.default_tol(.7, 9.05)
done(s, '300')

# ═══ 301 · P4 / P9 / P10 ════════════════════════════════════════════════════
s = sheet('301', '1:4', 'BALTIC BIRCH 1/2 (0.500)', 'SEALED, SATIN BLACK')
rear_holes = [(0.375, 1.0 + i*(G.REAR_H-2.0)/2, 0.190) for i in range(3)] + \
             [(G.REAR_W-0.375, 1.0 + i*(G.REAR_H-2.0)/2, 0.190) for i in range(3)]
part(s, 1.30, 8.55, .25, G.REAR_W, G.REAR_H, 'P4', 'REAR PANEL   QTY 1',
     'BALTIC BIRCH 1/2"', holes=rear_holes, note='6 x ⌀0.190 FOR ITEM 13')
vr_slots = [(G.VR_W/2, 3.0 + i*(G.VESA), 0.190, 0.190+3.0) for i in range(2)]
part(s, 6.30, 8.55, .25, G.VR_W, G.VR_L, 'P9', 'VESA RAIL   QTY 2',
     'BALTIC BIRCH 1/2"', slots=vr_slots, note='SLOTS ⌀0.190 x 3.000 TRAVEL')
part(s, 7.90, 4.35, .50, G.TRAY_W, G.TRAY_D, 'P10', 'PI TRAY   QTY 1', 'BALTIC BIRCH 1/2"')
s.rect(11.0, 1.05, 5.45, 3.05, W_HID, INK, '#FFFFFF')
s.text(11.12, 1.33, 'MONITOR MOUNTING — P9', .11, INK, bold=True)
for k, ln in enumerate([
 'VESA 100 x 100 (3.937 SQUARE). TWO RAILS AT',
 f'X = {G.VR_X[0]:.3f} AND {G.VR_X[1]:.3f} FROM THE LEFT EDGE OF P1.',
 '',
 'THE SLOTS GIVE 3.000 OF VERTICAL TRAVEL. THE MONITOR IS',
 'ALIGNED TO THE P1 WINDOW, NOT TO THE BOX — SET IT BY EYE',
 'THROUGH THE WINDOW WITH THE FACE PLATE TEMPORARILY FITTED,',
 'THEN TIGHTEN ITEM 14.',
 '',
 'DEPTH IS SET BY THE MONITOR, NOT BY THIS DRAWING. THE VESA',
 'BOSS SITS AT A DIFFERENT DEPTH ON EVERY MODEL. SHIM BEHIND',
 'P9 AT ASSEMBLY SO THE PANEL FACE LANDS 0.100 BEHIND P1.',
 '',
 'CHECK BEFORE ORDERING THE MONITOR: MATTE, IPS, VESA 100,',
 'AND IT MUST POWER ITSELF ON AFTER A MAINS CUT.']):
    s.text(11.12, 1.57+k*.185, ln, .086, INK if not ln.startswith('CHECK') else FLAG)
s.rect(11.0, 4.35, 5.45, 1.15, W_HID, INK, '#FFFFFF')
s.text(11.12, 4.63, 'P10  PI TRAY', .11, INK, bold=True)
for k, ln in enumerate([
 'SITS IN THE BAY BELOW THE MONITOR ON TWO 0.500 SQ CLEATS.',
 'SLIDES OUT FORWARD ONCE P4 IS OFF. RASPBERRY PI 4B MOUNTS',
 'ON M2.5 STANDOFFS, 58.0 x 49.0 HOLE PATTERN.']):
    s.text(11.12, 4.87+k*.185, ln, .086, INK)
s.default_tol(.7, 9.05)
done(s, '301')

# ═══ 302 · CLEATS ═══════════════════════════════════════════════════════════
s = sheet('302', '1:4', 'HARDWOOD, CLEAR', 'SEALED, SATIN BLACK')
cl = [('P5','FRONT CLEAT, VERTICAL',2,G.CL,G.CLV_L,'1.00 SQ'),
      ('P6','FRONT CLEAT, HORIZONTAL',2,G.CL,G.CLH_L,'1.00 SQ'),
      ('P7','BUTTON RAIL',1,G.CL,G.RAIL_L,'1.00 SQ'),
      ('P8','REAR CLEAT, VERTICAL',2,G.RC,G.RCV_L,'0.75 SQ')]
for k, (pn, nm, qty, sec, ln_, secs) in enumerate(cl):
    ox = 1.55 + k*2.35
    V = View(s, ox, 8.35, .25)
    s.rect(V.x(0), V.y(ln_), V.d(sec), V.d(ln_), W_VIS, INK, '#EFE7D8')
    s.dim_v(V.x(0)-.34, V.y(0), V.y(ln_), f'{ln_:.3f}', ext_from=V.x(0))
    s.dim_h(V.y(ln_)-.30, V.x(0), V.x(sec), secs)
    s.text(V.x(sec/2), V.y(0)+.30, f'{pn}   QTY {qty}', .105, INK, 'middle', bold=True)
    s.text(V.x(sec/2), V.y(0)+.48, nm, .085, THIN, 'middle')
    if pn in ('P5','P6','P7'):
        n = 5 if pn == 'P5' else 1
        for i in range(n):
            yy = (G.EDGE if pn=='P5' else ln_/2) + (i*(G.OA_H-2*G.EDGE)/4 if pn=='P5' else 0)
            if yy <= ln_:
                s.circ(V.x(sec/2), V.y(ln_-yy), V.d(.10), W_HID, INK, '#FFFFFF', dash='.04 .03')
        s.text(V.x(sec/2), V.y(0)+.66, 'ITEM 11 INSERTS ON P1 HOLE CENTRES', .08, FLAG, 'middle')
s.rect(1.35, 1.05, 7.4, 2.55, W_HID, INK, '#FFFFFF')
s.text(1.47, 1.33, 'CLEAT NOTES', .11, INK, bold=True)
for k, ln in enumerate([
 '1.  P5 AND P6 GLUE INSIDE THE BOX FLUSH WITH THE FRONT EDGE. P5 RUNS THE FULL',
 '     CAVITY HEIGHT; P6 FITS BETWEEN THEM.',
 '2.  P7 IS THE BUTTON RAIL. ITS CENTRELINE SITS 23.715 BELOW THE TOP OF P1, WHICH',
 '     IS 1.725 ABOVE THE BUTTON CENTRELINE — CLEAR OF THE SWITCH BODIES, WHICH',
 '     STAND ABOUT 1.000 PROUD BEHIND THE PLATE.',
 '3.  DRILL ITEM 11 THREADED INSERTS USING P1 AS THE TEMPLATE. CLAMP P1 IN PLACE,',
 '     SPOT THROUGH ALL 15 HOLES, REMOVE, THEN DRILL AND SET THE INSERTS.',
 '4.  NEVER DRIVE A FASTENER INTO A PLYWOOD EDGE. THAT IS WHAT THESE CLEATS ARE FOR.',
 '5.  P8 SETS BACK 0.750 FROM THE REAR EDGE SO P4 FINISHES FLUSH.',
 '6.  HARDWOOD PREFERRED FOR INSERT PULL-OUT STRENGTH. POPLAR OR MAPLE IS FINE.']):
    s.text(1.47, 1.57+k*.19, ln, .086, INK)
s.default_tol(9.1, 9.05)
done(s, '302')
print('sheets 300, 301, 302')

# ═══ 400 · HOLE AND FASTENER SCHEDULE ═══════════════════════════════════════
s = sheet('400', '1:4', '—', '—')
V = View(s, 1.9, 8.75, .25); X, Y, D = V.x, V.y, V.d
yt = lambda top: Y(G.OA_H - top)
s.rect(X(0), Y(G.OA_H), D(G.OA_W), D(G.OA_H), W_HID, GREY, '#FFFFFF', r=D(G.R_OUT))
s.rect(X(G.WIN_X), yt(G.WIN_TOP), D(G.WIN_W), D(G.WIN_H), W_HID, GREY, '#F7F8F9', r=D(G.R_IN))
tbl = []
for i in range(5):
    ytop = G.EDGE + i*(G.OA_H - 2*G.EDGE)/4
    tbl += [(f'B{i*2+1}', G.EDGE, ytop), (f'B{i*2+2}', G.OA_W-G.EDGE, ytop)]
tbl += [('B11', G.OA_W/2, G.EDGE), ('B12', G.OA_W/2, G.OA_H-G.EDGE)]
tbl += [('C1', 3.500, G.RAIL_TOP), ('C2', G.OA_W/2, G.RAIL_TOP), ('C3', G.OA_W-3.500, G.RAIL_TOP)]
for i, (cx, ct) in enumerate([(G.OA_W/2 + j*G.BTN_CC, G.BTN_TOP) for j in (-1,0,1)]):
    s.circ(X(cx), yt(ct), D(G.BTN_DIA/2), W_VIS, INK, '#FFFFFF')
    s.text(X(cx), yt(ct), f'A{i+1}', .10, ACC, 'middle', bold=True, mid=True)
for tag, cx, ct in tbl:
    s.circ(X(cx), yt(ct), D(G.HOLE/2), W_VIS, INK, '#FFFFFF')
    s.text(X(cx)+.17, yt(ct), tag, .085, ACC, mid=True)
s.text(X(G.OA_W/2), Y(0)+.40, 'P1 — HOLE LOCATION MAP', T_LBL, INK, 'middle', bold=True)
s.text(X(G.OA_W/2), Y(0)+.62, 'ALL POSITIONS FROM DATUM -A- (LEFT EDGE) AND -B- (TOP EDGE)',
       .085, THIN, 'middle')
hx, hy = 7.0, 1.05
s.text(hx, hy-.10, 'HOLE SCHEDULE', .115, THIN, bold=True, ls=.02)
cols = [(0,'TAG'),(.55,'X'),(1.45,'Y'),(2.35,'⌀'),(3.20,'DEPTH / THRU'),(4.80,'RECEIVES')]
s.rect(hx, hy, 9.0, .24, W_HID, INK)
for cx, h in cols:
    s.text(hx+cx+.06, hy+.165, h, .078, THIN, bold=True, ls=.012)
rows = [(f'A{i+1}', G.OA_W/2 + j*G.BTN_CC, G.BTN_TOP, '1.2008', 'THRU 0.118',
         'H5 SWITCH, 30 mm ANTI-VANDAL') for i, j in enumerate((-1,0,1))]
rows += [(t, cx, ct, '0.1875', 'THRU 0.118',
          'H2 SCREW INTO H1 INSERT IN ' + ('P7' if t.startswith('C') else 'P5 / P6'))
         for t, cx, ct in tbl]
for k, r in enumerate(rows):
    y = hy+.24+k*.205
    if k % 2: s.rect(hx, y, 9.0, .205, 0, 'none', '#F5F7F8')
    s.text(hx+.06, y+.145, r[0], .085, ACC, bold=True)
    s.text(hx+.61, y+.145, f'{r[1]:.3f}', .085, INK)
    s.text(hx+1.51, y+.145, f'{r[2]:.3f}', .085, INK)
    s.text(hx+2.41, y+.145, r[3], .085, INK)
    s.text(hx+3.26, y+.145, r[4], .085, INK)
    s.text(hx+4.86, y+.145, r[5], .082, INK)
    s.line(hx, y+.205, hx+9.0, y+.205, W_XTHIN, '#DDDDDD')
s.rect(hx, hy, 9.0, .24+len(rows)*.205, W_HID, INK)
fy = hy+.30+len(rows)*.205
s.rect(hx, fy, 9.0, 2.05, W_HID, INK, '#FFFFFF')
s.text(hx+.12, fy+.28, 'FASTENER NOTES', .11, INK, bold=True)
for k, ln in enumerate([
 '1.  DRILL H1 INSERTS USING P1 AS THE TEMPLATE — CLAMP, SPOT THROUGH ALL 15 HOLES, REMOVE, DRILL, SET.',
 '2.  H2 IS PIN-TORX SO THE PUBLIC CANNOT CASUALLY REMOVE THE FACE. HEADS ARE VISIBLE: BLACK ON BLACK,',
 '     TREATED AS AN INSTRUMENT-PANEL DETAIL. SEE SHEET 000 NOTE 7 FOR THE BONDED ALTERNATE.',
 '3.  H3 QUARTER-TURN FASTENERS ON P4 — CAPTIVE, SO NOTHING DROPS INSIDE A MUSEUM ARTIFACT.',
 '4.  TORQUE H2 TO SEAT ONLY. ACM WILL DIMPLE IF OVERTIGHTENED.',
 '5.  NO FASTENER IN THIS PACKAGE ENTERS THE CONCURRENT 3280.']):
    s.text(hx+.12, fy+.52+k*.19, ln, .086, INK if k != 4 else FLAG)
done(s, '400')

# ═══ 500 · ELECTRICAL ═══════════════════════════════════════════════════════
s = sheet('500', 'NTS', '—', '—')
def box(x, y, w, h, lab, sub=None, c=INK):
    s.rect(x, y, w, h, W_VIS, c, '#FFFFFF')
    s.text(x+w/2, y+(h/2 if not sub else h/2-.09), lab, .105, c, 'middle', mid=True, bold=True)
    if sub: s.text(x+w/2, y+h/2+.12, sub, .082, THIN, 'middle', mid=True)
def wire(pts, c=INK, dash=None, w=W_DIM):
    for i in range(len(pts)-1):
        s.line(pts[i][0], pts[i][1], pts[i+1][0], pts[i+1][1], w, c, dash=dash)
s.text(.9, 1.15, 'POWER DISTRIBUTION', .125, THIN, bold=True, ls=.02)
box(.9, 1.45, 1.9, .70, 'H6  IEC C14', 'FUSED INLET')
box(3.5, 1.45, 1.9, .70, 'FUSED SPLIT', '2 WAY, 120 VAC')
box(6.1, 1.05, 2.1, .70, 'E3  MONITOR', '24" IPS, INTERNAL PSU')
box(6.1, 1.90, 2.1, .70, 'E2  PSU', '5 V 3 A USB-C')
box(9.0, 1.90, 1.9, .70, 'E1  PI 4B', '4 GB')
wire([(2.8,1.80),(3.5,1.80)]); wire([(5.4,1.80),(5.75,1.80),(5.75,1.40),(6.1,1.40)])
wire([(5.75,1.80),(5.75,2.25),(6.1,2.25)]); wire([(8.2,2.25),(9.0,2.25)])
wire([(8.2,1.40),(8.6,1.40),(8.6,3.30),(9.95,3.30),(9.95,2.60)], ACC)
s.text(8.65,1.30,'HDMI  E4  RIGHT-ANGLE', .085, ACC)
s.text(.9, 3.25, 'MAINS IS CUT AT CLOSE BY AN AC TIMER. THE MONITOR MUST POWER ITSELF BACK ON.', .09, FLAG, bold=True)
s.text(.9, 3.45, 'TEST BEFORE PURCHASE: SWITCHED STRIP, KILL POWER, RESTORE, CONFIRM IT COMES BACK WITH NO INPUT.', .088, INK)
s.text(.9, 4.35, 'CONTROL WIRING', .125, THIN, bold=True, ls=.02)
gx, gy = 9.0, 4.75
s.rect(gx, gy, 1.9, 2.65, W_VIS, INK, '#FFFFFF')
s.text(gx+.95, gy+.28, 'E1  RASPBERRY PI 4B', .095, INK, 'middle', bold=True)
s.text(gx+.95, gy+.46, '40-PIN HEADER', .082, THIN, 'middle')
pins = [('GPIO5','PIN 29','BACK'),('GPIO6','PIN 31','HOME'),('GPIO13','PIN 33','NEXT'),('GND','PIN 39','COMMON')]
for k,(g,p,fn) in enumerate(pins):
    y = gy+.80+k*.42
    s.text(gx+.12, y, g, .095, INK, mid=True, bold=True)
    s.text(gx+1.78, y, p, .085, THIN, 'end', mid=True)
    s.line(gx, y, gx-.55, y, W_DIM, ACC if fn!='COMMON' else INK)
    if fn != 'COMMON':
        sx = gx-.55
        s.circ(sx-.30, y, .085, W_VIS, INK, '#FFFFFF')
        s.text(sx-.30, y, str(k+1), .075, INK, 'middle', mid=True)
        s.line(sx-.215, y, sx, y, W_DIM, ACC)
        s.line(sx-.385, y, sx-1.05, y, W_DIM, ACC)
        s.text(sx-1.15, y, f'H5-{k+1}  {fn}', .095, INK, 'end', mid=True)
        s.line(sx-1.05, y, sx-1.05, gy+2.42, W_DIM, INK)
s.line(gx-.55, gy+2.42-0*.42+ .0, gx-.55, gy+.80+3*.42, W_DIM, INK)
s.line(6.4, gy+2.42, gx-.55, gy+2.42, W_DIM, INK)
s.text(6.3, gy+2.42, 'COMMON RETURN', .09, INK, 'end', mid=True)
s.rect(.9, 4.75, 5.2, 2.65, W_HID, INK, '#FFFFFF')
s.text(1.02, 5.03, 'BUTTON CIRCUIT', .11, INK, bold=True)
for k, ln in enumerate([
 'THREE SPST-NO MOMENTARY SWITCHES, EACH ONE LEG TO A GPIO',
 'AND ONE LEG TO A COMMON GROUND RETURN. NO EXTERNAL',
 'PULL-UPS — ENABLE THE PI INTERNAL PULL-UPS IN SOFTWARE.',
 '',
 'WIRE 22 AWG STRANDED. LEAVE 6 INCHES OF SLACK AT EACH',
 'SWITCH SO THE PI TRAY CAN SLIDE OUT WITHOUT UNPLUGGING.',
 'STRAIN-RELIEVE THE LOOM TO P7 BUTTON RAIL.',
 '',
 'IF THE SWITCHES ARE ILLUMINATED, THE LED LEG IS SEPARATE —',
 'FEED IT FROM 3V3 THROUGH A RESISTOR, NOT FROM THE GPIO.',
 '',
 'GPIO ASSIGNMENT MUST MATCH src/controller/. CHANGE ONE,',
 'CHANGE BOTH.']):
    s.text(1.02, 5.27+k*.185, ln, .086, FLAG if ln.startswith('GPIO ASSIGN') or ln.startswith('CHANGE BOTH') else INK)
done(s, '500')
print('sheets 400, 500')

# ═══ 600 · ASSEMBLY SEQUENCE ════════════════════════════════════════════════
s = sheet('600', 'NTS', 'ASSEMBLY', '—')
STEPS = [
 ('01','PREPARE THE PANELS', [
   'Cut P2, P3, P4, P9, P10 to size. Sand to 180.',
   'Seal and paint every internal surface satin black before',
   'assembly — bare ply reflects through the window.']),
 ('02','BUILD THE BOX', [
   'Glue and screw P2 sides to P3 top and bottom, item 17,',
   '4 per joint, pilot drilled. Clamp square: measure both',
   'diagonals, within 0.06 of each other.']),
 ('03','FIT THE CLEATS', [
   'Glue P5 vertical cleats flush with the front edge, then P6',
   'between them. Glue P7 button rail with its centreline',
   '23.715 below the top of the box. Glue P8 rear cleats set',
   'back 0.750 from the rear edge.']),
 ('04','SET THE THREADED INSERTS', [
   'Clamp P1 to the front. Spot through all 15 holes. Remove',
   'P1, drill for item 11 and set the inserts. Do not skip the',
   'clamp-and-spot — the holes must match, not merely measure.']),
 ('05','MOUNT THE VESA RAILS', [
   'Fit P9 rails at X = 5.716 and 9.654 from the left edge.',
   'Glue and screw to P3 top and bottom. Leave the monitor',
   'bolts loose for now.']),
 ('06','HANG THE MONITOR', [
   'Bolt the monitor to P9 with item 14, finger tight.',
   'Temporarily fit P1 and sight the active area through the',
   'window. Slide the monitor until the margin is even all',
   'round, then torque item 14. Shim behind P9 if the panel',
   'face is not 0.100 behind P1.']),
 ('07','FIT THE SWITCHES', [
   'Item 15 into the three ⌀1.2008 holes in P1 from the front.',
   'Nut from behind. Do not overtighten — ACM will dimple.']),
 ('08','WIRE', [
   'Per sheet 500. Common return to one GND pin. Leave 6 in of',
   'slack at each switch. Strain-relieve the loom to P7.']),
 ('09','FIT THE PI AND POWER', [
   'P10 tray into the bay on its cleats. Pi on M2.5 standoffs.',
   'H6 inlet in the lower rear. Route HDMI and DC downward with',
   'right-angle plugs — straight plugs will not fit.']),
 ('10','CLOSE UP', [
   'Fit P1 with item 12. Torque to seat only. Fit P4 with item',
   '13. Apply the BACK / HOME / NEXT vinyl legends, centred',
   'under each button.']),
 ('11','BENCH TEST — ONE WEEK', [
   'Run the complete kiosk on a table. Confirm: all three',
   'buttons, boot to the app unattended, and recovery from a',
   'mains cut with no human input. Do not skip the week.']),
 ('12','ONLY THEN — MOUNT', [
   'Design and build the reversible adapter. Total projection',
   'from the door face ≤ 4.000. No fastener enters the 3280.']),
]
for k, (n, title, lines) in enumerate(STEPS):
    col, row = k // 6, k % 6
    x = .9 + col*7.9
    y = 1.15 + row*1.42
    s.circ(x+.20, y+.20, .195, W_VIS, ACC, '#FFFFFF')
    s.text(x+.20, y+.20, n, .105, ACC, 'middle', bold=True, mid=True)
    s.text(x+.55, y+.26, title, .125, INK, bold=True)
    for j, ln in enumerate(lines):
        s.text(x+.55, y+.52+j*.185, ln, .090, INK)
    s.line(x, y+1.28, x+7.2, y+1.28, W_XTHIN, '#DDDDDD')
s.rect(8.8, 9.75, 7.6, .0, 0)
done(s, '600')

# ═══ 700 · INSPECTION ═══════════════════════════════════════════════════════
s = sheet('700', 'NTS', '—', '—')
s.text(.9, 1.15, 'INSPECTION DIMENSIONS', .125, THIN, bold=True, ls=.02)
s.text(.9, 1.42, 'Check these before the kiosk leaves the bench. Anything out of tolerance here shows up on the machine.', .095, INK)
INSP = [
 ('1','P1 OVERALL','15.370 x 28.690','± 0.030','TAPE / CALIPER','SUPPLIER CUT — SPOT CHECK ONLY'),
 ('2','P1 WINDOW','12.170 x 21.240','± 0.030','CALIPER','MUST NOT CROP THE ACTIVE AREA'),
 ('3','BUTTON CENTRELINE BELOW TOP EDGE','25.440','± 0.030','TAPE FROM DATUM -B-','SETS ADA HEIGHT — CRITICAL'),
 ('4','BUTTON PITCH','3.500','± 0.020','CALIPER','—'),
 ('5','BUTTON CUTOUT','⌀1.2008','+0.010 / -0.000','PIN / CALIPER','VERIFY AGAINST SWITCH DATASHEET'),
 ('6','BOX DIAGONALS, FRONT OPENING','EQUAL','WITHIN 0.060','TAPE, CORNER TO CORNER','SQUARENESS'),
 ('7','OVERALL DEPTH, ASSEMBLED','3.250','± 0.040','CALIPER AT 4 CORNERS','FEEDS THE 4.000 §307.2 BUDGET'),
 ('8','P1 FLUSH TO BOX EDGE','0.000','± 0.020','STRAIGHTEDGE','NO PROUD EDGE TO CATCH'),
 ('9','MONITOR MARGIN IN WINDOW','EVEN ALL ROUND','± 0.060','EYE + RULE','ADJUST AT P9 SLOTS'),
 ('10','SERVICE AIR, MONITOR TO P4','0.732 MIN','MIN','DEPTH GAUGE','CABLE BEND CLEARANCE'),
 ('11','ALL 15 FIXINGS ENGAGE','15 OF 15','—','BY HAND','NO STRIPPED INSERT'),
 ('12','P4 REMOVES AND REFITS','—','—','BY HAND','WITHOUT TOOLS OR LOOSE PARTS'),
]
hx, hy = .9, 1.75
cols = [(0,'#'),(.40,'FEATURE'),(5.10,'NOMINAL'),(6.85,'TOLERANCE'),(8.55,'METHOD'),(11.35,'WHY IT MATTERS')]
s.rect(hx, hy, 15.2, .26, W_HID, INK, '#EEF1F2')
for cx, h in cols:
    s.text(hx+cx+.07, hy+.18, h, .080, THIN, bold=True, ls=.012)
for k, r in enumerate(INSP):
    y = hy+.26+k*.255
    if k % 2: s.rect(hx, y, 15.2, .255, 0, 'none', '#F5F7F8')
    crit = 'CRITICAL' in r[5]
    s.text(hx+.07, y+.175, r[0], .09, INK)
    s.text(hx+.47, y+.175, r[1], .092, INK, bold=crit)
    s.text(hx+5.17, y+.175, r[2], .092, INK)
    s.text(hx+6.92, y+.175, r[3], .092, INK)
    s.text(hx+8.62, y+.175, r[4], .088, INK)
    s.text(hx+11.42, y+.175, r[5], .088, FLAG if crit else THIN)
    s.line(hx, y+.255, hx+15.2, y+.255, W_XTHIN, '#DDDDDD')
s.rect(hx, hy, 15.2, .26+len(INSP)*.255, W_HID, INK)
gy = hy+.55+len(INSP)*.255
s.rect(hx, gy, 7.4, 2.10, W_HID, FLAG, '#FFFFFF')
s.text(hx+.12, gy+.30, 'GO / NO-GO ON THE MONITOR', .115, FLAG, bold=True)
for k, ln in enumerate([
 '1.  IT MUST POWER ITSELF BACK ON AFTER A MAINS CUT.',
 '     The exhibit is on an AC timer. Many monitors return to standby',
 '     and need a button press — that is a black screen every morning.',
 '     Test: switched strip, kill power, restore, confirm it comes back',
 '     with no input. This is go / no-go, not a preference.',
 '2.  MATTE ONLY. Overhead lights and daylight; glossy panels mirror them.']):
    s.text(hx+.12, gy+.56+k*.20, ln, .088, INK)
s.rect(hx+7.8, gy, 7.4, 2.10, W_HID, ACC, '#FFFFFF')
s.text(hx+7.92, gy+.30, 'SIGN-OFF', .115, ACC, bold=True)
for k, ln in enumerate(['INSPECTED BY','DATE','BENCH TEST START','BENCH TEST END','RELEASED TO INSTALL']):
    y = gy+.62+k*.29
    s.text(hx+7.92, y, ln, .088, THIN)
    s.line(hx+10.6, y+.03, hx+15.05, y+.03, W_HID, INK)
done(s, '700')
print('sheets 600, 700')
