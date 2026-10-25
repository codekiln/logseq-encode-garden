logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 057
preset-synth-microfreak-name:: Hollows
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/056 PowerStab]]
next:: [[Microfreak/Preset/058 Junk.J]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
preset-synth-microfreak-parameter-payload-sha256:: 058eefa5bf65626a3721082811872acb0d0e6f6a20c2b4cbbf0b9ca749e77d8c
preset-synth-file:: [Hollows — October 25 slot 57 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___057%20Hollows___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: a73ac875ed2b10e959456a1c479799587db8ed899d05a7ce86465492b58dfafe
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 57 over USB on October 25, 2026 with `mise run microfreak:download --slot 57`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.1 slot 142, Factory 3.0 slot 142, Factory 6.0 slot 264). Comparison used `mise run microfreak:compare`.
		- [Download the slot 57 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___057%20Hollows___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/057 Hollows/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SuperWave. [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
		- Wave: 1 (stored choice code). Detune: 0.486. Volume: 0.620.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Band-pass filter. Saved cutoff: 0.602; resonance: 0.706. [[Microfreak/UG/07 Filter/01 Modifying Sound/02 Band Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.461, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.143, FallSlp 0.500, Hold 0.000, Amount 0.591. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.587. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: −0.048.
		- KEY/ARP → Cutoff: −0.041.
		- PRESSURE → Assign 1 → matrix amount LFO → Pitch: +0.010.
		- PRESSURE → Assign 2 → LFO Rate: +0.092.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
