# OEM Cabinet Specification — Concurrent 3280MPS

**Source:** Concurrent Computer Corporation, *3280 and Micro3200 Families Product
Overview*, publication **50-045R00, August 1989**, Chapter 4 — "The 3280MPS
Multiprocessor / Physical Profile", pages 73–74.
Archived at [bitsavers](https://bitsavers.org/pdf/interdata/32bit/3280/50-045R00_3280_ProdOverview_1989.pdf).

This is **manufacturer data, not a field measurement.** It tells us what
Concurrent shipped; [`me1-findings.md`](me1-findings.md) records what's actually
in the warehouse. Where they disagree, the machine wins.

---

## 1. The numbers

> *"Regardless of an individual configuration, the 3280MPS always starts with a
> processor/S-bus cabinet. This cabinet is 71″ tall and houses power and cooling
> assemblies and upper and lower PC board chassis."* — p.73

> *"Each of these cabinets is 71″ tall."* (of the expansion cabinets) — p.74

| Dimension | OEM spec | Our assumption | ME-1 photo read |
|---|---|---|---|
| **Height** | **71″** | 69.5″ | ≈ 67-7/8″ ⚠️ |
| **Width** | **24″** (61 cm) | 23.0″ | ≈ 23–24″ |
| **Depth** | **34″** (86.4 cm) | 26–36″ (unknown) | not measured |
| Footprint | ≈ 5.7 ft² / 0.53 m² | — | — |

The figure on p.74 labels the primary cabinet **"71″ CABINET OPTION / STANDARD OR
PERIPHERAL PRIMARY CABINET"** — the word *option* implies other heights existed.
Concurrent definitely shipped multiple cabinet heights in this era; the 1986
Datapro report notes the XF/600 was offered in *"either a 30-inch or 56-inch high
cabinet."*

### ⚠️ The height doesn't reconcile — and that matters

**71″ (OEM) vs ≈67-7/8″ (my read of your tape).** A 3-1/8″ gap is too large to be
rounding and too small to be a different cabinet family. Most likely one of:

1. **I misread the photo** — the tape is at an angle in a rotated frame. Most likely.
2. **The tape wasn't hooked at the floor** — e.g. measured from the top of a
   plinth or levelling base. A ~3″ base reconciles it almost exactly.
3. **A genuinely different cabinet option.**

**Re-measure floor → top, and this closes.** Until then, treat 71″ as the
catalogue value and ~68″ as unverified.

---

## 2. Internal layout (p.73, figure 045-39)

Top to bottom in the processor/S-bus cabinet:

```
  POWER
  FAN ASSEMBLY
  CPU  |  18 S-BUS SLOTS
  INTERMEDIATE DUCT
  I/O CHASSIS  (20-slot / 12-slot / 8-slot options)
  FAN ASSEMBLY
```

**This explains the louvered doors.** Fan assemblies top *and* bottom with an
intermediate duct between the chassis means the cabinet is a vertical air
plenum — the louvers are the intake/exhaust path, and the perforated inner door
is part of the airflow design, not just a guard.

Two consequences for us:

- **A solid kiosk panel in the outer door aperture blocks that path.** Irrelevant
  for a static exhibit, but it should be written down in case VCF ever powers the
  machine — and it argues for keeping the original louvered door rather than
  discarding it.
- The **"intermediate duct"** band between the upper and lower chassis is a
  horizontal structural element at roughly mid-height. Worth locating on the real
  machine — it may be exactly where a display panel wants to sit, or exactly
  where it can't.

---

## 3. What this does and doesn't settle

**Settles:**
- Cabinet width ≈ **24″** — our 23″ assumption was 1″ light, and the ME-1 photo
  agrees with the catalogue.
- Cabinet depth **34″** — first hard number we've had. Plenty of room behind any
  door-mounted display.
- Why the machine has louvered and perforated doors.

**Does not settle — still needs the tape:**
- **C1**, the outer-door-plane to inner-door clearance. No catalogue gives this.
- Door aperture height and width.
- Floor → aperture bottom (ADA).
- The 71″ / 68″ discrepancy.

---

## 4. Other documents worth pulling

From [`bitsavers.org/pdf/interdata/32bit/`](https://bitsavers.org/pdf/interdata/32bit/):

| Path | Why |
|---|---|
| `3280/50-045R00_3280_ProdOverview_1989.pdf` | This document — 110 pp |
| `3280/63-002_SystemBusTheory_1987.pdf` | S-bus theory; unlikely to have mechanicals |
| `3230/47-004R21_3230_Maint_1982.pdf` | **45 MB maintenance manual.** Maintenance manuals usually *do* carry cabinet drawings, door removal, and dimensioned service clearances. Best remaining lead for real cabinet geometry |
| `3203/`, `3205/`, `3210/`, `3220/`, `3250/` | Sibling models — may share the cabinet |

A **site-planning or installation manual** would give C1-class detail directly.
None is on bitsavers under these paths; if one surfaces it supersedes this page.

---

*Recorded 2026-08-27. Manufacturer data — the machine in the warehouse is the
authority.*
