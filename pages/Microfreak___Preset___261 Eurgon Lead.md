logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 261
preset-synth-microfreak-name:: Eurgon Lead
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Lead]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/260 8bitfi]]
next:: [[Microfreak/Preset/262 Pled]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
preset-synth-microfreak-parameter-payload-sha256:: 6b461c0230e528e578fe0a73848f11bf1e67b228907060dcb64680d3b8f1293b
preset-synth-file:: [Eurgon Lead — October 25 slot 261 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___261%20Eurgon%20Lead___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 8faaa85e0bd06736491b97418a5c95608e21b96fa8a59cb841a37dd5dbfb2b63
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 261 over USB on October 25, 2026 with `mise run microfreak:download --slot 261`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 328, Factory 6.0 slot 243). Comparison used `mise run microfreak:compare`.
		- [Download the slot 261 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___261%20Eurgon%20Lead___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/261 Eurgon Lead/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Bass. [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
		- Saturate: 0.121. Fold: 0.139. Noise: 0.000.
		- Keyboard octave: +1. Glide: 0.088.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.186; resonance: 0.233. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.371, sustain 0.642. Amp Mod is off. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.197, RiseSlp 0.500, FallLvl 0.163, FallSlp 0.500, Hold 0.000, Amount 0.841. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 9. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- PRESSURE → Wave: +0.212.
		- PRESSURE → Timbre: +0.112.
		- ENV → Cutoff: +0.355.
		- PRESSURE → Cutoff: +0.225.
		- KEY/ARP → Cutoff: +0.693.
		- PRESSURE → Assign 1 → matrix amount LFO → Pitch: +0.012.
		- PRESSURE → Assign 2 → Noise: +0.027.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
