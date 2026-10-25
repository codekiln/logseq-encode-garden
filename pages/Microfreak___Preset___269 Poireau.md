logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 269
preset-synth-microfreak-name:: Poireau
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/268 Melon]]
next:: [[Microfreak/Preset/270 Emo]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-microfreak-parameter-payload-sha256:: 364c11be7f2748d07cf989469a24265b017232a4b8bb23a954e82116e7a015c4
preset-synth-file:: [Poireau — October 25 slot 269 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___269%20Poireau___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 16b8c5ee4a9764df65fc50382a2c33f46d2473294ee57b7c67063ed41a165199
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 269 over USB on October 25, 2026 with `mise run microfreak:download --slot 269`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 335, Factory 6.0 slot 400). Comparison used `mise run microfreak:compare`.
		- [Download the slot 269 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___269%20Poireau___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/269 Poireau/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harm. [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
		- Spread: 0.040. Rectification: 0.457. Noise: 0.240.
		- Keyboard octave: +1. Glide: 0.151.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.540; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.405, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.451, FallSlp 0.500, Hold 0.000, Amount 0.301. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync on; stored division code: 1. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Wave: +0.516.
		- LFO → Timbre: +0.855.
		- ENV → Cutoff: +0.255.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
