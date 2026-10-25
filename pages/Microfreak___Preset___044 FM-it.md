logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 044
preset-synth-microfreak-name:: FM-it
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/043 IDm5]]
next:: [[Microfreak/Preset/045 Lottreux]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/04 Harmo]]
preset-synth-microfreak-parameter-payload-sha256:: 930760da529a1770cda1032a6da4b1744eaaa7cb513029c9d24a9e4808b84df2
preset-synth-file:: [FM-it — October 25 slot 44 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___044%20FM-it___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: de7ace9dcc51b952fbee223b1237fcdf0c02753897066d4b29ff455c321ad9bc
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 44 over USB on October 25, 2026 with `mise run microfreak:download --slot 44`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 130, Factory 2.1 slot 130, Factory 3.0 slot 130, Factory 6.0 slot 341). Comparison used `mise run microfreak:compare`.
		- [Download the slot 44 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___044%20FM-it___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/044 FM-it/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harmo. [[Microfreak/UG/06 Dig Osc/03 Types/04 Harmo]]
		- Content: 0.000. Sculpting: 0.000. Chorus: 0.317.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- High-pass filter. Saved cutoff: 0.332; resonance: 0.690. [[Microfreak/UG/07 Filter/01 Modifying Sound/03 High Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.107, sustain 0.590. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.105, RiseSlp 0.500, FallLvl 0.098, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync off; stored normalized rate: 0.370. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.211.
		- ENV → Cutoff: +0.232.
		- LFO → Cutoff: +0.100.
		- PRESSURE → Cutoff: +0.297.
		- KEY/ARP → Assign 3 → `Mat.Assign3`: +0.001.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
