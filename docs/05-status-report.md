# 3280 Kiosk — Project Status Report

**As of 2026-08-28** · repo [nickdnj/3280-kiosk](https://github.com/nickdnj/3280-kiosk)
· written as a **handoff for a team joining in parallel**

---

## 0. Read this first

An interactive exhibit kiosk built into the Vintage Computer Federation's
**Concurrent 3280** minicomputer. A portrait screen where the machine's door is,
driven by **three physical buttons — BACK / HOME / NEXT. No touchscreen.**

**Phase:** planning complete, execution barely started. 39 GitHub issues, **0
closed**. One site visit done.

**The single most important thing to know:** the machine is **not** what the
concept art shows. Roughly half the mechanical documentation in this repo was
written before we measured it and is **superseded**. §6 tells you exactly which
files to ignore. Read that before you read anything else in `mechanical/`.

**Everything mechanical is blocked on one unmeasured dimension** (§5). Everything
in the **software track is unblocked, untouched, and safe to work in parallel**
(§8).

---

## 1. The product

A docent or visitor steps through a short deck of screens telling the machine's
story. Swing the display open and the real hardware is behind it.

| | |
|---|---|
| Interaction | 3 buttons only. No touch, no keyboard, no network dependence |
| Display | Portrait, ~27″ |
| Compute | Raspberry Pi 4, Chromium kiosk, offline in production |
| Content bar | ~30% of web copy, 3–5 bullets/screen, big sans-serif, readable at 3–6 ft, verified facts only |
| Hard constraint | The 3280 is a **museum artifact** — all mounting reversible, non-destructive |
| Success | Ownership transfers to the museum. "Nick-in-the-loop forever" = failure |

Docent review (Rick Lewis) set the content bar and approved the concept:
*"YES YES YES. This is just the job."* That approval was against art that has
since turned out to misrepresent the machine — see §7.

---

## 2. What we know about the machine

**Provenance matters here.** Four different confidence levels:

### Measured — tape on the machine, 2026-08-26

| Dimension | Value | Confidence |
|---|---|---|
| Cabinet **box** height (excl. feet) | **67-7/8″** | Good |
| Front opening, clear width | **~19.75″** (19.5–20) | Good |
| Outer door width | ~23–24″ | Poor — couldn't see both tape ends |
| Two vertical runs | ~48″ and ~32″ | Readings clear, **what they span is unknown** |

### OEM — Concurrent *3280/Micro3200 Product Overview*, 50-045R00, Aug 1989, pp.73–74

| | |
|---|---|
| Cabinet | **71″ H × 24″ W × 34″ D**, ≈5.7 ft² |
| Internal stack | power → fan → CPU + 18 S-bus slots → intermediate duct → I/O chassis → fan |

Height reconciles exactly: **67-7/8″ box + 3-1/8″ feet = 71″**. A 1989 catalogue
and a warehouse tape agreeing to an eighth is strong mutual confirmation.

### Sibling model — Perkin-Elmer 3230 *Installation & Maintenance*, 47-004 R21, 1982, ch.3

The 3230 is a 56″ rack, not our 71″ cabinet — **family evidence, not gospel.**

| | |
|---|---|
| **19″ EIA rack** | Panel space 1292 mm (50.87″) × **482.6 mm (19.00″)**; 28″ upright-to-upright |
| Door | Part **13.045 F01**, 54.32″ × 24.3″, two spring latches at top, foam gasket, vertical louvers |
| **Paint** | **P.E. #464 TEXTURED** — factory spec. Texture matters as much as hue |
| Materials | CRS .104″ structure, .047″ skins |
| Cooling | Bottom blower 450 CFM, right-side plenum, five removable covers (solid / perforated) |

### Derived — from a uniform frame offset (working assumption, 2026-08-27)

```
frame offset = (24.00 − 19.75)/2 = 2.125"  uniform on all four sides
aperture     = 19.75" × 63.625"    (5.25" – 68.88" AFF)
door         = 24.30" × 68.175"    (2.98" AFF), 0.15" overhang all round
```

Self-consistent: door height 68.175″ = box 67.875″ + 2 × 0.15″, *the same
overhang the door has in width*. Two independently sourced numbers agreeing.

### Not known

- **C1 — the closing clearance.** See §5. This is the blocker.
- What the 48″ and 32″ readings measure
- Hinge type and spacing; latch mechanism
- Whether rack rails are present with a free run
- Floor → aperture bottom, confirmed rather than derived

---

## 3. The finding that changed the project

**The 3280 has two doors. There is no open card cage.**

- **Outer:** tan **louvered** door, hinged, dark trim strip, "SYSTEM #1" label
- **Inner:** **perforated zinc-plated steel** panel on a piano hinge
- **Behind:** the card cage, with Concurrent power-supply modules down one side

Every drawing produced before the site visit shows an **open front opening with a
visible card cage** and a fixed frame spanning it. **That geometry does not
exist** — the AI concept render invented it.

Consequences:

- **Mounting is solved.** Remove the outer door, store it, hang the kiosk panel
  on its hinges. More reversible than clamping rails or gripping a frame lip,
  because a cover door is *built* to come off. ME-2 and ME-3 (reversible mount,
  fixed frame) largely collapse.
- **Exposed-board risk is moot.** The boards already sit behind perforated steel.
  ME-10 / the deferred plexiglass is unnecessary.
- **MR3 breaks.** "Viewing area around the display" meant seeing the machine
  around the screen. There's a steel panel there. Partially recovered by a
  **viewing cutout in the lower third** of the door — it's 68″ tall, so there's
  room. **This is a docent decision, not an engineering one.**

---

## 4. The design as it stands

```
Remove the outer louvered door  →  store it
Carrier panel (24.30" × 68.175") hangs on the original hinges
  ├── 27" IPS 1440p matte monitor, cased, portrait, VESA 100×100
  ├── button plate below — 3 buttons + 2 spare blanks, centre 34" AFF
  ├── viewing cutout, lower third
  └── Raspberry Pi 4 behind the monitor
```

Screen centre ≈ **49″ AFF**. Buttons at 34″ AFF sit mid-band in the 15″–48″ ADA
reach range.

### Decisions, including the ones we reversed

| Decision | Reversed from | Why |
|---|---|---|
| **Cased monitor, kept whole** | De-cased bare LCD panel | De-casing is one-way and risks a good panel. A cased monitor is **docent-replaceable**, and its own housing solves the enclosure and thermal requirements |
| **27″** | 24″ | The door is 24.3″ wide, not the 14.5″ we'd assumed. A 24″ portrait panel is 12.5″ — 51% of the door |
| **Replace the existing door** | Fabricate a fixed frame | The machine already has a hinged, removable door of the right size |
| **1 panel or none to fabricate** | 4-part laser-cut aluminium package | Cascade of the above |

**27″ specifically:** IPS is near-mandatory (visitors approach off-axis, and 32″
is often VA); 1440p is 109 PPI and a Pi 4 rotates it comfortably where 4K is
sluggish; ~12 lb on original hinges vs ~17 lb for 32″.

### Two easily-missed selection criteria

1. **The monitor must power itself back on after a mains cut.** The exhibit runs
   on an AC timer. Many monitors wake into standby — that's a black screen every
   morning. **Go/no-go.**
2. **Matte only.** Museum lighting mirrors off glossy panels.

---

## 5. The blocker

**C1 = distance from the outer door plane to the inner perforated panel.**

Required: **≥ 2.48″** (carrier panel 0.125 + monitor body 1.85 + 0.5 clearance).

Not measured. No catalogue carries it. It decides **recessed vs. proud**
mounting — and the proud variant needs almost none, so a bad C1 doesn't kill the
project, it just changes how it looks.

Measure it at top, middle and bottom of the aperture and design to the smallest.

**Also worth one tape each:** the door height (confirms §2's derivation), the
foot height (currently derived), and whether rack rails have a free run.

---

## 6. ⚠️ Repo map — current vs. superseded

**Roughly half of `mechanical/` is obsolete but still present.** Do not build
from the right-hand column.

### Current

| File | What it is |
|---|---|
| `mechanical/me1-findings.md` | **The site visit. Read first.** |
| `mechanical/monitor-selection.md` | Why 27″, with the fit maths |
| `mechanical/cabinet-spec-oem.md` | Concurrent's published cabinet spec |
| `mechanical/cabinet-drawings-3230.md` | Perkin-Elmer mechanical drawings, sibling model |
| `mechanical/drawings/01…07` | Full drawing set, measured geometry |
| `mechanical/drawings/make-drawings.py` | **Generates 01–06 from one geometry block.** Edit params, re-run |
| `mechanical/measurement-checklist.md` | Field sheet; C1 and door height are what's left |
| `mechanical/photos/` | Site photographs |
| `docs/00`–`04` | Brief, PRD, architecture, UX, dev plan — **still broadly valid** |
| `src/kiosk-app/` | Working concept app + builder. **Untouched, valid** |

### Superseded — ignore

| File | Why |
|---|---|
| `mechanical/dimensions-assumed.md` | Pre-measurement guesses. Wrong cabinet, wrong door |
| `mechanical/door-construction.md` | De-cased-panel build spec. Obsolete route |
| `mechanical/fab/` (DXFs, generator, DRAWING-PACKAGE.md) | 4-part laser-cut package for a door we're no longer building |
| `mechanical/enclosure-buy-vs-build.md` | Moot — the cabinet supplies the enclosure |
| `mechanical/display-approach-options.md` | Decision made (Option C). Historical |
| `mechanical/drawings/superseded/` | Pre-measurement drawings |

**Also stale:** the 39 GitHub issues were written against the pre-measurement
plan. **ME-2, ME-3, ME-10 are likely moot; ME-4 changed completely.** Nobody has
reconciled the issue list with §3–§4 yet — *that is itself available work.*

---

## 7. Traps

Things that already cost us time:

1. **The AI concept renders are wrong about the machine.** They show an open card
   cage that doesn't exist, and dimensions off by 1–1.5″. They're flagged as
   concept art throughout, but they drove real design decisions for days.
2. **We designed a 14.5″ door for a 19″ opening** when the actual usable face is
   a 24.3″ door. Everything downstream — monitor size, panel layout, fab package
   — inherited that error.
3. **A measurement can be right and still mislead.** The 67-7/8″ height looked
   like it contradicted the OEM's 71″. It didn't — one was the box, one included
   the feet. Always ask *what* was measured, not just the number.
4. **Sibling-model documentation is not the machine.** The 3230 data is good
   evidence and clearly labelled as such, but it's a 56″ rack, not our 71″ cabinet.

---

## 8. Work available in parallel

The **software track is completely untouched and completely unblocked.** It has
no dependency on the cabinet, the monitor choice, or C1.

### Safe to take — no collision

| Issue | Story |
|---|---|
| #2 SW-A1 | Split the screen deck out of `build-app.py` into a `content.json` data file |
| #3 SW-A2 | Encode the 8-screen deck (UX §4) in that data file |
| #5–8 SW-B | Kiosk runtime: fullscreen/no chrome, key nav, idle→Home reset, "more" scaffolding |
| #12–17 SW-D | Pi OS image: boot-to-kiosk, read-only root, USB content mount, watchdog, golden image |
| #18–19 SW-E | Usage logging + summary |
| #9–11 SW-C | GPIO service, uinput key mapping — needs a Pi and buttons, not the cabinet |

`src/kiosk-app/` is a **real working app** (`build-app.py` emits a self-contained
`index.html`). Content is currently hardcoded in the Python; SW-A1 is the natural
first task and unblocks everything else in the deck.

### Do not take — actively in flight

- `mechanical/` and `mechanical/drawings/` — being reworked as measurements land
- Anything gated on C1
- Reconciling the GitHub issue list is *available* but coordinate first, since
  it touches the same milestones

### Conventions that matter

- **Commit only files you changed** — `git add <paths>`, never `git add -A`
- Docs-first: PRD → architecture → UX → dev plan → issues → build
- No demo fallback: show error states, not demo data
- Everything is labelled **concept** until built and installed
- Authoritative knowledge base is the wiki at `~/Workspaces/wiki/`
  (`projects/concurrent-3280-museum/`); propose changes via wiki-ingest, never
  write it directly

---

## 9. Sources

- Concurrent, *3280 and Micro3200 Families Product Overview*, 50-045R00, Aug 1989 —
  [bitsavers](https://bitsavers.org/pdf/interdata/32bit/3280/50-045R00_3280_ProdOverview_1989.pdf)
- Perkin-Elmer, *Model 3230 Processor Installation and Maintenance Manual*,
  47-004 R21, 1982 —
  [bitsavers](https://bitsavers.org/pdf/interdata/32bit/3230/47-004R21_3230_Maint_1982.pdf)
  ([OCR text](https://archive.org/stream/bitsavers_interdata30Maint1982_46790039/47-004R21_3230_Maint_1982_djvu.txt))
- Datapro, *Concurrent Computer Corporation Supermini Systems*, M11-230-101, Feb 1986 —
  [bitsavers](http://bitsavers.org/pdf/datapro/datapro_reports_70s-90s/Concurrent/M11-230-10_8602_Concurrent_3200.pdf)
- Site photographs, 2026-08-26 — `mechanical/photos/`
- Docent concept review — the shared artifact, updated 2026-08-27

---

*Written 2026-08-28. The machine in the warehouse is the authority; where this
document and the machine disagree, the machine wins.*
