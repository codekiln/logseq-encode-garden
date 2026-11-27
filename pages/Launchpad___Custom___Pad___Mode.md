up:: [[Launchpad/UG/08 Custom Modes]]

- # Pad mode
	- Pad mode determines the behavior of a pad button in [[Novation/Components]] custom modes: what the pad sends when it is pressed and when it is released. It appears in the pad's side panel in the Custom Mode editor, above the CC number, on value, off value and MIDI channel.
	- The Launchpad Pro manual describes the three behaviours: a pad "can toggle, trigger, or act momentarily" ([[Launchpad/UG/08 Custom Modes/04 Set Up a Custom Mode]]).
	- ## Values
		- {{embed [[Launchpad/Custom/Pad/Mode/Momentary]]}}
		- {{embed [[Launchpad/Custom/Pad/Mode/Toggle]]}}
		- {{embed [[Launchpad/Custom/Pad/Mode/Trigger]]}}
	- ## Fields
		- **Every pad mode** shows these fields in the pad's side panel:
			- **CC number** and **MIDI channel** — the message the pad sends.
			- **Colour** — the pad's own colour, shown while it is idle.
		- **Momentary and Toggle** add an **On value** and an **Off value**. Momentary sends the off value on release; Toggle sends it on the press that turns the pad off.
		- **Trigger** adds only an **On value**, because it sends one message per press and nothing on release.
		- **On colour** sits below the grid, not in the pad's side panel. It is one colour for the whole custom mode, shown on a pad while it is held, or while a Toggle pad is on. The manual describes the same split: each pad has its own off colour, and one shared on colour covers the whole mode ([[Launchpad/UG/08 Custom Modes/04 Set Up a Custom Mode]]).
	- ## Mapping a Live button
		- For a pad MIDI-mapped to [[Ableton/Live/UI/Control-Bar/Button/Stop]], Momentary works, sending 127 on press and 0 on release.
		- [[Launchpad/Custom/Available/1-Arrangement]] uses Toggle for [[Ableton/Live/UI/Control-Bar/Button/Arrangement-Record]], whose state stays on until pressed again.