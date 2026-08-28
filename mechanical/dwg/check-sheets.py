#!/usr/bin/env python3
"""
QA the generated sheets: nothing may fall outside the printable area.

Catches the failure mode that bites when a view scale changes — a dimension
ladder or a label quietly walking off the paper. Text is measured by estimated
extent, not just its anchor, because an 'end'-anchored note is the usual
offender.

    python3 check-sheets.py
"""
import re, glob, sys

FR = (0.15, 0.15, 16.85, 10.85)      # printable area; border furniture sits in the margin
bad = 0
for path in sorted(glob.glob('[0-9]*.svg')):
    t = open(path).read()
    pts = []
    for m in re.finditer(r'<rect x="([-\d.]+)" y="([-\d.]+)" width="([\d.]+)" height="([\d.]+)"', t):
        x, y, w, h = map(float, m.groups())
        if w > 16.9: continue                       # full-bleed background
        pts += [(x, y), (x+w, y+h)]
    for m in re.finditer(r'<circle cx="([-\d.]+)" cy="([-\d.]+)" r="([\d.]+)"', t):
        cx, cy, r = map(float, m.groups()); pts += [(cx-r, cy-r), (cx+r, cy+r)]
    for m in re.finditer(r'<path d="M([-\d.]+) ([-\d.]+)L([-\d.]+) ([-\d.]+)"', t):
        a, b, c, d = map(float, m.groups()); pts += [(a, b), (c, d)]
    for m in re.finditer(r'<text x="([-\d.]+)" y="([-\d.]+)"[^>]*font-size="([\d.]+)"'
                         r'[^>]*text-anchor="(\w+)"[^>]*>([^<]*)</text>', t):
        x, y, fs, an, body = (float(m.group(1)), float(m.group(2)), float(m.group(3)),
                              m.group(4), m.group(5))
        if 'rotate' in m.group(0):
            pts.append((x, y)); continue
        w = len(body) * fs * 0.62                   # monospace advance estimate
        x0 = x if an == 'start' else (x - w if an == 'end' else x - w/2)
        pts += [(x0, y - fs), (x0 + w, y)]
    E = 0.005
    out = [p for p in pts if not (FR[0]-E <= p[0] <= FR[2]+E and FR[1]-E <= p[1] <= FR[3]+E)]
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    if out: bad += 1
    print(f"{'OK  ' if not out else 'OVER'} {path}  X {min(xs):6.2f}–{max(xs):6.2f}  "
          f"Y {min(ys):6.2f}–{max(ys):6.2f}  outside: {len(out)}")
    for p in sorted(set((round(a, 2), round(b, 2)) for a, b in out))[:6]:
        print(f"        {p}")
print('\nALL SHEETS INSIDE THE FRAME' if not bad else f'\n{bad} SHEET(S) NEED ATTENTION')
sys.exit(1 if bad else 0)
