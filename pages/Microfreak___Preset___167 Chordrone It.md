logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 167
preset-synth-microfreak-name:: Chordrone It
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Pad]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/166 Rnd Rytm Arp]]
next:: [[Microfreak/Preset/168 Arpic]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/05 KarplusStr]]
preset-synth-microfreak-parameter-payload-sha256:: a082f78a70d01837e2f6b23eee1124e8f2877aaf11e99a73238ab574e7f11215
preset-synth-file:: [Chordrone It — October 25 slot 167 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___167%20Chordrone%20It___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 293fa8eb53814da083b2253456619e62d7859f023ca0cb876189681037e4579b
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 167 over USB on October 25, 2026 with `mise run microfreak:download --slot 167`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 140, Factory 2.1 slot 242, Factory 3.0 slot 242, Factory 6.0 slot 212). Comparison used `mise run microfreak:compare`.
		- [Download the slot 167 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___167%20Chordrone%20It___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/167 Chordrone It/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: KarplusStr. [[Microfreak/UG/06 Dig Osc/03 Types/05 KarplusStr]]
		- Bow: 0.651. Position: 0.104. Decay: 1.000.
		- Keyboard octave: -1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.683; resonance: 0.376. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.358, decay/release 0.659, sustain 0.796. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.254, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 6. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- PRESSURE → Timbre: +1.000.
		- ENV → Cutoff: +0.085.
		- PRESSURE → Cutoff: −0.271.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
