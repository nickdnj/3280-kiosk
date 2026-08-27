#!/usr/bin/env python3
"""Monitor size validation against MEASURED cabinet geometry.
Emits 07-monitor-fit.svg. See ../monitor-selection.md."""
import pathlib, math

# ---- cabinet: measured + OEM (see cabinet-spec-oem.md, me1-findings.md) -----
CAB_W        = 24.00     # OEM, agrees with tape
CAB_H        = 71.00     # OEM overall, floor -> top
BASE_H       =  3.125    # derived: 71.00 - 67.875 measured box
OPENING_W    = 19.75     # measured ~19.5-20
DOOR_W       = 24.30     # 3230 fig 3-4; 3280 assumed same family
DOOR_H       = 48.00     # ⚠️ ASSUMED — one of the unconfirmed tape readings
DOOR_BOT_AFF =  7.00     # ⚠️ ASSUMED

# ---- monitor geometry: 16:9, portrait ---------------------------------------
K_LONG, K_SHORT = 16/math.hypot(16,9), 9/math.hypot(16,9)
BZ_SIDE, BZ_TOP, BZ_CHIN = 0.35, 0.35, 0.80
def mon(diag):
    aw, ah = diag*K_SHORT, diag*K_LONG          # portrait: w=short, h=long
    return dict(d=diag, aw=aw, ah=ah,
                ow=aw+2*BZ_SIDE, oh=ah+BZ_TOP+BZ_CHIN)
OPTS = [mon(24), mon(27), mon(32)]

GAP, PLATE_H = 1.00, 4.00
S = 8.0
FLOOR = 698.0
COLS = [90, 392, 694]
W, H = 1060, 1010
TAN, TAN2, INK, DARK = '#E5DDCB', '#EFE9DC', '#2b2b2b', '#141414'
SCREEN, DIMC, GOOD, WARN = '#E9E2D0', '#B3401A', '#2F5D3A', '#8a5f10'

o=[]
def add(t): o.append(t)
def txt(x,y,s,size=11,fill='#333',anchor='start',weight='400'):
    add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" '
        f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')
def yy(h): return FLOOR - S*h

add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
    f'font-family="Helvetica,Arial,sans-serif"><rect width="{W}" height="{H}" fill="#fff"/>')
txt(40,42,'Monitor Size — Fit Against the Measured Cabinet',22,'#1b1b1b',weight='700')
txt(40,64,'Carrier panel replaces the outer louvered door. Cabinet 24" x 71" overall on a 3-1/8" base — '
          'OEM spec confirmed by tape. Scale 8 px = 1 in.',12.5,'#555')
add(f'<rect x="40" y="78" width="560" height="21" fill="#FBE7E1" stroke="{DIMC}"/>')
txt(50,93,'DOOR APERTURE (48" tall, 7" AFF) IS STILL ASSUMED — everything else is measured or OEM',
    11.5,DIMC,weight='700')

for i,m in enumerate(OPTS):
    x0 = COLS[i]; cx = x0 + CAB_W*S/2
    # cabinet body + base
    add(f'<rect x="{x0}" y="{yy(CAB_H):.1f}" width="{CAB_W*S:.1f}" height="{(CAB_H-BASE_H)*S:.1f}" '
        f'fill="{TAN}" stroke="{INK}" stroke-width="1.3"/>')
    add(f'<rect x="{x0-3}" y="{yy(CAB_H):.1f}" width="{CAB_W*S+6:.1f}" height="{4.0*S:.1f}" '
        f'fill="{TAN2}" stroke="{INK}" stroke-width="1.3"/>')
    add(f'<rect x="{x0+6}" y="{yy(BASE_H):.1f}" width="{CAB_W*S-12:.1f}" height="{BASE_H*S:.1f}" '
        f'fill="#3a3a3a"/>')
    # louvers above / below the door aperture
    for hgt in [h*0.9 for h in range(int((DOOR_BOT_AFF)*10//9))]:
        pass
    for yv in [DOOR_BOT_AFF+DOOR_H+1.2+k*1.2 for k in range(int((CAB_H-4-(DOOR_BOT_AFF+DOOR_H+1.2))/1.2))]:
        add(f'<line x1="{x0+7:.1f}" y1="{yy(yv):.1f}" x2="{x0+CAB_W*S-7:.1f}" y2="{yy(yv):.1f}" '
            f'stroke="#cfc6b4" stroke-width="1.1"/>')
    for yv in [BASE_H+0.9+k*1.2 for k in range(int((DOOR_BOT_AFF-BASE_H-1.4)/1.2))]:
        add(f'<line x1="{x0+7:.1f}" y1="{yy(yv):.1f}" x2="{x0+CAB_W*S-7:.1f}" y2="{yy(yv):.1f}" '
            f'stroke="#cfc6b4" stroke-width="1.1"/>')
    # carrier panel (replacement door)
    dy0, dh = yy(DOOR_BOT_AFF+DOOR_H), DOOR_H*S
    dw = DOOR_W*S
    add(f'<rect x="{cx-dw/2:.1f}" y="{dy0:.1f}" width="{dw:.1f}" height="{dh:.1f}" '
        f'fill="{TAN}" stroke="{INK}" stroke-width="1.6"/>')
    # hinge
    for hy in (dy0+22, dy0+dh-40):
        add(f'<rect x="{cx-dw/2-4:.1f}" y="{hy:.1f}" width="4" height="18" fill="#9a9a9a" stroke="#444" stroke-width="0.6"/>')
    # badge
    add(f'<rect x="{cx-dw/2+10:.1f}" y="{dy0+8:.1f}" width="52" height="11" fill="#1b1b1b"/>')
    txt(cx-dw/2+36, dy0+16.5, 'CONCURRENT', 6.5, '#f0ebe0', 'middle')
    # monitor block, vertically centred in the aperture
    block = m['oh'] + GAP + PLATE_H
    top   = DOOR_BOT_AFF + DOOR_H - (DOOR_H-block)/2
    mtop  = yy(top); mh = m['oh']*S; mw = m['ow']*S
    add(f'<rect x="{cx-mw/2:.1f}" y="{mtop:.1f}" width="{mw:.1f}" height="{mh:.1f}" '
        f'fill="{DARK}" stroke="#000" stroke-width="0.9"/>')
    add(f'<rect x="{cx-m["aw"]*S/2:.1f}" y="{mtop+BZ_TOP*S:.1f}" width="{m["aw"]*S:.1f}" '
        f'height="{m["ah"]*S:.1f}" fill="{SCREEN}"/>')
    txt(cx, mtop+mh/2-4, f'{m["d"]:g}"', 15, '#5a5344', 'middle', '700')
    txt(cx, mtop+mh/2+12, 'PORTRAIT', 8.5, '#8d8677', 'middle')
    # button plate
    py = mtop + mh + GAP*S
    add(f'<rect x="{cx-mw/2:.1f}" y="{py:.1f}" width="{mw:.1f}" height="{PLATE_H*S:.1f}" fill="#1b1b1b"/>')
    for k in (-1,0,1):
        add(f'<circle cx="{cx+k*mw*0.27:.1f}" cy="{py+PLATE_H*S/2:.1f}" r="{0.62*S:.1f}" '
            f'fill="#3d3d3d" stroke="#8d8d8d" stroke-width="0.6"/>')
    # tan margin callout
    marg = (DOOR_W - m['ow'])/2
    add(f'<line x1="{cx-dw/2:.1f}" y1="{mtop+mh*0.5:.1f}" x2="{cx-mw/2:.1f}" y2="{mtop+mh*0.5:.1f}" '
        f'stroke="{DIMC}" stroke-width="1"/>')
    txt(cx-dw/2-4, mtop+mh*0.5-5, f'{marg:.1f}"', 10, DIMC, 'end', '600')

add(f'<line x1="40" y1="{FLOOR}" x2="{W-40}" y2="{FLOOR}" stroke="#333" stroke-width="1.6"/>')

# overall dims on the first cabinet
x0=COLS[0]
add(f'<g stroke="{DIMC}" stroke-width="1" fill="none">'
    f'<line x1="{x0}" y1="{yy(CAB_H)-16:.1f}" x2="{x0+CAB_W*S:.1f}" y2="{yy(CAB_H)-16:.1f}"/>'
    f'<line x1="{x0}" y1="{yy(CAB_H)-21:.1f}" x2="{x0}" y2="{yy(CAB_H)-11:.1f}"/>'
    f'<line x1="{x0+CAB_W*S:.1f}" y1="{yy(CAB_H)-21:.1f}" x2="{x0+CAB_W*S:.1f}" y2="{yy(CAB_H)-11:.1f}"/>'
    f'<line x1="{x0-30}" y1="{yy(CAB_H):.1f}" x2="{x0-30}" y2="{FLOOR}"/>'
    f'<line x1="{x0-35}" y1="{yy(CAB_H):.1f}" x2="{x0-25}" y2="{yy(CAB_H):.1f}"/>'
    f'<line x1="{x0-35}" y1="{FLOOR}" x2="{x0-25}" y2="{FLOOR}"/></g>')
add(f'<rect x="{x0+CAB_W*S/2-22:.1f}" y="{yy(CAB_H)-24:.1f}" width="44" height="15" fill="#fff"/>')
txt(x0+CAB_W*S/2, yy(CAB_H)-13, '24.0"', 11.5, DIMC, 'middle', '600')
_my=(yy(CAB_H)+FLOOR)/2
add(f'<rect x="{x0-40}" y="{_my-16:.1f}" width="20" height="32" fill="#fff"/>')
add(f'<text x="{x0-30}" y="{_my:.1f}" font-size="11.5" fill="{DIMC}" font-weight="600" '
    f'text-anchor="middle" transform="rotate(-90 {x0-30} {_my:.1f})">71.0"</text>')

# ---- caption cards ----------------------------------------------------------
def card(i, m, verdict, vcol, rows):
    x = COLS[i]-18
    add(f'<rect x="{x}" y="738" width="248" height="24" fill="{vcol}"/>')
    txt(x+9, 755, f'{m["d"]:g}" 16:9 PORTRAIT — {verdict}', 11.5, '#fff', weight='700')
    yv = 780
    for lab, val, col in rows:
        txt(x, yv, lab, 9.5, '#888')
        txt(x+248, yv, val, 10, col, 'end', '600')
        add(f'<line x1="{x}" y1="{yv+4}" x2="{x+248}" y2="{yv+4}" stroke="#e6e6e6" stroke-width="0.7"/>')
        yv += 18

def rows_for(m, wt, tech, note, notecol):
    marg=(DOOR_W-m['ow'])/2
    return [('Active area', f'{m["aw"]:.1f}" x {m["ah"]:.1f}"', '#333'),
            ('Outline w/ bezel', f'{m["ow"]:.1f}" x {m["oh"]:.1f}"', '#333'),
            ('Tan margin each side', f'{marg:.1f}"', '#333'),
            ('Screen / door width', f'{100*m["ow"]/DOOR_W:.0f}%', '#333'),
            ('Fits 19.75" opening', 'yes' if m['ow']<OPENING_W-1.0 else 'tight', GOOD if m['ow']<OPENING_W-1.0 else WARN),
            ('Weight, cased', wt, '#333'),
            ('Panel tech at this size', tech, '#333'),
            ('Verdict', note, notecol)]

card(0, OPTS[0], 'UNDERSIZED', '#8a5f10',
     rows_for(OPTS[0], '~8-10 lb', 'IPS everywhere', 'too small for a 24.3" door', WARN))
card(1, OPTS[1], 'RECOMMENDED', '#2F5D3A',
     rows_for(OPTS[1], '~11-13 lb', 'IPS everywhere', 'best balance', GOOD))
card(2, OPTS[2], 'STRETCH', '#8a5f10',
     rows_for(OPTS[2], '~15-18 lb', 'often VA — check', 'viable, watch angles + weight', WARN))

txt(40, 972, 'Key correction: the carrier panel replaces the 24.3"-wide outer door — not a 14.5" door inside a 19" opening, which is what every',
    11.5, DIMC, weight='600')
txt(40, 990, 'earlier drawing assumed. There is far more face to fill than we had drawn, which is why 24" now reads as undersized.',
    11.5, DIMC, weight='600')
add('</svg>')
pathlib.Path('07-monitor-fit.svg').write_text('\n'.join(o))
print('07-monitor-fit.svg written')
for m in OPTS:
    print(f'{m["d"]:g}" portrait: active {m["aw"]:.2f} x {m["ah"]:.2f}, '
          f'outline {m["ow"]:.2f} x {m["oh"]:.2f}, margin {(DOOR_W-m["ow"])/2:.2f}", '
          f'{100*m["ow"]/DOOR_W:.0f}% of door width')
