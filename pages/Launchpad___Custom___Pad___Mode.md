up:: [[Launchpad/UG/08 Custom Modes]]

- # Pad mode
	- Pad mode determines the behavior of a pad button in [[Novation/Components]] custom modes: what the pad sends when it is pressed and when it is released. It appears in the pad's side panel in the Custom Mode editor, above the CC number, on value, off value and MIDI channel.
	- The Launchpad Pro manual describes the three behaviours: a pad "can toggle, trigger, or act momentarily" ([[Launchpad/UG/08 Custom Modes/04 Set Up a Custom Mode]]).
	- ## Values
		- {{embed [[Launchpad/Custom/Pad/Mode/Momentary]]}}
		- {{embed [[Launchpad/Custom/Pad/Mode/Toggle]]}}
		- {{embed [[Launchpad/Custom/Pad/Mode/Trigger]]}}
	- ## Mapping a Live button
		- For a pad MIDI-mapped to [[Ableton/Live/UI/Control Bar/Button/Stop]], Momentary works, sending 127 on press and 0 on release.
		- [[Launchpad/Custom/1/Arrangement]] uses Toggle for [[Ableton/Live/UI/Control Bar/Button/Arrangement Record]], whose state stays on until pressed again.