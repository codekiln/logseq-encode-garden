logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Launchpad/Custom/Mode/1 Arrangement]]

- # Which [[MIDI]] CC numbers are free for custom mappings?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [MIDI 1.0 Control Change Messages](https://midi.org/midi-1-0-control-change-messages)
		- **Short answer:** use the controllers the MIDI spec marks "Undefined": 3, 9, 14, 15, 20–31, 85–87, 89, 90 and 102–119. The block 102–119 is the largest run.
		- **Avoid 120–127.** These are Channel Mode Messages, which "affect the channel's operating mode" rather than a sound parameter: All Sound Off, Reset All Controllers, Local Control On/Off, All Notes Off, Omni Off, Omni On, Mono On and Poly On.
		- **88 is not free.** It is High Resolution Velocity Prefix, between the undefined 85–87 and 89–90.
		- **Check the controller's own defaults too.** The Launchpad Pro's Custom 2 faders send CC 15–22 ([[Launchpad/UG/08 Custom Modes/02 Default Custom Modes]]), which overlaps the undefined 15 and 20–22.
		- **Example:** [[Launchpad/Custom/Mode/1 Arrangement]] uses CC 116–119 on channel 16. The next free numbers are 115 and down to 102.
