#!/usr/bin/env python3
"""Monitor size validation against measured cabinet geometry.
Door aperture derived from a UNIFORM frame offset on all four sides.
Emits 07-monitor-fit.svg. See ../monitor-selection.md."""
import pathlib, math

# ---- cabinet: measured + OEM ------------------------------------------------
CAB_W, CAB_H, BASE = 24.00, 71.00, 3.125     # OEM width/height; base derived
BOX_H   = CAB_H - BASE                        # 67.875 measured
OPEN_W  = 19.75                               # measured clear opening
FRAME   = (CAB_W - OPEN_W) / 2                # 2.125 — uniform, all four sides
APER_W, APER_H = OPEN_W, BOX_H - 2*FRAME      # 19.75 x 63.625
APER_BOT = BASE + FRAME                       # 5.25 AFF
DOOR_W  = 24.30                               # 3230 fig 3-4
OVER    = (DOOR_W - CAB_W) / 2                # 0.15 overhang each edge
DOOR_H  = APER_H + 2*(FRAME + OVER)           # 68.175  == BOX_H + 2*OVER
DOOR_BOT = APER_BOT - FRAME - OVER            # 2.975 AFF

# ---- monitor: 16:9 portrait -------------------------------------------------
K_L, K_S = 16/math.hypot(16,9), 9/math.hypot(16,9)
BZ_S, BZ_T, BZ_C = 0.35, 0.35, 0.80
def mon(d):
    aw, ah = d*K_S, d*K_L
    return dict(d=d, aw=aw, ah=ah, ow=aw+2*BZ_S, oh=ah+BZ_T+BZ_C)
OPTS = [mon(24), mon(27), mon(32)]

PLATE_H, GAP, BTN_CTR_AFF = 4.00, 1.00, 34.00
CUT_BOT, CUT_TOP, CUT_W = 8.0, 28.0, 15.0     # optional viewing cutout

S, FLOOR = 8.0, 698.0
COLS = [90, 392, 694]
W, H = 1060, 1030
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
txt(40,64,f'Carrier panel replaces the outer door. Cabinet 24" x 71" on a 3-1/8" base; '
          f'uniform {FRAME:.3f}" frame offset all four sides. Scale 8 px = 1 in.',12.5,'#555')
add(f'<rect x="40" y="78" width="700" height="21" fill="#E4EFDF" stroke="{GOOD}"/>')
txt(50,93,f'DERIVED: aperture {APER_W:.2f}" x {APER_H:.3f}" ({APER_BOT:.2f}"–{APER_BOT+APER_H:.2f}" AFF) · '
          f'door {DOOR_W:.2f}" x {DOOR_H:.3f}", overhang {OVER:.2f}" all round',11.5,GOOD,weight='700')

for i,m in enumerate(OPTS):
    x0 = COLS[i]; cx = x0 + CAB_W*S/2
    add(f'<rect x="{x0}" y="{yy(CAB_H):.1f}" width="{CAB_W*S:.1f}" height="{BOX_H*S:.1f}" '
        f'fill="{TAN2}" stroke="{INK}" stroke-width="1.3"/>')
    add(f'<rect x="{x0+6}" y="{yy(BASE):.1f}" width="{CAB_W*S-12:.1f}" height="{BASE*S:.1f}" fill="#3a3a3a"/>')
    # aperture behind the door
    add(f'<rect x="{cx-APER_W*S/2:.1f}" y="{yy(APER_BOT+APER_H):.1f}" width="{APER_W*S:.1f}" '
        f'height="{APER_H*S:.1f}" fill="#20211f"/>')
    # carrier panel = replacement door
    add(f'<rect x="{cx-DOOR_W*S/2:.1f}" y="{yy(DOOR_BOT+DOOR_H):.1f}" width="{DOOR_W*S:.1f}" '
        f'height="{DOOR_H*S:.1f}" fill="{TAN}" stroke="{INK}" stroke-width="1.6"/>')
    for hy in (yy(DOOR_BOT+DOOR_H)+30, yy(DOOR_BOT)-48):
        add(f'<rect x="{cx-DOOR_W*S/2-4:.1f}" y="{hy:.1f}" width="4" height="18" '
            f'fill="#9a9a9a" stroke="#444" stroke-width="0.6"/>')
    add(f'<rect x="{cx-DOOR_W*S/2+10:.1f}" y="{yy(DOOR_BOT+DOOR_H)+9:.1f}" width="54" height="11" fill="#1b1b1b"/>')
    txt(cx-DOOR_W*S/2+37, yy(DOOR_BOT+DOOR_H)+17.5, 'CONCURRENT', 6.5, '#f0ebe0', 'middle')
    # optional viewing cutout, lower zone
    add(f'<rect x="{cx-CUT_W*S/2:.1f}" y="{yy(CUT_TOP):.1f}" width="{CUT_W*S:.1f}" '
        f'height="{(CUT_TOP-CUT_BOT)*S:.1f}" fill="#20211f" opacity="0.30" '
        f'stroke="{DIMC}" stroke-width="1.1" stroke-dasharray="6 4"/>')
    if i==1:
        txt(cx, yy((CUT_TOP+CUT_BOT)/2)-4, 'optional', 9, DIMC, 'middle', '600')
        txt(cx, yy((CUT_TOP+CUT_BOT)/2)+8, 'viewing cutout', 9, DIMC, 'middle', '600')
    # monitor + buttons, button plate centred at BTN_CTR_AFF
    p_bot = BTN_CTR_AFF - PLATE_H/2
    m_bot = p_bot + PLATE_H + GAP
    mw, mh = m['ow']*S, m['oh']*S
    mtop = yy(m_bot + m['oh'])
    add(f'<rect x="{cx-mw/2:.1f}" y="{mtop:.1f}" width="{mw:.1f}" height="{mh:.1f}" '
        f'fill="{DARK}" stroke="#000" stroke-width="0.9"/>')
    add(f'<rect x="{cx-m["aw"]*S/2:.1f}" y="{mtop+BZ_T*S:.1f}" width="{m["aw"]*S:.1f}" '
        f'height="{m["ah"]*S:.1f}" fill="{SCREEN}"/>')
    txt(cx, mtop+mh/2-3, f'{m["d"]:g}"', 15, '#5a5344', 'middle', '700')
    txt(cx, mtop+mh/2+12, 'PORTRAIT', 8.5, '#8d8677', 'middle')
    py = yy(p_bot + PLATE_H)
    add(f'<rect x="{cx-mw/2:.1f}" y="{py:.1f}" width="{mw:.1f}" height="{PLATE_H*S:.1f}" fill="#1b1b1b"/>')
    for k in (-1,0,1):
        add(f'<circle cx="{cx+k*mw*0.27:.1f}" cy="{py+PLATE_H*S/2:.1f}" r="{0.62*S:.1f}" '
            f'fill="#3d3d3d" stroke="#8d8d8d" stroke-width="0.6"/>')
    marg = (DOOR_W - m['ow'])/2
    add(f'<line x1="{cx-DOOR_W*S/2:.1f}" y1="{mtop+mh*0.45:.1f}" x2="{cx-mw/2:.1f}" '
        f'y2="{mtop+mh*0.45:.1f}" stroke="{DIMC}" stroke-width="1"/>')
    txt(cx-DOOR_W*S/2-4, mtop+mh*0.45-5, f'{marg:.1f}"', 10, DIMC, 'end', '600')
    txt(cx, yy(BTN_CTR_AFF)+34, f'buttons {BTN_CTR_AFF:g}" AFF', 9, GOOD, 'middle', '600')
    txt(cx, yy(m_bot+m['oh']/2)-0, '', 9)

add(f'<line x1="40" y1="{FLOOR}" x2="{W-40}" y2="{FLOOR}" stroke="#333" stroke-width="1.6"/>')

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

def card(i, m, verdict, vcol, note, notecol, wt, tech):
    x = COLS[i]-18
    add(f'<rect x="{x}" y="760" width="248" height="24" fill="{vcol}"/>')
    txt(x+9, 777, f'{m["d"]:g}" 16:9 PORTRAIT — {verdict}', 11.5, '#fff', weight='700')
    marg=(DOOR_W-m['ow'])/2
    rows=[('Active area', f'{m["aw"]:.1f}" x {m["ah"]:.1f}"', '#333'),
          ('Outline w/ bezel', f'{m["ow"]:.1f}" x {m["oh"]:.1f}"', '#333'),
          ('Tan margin each side', f'{marg:.1f}"', '#333'),
          ('Screen / door width', f'{100*m["ow"]/DOOR_W:.0f}%', '#333'),
          ('Screen centre height', f'{BTN_CTR_AFF+PLATE_H/2+GAP+m["oh"]/2:.0f}" AFF', '#333'),
          ('Fits 19.75" aperture', 'yes' if m['ow']<OPEN_W-1.0 else 'tight',
           GOOD if m['ow']<OPEN_W-1.0 else WARN),
          ('Weight, cased', wt, '#333'),
          ('Panel tech at this size', tech, '#333'),
          ('Verdict', note, notecol)]
    yv=802
    for lab,val,col in rows:
        txt(x, yv, lab, 9.5, '#888'); txt(x+248, yv, val, 10, col, 'end', '600')
        add(f'<line x1="{x}" y1="{yv+4}" x2="{x+248}" y2="{yv+4}" stroke="#e6e6e6" stroke-width="0.7"/>')
        yv += 18

card(0, OPTS[0], 'UNDERSIZED', '#8a5f10', 'too small for a 24.3" door', WARN, '~8-10 lb', 'IPS everywhere')
card(1, OPTS[1], 'RECOMMENDED', '#2F5D3A', 'best balance', GOOD, '~11-13 lb', 'IPS everywhere')
card(2, OPTS[2], 'STRETCH', '#8a5f10', 'viable, watch angles + weight', WARN, '~15-18 lb', 'often VA — check')

txt(40, 992, f'Aperture derived from a uniform {FRAME:.3f}" offset on all four sides. Check: door {DOOR_H:.3f}" = box '
             f'{BOX_H:.3f}" + 2 x {OVER:.2f}" — the same overhang it has in width.', 11.5, GOOD, weight='600')
txt(40, 1010, 'The door is far taller than we had drawn, so the lower third is free. A viewing cutout there restores the '
              '"see the machine" value the concept lost (MR3).', 11.5, DIMC, weight='600')
add('</svg>')
pathlib.Path('07-monitor-fit.svg').write_text('\n'.join(o))
print(f'aperture {APER_W:.2f} x {APER_H:.3f} @ {APER_BOT:.2f} AFF | door {DOOR_W:.2f} x {DOOR_H:.3f} @ {DOOR_BOT:.3f} AFF')
for m in OPTS:
    print(f'{m["d"]:g}": outline {m["ow"]:.2f} x {m["oh"]:.2f}, margin {(DOOR_W-m["ow"])/2:.2f}", '
          f'{100*m["ow"]/DOOR_W:.0f}% width, screen centre '
          f'{BTN_CTR_AFF+PLATE_H/2+GAP+m["oh"]/2:.1f}" AFF')
