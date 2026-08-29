# Build kit — the 15 × 30 box

> ⚠️ **Concept.** Nothing has been built. Everything here is generated from
> [`../fab-rev1/_p1.py`](../fab-rev1/_p1.py), so the cookbook, the DXF and the
> cut list cannot disagree.

**[`3280-K-box-cookbook.pdf`](3280-K-box-cookbook.pdf)** — 20 pages, Letter.
Print it and build from it.

```bash
./make-pdf.sh          # regenerates + verifies 20 Letter pages
python3 _kit.py        # kit contents + 7 checks
```

---

## What's in the book

| | |
|---|---|
| 1 | Cover — the finished box |
| 2 | Safety: glasses and mask · work flat on a blanket · no hammer · pilot every hole · two people |
| **3** | **Kit A — wood as bought**, with model numbers |
| **4** | **Kit B — the eight parts**, drawn to relative scale |
| **5** | **Kit C — fasteners**, F1–F7 at 1:1 with counts |
| **6** | **Kit D — glue and finish**, plus the all-six-faces rule |
| **7** | **Kit E — the twelve tools** |
| 8 | How to measure: one end · square the line · blade on the waste side |
| 9 | The nine crosscuts, laid out on each board |
| 10–19 | Assembly, one step per page |
| 20 | Done — and don't hang it on the machine yet |

Wordless except where a human has to measure something. The only numerals are
dimensions, counts and part codes.

## Kit contents

**Wood** — 1×4 × 8 ft (914681) ×2 · 1×3 × 8 ft (914649) ×3 · ½″ MDF 2×4 (109097)
×1. Home Depot cuts the MDF; you never handle a sheet good.

**Parts, all crosscuts** — P2 side 3½ × 30 ×2 · P3 top/bottom 3½ × 13½ ×2 ·
P7 button rail 13½ · P8 rear cleat 28½ ×2 · P9 VESA rail 28½ ×2 · P4 rear panel
13¼ × 28¼ (MDF) · P10 tray 4 × 3 (MDF) · P1 face plate 15 × 30 (ACM, ordered).

**Fasteners — 90 pieces**

| | | |
|---|---|---|
| F1 | wood screw #6 × 1¼ | ×40 |
| F2 | threaded insert #8-32 brass | ×21 |
| F3 | screw #8-32 × ½ button head | ×15 |
| F4 | thumbscrew #8-32 × ½ | ×6 |
| F5 | bolt M4 × 12 + washer | ×4 |
| F6 | switch, 30 mm anti-vandal | ×3 |
| F7 | inlet, IEC C14 fused | ×1 |

F2 and F3 are **derived from P1's hole count**, and `_kit.py` checks it — if the
face plate ever changes, the kit count follows.

**Glue and finish** — G1 PVA wood glue · G2 five-minute epoxy (the 21 inserts,
nothing else) · G3 sanding sealer or primer · G4 satin black.

**Tools** — mitre saw · tape · combination square · pencil · drill/driver ·
bits (7/64 pilot, 3/8 insert, countersink) · insert driver · clamps ×4 ·
sandpaper 120 + 180 · safety glasses · dust mask · brush.

**Also bring** — blue tape, a rag and denatured alcohol for squeeze-out, and
cardboard for the printed P1 mock-up.

## The three rules the book keeps repeating

1. **Cut P2 first, dry-fit, measure the real cavity.** Then cut everything else
   to what you measured. The tables are a prediction; the box is the truth.
2. **Pilot every hole.** Pine end grain splits, and the corner screws go into it.
3. **Seal all six faces**, inside included. A panel sealed on one side cups
   toward the unsealed one, and a cupped rear panel opens a gap at the face plate.

## Not in the kit

The **monitor** — ungated, and it must survive a power cut and be matte.
The **Raspberry Pi and PSU**. The **mounting adapter**, still undesigned with
0.382″ of the ADA §307.2 budget left.

And the ⌀30.5 mm switch cutout is **still unverified**. It gates P1's release.
