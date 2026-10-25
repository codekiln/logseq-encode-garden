logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 109
preset-synth-microfreak-name:: VeloSparklz
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/108 ATZap]]
next:: [[Microfreak/Preset/110 F-Back]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/04 Harmo]]
preset-synth-microfreak-parameter-payload-sha256:: 42440e2c2c8196ce1b3092cabcdfdf1bc07a9bdd37ff8b6d9ad89ce604d4ac44
preset-synth-file:: [VeloSparklz — October 25 slot 109 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___109%20VeloSparklz___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: fff80f57eb5c23d277ed1ddce330b57e5b9410eee42210dd366369e834325bda
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 109 over USB on October 25, 2026 with `mise run microfreak:download --slot 109`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot None, Factory 1.1 slot 202, Factory 2.1 slot 19, Factory 3.0 slot 19, Factory 6.0 slot None). Comparison used `mise run microfreak:compare`.
		- [Download the slot 109 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___109%20VeloSparklz___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/109 VeloSparklz/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harmo. [[Microfreak/UG/06 Dig Osc/03 Types/04 Harmo]]
		- Content: 0.128. Sculpting: 0.153. Chorus: 0.457.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- High-pass filter. Saved cutoff: 1.000; resonance: 0.931. [[Microfreak/UG/07 Filter/01 Modifying Sound/03 High Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.110, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.245, RiseSlp 0.024, FallLvl 0.527, FallSlp 0.020, Hold 1.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold, clock sync off; stored normalized rate: 1.000. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: −0.500.
		- LFO → Pitch: +0.753.
		- ENV → Wave: +0.145.
		- ENV → Timbre: +0.265.
		- Cycling Envelope → Cutoff: −0.765.
		- ENV → Cutoff: −0.071.
		- KEY/ARP → Cutoff: +1.000.
		- Cycling Envelope → Assign 1 → matrix amount LFO → Pitch: −0.753.
		- Cycling Envelope → Assign 2 → Decay/Release: +0.519.
		- PRESSURE → Assign 2 → Decay/Release: −0.517.
		- PRESSURE → Assign 3 → Cycling Envelope Fall: −0.330.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
