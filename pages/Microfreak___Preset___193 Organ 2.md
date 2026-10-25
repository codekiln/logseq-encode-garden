logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 193
preset-synth-microfreak-name:: Organ 2
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Template]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/192 Organ 1]]
next:: [[Microfreak/Preset/194 Glass Organ]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
preset-synth-microfreak-parameter-payload-sha256:: 6a088f819d2c82e60cfcdb76d480180e7487b10e63edb87addd52e9e0460065d
preset-synth-file:: [Organ 2 — October 25 slot 193 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___193%20Organ%202___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 936fa411f1e4bfbc1e81bde995323ad201eff289bed18481ef46261a270bff14
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 193 over USB on October 25, 2026 with `mise run microfreak:download --slot 193`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 222, Factory 2.1 slot 36, Factory 3.0 slot 266, Factory 6.0 slot 340). Comparison used `mise run microfreak:compare`.
		- [Download the slot 193 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___193%20Organ%202___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/193 Organ 2/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Wavetable. [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
		- Table: 11 (stored choice code). Position: 0.441. Chorus: 0.000.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.677; resonance: 0.213. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.000, sustain 0.000. Amp Mod is off. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.157, RiseSlp 0.500, FallLvl 0.157, FallSlp 0.500, Hold 0.000, Amount 0.843. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.685. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Timbre: −1.000.
		- ENV → Cutoff: +0.863.
		- KEY/ARP → Cutoff: +0.693.
		- PRESSURE → Assign 1 → LFO Rate: −0.129.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
