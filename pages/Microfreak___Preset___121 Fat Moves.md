logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 121
preset-synth-microfreak-name:: Fat Moves
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/120 Jobs 4 Rhythm]]
next:: [[Microfreak/Preset/122 Simon Says]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
preset-synth-microfreak-parameter-payload-sha256:: e49f72762618974992f174af5e5172f1874b946cfbb57e146f5252250dcc166d
preset-synth-file:: [Fat Moves — October 25 slot 121 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___121%20Fat%20Moves___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 6313eda6aaacc797bbaac1d90bba881dc2907f2eaea8921eac6815aca8934f46
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 121 over USB on October 25, 2026 with `mise run microfreak:download --slot 121`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 9, Factory 2.1 slot None, Factory 3.0 slot 200, Factory 6.0 slot 388). Comparison used `mise run microfreak:compare`.
		- [Download the slot 121 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___121%20Fat%20Moves___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/121 Fat Moves/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SuperWave. [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
		- Wave: 0 (stored choice code). Detune: 0.333. Volume: 0.747.
		- Keyboard octave: 0. Glide: 0.150.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.121; resonance: 0.435. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.013, decay/release 0.396, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.163, RiseSlp 0.500, FallLvl 0.163, FallSlp 0.500, Hold 0.000, Amount 0.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync off; stored normalized rate: 0.906. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: +0.006.
		- ENV → Cutoff: +0.750.
		- KEY/ARP → Cutoff: +0.604.
		- PRESSURE → Assign 1 → Detune: +0.416.
		- KEY/ARP → Assign 1 → Detune: +0.500.
		- KEY/ARP → Assign 2 → Volume: +0.499.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
