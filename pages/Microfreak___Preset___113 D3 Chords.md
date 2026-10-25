logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 113
preset-synth-microfreak-name:: D3 Chords
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/112 Anlg]]
next:: [[Microfreak/Preset/114 Fate In Freaks]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/04 Harmo]]
preset-synth-microfreak-parameter-payload-sha256:: 3193714b66897697c443115c8dc8b465901f0625affc3fccfb69fbe812bc600e
preset-synth-file:: [D3 Chords — October 25 slot 113 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___113%20D3%20Chords___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 2a40645cf2494e2ca93884629a28155a86c3aa50f6c1386ddd8a7d30a1798337
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 113 over USB on October 25, 2026 with `mise run microfreak:download --slot 113`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 1, Factory 2.1 slot None, Factory 3.0 slot 193, Factory 6.0 slot 290). Comparison used `mise run microfreak:compare`.
		- [Download the slot 113 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___113%20D3%20Chords___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/113 D3 Chords/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harmo. [[Microfreak/UG/06 Dig Osc/03 Types/04 Harmo]]
		- Content: 0.000. Sculpting: 0.108. Chorus: 0.593.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.576; resonance: 0.322. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.155, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.758, RiseSlp 0.481, FallLvl 0.754, FallSlp 0.456, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sawtooth, clock sync on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Wave: −0.046.
		- Cycling Envelope → Timbre: +0.052.
		- LFO → Timbre: −0.102.
		- ENV → Cutoff: +0.595.
		- KEY/ARP → Assign 1 → Decay/Release: −0.329.
		- ENV → Assign 2 → matrix amount LFO → Wave: −0.347.
		- Cycling Envelope → Assign 3 → Decay/Release: +0.093.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
