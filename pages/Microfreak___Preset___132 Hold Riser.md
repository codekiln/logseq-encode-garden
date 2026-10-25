logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 132
preset-synth-microfreak-name:: Hold Riser
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/131 Colik]]
next:: [[Microfreak/Preset/133 Malfunction]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
preset-synth-microfreak-parameter-payload-sha256:: f9ab74916972010a9c544700484df9f8d69e62d35291ca71a735633f8046d259
preset-synth-file:: [Hold Riser — October 25 slot 132 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___132%20Hold%20Riser___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: beadec309a3f1a3e77a1ff5931e710236689d1bc770838bde475ec35b640565a
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 132 over USB on October 25, 2026 with `mise run microfreak:download --slot 132`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 109, Factory 2.1 slot 210, Factory 3.0 slot 210, Factory 6.0 slot 317). Comparison used `mise run microfreak:compare`.
		- [Download the slot 132 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___132%20Hold%20Riser___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/132 Hold Riser/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Noise. [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
		- Wave: 0.385. Timbre: 0.603. Shape: 0.525.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.193; resonance: 0.381. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.404, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.095, RiseSlp 0.500, FallLvl 0.312, FallSlp 0.192, Hold 0.000, Amount 0.825. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sawtooth, clock sync on; stored division code: 0. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.996.
		- LFO → Pitch: +0.280.
		- Cycling Envelope → Timbre: +0.861.
		- LFO → Timbre: +0.074.
		- ENV → Cutoff: +0.736.
		- LFO → Assign 1 → Decay/Release: +0.289.
		- LFO → Assign 2 → matrix amount ENV → Cutoff: +0.257.
		- LFO → Assign 3 → Cycling Envelope Fall: −0.240.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
