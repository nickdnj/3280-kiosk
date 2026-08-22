# Concept Render Prompts

Paste-ready image-generation prompts for the display-approach options
([`../display-approach-options.md`](../display-approach-options.md)). Written for
ChatGPT, but they work in any image model that takes long prompts.

> ⚠️ **Whatever comes back is concept art, not a drawing.** Do not measure off
> it, and do not reuse any text the model invents on the screen or the cabinet —
> that rule has been in force since the first renders (see the project brief).
> These images are for showing docents what an approach *feels* like.

---

## C2 — monitor proud, door closed

```
Create a photorealistic industrial-design concept render, straight-on front
elevation, of a vintage minicomputer cabinet with a modern kiosk display
mounted on it.

THE CABINET
A 1980s Concurrent 3280 minicomputer cabinet, standing on the floor,
approximately 23 inches wide and 69.5 inches tall — tall, narrow and
rectangular. Painted cream-tan steel with a slightly overhanging top cap and a
solid plinth at the base on four small black leveling feet. The middle of the
front is a tall recessed opening running most of the cabinet's height, revealing
the machine's interior: a dense card cage of vertical circuit boards seen
edge-on, with visible card guides, ribbon cables and colored components. The
paint is subtly aged — a museum artifact in good condition, not pristine.

THE KIOSK — this is the focus
Mounted in the upper-middle of the front opening is a flat cream-tan panel about
15 inches wide and 29 inches tall, the same color as the cabinet. It is hinged on
its LEFT edge with two visible dark hinge barrels, and is currently closed.

Bolted to the FRONT face of that tan panel — standing proud of it by about two
inches, clearly sitting on top of the panel rather than set into it — is a modern
commercial LCD computer monitor in its own matte black plastic housing, rotated
to PORTRAIT orientation. Thin black bezel, a slightly deeper chin at the bottom,
no brand markings. It casts a soft drop shadow onto the tan panel behind it,
making the mounting depth obvious.

Directly below the monitor, on the tan panel, is a black rectangular control
plate about 12 inches wide and 4 inches tall carrying exactly THREE round
physical arcade-style buttons in a row: a left-arrow, a house icon, and a
right-arrow, labelled BACK, HOME and NEXT in small clean sans-serif capitals.
There is no touchscreen — the three buttons are the only controls.

The card cage remains visible above and below the tan panel, so the machine's
interior frames the display.

SCREEN CONTENT
Keep the screen simple and legible: a warm off-white background with one short
bold sans-serif headline and three or four short bullet lines. Do not invent
technical specifications, dates, model numbers or paragraphs of text.

STYLE
Product-photography concept render. Neutral light-grey seamless background, soft
even studio lighting, gentle contact shadow on the floor, sharp focus, straight-on
eye-level camera with no perspective distortion, entire cabinet in frame with
margin around it. Clean, editorial, museum-exhibit-proposal feel.

DO NOT INCLUDE
No people, no keyboard or mouse, no additional screens, no brand logos or
watermarks, no touchscreen gestures, no cables draped across the front, no text
anywhere on the cabinet itself.
```

---

## C2 — door open, revealing the card cage

Run this second. It shows the feature the whole exhibit exists for.

```
Same cabinet, same tan panel with the portrait monitor bolted to its front and
the three-button BACK/HOME/NEXT plate below it — but now the panel is SWUNG OPEN
about 100 degrees on its left hinges, like a door, projecting toward the viewer
and to the left.

The camera is slightly to the right of straight-on so the opened panel is seen at
an angle and the newly exposed interior is clearly visible: the full card cage
behind it, rows of vertical circuit boards, card guides, ribbon cables. The back
of the tan panel is visible and tidy — a small single-board computer on
standoffs, one slim cable running through the hinge side, nothing loose or
dangling.

Same lighting, background and style as before. No people, no invented text.
```

---

## Adapting to the other options

Change only the kiosk paragraph:

**C1 — monitor recessed.** Replace "bolted to the FRONT face… standing proud" with:

> *set INTO a rectangular cutout in the tan panel so the monitor sits flush
> behind it and only the screen and a thin black bezel are visible — the display
> reads as built into the panel, not mounted on it. No drop shadow on the panel.*

**A — custom door (the approved concept).** Replace it with:

> *a tan door with a black bezel surrounding a portrait screen, a small dark
> CONCURRENT badge at the top left, and the three-button plate below — the
> display is fully integrated into the door, which is the same cream-tan as the
> cabinet.*

---

## Getting a usable result

- **Ask for the straight-on elevation first.** Perspective views hide the
  proportions that matter.
- **Iterate on one thing at a time** — "make the monitor stand further proud,"
  "make the tan match the cabinet exactly," "show more card cage below."
- **The model will get the cabinet proportions wrong.** It's illustration. The
  honest geometry lives in
  [`06-option-comparison.svg`](06-option-comparison.svg).
- Save what you use to `src/kiosk-app/assets/renders/` and flag it as concept art.
