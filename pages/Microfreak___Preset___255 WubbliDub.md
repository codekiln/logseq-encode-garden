logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 255
preset-synth-microfreak-name:: WubbliDub
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/254 Comb-Me]]
next:: [[Microfreak/Preset/256 Fmit]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
preset-synth-microfreak-parameter-payload-sha256:: 2dfd488968f2997aa652e23053432e9b830bf5d2b6c77f08ba1a6fe92ebf9faa
preset-synth-file:: [WubbliDub — October 25 slot 255 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___255%20WubbliDub___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 302e65a713850fceae27fb8252ff5a17f0b180a50c91aa952c6148565b90cebe
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 255 over USB on October 25, 2026 with `mise run microfreak:download --slot 255`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 322, Factory 6.0 slot 415). Comparison used `mise run microfreak:compare`.
		- [Download the slot 255 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___255%20WubbliDub___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/255 WubbliDub/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Two Op. FM. [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
		- Ratio: 0.999. Amount: 0.880. Shape: 0.513.
		- Keyboard octave: -2. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.103; resonance: 0.558. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.212, decay/release 0.169, sustain 0.485. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.235, RiseSlp 0.847, FallLvl 0.418, FallSlp 0.104, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 6. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Wave: −0.022.
		- PRESSURE → Wave: +0.028.
		- Cycling Envelope → Timbre: +1.000.
		- Cycling Envelope → Cutoff: +0.369.
		- ENV → Cutoff: +0.031.
		- KEY/ARP → Cutoff: +0.079.
		- Cycling Envelope → Assign 1 → Shape: +0.112.
		- PRESSURE → Assign 2 → Cycling Envelope Rise: +0.014.
		- PRESSURE → Assign 3 → Cycling Envelope Fall: −0.385.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
