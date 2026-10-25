logseq-entity:: [[Logseq/Entity/Definition]]

- # UI Control Setting
	- In this garden, **UI Control Setting** pages model one mode a [[Logseq/Entity/UI/Control]] selects, or one parameter that exists only in such a mode.
	- ## What counts
		- A mode: one named position of a selector, such as the oscillator model [[Microfreak/UI/Oscillator/Knob/Type/VAnalog]].
		- A parameter: the name another control takes while that mode is active, such as [[Microfreak/UI/Oscillator/Knob/Type/VAnalog/Detune]], which the Wave knob sets.
		- A plain value along a range, such as 64 on a knob, is not a setting page.
	- ## Identity and names
		- A mode sits at `<Control>/<Mode>`, beneath the control that selects it; a parameter sits at `<Control>/<Mode>/<Parameter>`.
		- Use the names the display or manual shows.
	- ## Page shape
		- Frontmatter: `logseq-entity:: [[Logseq/Entity/UI/Control/Setting]]` and `up::` to the control or mode above it; `prev::` and `next::` follow the order of modes in the manual when the modes are numbered.
		- One bullet-wrapped H1, then one sentence on what the setting does.
		- A parameter page names the control that sets it, with a link.
		- A **Source** line links the user guide or manual section.
