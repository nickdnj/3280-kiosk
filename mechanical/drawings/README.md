# Drawings

> ## ⛔ SUPERSEDED FOR REV 1
> The kiosk is no longer a replacement door integrated into the cabinet. It is a
> **self-contained enclosure surface-mounted on the closed factory door** — see
> [`../rev1-standalone-kiosk.md`](../rev1-standalone-kiosk.md) and the
> [interactive design study](../rev1-design-study.html).
> This document describes the **Rev 2** concept and is kept for provenance.
> Don't build from it.

All six sheets are generated from **one shared geometry block** in
[`make-drawings.py`](make-drawings.py). Change a dimension there and re-run:

```bash
cd mechanical/drawings
python3 make-drawings.py        # 01–06
python3 make-monitor-fit.py     # 07
```

| | Sheet | What it settles |
|---|---|---|
| 01 | [Front elevation](01-front-elevation.svg) | The whole thing at real scale; ADA band, screen and button heights |
| 02 | [Carrier panel](02-carrier-panel.svg) | Every feature dimensioned, with a schedule — the fabrication sheet |
| 03 | [Plan section](03-plan-section.svg) | Depth budget, swing envelope, **the C1 requirement** |
| 04 | [Door replacement](04-door-replacement.svg) | How it mounts, and why it's reversible |
| 05 | [Assembly stack](05-assembly-stack.svg) | Carrier panel + cased monitor + Pi |
| 06 | [Recessed vs proud](06-recessed-vs-proud.svg) | The open aesthetic choice — for the docents |
| 07 | [Monitor fit](07-monitor-fit.svg) | Why 27″ and not 24″ |

## Geometry these are built on

```
cabinet     24.00" W x 71.00" H x 34.00" D      OEM 50-045R00
base         3.125"                             derived (71.00 - 67.875 measured)
opening     19.75" clear                        measured
frame offset 2.125" uniform, all four sides     assumption, 2026-08-27
aperture    19.75" x 63.625"   (5.25" AFF)      derived
door        24.30" x 68.175"   (2.98" AFF)      derived, 0.15" overhang all round
monitor     27" 16:9 portrait, 13.94 x 24.68    chosen
buttons     34" AFF     screen centre ~49" AFF  chosen
C1 required 2.48"                               STILL UNMEASURED
```

⚠️ **[`superseded/`](superseded/)** holds the pre-measurement set. Don't build
from those.
