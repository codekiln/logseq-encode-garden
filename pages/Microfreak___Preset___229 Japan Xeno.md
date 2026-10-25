logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 229
preset-synth-microfreak-name:: Japan Xeno
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/228 Last Days]]
next:: [[Microfreak/Preset/230 Cristal Church]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
preset-synth-microfreak-parameter-payload-sha256:: 03ef0714d954c6727fd44d217b432fdd74b89458e2a915bc518fa70e37fafb21
preset-synth-file:: [Japan Xeno — October 25 slot 229 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___229%20Japan%20Xeno___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: fdf49b254da7eca544a388607ed7109f6f977da407578acd788cf3e2376af266
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 229 over USB on October 25, 2026 with `mise run microfreak:download --slot 229`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 299, Factory 6.0 slot 143). Comparison used `mise run microfreak:compare`.
		- [Download the slot 229 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___229%20Japan%20Xeno___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/229 Japan Xeno/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Bass. [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
		- Saturate: 0.702. Fold: 0.371. Noise: 0.332.
		- Keyboard octave: -2. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.638; resonance: 0.675. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.431, sustain 0.421. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.000, RiseSlp 1.000, FallLvl 1.000, FallSlp 0.000, Hold 1.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync off; stored normalized rate: 0.753. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.075.
		- LFO → Pitch: +0.015.
		- ENV → Wave: +1.000.
		- Cycling Envelope → Timbre: +0.229.
		- ENV → Cutoff: +0.253.
		- PRESSURE → Assign 1 → Unison Spread: −0.084.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
