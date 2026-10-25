logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 076
preset-synth-microfreak-name:: AutoCHILL
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Pad]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/075 Saying Goodbye]]
next:: [[Microfreak/Preset/077 Eonz]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
preset-synth-microfreak-parameter-payload-sha256:: 5eb92624b5e905db04fc8e52536b5ec897b05f31968d0b04ba8758cc19655be1
preset-synth-file:: [AutoCHILL — October 25 slot 76 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___076%20AutoCHILL___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 24358a6fc67181a6cdeac11699a9e3a1c82128a6804ffe64ecb04d9d97811e45
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 76 over USB on October 25, 2026 with `mise run microfreak:download --slot 76`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0 (Factory 1.1 slot 162, Factory 2.1 slot 16, Factory 3.0 slot 16). Comparison used `mise run microfreak:compare`.
		- [Download the slot 76 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___076%20AutoCHILL___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/076 AutoCHILL/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Chords. [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
		- Type: 4 (stored choice code). Inv/Transp: 0.130. Shape control: 0.559.
		- Keyboard octave: +1. Glide: 0.000.
	- ## Filter
		- Band-pass filter. Saved cutoff: 0.452; resonance: 0.141. [[Microfreak/UG/07 Filter/01 Modifying Sound/02 Band Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.654, decay/release 0.562, sustain 0.648. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 1.000, RiseSlp 0.500, FallLvl 1.000, FallSlp 0.500, Hold 1.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold Filtered, clock sync off; stored normalized rate: 0.333. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: −0.001.
		- Cycling Envelope → Wave: +0.881.
		- LFO → Cutoff: +0.050.
		- PRESSURE → Assign 1 → Shape: +0.034.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
