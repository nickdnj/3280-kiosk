#!/usr/bin/env python3
"""
3280-K assembly manual — IKEA-style, one SVG per page.

IKEA manuals are wordless because IKEA ships you finished parts. We do not:
every part here has to be cut from a shelf, so the parts, cut-plan and hardware
pages carry numerals. Everything after that is pictures.

    python3 make-manual.py
"""
import math, os
import _geom_k as G
from _draw import Page, iso, INK, GHOST, W_HEAVY, W_MED, W_LIGHT, W_HAIR

OUT = 'manual'
TOTAL = 15


# ── isometric helpers ────────────────────────────────────────────────────────
def ipoly(pg, pts3, ox, oy, sc, **kw):
    pg.poly([(ox + iso(*p)[0]*sc, oy + iso(*p)[1]*sc) for p in pts3], **kw)


def icirc(pg, cu, cv, wd, r, ox, oy, sc, n=28, **kw):
    ipoly(pg, [(cu + r*math.cos(2*math.pi*i/n), cv + r*math.sin(2*math.pi*i/n), wd)
               for i in range(n)], ox, oy, sc, **kw)


def ipt(u, v, wd, ox, oy, sc):
    p = iso(u, v, wd)
    return ox + p[0]*sc, oy + p[1]*sc


# ── the product ──────────────────────────────────────────────────────────────
WIN_V0 = G.OA_H - G.WIN_TOP - 21.240
WIN_V1 = G.OA_H - G.WIN_TOP
WIN_U0, WIN_U1 = 1.600, 1.600 + 12.170
BTN_V = G.OA_H - G.BTN_TOP
BTN_U = [G.OA_W/2 - G.BTN_CC, G.OA_W/2, G.OA_W/2 + G.BTN_CC]


def face_plate(pg, ox, oy, sc, lw=W_MED):
    """P1 on the front plane, with its window and three switches."""
    D = G.OA_D
    ipoly(pg, [(WIN_U0, WIN_V0, D), (WIN_U1, WIN_V0, D),
               (WIN_U1, WIN_V1, D), (WIN_U0, WIN_V1, D)], ox, oy, sc, w=lw, fill='#EDEFF1')
    for u in BTN_U:
        icirc(pg, u, BTN_V, D, G.BTN_DIA/2, ox, oy, sc, w=lw, fill='#FFFFFF')


def kiosk(pg, ox, oy, sc, face=True, lw=W_MED):
    pg.slab(0, 0, 0, G.OA_W, G.OA_H, G.OA_D, ox, oy, sc, lw=lw)
    if face:
        face_plate(pg, ox, oy, sc, lw)


def box_only(pg, ox, oy, sc, lw=W_MED):
    """The four-sided pine tube, open front and back."""
    T, D = G.T, G.TUBE_D
    pg.slab(0, 0, 0, T, G.OA_H, D, ox, oy, sc, lw=lw)                       # left
    pg.slab(G.OA_W-T, 0, 0, T, G.OA_H, D, ox, oy, sc, lw=lw)                # right
    pg.slab(T, G.OA_H-T, 0, G.CAV_W, T, D, ox, oy, sc, lw=lw)               # top
    pg.slab(T, 0, 0, G.CAV_W, T, D, ox, oy, sc, lw=lw)                      # bottom


def rear_module(p, ox, oy, sc, w0, ou=0.0, ov=0.0, lw=W_MED, mon=True):
    """K4 with the monitor on standoffs and the Pi tray — one lift-out unit."""
    p.slab(ou, ov, w0, G.REAR_W, G.REAR_H, G.T, ox, oy, sc, lw=lw)
    mu = ou + (G.REAR_W - G.MON_OW)/2
    mv = ov + G.REAR_H - (G.MON_TOP - G.T) - G.MON_OH
    for du in (-G.VESA_HALF, G.VESA_HALF):
        for dv in (-G.VESA_HALF, G.VESA_HALF):
            p.slab(ou + G.REAR_W/2 + du - 0.10, mv + G.MON_OH/2 + dv - 0.10,
                   w0 + G.T, 0.20, 0.20, G.STANDOFF, ox, oy, sc,
                   lw=W_LIGHT, fill='#E8EAEC')
    if mon:
        p.slab(mu, mv, w0 + G.T + G.STANDOFF, G.MON_OW, G.MON_OH, G.MON_T,
               ox, oy, sc, lw=W_HEAVY)
    p.slab(ou + 1.0, ov + 1.0, w0 + G.T, G.TRAY_W, G.TRAY_D, 0.45,
           ox, oy, sc, lw=W_LIGHT, fill='#E8EAEC')
    return mu, mv


def cabinet_ghost(pg, ox, oy, sc):
    """The 3280, drawn light, with the kiosk in place on the closed door."""
    pg.slab(0, 0, 0, 24.0, 71.0, 34.0, ox, oy, sc, lw=W_LIGHT, fill='none')
    for v in (12, 24, 36, 48, 60):
        pg.iso_line((1.0, v, 34.0), (23.0, v, 34.0), ox, oy, sc, w=W_HAIR, col=GHOST)
    u0 = (24.0 - G.OA_W)/2
    pg.slab(u0, G.KIOSK_BOT, 34.0,
            G.OA_W, G.OA_H, G.OA_D, ox, oy, sc, lw=W_MED)


# ═══ 1 · COVER ══════════════════════════════════════════════════════════════
def page1():
    p = Page(1, TOTAL)
    p.text(0.80, 1.15, '3280-K', size=0.60, anchor='start')
    p.text(0.80, 1.46, 'KIOSK ENCLOSURE', size=0.175, anchor='start', weight='normal')
    p.line(0.80, 1.62, 3.05, 1.62, w=W_HEAVY)
    p.text(0.82, 1.86, 'CONCEPT — NOT A SHIPPED PRODUCT', size=0.115,
           anchor='start', weight='normal', col='#6B7075')
    kiosk(p, 2.95, 7.95, 0.200, lw=W_HEAVY)
    cabinet_ghost(p, 7.10, 9.05, 0.026)
    p.text(0.80, 10.05, f'{G.OA_W}" × {G.OA_H}" × {G.OA_D}"', size=0.155,
           anchor='start', weight='normal')
    p.text(0.80, 10.28, f'{G.weight()["total"]:.0f} lb', size=0.155,
           anchor='start', weight='normal')
    return p


# ═══ 2 · BEFORE YOU START ═══════════════════════════════════════════════════
def page2():
    p = Page(2, TOTAL)
    p.stepnum(0.95, 1.05, '!')
    bw, bh = 3.35, 2.35
    rows = [1.75, 4.45, 7.15]

    # (a) two people — the rear panel carries the monitor
    p.cross_out(0.85, rows[0], bw, bh)
    p.person(2.10, rows[0]+0.60, 0.72, arms='fwd')
    p.rect(2.55, rows[0]+0.72, 0.95, 1.05, w=W_MED)
    p.path(f'M 2.62 {rows[0]+2.05:.2f} q 0.35 0.22 0.72 0.02', w=W_MED)
    p.no(3.55, rows[0]+0.45, 0.24)
    p.tick_box(4.55, rows[0], bw, bh)
    p.person(5.35, rows[0]+0.60, 0.72, arms='fwd')
    p.person(7.05, rows[0]+0.60, 0.72, arms='fwd', mirror=True)
    p.rect(5.85, rows[0]+0.78, 1.35, 1.00, w=W_MED)
    p.tick(7.55, rows[0]+0.45, 0.26)

    # (b) screwdriver, not a hammer
    p.cross_out(0.85, rows[1], bw, bh)
    hx, hy = 2.35, rows[1]+1.25
    p.rect(hx, hy-0.16, 0.22, 0.90, w=W_MED, r=0.06)          # handle
    p.rect(hx-0.02, hy-0.62, 0.26, 0.46, w=W_MED)             # shaft
    p.rect(hx-0.30, hy-0.95, 0.82, 0.36, w=W_MED, r=0.05)     # head
    p.no(3.55, rows[1]+0.45, 0.24)
    p.tick_box(4.55, rows[1], bw, bh)
    sx, sy = 5.95, rows[1]+0.75
    p.rect(sx, sy, 0.26, 0.80, w=W_MED, r=0.10)
    p.rect(sx+0.09, sy+0.80, 0.08, 0.62, w=W_MED)
    p.rect(sx+0.03, sy+1.42, 0.20, 0.10, w=W_MED)
    p.path(f'M 6.95 {sy+0.20:.2f} L 6.95 {sy+1.05:.2f} L 7.55 {sy+1.05:.2f}', w=W_HEAVY)
    p.tick(7.55, rows[1]+0.45, 0.26)

    # (c) blanket on a bench, face down
    p.cross_out(0.85, rows[2], bw, bh)
    p.line(1.15, rows[2]+1.85, 3.75, rows[2]+1.85, w=W_HEAVY)
    p.poly([(1.75, rows[2]+1.85), (2.05, rows[2]+0.95), (3.35, rows[2]+0.95),
            (3.05, rows[2]+1.85)], w=W_MED)
    p.no(3.55, rows[2]+0.45, 0.24)
    p.tick_box(4.55, rows[2], bw, bh)
    p.line(4.85, rows[2]+1.85, 7.45, rows[2]+1.85, w=W_HEAVY)
    p.path(f'M 4.95 {rows[2]+1.80:.2f} q 0.55 -0.28 1.20 -0.12 q 0.75 0.18 1.35 -0.10 '
           f'l 0.00 0.22 q -0.60 0.28 -1.35 0.10 q -0.65 -0.16 -1.20 0.12 Z', w=W_MED)
    p.poly([(5.45, rows[2]+1.62), (5.75, rows[2]+0.85), (7.00, rows[2]+0.85),
            (6.70, rows[2]+1.62)], w=W_MED)
    p.tick(7.55, rows[2]+0.45, 0.26)
    return p


# ═══ 3 · PARTS ══════════════════════════════════════════════════════════════
def page3():
    p = Page(3, TOTAL)
    p.stepnum(0.95, 1.05, 'A')
    S = 0.125
    slots = {
        'K2': (1.10, 1.85), 'K3': (2.55, 1.85), 'K4': (4.35, 1.85),
        'K5': (1.10, 6.70), 'K6': (1.10, 7.45), 'K7': (1.10, 8.05),
        'K8': (1.10, 8.65), 'K9': (1.10, 9.25), 'K10': (5.80, 6.70),
    }
    dims = {
        'K2': (G.SIDE_D, G.SIDE_H), 'K3': (G.TOPB_D, G.TOPB_L),
        'K4': (G.REAR_W, G.REAR_H), 'K5': (G.CLEAT, G.CLV_L),
        'K6': (G.CLEAT, G.CLH_L), 'K7': (G.CLEAT, G.RAIL_L),
        'K8': (G.CLEAT, G.RCV_L), 'K9': (G.CLEAT, G.RCH_L),
        'K10': (G.TRAY_W, G.TRAY_D),
    }
    for code, name, qty, size, shelf in G.PARTS:
        x, y = slots[code]
        w_, h_ = dims[code]
        if code in ('K5', 'K6', 'K7', 'K8', 'K9'):      # cleats lie down
            w_, h_ = h_, w_
        p.rect(x, y, w_*S, h_*S, w=W_HEAVY, fill='#FFFFFF')
        p.balloon(x - 0.34, y + 0.20, code.replace('K', ''))
        p.text(x, y + h_*S + 0.235, f'{size}   ×{qty}', size=0.125,
               anchor='start', weight='normal')
        p.text(x - 0.34, y + 0.62, f'({shelf})', size=0.105, weight='normal', col='#6B7075')
    return p


# ═══ 4 · WHAT TO BUY ════════════════════════════════════════════════════════
def shelf_icon(p, x, y, L, W, sc, label, sku, usd, qty):
    p.slab(0, 0, 0, L, G.T, W, x, y, sc, lw=W_HEAVY)
    for i in range(1, 5):                                # edge-glued staves
        p.iso_line((0, G.T, W*i/5), (L, G.T, W*i/5), x, y, sc, w=W_HAIR, col=GHOST)
    p.text(x + 0.05, y + 0.62, label, size=0.155, anchor='start')
    p.text(x + 0.05, y + 0.84, sku, size=0.125, anchor='start', weight='normal', col='#6B7075')
    p.text(x + 0.05, y + 1.06, f'${usd:.2f}   ×{qty}', size=0.135, anchor='start', weight='normal')


def page4():
    p = Page(4, TOTAL)
    p.stepnum(0.95, 1.05, 'B')
    A, C = G.SHELF_A, G.SHELF_C
    sc = 0.095
    for oy, (art, sku, usd, qty, Wd) in zip(
            (2.30, 4.75, 7.20),
            [('IVAR 83×30', A['sku'], A['usd'], 2, A['W']),
             ('IVAR 83×30', A['sku'], A['usd'], 2, A['W']),
             ('IVAR 83×50', C['sku'], C['usd'], 1, C['W'])]):
        shelf_icon(p, 2.65, oy, A['L'], Wd, sc, art, sku, usd, qty)
    for dx, dy in [(0, 0), (0.42, 0.10), (0.20, 0.46)]:
        cx, cy = 6.55 + dx, 8.70 + dy
        p.poly([(cx + 0.19*math.cos(math.radians(60*k)),
                 cy + 0.19*math.sin(math.radians(60*k))) for k in range(6)],
               w=W_MED, fill='#F1F2F3')
    p.text(6.40, 9.62, 'FIXA / TRIXIG', size=0.135, anchor='start')
    p.text(6.40, 9.82, 'felt pads, ×20', size=0.115, anchor='start', weight='normal')
    p.line(1.10, 10.12, 7.35, 10.12, w=W_HEAVY)
    p.text(7.35, 10.42, f'${A["usd"]*2 + C["usd"]:.2f}', size=0.30, anchor='end')
    return p


# ═══ 5-6 · CUT PLANS ════════════════════════════════════════════════════════
def cut_sheet(p, x, y, sc, L, W, pieces, title):
    p.rect(x, y, L*sc, W*sc, w=W_HEAVY, fill='#FFFFFF')
    p.text(x, y - 0.16, title, size=0.145, anchor='start')
    p.text(x + L*sc, y - 0.16, f'{L}" × {W}" × {G.T}"', size=0.115,
           anchor='end', weight='normal', col='#6B7075')
    for (px_, py_, pw, ph, lab) in pieces:
        fill = '#FFFFFF' if lab else '#E8EAEC'
        p.rect(x + px_*sc, y + py_*sc, pw*sc, ph*sc, w=W_MED, fill=fill)
        if lab:
            p.text(x + (px_ + pw/2)*sc, y + (py_ + ph/2)*sc + 0.055, lab, size=0.125)
    # grain arrow
    p.arrow(x + 0.12, y + W*sc + 0.30, x + L*sc - 0.12, y + W*sc + 0.30, w=W_LIGHT)
    p.arrow(x + L*sc - 0.12, y + W*sc + 0.30, x + 0.12, y + W*sc + 0.30, w=W_LIGHT)


def page5():
    p = Page(5, TOTAL)
    p.stepnum(0.95, 1.05, 'C')
    K, A = G.KERF, G.SHELF_A
    sc = 0.205
    b = [i*(G.SIDE_D + K) for i in range(3)]
    a_pieces = [
        (0, b[0], G.SIDE_H, G.SIDE_D, 'K2'),
        (0, b[1], G.SIDE_H, G.SIDE_D, 'K2'),
        (0, b[2], G.TOPB_L, G.TOPB_D, 'K3'),
        (G.TOPB_L + K, b[2], G.TOPB_L, G.TOPB_D, 'K3'),
        (G.SIDE_H + K, b[0], A['L'] - G.SIDE_H - K, G.SIDE_D, ''),
        (G.SIDE_H + K, b[1], A['L'] - G.SIDE_H - K, G.SIDE_D, ''),
        (2*G.TOPB_L + 2*K, b[2], A['L'] - 2*G.TOPB_L - 2*K, G.TOPB_D, ''),
        (0, 3*(G.SIDE_D + K), A['L'], A['W'] - 3*(G.SIDE_D + K), ''),
    ]
    cut_sheet(p, 1.10, 2.05, sc, A['L'], A['W'], a_pieces, 'SHELF A   IVAR 83×30')

    b_len = A['L'] - G.TRAY_W - K
    strips = [('K5', G.CLV_L, None), ('K5', G.CLV_L, None), ('K8', G.RCV_L, None),
              ('K8', G.RCV_L, None), ('K6', G.CLH_L, 'K6'), ('K7', G.RAIL_L, 'K9'),
              ('K9', G.RCH_L, None)]
    b_pieces = [(0, 0, G.TRAY_W, G.TRAY_D, 'K10'),
                (0, G.TRAY_D + K, G.TRAY_W, A['W'] - G.TRAY_D - K, '')]
    for i, (lab, ln, lab2) in enumerate(strips):
        yy = i*(G.CLEAT + K)
        b_pieces.append((G.TRAY_W + K, yy, ln, G.CLEAT, lab))
        if lab2:
            b_pieces.append((G.TRAY_W + K + ln + K, yy, ln, G.CLEAT, lab2))
        else:
            b_pieces.append((G.TRAY_W + K + ln, yy, b_len - ln, G.CLEAT, ''))
    b_pieces.append((G.TRAY_W + K, len(strips)*(G.CLEAT + K), b_len,
                     A['W'] - len(strips)*(G.CLEAT + K), ''))
    cut_sheet(p, 1.10, 6.60, sc, A['L'], A['W'], b_pieces, 'SHELF B   IVAR 83×30')
    return p


def page6():
    p = Page(6, TOTAL)
    p.stepnum(0.95, 1.05, 'D')
    C = G.SHELF_C
    sc = 0.190
    cut_sheet(p, 1.10, 1.95, sc, C['L'], C['W'], [
        (0, 0, G.REAR_H, G.REAR_W, 'K4'),
        (G.REAR_H + G.KERF, 0, C['L'] - G.REAR_H - G.KERF, G.REAR_W, ''),
        (0, G.REAR_W + G.KERF, C['L'], C['W'] - G.REAR_W - G.KERF, ''),
    ], 'SHELF C   IVAR 83×50')

    p.text(1.10, 6.85, 'GRAIN', size=0.155, anchor='start')
    p.tick_box(1.10, 7.10, 2.85, 2.45)
    p.rect(1.80, 7.42, 1.55, 1.80, w=W_HEAVY)
    for i in range(1, 6):
        p.line(1.80 + i*0.258, 7.42, 1.80 + i*0.258, 9.22, w=W_HAIR, col=GHOST)
    p.arrow(1.55, 9.22, 1.55, 7.42, w=W_LIGHT)
    p.tick(3.62, 9.82, 0.24)
    p.cross_out(4.55, 7.10, 2.85, 2.45)
    p.rect(5.25, 7.42, 1.55, 1.80, w=W_HEAVY)
    for i in range(1, 5):
        p.line(5.25, 7.42 + i*0.36, 6.80, 7.42 + i*0.36, w=W_HAIR, col=GHOST)
    p.arrow(5.25, 9.40, 6.80, 9.40, w=W_LIGHT)
    p.no(7.05, 9.82, 0.24)
    return p


# ═══ 7 · HARDWARE ═══════════════════════════════════════════════════════════
def hw_icon(p, kind, x, y):
    if kind == 'insert':
        p.rect(x, y, 0.17, 0.44, w=W_MED)
        for i in range(4):
            p.line(x, y + 0.06 + i*0.11, x + 0.17, y + 0.02 + i*0.11, w=W_HAIR)
    elif kind == 'screw':
        p.rect(x, y, 0.26, 0.09, w=W_MED, r=0.04)
        p.rect(x + 0.085, y + 0.09, 0.09, 0.42, w=W_MED)
        for i in range(5):
            p.line(x + 0.085, y + 0.13 + i*0.08, x + 0.175, y + 0.10 + i*0.08, w=W_HAIR)
    elif kind == 'thumb':
        p.circle(x + 0.13, y + 0.11, 0.13, w=W_MED)
        for k in range(8):
            a = math.radians(45*k)
            p.line(x + 0.13 + 0.11*math.cos(a), y + 0.11 + 0.11*math.sin(a),
                   x + 0.13 + 0.15*math.cos(a), y + 0.11 + 0.15*math.sin(a), w=W_HAIR)
        p.rect(x + 0.085, y + 0.22, 0.09, 0.34, w=W_MED)
    elif kind == 'bolt':
        pts = [(x + 0.13 + 0.12*math.cos(math.radians(60*k + 30)),
                y + 0.11 + 0.12*math.sin(math.radians(60*k + 30))) for k in range(6)]
        p.poly(pts, w=W_MED)
        p.rect(x + 0.095, y + 0.22, 0.07, 0.34, w=W_MED)
    elif kind == 'standoff':
        p.rect(x + 0.05, y, 0.16, 0.47, w=W_MED)
        p.rect(x + 0.095, y + 0.47, 0.07, 0.17, w=W_MED)
        p.line(x + 0.05, y + 0.09, x + 0.21, y + 0.09, w=W_HAIR)
    elif kind == 'switch':
        p.circle(x + 0.20, y + 0.20, 0.20, w=W_MED)
        p.circle(x + 0.20, y + 0.20, 0.12, w=W_HAIR)
        p.rect(x + 0.11, y + 0.40, 0.18, 0.26, w=W_MED)
    elif kind == 'inlet':
        p.rect(x, y + 0.06, 0.46, 0.34, w=W_MED, r=0.05)
        for i in range(3):
            p.line(x + 0.13 + i*0.10, y + 0.16, x + 0.13 + i*0.10, y + 0.30, w=W_MED)
    elif kind == 'glue':
        p.rect(x + 0.04, y + 0.14, 0.24, 0.50, w=W_MED, r=0.05)
        p.poly([(x + 0.12, y + 0.14), (x + 0.16, y), (x + 0.20, y + 0.14)], w=W_MED)


def page7():
    p = Page(7, TOTAL)
    p.stepnum(0.95, 1.05, 'E')
    kinds = ['insert', 'screw', 'thumb', 'bolt', 'standoff', 'switch', 'inlet', 'screw', 'glue']
    y = 1.95
    for (code, name, qty, note), kind in zip(G.HARDWARE, kinds):
        p.balloon(1.15, y + 0.22, code)
        hw_icon(p, kind, 1.70, y)
        p.text(2.45, y + 0.30, name, size=0.135, anchor='start', weight='normal')
        p.text(7.35, y + 0.30, f'×{qty}', size=0.165, anchor='end')
        p.line(1.15, y + 0.80, 7.35, y + 0.80, w=W_HAIR, col=GHOST)
        y += 0.95
    return p


# ═══ 8 · TOOLS ══════════════════════════════════════════════════════════════
def page8():
    p = Page(8, TOTAL)
    p.stepnum(0.95, 1.05, 'F')
    cell = [(1.35, 2.10), (3.55, 2.10), (5.75, 2.10),
            (1.35, 4.55), (3.55, 4.55), (5.75, 4.55),
            (1.35, 7.00), (3.55, 7.00), (5.75, 7.00)]
    def saw(x, y):
        p.poly([(x + 0.05, y + 0.50), (x + 1.00, y + 0.62),
                (x + 1.00, y + 0.88), (x + 0.05, y + 0.86)], w=W_MED)
        teeth = []
        for i in range(11):
            teeth.append((x + 0.07 + i*0.085, y + 0.86 + (0.00 if i % 2 else 0.09)))
        p.poly(teeth, w=W_HAIR, close=False)
        p.rect(x + 1.00, y + 0.52, 0.30, 0.46, w=W_MED, r=0.10)
        p.circle(x + 1.15, y + 0.75, 0.10, w=W_HAIR)
    def drill(x, y):
        p.rect(x + 0.15, y + 0.35, 0.72, 0.42, w=W_MED, r=0.10)
        p.rect(x + 0.28, y + 0.77, 0.30, 0.55, w=W_MED, r=0.07)
        p.rect(x + 0.87, y + 0.47, 0.42, 0.18, w=W_MED)
    def driver(x, y):
        p.rect(x + 0.42, y + 0.25, 0.26, 0.62, w=W_MED, r=0.10)
        p.rect(x + 0.51, y + 0.87, 0.08, 0.45, w=W_MED)
    def clamp(x, y):
        p.rect(x + 0.20, y + 0.30, 0.20, 1.00, w=W_MED)
        p.rect(x + 0.20, y + 0.30, 0.95, 0.18, w=W_MED)
        p.rect(x + 0.20, y + 1.12, 0.95, 0.18, w=W_MED)
        p.rect(x + 0.95, y + 0.48, 0.16, 0.42, w=W_MED)
    def tape(x, y):
        p.rect(x + 0.15, y + 0.55, 0.70, 0.62, w=W_MED, r=0.10)
        p.circle(x + 0.50, y + 0.86, 0.18, w=W_MED)
        p.rect(x + 0.85, y + 0.92, 0.48, 0.13, w=W_MED)
    def square(x, y):
        p.poly([(x + 0.15, y + 0.35), (x + 0.35, y + 0.35), (x + 0.35, y + 1.10),
                (x + 1.20, y + 1.10), (x + 1.20, y + 1.30), (x + 0.15, y + 1.30)], w=W_MED)
    def pencil(x, y):
        p.rect(x + 0.20, y + 0.45, 0.16, 0.72, w=W_MED)
        p.poly([(x + 0.20, y + 1.17), (x + 0.28, y + 1.32), (x + 0.36, y + 1.17)], w=W_MED)
    def sand(x, y):
        p.rect(x + 0.20, y + 0.45, 0.95, 0.80, w=W_MED, r=0.05)
        for i in range(16):
            cx = x + 0.28 + (i % 5)*0.20
            cy = y + 0.55 + (i // 5)*0.20
            p.circle(cx, cy, 0.022, w=W_HAIR, fill=INK)
    def bit(x, y):
        p.rect(x + 0.45, y + 0.35, 0.14, 0.30, w=W_MED)
        p.path(f'M {x+0.45:.2f} {y+0.65:.2f} L {x+0.45:.2f} {y+1.25:.2f} '
               f'L {x+0.59:.2f} {y+1.25:.2f} L {x+0.59:.2f} {y+0.65:.2f}', w=W_MED)
        for i in range(4):
            p.line(x + 0.45, y + 0.72 + i*0.14, x + 0.59, y + 0.80 + i*0.14, w=W_HAIR)
    for fn, (x, y) in zip([saw, drill, bit, driver, clamp, square, tape, pencil, sand], cell):
        fn(x, y)
    return p


# ═══ 9-14 · ASSEMBLY ════════════════════════════════════════════════════════
SC = 0.150
OX, OY = 3.30, 8.05


def page9():
    """Tube: two sides, top and bottom. Glue and screw."""
    p = Page(9, TOTAL)
    p.stepnum(0.95, 1.05, 1)
    box_only(p, OX, OY, SC, lw=W_HEAVY)
    p.balloon(*ipt(G.T/2, G.OA_H*0.62, G.TUBE_D, OX, OY, SC), '2')
    bx, by = ipt(G.OA_W - G.T/2, G.OA_H*0.30, G.TUBE_D, OX, OY, SC)
    p.balloon(bx + 0.46, by, '2')
    p.line(bx, by, bx + 0.30, by, w=W_HAIR)
    p.balloon(*ipt(G.OA_W/2, G.OA_H - G.T/2, G.TUBE_D, OX, OY, SC), '3')
    p.balloon(*ipt(G.OA_W/2, G.T/2, G.TUBE_D, OX, OY, SC), '3')
    for v in (G.OA_H - G.T/2, G.T/2):
        for u in (G.T/2, G.OA_W - G.T/2):
            x, y = ipt(u, v, G.TUBE_D*0.5, OX, OY, SC)
            p.arrow(x - 0.62, y + 0.36, x - 0.14, y + 0.08, w=W_LIGHT, head=0.09)

    cx, cy, r = 6.30, 3.25, 1.00
    p.detail_bubble(cx, cy, r, *ipt(G.OA_W - G.T/2, G.OA_H - G.T/2,
                                    G.TUBE_D*0.5, OX, OY, SC), 0.30)
    p.rect(cx - 0.45, cy - 0.50, 0.36, 1.10, w=W_MED)          # side panel, K2
    p.rect(cx - 0.09, cy - 0.50, 0.80, 0.36, w=W_MED)          # top panel, K3
    p.line(cx - 0.09, cy - 0.14, cx + 0.71, cy - 0.14, w=W_HAIR, dash='0.04 0.03')
    p.line(cx - 0.62, cy - 0.32, cx + 0.28, cy - 0.32, w=W_MED)   # screw shank
    p.rect(cx - 0.68, cy - 0.38, 0.07, 0.12, w=W_MED)             # screw head
    p.balloon(cx - 0.10, cy + 0.72, '8')
    p.line(cx - 0.20, cy - 0.32, cx - 0.13, cy + 0.57, w=W_HAIR)
    return p


def page10():
    """Cleats: front flush, rear flush, button rail."""
    p = Page(10, TOTAL)
    p.stepnum(0.95, 1.05, 2)
    box_only(p, OX, OY, SC, lw=W_MED)
    D, T, C = G.TUBE_D, G.T, G.CLEAT

    def cleat(u, v, w_, du, dv, dw, lab, lx, ly):
        p.slab(u, v, w_, du, dv, dw, OX, OY, SC, lw=W_HEAVY, fill='#E8EAEC')
        px, py = ipt(u + du/2, v + dv/2, w_ + dw, OX, OY, SC)
        p.balloon(px + lx, py + ly, lab)
        p.line(px, py, px + lx*0.70, py + ly*0.70, w=W_HAIR)

    cleat(T, T, 0, C, G.RCV_L, C, '8', -1.00, 0.30)
    cleat(T + C, T, 0, G.RCH_L, C, C, '9', -0.20, 1.05)
    cleat(T, T, D - C, C, G.CLV_L, C, '5', -0.82, -0.55)
    cleat(G.OA_W - T - C, T, D - C, C, G.CLV_L, C, '5', 0.80, -0.15)
    cleat(T + C, G.OA_H - T - C, D - C, G.CLH_L, C, C, '6', 0.34, -0.66)
    cleat(T + C, T, D - C, G.CLH_L, C, C, '6', 0.86, 0.52)
    cleat(T + C, G.OA_H - G.RAIL_TOP - C/2, D - C, G.RAIL_L, C, C, '7', 0.98, 0.10)

    cx, cy, r = 6.35, 3.10, 0.95
    p.detail_bubble(cx, cy, r, *ipt(G.T + G.CLEAT/2, G.OA_H*0.55, G.TUBE_D,
                                    OX, OY, SC), 0.28)
    p.rect(cx - 0.72, cy - 0.55, 0.30, 1.10, w=W_MED)      # K2 in section
    p.rect(cx - 0.42, cy - 0.55, 0.30, 0.30, w=W_MED)      # K5, flush at the front
    p.line(cx - 0.72, cy - 0.66, cx + 0.10, cy - 0.66, w=W_HAIR, dash='0.04 0.03')
    p.arrow(cx + 0.42, cy - 0.66, cx + 0.14, cy - 0.66, w=W_LIGHT, head=0.09)
    p.text(cx + 0.48, cy - 0.60, '0', size=0.145, anchor='start')
    return p


def page11():
    """Threaded inserts — 15 on the P1 pattern in front, 6 for K4 behind."""
    p = Page(11, TOTAL)
    p.stepnum(0.95, 1.05, 3)
    box_only(p, OX, OY, SC, lw=W_LIGHT)
    ys = [G.EDGE_FACE + i*(G.OA_H - 2*G.EDGE_FACE)/4 for i in range(5)]
    front = [(G.EDGE_FACE, y) for y in ys] + [(G.OA_W - G.EDGE_FACE, y) for y in ys]
    front += [(G.OA_W/2, G.EDGE_FACE), (G.OA_W/2, G.OA_H - G.EDGE_FACE)]
    vr = G.OA_H - G.RAIL_TOP
    front += [(3.50, vr), (G.OA_W/2, vr), (G.OA_W - 3.50, vr)]
    for u, v in front:
        icirc(p, u, v, G.TUBE_D, 0.20, OX, OY, SC, w=W_MED, fill='#FFFFFF')
    rear = [(u, v) for u in (G.T + G.CLEAT/2, G.OA_W - G.T - G.CLEAT/2)
            for v in (2.4, G.OA_H/2, G.OA_H - 2.4)]
    for u, v in rear:
        icirc(p, u, v, 0.20, 0.20, OX, OY, SC, w=W_MED, fill='#FFFFFF')

    x, y = ipt(G.OA_W - G.EDGE_FACE, ys[1], G.TUBE_D, OX, OY, SC)
    p.text(x + 0.72, y + 0.06, f'×{len(front)}', size=0.20, anchor='start')
    p.line(x + 0.14, y, x + 0.66, y, w=W_HAIR)
    x, y = ipt(G.OA_W - G.T - G.CLEAT/2, 2.4, 0.20, OX, OY, SC)
    p.text(x + 0.72, y + 0.06, f'×{len(rear)}', size=0.20, anchor='start')
    p.line(x + 0.14, y, x + 0.66, y, w=W_HAIR)
    p.balloon(6.55, 9.55, '1')
    p.text(6.90, 9.63, f'×{len(front) + len(rear)}', size=0.26, anchor='start')

    cx, cy, r = 6.35, 2.80, 0.92
    p.detail_bubble(cx, cy, r, *ipt(G.EDGE_FACE, ys[3], G.TUBE_D, OX, OY, SC), 0.26)
    p.rect(cx - 0.55, cy - 0.20, 1.10, 0.72, w=W_MED)
    p.line(cx + 0.02, cy - 0.20, cx + 0.02, cy + 0.52, w=W_HAIR, dash='0.04 0.03')
    hw_icon(p, 'insert', cx - 0.09, cy - 0.14)
    p.arrow(cx, cy - 0.72, cx, cy - 0.26, w=W_LIGHT, head=0.09)
    return p


def page12():
    """The rear-panel module: standoffs, monitor, Pi tray."""
    p = Page(12, TOTAL)
    p.stepnum(0.95, 1.05, 4)
    ox, oy, sc = 3.30, 7.40, 0.150
    p.slab(0, 0, 0, G.REAR_W, G.REAR_H, G.T, ox, oy, sc, lw=W_HEAVY)
    px, py = ipt(0.6, G.REAR_H*0.5, G.T, ox, oy, sc)
    p.balloon(px - 0.62, py, '4')
    mu = (G.REAR_W - G.MON_OW)/2
    mv = G.REAR_H - (G.MON_TOP - G.T) - G.MON_OH
    for du in (-G.VESA_HALF, G.VESA_HALF):
        for dv in (-G.VESA_HALF, G.VESA_HALF):
            u = G.REAR_W/2 + du
            v = mv + G.MON_OH/2 + dv
            p.slab(u - 0.10, v - 0.10, G.T, 0.20, 0.20, G.STANDOFF, ox, oy, sc,
                   lw=W_MED, fill='#E8EAEC')
    p.slab(mu, mv, G.T + G.STANDOFF, G.MON_OW, G.MON_OH, G.MON_T, ox, oy, sc, lw=W_HEAVY)
    px, py = ipt(mu + G.MON_OW/2, mv + G.MON_OH, G.T + G.STANDOFF + G.MON_T, ox, oy, sc)
    p.balloon(px + 0.05, py - 0.60, 'E3')
    p.line(px, py, px + 0.04, py - 0.44, w=W_HAIR)
    p.slab(1.0, 1.0, G.T, G.TRAY_W, G.TRAY_D, 0.45, ox, oy, sc, lw=W_MED, fill='#E8EAEC')
    px, py = ipt(1.0 + G.TRAY_W/2, 1.0, G.T + 0.45, ox, oy, sc)
    p.balloon(px - 0.18, py + 0.58, '10')
    p.detail_bubble(6.55, 3.10, 0.86, *ipt(G.REAR_W/2 + G.VESA_HALF,
                    mv + G.MON_OH/2 + G.VESA_HALF, G.T + G.STANDOFF, ox, oy, sc), 0.26)
    p.rect(5.85, 3.32, 1.40, 0.34, w=W_MED)
    hw_icon(p, 'standoff', 6.42, 2.66)
    p.arrow(6.50, 3.95, 6.50, 3.72, w=W_LIGHT)
    p.balloon(6.05, 2.48, '5')
    p.balloon(7.10, 2.48, '4')
    return p


def page13():
    """The module drops in from behind. Tool-free."""
    p = Page(13, TOTAL)
    p.stepnum(0.95, 1.05, 5)
    ox, oy, sc = 3.05, 6.75, 0.140
    OFF = 10.0
    box_only(p, ox, oy, sc, lw=W_LIGHT)
    rear_module(p, ox, oy, sc, -OFF, ou=G.T + 0.10, ov=G.T + 0.05, lw=W_MED)
    a = ipt(G.OA_W/2, 3.2, -OFF + G.T, ox, oy, sc)
    b = ipt(G.OA_W/2, 3.2, 0.45, ox, oy, sc)
    p.arrow(a[0], a[1], b[0], b[1], w=W_HEAVY, head=0.17)
    for u in (G.T + G.CLEAT/2, G.OA_W - G.T - G.CLEAT/2):
        for v in (2.4, G.OA_H/2, G.OA_H - 2.4):
            icirc(p, u, v, 0.20, 0.26, ox, oy, sc, w=W_MED, fill='#FFFFFF')
    p.balloon(6.42, 9.40, '3')
    p.text(6.78, 9.48, '×6', size=0.26, anchor='start')
    p.no(1.55, 9.40, 0.26)
    hw_icon(p, 'screw', 1.98, 9.14)
    return p


def page14():
    """Switches into P1, wire it, then the face plate."""
    p = Page(14, TOTAL)
    p.stepnum(0.95, 1.05, 6)
    ox, oy, sc = 3.05, 7.30, 0.145
    OFF = 5.0
    box_only(p, ox, oy, sc, lw=W_LIGHT)
    D = G.OA_D + OFF
    p.slab(0, 0, D - G.T_ACM, G.OA_W, G.OA_H, G.T_ACM, ox, oy, sc, lw=W_HEAVY)
    ipoly(p, [(WIN_U0, WIN_V0, D), (WIN_U1, WIN_V0, D),
              (WIN_U1, WIN_V1, D), (WIN_U0, WIN_V1, D)], ox, oy, sc,
          w=W_MED, fill='#EDEFF1')
    for u in BTN_U:
        icirc(p, u, BTN_V, D, G.BTN_DIA/2, ox, oy, sc, w=W_MED, fill='#FFFFFF')

    hx, hy = ipt(BTN_U[0], BTN_V, D, ox, oy, sc)
    sx, sy = hx - 1.35, hy + 0.60
    p.circle(sx, sy, 0.24, w=W_HEAVY, fill='#FFFFFF')
    p.circle(sx, sy, 0.14, w=W_HAIR)
    p.rect(sx - 0.13, sy + 0.24, 0.26, 0.34, w=W_MED)
    for k in range(4):
        p.line(sx - 0.13, sy + 0.30 + k*0.08, sx + 0.13, sy + 0.27 + k*0.08, w=W_HAIR)
    p.arrow(sx + 0.32, sy - 0.10, hx - 0.16, hy + 0.10, w=W_MED, head=0.12)
    p.balloon(sx - 0.02, sy - 0.62, '6')
    p.text(sx + 0.22, sy - 0.55, '\u00d73', size=0.185, anchor='start')

    a = ipt(G.OA_W/2, G.OA_H*0.80, D + 0.30, ox, oy, sc)
    b = ipt(G.OA_W/2, G.OA_H*0.80, G.OA_D + 0.25, ox, oy, sc)
    p.arrow(a[0], a[1], b[0], b[1], w=W_HEAVY, head=0.17)
    p.balloon(6.42, 9.55, '2')
    p.text(6.78, 9.63, '\u00d715', size=0.26, anchor='start')
    return p


def page15():
    """Finished — and the one thing not to do yet."""
    p = Page(15, TOTAL)
    kiosk(p, 2.95, 6.55, 0.152, lw=W_HEAVY)
    p.circle(6.85, 2.20, 0.42, w=W_HEAVY)
    p.tick(6.85, 2.25, 0.36)

    p.cross_out(1.35, 8.20, 5.95, 2.15)
    S = 0.0265
    cab_x, cab_y = 5.45, 8.42
    p.rect(cab_x, cab_y, 24.0*S, 71.0*S, w=W_MED)
    p.line(cab_x, cab_y + (71.0 - 3.125)*S, cab_x + 24.0*S,
           cab_y + (71.0 - 3.125)*S, w=W_HAIR, col=GHOST)
    kx = 3.15
    ky = cab_y + (71.0 - G.KIOSK_BOT - G.OA_H)*S
    p.rect(kx, ky, G.OA_W*S, G.OA_H*S, w=W_HEAVY, fill='#FFFFFF')
    p.rect(kx + 1.60*S, ky + G.WIN_TOP*S, 12.170*S, 21.240*S, w=W_HAIR, fill='#EDEFF1')
    p.arrow(kx + G.OA_W*S + 0.30, ky + G.OA_H*S/2,
            cab_x + (24.0 - G.OA_W)/2*S - 0.06, ky + G.OA_H*S/2, w=W_MED)
    p.no(6.85, 9.90, 0.26)
    return p


# ── driver ───────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    pages = [page1, page2, page3, page4, page5, page6, page7, page8,
             page9, page10, page11, page12, page13, page14, page15]
    assert len(pages) == TOTAL, f'{len(pages)} pages, TOTAL says {TOTAL}'
    bad = 0
    for fn in pages:
        pg = fn()
        path = os.path.join(OUT, f'{pg.n:02d}.svg')
        pg.save(path)
        flag = '' if not pg.stray else f'   <<< {len(pg.stray)} OFF-PAGE {pg.stray[:4]}'
        bad += len(pg.stray)
        print(f'  {path}   {len(pg.o):3d} elements   '
              f'x {pg.bb[0]:5.2f}-{pg.bb[2]:5.2f}  y {pg.bb[1]:5.2f}-{pg.bb[3]:5.2f}{flag}')
    print(f'\n{TOTAL} pages -> {OUT}/'
          + ('   ALL ON PAGE' if not bad else f'   *** {bad} OFF-PAGE ***'))
