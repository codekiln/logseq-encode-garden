logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 294
preset-synth-microfreak-name:: Synchronizer
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Lead]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/293 Digital Roads]]
next:: [[Microfreak/Preset/295 Tactile Techno]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
preset-synth-microfreak-parameter-payload-sha256:: 4a27da5dfe4e9d6489900a2fc646bd75c86e071a2adb716e0d741a5aa8ebf533
preset-synth-file:: [Synchronizer — October 25 slot 294 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___294%20Synchronizer___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: edc2ea5eab13654117e543ff0650fbfd7fc3c983a8a08e6b771b82a351184b8a
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 294 over USB on October 25, 2026 with `mise run microfreak:download --slot 294`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 358, Factory 6.0 slot 394). Comparison used `mise run microfreak:compare`.
		- [Download the slot 294 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___294%20Synchronizer___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/294 Synchronizer/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SawX. [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
		- Saw Mod: 0.001. Shape: 1.000. Noise: 0.340.
		- Keyboard octave: -1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.298; resonance: 0.166. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.529, sustain 0.513. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.403, FallSlp 0.360, Hold 0.067, Amount 0.696. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync off; stored normalized rate: 0.585. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.002.
		- Cycling Envelope → Wave: +0.951.
		- KEY/ARP → Wave: −1.000.
		- Cycling Envelope → Timbre: −1.000.
		- KEY/ARP → Timbre: −0.657.
		- ENV → Cutoff: +0.730.
		- PRESSURE → Cutoff: −0.651.
		- KEY/ARP → Cutoff: −0.667.
		- PRESSURE → Assign 1 → Noise: −1.000.
		- LFO → Assign 2 → Cycling Envelope Hold: +0.011.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
