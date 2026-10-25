logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 086
preset-synth-microfreak-name:: Whimsy
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Pad]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/085 Arp 2ol9]]
next:: [[Microfreak/Preset/087 ATSpookBass]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/04 Harmo]]
preset-synth-microfreak-parameter-payload-sha256:: 661c3103972f4412b518f82b322d8202cbf61b94e1a63413ce898a5212819465
preset-synth-file:: [Whimsy — October 25 slot 86 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___086%20Whimsy___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 21ac0c5296208e42ce4031dcf7106209ee811c600b2de374bccbeb146486a394
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 86 over USB on October 25, 2026 with `mise run microfreak:download --slot 86`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0 (Factory 1.0 slot 173, Factory 1.1 slot 173, Factory 2.1 slot 169, Factory 3.0 slot 169). Comparison used `mise run microfreak:compare`.
		- [Download the slot 86 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___086%20Whimsy___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/086 Whimsy/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harmo. [[Microfreak/UG/06 Dig Osc/03 Types/04 Harmo]]
		- Content: 0.000. Sculpting: 0.000. Chorus: 0.000.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.723; resonance: 0.077. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.473, decay/release 0.467, sustain 0.619. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.158, RiseSlp 0.500, FallLvl 0.151, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold Filtered, clock sync on; stored division code: 8. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- PRESSURE → Wave: +0.263.
		- Cycling Envelope → Timbre: +0.678.
		- LFO → Timbre: +0.293.
		- ENV → Cutoff: −0.253.
		- PRESSURE → Cutoff: +0.170.
		- LFO → Assign 1 → Chorus: +0.169.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
