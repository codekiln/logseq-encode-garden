logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 303
preset-synth-microfreak-name:: 2020 Behind
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/302 No Rush]]
next:: [[Microfreak/Preset/304 Saw Vox]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
preset-synth-microfreak-parameter-payload-sha256:: 6998c5de7c37d7ae366b4577dd7268ede9dc3799b98d95177246a0825f338064
preset-synth-file:: [2020 Behind — October 25 slot 303 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___303%202020%20Behind___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: c92a4571071a01fb7a0c5945ba537aa8543458d80115aa6eb20c224f78b33bb0
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 303 over USB on October 25, 2026 with `mise run microfreak:download --slot 303`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 366, Factory 6.0 slot 224). Comparison used `mise run microfreak:compare`.
		- [Download the slot 303 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___303%202020%20Behind___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/303 2020 Behind/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SawX. [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
		- Saw Mod: 0.053. Shape: 0.463. Noise: 0.453.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- High-pass filter. Saved cutoff: 0.818; resonance: 0.704. [[Microfreak/UG/07 Filter/01 Modifying Sound/03 High Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.776, sustain 0.567. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.795, RiseSlp 0.000, FallLvl 0.801, FallSlp 0.000, Hold 0.639, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Square, clock sync off; stored normalized rate: 0.720. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: +0.250.
		- Cycling Envelope → Wave: +0.724.
		- Cycling Envelope → Cutoff: −0.620.
		- ENV → Cutoff: −0.685.
		- KEY/ARP → Cutoff: +0.706.
		- ENV → Assign 1 → Cycling Envelope Hold: −1.000.
		- PRESSURE → Assign 2 → LFO Rate: +0.130.
		- KEY/ARP → Assign 2 → LFO Rate: +0.056.
		- PRESSURE → Assign 3 → Sustain: +0.124.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
