logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/34 MIDI and Key Remote/02 The Mapping Browser]]
prev:: [[Ableton/Live/UG/34 MIDI and Key Remote/02 The Mapping Browser/03 Mapping to Absolute MIDI Controllers]]
next:: [[Ableton/Live/UG/34 MIDI and Key Remote/02 The Mapping Browser/05 Computer Keyboard Remote Control]]
- # [34.2.4 Mapping to Relative MIDI Controllers](https://www.ableton.com/en/live-manual/12/midi-and-key-remote-control/#mapping-to-relative-midi-controllers)
	- Relative controllers send "increase" and "decrease" messages instead of absolute values, so a parameter never jumps when the hardware and Live disagree. A relative pan knob just moves the pan a little from wherever it is.
	- Live supports four kinds — **Signed Bit**, **Signed Bit 2**, **Bin Offset** and **Twos Complement** — each also in a linear version. Some encoders accelerate, sending bigger steps when turned quickly.
	- For controllers that are not natively supported, Live tries to detect the kind and whether acceleration is used. Turning the control slowly to the left while mapping helps. Live's guess appears in the Status Bar's mode chooser, where it can be changed by hand.
	- What the messages do:
		- **Session View slots** — increase acts as Note On, decrease as Note Off.
		- **Switches** — increase turns on, decrease turns off.
		- **Radio buttons** — increase steps forward, decrease steps back.
		- **Continuous controls** — each kind reads the 0–127 range differently to tell increases from decreases.
	- ### [34.2.4.1 Relative Session View Navigation](https://www.ableton.com/en/live-manual/12/midi-and-key-remote-control/#relative-session-view-navigation)
		- Besides mapping single slots and scenes, controls can be mapped to move the highlighted scene and launch the highlighted clips. In MIDI Map Mode and Key Map Mode a strip of mappable controls appears below the Session grid.
			- ![The Relative Session Mapping Strip](https://ableton-production.imgix.net/live-manual/12/RelativeSessionMap.png?auto=&w=320)
		- The strip has:
			- buttons that move the highlighted scene up and down
			- a scene number box, best mapped to an endless encoder, for scrolling through scenes
			- a button that launches the highlighted scene; with **Select Next Scene on Launch** on in the Record, Warp & Launch Settings, each press moves on to the next scene
			- a button that cancels a triggered scene launch
			- one button per track that launches that track's clip in the highlighted scene
		- Live keeps the highlighted scene centered in Session View, which helps in large Sets.
	- ### [34.2.4.2 Mapping to Clip View Controls](https://www.ableton.com/en/live-manual/12/midi-and-key-remote-control/#mapping-to-clip-view-controls)
		- Clip View shows whichever clip is selected, or several clips at once, so a mapping to a Clip View control can change any clip in the Set. The manual recommends relative controllers for Clip View controls to avoid jumps.