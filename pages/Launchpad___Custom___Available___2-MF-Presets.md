logseq-entity:: [[Logseq/Entity/Launchpad/Custom/Mode]]
launchpad-custom-mode-url:: https://components.novationmusic.com/launchpad-pro-mk3/custom-modes/795113

- # 2 MF Presets
	- [[Launchpad]] Custom Mode for choosing a [[Microfreak]] preset with a bank pad and then a Program Change pad, made for [[Launchpad/Q/Can Custom Mode select MicroFreak presets by bank and program change?]].
	- ![2 MF Presets in the Components editor](../assets/.remote/logseq-encode-garden/Launchpad___Custom___Available___2-MF-Presets___Asset___Components-editor.png)
		- Transcription: [[Launchpad/Custom/Available/2-MF-Presets/Asset/Components-editor/png]]
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
	- ## Rendering on the page
		- [[Person/codekiln/GitHub/logseq-gardener/Idea/Custom-Block-and-Static-Site-Rendering]] proposes drawing this grid from data on the page instead of a screenshot.
	- ## Status
		- Worked on [[2026-11-28 Sat]]: codekiln loaded recent [[GitP/A/Session]] presets with the bank and Program Change pads ([[GitP/A/Log/26/11/28-Sat]]).
		- [[Launchpad/Custom/Available/3-MF-Number-Pad]] reaches any of the 512 slots in one entry and also worked on [[2026-11-27 Fri]].
