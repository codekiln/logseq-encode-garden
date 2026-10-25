logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 243
preset-synth-microfreak-name:: Noisy
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/242 93s  Rave]]
next:: [[Microfreak/Preset/244 Nebem]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
preset-synth-microfreak-parameter-payload-sha256:: bc0da47a487504d5efaa859ae67a05c6edc6e030f7ddc2e5ca348fe67af61756
preset-synth-file:: [Noisy — October 25 slot 243 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___243%20Noisy___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 1ea8f548ff1923aa8ef12880a947688f7f18bff6e02709c07dd9f29e1acf0a5d
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 243 over USB on October 25, 2026 with `mise run microfreak:download --slot 243`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 311, Factory 6.0 slot 362). Comparison used `mise run microfreak:compare`.
		- [Download the slot 243 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___243%20Noisy___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/243 Noisy/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SawX. [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
		- Saw Mod: 0.112. Shape: 0.121. Noise: 0.001.
		- Keyboard octave: -2. Glide: 0.109.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.804; resonance: 0.759. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.010, decay/release 0.103, sustain 0.233. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.867, RiseSlp 0.818, FallLvl 0.053, FallSlp 0.825, Hold 0.102, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold Filtered, clock sync on; stored division code: 5. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Timbre: +0.158.
		- Cycling Envelope → Cutoff: +1.000.
		- ENV → Cutoff: +0.008.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
