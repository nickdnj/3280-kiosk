#!/usr/bin/env python3
"""
1:1 printable stencil for P1, tiled onto US Letter pages.

Print at 100% scale with margins set to None, tape the sheets together on the
registration marks, cut the voids, and use it to transfer the shape to cardboard.

    python3 make-stencil.py     ->  stencil-letter.html
"""
import math
import _p1 as P

# ── plate geometry: the SAME module the DXF is cut from ─────────────────────
PW, PH        = P.PW, P.PH
WIN_X, WIN_Y  = P.WIN_X, P.WIN_Y
WIN_W, WIN_H  = P.WIN_W, P.WIN_H
BTN_CC, BTN_D = P.BTN_CC, P.BTN_D
BTN_Y         = P.BTN_Y
EDGE, HOLE    = P.EDGE, P.HOLE
RAIL_Y        = P.RAIL_Y
R_OUT = R_IN  = P.R_OUT

mount = list(P.MOUNT)
btn   = list(P.BUTTONS)

# ── page layout ─────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = 8.5, 11.0
WIN_L, WIN_T   = 0.30, 0.88            # artwork window on the page
ART_W, ART_H   = 7.90, 9.90
MIN_OVL = 0.40                         # smallest tape/registration band we accept
COLS = math.ceil((PW - MIN_OVL) / (ART_W - MIN_OVL))
ROWS = math.ceil((PH - MIN_OVL) / (ART_H - MIN_OVL))
sx = [i*(PW - ART_W)/(COLS-1) for i in range(COLS)] if COLS > 1 else [0]
sy = [j*(PH - ART_H)/(ROWS-1) for j in range(ROWS)] if ROWS > 1 else [0]
OVL_X = ART_W - (sx[1]-sx[0] if COLS > 1 else ART_W)
OVL_Y = ART_H - (sy[1]-sy[0] if ROWS > 1 else ART_H)

def f(v, p=4):
    return f'{v:.{p}f}'.rstrip('0').rstrip('.') or '0'

def rr(x, y, w, h, r):
    return (f'M{f(x+r)} {f(y)}H{f(x+w-r)}A{f(r)} {f(r)} 0 0 1 {f(x+w)} {f(y+r)}'
            f'V{f(y+h-r)}A{f(r)} {f(r)} 0 0 1 {f(x+w-r)} {f(y+h)}'
            f'H{f(x+r)}A{f(r)} {f(r)} 0 0 1 {f(x)} {f(y+h-r)}'
            f'V{f(y+r)}A{f(r)} {f(r)} 0 0 1 {f(x+r)} {f(y)}Z')

def tile_svg(cx, cy):
    """Artwork for the tile whose top-left is at plate coords (cx, cy)."""
    o = [f'<svg class="art" width="{ART_W}in" height="{ART_H}in" '
         f'viewBox="{f(cx)} {f(cy)} {ART_W} {ART_H}" '
         f'xmlns="http://www.w3.org/2000/svg">']
    # 1 inch grid, labelled in plate coordinates
    g = []
    for gx in range(math.floor(cx), math.ceil(cx+ART_W)+1):
        if 0 <= gx <= PW: g.append(f'M{gx} {f(max(cy,0))}V{f(min(cy+ART_H,PH))}')
    for gy in range(math.floor(cy), math.ceil(cy+ART_H)+1):
        if 0 <= gy <= PH: g.append(f'M{f(max(cx,0))} {gy}H{f(min(cx+ART_W,PW))}')
    o.append(f'<path d="{"".join(g)}" stroke="#C8D4D8" stroke-width=".008" fill="none"/>')
    for gx in range(math.floor(cx), math.ceil(cx+ART_W)+1):
        for gy in range(math.floor(cy), math.ceil(cy+ART_H)+1):
            if 0 <= gx <= PW and 0 <= gy <= PH and gx % 2 == 0 and gy % 2 == 0:
                o.append(f'<text x="{gx+.05}" y="{gy-.06}" font-size=".13" fill="#7FA0AC" '
                         f'font-family="monospace">{gx},{gy}</text>')
    # mounting holes — mark only
    for hx, hy in mount:
        o.append(f'<path d="M{f(hx-.13)} {f(hy)}H{f(hx+.13)}M{f(hx)} {f(hy-.13)}V{f(hy+.13)}" '
                 f'stroke="#6C7A80" stroke-width=".012" fill="none"/>')
        o.append(f'<circle cx="{f(hx)}" cy="{f(hy)}" r="{f(HOLE/2)}" stroke="#6C7A80" '
                 f'stroke-width=".010" fill="none"/>')
    # button voids
    for bx, by in btn:
        o.append(f'<circle cx="{f(bx)}" cy="{f(by)}" r="{f(BTN_D/2)}" stroke="#111" '
                 f'stroke-width=".026" fill="none" stroke-dasharray=".16 .09"/>')
        o.append(f'<path d="M{f(bx-.34)} {f(by)}H{f(bx+.34)}M{f(bx)} {f(by-.34)}V{f(by+.34)}" '
                 f'stroke="#111" stroke-width=".010" fill="none"/>')
    # screen void
    o.append(f'<path d="{rr(WIN_X, WIN_Y, WIN_W, WIN_H, R_IN)}" stroke="#111" '
             f'stroke-width=".030" fill="none" stroke-dasharray=".22 .12"/>')
    # plate outline
    o.append(f'<path d="{rr(0, 0, PW, PH, R_OUT)}" stroke="#111" stroke-width=".034" fill="none"/>')
    # labels, only where they land on this tile
    def lab(x, y, s, size=.17, col='#111', anch='middle'):
        if cx-1 < x < cx+ART_W+1 and cy-.5 < y < cy+ART_H+.5:
            o.append(f'<text x="{f(x)}" y="{f(y)}" font-size="{size}" fill="{col}" '
                     f'font-family="monospace" font-weight="700" text-anchor="{anch}">{s}</text>')
    # left-anchored and kept inside column 1 so nothing is clipped at a tile edge
    lab(2.20, WIN_Y + WIN_H/2, 'CUT OUT — SCREEN WINDOW', .17, '#111', 'start')
    lab(2.20, WIN_Y + WIN_H/2 + .28, f'{WIN_W:g} x {WIN_H:g}', .13, '#555', 'start')
    lab(2.20, BTN_Y + 1.15, f'CUT OUT — 3 BUTTONS ⌀{BTN_D:.4f}', .15, '#111', 'start')
    lab(2.20, PH - .42, 'CUT LAST — OUTSIDE PROFILE', .15, '#111', 'start')
    lab(2.4, .58, 'P1 FACE PLATE — 1:1 STENCIL', .17, '#111', 'start')
    lab(EDGE + 1.35, EDGE + .48, 'small circles = mount holes, MARK ONLY', .12, '#6C7A80', 'start')
    o.append('</svg>')
    return ''.join(o)

def reg_marks(ci, ri):
    """Registration crosses and neighbour edges, in page inches."""
    o = []
    def cross(px, py, lab_):
        o.append(f'<path d="M{f(px-.19)} {f(py)}H{f(px+.19)}M{f(px)} {f(py-.19)}V{f(py+.19)}" '
                 f'stroke="#B03A1F" stroke-width=".018" fill="none"/>')
        o.append(f'<circle cx="{f(px)}" cy="{f(py)}" r=".085" stroke="#B03A1F" '
                 f'stroke-width=".012" fill="none"/>')
        if lab_:
            o.append(f'<text x="{f(px+.24)}" y="{f(py+.05)}" font-size=".105" fill="#B03A1F" '
                     f'font-family="monospace">{lab_}</text>')
    L, T, R, B = WIN_L, WIN_T, WIN_L+ART_W, WIN_T+ART_H
    # overlap bands with the neighbouring sheets
    if ri < ROWS-1:
        yb = T + (sy[ri+1] - sy[ri])
        o.append(f'<path d="M{f(L)} {f(yb)}H{f(R)}" stroke="#B03A1F" stroke-width=".016" '
                 f'stroke-dasharray=".14 .09" fill="none"/>')
        o.append(f'<rect x="{f(L)}" y="{f(yb)}" width="{f(ART_W)}" height="{f(B-yb)}" '
                 f'fill="#B03A1F" opacity=".05"/>')
        o.append(f'<text x="{f(L+.06)}" y="{f(yb+.20)}" font-size=".115" fill="#B03A1F" '
                 f'font-family="monospace">OVERLAP — TOP EDGE OF THE SHEET BELOW LANDS HERE</text>')
        cross(L+1.1, yb, ''); cross(R-1.1, yb, '')
    if ci < COLS-1:
        xb = L + (sx[ci+1] - sx[ci])
        o.append(f'<path d="M{f(xb)} {f(T)}V{f(B)}" stroke="#B03A1F" stroke-width=".016" '
                 f'stroke-dasharray=".14 .09" fill="none"/>')
        o.append(f'<rect x="{f(xb)}" y="{f(T)}" width="{f(R-xb)}" height="{f(ART_H)}" '
                 f'fill="#B03A1F" opacity=".05"/>')
        o.append(f'<text x="{f(xb+.16)}" y="{f(T+.22)}" font-size=".115" fill="#B03A1F" '
                 f'font-family="monospace" transform="rotate(90 {f(xb+.16)} {f(T+.22)})">'
                 f'OVERLAP — LEFT EDGE OF THE NEXT SHEET LANDS HERE</text>')
        cross(xb, T+1.1, ''); cross(xb, B-1.1, '')
    for px, py in ((L, T), (R, T), (L, B), (R, B)):
        o.append(f'<path d="M{f(px-.22)} {f(py)}H{f(px+.22)}M{f(px)} {f(py-.22)}V{f(py+.22)}" '
                 f'stroke="#111" stroke-width=".014" fill="none"/>')
    return ''.join(o)

def header(n, total, ci, ri):
    o = [f'<svg class="hdr" width="{PAGE_W}in" height="{PAGE_H}in" '
         f'viewBox="0 0 {PAGE_W} {PAGE_H}" xmlns="http://www.w3.org/2000/svg">']
    o.append(f'<text x=".30" y=".32" font-size=".155" font-weight="700" '
             f'font-family="monospace">P1 FACE PLATE STENCIL — SHEET {n} OF {total}</text>')
    o.append(f'<text x=".30" y=".54" font-size=".112" fill="#555" font-family="monospace">'
             f'COLUMN {ci+1} OF {COLS} · ROW {ri+1} OF {ROWS} · 1:1 · '
             f'PRINT AT 100%, MARGINS NONE</text>')
    # 4 inch calibration bar
    bx, by, bl = .30, .76, 4.0
    o.append(f'<path d="M{bx} {by}h{bl}" stroke="#B03A1F" stroke-width=".020" fill="none"/>')
    for xx in (bx, bx+bl/2, bx+bl):
        o.append(f'<path d="M{f(xx)} {by-.07}v.14" stroke="#B03A1F" stroke-width=".016"/>')
    o.append(f'<text x="{bx+bl+.12}" y="{by+.045}" font-size=".105" fill="#B03A1F" '
             f'font-weight="700" font-family="monospace">'
             f'= 4.000 IN — IF NOT, THE PRINTER SCALED IT</text>')
    # tile map, sized by height so it always clears the artwork
    mh = .58
    mw = mh*PW/PH
    mx, my = PAGE_W - mw - .30, .12
    cw, ch = mw/COLS, mh/ROWS
    for j2 in range(ROWS):
        for i2 in range(COLS):
            on = (i2 == ci and j2 == ri)
            o.append(f'<rect x="{f(mx+i2*cw)}" y="{f(my+j2*ch)}" width="{f(cw)}" '
                     f'height="{f(ch)}" stroke="#111" stroke-width=".008" '
                     f'fill="{"#111" if on else "#FFF"}"/>')
    o.append(f'<text x="{f(mx+mw/2)}" y="{f(my+mh+.13)}" font-size=".085" fill="#555" '
             f'font-family="monospace" text-anchor="middle">TILE MAP</text>')
    o.append(reg_marks(ci, ri))
    o.append('</svg>')
    return ''.join(o)

pages = []
n = 0
for ri in range(ROWS):
    for ci in range(COLS):
        n += 1
        pages.append(f'<div class="page">{header(n, COLS*ROWS, ci, ri)}'
                     f'<div class="win">{tile_svg(sx[ci], sy[ri])}</div></div>')

HTML = f'''<!doctype html><meta charset="utf-8">
<title>P1 Face Plate — 1:1 Stencil</title>
<style>
  @page {{ size: {PAGE_W}in {PAGE_H}in; margin: 0; }}
  html,body {{ margin:0; padding:0; background:#8A9095; }}
  .page {{ position:relative; width:{PAGE_W}in; height:{PAGE_H}in; background:#fff;
           margin:0 auto 0.25in; overflow:hidden;
           page-break-after:always; break-after:page; }}
  .page:last-child {{ page-break-after:auto; break-after:auto; }}
  .hdr {{ position:absolute; inset:0; }}
  .win {{ position:absolute; left:{WIN_L}in; top:{WIN_T}in;
          width:{ART_W}in; height:{ART_H}in; overflow:hidden; }}
  .art {{ display:block; }}
  .instr {{ background:#fff; max-width:{PAGE_W}in; margin:0 auto .25in; padding:.45in .5in;
            font:12pt/1.5 -apple-system,system-ui,sans-serif; page-break-after:always; }}
  .instr ol, .instr ul {{ margin:.05in 0; padding-left:.26in; }}
  .instr h1 {{ font-size:19pt; margin:0 0 .12in; }}
  .instr h2 {{ font-size:11pt; margin:.26in 0 .07in; text-transform:uppercase;
               letter-spacing:.09em; color:#555; }}
  .instr li {{ margin-bottom:.09in; }}
  .instr code {{ font-family:ui-monospace,monospace; background:#EEF1F2; padding:1px 4px; }}
  .warn {{ border-left:3px solid #B03A1F; padding:.10in .18in; margin:.18in 0; background:#FBF4F2; }}
  @media print {{
    html,body {{ background:#fff; }}
    .page {{ margin:0; }}
    .instr {{ margin:0; padding:.34in .42in; font-size:10.2pt; line-height:1.38;
              height:{PAGE_H}in; box-sizing:border-box; overflow:hidden; }}
    .instr h1 {{ font-size:16pt; }}
    .instr h2 {{ margin:.17in 0 .05in; font-size:9.5pt; }}
    .instr li {{ margin-bottom:.05in; }}
    .warn {{ margin:.12in 0; padding:.08in .14in; }}
  }}
</style>
<div class="instr">
<h1>P1 Face Plate — 1:1 cardboard stencil</h1>
<p><b>{COLS} columns &times; {ROWS} rows = {COLS*ROWS} sheets</b>, plus this page.
Finished size <b>15.370 &times; 28.690 inches</b>.</p>
<h2>1 · Print</h2>
<ol>
<li>Print this file on US Letter. In the print dialog set <b>Scale: 100%</b>
    (not &ldquo;Fit to page&rdquo;) and <b>Margins: None</b>.</li>
<li><b>Check the red bar on sheet 1 with a ruler. It must measure exactly 4.000 inches.</b>
    If it doesn&rsquo;t, the printer scaled the page — fix the setting and print again.
    Everything downstream depends on this.</li>
</ol>
<h2>2 · Assemble</h2>
<ol>
<li>Lay the sheets out using the <b>tile map</b> in each header — the filled square shows
    where that sheet goes.</li>
<li>Each sheet has a <b>shaded overlap band</b> with a dashed red line and two red
    registration crosses. Slide the next sheet until its crosses sit exactly on top of the
    ones underneath, then tape.</li>
<li>The <b>1&nbsp;inch grid</b> is the real check. Grid lines must run straight across
    every joint, and the printed coordinates (<code>x,y</code> from the top-left corner of
    the plate) must agree on both sides of the tape.</li>
<li>Tape on the <b>front</b> so the tape doesn&rsquo;t lift when you cut.</li>
</ol>
<h2>3 · Cut</h2>
<ul>
<li><b>Heavy dashed</b> = cut out and discard: the screen window and the three buttons.</li>
<li><b>Small circles with crosses</b> = mounting holes. <b>Mark only</b> — don&rsquo;t cut them.</li>
<li><b>Heavy solid</b> = the outside profile. <b>Cut this last</b>, so the sheet stays
    stable while you do the interior.</li>
</ul>
<h2>4 · Transfer</h2>
<ol>
<li>Tape the assembled stencil to cardboard. Corrugated works; foam board is better if
    you want it to stand up.</li>
<li>Trace the outside profile and both voids, then cut the cardboard.</li>
<li>Hold it up against the 3280 with the <b>bottom edge 34.750&nbsp;inches above the
    floor</b>. That puts the button centres at 38.000&nbsp;AFF, which is where the ADA
    reach range put them.</li>
</ol>
<div class="warn">
<b>What this is for.</b> Proportion is the argument this whole design turns on — whether
the kiosk reads as an added interpretation device or as a monitor wearing a cabinet. A
photograph of cardboard taped to the real machine settles that in a way no drawing can.
Take one from six feet away, straight on, and from about 45&deg; to the side.
</div>
<p style="color:#666;font-size:10pt">
Generated by <code>make-stencil.py</code> from the same geometry as
<code>P1-face-plate.dxf</code>. Grid coordinates are inches from the top-left corner of the
plate. Overlap {OVL_Y:.3f}&Prime; vertical, {OVL_X:.3f}&Prime; horizontal.</p>
</div>
{''.join(pages)}
'''
open('stencil-letter.html', 'w').write(HTML)
print(f'stencil-letter.html — {COLS} x {ROWS} = {COLS*ROWS} sheets')
print(f'  artwork window   {ART_W} x {ART_H} in at ({WIN_L}, {WIN_T})')
print(f'  column starts    {[round(v,3) for v in sx]}')
print(f'  row starts       {[round(v,3) for v in sy]}')
print(f'  overlap          {OVL_X:.3f} horizontal, {OVL_Y:.3f} vertical')
print(f'  coverage         {sx[-1]+ART_W:.3f} x {sy[-1]+ART_H:.3f}  (plate {PW} x {PH})')
assert sx[-1]+ART_W >= PW-1e-9 and sy[-1]+ART_H >= PH-1e-9, 'TILES DO NOT COVER THE PLATE'
assert WIN_L+ART_W <= PAGE_W and WIN_T+ART_H <= PAGE_H, 'ARTWORK WINDOW OFF THE PAGE'
assert min(OVL_X, OVL_Y) >= MIN_OVL - 1e-9, f'OVERLAP TOO SMALL: {min(OVL_X,OVL_Y):.3f}'
print('  checks           coverage OK, window fits the page OK')
