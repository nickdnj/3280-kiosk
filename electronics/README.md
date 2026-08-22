# Electronics — the kiosk's electrical hardware

Everything that carries a signal or a volt in the kiosk: the three buttons, the
display, the single-board computer, power, and the wiring that joins them.

## Scope

- **Buttons.** Three arcade/industrial momentary pushbuttons (BACK / HOME /
  NEXT), their harness, and pull-up/debounce approach.
- **Display.** Portrait panel — model, interface (HDMI/DSI), power, backlight,
  brightness for museum lighting.
- **Compute.** SBC selection, storage, and how it drives display + reads buttons
  (see `../src/controller/`).
- **Power.** Single-cord entry, distribution, on/off, surge, and safe shutdown.

## Deliverables to produce here

- `bom.md` / `bom.csv` — bill of materials with part numbers and sourcing.
- `wiring/` — pinout tables and wiring diagrams (button → GPIO, display, power).
- `schematics/` — schematic + any adapter boards (KiCad preferred; export PDFs).
- `assembly.md` — how it goes together and how it's tested.

Empty for now — populated during the hardware design phase. Keep proprietary or
purchased datasheets out of git; link to them from `bom.md` instead.
