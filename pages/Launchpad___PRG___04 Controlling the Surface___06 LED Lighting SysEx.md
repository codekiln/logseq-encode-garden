logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Launchpad/PRG/04 Controlling the Surface]]
prev:: [[Launchpad/PRG/04 Controlling the Surface/05 Examples]]

- # LED lighting SysEx message
	- One SysEx message can light many LEDs. LED indices are always the Programmer Mode numbers, whatever layout is selected.
		- Hex: `F0h 00h 20h 29h 02h 0Eh 03h <Colour Spec> [<Colour Spec> ...] F7h`
		- Decimal: `240 0 32 41 2 14 3 <Colour Spec> [<Colour Spec> ...] 247`
	- Each `<Colour Spec>` is a lighting type byte, an LED index byte, then 1-3 bytes of lighting data.
	- Lighting types:
		- `00h` (0) static: 1 byte, palette index
		- `01h` (1) flashing: 2 bytes, colour B then colour A
		- `02h` (2) pulsing: 1 byte, palette index
		- `03h` (3) RGB: 3 bytes, red, green, blue, each 0-127
	- A message may carry up to 106 Colour Specs, enough for the whole surface.
	- Example in Programmer layout: `F0h 00h 20h 29h 02h 0Eh 03h 00h 0Bh 0Dh 01h 0Ch 15h 17h 02h 0Dh 25h F7h` (240 0 32 41 2 14 3 0 11 13 1 12 21 23 2 13 37 247)
		- Pad 11, the bottom-left pad: static yellow (13).
		- Pad 12: flashing between 21 and 23, dim and bright green.
		- Pad 13: pulsing turquoise (37).
