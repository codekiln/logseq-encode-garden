logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 080
preset-synth-microfreak-name:: Traditon
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/079 ArpZap]]
next:: [[Microfreak/Preset/081 Gaming]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
preset-synth-microfreak-parameter-payload-sha256:: 3cb4d59a568d28c4400f2a0b8135946765989bf95b20a8b6fdeddbb3cba9360f
preset-synth-file:: [Traditon — October 25 slot 80 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___080%20Traditon___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: eb30ab03496010ca6359a3d68d798bc86e95f72166c6969fbc140c522f64728b
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 80 over USB on October 25, 2026 with `mise run microfreak:download --slot 80`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 166, Factory 2.1 slot 163, Factory 3.0 slot 163, Factory 6.0 slot 7). Comparison used `mise run microfreak:compare`.
		- [Download the slot 80 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___080%20Traditon___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/080 Traditon/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: V.Analog. [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
		- Detune: 0.641. Shape: 0.556. Wave: 0.503.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.351; resonance: 0.565. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.198, sustain 0.413. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.171, RiseSlp 0.500, FallLvl 0.106, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold Filtered, clock sync on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ENV → Cutoff: +0.813.
		- PRESSURE → Cutoff: −0.089.
		- KEY/ARP → Cutoff: +1.000.
		- Cycling Envelope → Assign 1 → Filter Resonance: +0.205.
		- LFO → Assign 2 → Wave: +0.304.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
