#!/usr/bin/env python3
"""3280 Kiosk — all cabinet/kiosk drawings from one geometry block.

Emits 01..06. Drawing 07 (monitor fit) has its own script.
Edit GEOMETRY and re-run:   python3 make-drawings.py
"""
import pathlib, math, re

# ============================================================ GEOMETRY
CAB_W, CAB_H, CAB_D = 24.00, 71.00, 34.00     # OEM 50-045R00
BASE      = 3.125                              # derived: 71.00 - 67.875 measured
BOX_H     = CAB_H - BASE                       # 67.875 measured
OPEN_W    = 19.75                              # measured clear opening
FRAME     = (CAB_W - OPEN_W) / 2               # 2.125 uniform, all four sides
APER_W    = OPEN_W
APER_H    = BOX_H - 2*FRAME                    # 63.625
APER_BOT  = BASE + FRAME                       # 5.25 AFF
DOOR_W    = 24.30                              # 3230 fig 3-4
OVER      = (DOOR_W - CAB_W)/2                 # 0.15
DOOR_H    = APER_H + 2*(FRAME + OVER)          # 68.175
DOOR_BOT  = APER_BOT - FRAME - OVER            # 2.975 AFF

PANEL_T   = 0.125                              # carrier panel thickness
MON_D     = 27                                 # chosen diagonal
_K = math.hypot(16,9)
MON_AW, MON_AH = MON_D*9/_K, MON_D*16/_K       # portrait active
BZ_S, BZ_T, BZ_C = 0.35, 0.35, 0.80
MON_OW, MON_OH = MON_AW+2*BZ_S, MON_AH+BZ_T+BZ_C
MON_HUMP  = 1.85                               # depth behind the bezel
MON_BEZ_T = 0.40                               # bezel thickness at the edge

PLATE_W, PLATE_H = MON_OW, 4.00
GAP, BTN_CTR = 1.00, 34.00                     # buttons 34" AFF
BTN_D, BTN_N, BTN_EDGE = 1.125, 5, 0.40
CUT_BOT, CUT_TOP, CUT_W = 8.00, 28.00, 15.00   # viewing cutout
VESA = 100/25.4                                # 100 mm
C1_REQ = MON_HUMP + PANEL_T + 0.5

PLATE_BOT = BTN_CTR - PLATE_H/2
MON_BOT   = PLATE_BOT + PLATE_H + GAP
MON_TOP   = MON_BOT + MON_OH
SCR_CTR   = MON_BOT + MON_OH/2

TAN, TAN2, INK = '#E5DDCB', '#EFE9DC', '#2b2b2b'
DARK, SCREEN, DIMC = '#141414', '#E9E2D0', '#B3401A'
GOOD, WARN, LITE = '#2F5D3A', '#8a5f10', '#8a8a8a'
HERE = pathlib.Path(__file__).parent

# ============================================================ SHEET
_ENT = re.compile(r'&(?!(?:#\d+|#x[0-9A-Fa-f]+|amp|lt|gt|quot|apos);)')
def _esc(t):
    return _ENT.sub('&amp;', str(t)).replace('<', '&lt;')

# ============================================================ SHEET
class Sheet:
    def __init__(self, w, h, title, sub, banner=None, bcol=GOOD, bfill='#E4EFDF'):
        self.w, self.h, self.o = w, h, []
        self.add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
                 f'viewBox="0 0 {w} {h}" font-family="Helvetica,Arial,sans-serif">'
                 f'<rect width="{w}" height="{h}" fill="#ffffff"/>')
        self.txt(40,42,title,21,'#1b1b1b',weight='700')
        self.txt(40,64,sub,12.5,'#555')
        if banner:
            bw = 10.5*len(banner)*0.62+20
            self.add(f'<rect x="40" y="78" width="{bw:.0f}" height="21" fill="{bfill}" stroke="{bcol}"/>')
            self.txt(50,93,banner,11.5,bcol,weight='700')
    def add(self,t): self.o.append(t)
    def txt(self,x,y,s,size=11,fill='#333',anchor='start',weight='400',rot=None):
        s=_esc(s)
        r=f' transform="rotate({rot} {x:.1f} {y:.1f})"' if rot else ''
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" '
                 f'text-anchor="{anchor}" font-weight="{weight}"{r}>{s}</text>')
    def rect(self,x,y,w,h,fill='none',stroke=INK,sw=1.2,dash=None,op=None):
        d=f' stroke-dasharray="{dash}"' if dash else ''
        p=f' opacity="{op}"' if op else ''
        self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
                 f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}{p}/>')
    def line(self,x1,y1,x2,y2,stroke=INK,sw=1.0,dash=None):
        d=f' stroke-dasharray="{dash}"' if dash else ''
        self.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                 f'stroke="{stroke}" stroke-width="{sw}"{d}/>')
    def circ(self,cx,cy,r,fill='none',stroke=INK,sw=1.0):
        self.add(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" '
                 f'stroke="{stroke}" stroke-width="{sw}"/>')
    def hdim(self,x1,x2,y,label,col=DIMC,size=11.5):
        self.line(x1,y,x2,y,col,1); self.line(x1,y-5,x1,y+5,col,1); self.line(x2,y-5,x2,y+5,col,1)
        cx=(x1+x2)/2; wpx=len(label)*size*0.58
        self.add(f'<rect x="{cx-wpx/2:.1f}" y="{y-8:.1f}" width="{wpx:.1f}" height="15" fill="#fff"/>')
        self.txt(cx,y+4,label,size,col,'middle','600')
    def vdim(self,y1,y2,x,label,col=DIMC,size=11.5):
        self.line(x,y1,x,y2,col,1); self.line(x-5,y1,x+5,y1,col,1); self.line(x-5,y2,x+5,y2,col,1)
        cy=(y1+y2)/2
        self.add(f'<rect x="{x-9:.1f}" y="{cy-len(label)*size*0.30:.1f}" width="18" '
                 f'height="{len(label)*size*0.60:.1f}" fill="#fff"/>')
        self.txt(x,cy,label,size,col,'middle','600',rot=-90)
    def save(self,name):
        self.add('</svg>')
        (HERE/name).write_text('\n'.join(self.o))
        print(f'  {name}')

def footer(s, lines):
    y = s.h - 18 - 18*(len(lines)-1)
    for i,(t,c) in enumerate(lines):
        s.txt(40, y+18*i, t, 11.5, c, weight='600')

# ============================================================ shared elevation
def elevation(s, x0, yfloor, S, monitor=True, cutout=True, proud=False, labels=True):
    """Draw the cabinet front at scale S with the carrier panel fitted."""
    def yy(h): return yfloor - S*h
    cx = x0 + CAB_W*S/2
    s.rect(x0, yy(CAB_H), CAB_W*S, BOX_H*S, TAN2, INK, 1.3)
    s.rect(x0+6, yy(BASE), CAB_W*S-12, BASE*S, '#3a3a3a', '#3a3a3a', 1)
    s.rect(cx-APER_W*S/2, yy(APER_BOT+APER_H), APER_W*S, APER_H*S, '#20211f', '#20211f', 1)
    s.rect(cx-DOOR_W*S/2, yy(DOOR_BOT+DOOR_H), DOOR_W*S, DOOR_H*S, TAN, INK, 1.6)
    for hy in (yy(DOOR_BOT+DOOR_H)+0.06*DOOR_H*S, yy(DOOR_BOT)-0.10*DOOR_H*S):
        s.rect(cx-DOOR_W*S/2-0.5*S, hy, 0.5*S, 2.2*S, '#9a9a9a', '#444', 0.7)
    s.rect(cx-DOOR_W*S/2+1.0*S, yy(DOOR_BOT+DOOR_H)+0.9*S, 5.0*S, 1.1*S, '#1b1b1b', '#1b1b1b', 1)
    s.txt(cx-DOOR_W*S/2+3.5*S, yy(DOOR_BOT+DOOR_H)+1.72*S, 'CONCURRENT',
          max(5.5,0.62*S), '#f0ebe0', 'middle')
    if cutout:
        s.rect(cx-CUT_W*S/2, yy(CUT_TOP), CUT_W*S, (CUT_TOP-CUT_BOT)*S,
               '#20211f', DIMC, 1.1, dash='6 4', op=0.32)
    if monitor:
        mw, mh = MON_OW*S, MON_OH*S
        mt = yy(MON_TOP)
        if proud:
            s.rect(cx-mw/2+0.35*S, mt+0.35*S, mw, mh, '#000', '#000', 0, op=0.22)
        s.rect(cx-mw/2, mt, mw, mh, DARK, '#000', 0.9)
        s.rect(cx-MON_AW*S/2, mt+BZ_T*S, MON_AW*S, MON_AH*S, SCREEN, SCREEN, 0)
        py = yy(PLATE_BOT+PLATE_H)
        s.rect(cx-PLATE_W*S/2, py, PLATE_W*S, PLATE_H*S, '#1b1b1b', '#1b1b1b', 1)
        for k in (-1,0,1):
            s.circ(cx+k*PLATE_W*S*0.27, py+PLATE_H*S/2, 0.60*S, '#3d3d3d', '#8d8d8d', 0.7)
    return cx, yy

# ============================================================ 01 ELEVATION
def sheet01():
    S, FL = 11.0, 950.0
    s = Sheet(880, 1090, 'Kiosk Front Elevation — Measured Geometry',
              f'Carrier panel replaces the outer louvered door. Cabinet 24" x 71" on a 3-1/8" base. '
              f'{MON_D}" monitor, portrait. Scale 11 px = 1 in.',
              f'MEASURED + OEM, except the aperture — derived from a uniform {FRAME:.3f}" frame offset')
    x0 = 300
    cx, yy = elevation(s, x0, FL, S)
    s.line(150, FL, 840, FL, '#333', 1.6)
    # ADA band
    s.rect(150, yy(48), 22, (48-15)*S, '#E4EFDF', GOOD, 1)
    s.txt(161, (yy(48)+yy(15))/2, 'ADA REACH 15"-48"', 10, '#33612A', 'middle', rot=-90)
    # dims
    s.hdim(x0, x0+CAB_W*S, yy(CAB_H)-26, '24.0"')
    s.hdim(cx-DOOR_W*S/2, cx+DOOR_W*S/2, yy(CAB_H)-52, f'{DOOR_W:.2f}" door')
    s.vdim(yy(CAB_H), FL, x0-46, '71.0" overall')
    s.vdim(yy(DOOR_BOT+DOOR_H), yy(DOOR_BOT), x0+CAB_W*S+46, f'{DOOR_H:.3f}" door')
    s.vdim(yy(APER_BOT+APER_H), yy(APER_BOT), x0+CAB_W*S+96, f'{APER_H:.3f}" aperture')
    s.vdim(yy(BASE), FL, x0-46+0, '')
    # leaders
    for h,lab,col in ((BTN_CTR,f'buttons {BTN_CTR:g}" AFF',GOOD),
                      (SCR_CTR,f'screen centre {SCR_CTR:.0f}" AFF',GOOD),
                      (APER_BOT,f'aperture bottom {APER_BOT:.2f}" AFF',DIMC),
                      (BASE,f'base {BASE:.3f}"',DIMC)):
        s.line(x0+CAB_W*S, yy(h), 700, yy(h), col, 0.9, '4 3')
        s.txt(706, yy(h)+4, lab, 10.5, col, weight='600')
    s.txt(cx, yy((CUT_TOP+CUT_BOT)/2)-6, 'optional', 10.5, DIMC, 'middle', '700')
    s.txt(cx, yy((CUT_TOP+CUT_BOT)/2)+8, 'viewing cutout', 10.5, DIMC, 'middle', '700')
    s.txt(cx, yy((CUT_TOP+CUT_BOT)/2)+22, f'{CUT_W:g}" x {CUT_TOP-CUT_BOT:g}"', 9.5, DIMC, 'middle')
    footer(s, [(f'The original louvered door is removed and stored; the carrier panel hangs on its hinges. '
                f'Nothing structural is touched — fully reversible.', GOOD),
               (f'Aperture {APER_W:.2f}" x {APER_H:.3f}" derived from the uniform {FRAME:.3f}" offset; '
                f'confirm with one tape reading of the door height.', DIMC)])
    s.save('01-front-elevation.svg')

# ============================================================ 02 CARRIER PANEL
def sheet02():
    S = 11.0
    W,H = 1000, 1010
    s = Sheet(W,H,'Carrier Panel — Dimensioned Layout',
              f'Replacement for the outer louvered door. {MON_D}" monitor recessed. '
              f'Datum X0 Y0 at lower-left. Scale 11 px = 1 in.',
              'GEOMETRY DERIVED — confirm the door height before cutting')
    px0, pby = 300.0, 940.0
    def X(v): return px0 + v*S
    def Y(v): return pby - v*S
    s.rect(X(0), Y(DOOR_H), DOOR_W*S, DOOR_H*S, TAN, INK, 1.8)
    # monitor window (recessed): cut to the bezel outline less a lip
    lip = 0.30
    wW, wH = MON_OW-2*lip, MON_OH-2*lip
    wx, wy = (DOOR_W-wW)/2, MON_BOT-DOOR_BOT+lip
    s.rect(X(wx), Y(wy+wH), wW*S, wH*S, '#20211f', DIMC, 1.4)
    s.txt(X(DOOR_W/2), Y(wy+wH/2)+4, 'MONITOR WINDOW', 10.5, '#cfc6b4', 'middle', '700')
    s.txt(X(DOOR_W/2), Y(wy+wH/2)+18, f'{wW:.2f}" x {wH:.2f}"', 10, '#a89f8e', 'middle')
    # VESA pattern
    vcx, vcy = DOOR_W/2, wy+wH/2
    for dx in (-VESA/2, VESA/2):
        for dy in (-VESA/2, VESA/2):
            s.circ(X(vcx+dx), Y(vcy+dy), 0.16*S, 'none', GOOD, 1.6)
    s.txt(X(vcx), Y(vcy-VESA/2)+22, f'VESA 100 x 100 ({VESA:.2f}")', 9.5, GOOD, 'middle', '600')
    # button plate + holes
    pb = PLATE_BOT-DOOR_BOT
    s.rect(X((DOOR_W-PLATE_W)/2), Y(pb+PLATE_H), PLATE_W*S, PLATE_H*S, '#1b1b1b', '#1b1b1b', 1)
    span = PLATE_W - 2*(BTN_D/2 + BTN_EDGE); pitch = span/(BTN_N-1)
    bx0 = (DOOR_W-PLATE_W)/2 + BTN_D/2 + BTN_EDGE
    for i in range(BTN_N):
        s.circ(X(bx0+i*pitch), Y(pb+PLATE_H/2), BTN_D/2*S,
               '#3d3d3d' if 1<=i<=3 else 'none', '#9a9a9a' if 1<=i<=3 else '#6a6a6a', 1.2)
    # cutout
    s.rect(X((DOOR_W-CUT_W)/2), Y(CUT_TOP-DOOR_BOT), CUT_W*S, (CUT_TOP-CUT_BOT)*S,
           '#20211f', DIMC, 1.3, dash='6 4', op=0.32)
    s.txt(X(DOOR_W/2), Y((CUT_TOP+CUT_BOT)/2-DOOR_BOT)+4, 'VIEWING CUTOUT', 10, DIMC, 'middle', '700')
    # badge
    s.rect(X(1.0), Y(DOOR_H-0.9), 5.0*S, 1.1*S, '#1b1b1b', '#1b1b1b', 1)
    s.txt(X(3.5), Y(DOOR_H-1.72)+0, 'CONCURRENT', 7, '#f0ebe0', 'middle')
    # hinge edge
    s.line(X(0.45), Y(0), X(0.45), Y(DOOR_H), '#9a9a9a', 2.5, '10 5')
    s.txt(X(0.45)-14, Y(DOOR_H/2), 'HINGE EDGE — reuse original points', 9.5, '#555', 'middle', rot=-90)
    # dims
    s.hdim(X(0), X(DOOR_W), Y(DOOR_H)-26, f'{DOOR_W:.2f}"')
    s.vdim(Y(DOOR_H), Y(0), X(DOOR_W)+42, f'{DOOR_H:.3f}"')
    s.hdim(X(bx0), X(bx0+pitch), Y(pb)+30, f'{pitch:.3f}" c-c')
    # schedule
    cxs = 690
    rows=[('PANEL','','',True),
          ('Outline', f'{DOOR_W:.2f}" x {DOOR_H:.3f}"',''),
          ('Thickness', f'{PANEL_T:.3f}"',''),
          ('Overhang on the aperture', f'{FRAME+OVER:.3f}" all round',''),
          ('MONITOR WINDOW','','',True),
          ('Size', f'{wW:.2f}" x {wH:.2f}"',''),
          ('Origin (X,Y)', f'{wx:.2f}, {wy:.2f}',''),
          ('Lip over bezel', f'{lip:.2f}" all round',''),
          ('VESA', f'100 x 100 mm ({VESA:.3f}")',''),
          ('BUTTONS','','',True),
          ('Hole dia', f'{BTN_D:.3f}" (30 mm arcade)',''),
          ('Count / pitch', f'{BTN_N} @ {pitch:.3f}"',''),
          ('Centre height', f'{BTN_CTR:g}" AFF',''),
          ('Plate', f'{PLATE_W:.2f}" x {PLATE_H:.2f}"',''),
          ('VIEWING CUTOUT','','',True),
          ('Size', f'{CUT_W:g}" x {CUT_TOP-CUT_BOT:g}"',''),
          ('Height range', f'{CUT_BOT:g}"-{CUT_TOP:g}" AFF','')]
    yv=140
    for r in rows:
        if len(r)==4:
            yv+=8
            s.txt(cxs, yv, r[0], 11.5, '#1b1b1b', weight='700'); yv+=5
            s.line(cxs, yv, cxs+270, yv, LITE, 0.8); yv+=15
        else:
            s.txt(cxs, yv, r[0], 10, '#888'); s.txt(cxs+270, yv, r[1], 10.5, '#333','end','600'); yv+=17
    footer(s,[('Proud variant: delete the monitor window, keep the VESA holes — the monitor then bolts to the '
               'face and nothing precision needs cutting.', GOOD),
              ('Window is cut 0.30" inside the bezel outline so the monitor\'s own bezel overlaps the cut — '
               'far more forgiving than a bare panel.', DIMC)])
    s.save('02-carrier-panel.svg')

# ============================================================ 03 PLAN SECTION
def sheet03():
    S = 10.0
    W,H = 1140, 930
    s = Sheet(W,H,'Plan Section — Door Swing & Closing Clearance',
              'Looking down. Cabinet front at the bottom. Scale 10 px = 1 in.',
              f'C1 STILL UNMEASURED — need >= {C1_REQ:.2f}" from door plane to the inner perforated panel',
              DIMC, '#FBE7E1')
    fx, fy = 300.0, 520.0                      # front-left corner of the cabinet
    s.rect(fx, fy-CAB_D*S*0.62, CAB_W*S, CAB_D*S*0.62, '#F4F0E7', INK, 1.4)
    s.rect(fx, fy-CAB_D*S*0.62, FRAME*S, CAB_D*S*0.62, TAN, INK, 1)
    s.rect(fx+(CAB_W-FRAME)*S, fy-CAB_D*S*0.62, FRAME*S, CAB_D*S*0.62, TAN, INK, 1)
    s.txt(fx+CAB_W*S/2, fy-CAB_D*S*0.62+18, '(cabinet continues rearward, 34" deep)', 10.5, '#999', 'middle')
    # inner perforated panel + card cage
    ipy = fy - C1_REQ*S
    s.line(fx+FRAME*S, ipy, fx+(CAB_W-FRAME)*S, ipy, '#7a8494', 3.5, '5 3')
    s.txt(fx+CAB_W*S/2, ipy-10, 'inner perforated panel', 10, '#5a6473', 'middle', '600')
    for i in range(16):
        bx = fx+FRAME*S+10+i*((CAB_W-2*FRAME)*S-20)/15
        s.line(bx, ipy-24, bx, fy-CAB_D*S*0.62+34, '#5a6473', 2)
    s.txt(fx+CAB_W*S/2, (ipy+fy-CAB_D*S*0.62)/2+20, 'CARD CAGE', 11, '#3f4a58', 'middle', '700')
    # door closed
    dx0 = fx + (CAB_W-DOOR_W)/2*S
    s.rect(dx0, fy-PANEL_T*S, DOOR_W*S, PANEL_T*S, TAN, INK, 1.5)
    s.rect(fx+CAB_W*S/2-MON_OW*S/2, fy-(PANEL_T+MON_HUMP)*S, MON_OW*S, MON_HUMP*S, DARK, '#000', 1)
    s.txt(fx+CAB_W*S/2, fy-(PANEL_T+MON_HUMP)*S+16, 'monitor body', 9.5, '#cfc6b4', 'middle')
    s.txt(fx+CAB_W*S/2, fy+16, 'CARRIER PANEL (closed)', 10, '#333', 'middle', '600')
    # open ghost
    piv = (dx0, fy)
    s.add(f'<g transform="translate({piv[0]:.1f},{piv[1]:.1f}) rotate(100)" opacity="0.45">'
          f'<rect x="0" y="{-(PANEL_T+MON_HUMP)*S:.1f}" width="{DOOR_W*S:.1f}" '
          f'height="{(PANEL_T+MON_HUMP)*S:.1f}" fill="{TAN}" stroke="{INK}" stroke-width="1.4" '
          f'stroke-dasharray="5 3"/></g>')
    r = DOOR_W*S
    ex, ey = piv[0]+r*math.cos(math.radians(100)), piv[1]+r*math.sin(math.radians(100))
    s.add(f'<path d="M {piv[0]+r:.1f} {piv[1]:.1f} A {r:.1f} {r:.1f} 0 0 1 {ex:.1f} {ey:.1f}" '
          f'fill="none" stroke="{LITE}" stroke-width="1" stroke-dasharray="4 4"/>')
    s.circ(piv[0], piv[1], 6, '#9a9a9a', '#333', 1.5)
    s.txt(piv[0]-26, piv[1]+20, 'HINGE', 10.5, '#333', 'middle')
    s.txt(piv[0]-40, piv[1]+150, 'OPEN ~100&#176;', 11, '#333', 'middle', '700')
    s.txt(piv[0]+250, piv[1]+190, f'swing arc R {DOOR_W:.1f}"', 11, '#666')
    # dims
    s.hdim(fx, fx+CAB_W*S, fy-CAB_D*S*0.62-28, '24.0"')
    s.hdim(fx+FRAME*S, fx+(CAB_W-FRAME)*S, fy-CAB_D*S*0.62-6, f'{APER_W:.2f}" aperture')
    s.line(fx+CAB_W*S+16, fy, fx+CAB_W*S+16, ipy, DIMC, 1)
    s.line(fx+CAB_W*S+11, fy, fx+CAB_W*S+21, fy, DIMC, 1)
    s.line(fx+CAB_W*S+11, ipy, fx+CAB_W*S+21, ipy, DIMC, 1)
    s.txt(fx+CAB_W*S+26, (fy+ipy)/2+4, f'C1 >= {C1_REQ:.2f}" required', 11, DIMC, weight='700')
    # depth budget note
    nx=790
    s.txt(nx,150,'DEPTH BUDGET',12,'#1b1b1b',weight='700')
    s.line(nx,156,nx+300,156,LITE,0.8)
    for i,(a,b) in enumerate([(f'{PANEL_T:.3f}"','carrier panel'),
                              (f'{MON_HUMP:.2f}"','monitor body behind bezel'),
                              ('0.50"','clearance to inner panel'),
                              (f'{C1_REQ:.2f}"','= C1 required')]):
        s.txt(nx, 176+i*19, a, 11, '#1b1b1b' if i==3 else '#333', weight='700' if i==3 else '400')
        s.txt(nx+58, 176+i*19, b, 11, '#555')
    s.txt(nx,272,'IF C1 COMES IN SHORT',12,'#1b1b1b',weight='700')
    s.line(nx,278,nx+300,278,LITE,0.8)
    for i,t in enumerate(['1. Mount the monitor PROUD — nothing',
                          '   intrudes behind the door plane',
                          '2. Thinner monitor (check the hump,',
                          '   not the bezel)',
                          '3. Remove the inner perforated panel',
                          '   if VCF permits, and store it']):
        s.txt(nx, 298+i*17, t, 10.5, '#333')
    footer(s,[('The proud-mount variant needs almost no clearance at all — which is the strongest practical '
               'argument for it if C1 measures tight.', GOOD),
              ('Verify ~26" of clear approach to the hinge side so a fully open door does not foul a '
               'neighbouring exhibit.', DIMC)])
    s.save('03-plan-section.svg')

# ============================================================ 04 MOUNTING
def sheet04():
    S = 6.4
    W,H = 1020, 780
    s = Sheet(W,H,'Mounting — Replace the Outer Door',
              'The cabinet already provides a hinged, removable tan door of the right size. Reuse it.',
              'FULLY REVERSIBLE — no new holes, no adhesive, nothing structural touched')
    for i,(lab,mode) in enumerate([('AS FOUND','orig'),('DOOR REMOVED','none'),('CARRIER FITTED','new')]):
        x0 = 90 + i*310
        FL = 620.0
        def yy(h): return FL - S*h
        cx = x0 + CAB_W*S/2
        s.rect(x0, yy(CAB_H), CAB_W*S, BOX_H*S, TAN2, INK, 1.2)
        s.rect(x0+4, yy(BASE), CAB_W*S-8, BASE*S, '#3a3a3a', '#3a3a3a', 1)
        s.rect(cx-APER_W*S/2, yy(APER_BOT+APER_H), APER_W*S, APER_H*S, '#20211f', '#20211f', 1)
        if mode=='orig':
            s.rect(cx-DOOR_W*S/2, yy(DOOR_BOT+DOOR_H), DOOR_W*S, DOOR_H*S, TAN, INK, 1.5)
            for k in range(int(DOOR_H/2.2)):
                yv = DOOR_BOT+1.2+k*2.2
                if yv < DOOR_BOT+DOOR_H-1:
                    s.line(cx-DOOR_W*S/2+4, yy(yv), cx+DOOR_W*S/2-4, yy(yv), '#cfc6b4', 1.1)
            s.rect(cx+DOOR_W*S/2-4.2*S, yy(DOOR_BOT+DOOR_H-1), 2.0*S, (DOOR_H-2)*S, '#4a4640','#4a4640',1)
        elif mode=='none':
            for i2 in range(12):
                bx = cx-APER_W*S/2+8+i2*(APER_W*S-16)/11
                s.line(bx, yy(APER_BOT+APER_H-6), bx, yy(APER_BOT+8), '#5a6473', 1.8)
            s.txt(cx, yy(APER_BOT+APER_H/2), 'inner', 9.5, '#c9c2b4', 'middle')
            s.txt(cx, yy(APER_BOT+APER_H/2)+12, 'perforated', 9.5, '#c9c2b4', 'middle')
            s.txt(cx, yy(APER_BOT+APER_H/2)+24, 'panel', 9.5, '#c9c2b4', 'middle')
        else:
            elevation(s, x0, FL, S)
        for hy in (yy(DOOR_BOT+DOOR_H)+0.06*DOOR_H*S, yy(DOOR_BOT)-0.10*DOOR_H*S):
            s.rect(cx-DOOR_W*S/2-0.5*S, hy, 0.5*S, 2.2*S, '#9a9a9a', '#444', 0.7)
        s.line(x0-20, FL, x0+CAB_W*S+20, FL, '#333', 1.4)
        s.rect(x0, 648, CAB_W*S, 22, GOOD if mode=='new' else '#5a6473',
               GOOD if mode=='new' else '#5a6473', 1)
        s.txt(cx, 663, lab, 11, '#fff', 'middle', '700')
    nx=90
    s.txt(nx,700,'The original door is bagged, labelled and stored with the machine. Rehanging it returns the cabinet',
          11.5,GOOD,weight='600')
    s.txt(nx,718,'to exactly as-found — a stronger reversibility story than clamping rails or gripping a frame lip, '
                 'because a cover door is built to come off. (MR2)',11.5,GOOD,weight='600')
    s.txt(nx,744,'Confirm on the machine: hinge type and spacing, whether the door lifts off pins or swings, and the '
                 'latch. The 3230 used two spring latches at the top.',11.5,DIMC,weight='600')
    s.save('04-door-replacement.svg')

# ============================================================ 05 ASSEMBLY STACK
def sheet05():
    W,H = 1040, 660
    s = Sheet(W,H,'Assembly Stack — Carrier Panel + Cased Monitor',
              f'Front to back. {MON_D}" commercial monitor kept whole; no de-casing. Option C.',
              'NO DE-CASING, NO PRECISION CUT, DOCENT-REPLACEABLE')
    cols = [80, 320, 560, 800]
    labs = [('CARRIER PANEL', [f'{DOOR_W:.2f}" x {DOOR_H:.3f}"','tan, replaces the outer door',
                               'window + VESA + button holes']),
            ('VESA BRACKET', ['100 x 100 mm','M4 x 4','monitor bolts to the panel']),
            (f'{MON_D}" MONITOR', ['cased, intact, portrait','IPS 2560x1440 matte',
                                   'own housing = MR18 enclosure']),
            ('Pi + CABLING', ['Pi 4 behind the monitor','HDMI + 5 V','one loop over the hinge'])]
    for i,(t,ls) in enumerate(labs):
        x = cols[i]
        if i==0:
            s.rect(x, 150, 150, 300, TAN, INK, 1.5)
            s.rect(x+28, 190, 94, 150, '#20211f', DIMC, 1.2)
            s.rect(x+28, 356, 94, 34, '#1b1b1b', '#1b1b1b', 1)
            for k in (-1,0,1): s.circ(x+75+k*30, 373, 7, '#3d3d3d', '#8d8d8d', 0.8)
            s.rect(x+40, 404, 70, 40, '#20211f', DIMC, 1, dash='4 3', op=0.3)
        elif i==1:
            s.rect(x+30, 230, 90, 90, 'none', GOOD, 2)
            for dx in (0,90):
                for dy in (0,90): s.circ(x+30+dx, 230+dy, 5, 'none', GOOD, 2)
            s.txt(x+75, 285, '100 mm', 10, GOOD, 'middle', '600')
        elif i==2:
            s.rect(x+20, 160, 110, 280, DARK, '#000', 1.2)
            s.rect(x+28, 170, 94, 250, SCREEN, SCREEN, 0)
            s.rect(x+58, 300, 34, 12, '#3a3a3a', '#3a3a3a', 1)
        else:
            s.rect(x+25, 240, 100, 70, '#2b4a66', '#16293a', 1.2)
            s.txt(x+75, 280, 'Pi 4', 11, '#dbe6f0', 'middle', '700')
            s.add(f'<path d="M {x+25} 275 q -30 -20 -14 -44 q 16 -22 -10 -36" stroke="#2f6b3f" '
                  f'stroke-width="2" fill="none"/>')
        s.txt(x+75, 486, t, 12, '#1b1b1b', 'middle', '700')
        for j,l in enumerate(ls):
            s.txt(x+75, 506+j*15, l, 10.3, '#555', 'middle')
        if i<3:
            s.line(x+165, 300, x+195, 300, LITE, 1, '5 4')
            s.add(f'<polygon points="{x+195},300 {x+187},296 {x+187},304" fill="{LITE}"/>')
    s.txt(80, 585, 'RECESSED (recommended)', 11.5, GOOD, weight='700')
    s.txt(80, 603, 'Monitor sits behind a window cut 0.30" inside its bezel outline. Reads as built-in; '
                   'needs C1 >= ' + f'{C1_REQ:.2f}".', 11, '#333')
    s.txt(560, 585, 'PROUD (fallback)', 11.5, WARN, weight='700')
    s.txt(560, 603, 'Monitor bolts to the face. No window at all — round holes only. Needs almost no C1.', 11, '#333')
    footer(s,[('The monitor keeps its own housing, so MR18 (nothing exposed from behind) and the thermal design '
               'are both solved by the manufacturer.', GOOD)])
    s.save('05-assembly-stack.svg')

# ============================================================ 06 RECESSED vs PROUD
def sheet06():
    S = 8.6
    W,H = 900, 925
    s = Sheet(W,H,'Recessed vs. Proud — the Remaining Aesthetic Choice',
              f'Same {MON_D}" monitor, same carrier panel, real geometry. Scale 8.6 px = 1 in.',
              'BOTH ARE VIABLE — this one goes to the docents, not the engineers')
    FL = 716.0
    for i,(lab,proud,col,note) in enumerate([('RECESSED', False, GOOD, 'reads as built into the panel'),
                                             ('PROUD', True, WARN, 'reads as mounted on the panel')]):
        x0 = 130 + i*400
        cx, yy = elevation(s, x0, FL, S, proud=proud)
        s.line(x0-20, FL, x0+CAB_W*S+20, FL, '#333', 1.4)
        s.rect(x0, 738, CAB_W*S, 24, col, col, 1)
        s.txt(cx, 755, lab, 12, '#fff', 'middle', '700')
        s.txt(cx, 782, note, 11, '#333', 'middle')
        rows = [('Window in the panel','yes, 0.30" lip' if not proud else 'none — round holes only'),
                ('C1 required', f'{C1_REQ:.2f}"' if not proud else 'almost none'),
                ('Hardest operation','a forgiving rectangle' if not proud else 'drill press'),
                ('Monitor changeable','unbolt + lift out' if not proud else 'unbolt'),
                ('Looks','built-in' if not proud else 'bolted-on')]
        yv = 808
        for a,b in rows:
            s.txt(x0, yv, a, 9.5, '#888'); s.txt(x0+CAB_W*S, yv, b, 10, '#333','end','600')
            s.line(x0, yv+4, x0+CAB_W*S, yv+4, '#e6e6e6', 0.7); yv += 17
    s.save('06-recessed-vs-proud.svg')

# ============================================================
if __name__ == '__main__':
    print(f'geometry: aperture {APER_W:.2f} x {APER_H:.3f} @ {APER_BOT:.2f} AFF | '
          f'door {DOOR_W:.2f} x {DOOR_H:.3f} @ {DOOR_BOT:.3f} AFF | monitor {MON_D}" '
          f'{MON_OW:.2f} x {MON_OH:.2f} | C1 req {C1_REQ:.2f}"')
    for f in (sheet01, sheet02, sheet03, sheet04, sheet05, sheet06): f()
