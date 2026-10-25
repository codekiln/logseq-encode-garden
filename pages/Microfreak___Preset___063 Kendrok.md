logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 063
preset-synth-microfreak-name:: Kendrok
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Keys]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/062 Mood Strings]]
next:: [[Microfreak/Preset/064 Mood]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
preset-synth-microfreak-parameter-payload-sha256:: 8cac6eb1670acd09609b13585d03cd25582dede1ec9cea2ff02cfe3bf180039e
preset-synth-file:: [Kendrok — October 25 slot 63 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___063%20Kendrok___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 01099414a2e79ab3f6c25402698144da3e4eeffa1e1259d57dfa002cdf716ed2
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 63 over USB on October 25, 2026 with `mise run microfreak:download --slot 63`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 15, Factory 2.1 slot None, Factory 3.0 slot 148, Factory 6.0 slot 43). Comparison used `mise run microfreak:compare`.
		- [Download the slot 63 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___063%20Kendrok___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/063 Kendrok/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: V.Analog. [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
		- Detune: 0.525. Shape: 0.368. Wave: 0.486.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.005; resonance: 0.465. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.024, decay/release 0.415, sustain 0.363. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.000, RiseSlp 0.772, FallLvl 0.003, FallSlp 0.090, Hold 0.000, Amount 0.697. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sawtooth, clock sync on; stored division code: 2. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Timbre: −0.480.
		- Cycling Envelope → Cutoff: +1.000.
		- ENV → Cutoff: +0.310.
		- PRESSURE → Cutoff: −0.073.
		- ENV → Assign 1 → Cycling Envelope Amount: +0.596.
		- PRESSURE → Assign 3 → matrix amount LFO → Cutoff: +0.289.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
