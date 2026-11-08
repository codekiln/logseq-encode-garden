logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Launchpad/PRG/03 MIDI]]
prev:: [[Launchpad/PRG/03 MIDI/01 Device Inquiry]]
next:: [[Launchpad/PRG/03 MIDI/03 Selecting Layouts]]

- # SysEx message format used by the device
	- Every Launchpad Pro [MK3] SysEx message, in either direction, starts with this header:
		- Hex: `F0h 00h 20h 29h 02h 0Eh`
		- Decimal: `240 0 32 41 2 14`
	- `00h 20h 29h` is the Focusrite/Novation manufacturer ID, the same bytes that appear in the Device Inquiry reply.
	- A command byte follows the header and selects the function. [[Launchpad/PRG/06 SysEx Command Summary]] lists the commands.
