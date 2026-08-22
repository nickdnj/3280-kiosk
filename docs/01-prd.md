# 3280 Kiosk — Product Requirements (PRD)

> **Status: CONCEPT / v1 requirements.** This defines the exhibit we're driving
> toward, not a shipped product. Requirements are the target the architecture,
> electronics, and mechanical work build against. Everything here is revisable
> as we measure the real machine and learn.

**Product:** An interactive kiosk built into the Vintage Computer Federation
museum's **Concurrent 3280** ("Cruncher 2"). A portrait screen behind a small
hinged door in the cabinet's front tells the machine's story; a docent (or
visitor) swings the door open to reveal the real card cage behind it. Operated
by **three physical buttons only — BACK / HOME / NEXT. No touchscreen.**

**Author:** Nick D. · **Team:** Software Project Team (AgentArchitect) ·
**Date:** 2026-08-22 · Supersedes the framing notes in `00-project-brief.md`.

---

## 1. Summary

The 3280 is a powerful mainframe **designed and built in New Jersey (1981–1986)**
and deployed everywhere — weather radar, spaceflight, defense, Wall Street. Today
it reads, to a passing visitor, as a beige box. This kiosk turns the machine's own
front panel into the exhibit label: a portrait screen where a small door used to
be, three buttons anyone can press, and the real hand-wired card cage a half-turn
of a hinge away.

The build spans three disciplines in one repo — **software** (the on-screen app +
a Raspberry Pi controller), **electronics** (Pi, display, buttons, power), and
**mechanical** (the hinged door, button placement, and reversible mounting into a
museum artifact). Mechanical is the highest-risk area and gets the most detail
below; electronics is a solved, low-risk problem for the builder and is specified
lightly on purpose.

---

## 2. Goals & success metrics

**Primary goal (the one that defines success):** make a general visitor
understand that *this* computer was designed and built in New Jersey and ran the
world — the **NJ-origin story** lands.

| # | Goal | How we'll know |
|---|------|----------------|
| G1 | The NJ-origin story lands with general visitors | Docent observation + visitor recall ("built in NJ"); the Home screen states it in one line |
| G2 | Visitors stop and interact, unattended | **Local, offline usage counts** (screens viewed, button presses per session) trend up vs. a static placard |
| G3 | Docents have a reliable tour aid | Docents choose to use it on tours; the swing-open reveal works every time |
| G4 | It runs unattended without babysitting | Days of museum-hours operation between any human intervention |

**Explicit non-metric:** this is not measured by dwell-time analytics infra or
online dashboards. Counts are local and reviewed occasionally (see §12).

---

## 3. Non-goals (v1)

- **Touchscreen / gestures.** Three (plus spare) physical buttons only.
- **Audio.** The piece is **silent** — no speakers, narration, or headphone jack.
- **Networked operation.** No live data, remote content push, or cloud analytics.
- **Multilingual.** English-only for v1 (revisit later).
- **A content-management UI.** Content is edited in the repo and rebuilt by the
  builder; no non-technical editor tool in v1.
- **Generalizing to other exhibits.** Built specifically for the 3280; reuse is a
  bonus, not a requirement.

---

## 4. Users & personas

- **Visitor (primary).** Walks up unattended, presses BACK/HOME/NEXT, reads a few
  screens. May open the door to look inside. No instructions, no staff needed.
  Range: kids to seniors; some seated/wheelchair users (see accessibility).
- **Docent (primary).** Uses it during a guided tour; swings the door open to show
  and narrate the real card cage. Wants it to always work and always reset clean
  for the next group.
- **Maintainer / builder (Nick).** Installs it, edits content via the repo and
  rebuilds, powers it on/off with the exhibit, and services it. Ownership
  transfers to the museum/docent team after ship (repo docs must support that).

---

## 5. Experience & interaction model

- **Three buttons, always the same:** **BACK** (previous screen), **HOME** (return
  to the summary/Home screen), **NEXT** (advance). No hidden modes.
- **Home screen** is a one-screen summary — *"This computer was designed and built
  in New Jersey,"* years **1981–1986**, "deployed everywhere," with the
  four-domain montage. It is both the entry point and the idle reset target.
- **The deck** is a short, curated sequence of screens (what it did → how it was
  built → who built it → the SGI Onyx cross-link → a look inside). Full size on the
  real display — there is **no tap-to-enlarge** on the installed piece (that was a
  review-app affordance; the physical screen is already full size).
- **Idle → auto-reset.** After a set idle timeout (no button press), the app
  returns to Home so the next visitor starts fresh (attract state).
- **"More detail" on a spare button.** One of the provisioned-but-unpopulated
  buttons is reserved for an optional deeper-dive on the current screen — Rick
  Lewis's "More" idea, kept within the no-touch model. **Not populated in v1**, but
  the software and wiring must not preclude it.
- **The reveal.** The door swings open (left hinge) and **holds itself open** so a
  docent has both hands free; the screen keeps running while open.

---

## 6. Content requirements (docent-set bar)

The content bar comes from docent review (Rick Lewis) and is a hard requirement,
not a style preference:

- **CR1** — ~30% of web-page copy; **3–5 short bullets per screen**, one strong
  graphic, big **sans-serif** type.
- **CR2** — Readable at **3–6 ft** standing distance.
- **CR3** — **Contextualize technical facts** for a general audience; no jargon dumps.
- **CR4** — **Verified exhibit facts only.** Cabinet imagery in the concept is AI
  concept art and is labeled as such; do not reuse the renders' hallucinated text.
- **CR5** — Keep the **SGI Onyx / MIPS R10000 cross-link** (Ken Yeager architected
  the 3280 here, then the R10000 that runs the Onyx on display), sourced only to
  public/placard-approved records.
- **CR6** — Carry the visible **"Concept"** marker until the piece is actually
  built and installed.

Content is authored in `src/kiosk-app/` (data + `build-app.py`) and edited by the
builder, versioned in git.

---

## 7. Software requirements

### Kiosk app (`src/kiosk-app/`)
- **FR1** — Runs **fullscreen, offline**, from local files; no network dependency.
- **FR2** — Navigable entirely by **BACK / HOME / NEXT** (and mapped keys for
  bench testing). No cursor, scrollbars, gestures, context menu, or OS chrome.
- **FR3** — **Idle timeout → return to Home** (attract reset); timeout configurable.
- **FR4** — **Local, offline usage counts** — per-session screen views and button
  presses persisted on the device; anonymous; reviewable later (see §12).
- **FR5** — Reserve a **"More detail"** action bound to a spare button; inert in v1
  but wired in the interaction model.
- **FR6** — Content is data-driven and **rebuildable** (`build-app.py`); no live
  editor required. Content is deployed on a **swappable USB drive**, separate from
  the stable OS/Chromium/controller core on the SD card — a content refresh never
  re-images the core (see architecture A2.5).
- **FR7** — Portrait layout; content legible per CR1–CR3 on the chosen panel.

### Controller (`src/controller/`, on the Pi)
- **FR8** — **Boot straight to kiosk**: power-on → display up → app fullscreen, no
  desktop, no login prompt visible.
- **FR9** — **Debounced GPIO** input for the three active buttons; the same code
  supports additional buttons without a rewrite (see ER/MR spare provisioning).
- **FR10** — **Watchdog / auto-restart**: if the browser or app crashes, it comes
  back to Home on its own.
- **FR11** — **Clean shutdown / power-loss tolerance**: survives the scheduled
  daily power-down and abrupt cuts without corrupting storage (read-only or
  overlay root FS strongly preferred, given FR4 writes).

---

## 8. Electronics requirements (builder's domain — specified lightly)

The builder has high confidence here; this section states intent, not a design.

- **ER1** — **Raspberry Pi** (4/5 class) drives a standard **monitor** over HDMI
  and reads the buttons over **GPIO** — off-the-shelf, cheap, replaceable.
- **ER2** — **Buttons wired to GPIO** with pull-ups/debounce; momentary contacts.
- **ER3** — **Provision GPIO + wiring for additional buttons** for future use
  (e.g. the "More detail" function). Only **three are populated/active in v1**; the
  spares are wired/available but not fitted.
- **ER4** — **Standard AC wall power**, powered on during museum hours (see NFR).
- **ER5** — **Silent** — no audio hardware.
- **ER6** — Deliverables when built: `bom.md`, wiring/pinout notes, and a short
  assembly/test note under `electronics/`.

---

## 9. Mechanical requirements (highest-risk — the focus of this PRD)

Grounded in the two concept renders (`assets/renders/kiosk-concept.jpg` closed,
`interior-open.jpg` open) and confirmed in the requirements interview. **The 3280
is a museum artifact — every attachment must be reversible and non-destructive.**

### Cabinet & datum
- **MR1** — Design to the real machine. Cabinet is nominally **23.0″ W × 69.5″ H**
  (from the concept); **all dimensions must be re-measured** on the actual machine
  before any part is cut. The interior exposes a top power/cable bay over **two 9U
  card cages** (slots 1–9 each).
- **MR2** — **Reversible mounting only.** Attach via clamps, existing fasteners/
  holes, the 19″ rack rails, or straddle/bracket methods — **no new holes,
  welds, adhesives, or finish damage** to the cabinet. Removal must leave the
  artifact as found.

### Front architecture
- **MR3** — **Small hinged kiosk door set within a larger fixed front frame.** The
  fixed frame spans the cabinet's front opening; the smaller door (screen +
  buttons) sits in the **upper-middle**, sized to **preserve viewing area around
  the display** (per the concept). The frame itself mounts per MR2.
- **MR4** — **Open framing, no glazing.** The interior around the door is open
  (no glass/acrylic viewing window). *Risk to manage (§11): with open framing +
  anyone-can-open, the vintage boards are exposed to touch, dust, and ESD.*

### The door
- **MR5** — **Left-side hinge**, swinging outward, matching the concept.
- **MR6** — **Holds itself open** at the working angle (detent, friction hinge, or
  stay/strut) so a docent has both hands free; must also **hold reliably closed**
  (friction/magnetic catch) without drifting. **Anyone may open it** — no lock in
  v1 — so the mechanism must tolerate frequent, untrained use.
- **MR7** — **Over-travel stop.** A hard stop prevents the open door (or its
  cabling) from striking or stressing the exposed boards.
- **MR8** — **Carries the screen and all three (plus spare) buttons.** Both display
  and button wiring therefore **cross the hinge** — see MR10.
- **MR9** — **Hinge load & balance** sized for the chosen panel plus the button
  plate and any door-mounted electronics, with margin for repeated cycling. Keep
  the door light: favor the smaller panel (see MR12) and consider mounting the Pi
  on the door so that **only power crosses the hinge** (see §13, open recommendation).

### Door enclosure (low-profile rear cover)
- **MR18** — The door is a **fully enclosed assembly**. A rear cover/shroud closes
  off the **back of the monitor, the Raspberry Pi, and the backs of the buttons**
  so no electronics, wiring, or bare panel are exposed from behind — nothing loose
  hangs off the door. The Pi mounts **inside** this shroud (so only power crosses
  the hinge — see MR10, §13).
- **MR19** — **As low-profile as possible.** Minimize the assembly's front-to-back
  depth (bezel face → rear cover) so the closed door sits as near flush as it can
  and preserves maximum closing clearance to the card cage behind it (MR3, MR7).
  The rear cover must be **removable/openable for service** (MR16) and **vented**
  so the enclosed Pi and panel don't overheat (MR14).

### Cabling across the hinge
- **MR10** — **Service loop + strain relief** across the left hinge for the
  conductor(s) that cross it (with the Pi on the door per MR18, this is just
  **power** — plus the spare-button harness only if any spare lives off-door),
  rated for the door's full open/close travel over many cycles; no pinch, no
  tension on connectors at either extreme.

### Buttons (mechanical placement)
- **MR11** — Buttons ride on the door **below the screen** (per concept), in a
  labeled plate (BACK / HOME / NEXT) matching the on-screen controls, with blanks/
  provision for the spare button(s). Placement must meet accessibility reach (§11).

### Display
- **MR12** — Target a **~24″-class 16:9 panel run in portrait** (~11.8″ × 20.9″
  active): light on the hinge, cheap, replaceable, and it holds the concept's
  "viewing area around the display" proportions in a 23″-wide cabinet. **~27″ is
  the stretch option** if the measured opening is generous. **Final size is
  confirmed after measuring the real opening (MR1).** Mount the panel so it can be
  serviced/replaced without remaking the door.

### Finish & aesthetics
- **MR13** — **Match the machine**: tan/cream frame and door to blend with the
  3280, **black screen bezel**, and a **"CONCURRENT" badge**, per the concept.
  Color-matching the vintage finish is an accepted challenge; a clean modern
  finish is the fallback if matching proves impractical.

### Thermal, safety, service
- **MR14** — **Ventilation** for the Pi and panel — the enclosed rear shroud
  (MR18) must be vented (passive preferred) so heat doesn't build up in the sealed
  door; no hot surfaces reachable by visitors.
- **MR15** — **Public-safety detailing**: no pinch points at the hinge, no sharp
  edges, nothing that tips or pulls off under a visitor's hand.
- **MR16** — **Serviceability**: the builder can reach the Pi, wiring, and panel
  for maintenance without removing the whole assembly from the cabinet.
- **MR17** — Deliverables when built: CAD (source + STEP), dimensioned drawings /
  cut files, and a `mounting.md` describing the reversible attachment and fit
  check, under `mechanical/`.

---

## 10. Non-functional / reliability

- **NFR1** — **Unattended reliability.** Runs a full museum day with no human
  intervention; recovers from app/browser crashes on its own (FR10).
- **NFR2** — **Power schedule.** Standard AC; **on during museum hours**, sleeps or
  powers down otherwise; clean startup and shutdown that protect storage (FR11).
- **NFR3** — **Robust to abuse.** Buttons and door survive constant, untrained
  public use; no input sequence can wedge the app or expose the OS.
- **NFR4** — **Maintainability & handoff.** A non-author can rebuild content,
  re-image the Pi, and re-open the door for service from the repo docs; ownership
  transfers to the museum.

---

## 11. Accessibility & safety

- **A1** — **ADA-reachable buttons.** Button plate placed within an accessible
  reach range for seated visitors and children (target the standard 15″–48″
  reach), balanced against the door's mid-cabinet position — resolve exact height
  in mechanical design; if the door-mounted position can't satisfy reach, a
  separate low button plate is the fallback.
- **A2** — **Legibility.** Big sans-serif type readable at 3–6 ft (CR1–CR2);
  sufficient contrast; no reliance on color alone.
- **A3** — **Simple, forgiving controls.** Three clearly labeled buttons; any
  visitor can reset to Home; idle auto-reset covers walk-aways.
- **A4** — **Physical safety.** Per MR7, MR14, MR15 — stops, ventilation, no pinch
  points or sharp edges, stable mounting.
- **Exposed-board risk (from MR4).** Open framing + anyone-can-open leaves the
  original boards reachable. **Planned mitigation (deferred, low cost):** add a
  **plexiglass panel behind/in the opening** to shield the boards while keeping
  them visible. Not in the initial build — added later as a cheap follow-on;
  signage and docent guidance cover the interim.

---

## 12. Analytics & privacy

- **P1** — Usage counts are **local, offline, and anonymous** — screen views and
  button presses only. No cameras, no personal data, no network transmission.
- **P2** — Data is stored on the device and reviewed occasionally by the
  maintainer (e.g. copied off on a service visit); it informs content, not people.

---

## 13. Constraints & assumptions

**Constraints**
- Museum artifact → **reversible, non-destructive** mounting (MR2).
- **Offline / standalone**, **silent**, **English-only**, **no touchscreen** (v1).
- Built **hands-on by the builder**.
- **Salvage-first.** Most parts — the monitor, compute, buttons, brackets/rack
  hardware, panel stock — are **salvaged from the VCF warehouse and reused**. Buy
  new only what can't be salvaged. This favors adaptable, standards-based choices
  over anything that assumes a specific new SKU.

**Assumptions (flag to correct)**
- **Budget:** not a constraint — "don't worry about it"; salvage-and-reuse keeps
  cost low regardless. Build it right.
- **Timeline:** no hard deadline — build it right; "done" = the **full piece
  installed** in the real 3280 (not a bench demo).
- **Reliability:** unattended, auto-recovering, power-cycle-safe is required.

**Settled by the enclosure requirement**
- The **Pi mounts inside the door's rear shroud** (MR18), so only **power crosses
  the hinge** (MR10) — no HDMI/USB/button harness across it. Confirm against MR9
  hinge balance and MR16/MR19 serviceability during design.

---

## 14. Phasing / milestones

"Done" is the installed piece, but the build sequences to retire risk early:

1. **Content lock** — finalize the screen deck to the CR bar; app runs fullscreen
   on a plain monitor, button/key driven, with idle reset + local counts (FR1–FR7).
2. **Measure the machine (MR1)** — real cabinet/opening dimensions; confirm panel
   size (MR12) and mounting approach (MR2).
3. **Electronics bring-up** — Pi + monitor + buttons on the bench; boot-to-kiosk,
   watchdog, power-safe imaging (FR8–FR11, ER1–ER5).
4. **Mechanical build** — fixed front frame, hinged door, button plate, cabling,
   reversible mount; finish to match the machine (MR3–MR17).
5. **Integration & install** — assemble into the 3280, fit check, docent walkthrough,
   safety/reversibility sign-off with VCF.

---

## 15. Open questions

1. **Confirm panel size** after measuring (MR1/MR12): 24″ vs 27″ portrait — also
   sets the door depth / how low-profile the enclosure can go (MR19). Driven by
   what monitor is available to salvage.
2. **Reversible mount method** — what does the real cabinet offer to grab (rack
   rails, existing holes, frame lip)? Determined on measurement.
3. **Spare-button count** to provision (MR11/ER3) — how many beyond the three?
4. **ADA reach vs door position** (A1) — does the door-mounted button plate meet
   reach, or do we need a separate low plate?

*Resolved since first draft: budget is not a constraint; exposed boards get a
plexiglass panel later (MR4/§11); the Pi mounts in the door shroud (MR18).*

---

*Next in the flow: architecture (`docs/02-architecture.md`) — platform, boot/kiosk
stack, button→app transport, and the mechanical approach that carries MR2–MR17.
Say "let's do the architecture" when ready.*
