logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 160
preset-synth-microfreak-name:: Incoming Ship
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/159 Snow Man]]
next:: [[Microfreak/Preset/161 Crackle Sleep]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
preset-synth-microfreak-parameter-payload-sha256:: 508f3ebe705583f12fc5ccc84f35bb2db797bc5f3dfb24e57a236dc521ea39d6
preset-synth-file:: [Incoming Ship — October 25 slot 160 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___160%20Incoming%20Ship___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: c095f96461f2f3fa3e1053a6f1dc64a92f5d6427a8983f90c2473f56c2a58604
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 160 over USB on October 25, 2026 with `mise run microfreak:download --slot 160`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 134, Factory 2.1 slot 236, Factory 3.0 slot 236, Factory 6.0 slot 404). Comparison used `mise run microfreak:compare`.
		- [Download the slot 160 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___160%20Incoming%20Ship___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/160 Incoming Ship/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Noise. [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
		- Wave: 0.790. Timbre: 0.500. Shape: 0.506.
		- Keyboard octave: -1. Glide: 0.000.
	- ## Filter
		- High-pass filter. Saved cutoff: 0.403; resonance: 0.887. [[Microfreak/UG/07 Filter/01 Modifying Sound/03 High Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.970, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.070, FallSlp 0.500, Hold 0.000, Amount 0.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold, clock sync on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ENV → Wave: −0.710.
		- ENV → Timbre: +0.339.
		- KEY/ARP → Timbre: +1.000.
		- ENV → Cutoff: +0.385.
		- Cycling Envelope → Assign 1 → matrix amount LFO → Timbre: +0.190.
		- ENV → Assign 2 → Shape: +0.500.
		- LFO → Assign 2 → Shape: +1.000.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
