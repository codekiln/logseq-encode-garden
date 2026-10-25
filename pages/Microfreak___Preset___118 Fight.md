logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 118
preset-synth-microfreak-name:: Fight
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Lead]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/117 Minor Pad]]
next:: [[Microfreak/Preset/119 NoiseBusters]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
preset-synth-microfreak-parameter-payload-sha256:: 0cd4e2b218f3673e8d6eb33e94dd4a2cba6ea9c8e89c80d5abb0538902646efe
preset-synth-file:: [Fight — October 25 slot 118 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___118%20Fight___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: bd02bf0ebb4d11593d5b864499046beb6cc4901e261eea7d725b217e758bb307
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 118 over USB on October 25, 2026 with `mise run microfreak:download --slot 118`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 6, Factory 2.1 slot None, Factory 3.0 slot 198, Factory 6.0 slot 330). Comparison used `mise run microfreak:compare`.
		- [Download the slot 118 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___118%20Fight___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/118 Fight/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Chords. [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
		- Type: 1 (stored choice code). Inv/Transp: 0.391. Shape control: 0.455.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.423; resonance: 0.385. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.285, sustain 0.218. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.179, RiseSlp 0.500, FallLvl 0.421, FallSlp 0.500, Hold 0.000, Amount 0.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Square, clock sync on; stored division code: 46423. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Wave: +0.223.
		- LFO → Timbre: +0.017.
		- ENV → Cutoff: +0.643.
		- PRESSURE → Cutoff: +0.768.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
