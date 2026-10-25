logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 246
preset-synth-microfreak-name:: Queity
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/245 GivemeSub]]
next:: [[Microfreak/Preset/247 Laity]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
preset-synth-microfreak-parameter-payload-sha256:: 6a4110869273e9664ab9d5b3e37f0f14f91932db13e3483ac8eb972e4831c50a
preset-synth-file:: [Queity — October 25 slot 246 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___246%20Queity___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 1acfa125bc19633df18524a019f7d67f49358f108b343b572d2f184f4f5369de
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 246 over USB on October 25, 2026 with `mise run microfreak:download --slot 246`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 314, Factory 6.0 slot 14). Comparison used `mise run microfreak:compare`.
		- [Download the slot 246 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___246%20Queity___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/246 Queity/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SawX. [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
		- Saw Mod: 0.000. Shape: 0.003. Noise: 0.000.
		- Keyboard octave: -2. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.494; resonance: 0.599. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.195, sustain 0.543. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.573, RiseSlp 0.500, FallLvl 0.547, FallSlp 0.500, Hold 0.177, Amount 0.478. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold, clock sync on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: +0.001.
		- Cycling Envelope → Wave: +0.384.
		- ENV → Wave: +0.026.
		- Cycling Envelope → Timbre: +0.415.
		- ENV → Timbre: −0.732.
		- ENV → Cutoff: +0.101.
		- PRESSURE → Cutoff: +0.105.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
