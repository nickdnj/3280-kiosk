#!/usr/bin/env python3
"""
Build cookbook for the 15 x 30 box — one SVG per page, wordless where it can be.

Numerals appear only where a human has to measure something. Everything else is
pictures. Geometry comes from _kit.py -> ../fab-rev1/_p1.py.

    python3 make-manual.py
"""
import math, os
import _kit as K
from _draw import Page, iso, INK, GHOST, W_HEAVY, W_MED, W_LIGHT, W_HAIR

OUT, TOTAL = 'manual', 20
P = K.P


def ipoly(pg, pts, ox, oy, sc, **kw):
    pg.poly([(ox + iso(*q)[0]*sc, oy + iso(*q)[1]*sc) for q in pts], **kw)

def icirc(pg, cu, cv, wd, r, ox, oy, sc, n=28, **kw):
    ipoly(pg, [(cu + r*math.cos(2*math.pi*i/n), cv + r*math.sin(2*math.pi*i/n), wd)
               for i in range(n)], ox, oy, sc, **kw)

def ipt(u, v, wd, ox, oy, sc):
    q = iso(u, v, wd)
    return ox + q[0]*sc, oy + q[1]*sc


# ── the product ─────────────────────────────────────────────────────────────
WIN_V0 = K.OA_H - P.WIN_Y - P.WIN_H
WIN_V1 = K.OA_H - P.WIN_Y
BTN_V  = K.OA_H - P.BTN_Y
RAIL_V = K.OA_H - P.RAIL_Y


def tube(pg, ox, oy, sc, lw=W_MED):
    T, D = K.T, K.BW
    pg.slab(0, 0, 0, T, K.OA_H, D, ox, oy, sc, lw=lw)
    pg.slab(K.OA_W-T, 0, 0, T, K.OA_H, D, ox, oy, sc, lw=lw)
    pg.slab(T, K.OA_H-T, 0, K.CAV_W, T, D, ox, oy, sc, lw=lw)
    pg.slab(T, 0, 0, K.CAV_W, T, D, ox, oy, sc, lw=lw)


def faceplate(pg, ox, oy, sc, w0, lw=W_MED):
    pg.slab(0, 0, w0, K.OA_W, K.OA_H, P.MAT_T, ox, oy, sc, lw=lw)
    d = w0 + P.MAT_T
    ipoly(pg, [(P.WIN_X, WIN_V0, d), (P.WIN_X+P.WIN_W, WIN_V0, d),
               (P.WIN_X+P.WIN_W, WIN_V1, d), (P.WIN_X, WIN_V1, d)],
          ox, oy, sc, w=W_MED, fill='#EDEFF1')
    for x in P.BTN_X:
        icirc(pg, x, BTN_V, d, P.BTN_D/2, ox, oy, sc, w=W_MED, fill='#FFFFFF')


def finished(pg, ox, oy, sc, lw=W_HEAVY):
    pg.slab(0, 0, 0, K.OA_W, K.OA_H, K.OA_D, ox, oy, sc, lw=lw)
    faceplate(pg, ox, oy, sc, K.OA_D - P.MAT_T, lw=lw)


# ═══ 01 COVER ═══════════════════════════════════════════════════════════════
def p01():
    p = Page(1, TOTAL)
    p.text(0.80, 1.15, '3280-K', size=0.58, anchor='start')
    p.text(0.80, 1.46, 'BOX — BUILD COOKBOOK', size=0.175, anchor='start', weight='normal')
    p.line(0.80, 1.62, 3.60, 1.62, w=W_HEAVY)
    p.text(0.82, 1.86, 'CONCEPT — NOT A SHIPPED PRODUCT', size=0.115,
           anchor='start', weight='normal', col='#6B7075')
    finished(p, 3.05, 7.95, 0.185)
    p.text(0.80, 9.95, '15 × 30 × 3-5/8"', size=0.16, anchor='start', weight='normal')
    p.text(0.80, 10.18, '9 crosscuts · no rips', size=0.16, anchor='start', weight='normal')
    p.text(0.80, 10.41, '≈ 24 lb', size=0.16, anchor='start', weight='normal')
    return p


# ═══ 02 BEFORE YOU START ════════════════════════════════════════════════════
def p02():
    p = Page(2, TOTAL)
    p.stepnum(0.95, 1.05, '!')
    bw, bh, rows = 3.35, 2.25, [1.75, 4.30, 6.85]

    p.tick_box(0.85, rows[0], bw, bh)                       # eye + lung
    p.circle(2.05, rows[0]+1.00, 0.34, w=W_HEAVY)
    p.path(f'M 1.62 {rows[0]+0.92:.2f} q 0.43 -0.34 0.86 0', w=W_HEAVY)
    p.line(1.71, rows[0]+1.00, 2.39, rows[0]+1.00, w=W_MED)
    p.circle(3.05, rows[0]+1.05, 0.30, w=W_HEAVY)
    for i in range(3):
        p.line(2.83, rows[0]+0.96+i*0.09, 3.27, rows[0]+0.96+i*0.09, w=W_HAIR)
    p.tick(2.55, rows[0]+1.86, 0.26)
    p.tick_box(4.55, rows[0], bw, bh)                       # flat, on a blanket
    p.line(4.85, rows[0]+1.72, 7.45, rows[0]+1.72, w=W_HEAVY)
    p.path(f'M 4.95 {rows[0]+1.67:.2f} q 0.55 -0.26 1.20 -0.11 q 0.75 0.17 1.35 -0.09 '
           f'l 0 0.21 q -0.60 0.26 -1.35 0.09 q -0.65 -0.15 -1.20 0.11 Z', w=W_MED)
    p.poly([(5.45, rows[0]+1.50), (5.75, rows[0]+0.80), (7.00, rows[0]+0.80),
            (6.70, rows[0]+1.50)], w=W_MED)
    p.tick(7.55, rows[0]+1.86, 0.26)

    p.cross_out(0.85, rows[1], bw, bh)                      # no hammer
    hx, hy = 2.30, rows[1]+1.20
    p.rect(hx, hy-0.14, 0.22, 0.82, w=W_MED, r=0.06)
    p.rect(hx-0.02, hy-0.56, 0.26, 0.42, w=W_MED)
    p.rect(hx-0.30, hy-0.88, 0.82, 0.32, w=W_MED, r=0.05)
    p.no(3.55, rows[1]+0.42, 0.24)
    p.tick_box(4.55, rows[1], bw, bh)                       # pilot every hole
    p.rect(5.55, rows[1]+0.85, 1.30, 0.55, w=W_MED)
    p.line(6.20, rows[1]+0.85, 6.20, rows[1]+1.85, w=W_MED, dash='0.06 0.05')
    p.arrow(6.20, rows[1]+1.95, 6.20, rows[1]+1.48, w=W_LIGHT, head=0.10)
    p.rect(6.13, rows[1]+0.40, 0.14, 0.42, w=W_MED)
    p.tick(7.55, rows[1]+1.86, 0.26)

    p.cross_out(0.85, rows[2], bw, bh)                      # one person
    p.person(1.95, rows[2]+0.55, 0.68, arms='fwd')
    p.rect(2.40, rows[2]+0.66, 0.90, 1.05, w=W_MED)
    p.no(3.55, rows[2]+0.42, 0.24)
    p.tick_box(4.55, rows[2], bw, bh)                       # two people
    p.person(5.30, rows[2]+0.55, 0.68, arms='fwd')
    p.person(6.95, rows[2]+0.55, 0.68, arms='fwd', mirror=True)
    p.rect(5.78, rows[2]+0.72, 1.30, 0.98, w=W_MED)
    p.tick(7.55, rows[2]+1.86, 0.26)
    return p


# ═══ 03 WOOD AS BOUGHT ══════════════════════════════════════════════════════
def board(p, x, y, L, W, sc, label, model, qty):
    p.slab(0, 0, 0, L, K.T, W, x, y, sc, lw=W_HEAVY)
    for i in range(1, 4):
        p.iso_line((0, K.T, W*i/4), (L, K.T, W*i/4), x, y, sc, w=W_HAIR, col=GHOST)
    p.text(x + 0.05, y + 0.60, label, size=0.155, anchor='start')
    p.text(x + 0.05, y + 0.82, model, size=0.12, anchor='start', weight='normal', col='#6B7075')
    p.text(x + 0.05, y + 1.04, f'×{qty}', size=0.145, anchor='start')


def p03():
    p = Page(3, TOTAL)
    p.stepnum(0.95, 1.05, 'A')
    board(p, 2.55, 2.20, 96, 3.5, 0.055, '1×4 × 8 ft', '914681 · .750 × 3.5', 2)
    board(p, 2.55, 4.70, 96, 2.5, 0.055, '1×3 × 8 ft', '914649 · .750 × 2.5', 3)
    MS = 0.060
    p.rect(1.35, 7.00, 24*MS, 48*MS, w=W_HEAVY, fill='#F1F2F3')
    p.rect(1.35, 7.00, K.REAR_W*MS, K.REAR_H*MS, w=W_MED, fill='#FFFFFF')
    p.text(1.35 + K.REAR_W*MS/2, 7.00 + K.REAR_H*MS/2, 'P4', size=0.135)
    p.rect(1.35, 7.00 + (K.REAR_H+0.5)*MS, K.TRAY[0]*MS, K.TRAY[1]*MS,
           w=W_MED, fill='#FFFFFF')
    p.text(1.35 + K.TRAY[0]*MS/2, 7.00 + (K.REAR_H+0.5)*MS + K.TRAY[1]*MS/2 + 0.04,
           'P10', size=0.10)
    p.text(1.35, 6.82, '½" MDF  2 × 4', size=0.155, anchor='start')
    p.text(3.35, 7.35, '109097', size=0.12, anchor='start', weight='normal', col='#6B7075')
    p.text(3.35, 7.62, 'HOME DEPOT', size=0.145, anchor='start')
    p.text(3.35, 7.84, 'CUTS THIS', size=0.145, anchor='start')
    p.text(3.35, 8.22, 'P4   13-1/4 × 28-1/4', size=0.135, anchor='start', weight='normal')
    p.text(3.35, 8.44, 'P10  4 × 3', size=0.135, anchor='start', weight='normal')
    p.text(3.35, 8.80, 'you never handle', size=0.115, anchor='start',
           weight='normal', col='#6B7075')
    p.text(3.35, 8.98, 'a sheet good', size=0.115, anchor='start',
           weight='normal', col='#6B7075')
    return p


# ═══ 04 PARTS ═══════════════════════════════════════════════════════════════
def p04():
    p = Page(4, TOTAL)
    p.stepnum(0.95, 1.05, 'B')
    S = 0.115
    slots = {'P2': (1.20, 1.90), 'P3': (2.35, 1.90), 'P8': (3.35, 1.90),
             'P9': (4.35, 1.90), 'P4': (5.35, 1.90),
             'P7': (1.20, 6.10), 'P10': (1.20, 7.15), 'P1': (3.60, 6.10)}
    for code, name, stock, ww, ll, q, nice in K.PARTS:
        if code not in slots:
            continue
        x, y = slots[code]
        if code == 'P7':
            ww, ll = ll, ww
        fill = '#F1F2F3' if stock == 'MDF' else ('#E4E7E9' if stock == 'ACM' else '#FFFFFF')
        p.rect(x, y, ww*S, ll*S, w=W_HEAVY, fill=fill)
        p.balloon(x + 0.20, y - 0.22, code.replace('P', ''))
        p.text(x, y + ll*S + 0.22, nice, size=0.115, anchor='start', weight='normal')
        p.text(x, y + ll*S + 0.41, f'{stock}  ×{q}', size=0.115, anchor='start', col='#6B7075')
    return p


# ═══ 05 FASTENERS ═══════════════════════════════════════════════════════════
def hw(p, kind, x, y):
    if kind == 'screw':
        p.poly([(x, y+0.10), (x+0.13, y), (x+0.26, y+0.10)], w=W_MED)
        p.rect(x+0.085, y+0.10, 0.09, 0.44, w=W_MED)
        for i in range(5):
            p.line(x+0.085, y+0.15+i*0.08, x+0.175, y+0.12+i*0.08, w=W_HAIR)
    elif kind == 'insert':
        p.rect(x+0.04, y, 0.19, 0.42, w=W_MED)
        for i in range(4):
            p.line(x+0.04, y+0.06+i*0.10, x+0.23, y+0.02+i*0.10, w=W_HAIR)
        p.line(x+0.10, y, x+0.10, y+0.42, w=W_HAIR, dash='0.03 0.03')
    elif kind == 'button':
        p.path(f'M {x:.3f} {y+0.10:.3f} q 0.13 -0.14 0.26 0', w=W_MED)
        p.line(x, y+0.10, x+0.26, y+0.10, w=W_MED)
        p.rect(x+0.09, y+0.10, 0.08, 0.40, w=W_MED)
    elif kind == 'thumb':
        p.circle(x+0.13, y+0.11, 0.12, w=W_MED)
        for k in range(8):
            a = math.radians(45*k)
            p.line(x+0.13+0.10*math.cos(a), y+0.11+0.10*math.sin(a),
                   x+0.13+0.15*math.cos(a), y+0.11+0.15*math.sin(a), w=W_HAIR)
        p.rect(x+0.09, y+0.23, 0.08, 0.30, w=W_MED)
    elif kind == 'bolt':
        p.poly([(x+0.13+0.115*math.cos(math.radians(60*k+30)),
                 y+0.11+0.115*math.sin(math.radians(60*k+30))) for k in range(6)], w=W_MED)
        p.rect(x+0.095, y+0.23, 0.07, 0.30, w=W_MED)
        p.circle(x+0.13, y+0.26, 0.15, w=W_HAIR)
    elif kind == 'switch':
        p.circle(x+0.20, y+0.19, 0.19, w=W_MED)
        p.circle(x+0.20, y+0.19, 0.11, w=W_HAIR)
        p.rect(x+0.11, y+0.38, 0.18, 0.24, w=W_MED)
    elif kind == 'inlet':
        p.rect(x, y+0.08, 0.44, 0.32, w=W_MED, r=0.05)
        for i in range(3):
            p.line(x+0.12+i*0.10, y+0.17, x+0.12+i*0.10, y+0.31, w=W_MED)
    elif kind == 'glue':
        p.rect(x+0.04, y+0.14, 0.22, 0.46, w=W_MED, r=0.05)
        p.poly([(x+0.11, y+0.14), (x+0.15, y), (x+0.19, y+0.14)], w=W_MED)
    elif kind == 'epoxy':
        p.rect(x, y+0.16, 0.13, 0.42, w=W_MED, r=0.04)
        p.rect(x+0.15, y+0.16, 0.13, 0.42, w=W_MED, r=0.04)
        p.line(x+0.065, y+0.16, x+0.065, y+0.05, w=W_MED)
        p.line(x+0.215, y+0.16, x+0.215, y+0.05, w=W_MED)
    elif kind == 'can':
        p.rect(x, y+0.14, 0.30, 0.44, w=W_MED)
        p.path(f'M {x+0.05:.3f} {y+0.14:.3f} q 0.10 -0.12 0.20 0', w=W_MED)


def p05():
    p = Page(5, TOTAL)
    p.stepnum(0.95, 1.05, 'C')
    y = 1.90
    for code, name, qty, kind, note in K.FASTENERS:
        p.balloon(1.15, y + 0.24, code)
        hw(p, kind, 1.68, y)
        p.text(2.35, y + 0.22, name, size=0.125, anchor='start', weight='normal')
        p.text(2.35, y + 0.42, note, size=0.105, anchor='start', weight='normal', col='#6B7075')
        p.text(7.35, y + 0.30, f'×{qty}', size=0.19, anchor='end')
        p.line(1.15, y + 0.72, 7.35, y + 0.72, w=W_HAIR, col=GHOST)
        y += 0.90
    return p


# ═══ 06 GLUE AND FINISH ═════════════════════════════════════════════════════
def p06():
    p = Page(6, TOTAL)
    p.stepnum(0.95, 1.05, 'D')
    y = 2.00
    for code, name, kind, note in K.GLUES:
        p.balloon(1.15, y + 0.26, code)
        hw(p, kind, 1.68, y)
        p.text(2.35, y + 0.24, name, size=0.135, anchor='start', weight='normal')
        p.text(2.35, y + 0.45, note, size=0.11, anchor='start', weight='normal', col='#6B7075')
        p.line(1.15, y + 0.78, 7.35, y + 0.78, w=W_HAIR, col=GHOST)
        y += 0.98

    # ALL SIX FACES
    p.text(1.15, 6.85, 'ALL SIX FACES', size=0.165, anchor='start')
    p.tick_box(1.15, 7.10, 2.85, 2.40)
    p.slab(0, 0, 0, 1.4, 1.0, 1.0, 2.30, 8.55, 0.68, lw=W_HEAVY, fill='#DFE3E6')
    p.tick(3.62, 9.78, 0.24)
    p.cross_out(4.55, 7.10, 2.85, 2.40)
    p.slab(0, 0, 0, 1.4, 1.0, 1.0, 5.70, 8.55, 0.68, lw=W_HEAVY, fill='#FFFFFF')
    p.no(7.05, 9.78, 0.24)
    return p


# ═══ 07 TOOLS ═══════════════════════════════════════════════════════════════
def p07():
    p = Page(7, TOTAL)
    p.stepnum(0.95, 1.05, 'E')
    cells = [(1.25 + (i % 3)*2.20, 1.95 + (i // 3)*2.10) for i in range(12)]

    def saw(x, y):
        p.poly([(x+0.05, y+0.45), (x+1.00, y+0.57), (x+1.00, y+0.83), (x+0.05, y+0.81)], w=W_MED)
        p.poly([(x+0.07+i*0.085, y+0.81 + (0 if i % 2 else 0.09)) for i in range(11)],
               w=W_HAIR, close=False)
        p.rect(x+1.00, y+0.47, 0.28, 0.44, w=W_MED, r=0.10)
    def tape(x, y):
        p.rect(x+0.10, y+0.45, 0.68, 0.60, w=W_MED, r=0.10)
        p.circle(x+0.44, y+0.75, 0.17, w=W_MED)
        p.rect(x+0.78, y+0.80, 0.46, 0.12, w=W_MED)
    def square(x, y):
        p.poly([(x+0.10, y+0.35), (x+0.30, y+0.35), (x+0.30, y+0.98),
                (x+1.10, y+0.98), (x+1.10, y+1.18), (x+0.10, y+1.18)], w=W_MED)
    def pencil(x, y):
        p.rect(x+0.30, y+0.45, 0.15, 0.66, w=W_MED)
        p.poly([(x+0.30, y+1.11), (x+0.375, y+1.24), (x+0.45, y+1.11)], w=W_MED)
    def drill(x, y):
        p.rect(x+0.12, y+0.35, 0.70, 0.40, w=W_MED, r=0.10)
        p.rect(x+0.25, y+0.75, 0.28, 0.50, w=W_MED, r=0.07)
        p.rect(x+0.82, y+0.46, 0.38, 0.17, w=W_MED)
    def bits(x, y):
        for i, h in enumerate((0.75, 0.60, 0.45)):
            bx = x + 0.20 + i*0.30
            p.rect(bx, y+0.40, 0.11, h, w=W_MED)
            for k in range(4):
                p.line(bx, y+0.48+k*0.11, bx+0.11, y+0.54+k*0.11, w=W_HAIR)
    def driver(x, y):
        p.rect(x+0.38, y+0.30, 0.24, 0.55, w=W_MED, r=0.10)
        p.rect(x+0.46, y+0.85, 0.08, 0.40, w=W_MED)
    def clamp(x, y):
        p.rect(x+0.18, y+0.32, 0.18, 0.92, w=W_MED)
        p.rect(x+0.18, y+0.32, 0.88, 0.16, w=W_MED)
        p.rect(x+0.18, y+1.08, 0.88, 0.16, w=W_MED)
        p.rect(x+0.88, y+0.48, 0.15, 0.38, w=W_MED)
    def sand(x, y):
        p.rect(x+0.18, y+0.45, 0.90, 0.74, w=W_MED, r=0.05)
        for i in range(15):
            p.circle(x+0.26+(i % 5)*0.19, y+0.55+(i//5)*0.19, 0.021, w=W_HAIR, fill=INK)
    def glasses(x, y):
        p.path(f'M {x+0.15:.2f} {y+0.75:.2f} q 0.50 -0.30 1.05 0 l 0 0.28 '
               f'q -0.55 0.26 -1.05 0 Z', w=W_MED)
        p.line(x+0.15, y+0.78, x+0.05, y+0.62, w=W_MED)
        p.line(x+1.20, y+0.78, x+1.30, y+0.62, w=W_MED)
    def mask(x, y):
        p.path(f'M {x+0.20:.2f} {y+0.68:.2f} q 0.45 -0.34 0.90 0 '
               f'q -0.10 0.52 -0.45 0.52 q -0.35 0 -0.45 -0.52 Z', w=W_MED)
        p.line(x+0.20, y+0.68, x+1.14, y+0.55, w=W_HAIR)
    def brush(x, y):
        p.rect(x+0.36, y+0.35, 0.14, 0.55, w=W_MED)
        p.rect(x+0.28, y+0.90, 0.30, 0.30, w=W_MED)
    for fn, (x, y) in zip([saw, tape, square, pencil, drill, bits,
                           driver, clamp, sand, glasses, mask, brush], cells):
        fn(x, y)
    return p


# ═══ 08 HOW TO MEASURE ══════════════════════════════════════════════════════
def p08():
    p = Page(8, TOTAL)
    p.stepnum(0.95, 1.05, 1)
    # measure from ONE end, always
    p.rect(1.20, 2.10, 6.10, 0.95, w=W_HEAVY)
    p.line(1.20, 3.35, 1.20, 3.75, w=W_HAIR)
    p.line(5.60, 3.35, 5.60, 3.75, w=W_HAIR)
    p.arrow(1.20, 3.58, 5.60, 3.58, w=W_MED)
    p.arrow(5.60, 3.58, 1.20, 3.58, w=W_MED)
    p.text(3.40, 3.48, '30', size=0.24)
    p.line(5.60, 2.05, 5.60, 3.10, w=W_HEAVY, dash='0.10 0.06')
    p.text(5.72, 2.00, 'CUT', size=0.135, anchor='start')

    # square the line, mark with a knife
    p.tick_box(1.20, 4.35, 2.85, 2.30)
    p.rect(1.60, 5.05, 1.55, 0.85, w=W_MED)
    p.line(2.45, 4.85, 2.45, 6.10, w=W_HEAVY)
    p.poly([(2.15, 4.95), (2.45, 4.95), (2.45, 5.25)], w=W_MED)
    p.tick(3.72, 6.90, 0.24)
    p.cross_out(4.45, 4.35, 2.85, 2.30)
    p.rect(4.85, 5.05, 1.55, 0.85, w=W_MED)
    p.path('M 5.55 4.88 L 5.80 6.08', w=W_HEAVY)
    p.no(7.02, 6.90, 0.24)

    # cut on the waste side of the line
    p.rect(1.20, 7.65, 6.10, 0.95, w=W_HEAVY)
    p.rect(5.10, 7.65, 2.20, 0.95, w=W_HAIR, fill='#E8EAEC')
    p.line(5.10, 7.55, 5.10, 8.80, w=W_HEAVY)
    p.arrow(4.60, 9.05, 5.02, 8.72, w=W_MED)
    p.text(4.45, 9.28, 'BLADE HERE', size=0.135, anchor='end')
    p.text(6.20, 9.05, 'WASTE', size=0.135, col='#6B7075')
    return p


# ═══ 09 THE NINE CROSSCUTS ══════════════════════════════════════════════════
def p09():
    p = Page(9, TOTAL)
    p.stepnum(0.95, 1.05, 2)
    S = 0.062

    def stick(y, L, W, cuts, label):
        p.rect(1.20, y, L*S, W*0.115, w=W_HEAVY, fill='#FFFFFF')
        p.text(1.20, y - 0.14, label, size=0.13, anchor='start')
        x = 0.0
        for ln, name in cuts:
            p.line(1.20 + (x+ln)*S, y - 0.06, 1.20 + (x+ln)*S, y + W*0.115 + 0.06,
                   w=W_MED, dash='0.07 0.05')
            p.text(1.20 + (x + ln/2)*S, y + W*0.115/2 + 0.05, name, size=0.115)
            x += ln + 0.125
        p.rect(1.20 + x*S, y, (L - x)*S, W*0.115, w=W_HAIR, fill='#E8EAEC')

    stick(2.05, 96, 3.5, [(30, 'P2'), (30, 'P2'), (13.5, 'P3'), (13.5, 'P3')],
          '1×4 #1   —   4 cuts')
    stick(3.35, 96, 2.5, [(28.5, 'P8'), (28.5, 'P8'), (28.5, 'P9')],
          '1×3 #1   —   3 cuts')
    stick(4.55, 96, 2.5, [(28.5, 'P9'), (13.5, 'P7')],
          '1×3 #2   —   2 cuts')

    p.line(1.20, 5.60, 7.30, 5.60, w=W_HAIR, col=GHOST)
    p.text(1.20, 5.95, '9', size=0.45, anchor='start')
    p.text(1.75, 5.95, 'CUTS', size=0.22, anchor='start')

    # the golden rule
    p.tick_box(1.20, 6.45, 6.10, 3.10)
    tube(p, 3.35, 8.55, 0.070, lw=W_MED)
    p.arrow(5.10, 7.65, 4.35, 8.05, w=W_MED)
    p.text(5.22, 7.60, 'CUT P2 FIRST', size=0.145, anchor='start')
    p.text(5.22, 7.82, 'DRY-FIT', size=0.145, anchor='start')
    p.text(5.22, 8.04, 'MEASURE THE', size=0.145, anchor='start')
    p.text(5.22, 8.26, 'REAL CAVITY', size=0.145, anchor='start')
    p.text(5.22, 8.60, 'then cut everything', size=0.115, anchor='start',
           weight='normal', col='#6B7075')
    p.text(5.22, 8.78, 'else to what you', size=0.115, anchor='start',
           weight='normal', col='#6B7075')
    p.text(5.22, 8.96, 'measured', size=0.115, anchor='start', weight='normal', col='#6B7075')
    return p


# ═══ 10-19 ASSEMBLY ═════════════════════════════════════════════════════════
SC, OX, OY = 0.145, 3.15, 7.55


def step(n, num):
    p = Page(n, TOTAL)
    p.stepnum(0.95, 1.05, num)
    return p


def p10():
    """Dry fit, clamp, measure."""
    p = step(10, 3)
    tube(p, OX, OY, SC, lw=W_HEAVY)
    a = ipt(K.T, K.OA_H/2, K.BW, OX, OY, SC)
    b = ipt(K.OA_W-K.T, K.OA_H/2, K.BW, OX, OY, SC)
    p.arrow(a[0], a[1], b[0], b[1], w=W_MED)
    p.arrow(b[0], b[1], a[0], a[1], w=W_MED)
    p.text((a[0]+b[0])/2, (a[1]+b[1])/2 - 0.16, '?', size=0.30)
    for v in (2.0, K.OA_H-2.0):
        for u in (0.0, K.OA_W-K.T):
            x, y = ipt(u+K.T/2, v, K.BW/2, OX, OY, SC)
            p.rect(x-0.16, y-0.30, 0.32, 0.60, w=W_MED)
    p.text(1.10, 10.05, 'CLAMP · MEASURE · THEN CUT', size=0.155, anchor='start')
    return p


def p11():
    """Tube: pilot, glue, screw."""
    p = step(11, 4)
    tube(p, OX, OY, SC, lw=W_HEAVY)
    p.balloon(*ipt(K.T/2, K.OA_H*0.62, K.BW, OX, OY, SC), '2')
    p.balloon(*ipt(K.OA_W/2, K.OA_H-K.T/2, K.BW, OX, OY, SC), '3')
    p.balloon(*ipt(K.OA_W/2, K.T/2, K.BW, OX, OY, SC), '3')
    cx, cy, r = 6.35, 3.20, 1.00
    p.detail_bubble(cx, cy, r, *ipt(K.OA_W-K.T/2, K.OA_H-K.T/2, K.BW/2, OX, OY, SC), 0.30)
    p.rect(cx-0.46, cy-0.50, 0.34, 1.08, w=W_MED)
    p.rect(cx-0.12, cy-0.50, 0.78, 0.34, w=W_MED)
    p.line(cx-0.12, cy-0.16, cx+0.66, cy-0.16, w=W_HAIR, dash='0.04 0.03')
    p.line(cx-0.62, cy-0.33, cx+0.26, cy-0.33, w=W_MED)
    p.poly([(cx-0.70, cy-0.40), (cx-0.62, cy-0.33), (cx-0.70, cy-0.26)], w=W_MED)
    p.balloon(cx-0.08, cy+0.74, 'F1')
    p.line(cx-0.20, cy-0.33, cx-0.11, cy+0.58, w=W_HAIR)
    p.text(1.10, 10.05, 'PILOT 7/64  ·  GLUE  ·  SCREW', size=0.155, anchor='start')
    return p


def p12():
    """Button rail, front flush, 6 up from the bottom."""
    p = step(12, 5)
    tube(p, OX, OY, SC, lw=W_MED)
    p.slab(K.T, RAIL_V - K.T/2, K.BW - K.CW, K.CAV_W, K.T, K.CW,
           OX, OY, SC, lw=W_HEAVY, fill='#E8EAEC')
    x, y = ipt(K.OA_W/2, RAIL_V, K.BW, OX, OY, SC)
    p.balloon(x + 0.92, y + 0.10, '7')
    p.line(x, y, x + 0.72, y + 0.08, w=W_HAIR)
    bx, by = ipt(0, 0, K.BW, OX, OY, SC)
    p.line(bx - 0.42, by, bx - 0.10, by, w=W_HAIR)
    rx, ry = ipt(0, RAIL_V, K.BW, OX, OY, SC)
    p.line(rx - 0.42, ry, rx - 0.10, ry, w=W_HAIR)
    p.arrow(bx - 0.30, by, rx - 0.30, ry, w=W_MED)
    p.arrow(rx - 0.30, ry, bx - 0.30, by, w=W_MED)
    p.text(bx - 0.62, (by + ry)/2, '6', size=0.26, anchor='end')
    p.text(1.10, 10.05, 'FRONT FLUSH', size=0.155, anchor='start')
    return p


def p13():
    """Rear cleats, turned 90."""
    p = step(13, 6)
    tube(p, OX, OY, SC, lw=W_MED)
    for u in (K.T, K.OA_W - K.T - K.CW):
        p.slab(u, K.T, K.BW - K.T4 - K.T, K.CW, K.CAV_H, K.T,
               OX, OY, SC, lw=W_HEAVY, fill='#E8EAEC')
    x, y = ipt(K.T + K.CW/2, K.OA_H*0.5, K.BW - K.T4, OX, OY, SC)
    p.balloon(x - 0.86, y, '8')
    p.line(x, y, x - 0.60, y, w=W_HAIR)
    cx, cy, r = 6.30, 3.05, 0.95
    p.detail_bubble(cx, cy, r, x, y, 0.26)
    p.rect(cx-0.30, cy-0.62, 0.34, 1.24, w=W_MED)            # side wall in section
    p.rect(cx+0.04, cy-0.20, 0.62, 0.30, w=W_MED)            # cleat, laid flat
    p.text(cx+0.34, cy+0.02, '90°', size=0.13)
    p.arrow(cx+0.70, cy-0.52, cx+0.70, cy-0.24, w=W_LIGHT, head=0.09)
    p.text(1.10, 10.05, 'TURNED FLAT — 3/4 DEEP, BEHIND THE SCREEN', size=0.145, anchor='start')
    return p


def p14():
    """Inserts: drill 3/8, epoxy, 21 of them."""
    p = step(14, 7)
    tube(p, OX, OY, SC, lw=W_LIGHT)
    for x, y in P.MOUNT:
        icirc(p, x, K.OA_H - y, K.BW, 0.19, OX, OY, SC, w=W_MED, fill='#FFFFFF')
    for u in (K.T + K.CW/2, K.OA_W - K.T - K.CW/2):
        for v in (2.5, K.OA_H/2, K.OA_H - 2.5):
            icirc(p, u, v, 0.20, 0.19, OX, OY, SC, w=W_MED, fill='#FFFFFF')
    p.balloon(6.35, 9.45, 'F2')
    p.text(6.72, 9.53, '×21', size=0.26, anchor='start')
    cx, cy, r = 6.30, 2.80, 0.92
    p.detail_bubble(cx, cy, r, *ipt(P.EDGE, K.OA_H - P.MOUNT_Y[3], K.BW, OX, OY, SC), 0.24)
    p.rect(cx-0.52, cy-0.18, 1.04, 0.68, w=W_MED)
    p.line(cx, cy-0.18, cx, cy+0.50, w=W_HAIR, dash='0.04 0.03')
    hw(p, 'insert', cx-0.14, cy-0.10)
    p.arrow(cx, cy-0.74, cx, cy-0.28, w=W_LIGHT, head=0.09)
    p.text(1.10, 10.05, 'DRILL 3/8  ·  EPOXY  ·  FLUSH', size=0.155, anchor='start')
    return p


def p15():
    """VESA rails."""
    p = step(15, 8)
    tube(p, OX, OY, SC, lw=W_MED)
    for du in (-K.VESA/2, K.VESA/2):
        u = K.OA_W/2 + du - K.CW/2
        p.slab(u, K.T, K.BW - K.T4 - K.T, K.CW, K.CAV_H, K.T,
               OX, OY, SC, lw=W_HEAVY, fill='#E8EAEC')
    x, y = ipt(K.OA_W/2 + K.VESA/2, K.OA_H*0.62, K.BW - K.T4, OX, OY, SC)
    p.balloon(x + 0.80, y - 0.10, '9')
    p.line(x, y, x + 0.54, y - 0.08, w=W_HAIR)
    a = ipt(K.OA_W/2 - K.VESA/2, 2.2, K.BW - K.T4, OX, OY, SC)
    b = ipt(K.OA_W/2 + K.VESA/2, 2.2, K.BW - K.T4, OX, OY, SC)
    p.line(a[0], a[1] + 0.55, a[0], a[1] + 0.05, w=W_HAIR)
    p.line(b[0], b[1] + 0.55, b[0], b[1] + 0.05, w=W_HAIR)
    p.arrow(a[0], a[1] + 0.42, b[0], b[1] + 0.42, w=W_LIGHT, head=0.09)
    p.arrow(b[0], b[1] + 0.42, a[0], a[1] + 0.42, w=W_LIGHT, head=0.09)
    p.text((a[0]+b[0])/2, (a[1]+b[1])/2 + 0.78, '100 mm', size=0.155)
    p.text(1.10, 10.05, 'VESA 100', size=0.155, anchor='start')
    return p


def p16():
    """Seal and paint — all six faces, before anything goes in."""
    p = step(16, 9)
    tube(p, OX, OY, SC, lw=W_MED)
    for u in (0.9, K.OA_W*0.5, K.OA_W - 1.6):
        x, y = ipt(u, K.OA_H*0.55, K.BW, OX, OY, SC)
        p.path(f'M {x:.2f} {y:.2f} q 0.20 -0.42 0.40 0', w=W_MED)
    bx, by = 1.55, 9.35
    p.rect(bx, by, 0.30, 0.44, w=W_MED)
    p.rect(bx+0.09, by-0.55, 0.13, 0.55, w=W_MED)
    p.rect(bx+0.02, by-0.85, 0.27, 0.30, w=W_MED)
    p.text(1.10, 10.30, 'SEAL ALL SIX FACES — INSIDE TOO', size=0.155, anchor='start')
    return p


def p17():
    """Monitor onto the rails, Pi tray below."""
    p = step(17, 10)
    tube(p, OX, OY, SC, lw=W_LIGHT)
    mu = (K.OA_W - P.MON_OW)/2
    mv = K.OA_H - P.MON_TOP - P.MON_OH
    p.slab(mu, mv, K.BW - K.T4 - K.T - P.MON_T, P.MON_OW, P.MON_OH, P.MON_T,
           OX, OY, SC, lw=W_HEAVY)
    p.slab(1.2, 1.2, K.BW - K.T4 - K.T, K.TRAY[0], K.TRAY[1], 0.45,
           OX, OY, SC, lw=W_MED, fill='#E8EAEC')
    x, y = ipt(1.2 + K.TRAY[0]/2, 1.2, K.BW - K.T4 - K.T + 0.45, OX, OY, SC)
    p.balloon(x - 0.20, y + 0.62, '10')
    p.balloon(6.35, 9.45, 'F5')
    p.text(6.72, 9.53, '×4', size=0.26, anchor='start')
    p.text(1.10, 10.05, 'MONITOR ONTO THE RAILS', size=0.155, anchor='start')
    return p


def p18():
    """Switches into P1, then wire."""
    p = step(18, 11)
    ox, oy, sc = 3.05, 7.40, 0.145
    tube(p, ox, oy, sc, lw=W_LIGHT)
    OFF = 5.0
    faceplate(p, ox, oy, sc, K.OA_D - P.MAT_T + OFF, lw=W_HEAVY)
    d = K.OA_D + OFF
    hx, hy = ipt(P.BTN_X[0], BTN_V, d, ox, oy, sc)
    sx, sy = hx - 1.30, hy + 0.62
    p.circle(sx, sy, 0.23, w=W_HEAVY, fill='#FFFFFF')
    p.circle(sx, sy, 0.13, w=W_HAIR)
    p.rect(sx-0.13, sy+0.23, 0.26, 0.32, w=W_MED)
    for k in range(4):
        p.line(sx-0.13, sy+0.29+k*0.07, sx+0.13, sy+0.26+k*0.07, w=W_HAIR)
    p.arrow(sx+0.31, sy-0.10, hx-0.16, hy+0.10, w=W_MED, head=0.12)
    p.balloon(sx-0.02, sy-0.60, 'F6')
    p.text(sx+0.22, sy-0.53, '×3', size=0.185, anchor='start')
    p.text(1.10, 10.05, 'SWITCHES FIRST, THEN WIRE', size=0.155, anchor='start')
    return p


def p19():
    """Face plate on, then the back."""
    p = step(19, 12)
    ox, oy, sc = 3.05, 7.40, 0.145
    tube(p, ox, oy, sc, lw=W_MED)
    OFF = 3.6
    faceplate(p, ox, oy, sc, K.OA_D - P.MAT_T + OFF, lw=W_HEAVY)
    a = ipt(K.OA_W/2, K.OA_H*0.80, K.OA_D + OFF, ox, oy, sc)
    b = ipt(K.OA_W/2, K.OA_H*0.80, K.OA_D + 0.3, ox, oy, sc)
    p.arrow(a[0], a[1], b[0], b[1], w=W_HEAVY, head=0.17)
    p.slab(K.T+0.125, K.T+0.125, -7.5, K.REAR_W, K.REAR_H, K.T4,
           ox, oy, sc, lw=W_MED, fill='#F1F2F3')
    c = ipt(K.OA_W/2, 3.0, -7.5 + K.T4, ox, oy, sc)
    e = ipt(K.OA_W/2, 3.0, K.BW - K.T4 - 0.2, ox, oy, sc)
    p.arrow(c[0], c[1], e[0], e[1], w=W_HEAVY, head=0.17)
    p.balloon(1.35, 9.35, 'F3')
    p.text(1.72, 9.43, '×15', size=0.20, anchor='start')
    p.balloon(1.35, 9.90, 'F4')
    p.text(1.72, 9.98, '×6', size=0.20, anchor='start')
    p.no(6.60, 9.90, 0.24)
    hw(p, 'screw', 7.00, 9.66)
    return p


# ═══ 20 DONE ════════════════════════════════════════════════════════════════
def p20():
    p = Page(20, TOTAL)
    finished(p, 2.95, 6.55, 0.152)
    p.circle(6.85, 2.20, 0.42, w=W_HEAVY)
    p.tick(6.85, 2.25, 0.36)
    p.cross_out(1.35, 8.20, 5.95, 2.15)
    S = 0.0265
    cab_x, cab_y = 5.45, 8.42
    p.rect(cab_x, cab_y, 24.0*S, 71.0*S, w=W_MED)
    p.line(cab_x, cab_y + (71.0-3.125)*S, cab_x + 24.0*S, cab_y + (71.0-3.125)*S,
           w=W_HAIR, col=GHOST)
    kx = 3.15
    ky = cab_y + (71.0 - 34.0 - K.OA_H)*S
    p.rect(kx, ky, K.OA_W*S, K.OA_H*S, w=W_HEAVY, fill='#FFFFFF')
    p.rect(kx + P.WIN_X*S, ky + P.WIN_Y*S, P.WIN_W*S, P.WIN_H*S, w=W_HAIR, fill='#EDEFF1')
    p.arrow(kx + K.OA_W*S + 0.30, ky + K.OA_H*S/2,
            cab_x + (24.0-K.OA_W)/2*S - 0.06, ky + K.OA_H*S/2, w=W_MED)
    p.no(6.85, 9.90, 0.26)
    return p


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    pages = [p01, p02, p03, p04, p05, p06, p07, p08, p09, p10,
             p11, p12, p13, p14, p15, p16, p17, p18, p19, p20]
    assert len(pages) == TOTAL, f'{len(pages)} pages, TOTAL says {TOTAL}'
    bad = 0
    for fn in pages:
        pg = fn()
        path = os.path.join(OUT, f'{pg.n:02d}.svg')
        pg.save(path)
        bad += len(pg.stray)
        flag = '' if not pg.stray else f'   <<< OFF-PAGE {pg.stray[:3]}'
        print(f'  {path}   {len(pg.o):3d} el   x {pg.bb[0]:5.2f}-{pg.bb[2]:5.2f}'
              f'  y {pg.bb[1]:5.2f}-{pg.bb[3]:5.2f}{flag}')
    print(f'\n{TOTAL} pages -> {OUT}/' + ('   ALL ON PAGE' if not bad
                                          else f'   *** {bad} OFF-PAGE ***'))
