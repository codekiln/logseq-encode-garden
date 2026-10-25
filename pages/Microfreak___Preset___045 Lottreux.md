logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 045
preset-synth-microfreak-name:: Lottreux
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Pad]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/044 FM-it]]
next:: [[Microfreak/Preset/046 XnastX]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
preset-synth-microfreak-parameter-payload-sha256:: 457f05adda95072eb82a711e17e3b98a1deec6405e30648f5d14a20a04220a77
preset-synth-file:: [Lottreux — October 25 slot 45 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___045%20Lottreux___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: d8dbf43d45cc2ff717bb2889b0bd0dbbf05ef7d4602a92b685589c6dd63abf74
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 45 over USB on October 25, 2026 with `mise run microfreak:download --slot 45`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 131, Factory 2.1 slot 131, Factory 3.0 slot 131, Factory 6.0 slot 198). Comparison used `mise run microfreak:compare`.
		- [Download the slot 45 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___045%20Lottreux___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/045 Lottreux/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Wavetable. [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
		- Table: 12 (stored choice code). Position: 0.552. Chorus: 0.695.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.453; resonance: 0.847. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.401, decay/release 0.640, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.336, RiseSlp 0.500, FallLvl 0.395, FallSlp 0.000, Hold 0.000, Amount 0.950. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold, clock sync on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- KEY/ARP → Wave: +0.501.
		- Cycling Envelope → Timbre: −0.834.
		- ENV → Timbre: −0.472.
		- ENV → Cutoff: +0.587.
		- PRESSURE → Cutoff: +0.604.
		- LFO → Assign 1 → Glide: +0.289.
		- LFO → Assign 2 → Decay/Release: +0.142.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
