logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 114
preset-synth-microfreak-name:: Fate In Freaks
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/113 D3 Chords]]
next:: [[Microfreak/Preset/115 Notobeat]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/09 Formant]]
preset-synth-microfreak-parameter-payload-sha256:: 5654db8c66592316fe89936be66cfe00d5bd4c933c427d54d8c1a0067d06863c
preset-synth-file:: [Fate In Freaks — October 25 slot 114 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___114%20Fate%20In%20Freaks___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 4e872de3514746a49f56dc95ac18e0c9c041b5abfdb9deda4afe46c97e550e27
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 114 over USB on October 25, 2026 with `mise run microfreak:download --slot 114`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 2, Factory 2.1 slot None, Factory 3.0 slot 194, Factory 6.0 slot 276). Comparison used `mise run microfreak:compare`.
		- [Download the slot 114 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___114%20Fate%20In%20Freaks___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/114 Fate In Freaks/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Formant. [[Microfreak/UG/06 Dig Osc/03 Types/09 Formant]]
		- Interval: 0.300. Formant: 0.090. Shape: 0.802.
		- Keyboard octave: -2. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.004; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.254, sustain 0.000. Amp Mod is off. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.112, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.154. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: −0.001.
		- PRESSURE → Pitch: +0.001.
		- Cycling Envelope → Wave: +0.427.
		- LFO → Timbre: +0.094.
		- ENV → Cutoff: +0.796.
		- KEY/ARP → Cutoff: −0.212.
		- ENV → Assign 1 → Shape: +0.200.
		- KEY/ARP → Assign 1 → Shape: +1.000.
		- ENV → Assign 2 → Cycling Envelope Amount: −1.000.
		- KEY/ARP → Assign 2 → Cycling Envelope Amount: −0.426.
		- KEY/ARP → Assign 3 → Cycling Envelope Amount: +1.000.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
