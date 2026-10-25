logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 157
preset-synth-microfreak-name:: Ice Cold
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Keys]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/156 Prosper]]
next:: [[Microfreak/Preset/158 Grimy Beat]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
preset-synth-microfreak-parameter-payload-sha256:: d727352623f1c7723ce209845af88f45d43d372c57d42276818fbc7daf09769a
preset-synth-file:: [Ice Cold — October 25 slot 157 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___157%20Ice%20Cold___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 4775ae676148db993100fb45f488c0571be82722eeff3d4e92139b5ba5801a15
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 157 over USB on October 25, 2026 with `mise run microfreak:download --slot 157`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0 (Factory 2.0 slot 131, Factory 2.1 slot 233, Factory 3.0 slot 233). Comparison used `mise run microfreak:compare`.
		- [Download the slot 157 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___157%20Ice%20Cold___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/157 Ice Cold/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Noise. [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
		- Wave: 0.000. Timbre: 1.000. Shape: 0.000.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.210; resonance: 0.285. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.645, sustain 0.667. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.276, RiseSlp 1.000, FallLvl 0.207, FallSlp 1.000, Hold 0.000, Amount 0.365. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.430. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: +0.001.
		- ENV → Wave: +0.186.
		- ENV → Cutoff: +0.357.
		- PRESSURE → Cutoff: −0.254.
		- Cycling Envelope → Assign 1 → Shape: +0.236.
		- ENV → Assign 1 → Shape: +1.000.
		- LFO → Assign 2 → matrix amount LFO → Pitch: +0.004.
		- KEY/ARP → Assign 2 → matrix amount LFO → Pitch: +0.020.
		- Cycling Envelope → Assign 3 → Sustain: +0.668.
		- ENV → Assign 3 → Sustain: +0.117.
		- LFO → Assign 3 → Sustain: +0.150.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
