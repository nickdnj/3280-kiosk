#!/usr/bin/env bash
# Build the assembly manual PDF and prove the page geometry.
set -euo pipefail
cd "$(dirname "$0")"

python3 make-manual.py
rsvg-convert -f pdf --page-width=8.5in --page-height=11in manual/*.svg \
    -o 3280-K-assembly-manual.pdf

info=$(pdfinfo 3280-K-assembly-manual.pdf)
pages=$(sed -n 's/^Pages: *//p'     <<<"$info")
size=$(sed  -n 's/^Page size: *//p' <<<"$info")
[[ "$pages" == "15" ]]              || { echo "FAIL: $pages pages, expected 15"; exit 1; }
[[ "$size" == 612\ x\ 792* ]]       || { echo "FAIL: page size $size"; exit 1; }
echo "OK  3280-K-assembly-manual.pdf  ${pages} pages  ${size}"
