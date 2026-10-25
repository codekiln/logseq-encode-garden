logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 213
preset-synth-microfreak-name:: Hypno Chaos
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/212 Raver]]
next:: [[Microfreak/Preset/214 Gaia]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-microfreak-parameter-payload-sha256:: 88229ce9fca4306d0d09e5ec765f484d5e1bbf8f33ef32f641def165bedfdf2a
preset-synth-file:: [Hypno Chaos — October 25 slot 213 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___213%20Hypno%20Chaos___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: ff9ad316c6ccb6aa463a31224437282a845b38839a4551b752fe5dab92c51393
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 213 over USB on October 25, 2026 with `mise run microfreak:download --slot 213`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 284, Factory 6.0 slot 426). Comparison used `mise run microfreak:compare`.
		- [Download the slot 213 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___213%20Hypno%20Chaos___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/213 Hypno Chaos/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harm. [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
		- Spread: 0.570. Rectification: 0.516. Noise: 0.308.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.428; resonance: 0.686. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.352, sustain 0.432. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.109, RiseSlp 0.500, FallLvl 0.330, FallSlp 0.500, Hold 1.000, Amount 0.272. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync on; stored division code: 7. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: +0.432.
		- Cycling Envelope → Wave: −0.025.
		- LFO → Wave: +0.156.
		- Cycling Envelope → Timbre: +0.216.
		- ENV → Cutoff: +0.393.
		- LFO → Assign 1 → Unison Spread: +0.307.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
