up:: [[Launchpad/UG/08 Custom Modes]]

- # Pad mode
	- Setting in [Novation Components](https://components.novationmusic.com/)' Custom Mode editor that decides what a pad sends when it is pressed and released. It appears in the pad's side panel, above the CC number, on value, off value and MIDI channel.
	- The Launchpad Pro manual describes the three behaviours: a pad "can toggle, trigger, or act momentarily" ([[Launchpad/UG/08 Custom Modes/04 Set Up a Custom Mode]]).
	- ## Values
		- **Momentary** — sends the on value when the pad is pressed and the off value when it is released. The pad is on only while held.
		- **Toggle** — each press switches between the on value and the off value, so the pad stays on until pressed again.
		- **Trigger** — sends one set value on each press.
	- ## Mapping a Live button
		- For a pad MIDI-mapped to [[Ableton/Live/UI/Control Bar/Button/Stop]], Momentary works, sending 127 on press and 0 on release.
		- [[Launchpad/Custom/Mode/1 Arrangement]] uses Toggle for [[Ableton/Live/UI/Control Bar/Button/Arrangement Record]], whose state stays on until pressed again.
