logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 257
preset-synth-microfreak-name:: Power Touch
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/256 Fmit]]
next:: [[Microfreak/Preset/258 Glip]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
preset-synth-microfreak-parameter-payload-sha256:: a10e654667aefe4170d1d8827ed00465141d3dd5d8f65620e84bcfa608bc4650
preset-synth-file:: [Power Touch — October 25 slot 257 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___257%20Power%20Touch___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 0fa7bfb384956024ed46b0153891ad7763d09ccb104fe7033599e5ccfd881dd1
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 257 over USB on October 25, 2026 with `mise run microfreak:download --slot 257`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 324, Factory 6.0 slot 349). Comparison used `mise run microfreak:compare`.
		- [Download the slot 257 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___257%20Power%20Touch___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/257 Power Touch/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SawX. [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
		- Saw Mod: 0.000. Shape: 0.000. Noise: 0.000.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Band-pass filter. Saved cutoff: 0.441; resonance: 0.664. [[Microfreak/UG/07 Filter/01 Modifying Sound/02 Band Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.176, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.054, RiseSlp 0.500, FallLvl 0.050, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold Filtered, clock sync on; stored division code: 6. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +1.000.
		- PRESSURE → Wave: +0.051.
		- PRESSURE → Timbre: +0.045.
		- ENV → Cutoff: +0.059.
		- PRESSURE → Cutoff: +0.363.
		- KEY/ARP → Cutoff: +1.000.
		- PRESSURE → Assign 1 → Cycling Envelope Fall: +0.168.
		- KEY/ARP → Assign 1 → Cycling Envelope Fall: +0.592.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
