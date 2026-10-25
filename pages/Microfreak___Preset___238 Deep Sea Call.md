logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 238
preset-synth-microfreak-name:: Deep Sea Call
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Keys]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/237 Funk Blaster]]
next:: [[Microfreak/Preset/239 70s Dracula]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-microfreak-parameter-payload-sha256:: ca8f6f1f5719cd064311130fcca5198315bd0317f047b6a56ccf76a998cbc476
preset-synth-file:: [Deep Sea Call — October 25 slot 238 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___238%20Deep%20Sea%20Call___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 6aac1086f567f0ce8a0140ab6262f21bb86027109144e7a1cb72cb11a497cf6e
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 238 over USB on October 25, 2026 with `mise run microfreak:download --slot 238`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 307, Factory 6.0 slot 406). Comparison used `mise run microfreak:compare`.
		- [Download the slot 238 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___238%20Deep%20Sea%20Call___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/238 Deep Sea Call/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harm. [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
		- Spread: 0.409. Rectification: 0.752. Noise: 0.007.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.135; resonance: 0.639. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.156, decay/release 0.560, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.716, RiseSlp 0.500, FallLvl 0.534, FallSlp 0.500, Hold 0.000, Amount 0.604. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold Filtered, clock sync on; stored division code: 0. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ENV → Pitch: +0.005.
		- Cycling Envelope → Wave: +0.071.
		- LFO → Timbre: +0.364.
		- ENV → Cutoff: +0.367.
		- PRESSURE → Cutoff: +0.394.
		- ENV → Assign 3 → Filter Resonance: −0.316.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
