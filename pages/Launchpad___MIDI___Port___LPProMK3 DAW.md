logseq-entity:: [[Logseq/Entity/MIDI/Port]]

- # LPProMK3 DAW
	- Carries the messages between a DAW and the Launchpad Pro MK3's Session mode, which launches the DAW's clips from the pad grid ([[Launchpad/PRG/03 MIDI]], [[Launchpad/UG/05 Session Mode/01 Ableton Live Session View]]).
	- ## In [[Ableton/Live]]
		- Live finds the Launchpad when it opens and switches it to Session mode ([[Launchpad/UG/02 Getting Up and Running/03 Ableton Live]]). Row 2 of codekiln's Control Surface table holds the Launchpad Pro MK3 control surface ([[Ableton/Live/UG/34 MIDI and Key Remote/01 MIDI Remote Control/01 Natively Supported Control Surfaces]]).
		- Live labels this port with the control surface's name:
			- In a track's MIDI From menu: `Launchpad Pro MK3 Input (Launchpad Pro MK3 (LPProMK3 DAW))`.
			- In the MIDI Ports list: `Launchpad_Pro_MK3 Input (Laun…` and `Launchpad_Pro_MK3 Output (Lau…`, cut off in the window.
		- codekiln's [[Ableton/Live/MIDI/Port]] settings on [[2026-11-14 Sat]]: Track on for the input and the output.
		- On [[GitP/A/Log/26/11/13-Fri]], with the Launchpad in Note mode, a track with this port as its MIDI From played the Drum Rack, and the Launchpad lit the pads that held samples.
	- ## Source
		- [[Launchpad/PRG/03 MIDI]]
		- [[Launchpad/UI/Area/5-Rear/1-USB-C-Port]]
		- [[Launchpad/UG/02 Getting Up and Running/03 Ableton Live]]
		- [[Launchpad/UG/05 Session Mode/01 Ableton Live Session View]]
		- [[Ableton/Live/UG/17 Routing and IO/03 External MIDI In-Out/01 MIDI Port Inputs and Outputs]]
		- [[Ableton/Live/UG/34 MIDI and Key Remote/01 MIDI Remote Control/01 Natively Supported Control Surfaces]]
