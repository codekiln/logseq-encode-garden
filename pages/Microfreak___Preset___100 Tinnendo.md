logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 100
preset-synth-microfreak-name:: Tinnendo
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Keys]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/099 Tout Doux]]
next:: [[Microfreak/Preset/101 Etna 01]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
preset-synth-microfreak-parameter-payload-sha256:: dfee8dac908d2a4774c5c53419beba49314d69b2cc404f738b1e3105e4e93163
preset-synth-file:: [Tinnendo — October 25 slot 100 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___100%20Tinnendo___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 342b462a9bb49737468cf271615a93f639cfd3b6743acee82fb061148fb1f1dc
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 100 over USB on October 25, 2026 with `mise run microfreak:download --slot 100`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0 (Factory 1.1 slot 188, Factory 2.1 slot 181, Factory 3.0 slot 181). Comparison used `mise run microfreak:compare`.
		- [Download the slot 100 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___100%20Tinnendo___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/100 Tinnendo/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Wavetable. [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
		- Table: 8 (stored choice code). Position: 0.911. Chorus: 1.000.
		- Keyboard octave: +1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.615; resonance: 0.160. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.830, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.181, RiseSlp 0.177, FallLvl 0.157, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Square, clock sync on; stored division code: 9. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: +0.004.
		- Cycling Envelope → Timbre: +0.717.
		- PRESSURE → Timbre: −1.000.
		- Cycling Envelope → Cutoff: +0.999.
		- ENV → Cutoff: +0.729.
		- PRESSURE → Assign 1 → Decay/Release: −0.853.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
