logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Launchpad/UG/09 Sequencer/12 Projects]]

- # What are [[Novation/Launchpad/Pro/Mk3]] "packs"?
	- Seen in the Projects tab of Novation Components at `components.novationmusic.com/launchpad-pro-mk3/projects`, with **New Pack**, **My Packs**, **Novation Packs**, **Get Pack from Launchpad Pro [MK3]**, **Create Pack** and **Upload Pack**.
	- ## [[AI Answer]]
		- **Short answer:** a pack is how Novation Components handles the Launchpad Pro's sequencer Projects as one set. **Get Pack** reads the Projects off the device in one go, and the set can be saved to your Novation account or your computer. This comes from a search summary of Novation's [Launchpad Pro Mk3 Components guide](https://support.novationmusic.com/hc/en-gb/articles/4411807448850-Launchpad-Pro-Mk3-Components-guide); the page itself refused automated fetches, so it has not been read word for word.
		- **What goes in it:** Projects. A Project stores the sequencer's Patterns, Scenes, scale and root, track types and track MIDI channels, and the device has 64 Project slots ([[Launchpad/UG/09 Sequencer/12 Projects]]). The user guide says Components can back up Projects online ([[Launchpad/UG/09 Sequencer/12 Projects/02 Backup]]).
		- **The buttons, read from the screenshot:**
			- **Get Pack from Launchpad Pro [MK3]** — copy the device's current Projects into Components.
			- **Create Pack** / **New Pack** — start an empty pack in Components.
			- **Upload Pack** — load a pack file from your computer.
			- **My Packs** — packs you have saved to your account.
			- **Novation Packs** — packs Novation supplies.
			- These roles follow from the labels; only **Get Pack** is confirmed by the search summary.
		- **Not the same as:**
			- Custom Modes, which have their own tab and editor in Components ([Custom Mode Editor Guide](https://support.novationmusic.com/hc/en-gb/articles/360009860380--Components-Launchpad-Mini-MK3-Launchpad-X-and-Launchpad-Pro-MK3-Custom-Mode-Editor-Guide)).
			- The Ampify sample packs in Launchpad Intro ([[Launchpad/UG/02 Getting Up and Running/02 Launchpad Intro]]).
		- **Update 2026-11-08:** the Components guide, read in a browser, says Projects are uploaded as a SysEx file, each slot can be got or sent on its own, and **Send to Launchpad Pro Mk3** sends the whole bank. See [[Launchpad/Q/Can I define sequencer Projects programmatically, or do I have to use Novation Components?]].
		- **Still open:** whether a pack always holds all 64 slots, and the byte layout of the pack file.
