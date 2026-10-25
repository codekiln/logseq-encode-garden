logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 087
preset-synth-microfreak-name:: ATSpookBass
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/086 Whimsy]]
next:: [[Microfreak/Preset/088 D-Funk]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
preset-synth-microfreak-parameter-payload-sha256:: 67b18ce9851d52baf6712b2c8d16abc632e962b82efac74f62c4d488230dd2e7
preset-synth-file:: [ATSpookBass — October 25 slot 87 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___087%20ATSpookBass___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: b94e8afb71f56df6abe754c2c4083752d49e5a1f58c68f300b4b9b35e997a9c2
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 87 over USB on October 25, 2026 with `mise run microfreak:download --slot 87`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.1 slot 17, Factory 3.0 slot 17, Factory 6.0 slot None). Comparison used `mise run microfreak:compare`.
		- [Download the slot 87 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___087%20ATSpookBass___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/087 ATSpookBass/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Wavetable. [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
		- Table: 5 (stored choice code). Position: 0.001. Chorus: 0.000.
		- Keyboard octave: -2. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.659; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.259, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.158, RiseSlp 0.500, FallLvl 0.205, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sawtooth, clock sync on; stored division code: 3. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.019.
		- LFO → Timbre: +0.011.
		- PRESSURE → Timbre: +0.014.
		- PRESSURE → Cutoff: +0.536.
		- LFO → Assign 1 → Chorus: +0.619.
		- LFO → Assign 2 → matrix amount Cycling Envelope → Pitch: +0.015.
		- PRESSURE → Assign 3 → matrix amount LFO → Timbre: +0.014.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
