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

| Dimension | OEM spec | Our assumption | ME-1 measured |
|---|---|---|---|
| **Height, overall (floor → top)** | **71″** | 69.5″ | ✅ reconciles — see §1.1 |
| **Height, cabinet box only** | — | — | **67-7/8″** |
| **Base / feet height** | — | 8.0″ ❌ | **≈ 3-1/8″** (derived) |
| **Width** | **24″** (61 cm) | 23.0″ | ≈ 23–24″ ✅ |
| **Depth** | **34″** (86.4 cm) | 26–36″ (unknown) | not measured |
| Footprint | ≈ 5.7 ft² / 0.53 m² | — | — |

### 1.1 Height discrepancy — RESOLVED

**There was never a conflict.** Confirmed 2026-08-27: the 67-7/8″ tape reading is
the **cabinet box alone**. The machine sits on feet below that.

```
      71″     OEM overall height (floor → top of cabinet)
  −  67-7/8″  measured cabinet box
  ─────────
  =   3-1/8″  feet / base
```

3-1/8″ is a wholly plausible foot height, and the two independent figures — a
1989 catalogue and a tape measure in a warehouse — closing to an exact eighth is
strong mutual confirmation. **Both numbers are good.** Use 71″ for floor-relative
work (ADA, sightlines, install) and 67-7/8″ for anything referenced to the box.

⚠️ The 3-1/8″ is *derived*, not measured. Put a tape on the feet to confirm, and
note whether they're fixed feet, levellers or casters — levellers would make the
overall height adjustable by an inch or so.

The figure on p.74 labels the primary cabinet **"71″ CABINET OPTION / STANDARD OR
PERIPHERAL PRIMARY CABINET"** — the word *option* implies other heights existed.
Concurrent definitely shipped multiple cabinet heights in this era; the 1986
Datapro report notes the XF/600 was offered in *"either a 30-inch or 56-inch high
cabinet."*

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
- Floor → aperture bottom (ADA) — though the base height now gives us a datum.
- Foot height, measured rather than derived; fixed / levelling / casters.

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
