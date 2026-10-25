logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 245
preset-synth-microfreak-name:: GivemeSub
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/244 Nebem]]
next:: [[Microfreak/Preset/246 Queity]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-microfreak-parameter-payload-sha256:: bbdec4cadf584db40464d249da2ae9fd44a2dee9cc628ac00ce092c3280c4440
preset-synth-file:: [GivemeSub — October 25 slot 245 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___245%20GivemeSub___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: b9f3976c91b990373094d9af71fbe7be737fe552c0d16e43a92e6b87c2bfec79
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 245 over USB on October 25, 2026 with `mise run microfreak:download --slot 245`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 313, Factory 6.0 slot 100). Comparison used `mise run microfreak:compare`.
		- [Download the slot 245 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___245%20GivemeSub___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/245 GivemeSub/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harm. [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
		- Spread: 0.526. Rectification: 0.068. Noise: 0.283.
		- Keyboard octave: -2. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.088; resonance: 0.936. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.022, decay/release 0.190, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.120, FallSlp 0.500, Hold 0.000, Amount 0.184. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sawtooth, clock sync off; stored normalized rate: 0.146. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- PRESSURE → Pitch: +0.050.
		- Cycling Envelope → Cutoff: +0.499.
		- ENV → Cutoff: +0.127.
		- LFO → Cutoff: +0.017.
		- PRESSURE → Assign 1 → LFO Rate: +0.497.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
