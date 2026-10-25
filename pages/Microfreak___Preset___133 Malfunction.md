logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 133
preset-synth-microfreak-name:: Malfunction
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/132 Hold Riser]]
next:: [[Microfreak/Preset/134 Qbit Brass]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
preset-synth-microfreak-parameter-payload-sha256:: b12a6f434d31850e1929ff3351a62476a8eda1b41e5d37b14f9737f957af8091
preset-synth-file:: [Malfunction — October 25 slot 133 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___133%20Malfunction___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: e7c04bb80d8c0c297a6b31cb5838822b3c737416ba041837d6d0aaf93254a6f9
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 133 over USB on October 25, 2026 with `mise run microfreak:download --slot 133`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 11, Factory 2.1 slot None, Factory 3.0 slot 211, Factory 6.0 slot 348). Comparison used `mise run microfreak:compare`.
		- [Download the slot 133 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___133%20Malfunction___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/133 Malfunction/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Noise. [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
		- Wave: 0.333. Timbre: 1.000. Shape: 0.500.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.474; resonance: 0.474. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.491, sustain 0.136. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.081, RiseSlp 0.500, FallLvl 0.421, FallSlp 0.158, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync on; stored division code: 1. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: +0.001.
		- LFO → Wave: +1.000.
		- LFO → Timbre: +1.000.
		- Cycling Envelope → Cutoff: +0.101.
		- ENV → Cutoff: +0.120.
		- PRESSURE → Cutoff: +0.154.
		- KEY/ARP → Cutoff: +0.297.
		- KEY/ARP → Assign 1 → Filter Resonance: +1.000.
		- KEY/ARP → Assign 2 → Filter Resonance: −1.000.
		- LFO → Assign 3 → matrix amount LFO → Pitch: +0.023.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
