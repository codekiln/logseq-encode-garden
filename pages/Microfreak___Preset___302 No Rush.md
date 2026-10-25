logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 302
preset-synth-microfreak-name:: No Rush
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Lead]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/301 Perculiar Bass]]
next:: [[Microfreak/Preset/303 2020 Behind]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-microfreak-parameter-payload-sha256:: 974fcfb97143747aaaa74ce8604936d420026d6ba72e79bedd4546984204d071
preset-synth-file:: [No Rush — October 25 slot 302 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___302%20No%20Rush___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: b45a2982d1128052cd05087b2df72e37133d609cb8ce5ed70081dea97f81fd2f
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 302 over USB on October 25, 2026 with `mise run microfreak:download --slot 302`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 365, Factory 6.0 slot 395). Comparison used `mise run microfreak:compare`.
		- [Download the slot 302 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___302%20No%20Rush___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/302 No Rush/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harm. [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
		- Spread: 0.999. Rectification: 0.566. Noise: 0.704.
		- Keyboard octave: -1. Glide: 0.000.
	- ## Filter
		- Band-pass filter. Saved cutoff: 0.201; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/02 Band Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.507, sustain 0.418. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.721, FallSlp 0.000, Hold 0.000, Amount 0.137. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync off; stored normalized rate: 0.486. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +1.000.
		- LFO → Pitch: +0.004.
		- KEY/ARP → Pitch: +0.003.
		- Cycling Envelope → Wave: −1.000.
		- ENV → Cutoff: +0.339.
		- KEY/ARP → Cutoff: +0.706.
		- ENV → Assign 1 → Cycling Envelope Hold: −0.993.
		- PRESSURE → Assign 2 → LFO Rate: +0.130.
		- PRESSURE → Assign 3 → Sustain: +0.124.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
