logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 064
preset-synth-microfreak-name:: Mood
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Keys]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/063 Kendrok]]
next:: [[Microfreak/Preset/065 Cafe Chord]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
preset-synth-microfreak-parameter-payload-sha256:: ecbe3e9fbcc48515d3743cd415d17bc4b1aa81b876bbd8f043684b0affd27785
preset-synth-file:: [Mood — October 25 slot 64 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___064%20Mood___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 548bcb24066fa763168e57b4c7b22c21c8cc5f9ac5779024d67270ce5a9bd047
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 64 over USB on October 25, 2026 with `mise run microfreak:download --slot 64`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot 150, Factory 1.1 slot 150, Factory 2.1 slot 149, Factory 3.0 slot 149, Factory 6.0 slot 301). Comparison used `mise run microfreak:compare`.
		- [Download the slot 64 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___064%20Mood___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/064 Mood/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Chords. [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
		- Type: 0 (stored choice code). Inv/Transp: 0.000. Shape control: 1.000.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.513; resonance: 0.488. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.161, decay/release 0.780, sustain 0.474. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.352, RiseSlp 0.500, FallLvl 0.269, FallSlp 0.500, Hold 0.104, Amount 0.917. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 46877. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ENV → Timbre: +0.647.
		- PRESSURE → Timbre: +0.448.
		- Cycling Envelope → Cutoff: +0.279.
		- ENV → Cutoff: +1.000.
		- PRESSURE → Assign 1 → Cycling Envelope Fall: −0.507.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
