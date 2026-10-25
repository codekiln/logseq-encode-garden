logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 236
preset-synth-microfreak-name:: Fastrun
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Percussion]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/235 Shy Robot]]
next:: [[Microfreak/Preset/237 Funk Blaster]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
preset-synth-microfreak-parameter-payload-sha256:: 4e6ef92dec26ab31f8500cebac1773588fcb169573def5e663873b871cc147a4
preset-synth-file:: [Fastrun — October 25 slot 236 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___236%20Fastrun___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 59ca22408b008c2608ad9ce77b4cf64c9e255840c98bba325f163f01576a5391
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 236 over USB on October 25, 2026 with `mise run microfreak:download --slot 236`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 305, Factory 6.0 slot 269). Comparison used `mise run microfreak:compare`.
		- [Download the slot 236 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___236%20Fastrun___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/236 Fastrun/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Two Op. FM. [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
		- Ratio: 0.274. Amount: 0.000. Shape: 0.000.
		- Keyboard octave: 0. Glide: 0.268.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.394; resonance: 0.555. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.000, sustain 0.000. Amp Mod is off. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.026, RiseSlp 0.000, FallLvl 0.305, FallSlp 0.000, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold Filtered, clock sync on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.348.
		- Cycling Envelope → Wave: +1.000.
		- Cycling Envelope → Timbre: +1.000.
		- Cycling Envelope → Cutoff: +0.514.
		- ENV → Cutoff: +0.585.
		- LFO → Cutoff: +0.618.
		- KEY/ARP → Cutoff: +0.797.
		- LFO → Assign 1 → Cycling Envelope Fall: +0.296.
		- LFO → Assign 2 → Oscillator Type: −0.120.
		- LFO → Assign 3 → Decay/Release: +0.881.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
