#!/usr/bin/env python3
"""
3280 Kiosk — door fabrication package generator.

Emits laser-cut DXFs and review previews for the four outsourced parts.
ALL INPUT NUMBERS ARE ASSUMED (see ../dimensions-assumed.md). When ME-1 and
EL-5 land, edit the PARAMS block and re-run:

    python3 generate.py

Outputs (this directory):
    P1-face.dxf / .svg          door face, 0.080" 5052, flat
    P2-shroud-flat.dxf / .svg   rear shroud, 0.063" 5052, 4 bends
    P3-button-plate.dxf / .svg  button plate, 0.080" 5052, black anodised
    P4-panel-bracket.dxf / .svg panel retention bracket, 0.063" 5052, 1 bend

Units: inches. DXF is R12 ASCII, layers CUT and BEND.
"""
import math, pathlib

HERE = pathlib.Path(__file__).parent

# ============================================================ PARAMS (ASSUMED)
P = dict(
    # --- display, from a 24" 16:9 panel run portrait -------------------------
    active_w      = 11.77,   # LCD active area width   (VERIFY: real panel)
    active_h      = 20.92,   # LCD active area height  (VERIFY: real panel)
    window_under  = 0.06,    # window cut under active area, total (0.03/side)
    # --- door face layout ----------------------------------------------------
    door_w        = 14.50,
    door_h        = 30.00,
    badge_band    = 2.00,    # top band carrying the CONCURRENT badge
    bezel_block_w = 12.80,   # painted satin-black bezel field
    bezel_block_h = 21.90,
    reveal        = 0.60,    # gap between bezel block and button plate
    plate_w       = 12.80,
    plate_h       = 4.00,
    bottom_rail   = 1.50,
    # --- depth ---------------------------------------------------------------
    door_depth    = 2.50,    # bezel face -> rear shroud (VERIFY: C1 >= this +0.5)
    face_t        = 0.080,
    shroud_t      = 0.063,
    # --- buttons -------------------------------------------------------------
    btn_count     = 5,       # 3 mapped + 2 spare blanks (ER3)
    btn_hole_d    = 1.125,   # 30 mm arcade body, 28.5 mm mounting hole
    btn_clear_d   = 1.250,   # clearance in P1 so P3 alone locates the button
    btn_edge_marg = 0.400,   # material between hole edge and plate edge
    # --- fasteners / features ------------------------------------------------
    m3            = 0.128,   # M3 clearance
    perim_inset   = 0.350,   # perimeter fastener line, in from the door edge
    corner_r      = 0.250,
    window_r      = 0.125,
    plate_r       = 0.125,
    badge_w       = 4.80,
    badge_h       = 1.20,
    # --- shroud --------------------------------------------------------------
    wall_h        = 2.40,    # outside wall height = door_depth - face_t (rounded)
    bend_ir       = 0.063,   # inside bend radius (= material thickness)
    k_factor      = 0.42,    # 5052 with IR ~= T
    vent_slot_l   = 1.60,
    vent_slot_w   = 0.20,
    vent_cols     = 6,
    vent_rows     = 10,      # per field; two fields (intake low, exhaust high)
    # --- panel retention bracket P4 -----------------------------------------
    p4_leg_a      = 0.75,    # fixing leg (slotted)
    p4_leg_b      = 0.60,    # clamping lip over the panel chassis edge
    p4_len        = 3.00,
    p4_slot_l     = 0.40,
    p4_qty        = 4,
)

# ============================================================ BEND MATHS
def bend_deduction(t, ir, k, angle_deg=90.0):
    """Outside-dimension bend deduction. flat = sum(outside legs) - n*BD."""
    a = math.radians(angle_deg)
    ba = a * (ir + k * t)                      # bend allowance
    ossb = math.tan(a / 2.0) * (ir + t)        # outside setback
    return 2.0 * ossb - ba

BD63 = bend_deduction(P['shroud_t'], P['bend_ir'], P['k_factor'])

# ============================================================ GEOMETRY HELPERS
class Part:
    def __init__(self, name, title, material, thick, ops, finish, qty=1):
        self.name, self.title = name, title
        self.material, self.thick = material, thick
        self.ops, self.finish, self.qty = ops, finish, qty
        self.cut, self.bend = [], []          # entity lists
        self.notes = []
    # -- primitives (layer-tagged) -------------------------------------------
    def line(self, x1, y1, x2, y2, layer='CUT'):
        (self.cut if layer == 'CUT' else self.bend).append(('LINE', x1, y1, x2, y2))
    def arc(self, cx, cy, r, a0, a1, layer='CUT'):
        (self.cut if layer == 'CUT' else self.bend).append(('ARC', cx, cy, r, a0, a1))
    def circle(self, cx, cy, r, layer='CUT'):
        (self.cut if layer == 'CUT' else self.bend).append(('CIRCLE', cx, cy, r))
    # -- compound shapes ------------------------------------------------------
    def rrect(self, x, y, w, h, r):
        self.line(x + r, y, x + w - r, y)
        self.line(x + w, y + r, x + w, y + h - r)
        self.line(x + w - r, y + h, x + r, y + h)
        self.line(x, y + h - r, x, y + r)
        self.arc(x + w - r, y + r,     r, 270, 360)
        self.arc(x + w - r, y + h - r, r,   0,  90)
        self.arc(x + r,     y + h - r, r,  90, 180)
        self.arc(x + r,     y + r,     r, 180, 270)
    def rect(self, x, y, w, h, layer='CUT'):
        self.line(x, y, x + w, y, layer); self.line(x + w, y, x + w, y + h, layer)
        self.line(x + w, y + h, x, y + h, layer); self.line(x, y + h, x, y, layer)
    def hole(self, cx, cy, d):
        self.circle(cx, cy, d / 2.0)
    def slot(self, cx, cy, length, width, vertical=False):
        r = width / 2.0; d = (length - width) / 2.0
        if d <= 0: return self.hole(cx, cy, width)
        if not vertical:
            self.line(cx - d, cy + r, cx + d, cy + r)
            self.line(cx + d, cy - r, cx - d, cy - r)
            self.arc(cx + d, cy, r, 270, 90); self.arc(cx - d, cy, r, 90, 270)
        else:
            self.line(cx - r, cy - d, cx - r, cy + d)
            self.line(cx + r, cy + d, cx + r, cy - d)
            self.arc(cx, cy + d, r,   0, 180); self.arc(cx, cy - d, r, 180, 360)
    # -- extents --------------------------------------------------------------
    def extents(self):
        xs, ys = [], []
        for e in self.cut + self.bend:
            if e[0] == 'LINE':   xs += [e[1], e[3]]; ys += [e[2], e[4]]
            elif e[0] == 'ARC':  xs += [e[1]-e[3], e[1]+e[3]]; ys += [e[2]-e[3], e[2]+e[3]]
            elif e[0] == 'CIRCLE': xs += [e[1]-e[3], e[1]+e[3]]; ys += [e[2]-e[3], e[2]+e[3]]
        return min(xs), min(ys), max(xs), max(ys)

# ============================================================ DXF WRITER (R12)
def dxf(part):
    o = []
    def g(code, val): o.append(str(code)); o.append(str(val))
    g(0,'SECTION'); g(2,'HEADER')
    g(9,'$INSUNITS'); g(70,1)                      # 1 = inches
    g(9,'$MEASUREMENT'); g(70,0)                   # 0 = imperial
    g(0,'ENDSEC')
    g(0,'SECTION'); g(2,'TABLES'); g(0,'TABLE'); g(2,'LAYER'); g(70,2)
    for nm, col in (('CUT',7), ('BEND',1)):
        g(0,'LAYER'); g(2,nm); g(70,0); g(62,col); g(6,'CONTINUOUS')
    g(0,'ENDTAB'); g(0,'ENDSEC')
    g(0,'SECTION'); g(2,'ENTITIES')
    for layer, ents in (('CUT', part.cut), ('BEND', part.bend)):
        for e in ents:
            if e[0] == 'LINE':
                _, x1, y1, x2, y2 = e
                g(0,'LINE'); g(8,layer)
                g(10,f'{x1:.5f}'); g(20,f'{y1:.5f}'); g(30,'0.0')
                g(11,f'{x2:.5f}'); g(21,f'{y2:.5f}'); g(31,'0.0')
            elif e[0] == 'ARC':
                _, cx, cy, r, a0, a1 = e
                g(0,'ARC'); g(8,layer)
                g(10,f'{cx:.5f}'); g(20,f'{cy:.5f}'); g(30,'0.0')
                g(40,f'{r:.5f}'); g(50,f'{a0:.4f}'); g(51,f'{a1:.4f}')
            elif e[0] == 'CIRCLE':
                _, cx, cy, r = e
                g(0,'CIRCLE'); g(8,layer)
                g(10,f'{cx:.5f}'); g(20,f'{cy:.5f}'); g(30,'0.0'); g(40,f'{r:.5f}')
    g(0,'ENDSEC'); g(0,'EOF')
    return '\n'.join(o) + '\n'

# ============================================================ SVG PREVIEW
def svg(part, dims=()):
    x0, y0, x1, y1 = part.extents()
    w, h = x1 - x0, y1 - y0
    s = min(760.0 / w, 620.0 / h)
    PADL, PADT = 60, 96
    PADB = 78 + len(dims) * 17 + 24        # grow with the note block
    W = int(w * s) + PADL * 2
    H = int(h * s) + PADT + PADB
    def px(x): return PADL + (x - x0) * s
    def py(y): return PADT + (y1 - y) * s
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
           f'viewBox="0 0 {W} {H}" font-family="Helvetica,Arial,sans-serif">',
           f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
           f'<text x="30" y="32" font-size="18" font-weight="700" fill="#1b1b1b">'
           f'{part.name} &#183; {part.title}</text>',
           f'<text x="30" y="52" font-size="12" fill="#555">{part.material} &#183; '
           f'{part.thick:.3f}" &#183; qty {part.qty} &#183; {part.ops} &#183; {part.finish}</text>',
           f'<rect x="30" y="64" width="360" height="19" fill="#FBE7E1" stroke="#B3401A"/>',
           f'<text x="39" y="77.5" font-size="11.5" font-weight="700" fill="#B3401A">'
           f'ASSUMED GEOMETRY &#8212; NOT FOR ORDER UNTIL ME-1 + EL-5</text>']
    for layer, ents, col, wid in (('CUT', part.cut, '#1b1b1b', 1.4),
                                  ('BEND', part.bend, '#B3401A', 1.1)):
        dash = ' stroke-dasharray="7 4"' if layer == 'BEND' else ''
        out.append(f'<g fill="none" stroke="{col}" stroke-width="{wid}"{dash}>')
        for e in ents:
            if e[0] == 'LINE':
                _, ax, ay, bx, by = e
                out.append(f'<line x1="{px(ax):.2f}" y1="{py(ay):.2f}" '
                           f'x2="{px(bx):.2f}" y2="{py(by):.2f}"/>')
            elif e[0] == 'ARC':
                _, cx, cy, r, a0, a1 = e
                sa, ea = math.radians(a0), math.radians(a1)
                ax, ay = cx + r*math.cos(sa), cy + r*math.sin(sa)
                bx, by = cx + r*math.cos(ea), cy + r*math.sin(ea)
                sweep = (a1 - a0) % 360
                large = 1 if sweep > 180 else 0
                out.append(f'<path d="M {px(ax):.2f} {py(ay):.2f} A {r*s:.2f} {r*s:.2f} '
                           f'0 {large} 0 {px(bx):.2f} {py(by):.2f}"/>')
            elif e[0] == 'CIRCLE':
                _, cx, cy, r = e
                out.append(f'<circle cx="{px(cx):.2f}" cy="{py(cy):.2f}" r="{r*s:.2f}"/>')
        out.append('</g>')
    ty = PADT + h * s + 34
    out.append(f'<text x="30" y="{ty}" font-size="12" font-weight="700" fill="#1b1b1b">'
               f'KEY DIMENSIONS (in)</text>')
    for i, d in enumerate(dims):
        out.append(f'<text x="30" y="{ty + 20 + i*17}" font-size="11.5" fill="#333">{d}</text>')
    out.append(f'<text x="{W-30}" y="{H-16}" font-size="10.5" fill="#888" '
               f'text-anchor="end">solid = CUT &#183; dashed = BEND &#183; '
               f'generated by fab/generate.py</text>')
    out.append('</svg>')
    return '\n'.join(out)

# ============================================================ P1 — DOOR FACE
def build_p1():
    p = Part('P1', 'DOOR FACE', '5052-H32 aluminium', P['face_t'],
             'laser cut, flat, deburr all edges',
             'RAW — primed + tan topcoat locally')
    W, H = P['door_w'], P['door_h']
    p.rrect(0, 0, W, H, P['corner_r'])

    # screen window, centred, sitting inside the bezel block
    blk_y0 = P['bottom_rail'] + P['plate_h'] + P['reveal']
    act_x0 = (W - P['active_w']) / 2.0
    act_y0 = blk_y0 + (P['bezel_block_h'] - P['active_h']) / 2.0
    u = P['window_under'] / 2.0
    win_x0, win_y0 = act_x0 + u, act_y0 + u
    win_w,  win_h  = P['active_w'] - P['window_under'], P['active_h'] - P['window_under']
    p.rrect(win_x0, win_y0, win_w, win_h, P['window_r'])

    # button clearance holes (P3 in front locates the buttons)
    for cx in button_x():
        p.hole(cx, P['bottom_rail'] + P['plate_h'] / 2.0, P['btn_clear_d'])
    # P3 fixing holes, in the gaps between buttons
    for cx in p3_fix_x():
        for cy in (P['bottom_rail'] + 0.45, P['bottom_rail'] + P['plate_h'] - 0.45):
            p.hole(cx, cy, P['m3'])
    # badge fixing holes
    bx0 = (W - P['bezel_block_w']) / 2.0
    by  = H - P['badge_band'] / 2.0
    for cx in (bx0 + 0.40, bx0 + P['badge_w'] - 0.40):
        p.hole(cx, by, P['m3'])
    # perimeter fixing line -> shroud (clinch studs from the back, or M3)
    i = P['perim_inset']
    for cy in (1.00, 7.50, 15.00, 22.50, 29.00):
        p.hole(i, cy, P['m3']); p.hole(W - i, cy, P['m3'])
    for cx in (W / 3.0, W * 2.0 / 3.0):
        p.hole(cx, i, P['m3']); p.hole(cx, H - i, P['m3'])

    p.notes = [
        f'Outline {W:.2f} x {H:.2f}, corner R{P["corner_r"]:.3f}',
        f'Window {win_w:.2f} x {win_h:.2f} @ ({win_x0:.3f}, {win_y0:.3f}), R{P["window_r"]:.3f}',
        f'  = active area {P["active_w"]:.2f} x {P["active_h"]:.2f} less {P["window_under"]:.2f} overall',
        f'Button clearance {P["btn_clear_d"]:.3f} dia x {P["btn_count"]} @ y={P["bottom_rail"]+P["plate_h"]/2:.2f}',
        f'  centres x = ' + ', '.join(f'{v:.2f}' for v in button_x()),
        f'Perimeter fixings {P["m3"]:.3f} dia x 14, {i:.2f} in from edge',
        'NO hinge holes in this part — hinge lands on the P2 side wall,',
        'so the visible tan face carries no fasteners.',
    ]
    return p, p.notes

def button_x():
    pw, d = P['plate_w'], P['btn_hole_d'] / 2.0 + P['btn_edge_marg']
    span = pw - 2 * d
    pitch = span / (P['btn_count'] - 1)
    x0 = (P['door_w'] - pw) / 2.0
    return [x0 + d + i * pitch for i in range(P['btn_count'])]

def p3_fix_x():
    xs = button_x()
    mids = [(xs[i] + xs[i+1]) / 2.0 for i in range(len(xs) - 1)]
    return [mids[0], mids[-1]]

# ============================================================ P3 — BUTTON PLATE
def build_p3():
    p = Part('P3', 'BUTTON PLATE', '5052-H32 aluminium', P['face_t'],
             'laser cut, flat, deburr all edges',
             'BLACK ANODISED — no local finishing')
    w, h = P['plate_w'], P['plate_h']
    p.rrect(0, 0, w, h, P['plate_r'])
    x0 = (P['door_w'] - w) / 2.0
    for cx in button_x():
        p.hole(cx - x0, h / 2.0, P['btn_hole_d'])
    for cx in p3_fix_x():
        p.hole(cx - x0, 0.45, P['m3']); p.hole(cx - x0, h - 0.45, P['m3'])
    pitch = (button_x()[1] - button_x()[0])
    p.notes = [
        f'Outline {w:.2f} x {h:.2f}, corner R{P["plate_r"]:.3f}',
        f'{P["btn_count"]} x {P["btn_hole_d"]:.3f} dia @ {pitch:.3f} pitch, y={h/2:.2f}',
        f'  = 30 mm arcade body (28.5 mm / {P["btn_hole_d"]:.3f}" mounting hole)',
        f'  middle three are BACK / HOME / NEXT; outer two blanked (ER3)',
        f'Edge margin {P["btn_edge_marg"]:.2f} material, hole edge to plate edge',
        f'4 x {P["m3"]:.3f} dia fixings, clear of every button',
        'Mounts on the FRONT of P1 — buttons pass through both and clamp them.',
        'Separate part so spares can be re-drilled without touching the tan face.',
    ]
    return p, p.notes

# ============================================================ P2 — REAR SHROUD
def build_p2():
    p = Part('P2', 'REAR SHROUD (flat blank)', '5052-H32 aluminium', P['shroud_t'],
             '4 bends, 90 deg up, corner relief',
             'RAW — primed + tan topcoat locally')
    wh, W, H = P['wall_h'], P['door_w'], P['door_h']
    f = wh - BD63                              # flat leg length after deduction
    FW, FH = W + 2 * f, H + 2 * f              # flat blank envelope
    # cross / plus shape: centre panel + four walls, corners removed
    p.line(f, 0, f + W, 0)                     # bottom wall, outer edge
    p.line(f + W, 0, f + W, f)
    p.line(f + W, f, FW, f)                    # right wall, lower edge
    p.line(FW, f, FW, f + H)
    p.line(FW, f + H, f + W, f + H)            # right wall, upper edge
    p.line(f + W, f + H, f + W, FH)
    p.line(f + W, FH, f, FH)                   # top wall, outer edge
    p.line(f, FH, f, f + H)
    p.line(f, f + H, 0, f + H)                 # left wall, upper edge
    p.line(0, f + H, 0, f)
    p.line(0, f, f, f)                         # left wall, lower edge
    p.line(f, f, f, 0)
    # bend lines
    p.line(f, f, f + W, f, 'BEND')
    p.line(f, f + H, f + W, f + H, 'BEND')
    p.line(f, f, f, f + H, 'BEND')
    p.line(f + W, f, f + W, f + H, 'BEND')
    # ventilation: two fields on the rear face, intake low / exhaust high
    sl, sw = P['vent_slot_l'], P['vent_slot_w']
    cols = [f + W * (i + 1) / (P['vent_cols'] + 1) for i in range(P['vent_cols'])]
    open_area = 0.0
    for base in (f + 1.2, f + H - 1.2 - (P['vent_rows'] - 1) * 0.75):
        for r in range(P['vent_rows']):
            for cx in cols:
                p.slot(cx, base + r * 0.75, sl, sw)
                open_area += sl * sw
    # fixing holes through the walls -> perimeter angle -> P1
    for cy in (1.00, 7.50, 15.00, 22.50, 29.00):
        p.hole(f / 2.0, f + cy, P['m3']); p.hole(FW - f / 2.0, f + cy, P['m3'])
    for cx in (W / 3.0, W * 2.0 / 3.0):
        p.hole(f + cx, f / 2.0, P['m3']); p.hole(f + cx, FH - f / 2.0, P['m3'])
    pct = 100.0 * open_area / (W * H)
    p.notes = [
        f'FORMED: {W:.2f} x {H:.2f} outside x {wh:.2f} deep tray, walls up',
        f'FLAT BLANK: {FW:.3f} x {FH:.3f}',
        f'Bend deduction {BD63:.4f} per bend (t={P["shroud_t"]:.3f}, IR={P["bend_ir"]:.3f}, K={P["k_factor"]})',
        f'  -> flat leg {f:.3f} per wall. SHOP: verify against your own bend table.',
        f'Corner relief: corners removed square; closed on assembly with angle.',
        f'Vents {P["vent_cols"]}x{P["vent_rows"]} slots x2 fields, {sl:.2f} x {sw:.2f}',
        f'  open area {open_area:.1f} sq in = {pct:.1f}% of the rear face',
        f'  lower field = intake, upper field = exhaust (chimney)',
        'Hinge lands on the LEFT wall of this part — locate after ME-1.',
    ]
    return p, p.notes

# ============================================================ P4 — PANEL BRACKET
def build_p4():
    p = Part('P4', 'PANEL RETENTION BRACKET (flat blank)', '5052-H32 aluminium',
             P['shroud_t'], '1 bend, 90 deg', 'RAW', qty=P['p4_qty'])
    a, b, L = P['p4_leg_a'], P['p4_leg_b'], P['p4_len']
    fa = a - BD63 / 2.0
    fb = b - BD63 / 2.0
    FW = fa + fb
    p.rect(0, 0, FW, L)
    p.line(fa, 0, fa, L, 'BEND')
    for cy in (0.60, L - 0.60):
        p.slot(fa / 2.0, cy, P['p4_slot_l'], P['m3'], vertical=True)
    p.notes = [
        f'FORMED: {a:.2f} fixing leg x {b:.2f} clamping lip x {L:.2f} long',
        f'FLAT BLANK: {FW:.3f} x {L:.2f}, bend at {fa:.3f}',
        f'2 x {P["m3"]:.3f} slots, {P["p4_slot_l"]:.2f} long, in the fixing leg',
        'SLOTS ARE DELIBERATE: the salvaged panel outline is the largest',
        'unknown in this design and these brackets absorb the variation.',
        'The lip clamps the panel CHASSIS EDGE on foam.',
        'Never screw into the panel.',
    ]
    return p, p.notes

# ============================================================ MAIN
def main():
    built = []
    for fn, dimsrc in ((build_p1, None), (build_p2, None),
                       (build_p3, None), (build_p4, None)):
        part, notes = fn()
        (HERE / f'{part.name}-{part.title.split("(")[0].strip().lower().replace(" ","-")}.dxf'
         ).write_text(dxf(part))
        built.append((part, notes))
    return built

if __name__ == '__main__':
    parts = []
    for fn in (build_p1, build_p2, build_p3, build_p4):
        part, notes = fn()
        slug = {'P1':'P1-face','P2':'P2-shroud-flat','P3':'P3-button-plate',
                'P4':'P4-panel-bracket'}[part.name]
        (HERE / f'{slug}.dxf').write_text(dxf(part))
        (HERE / f'{slug}.svg').write_text(svg(part, notes))
        x0,y0,x1,y1 = part.extents()
        print(f'{part.name}  {slug:22s} blank {x1-x0:7.3f} x {y1-y0:7.3f} in   '
              f'{len(part.cut):4d} cut ents, {len(part.bend)} bend')
        parts.append(part)
    print(f'\nbend deduction (0.063 5052, 90 deg, IR 0.063, K 0.42) = {BD63:.4f} in')
