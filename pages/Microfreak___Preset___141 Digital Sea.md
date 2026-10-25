logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 141
preset-synth-microfreak-name:: Digital Sea
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/140 Hats maker]]
next:: [[Microfreak/Preset/142 Kick A]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
preset-synth-microfreak-parameter-payload-sha256:: 4fdf0b95dcf4b74194b0ff7542bc47dbcd82ab78d0d583bd9954ac3cd85a2535
preset-synth-file:: [Digital Sea — October 25 slot 141 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___141%20Digital%20Sea___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 318aa928549b305ddb080a78fa27c3d7b2a8d5f6b7b9198cc217aae7b87af6b9
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 141 over USB on October 25, 2026 with `mise run microfreak:download --slot 141`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0 (Factory 2.0 slot 117, Factory 2.1 slot 219, Factory 3.0 slot 219). Comparison used `mise run microfreak:compare`.
		- [Download the slot 141 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___141%20Digital%20Sea___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/141 Digital Sea/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Noise. [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
		- Wave: 0.292. Timbre: 0.928. Shape: 0.000.
		- Keyboard octave: -2. Glide: 0.000.
	- ## Filter
		- Band-pass filter. Saved cutoff: 0.101; resonance: 0.013. [[Microfreak/UG/07 Filter/01 Modifying Sound/02 Band Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.708, decay/release 0.662, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.668, RiseSlp 0.637, FallLvl 0.697, FallSlp 0.078, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold Filtered, clock sync off; stored normalized rate: 0.141. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Wave: −0.124.
		- Cycling Envelope → Timbre: +0.150.
		- Cycling Envelope → Cutoff: +0.283.
		- LFO → Assign 1 → Cycling Envelope Rise: +0.109.
		- LFO → Assign 2 → Cycling Envelope Fall: +0.107.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
