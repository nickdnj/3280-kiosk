#!/usr/bin/env python3
"""Concept comparison: the display-approach options, drawn to real geometry.
Emits 06-option-comparison.svg. See ../display-approach-options.md."""
import pathlib

S = 7.0                       # px per inch
FLOOR = 617.0
CAB_W, CAB_H = 23.0, 69.5
OPEN_W = 19.0
COLS = [133, 404, 675, 946]   # cabinet left edges
W, H = 1240, 1010

TAN, TAN2, INK = '#E5DDCB', '#EFE9DC', '#2b2b2b'
DARK, SCREEN, DIMC = '#1c1c1c', '#E9E2D0', '#B3401A'
GOOD, WARN = '#2F5D3A', '#8a5f10'

def yy(h): return FLOOR - S * h
o = []
def add(t): o.append(t)
def txt(x, y, s, size=11, fill='#333', anchor='start', weight='400'):
    add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" '
        f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')

add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
    f'font-family="Helvetica,Arial,sans-serif"><rect width="{W}" height="{H}" fill="#ffffff"/>')
txt(40, 42, 'Display Approach — Concept Comparison', 22, '#1b1b1b', weight='700')
txt(40, 64, 'Four ways to put the screen on the 3280. Drawn to the assumed cabinet geometry, '
            'not AI concept art — proportions are real.', 12.5, '#555')
add(f'<rect x="40" y="78" width="470" height="21" fill="#FBE7E1" stroke="{DIMC}"/>')
txt(50, 93, 'ALL FOUR STILL GATED ON C1 — the measured closing clearance (ME-1 §C)',
    11.5, DIMC, weight='700')

def cabinet(x0):
    """Cabinet shell with the card cage showing; returns opening bounds."""
    add(f'<rect x="{x0}" y="{yy(CAB_H):.1f}" width="{CAB_W*S:.1f}" height="{CAB_H*S:.1f}" '
        f'fill="{TAN}" stroke="{INK}" stroke-width="1.2"/>')
    add(f'<rect x="{x0-4}" y="{yy(CAB_H):.1f}" width="{CAB_W*S+8:.1f}" height="{4.5*S:.1f}" '
        f'fill="{TAN2}" stroke="{INK}" stroke-width="1.2"/>')
    ox = x0 + (CAB_W - OPEN_W) / 2 * S
    add(f'<rect x="{ox:.1f}" y="{yy(65):.1f}" width="{OPEN_W*S:.1f}" '
        f'height="{57*S:.1f}" fill="{DARK}"/>')
    # card cage
    n = 20
    for i in range(n):
        bx = ox + 6 + i * (OPEN_W * S - 12) / (n - 1)
        add(f'<line x1="{bx:.1f}" y1="{yy(24):.1f}" x2="{bx:.1f}" y2="{yy(11):.1f}" '
            f'stroke="#4a5566" stroke-width="1.6"/>')
    add(f'<line x1="{ox+4:.1f}" y1="{yy(10.5):.1f}" x2="{ox+OPEN_W*S-4:.1f}" '
        f'y2="{yy(10.5):.1f}" stroke="#7a8494" stroke-width="2"/>')
    add(f'<rect x="{x0}" y="{yy(8):.1f}" width="{CAB_W*S:.1f}" height="{6*S:.1f}" '
        f'fill="{TAN}" stroke="{INK}" stroke-width="1.2"/>')
    for fx in (x0 + 8, x0 + CAB_W * S - 26):
        add(f'<rect x="{fx:.1f}" y="{yy(2):.1f}" width="18" height="{2*S:.1f}" fill="#2b2b2b"/>')
    return ox, ox + OPEN_W * S

def buttons(cx, cy, w):
    add(f'<rect x="{cx-w/2:.1f}" y="{cy:.1f}" width="{w:.1f}" height="{4*S:.1f}" fill="#1b1b1b"/>')
    for k in (-1, 0, 1):
        add(f'<circle cx="{cx + k*w*0.26:.1f}" cy="{cy + 2*S:.1f}" r="{0.62*S:.1f}" '
            f'fill="#3d3d3d" stroke="#8d8d8d" stroke-width="0.7"/>')

def hinge(x, ytop, ybot):
    for hy in (ytop + 14, ybot - 22):
        add(f'<rect x="{x-5:.1f}" y="{hy:.1f}" width="5" height="14" fill="#9a9a9a" stroke="#444" stroke-width="0.7"/>')

# ---------------------------------------------------------------- A
ox, _ = cabinet(COLS[0])
cx = COLS[0] + CAB_W * S / 2
dw, dh, dy0 = 14.5 * S, 30 * S, yy(56)
add(f'<rect x="{cx-dw/2:.1f}" y="{dy0:.1f}" width="{dw:.1f}" height="{dh:.1f}" '
    f'fill="{TAN}" stroke="{INK}" stroke-width="1.2"/>')
add(f'<rect x="{cx-dw/2+4:.1f}" y="{dy0+3:.1f}" width="34" height="8" fill="#1b1b1b"/>')
bw, bh = 12.8 * S, 21.9 * S
by = dy0 + 2 * S
add(f'<rect x="{cx-bw/2:.1f}" y="{by:.1f}" width="{bw:.1f}" height="{bh:.1f}" fill="#141414"/>')
add(f'<rect x="{cx-11.77*S/2:.1f}" y="{by+0.49*S:.1f}" width="{11.77*S:.1f}" '
    f'height="{20.92*S:.1f}" fill="{SCREEN}"/>')
buttons(cx, dy0 + 24.5 * S, bw)
hinge(cx - dw / 2, dy0, dy0 + dh)

# ---------------------------------------------------------------- B
ox, _ = cabinet(COLS[1])
cx = COLS[1] + CAB_W * S / 2
dw, dh, dy0 = 14.3 * S, 28 * S, yy(55)
add(f'<rect x="{cx-dw/2:.1f}" y="{dy0:.1f}" width="{dw:.1f}" height="{dh:.1f}" '
    f'fill="{TAN}" stroke="{INK}" stroke-width="1.2"/>')
add(f'<rect x="{cx-dw/2+4:.1f}" y="{dy0+3:.1f}" width="34" height="8" fill="#1b1b1b"/>')
by = dy0 + 1.6 * S
add(f'<rect x="{cx-bw/2:.1f}" y="{by:.1f}" width="{bw:.1f}" height="{bh:.1f}" fill="#141414"/>')
add(f'<rect x="{cx-11.77*S/2:.1f}" y="{by+0.49*S:.1f}" width="{11.77*S:.1f}" '
    f'height="{20.92*S:.1f}" fill="{SCREEN}"/>')
buttons(cx, dy0 + 23 * S, bw)
hinge(cx - dw / 2, dy0, dy0 + dh)

# ---------------------------------------------------------------- C recessed
ox, _ = cabinet(COLS[2])
cx = COLS[2] + CAB_W * S / 2
dw, dh, dy0 = 15.0 * S, 29 * S, yy(55.5)
add(f'<rect x="{cx-dw/2:.1f}" y="{dy0:.1f}" width="{dw:.1f}" height="{dh:.1f}" '
    f'fill="{TAN}" stroke="{INK}" stroke-width="1.2"/>')
add(f'<rect x="{cx-dw/2+4:.1f}" y="{dy0+3:.1f}" width="34" height="8" fill="#1b1b1b"/>')
mw, mh = 12.4 * S, 21.5 * S
my = dy0 + 1.6 * S
add(f'<rect x="{cx-mw/2:.1f}" y="{my:.1f}" width="{mw:.1f}" height="{mh:.1f}" '
    f'fill="#0d0d0d" stroke="#000" stroke-width="0.8"/>')
add(f'<rect x="{cx-11.77*S/2:.1f}" y="{my+0.55*S:.1f}" width="{11.77*S:.1f}" '
    f'height="{20.92*S:.1f}" fill="{SCREEN}"/>')
buttons(cx, dy0 + 23.6 * S, 12.4 * S)
hinge(cx - dw / 2, dy0, dy0 + dh)
txt(cx, dy0 + dh + 13, 'monitor recessed behind the cut', 8.5, GOOD, 'middle')

# ---------------------------------------------------------------- C proud
ox, _ = cabinet(COLS[3])
cx = COLS[3] + CAB_W * S / 2
dw, dh, dy0 = 15.0 * S, 29 * S, yy(55.5)
add(f'<rect x="{cx-dw/2:.1f}" y="{dy0:.1f}" width="{dw:.1f}" height="{dh:.1f}" '
    f'fill="{TAN}" stroke="{INK}" stroke-width="1.2"/>')
add(f'<rect x="{cx-mw/2+5:.1f}" y="{my+5:.1f}" width="{mw:.1f}" height="{mh+0.9*S:.1f}" '
    f'fill="#000" opacity="0.22"/>')
add(f'<rect x="{cx-mw/2:.1f}" y="{my:.1f}" width="{mw:.1f}" height="{mh+0.9*S:.1f}" '
    f'fill="#141414" stroke="#000" stroke-width="1"/>')
add(f'<rect x="{cx-11.77*S/2:.1f}" y="{my+0.5*S:.1f}" width="{11.77*S:.1f}" '
    f'height="{20.92*S:.1f}" fill="{SCREEN}"/>')
add(f'<rect x="{cx-9:.1f}" y="{my+mh+0.28*S:.1f}" width="18" height="3.5" rx="1.8" fill="#555"/>')
buttons(cx, dy0 + 24.8 * S, 12.4 * S)
hinge(cx - dw / 2, dy0, dy0 + dh)
txt(cx, dy0 + dh + 13, 'monitor stands proud of the panel', 8.5, WARN, 'middle')

add(f'<line x1="60" y1="{FLOOR}" x2="{W-40}" y2="{FLOOR}" stroke="#333" stroke-width="1.6"/>')

# ---------------------------------------------------------------- depth strips
DS = 26.0
txt(40, 660, 'DEPTH BEHIND THE CABINET FACE', 11, '#1b1b1b', weight='700')
for i, (d, lab, col) in enumerate([(2.5, '2.5"', GOOD), (3.85, '3.85"', WARN),
                                   (2.2, '2.2"', GOOD), (2.2, '2.2" + proud', GOOD)]):
    x = COLS[i]
    add(f'<line x1="{x}" y1="668" x2="{x}" y2="700" stroke="{INK}" stroke-width="1.6"/>')
    add(f'<rect x="{x}" y="674" width="{d*DS:.1f}" height="20" fill="{col}" opacity="0.30" stroke="{col}"/>')
    txt(x + d * DS + 8, 689, lab, 10.5, col, weight='700')
    txt(x - 2, 712, 'cabinet face', 8.5, '#888')

# ---------------------------------------------------------------- captions
CAPS = [
 ('A', 'CUSTOM DOOR', TAN,
  ['De-cased LCD in a fabricated tan door.',
   'The approved concept, built as drawn.'],
  [('Fab parts', '4', WARN), ('De-casing', 'required — one-way', WARN),
   ('Hardest cut', 'window, ±0.03"', WARN), ('Docent-replaceable', 'no', '#b03030'),
   ('Looks built-in', 'best', GOOD)]),
 ('B', 'BOUGHT CAN + FACE', TAN,
  ['Leviton structured-media can, our tan',
   'face plate over it. Same front as A.'],
  [('Fab parts', '1 flat plate', GOOD), ('De-casing', 'required — one-way', WARN),
   ('Hardest cut', 'window, ±0.03"', WARN), ('Docent-replaceable', 'no', '#b03030'),
   ('Looks built-in', 'good', GOOD)]),
 ('C1', 'MONITOR RECESSED', TAN,
  ['Cased monitor behind a bezel-sized cut',
   'in a hinged tan carrier panel.'],
  [('Fab parts', '1 flat plate', GOOD), ('De-casing', 'none', GOOD),
   ('Hardest cut', 'window, ±0.1" — forgiving', GOOD),
   ('Docent-replaceable', 'YES', GOOD), ('Looks built-in', 'near-identical to A', GOOD)]),
 ('C2', 'MONITOR PROUD', TAN,
  ['Monitor VESA-bolted to the front of the',
   'carrier panel. No window at all.'],
  [('Fab parts', '1 — round holes only', GOOD), ('De-casing', 'none', GOOD),
   ('Hardest cut', 'none — drill press', GOOD),
   ('Docent-replaceable', 'YES', GOOD), ('Looks built-in', 'reads as bolted-on', '#b03030')]),
]
for i, (k, name, _, desc, rows) in enumerate(CAPS):
    x = COLS[i]
    add(f'<rect x="{x}" y="736" width="248" height="24" fill="#2F5D3A"/>')
    txt(x + 9, 753, f'{k} &#183; {name}', 12, '#fff', weight='700')
    yv = 776
    for d in desc:
        txt(x, yv, d, 10.5, '#333'); yv += 14
    yv += 6
    for lab, val, col in rows:
        txt(x, yv, lab, 9.5, '#888')
        txt(x + 248, yv, val, 10, col, 'end', weight='600')
        add(f'<line x1="{x}" y1="{yv+4}" x2="{x+248}" y2="{yv+4}" stroke="#e2e2e2" stroke-width="0.7"/>')
        yv += 18

txt(40, 985, 'Every option keeps the left hinge — swinging the display open to reveal the card cage is the premise of the exhibit (MR5). '
             'VESA-mounting straight to the cabinet is not an option.', 11.5, DIMC, weight='600')
add('</svg>')
pathlib.Path('06-option-comparison.svg').write_text('\n'.join(o))
print('06-option-comparison.svg written')
