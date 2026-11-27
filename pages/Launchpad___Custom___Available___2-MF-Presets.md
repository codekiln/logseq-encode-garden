logseq-entity:: [[Logseq/Entity/Launchpad/Custom/Mode]]

- # 2 MF Presets
	- [[Launchpad]] Custom Mode for choosing a [[Microfreak]] preset with a bank pad and then a Program Change pad, made for [[Launchpad/Q/Can Custom Mode select MicroFreak presets by bank and program change?]].
	- ## Pads
		- Every pad sends on MIDI channel 16, which the Launchpad's sequencer tracks on channels 1 to 4 don't use.
		- Row 1, columns 1 to 4 (white): CC Button, Trigger, CC 0 with values 0, 1, 2 and 3 from left to right. Each selects a MicroFreak bank.
		- Below each bank pad, from row 3 down: Program Change pads for presets in that bank.
			- Bank 0: [[Microfreak/Preset/016 Voidom]], program 15, yellow.
			- Bank 1: [[Microfreak/Preset/151 The Unstable]] (22, yellow), [[Microfreak/Preset/245 GivemeSub]] (116, blue), [[Microfreak/Preset/247 Laity]] (118, yellow), [[Microfreak/Preset/248 GrowLing]] (119, blue).
			- Bank 2: [[Microfreak/Preset/259 Infini Pad]] (2, red), [[Microfreak/Preset/297 Shiny Hat]] (40, blue).
			- Bank 3: [[Microfreak/Preset/399 FireAlarmLoBat]], program 14, blue.
		- Color shows how many [[GitP/A/Session]] days used the preset: red three, yellow two, blue one.
		- **Controls:** no Live mapping. A MIDI track listening to the Launchpad's `LPProMK3 MIDI` port on channel 16 passes the messages to the MicroFreak.
	- ## Status
		- Not tested yet. [[Launchpad/Custom/Available/3-MF-Number-Pad]] reaches any of the 512 slots in one entry and worked on [[2026-11-27 Fri]].
