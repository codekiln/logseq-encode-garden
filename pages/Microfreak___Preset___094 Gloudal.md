logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 094
preset-synth-microfreak-name:: Gloudal
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Keys]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/093 Blind]]
next:: [[Microfreak/Preset/095 Boers]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
preset-synth-microfreak-parameter-payload-sha256:: b83481b2d445e17526015489a82fab80a6ced4cd47e32e86bf2189020d3593d2
preset-synth-file:: [Gloudal — October 25 slot 94 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___094%20Gloudal___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 83cbbb91f4e8686bc05e2d95969c0b19ebabc92d2dc75e5edcf0ad3a80a2ff90
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 94 over USB on October 25, 2026 with `mise run microfreak:download --slot 94`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot 181, Factory 1.1 slot 181, Factory 2.1 slot 176, Factory 3.0 slot 176, Factory 6.0 slot 145). Comparison used `mise run microfreak:compare`.
		- [Download the slot 94 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___094%20Gloudal___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/094 Gloudal/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Wavetable. [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
		- Table: 15 (stored choice code). Position: 0.214. Chorus: 0.911.
		- Keyboard octave: 0. Glide: 0.156.
	- ## Filter
		- High-pass filter. Saved cutoff: 0.633; resonance: 0.789. [[Microfreak/UG/07 Filter/01 Modifying Sound/03 High Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.869, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.242, RiseSlp 0.500, FallLvl 0.176, FallSlp 0.500, Hold 0.059, Amount 0.074. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sawtooth, clock sync on; stored division code: 4. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.053.
		- ENV → Cutoff: −0.612.
		- KEY/ARP → Cutoff: +1.000.
		- LFO → Assign 1 → Chorus: +0.484.
		- KEY/ARP → Assign 1 → Chorus: +1.000.
		- PRESSURE → Assign 2 → Cycling Envelope Amount: +1.000.
		- Cycling Envelope → Assign 3 → Glide: +0.245.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
