logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Ableton/Live/UG/30 MIDI Effect Reference]]
prev:: [[Ableton/Live/UG/30 MIDI Effect Reference/01 Arpeggiator]]
next:: [[Ableton/Live/UG/30 MIDI Effect Reference/03 Chord]]
- # [30.2 CC Control](https://www.ableton.com/en/live-manual/12/live-midi-effect-reference/#cc-control)
	- ![The CC Control Effect](https://ableton-production.imgix.net/live-manual/12/CCControlL12.png?auto=&w=320)
	- CC Control sends MIDI CC messages to hardware. It has three fixed knobs, one custom button, and twelve custom dials.
	- Fixed knobs:
		- **Mod Wheel** — modulation amount on the receiving device
		- **Pitch Bend** — bends down with negative values, up with positive
		- **Pressure** — channel pressure (aftertouch)
	- **Custom A** is a button that sends on/off or minimum/maximum. It defaults to the sustain pedal (CC 64) and can be set to any other CC with its CC Type chooser.
	- **Custom B–M** are dials that can be renamed and set to any CC. Names and assignments show on Push and are saved with presets. Automate them in lanes or turn the dials live.
	- Title bar:
		- two toggles switch between controls 1–8 and 9–16
		- **Send** sends every current CC value at once
		- **Learn** assigns a custom control from incoming MIDI, which also shows which CC a hardware controller sends
	- If the clip already has automation for a CC that CC Control also sends, the two streams are merged.