logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 116
preset-synth-microfreak-name:: Analog Chaser
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/115 Notobeat]]
next:: [[Microfreak/Preset/117 Minor Pad]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
preset-synth-microfreak-parameter-payload-sha256:: b10bee474de61f3f36a90829494d215bd2ce0b4df03f55416de3d91c5b696842
preset-synth-file:: [Analog Chaser — October 25 slot 116 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___116%20Analog%20Chaser___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: a4ec1d179de154900e2c88540a51a0154976433023ee9645a7c42a4bae3118a2
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 116 over USB on October 25, 2026 with `mise run microfreak:download --slot 116`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 4, Factory 2.1 slot None, Factory 3.0 slot 196, Factory 6.0 slot 342). Comparison used `mise run microfreak:compare`.
		- [Download the slot 116 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___116%20Analog%20Chaser___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/116 Analog Chaser/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: V.Analog. [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
		- Detune: 0.276. Shape: 0.476. Wave: 0.395.
		- Keyboard octave: 0. Glide: 0.084.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.030; resonance: 0.190. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.245, sustain 0.502. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.271, RiseSlp 0.500, FallLvl 0.326, FallSlp 0.500, Hold 0.184, Amount 0.540. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sawtooth, clock sync on; stored division code: 9. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Timbre: −0.084.
		- Cycling Envelope → Cutoff: +0.250.
		- ENV → Cutoff: +0.645.
		- LFO → Assign 1 → Sustain: +0.360.
		- ENV → Assign 2 → Filter Resonance: +0.152.
		- Cycling Envelope → Assign 3 → Decay/Release: +0.074.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
