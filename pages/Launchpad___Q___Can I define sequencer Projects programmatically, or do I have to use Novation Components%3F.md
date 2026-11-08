logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Launchpad/PRG]], [[Launchpad/Custom/Mode/1 Arrangement]]

- # Can I define [[Launchpad]] sequencer Projects programmatically, or do I have to use Novation Components?
	- ## [[AI Answer]]
		- **Short answer:** there is no documented way to write a Project from code. Novation Components is the only official editor. But a Project travels as a SysEx file, so you can send a Project file you already have without Components; building one from scratch means reverse-engineering an undocumented format.
		- [[Answer/Official]] from the [Launchpad Pro Mk3 Components guide](https://support.novationmusic.com/hc/en-gb/articles/4411807448850-Launchpad-Pro-Mk3-Components-guide) and [[Launchpad/PRG]]:
			- **What the Programmer's Reference covers:** layout switching, LED lighting, DAW faders, and Live/Programmer mode. It has no message for reading or writing Project, Pattern, Scene, or step data. Its Select Layout message can only show the Sequencer Projects view (`0Dh`) or Patterns view (`0Eh`) on the surface ([[Launchpad/PRG/03 MIDI/03 Selecting Layouts]]).
			- **What Components does with Projects:** it gets the Projects from the device, starts a blank set, or uploads Projects from a SysEx file. Per slot, you can rename, download, replace, recolour, delete, or get and send that one slot. **Send to Launchpad Pro Mk3** sends the whole bank, and the set saves to your Novation account or your computer.
			- **Components does not edit Project contents.** Patterns and steps are written on the device's own sequencer ([[Launchpad/UG/09 Sequencer]]); Components moves and organizes finished Projects. See [[Launchpad/Q/What are Novation Launchpad Pro packs?]].
		- **What that leaves you, programmatically:**
			- **Replaying a saved Project — likely works.** Components runs over Web MIDI and the file is SysEx, so sending that file from another SysEx tool (`sendmidi`, Python `mido`, SysEx Librarian) should reproduce what Components sends. This is an inference; nobody in the garden has tested it yet.
			- **Generating a Project from data — undocumented.** A search found no public spec or community reverse-engineering of the Project format. You would capture several `.syx` exports that differ by one step and diff the bytes.
			- **Custom Modes are the precedent.** Their Components export is also undocumented SysEx with the `F0 00 20 29 02 0E` header, yet readable: the `.syx` files on [[Launchpad/Custom/Mode/1 Arrangement]] show the mode name in plain ASCII followed by one short record per control. Project files would need the same byte-level reading.
		- **Still open:** whether the device accepts a Project `.syx` from a tool other than Components, and the byte layout of a Project. A test: get one Project out of Components, send it back to an empty slot with `sendmidi`, and check the slot on the device.
