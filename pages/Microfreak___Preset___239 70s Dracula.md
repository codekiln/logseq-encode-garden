logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 239
preset-synth-microfreak-name:: 70s Dracula
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Lead]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/238 Deep Sea Call]]
next:: [[Microfreak/Preset/240 Move U Head]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-microfreak-parameter-payload-sha256:: 44587286f47ff1aead3f969378522cd8d277e3b2234a544ddd025a05bf9a06c8
preset-synth-file:: [70s Dracula — October 25 slot 239 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___239%2070s%20Dracula___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 7d5186426ce8f55ac2beef305342a0e65de6f17b24ef2e6d46e78f947089d116
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 239 over USB on October 25, 2026 with `mise run microfreak:download --slot 239`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 308, Factory 6.0 slot 366). Comparison used `mise run microfreak:compare`.
		- [Download the slot 239 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___239%2070s%20Dracula___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/239 70s Dracula/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harm. [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
		- Spread: 0.000. Rectification: 0.772. Noise: 0.221.
		- Keyboard octave: -2. Glide: 0.131.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.420; resonance: 0.691. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.300, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.673, RiseSlp 0.500, FallLvl 1.000, FallSlp 0.500, Hold 1.000, Amount 0.181. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold, clock sync on; stored division code: 12. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: +0.006.
		- LFO → Wave: −0.005.
		- Cycling Envelope → Timbre: +1.000.
		- ENV → Cutoff: +0.450.
		- PRESSURE → Cutoff: −0.161.
		- PRESSURE → Assign 1 → Noise: +1.000.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
