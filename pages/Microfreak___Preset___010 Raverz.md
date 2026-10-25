logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 010
preset-synth-microfreak-name:: Raverz
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/009 261e]]
next:: [[Microfreak/Preset/011 Club V]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
preset-synth-microfreak-parameter-payload-sha256:: 91abba6680ffcc5546213259ceced6f08113992633f8a4a5e2419a164b3f48f5
preset-synth-file:: [Raverz — October 25 slot 10 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___010%20Raverz___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: c05c8c3949031cd78acde893964ea4ead9251fcf3a1e97016dbc211abd204a90
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 10 over USB on October 25, 2026 with `mise run microfreak:download --slot 10`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot 110, Factory 1.1 slot 110, Factory 2.1 slot 10, Factory 3.0 slot 10, Factory 6.0 slot None). Comparison used `mise run microfreak:compare`.
		- [Download the slot 10 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___010%20Raverz___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/010 Raverz/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: V.Analog. [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
		- Detune: 1.000. Shape: 0.503. Wave: 0.794.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.017; resonance: 0.177. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.474, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.557, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync on; stored division code: 2. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +1.000.
		- LFO → Timbre: +0.409.
		- Cycling Envelope → Cutoff: +1.000.
		- ENV → Cutoff: −0.046.
		- LFO → Cutoff: +0.626.
		- Cycling Envelope → Assign 1 → Cycling Envelope Fall: −0.482.
		- ENV → Assign 1 → Cycling Envelope Fall: −0.009.
		- ENV → Assign 2 → Wave: +0.294.
		- LFO → Assign 2 → Wave: −0.357.
		- ENV → Assign 3 → matrix amount LFO → Assign 2: +0.550.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
