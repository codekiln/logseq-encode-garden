logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 041
preset-synth-microfreak-name:: Madtraker
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/040 Disrespectful]]
next:: [[Microfreak/Preset/042 Hoss]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
preset-synth-microfreak-parameter-payload-sha256:: 0a7aff30ddaab16da6270a9f3eed480f991e1d78c6b98e9db9f30ab94ff73f40
preset-synth-file:: [Madtraker — October 25 slot 41 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___041%20Madtraker___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: b144f7bc15b79699fdaf6385d1b8175e11d5aaa9f0fbf065320c7fa7edccb802
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 41 over USB on October 25, 2026 with `mise run microfreak:download --slot 41`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot 128, Factory 1.1 slot 128, Factory 2.1 slot 128, Factory 3.0 slot 128, Factory 6.0 slot 251). Comparison used `mise run microfreak:compare`.
		- [Download the slot 41 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___041%20Madtraker___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/041 Madtraker/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Wavetable. [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
		- Table: 7 (stored choice code). Position: 0.811. Chorus: 1.000.
		- Keyboard octave: -3. Glide: 0.000.
	- ## Filter
		- High-pass filter. Saved cutoff: 0.190; resonance: 0.950. [[Microfreak/UG/07 Filter/01 Modifying Sound/03 High Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.462, sustain 0.233. Amp Mod is off. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.026, RiseSlp 0.000, FallLvl 0.305, FallSlp 0.000, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold, clock sync on; stored division code: 4. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +1.000.
		- Cycling Envelope → Wave: +1.000.
		- Cycling Envelope → Timbre: +1.000.
		- Cycling Envelope → Cutoff: +0.514.
		- KEY/ARP → Cutoff: +0.797.
		- LFO → Assign 1 → Cycling Envelope Fall: +0.296.
		- LFO → Assign 2 → Oscillator Type: −0.120.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
