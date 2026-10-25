logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 218
preset-synth-microfreak-name:: Metal Sequence
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Percussion]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/217 Rectify]]
next:: [[Microfreak/Preset/219 Dusty Bass]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-microfreak-parameter-payload-sha256:: 5d5dbb1f892aa7bd1035a18fe3cacec2490b462ee311814e21315cba97de744a
preset-synth-file:: [Metal Sequence — October 25 slot 218 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___218%20Metal%20Sequence___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 486d12099bfa4daae1010a610cbd6d1b85eb3eb9e75e1779343399b8f9f86208
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 218 over USB on October 25, 2026 with `mise run microfreak:download --slot 218`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 289, Factory 6.0 slot 189). Comparison used `mise run microfreak:compare`.
		- [Download the slot 218 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___218%20Metal%20Sequence___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/218 Metal Sequence/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harm. [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
		- Spread: 0.143. Rectification: 0.283. Noise: 0.462.
		- Keyboard octave: 0. Glide: 0.071.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.341; resonance: 0.493. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.174, sustain 0.085. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.592, RiseSlp 0.938, FallLvl 0.167, FallSlp 0.136, Hold 0.000, Amount 0.685. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold Filtered, clock sync off; stored normalized rate: 0.899. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ENV → Pitch: +0.007.
		- Cycling Envelope → Wave: +0.362.
		- PRESSURE → Wave: −0.061.
		- Cycling Envelope → Timbre: +0.523.
		- LFO → Timbre: +0.555.
		- PRESSURE → Timbre: −0.489.
		- Cycling Envelope → Cutoff: +0.281.
		- ENV → Cutoff: +0.514.
		- LFO → Cutoff: +0.019.
		- Cycling Envelope → Assign 1 → LFO Rate: +0.808.
		- ENV → Assign 1 → LFO Rate: +0.028.
		- LFO → Assign 1 → LFO Rate: +0.471.
		- Cycling Envelope → Assign 2 → Rectification: +0.774.
		- ENV → Assign 2 → Rectification: −0.001.
		- LFO → Assign 2 → Rectification: +0.391.
		- Cycling Envelope → Assign 3 → Cycling Envelope Amount: −0.188.
		- LFO → Assign 3 → Cycling Envelope Amount: +0.173.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
