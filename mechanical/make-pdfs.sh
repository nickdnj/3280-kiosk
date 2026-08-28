#!/usr/bin/env bash
# Build the PDF deliverables from the generated sources.
#
#   ./make-pdfs.sh
#
# Two different jobs, two different tools:
#   dwg/     12 SVG sheets  -> one 17x11 landscape PDF   (rsvg-convert)
#   fab-rev1 stencil HTML   -> one Letter 1:1 PDF        (headless Chrome)
#
# Run this only when issuing a revision. The SVG and HTML are the reviewable
# artifacts and diff cleanly; the PDFs are the handoff and churn the repo.
set -euo pipefail
cd "$(dirname "$0")"

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PORT=8753

echo "→ drawing package"
command -v rsvg-convert >/dev/null || { echo "need rsvg-convert (brew install librsvg)"; exit 1; }
( cd dwg && rsvg-convert -f pdf \
    --page-width=17in --page-height=11in --width=17in --height=11in --keep-aspect-ratio \
    000.svg 100.svg 101.svg 102.svg 200.svg 300.svg 301.svg 302.svg \
    400.svg 500.svg 600.svg 700.svg \
    -o 3280-kiosk-rev1-drawing-package.pdf )
echo "  dwg/3280-kiosk-rev1-drawing-package.pdf"

echo "→ 1:1 stencil"
[ -x "$CHROME" ] || { echo "need Google Chrome for HTML->PDF"; exit 1; }
( cd fab-rev1 && python3 -m http.server $PORT >/dev/null 2>&1 & echo $! > /tmp/_stpid )
sleep 1
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$PWD/fab-rev1/P1-face-plate-stencil.pdf" \
  "http://localhost:$PORT/stencil-letter.html" >/dev/null 2>&1
kill "$(cat /tmp/_stpid)" 2>/dev/null || true; rm -f /tmp/_stpid
echo "  fab-rev1/P1-face-plate-stencil.pdf"

python3 - <<'PY'
import re, sys
for f, want in (('dwg/3280-kiosk-rev1-drawing-package.pdf', (1224, 792)),
                ('fab-rev1/P1-face-plate-stencil.pdf',      (612, 792))):
    d = open(f, 'rb').read()
    boxes = {tuple(round(float(v)) for v in m.group(1).split()[2:])
             for m in re.finditer(rb'/MediaBox\s*\[([\d.\s]+)\]', d)}
    ok = not boxes or boxes == {want}
    print(f"  {'OK  ' if ok else 'CHECK'} {f}  {len(d)//1024} KB  media {boxes or 'compressed'}")
PY
echo "done. the stencil must print at 100% / margins none, or the 4.000 in bar will not measure."
