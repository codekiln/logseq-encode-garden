logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 301
preset-synth-microfreak-name:: Perculiar Bass
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/300 MfCheese]]
next:: [[Microfreak/Preset/302 No Rush]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
preset-synth-microfreak-parameter-payload-sha256:: 63fae6c55e66643c906ab7ae7cad5db242b73accb52fc9e9811c51443f35d25a
preset-synth-file:: [Perculiar Bass — October 25 slot 301 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___301%20Perculiar%20Bass___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 1be84d11f21174d5a79d85d5de35e7ec058bbb7cc0062b7af2a3720cb848fae5
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 301 over USB on October 25, 2026 with `mise run microfreak:download --slot 301`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 364, Factory 6.0 slot 310). Comparison used `mise run microfreak:compare`.
		- [Download the slot 301 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___301%20Perculiar%20Bass___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/301 Perculiar Bass/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Bass. [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
		- Saturate: 0.384. Fold: 1.000. Noise: 0.000.
		- Keyboard octave: -1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.000; resonance: 0.411. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.291, sustain 0.190. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.392, RiseSlp 0.500, FallLvl 0.405, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold Filtered, clock sync on; stored division code: 6. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: −0.001.
		- Cycling Envelope → Wave: +0.673.
		- LFO → Timbre: +1.000.
		- ENV → Cutoff: +0.520.
		- KEY/ARP → Cutoff: −0.367.
		- Cycling Envelope → Assign 2 → matrix amount ENV → Cutoff: +0.159.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
