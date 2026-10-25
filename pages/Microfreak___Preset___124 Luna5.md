logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 124
preset-synth-microfreak-name:: Luna5
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/123 TaBass]]
next:: [[Microfreak/Preset/125 Amigras]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
preset-synth-microfreak-parameter-payload-sha256:: 4a93c6197382a24a088f6b34115bd822be5368457ba1f91461d63bea5bfcaccd
preset-synth-file:: [Luna5 — October 25 slot 124 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___124%20Luna5___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: ae4ce1c12b428fb4be77c2f937b70e5224c0008a2db8966818de1c1d2b0015e2
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 124 over USB on October 25, 2026 with `mise run microfreak:download --slot 124`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 101, Factory 2.1 slot 203, Factory 3.0 slot 203, Factory 6.0 slot 313). Comparison used `mise run microfreak:compare`.
		- [Download the slot 124 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___124%20Luna5___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/124 Luna5/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Noise. [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
		- Wave: 0.060. Timbre: 0.740. Shape: 0.720.
		- Keyboard octave: 0. Glide: 0.080.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.148; resonance: 0.560. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.278, sustain 0.102. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.357, RiseSlp 0.950, FallLvl 0.163, FallSlp 0.072, Hold 0.000, Amount 0.382. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync on; stored division code: 5. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: +0.003.
		- KEY/ARP → Wave: −0.203.
		- Cycling Envelope → Cutoff: +0.261.
		- ENV → Cutoff: +0.311.
		- PRESSURE → Cutoff: +0.069.
		- KEY/ARP → Cutoff: +0.500.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
