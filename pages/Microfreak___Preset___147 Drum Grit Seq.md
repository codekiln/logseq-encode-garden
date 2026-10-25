logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 147
preset-synth-microfreak-name:: Drum Grit Seq
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Percussion]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/146 Snare Seq 1]]
next:: [[Microfreak/Preset/148 Mad Drums]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
preset-synth-microfreak-parameter-payload-sha256:: 1818f26c1222257a6fc4dc384bf3898bb6059aa00a0dda75ee57133db1ee57fe
preset-synth-file:: [Drum Grit Seq — October 25 slot 147 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___147%20Drum%20Grit%20Seq___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: dc0c42d91348229531203cb4ebae055142c754d678f02a8cee8c44536aa7c1f6
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 147 over USB on October 25, 2026 with `mise run microfreak:download --slot 147`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 122, Factory 2.1 slot 224, Factory 3.0 slot 224, Factory 6.0 slot 339). Comparison used `mise run microfreak:compare`.
		- [Download the slot 147 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___147%20Drum%20Grit%20Seq___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/147 Drum Grit Seq/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Noise. [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
		- Wave: 0.860. Timbre: 0.500. Shape: 0.518.
		- Keyboard octave: -1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.000; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.225, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.187, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 0. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.650.
		- KEY/ARP → Timbre: +1.000.
		- ENV → Cutoff: +0.498.
		- KEY/ARP → Cutoff: +0.221.
		- KEY/ARP → Assign 1 → Decay/Release: +0.010.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
