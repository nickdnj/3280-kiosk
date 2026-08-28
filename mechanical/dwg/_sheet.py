"""
Drawing-sheet framework — B-size (17 x 11) landscape, ANSI-style title block.

Everything is authored in PAPER INCHES. Model geometry is placed through
View(), which carries a drawing scale. That keeps line weights and lettering
constant across sheets no matter what each view is scaled to.
"""
import math, re

SW, SH = 17.0, 11.0          # sheet, inches
MARGIN = 0.35
TB_W, TB_H = 6.60, 1.85      # title block

# line weights, inches — ASME Y14.2 thick/thin convention
W_VIS, W_HID, W_DIM, W_CEN, W_PHAN, W_XTHIN = .020, .010, .008, .008, .008, .005
# lettering heights, inches
T_DIM, T_NOTE, T_LBL, T_HEAD, T_TITLE = .105, .105, .125, .155, .240

INK   = '#111111'
THIN  = '#444444'
ACC   = '#0E5A6B'
FLAG  = '#93331F'
GREY  = '#8A9095'

_AMP = re.compile(r'&(?!(?:#\d+|#x[0-9A-Fa-f]+|amp|lt|gt|quot|apos);)')
def esc(s):
    return _AMP.sub('&amp;', str(s)).replace('<', '&lt;').replace('>', '&gt;')

def f(v, p=4):
    return f"{v:.{p}f}".rstrip('0').rstrip('.') or '0'

class Sheet:
    def __init__(self, number, title, scale, material, finish, sheet_no, sheet_of,
                 rev='A', date='2026-08-28'):
        self.meta = dict(number=number, title=title, scale=scale, material=material,
                         finish=finish, n=sheet_no, of=sheet_of, rev=rev, date=date)
        self.o = []

    # ── primitives, paper inches, Y DOWN ─────────────────────────────────────
    def line(self, x1, y1, x2, y2, w=W_VIS, c=INK, dash=None, cap='butt'):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.o.append(f'<path d="M{f(x1)} {f(y1)}L{f(x2)} {f(y2)}" stroke="{c}" '
                      f'stroke-width="{w}" fill="none" stroke-linecap="{cap}"{d}/>')
    def poly(self, pts, w=W_VIS, c=INK, fill='none', dash=None, close=True):
        d = 'M' + 'L'.join(f'{f(x)} {f(y)}' for x, y in pts) + ('Z' if close else '')
        da = f' stroke-dasharray="{dash}"' if dash else ''
        self.o.append(f'<path d="{d}" stroke="{c}" stroke-width="{w}" fill="{fill}"{da}/>')
    def rect(self, x, y, w, h, lw=W_VIS, c=INK, fill='none', dash=None, r=0):
        da = f' stroke-dasharray="{dash}"' if dash else ''
        self.o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" rx="{f(r)}" '
                      f'stroke="{c}" stroke-width="{lw}" fill="{fill}"{da}/>')
    def circ(self, cx, cy, r, lw=W_VIS, c=INK, fill='none', dash=None):
        da = f' stroke-dasharray="{dash}"' if dash else ''
        self.o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" stroke="{c}" '
                      f'stroke-width="{lw}" fill="{fill}"{da}/>')
    def text(self, x, y, s, h=T_NOTE, c=INK, anchor='start', bold=False, mid=False,
             rot=None, mono=True, ls=0):
        fam = ('"Space Mono",ui-monospace,monospace' if mono
               else '"Archivo",Helvetica,Arial,sans-serif')
        tr = f' transform="rotate({rot} {f(x)} {f(y)})"' if rot is not None else ''
        db = ' dominant-baseline="central"' if mid else ''
        lsp = f' letter-spacing="{f(ls)}"' if ls else ''
        self.o.append(f'<text x="{f(x)}" y="{f(y)}" font-family={chr(39)}{fam}{chr(39)} '
                      f'font-size="{h}" fill="{c}" text-anchor="{anchor}"'
                      f'{" font-weight=\'700\'" if bold else ""}{db}{tr}{lsp}>{esc(s)}</text>')

    # ── dimensions ───────────────────────────────────────────────────────────
    def dim_h(self, y, x1, x2, label, above=True, ext_from=None, c=ACC):
        l, r_ = min(x1, x2), max(x1, x2)
        a = .055
        self.line(l, y, r_, y, W_DIM, c)
        for x in (l, r_):
            self.line(x, y-a, x, y+a, W_DIM, c)
            if ext_from is not None:
                self.line(x, ext_from, x, y + (a if y > ext_from else -a), W_XTHIN, c)
        self.text((l+r_)/2, y - .06 if above else y + .16, label, T_DIM, c, 'middle')
    def dim_v(self, x, y1, y2, label, left=True, ext_from=None, c=ACC):
        t, b = min(y1, y2), max(y1, y2)
        a = .055
        self.line(x, t, x, b, W_DIM, c)
        for y in (t, b):
            self.line(x-a, y, x+a, y, W_DIM, c)
            if ext_from is not None:
                self.line(ext_from, y, x + (a if x > ext_from else -a), y, W_XTHIN, c)
        ox = x - .07 if left else x + .07
        self.text(ox, (t+b)/2, label, T_DIM, c, 'middle', mid=True, rot=-90)
    def leader(self, x1, y1, x2, y2, label, anchor='start', c=INK, h=T_NOTE):
        self.line(x1, y1, x2, y2, W_DIM, c)
        self.circ(x1, y1, .022, W_DIM, c, c)
        self.text(x2 + (.07 if anchor == 'start' else -.07), y2, label, h, c, anchor, mid=True)
    def balloon(self, x, y, n, tx, ty):
        self.line(x, y, tx, ty, W_DIM, INK)
        self.circ(x, y, .022, W_DIM, INK, INK)
        self.circ(tx, ty, .145, W_DIM, INK, '#FFFFFF')
        self.text(tx, ty, str(n), T_DIM, INK, 'middle', bold=True, mid=True)
    def centre(self, cx, cy, r):
        e = r + .09
        self.line(cx-e, cy, cx+e, cy, W_CEN, GREY, dash='.10 .05 .02 .05')
        self.line(cx, cy-e, cx, cy+e, W_CEN, GREY, dash='.10 .05 .02 .05')
    def hatch(self, x, y, w, h, pitch=.07, c=GREY, ang=45):
        cid = f'h{len(self.o)}'
        self.o.append(f'<clipPath id="{cid}"><rect x="{f(x)}" y="{f(y)}" '
                      f'width="{f(w)}" height="{f(h)}"/></clipPath>')
        d = []
        n = int((w + h)/pitch) + 2
        for i in range(-n, n):
            d.append(f'M{f(x+i*pitch)} {f(y+h)}L{f(x+i*pitch+h)} {f(y)}')
        self.o.append(f'<path d="{"".join(d)}" stroke="{c}" stroke-width="{W_XTHIN}" '
                      f'fill="none" clip-path="url(#{cid})"/>')

    # ── frame + title block ──────────────────────────────────────────────────
    def frame(self):
        m = MARGIN
        self.rect(m, m, SW-2*m, SH-2*m, W_VIS, INK)
        self.rect(m+.09, m+.09, SW-2*m-.18, SH-2*m-.18, W_XTHIN, THIN)
        cols, rows = 8, 5
        for i in range(1, cols):
            x = m + i*(SW-2*m)/cols
            for yy in (m, SH-m-.09):
                self.line(x, yy, x, yy+.09, W_XTHIN, THIN)
        for i in range(cols):
            x = m + (i+.5)*(SW-2*m)/cols
            self.text(x, m+.075, str(cols-i), .085, THIN, 'middle', mid=True)
            self.text(x, SH-m-.045, str(cols-i), .085, THIN, 'middle', mid=True)
        for i in range(rows):
            y = m + (i+.5)*(SH-2*m)/rows
            ltr = 'EDCBA'[i]
            self.text(m+.045, y, ltr, .085, THIN, 'middle', mid=True)
            self.text(SW-m-.045, y, ltr, .085, THIN, 'middle', mid=True)

    def title_block(self):
        M = self.meta
        x0, y0 = SW-MARGIN-TB_W, SH-MARGIN-TB_H
        self.rect(x0, y0, TB_W, TB_H, W_VIS, INK, '#FFFFFF')
        rows = [.42, .78, 1.14, 1.50]
        for r in rows:
            self.line(x0, y0+r, x0+TB_W, y0+r, W_HID, INK)
        for x in (2.55, 4.30):
            self.line(x0+x, y0+.42, x0+x, y0+TB_H, W_HID, INK)
        def cell(cx, cy, k, v, vh=T_LBL, bold=True):
            self.text(x0+cx+.07, y0+cy+.145, k, .075, THIN, ls=.012)
            self.text(x0+cx+.07, y0+cy+.325, v, vh, INK, bold=bold)
        self.text(x0+.09, y0+.185, '3280 KIOSK  ·  REV 1 STANDALONE', .095, ACC, bold=True, ls=.02)
        self.text(x0+TB_W-.09, y0+.185, 'VINTAGE COMPUTER FEDERATION  ·  INFOAGE', .085,
                  THIN, 'end')
        self.text(x0+.09, y0+.62, M['title'].upper(), T_HEAD, INK, bold=True)
        self.text(x0+.09, y0+.79+.30, 'CONCEPT — NOT RELEASED FOR PRODUCTION', .085, FLAG, bold=True)
        cell(2.55, .42, 'DWG NO', M['number'], T_LBL)
        cell(4.30, .42, 'REV', M['rev'], T_LBL)
        cell(2.55, .78, 'SCALE', M['scale'], T_DIM)
        cell(4.30, .78, 'SHEET', f"{M['n']} OF {M['of']}", T_DIM)
        cell(2.55, 1.14, 'MATERIAL', M['material'], .095)
        cell(4.30, 1.14, 'FINISH', M['finish'], .095)
        cell(0.00, 1.14, 'DRAWN', 'CLAUDE / N. DEMARCO', .095)
        cell(0.00, 1.50, 'DATE', M['date'], .095)
        cell(2.55, 1.50, 'UNITS', 'INCHES', .095)
        cell(4.30, 1.50, 'PROJECTION', 'THIRD ANGLE', .085)
        # third-angle symbol
        sx, sy = x0+TB_W-.55, y0+1.72
        self.circ(sx, sy, .085, W_HID, INK)
        self.circ(sx, sy, .038, W_HID, INK)
        self.poly([(sx-.34, sy-.085), (sx-.16, sy), (sx-.34, sy+.085)], W_HID, INK)

    def default_tol(self, x, y):
        self.rect(x, y, 2.55, .78, W_HID, INK, '#FFFFFF')
        self.text(x+.07, y+.17, 'UNLESS OTHERWISE SPECIFIED', .075, THIN, ls=.012)
        for i, s in enumerate(['DECIMAL  .XX  ± .03    .XXX  ± .010',
                               'CUT PARTS PER SUPPLIER TOLERANCE',
                               'BREAK SHARP EDGES  ·  DEBURR ALL HOLES']):
            self.text(x+.07, y+.34+i*.15, s, .085, INK)

    def save(self, path, px_per_inch=110):
        head = (f'<svg xmlns="http://www.w3.org/2000/svg" '
                f'width="{SW*px_per_inch:.0f}" height="{SH*px_per_inch:.0f}" '
                f'viewBox="0 0 {SW} {SH}">'
                f'<rect width="100%" height="100%" fill="#FFFFFF"/>')
        open(path, 'w').write(head + ''.join(self.o) + '</svg>')
        return path

class View:
    """Maps model inches to paper inches at a drawing scale."""
    def __init__(self, sheet, ox, oy, scale, flip_y=True):
        self.s, self.ox, self.oy, self.k, self.fy = sheet, ox, oy, scale, flip_y
    def x(self, mx): return self.ox + mx*self.k
    def y(self, my): return self.oy - my*self.k if self.fy else self.oy + my*self.k
    def d(self, md):  return md*self.k
