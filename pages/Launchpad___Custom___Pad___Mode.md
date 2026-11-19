up:: [[Launchpad/UG/08 Custom Modes]]

- # Pad mode
	- Setting in [Novation Components](https://components.novationmusic.com/)' Custom Mode editor that decides what a pad sends when it is pressed and released. It appears in the pad's side panel, above the CC number, on value, off value and MIDI channel.
	- The Launchpad Pro manual describes the three behaviours: a pad "can toggle, trigger, or act momentarily" ([[Launchpad/UG/08 Custom Modes/04 Set Up a Custom Mode]]).
	- ## Values
		- {{embed [[Launchpad/Custom/Pad/Mode/Momentary]]}}
		- {{embed [[Launchpad/Custom/Pad/Mode/Toggle]]}}
		- {{embed [[Launchpad/Custom/Pad/Mode/Trigger]]}}
	- ## Mapping a Live button
		- For a pad MIDI-mapped to [[Ableton/Live/UI/Control Bar/Button/Stop]], Momentary works, sending 127 on press and 0 on release.
		- [[Launchpad/Custom/1/Arrangement]] uses Toggle for [[Ableton/Live/UI/Control Bar/Button/Arrangement Record]], whose state stays on until pressed again.