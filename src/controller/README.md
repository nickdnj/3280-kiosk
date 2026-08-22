# Controller — buttons → app bridge

The software that runs on the kiosk's single-board computer: it launches the
kiosk app in a locked-down fullscreen browser and maps the three physical
buttons to app navigation.

## Responsibilities

- **Boot to kiosk.** On power-up, bring up the display, hide all OS chrome, and
  launch `../kiosk-app/index.html` fullscreen (kiosk/kiosk-mode browser).
- **Read the buttons.** Debounced GPIO input for BACK / HOME / NEXT.
- **Drive navigation.** Translate button presses into app actions (previous
  screen / return to HOME / next screen). Likely via synthetic key events or a
  tiny local WebSocket the app listens on.
- **Stay up.** Watchdog / auto-restart on crash; idle timer that returns to
  HOME after N minutes of no input (attract state).

## Undecided (for the architecture phase)

- Compute platform: Raspberry Pi (4/5) vs. other SBC. Drives GPIO choice,
  power budget, and the mounting in `../../electronics/` and `../../mechanical/`.
- Button interface: direct GPIO vs. a USB HID adapter.
- App↔controller transport: injected key events vs. local socket.

Nothing is built here yet — this folder is a placeholder the software team fills
in after the architecture doc lands.
