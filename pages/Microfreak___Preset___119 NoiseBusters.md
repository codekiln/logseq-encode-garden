logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 119
preset-synth-microfreak-name:: NoiseBusters
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Keys]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/118 Fight]]
next:: [[Microfreak/Preset/120 Jobs 4 Rhythm]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
preset-synth-microfreak-parameter-payload-sha256:: 9ad0fd7a87ad623d512f004fe1a0a4cfb441a58537173547aacbfce4c8fe8cd2
preset-synth-file:: [NoiseBusters — October 25 slot 119 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___119%20NoiseBusters___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 7c05681f3deaa1b1eb87db2e7ec2f226eda0e21cbced0ae57c1cc2ab7ac63ccd
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 119 over USB on October 25, 2026 with `mise run microfreak:download --slot 119`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 7, Factory 2.1 slot None, Factory 3.0 slot 199, Factory 6.0 slot 307). Comparison used `mise run microfreak:compare`.
		- [Download the slot 119 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___119%20NoiseBusters___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/119 NoiseBusters/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Noise. [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
		- Wave: 0.374. Timbre: 0.790. Shape: 0.710.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.174; resonance: 0.415. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.510, sustain 0.430. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.233, RiseSlp 1.000, FallLvl 0.222, FallSlp 1.000, Hold 0.217, Amount 0.236. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold, clock sync off; stored normalized rate: 0.999. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.002.
		- KEY/ARP → Pitch: −0.001.
		- Cycling Envelope → Wave: −0.710.
		- Cycling Envelope → Timbre: −1.000.
		- KEY/ARP → Timbre: +1.000.
		- ENV → Cutoff: +0.378.
		- PRESSURE → Cutoff: +0.373.
		- KEY/ARP → Cutoff: +0.605.
		- Cycling Envelope → Assign 1 → LFO Rate: −1.000.
		- LFO → Assign 1 → LFO Rate: +0.379.
		- KEY/ARP → Assign 1 → LFO Rate: +1.000.
		- LFO → Assign 2 → Cycling Envelope Amount: +0.410.
		- LFO → Assign 3 → Cycling Envelope Fall: +0.302.
		- KEY/ARP → Assign 3 → Cycling Envelope Fall: +0.014.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
