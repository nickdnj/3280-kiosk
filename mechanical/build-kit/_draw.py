"""Line-art primitives for the assembly manual. Page units are inches, y down."""
import math, re

_NUM = re.compile(r'-?\d+\.?\d*')

C30, S30 = math.cos(math.radians(30)), math.sin(math.radians(30))

# line weights
W_HEAVY, W_MED, W_LIGHT, W_HAIR = 0.030, 0.018, 0.011, 0.007
INK = '#111111'
GHOST = '#B8BCC0'


def iso(u, v, w):
    """u = width right, v = height up, w = depth forward from the back plane.
    The viewer sees the front, the right side and the top."""
    return ((u - w) * C30, (u + w) * S30 - v)


def hull(pts):
    pts = sorted(set((round(x, 6), round(y, 6)) for x, y in pts))
    def half(p):
        h = []
        for q in p:
            while len(h) > 1 and ((h[-1][0]-h[-2][0])*(q[1]-h[-2][1])
                                  - (h[-1][1]-h[-2][1])*(q[0]-h[-2][0])) <= 0:
                h.pop()
            h.append(q)
        return h
    return half(pts)[:-1] + half(pts[::-1])[:-1]


class Page:
    W, H = 8.5, 11.0

    LIVE = (0.35, 0.35, 8.15, 10.70)      # anything outside this will not print

    def __init__(self, number, total):
        self.o = []
        self.n, self.total = number, total
        self.bb = [99.0, 99.0, -99.0, -99.0]
        self.stray = []

    def _see(self, x, y, tag=''):
        self.bb = [min(self.bb[0], x), min(self.bb[1], y),
                   max(self.bb[2], x), max(self.bb[3], y)]
        l, t, r, b = self.LIVE
        if not (l <= x <= r and t <= y <= b):
            self.stray.append((round(x, 2), round(y, 2), tag))

    # ── raw ──────────────────────────────────────────────────────────────
    def raw(self, s):
        self.o.append(s)

    def line(self, x1, y1, x2, y2, w=W_MED, dash=None, col=INK):
        self._see(x1, y1, 'line'); self._see(x2, y2, 'line')
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.raw(f'<line x1="{x1:.4f}" y1="{y1:.4f}" x2="{x2:.4f}" y2="{y2:.4f}" '
                 f'stroke="{col}" stroke-width="{w}" stroke-linecap="round"{d}/>')

    def path(self, d, w=W_MED, fill='none', dash=None, col=INK):
        if not any(c in d for c in 'mlhvcsqtaz'):        # absolute-only paths
            n = [float(v) for v in _NUM.findall(d)]
            for i in range(0, len(n) - 1, 2):
                self._see(n[i], n[i+1], 'path')
        da = f' stroke-dasharray="{dash}"' if dash else ''
        self.raw(f'<path d="{d}" fill="{fill}" stroke="{col}" stroke-width="{w}" '
                 f'stroke-linejoin="round" stroke-linecap="round"{da}/>')

    def poly(self, pts, w=W_MED, fill='none', close=True, dash=None, col=INK):
        d = 'M ' + ' L '.join(f'{x:.4f} {y:.4f}' for x, y in pts) + (' Z' if close else '')
        self.path(d, w, fill, dash, col)

    def rect(self, x, y, ww, hh, w=W_MED, fill='none', r=0, dash=None, col=INK):
        self._see(x, y, 'rect'); self._see(x + ww, y + hh, 'rect')
        da = f' stroke-dasharray="{dash}"' if dash else ''
        self.raw(f'<rect x="{x:.4f}" y="{y:.4f}" width="{ww:.4f}" height="{hh:.4f}" '
                 f'rx="{r}" fill="{fill}" stroke="{col}" stroke-width="{w}"{da}/>')

    def circle(self, cx, cy, r, w=W_MED, fill='none', dash=None, col=INK):
        self._see(cx - r, cy - r, 'circle'); self._see(cx + r, cy + r, 'circle')
        da = f' stroke-dasharray="{dash}"' if dash else ''
        self.raw(f'<circle cx="{cx:.4f}" cy="{cy:.4f}" r="{r:.4f}" fill="{fill}" '
                 f'stroke="{col}" stroke-width="{w}"{da}/>')

    def text(self, x, y, s, size=0.16, anchor='middle', weight='bold', col=INK):
        w = len(str(s)) * size * 0.60
        x0 = x if anchor == 'start' else (x - w if anchor == 'end' else x - w/2)
        self._see(x0, y - size, f'text:{s}'); self._see(x0 + w, y, f'text:{s}')
        self.raw(f'<text x="{x:.4f}" y="{y:.4f}" font-family="Helvetica,Arial,sans-serif" '
                 f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" '
                 f'fill="{col}">{s}</text>')

    # ── composites ───────────────────────────────────────────────────────
    def arrow(self, x1, y1, x2, y2, w=W_MED, head=0.11):
        a = math.atan2(y2 - y1, x2 - x1)
        bx, by = x2 - head * math.cos(a), y2 - head * math.sin(a)
        self.line(x1, y1, bx, by, w)
        s = 0.42
        self.poly([(x2, y2),
                   (bx - head*s*math.sin(a), by + head*s*math.cos(a)),
                   (bx + head*s*math.sin(a), by - head*s*math.cos(a))],
                  w=W_HAIR, fill=INK)

    def curve_arrow(self, x1, y1, x2, y2, bow=0.5, w=W_MED):
        mx, my = (x1+x2)/2, (y1+y2)/2
        dx, dy = x2-x1, y2-y1
        cx, cy = mx - dy*bow*0.5, my + dx*bow*0.5
        self.path(f'M {x1:.4f} {y1:.4f} Q {cx:.4f} {cy:.4f} {x2:.4f} {y2:.4f}', w)
        a = math.atan2(y2-cy, x2-cx)
        h = 0.11
        bx, by = x2 - h*math.cos(a), y2 - h*math.sin(a)
        self.poly([(x2, y2), (bx - h*0.42*math.sin(a), by + h*0.42*math.cos(a)),
                   (bx + h*0.42*math.sin(a), by - h*0.42*math.cos(a))],
                  w=W_HAIR, fill=INK)

    def balloon(self, x, y, label, r=0.155, size=0.155):
        self.circle(x, y, r, w=W_MED, fill='#FFFFFF')
        self.text(x, y + size*0.36, label, size=size)

    def stepnum(self, x, y, n):
        self.circle(x, y, 0.30, w=W_HEAVY, fill='#FFFFFF')
        self.text(x, y + 0.135, str(n), size=0.38)

    def detail_bubble(self, cx, cy, r, fx, fy, fr):
        """Magnifier: circle at the feature, circle where the blow-up sits."""
        self.circle(fx, fy, fr, w=W_LIGHT, dash='0.05 0.04')
        a = math.atan2(cy - fy, cx - fx)
        self.line(fx + fr*math.cos(a), fy + fr*math.sin(a),
                  cx - r*math.cos(a), cy - r*math.sin(a), w=W_LIGHT, dash='0.05 0.04')
        self.circle(cx, cy, r, w=W_MED, fill='#FFFFFF')

    def person(self, x, y, s=1.0, arms='down', mirror=False):
        m = -1 if mirror else 1
        def p(dx, dy): return (x + m*dx*s, y + dy*s)
        self.circle(*p(0, 0), 0.115*s, w=W_HEAVY)
        self.line(*p(0, 0.115), *p(0, 0.62), w=W_HEAVY)
        if arms == 'down':
            self.line(*p(0, 0.24), *p(-0.24, 0.50), w=W_HEAVY)
            self.line(*p(0, 0.24), *p(0.24, 0.50), w=W_HEAVY)
        elif arms == 'up':
            self.line(*p(0, 0.24), *p(-0.26, 0.02), w=W_HEAVY)
            self.line(*p(0, 0.24), *p(0.26, 0.02), w=W_HEAVY)
        else:                                   # forward, carrying
            self.line(*p(0, 0.24), *p(-0.30, 0.24), w=W_HEAVY)
            self.line(*p(0, 0.24), *p(0.30, 0.24), w=W_HEAVY)
        self.line(*p(0, 0.62), *p(-0.20, 1.02), w=W_HEAVY)
        self.line(*p(0, 0.62), *p(0.20, 1.02), w=W_HEAVY)

    def cross_out(self, x, y, ww, hh):
        """The IKEA 'no': a rounded box with a diagonal slash."""
        self.rect(x, y, ww, hh, w=W_HEAVY, r=0.14)
        self.line(x + 0.10, y + hh - 0.10, x + ww - 0.10, y + 0.10, w=W_HEAVY)

    def tick_box(self, x, y, ww, hh):
        self.rect(x, y, ww, hh, w=W_HEAVY, r=0.14)

    def tick(self, x, y, s=0.30):
        self.path(f'M {x-s*0.45:.3f} {y:.3f} L {x-s*0.10:.3f} {y+s*0.36:.3f} '
                  f'L {x+s*0.50:.3f} {y-s*0.42:.3f}', w=W_HEAVY)

    def no(self, x, y, s=0.30):
        self.circle(x, y, s, w=W_HEAVY)
        self.line(x - s*0.71, y + s*0.71, x + s*0.71, y - s*0.71, w=W_HEAVY)

    # ── isometric solids ─────────────────────────────────────────────────
    def slab(self, u, v, w_, du, dv, dw, ox, oy, sc, lw=W_MED, fill='#FFFFFF'):
        pts = [iso(u + a*du, v + b*dv, w_ + c*dw)
               for a in (0, 1) for b in (0, 1) for c in (0, 1)]
        sp = [(ox + px*sc, oy + py*sc) for px, py in pts]
        self.poly(hull(sp), w=lw, fill=fill)
        near = (u+du, v+dv, w_+dw)
        for nb in ((u, v+dv, w_+dw), (u+du, v, w_+dw), (u+du, v+dv, w_)):
            a = iso(*near); b = iso(*nb)
            self.line(ox+a[0]*sc, oy+a[1]*sc, ox+b[0]*sc, oy+b[1]*sc, w=lw)
        return sp

    def iso_face(self, quad, ox, oy, sc, w=W_MED, fill='none', dash=None):
        self.poly([(ox + iso(*p)[0]*sc, oy + iso(*p)[1]*sc) for p in quad],
                  w=w, fill=fill, dash=dash)

    def iso_line(self, a, b, ox, oy, sc, w=W_MED, dash=None, col=INK):
        pa, pb = iso(*a), iso(*b)
        self.line(ox+pa[0]*sc, oy+pa[1]*sc, ox+pb[0]*sc, oy+pb[1]*sc, w=w, dash=dash, col=col)

    # ── output ───────────────────────────────────────────────────────────
    def save(self, path):
        self.text(self.W/2, self.H - 0.42, f'{self.n}', size=0.15, weight='normal')
        body = '\n'.join(self.o)
        open(path, 'w').write(
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.W}in" height="{self.H}in" '
            f'viewBox="0 0 {self.W} {self.H}">\n'
            f'<rect width="{self.W}" height="{self.H}" fill="#FFFFFF"/>\n{body}\n</svg>\n')
