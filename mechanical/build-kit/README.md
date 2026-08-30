# Build kit — the 15 × 30 box

> ⚠️ **Concept.** Nothing has been built. Everything here is generated from
> [`../fab-rev1/_p1.py`](../fab-rev1/_p1.py), so the cookbook, the DXF and the
> cut list cannot disagree.

**[`3280-K-box-cookbook.pdf`](3280-K-box-cookbook.pdf)** — 22 pages, Letter.
Print it and build from it.

```bash
./make-pdf.sh          # regenerates + verifies 22 Letter pages
python3 _kit.py        # kit contents + 13 checks, and the monitor buy criteria
```

---

## What's in the book

| | |
|---|---|
| 1 | Cover — the finished box |
| 2 | Safety: glasses and mask · work flat on a blanket · no hammer · pilot every hole · two people |
| **3** | **Step 0 — measure the monitor's lit rectangle.** Before P1 is ordered |
| **4** | **Kit A — wood as bought**, with model numbers |
| **5** | **Kit B — the eight parts**, drawn to relative scale |
| **6** | **Kit C — fasteners**, F1–F8 at 1:1 with counts |
| **7** | **Kit D — glue and finish**, plus the all-six-faces rule |
| **8** | **Kit E — the twelve tools** |
| 9 | How to measure: one end · square the line · blade on the waste side |
| 10 | The nine crosscuts, laid out on each board |
| 11–19 | Assembly, one step per page |
| **20** | **The light seal** — foam onto the back of P1, with the front-end section |
| 21 | Face plate on, then the back |
| 22 | Done — and don't hang it on the machine yet |

Wordless except where a human has to measure something. The only numerals are
dimensions, counts and part codes.

## Kit contents

**Wood** — 1×4 × 8 ft (914681) ×2 · 1×3 × 8 ft (914649) ×3 · ½″ MDF 2×4 (109097)
×1. Home Depot cuts the MDF; you never handle a sheet good.

**Parts, all crosscuts** — P2 side 3½ × 30 ×2 · P3 top/bottom 3½ × 13½ ×2 ·
P7 button rail 13½ · P8 rear cleat 28½ ×2 · P9 VESA rail 28½ ×2 · P4 rear panel
13¼ × 28¼ (MDF) · P10 tray 4 × 3 (MDF) · P1 face plate 15 × 30 (ACM, ordered).

**Fasteners and seals — 91 pieces**

| | | |
|---|---|---|
| F1 | wood screw #6 × 1¼ | ×40 |
| F2 | threaded insert #8-32 brass | ×21 |
| F3 | screw #8-32 × ½ button head | ×15 |
| F4 | thumbscrew #8-32 × ½ | ×6 |
| F5 | bolt M4 × 12 + washer | ×4 |
| F6 | switch, 30 mm anti-vandal | ×3 |
| F7 | inlet, IEC C14 fused | ×1 |
| F8 | foam tape, black neoprene, ¼ × 3⁄16, 10 ft | ×1 |

F2 and F3 are **derived from P1's hole count**, and `_kit.py` checks it — if the
face plate ever changes, the kit count follows.

**Glue and finish** — G1 PVA wood glue · G2 five-minute epoxy (the 21 inserts,
nothing else) · G3 sanding sealer or primer · G4 satin black.

**Tools** — mitre saw · tape · combination square · pencil · drill/driver ·
bits (7/64 pilot, 3/8 insert, countersink) · insert driver · clamps ×4 ·
sandpaper 120 + 180 · safety glasses · dust mask · brush.

**Also bring** — blue tape; a rag and denatured alcohol, both for squeeze-out
and for wiping the back of P1 before the foam goes on (it will not stick to a
dusty ACM face); and cardboard for the printed P1 mock-up.

## The three rules the book keeps repeating

1. **Cut P2 first, dry-fit, measure the real cavity.** Then cut everything else
   to what you measured. The tables are a prediction; the box is the truth.
2. **Pilot every hole.** Pine end grain splits, and the corner screws go into it.
3. **Seal all six faces**, inside included. A panel sealed on one side cups
   toward the unsealed one, and a cupped rear panel opens a gap at the face plate.
4. **The face plate never touches the monitor.** The P9 rails set the panel's
   position 1/8″ behind the ACM; the foam seal is 3/16″ thick and lands at 33 %
   compression. It is a light seal, not a clamp — see page 20.

## Not in the kit

The **monitor** — ungated, and it must survive a power cut and be matte.
The **Raspberry Pi and PSU**. The **mounting adapter**, still undesigned with
0.382″ of the ADA §307.2 budget left.

**Two things gate P1's release**, and both are cheap to clear:

1. The **⌀30.5 mm switch cutout**, against the datasheet of the switch you
   actually buy.
2. The **monitor's lit rectangle**, measured with a tape off a white screen.
   The window is now cut 3/16″ *smaller* than the picture so that no bezel shows,
   which means P1 can no longer be ordered before the monitor exists. Page 3.

The box itself is gated on neither. Buy the wood and start.
