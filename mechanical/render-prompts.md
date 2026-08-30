# Image-generation prompts — kiosk concept renders

> ⚠️ **Concept art.** Anything produced from these is a *visualisation of the
> target*, not a photograph of a built object. Label it that way wherever it is
> used, per the project's concept rule.

Proportions below are derived from [`fab-rev1/_p1.py`](fab-rev1/_p1.py). Image
models follow **percentages and ratios** far better than inch dimensions, so
every prompt states both.

**The single most important line in all of these: the kiosk is exactly twice as
tall as it is wide.** If a render comes back squarer than that, it is wrong and
everything else about it will look wrong too.

---

## Shared spec — paste this at the top of any of the four prompts

```
SUBJECT: a small wall-mounted interactive museum kiosk. Self-contained
rectangular enclosure. NOT a tablet, NOT a touchscreen, NOT a floor-standing
totem.

PROPORTIONS — follow these exactly:
- The enclosure is 15 inches wide by 30 inches tall by 3-5/8 inches deep.
- It is EXACTLY TWICE AS TALL AS IT IS WIDE. A precise 1:2 rectangle.
- Depth is about a quarter of the width — a shallow slab, not a box.
- Corners are softly rounded, radius about 1.7% of the width. Nearly square.

MATERIALS:
- Front face: matte black aluminium composite panel, 3 mm, CNC routed.
  Dead flat, completely non-reflective, fine even satin texture. No gloss,
  no mirror, no highlights. Crisp machined edges.
- Body: solid pine, painted satin black, faint wood grain readable through
  the paint under raking light.
- Fasteners: small black button-head machine screws, flush.

LIGHTING AND CAMERA: soft even studio light, one large softbox front-left and
a subtle fill right. Neutral seamless mid-grey background. Straight-on
orthographic framing, camera centred on the object, no perspective distortion,
no wide angle. Sharp throughout. Photorealistic product photography.

DO NOT INCLUDE: any logo, brand mark, lettering or label on the enclosure;
any glossy or reflective surface; a touchscreen; more or fewer than three
buttons; visible cables; visible seams other than those described; people;
a floor stand or pedestal.
```

---

## 1 · FRONT

```
[paste the shared spec, then:]

FRONT VIEW, straight on.

A matte black rectangular face plate fills the whole front, 15 x 30 inches,
exactly twice as tall as wide.

SCREEN OPENING: a single portrait rectangular cutout, 82% of the enclosure
width, centred left to right with equal 9% margins. Its top edge sits 5% down
from the top of the enclosure; its bottom edge sits 24% up from the bottom.
Behind it, a portrait computer monitor is visible and switched on — the black
screen surface sits about 1/8 inch behind the face plate, so the opening reads
as a clean machined window with a shallow shadowed reveal, not a bezel.

WHAT IS ON THE SCREEN: a portrait museum exhibit page. Large white sans-serif
headline across the upper third, three or four short lines of white body text
below it, generous spacing, near-black background. Softly self-illuminated,
legible, not blown out. Keep the text generic and unreadable at small size.

BUTTONS: exactly three round pushbuttons in a horizontal row low on the face,
below the screen opening. Centreline sits 13% up from the bottom of the
enclosure. They are 30 mm brushed stainless steel anti-vandal buttons —
diameter about 8% of the enclosure width — with flush domed heads and a thin
knurled ring where each meets the panel. Spacing between centres is 23% of the
width, so the outer two sit well inboard of the edges. All three identical and
unlabelled.

SCREWS: fifteen very small black button-head screws around the perimeter of
the face plate, set 3% in from the edge — five evenly spaced down each long
side, one top centre, one bottom centre, and a row of three just above the
buttons. Subtle, flush, easy to miss.
```

---

## 2 · BACK

```
[paste the shared spec, then:]

REAR VIEW, straight on.

The back of the same 15 x 30 inch enclosure — again exactly twice as tall as
wide.

A satin black painted solid pine frame about 3/4 inch wide runs around the
whole perimeter. Set INSIDE it and slightly RECESSED is a flat rear panel of
1/2 inch MDF, painted the same satin black, with a fine uniform surface and no
grain. The recess is shallow — about 1/2 inch — and reads as a clean deliberate
step with a soft shadow line, not a gap.

FASTENERS: six small knurled black thumbscrews holding the rear panel to the
frame — three evenly spaced down each long side, none top or bottom. Knurled
heads standing slightly proud, clearly meant to be turned by hand.

ONE OPENING ONLY: a small rectangular fused IEC C14 power inlet, low on the
rear panel and slightly left of centre, black, flush-mounted, with its three
recessed pins visible.

Otherwise the back is completely plain. No vents, no labels, no cables, no
brackets, no other holes.
```

---

## 3 · SIDE

```
[paste the shared spec, then:]

SIDE VIEW (left profile), straight on.

A tall narrow slab. The silhouette is 30 inches tall and only 3-5/8 inches
deep — a depth-to-height ratio of about 1:8. Emphasise how SHALLOW it is: this
is a flat panel with a little depth, not a cabinet.

Reading front to back across that 3-5/8 inches:
- At the very front, a crisp 1/8 inch black edge — the aluminium composite
  face plate, its machined edge catching a thin highlight.
- Then the painted satin black pine body making up nearly all the depth, with
  faint wood grain showing through the paint under raking light.
- At the very back, a fine shadow line where the recessed rear panel sits.

Softly rounded vertical corners top and bottom. No fasteners visible from
this angle. No mounting hardware — the back is flat and bare.

Light it from the front-left so the front edge and the body separate clearly
and the shallow depth is unmistakable.
```

---

## 4 · INSTALLED IN CONTEXT (optional, and the most useful one)

```
[paste the shared spec, then:]

THREE-QUARTER VIEW of the kiosk mounted on the front of a large vintage
minicomputer cabinet, in a museum gallery.

THE CABINET behind it: a 1970s-80s minicomputer, about 6 feet tall, 2 feet
wide and just under 3 feet deep. Beige-tan textured factory paint, slightly
aged. A tall louvered front door with fine horizontal vent slots. Plain,
industrial, no visible branding. It stands on the floor on a low plinth.

THE KIOSK is mounted flat on the closed front door of that cabinet, centred
left to right, its bottom edge about waist height — 34 inches above the floor,
so the buttons fall at 38 inches. The kiosk occupies roughly the middle of the
cabinet's height, with the tan machine clearly visible above and below it.
The kiosk is visually subordinate: the historic machine dominates the frame.

The kiosk's screen is on, showing a portrait exhibit page with large white
text on near-black.

Museum lighting: soft overhead, gentle falloff, a polished concrete or
plain floor. A neutral gallery wall behind. Photorealistic, eye-level camera
at about 6 feet away, slight angle from the left. No people.
```

---

## Notes

**If the model gets the proportion wrong** — and it usually will on the first
try — reply with only this: *"The enclosure must be exactly twice as tall as it
is wide, a precise 1:2 rectangle. Regenerate with that corrected and everything
else unchanged."*

**Finish colour is not decided.** These prompts assume satin black throughout,
which makes the kiosk read as one object. Two alternatives worth rendering
before anyone commits — it is a curatorial call, not an engineering one:

- *Tan body:* replace every "satin black painted solid pine" with **"beige-tan
  painted solid pine, matching the vintage cabinet behind it"**. The box
  disappears into the machine and only the black face and screen read.
- *Natural wood body:* replace it with **"natural pine with a clear satin
  finish, warm and lightly grained"**. Reads as deliberately maker-built.

The face plate stays matte black in all three — that part is ordered.
