logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 058
preset-synth-microfreak-name:: Junk.J
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/057 Hollows]]
next:: [[Microfreak/Preset/059 Suby Rainbow]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
preset-synth-microfreak-parameter-payload-sha256:: 8b008c9feb738a02d4a880d49677364c40e694569f98df63e5849d074d1c5178
preset-synth-file:: [Junk.J — October 25 slot 58 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___058%20Junk.J___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 5d459f704e4db293db3acfc8cf29c716d6251b34c1f9bf0f2b0f6bbc0bc52dea
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 58 over USB on October 25, 2026 with `mise run microfreak:download --slot 58`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot None, Factory 1.1 slot 143, Factory 2.1 slot 143, Factory 3.0 slot 143, Factory 6.0 slot 220). Comparison used `mise run microfreak:compare`.
		- [Download the slot 58 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___058%20Junk.J___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/058 Junk.J/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Two Op. FM. [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
		- Ratio: 0.825. Amount: 0.486. Shape: 0.000.
		- Keyboard octave: +2. Glide: 0.000.
	- ## Filter
		- High-pass filter. Saved cutoff: 0.145; resonance: 0.797. [[Microfreak/UG/07 Filter/01 Modifying Sound/03 High Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.143, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.000, RiseSlp 0.000, FallLvl 0.085, FallSlp 0.000, Hold 0.000, Amount 0.938. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold, clock sync off; stored normalized rate: 0.320. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.161.
		- KEY/ARP → Pitch: +1.000.
		- LFO → Wave: +0.378.
		- LFO → Timbre: −0.396.
		- Cycling Envelope → Cutoff: +0.851.
		- ENV → Cutoff: −0.277.
		- LFO → Cutoff: +0.353.
		- KEY/ARP → Cutoff: +1.000.
		- LFO → Assign 2 → Cycling Envelope Fall: +0.004.
		- LFO → Assign 3 → `Mat.Assign3`: −0.410.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
