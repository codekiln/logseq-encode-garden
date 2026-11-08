logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Launchpad/PRG/03 MIDI]]
next:: [[Launchpad/PRG/03 MIDI/02 SysEx Format]]

- # Device Inquiry message
	- The Launchpad answers the Universal Device Inquiry SysEx.
	- Host to Launchpad: `F0h 7Eh 7Fh 06h 01h F7h` (240 126 127 6 1 247)
	- Reply from the application: `F0h 7Eh 00h 06h 02h 00h 20h 29h 13h 01h 00h 00h <app_version> F7h` (240 126 0 6 2 0 32 41 19 1 0 0 <app_version> 247)
	- Reply from the bootloader: `F0h 7Eh 00h 06h 02h 00h 20h 29h 13h 11h 00h 00h <boot_version> F7h` (240 126 0 6 2 0 32 41 19 17 0 0 <boot_version> 247)
	- `<app_version>` and `<boot_version>` are four bytes, one decimal digit (0-9) each, matching the version shown on the bootloader's green pads.
