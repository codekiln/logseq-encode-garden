logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 251
preset-synth-microfreak-name:: Trinity
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Lead]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/250 Organic Random]]
next:: [[Microfreak/Preset/252 Monotron]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
preset-synth-microfreak-parameter-payload-sha256:: d6344757abe089a63c9055fe304ac390e3fe0d1c9865ebf1afe6917483876e11
preset-synth-file:: [Trinity — October 25 slot 251 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___251%20Trinity___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 592bfc496a1afb1539755fb013cca5503cebbe1b5461538d588387c00cbb5b8d
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 251 over USB on October 25, 2026 with `mise run microfreak:download --slot 251`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 319, Factory 6.0 slot 430). Comparison used `mise run microfreak:compare`.
		- [Download the slot 251 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___251%20Trinity___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/251 Trinity/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SawX. [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
		- Saw Mod: 0.000. Shape: 0.179. Noise: 0.000.
		- Keyboard octave: -1. Glide: 0.000.
	- ## Filter
		- Band-pass filter. Saved cutoff: 0.052; resonance: 0.602. [[Microfreak/UG/07 Filter/01 Modifying Sound/02 Band Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.102, sustain 0.619. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.747, RiseSlp 0.626, FallLvl 0.743, FallSlp 0.238, Hold 0.000, Amount 0.302. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold Filtered, clock sync on; stored division code: 4. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Wave: +0.045.
		- LFO → Wave: +0.068.
		- PRESSURE → Wave: +0.120.
		- Cycling Envelope → Timbre: +0.432.
		- LFO → Timbre: −0.182.
		- PRESSURE → Timbre: +0.090.
		- Cycling Envelope → Cutoff: +0.999.
		- ENV → Cutoff: +0.223.
		- LFO → Cutoff: +0.124.
		- PRESSURE → Cutoff: +0.064.
		- LFO → Assign 3 → Decay/Release: +0.030.
		- PRESSURE → Assign 3 → Decay/Release: +0.067.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
