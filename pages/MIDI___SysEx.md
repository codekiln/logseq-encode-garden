logseq-entity:: [[Logseq/Entity/Abbreviation]], [[Logseq/Entity/Term]]
alias:: [[MIDI/System Exclusive]]

- # MIDI SysEx
	- **System Exclusive** — a [[MIDI/Message]] whose content a manufacturer defines. It opens with F0h and a manufacturer ID, carries any number of data values from 0 to 127, and closes with F7h.
	- A receiver that doesn't recognize the ID ignores the rest. That lets each maker add its own commands for preset dumps, firmware updates and settings no standard message covers.
	- The IDs 7Eh and 7Fh belong to no manufacturer and carry Universal SysEx messages. Device Inquiry, which asks a device to identify itself, is one ([[Launchpad/PRG/03 MIDI/01 Device Inquiry]]).
	- Only real-time messages such as [[MIDI/Clock]] may arrive in the middle of a SysEx message.
	- In this garden: [[Launchpad/PRG/03 MIDI/02 SysEx Format]], [[Launchpad/PRG/06 SysEx Command Summary]], [[Microfreak/CLI/Preset metadata over USB]].
