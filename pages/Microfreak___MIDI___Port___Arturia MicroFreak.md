logseq-entity:: [[Logseq/Entity/MIDI/Port]]

- # Arturia MicroFreak
	- The MIDI port a computer sees when the MicroFreak is connected over USB. It carries the MicroFreak's notes to the computer, and notes and clock from the computer to the MicroFreak ([[Microfreak/UG/17 Ext Gear/01 Computer Connection]], [[Microfreak/UG/03 Overview/02 Rear Panel/05 USB DC In]]).
	- ## On the MicroFreak
		- The Global MIDI settings choose the channel it receives on and the channel it sends on, and whether it sends over USB, the MIDI jacks or both. The Sync settings choose whether it follows clock from USB ([[Microfreak/UG/14 Config/01 Utility & MCC/02 Global]]).
		- A DAW track plays the MicroFreak when the track's MIDI channel matches the MicroFreak's input channel ([[Microfreak/UG/17 Ext Gear/06 MIDI Channels/01 DAW Configuration]]).
	- ## In [[Ableton/Live]]
		- Input and output label: `Arturia MicroFreak (unknown mididevice)`, as the tracks [[GitP/A/Session/26/11/06-Fri/Set/Track/utility/LPP to MF]] and [[GitP/A/Session/26/11/06-Fri/Set/Track/utility/MF to LPP]] record it.
		- codekiln's [[Ableton/Live/MIDI/Port]] settings on [[2026-11-14 Sat]]: the input has Track on; the output has Track and Sync on, with MIDI Clock Sync Delay 0.00 ms and MIDI Clock Type Song. With Sync on, Live sends the MicroFreak its MIDI Clock ([[Ableton/Live/UG/37 Sync with Link Tempo Follower and MIDI/03 Synchronizing via MIDI/01 Synchronizing External MIDI Devices to Live]]).
	- ## Source
		- [[Microfreak/UG/17 Ext Gear/01 Computer Connection]]
		- [[Microfreak/UG/14 Config/01 Utility & MCC/02 Global]]
		- [[Microfreak/UG/17 Ext Gear/06 MIDI Channels/01 DAW Configuration]]
		- [[Ableton/Live/UG/17 Routing and IO/03 External MIDI In-Out/01 MIDI Port Inputs and Outputs]]
