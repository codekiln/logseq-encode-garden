logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 244
preset-synth-microfreak-name:: Nebem
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Keys]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/243 Noisy]]
next:: [[Microfreak/Preset/245 GivemeSub]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
preset-synth-microfreak-parameter-payload-sha256:: ca6c94828f44af2afd980892c0228285788920cf7d53b2176f879a1157a78a70
preset-synth-file:: [Nebem — October 25 slot 244 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___244%20Nebem___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 83a3d4e0304116abd27d6c6aa2f518eb671979087ba22641e4fea45c52325f78
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 244 over USB on October 25, 2026 with `mise run microfreak:download --slot 244`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 312, Factory 6.0 slot 125). Comparison used `mise run microfreak:compare`.
		- [Download the slot 244 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___244%20Nebem___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/244 Nebem/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SawX. [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
		- Saw Mod: 0.021. Shape: 0.666. Noise: 0.021.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.538; resonance: 0.625. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.512, sustain 0.665. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.492, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.404. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: +0.003.
		- Cycling Envelope → Wave: +0.010.
		- Cycling Envelope → Timbre: +0.097.
		- ENV → Cutoff: +0.341.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
