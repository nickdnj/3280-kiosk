# Rev 1 manufacturing drawing package

Twelve B-size (17 × 11) sheets, third-angle projection, ANSI-style title blocks.

**[`3280-kiosk-rev1-drawing-package.pdf`](3280-kiosk-rev1-drawing-package.pdf)** —
the whole package as one file. This is what you send to a shop. Fonts are
embedded, so it looks the same everywhere.

**[`index.html`](index.html)** — the same sheets in the browser, with a print
stylesheet (one sheet per page, Letter landscape, *Fit to page*).

| Sheet | | |
|---|---|---|
| **000** | Cover, drawing index, general notes | material and finish schedule, the ADA derivation, the museum constraint |
| **100** | General arrangement | front / side / top, plus the kiosk drawn on the 3280 with the ADA reach band |
| **101** | Exploded view and BOM | 21 numbered items, balloons, source sheet per part |
| **102** | Section A-A | rotated 90° CW; internal stack and the full depth chain |
| **200** | **P1 face plate** | the cut drawing — fully dimensioned, feature schedule |
| **300** | P2 side panel, P3 top/bottom | plus a horizontal section through the monitor zone |
| **301** | P4 rear panel, P9 VESA rail, P10 Pi tray | slot detail and the shim-to-suit note |
| **302** | P5–P8 cleats and button rail | insert locations and the clamp-and-spot method |
| **400** | Hole and fastener schedule | every hole tagged, located, and matched to an item |
| **500** | Electrical | power distribution and the button circuit, with GPIO assignment |
| **600** | Assembly sequence | twelve steps, bench test before the machine is touched |
| **700** | Inspection dimensions | nominal, tolerance, method, and why each one matters — with sign-off |

## Regenerating

```bash
python3 make-package.py     # writes 000.svg … 700.svg
python3 check-sheets.py     # nothing outside the printable area
../make-pdfs.sh             # rebuild the PDF deliverables
```

The SVGs are the reviewable artifact — they diff cleanly in git, so a revision
shows up as changed geometry rather than a changed blob. **The PDF is the
handoff.** Rebuild it when you issue a revision, not on every commit.

All geometry lives in [`_geom.py`](_geom.py), which mirrors
[`../fab-rev1/make-cutfiles.py`](../fab-rev1/make-cutfiles.py). Change a
dimension there and re-run both — the DXF and the drawings cannot drift apart.
[`_sheet.py`](_sheet.py) is the sheet framework: frame, zones, title block,
dimensions, leaders, balloons, section hatching.

## Status

**Concept package — not released for production.** Two things gate release:

1. **⌀30.5 mm** on sheet 200 is nominal for a 30 mm anti-vandal switch. Verify it
   against the datasheet of the switch actually bought. This is a one-piece part.
2. **The monitor.** Sheet 301's depth is shimmed to suit, and the go/no-go
   criteria on sheet 700 — powers itself back on after a mains cut, matte only —
   are not optional.

The mounting adapter is deliberately **not** in this package. See sheet 000
note 10.
