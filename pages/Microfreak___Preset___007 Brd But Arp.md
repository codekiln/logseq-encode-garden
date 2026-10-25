logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 007
preset-synth-microfreak-name:: Brd But Arp
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/006 Aft-WavPad]]
next:: [[Microfreak/Preset/008 Invitation]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
preset-synth-microfreak-parameter-payload-sha256:: 20016868adeb8c7287650ffdb5ac35fc40e0d26c0c1993f8e765f12e4c51b13b
preset-synth-file:: [Brd But Arp — October 25 slot 7 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___007%20Brd%20But%20Arp___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 85e298a76e490653ae95b732cb30e6314350f77edf690669730254a6dc8f04c8
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 7 over USB on October 25, 2026 with `mise run microfreak:download --slot 7`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 7, Factory 2.1 slot 7, Factory 3.0 slot 7, Factory 6.0 slot None). Comparison used `mise run microfreak:compare`.
		- [Download the slot 7 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___007%20Brd%20But%20Arp___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/007 Brd But Arp/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Two Op. FM. [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
		- Ratio: 0.242. Amount: 0.504. Shape: 0.971.
		- Keyboard octave: -1. Glide: 0.124.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.286; resonance: 0.325. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.264, sustain 0.131. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.605, RiseSlp 0.500, FallLvl 0.703, FallSlp 0.500, Hold 0.215, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.040. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Wave: +0.010.
		- Cycling Envelope → Timbre: +0.135.
		- KEY/ARP → Timbre: +0.446.
		- ENV → Cutoff: +0.552.
		- LFO → Cutoff: +0.198.
		- PRESSURE → Cutoff: −0.550.
		- KEY/ARP → Cutoff: +0.847.
		- LFO → Assign 1 → Decay/Release: +0.028.
		- LFO → Assign 2 → Shape: −0.163.
		- LFO → Assign 3 → matrix amount ENV → Cutoff: −0.221.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
