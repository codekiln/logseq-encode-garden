logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 298
preset-synth-microfreak-name:: King Snap
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/297 Shiny Hat]]
next:: [[Microfreak/Preset/299 I Saw It B4]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
preset-synth-microfreak-parameter-payload-sha256:: 02f736c45bb6ab326d2c0665548db9d0f996cbee18c08f025fe6a5b3e693f121
preset-synth-file:: [King Snap — October 25 slot 298 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___298%20King%20Snap___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: e141e7209e7066f75e247e1d645eeff96a6c313dc2968d189569f0047bc03b46
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 298 over USB on October 25, 2026 with `mise run microfreak:download --slot 298`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 361, Factory 6.0 slot 285). Comparison used `mise run microfreak:compare`.
		- [Download the slot 298 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___298%20King%20Snap___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/298 King Snap/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Bass. [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
		- Saturate: 0.379. Fold: 0.000. Noise: 0.000.
		- Keyboard octave: -1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.176; resonance: 0.670. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.085, sustain 0.257. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.303, FallSlp 0.423, Hold 0.000, Amount 0.276. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.673. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: +0.005.
		- Cycling Envelope → Timbre: +0.861.
		- ENV → Cutoff: +0.506.
		- PRESSURE → Cutoff: +0.229.
		- Cycling Envelope → Assign 1 → Sustain: −1.000.
		- KEY/ARP → Assign 2 → LFO Rate: +1.000.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
