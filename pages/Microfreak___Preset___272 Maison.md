logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 272
preset-synth-microfreak-name:: Maison
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/271 Debout]]
next:: [[Microfreak/Preset/273 Good]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
preset-synth-microfreak-parameter-payload-sha256:: 98892051b6e699deb8f14a34a8239a8839c878795d731d568a67dea5332dc89f
preset-synth-file:: [Maison — October 25 slot 272 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___272%20Maison___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 59d99fb2bd3504cdf16695bdbeaa3218845f94325a084b37d0a2ad1de0e2b80e
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 272 over USB on October 25, 2026 with `mise run microfreak:download --slot 272`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 338, Factory 6.0 slot 22). Comparison used `mise run microfreak:compare`.
		- [Download the slot 272 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___272%20Maison___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/272 Maison/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Chords. [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
		- Type: 3 (stored choice code). Inv/Transp: 0.240. Shape control: 0.531.
		- Keyboard octave: 0. Glide: 0.193.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.482; resonance: 0.432. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.277, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.319, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sawtooth, clock sync on; stored division code: 6. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ENV → Timbre: +0.062.
		- ENV → Cutoff: +0.393.
		- LFO → Cutoff: −0.529.
		- Cycling Envelope → Assign 1 → Shape: +0.159.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
