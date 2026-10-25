logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/34 MIDI and Key Remote/01 MIDI Remote Control]]
prev:: [[Ableton/Live/UG/34 MIDI and Key Remote/01 MIDI Remote Control/02 Manual Control Surface Setup]]
- # [34.1.3 Takeover Mode](https://www.ableton.com/en/live-manual/12/midi-and-key-remote-control/#takeover-mode)
	- ![MIDI Controller Takeover Mode](https://ableton-production.imgix.net/live-manual/12/MIDITakeOverMode.png?auto=&w=320)
	- Takeover Mode decides what happens when a control that sends absolute values, such as a fader, is first moved after a bank switch has pointed it at a different parameter, so the hardware and the parameter disagree.
		- **None** — the new value goes straight to the parameter, usually as a sudden jump.
		- **Pick-Up** — moving the control does nothing until it passes the parameter's current value; from then on the parameter follows the control. Smooth, but the pick-up point is hard to predict.
		- **Value Scaling** — Live compares the two values and brings the parameter toward the control smoothly as the control moves, then follows it 1:1 once they meet.