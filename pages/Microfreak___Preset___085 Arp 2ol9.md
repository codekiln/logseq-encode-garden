logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 085
preset-synth-microfreak-name:: Arp 2ol9
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/084 Press So]]
next:: [[Microfreak/Preset/086 Whimsy]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
preset-synth-microfreak-parameter-payload-sha256:: b9031186b5d03d3c79c9ce13a6e050a074d19a113d0ad6ae0355440b780cbf09
preset-synth-file:: [Arp 2ol9 — October 25 slot 85 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___085%20Arp%202ol9___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 2984279affb02356522481ef78b77bab0a561bb8392a713a7defd6231a0f15e3
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 85 over USB on October 25, 2026 with `mise run microfreak:download --slot 85`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot 172, Factory 1.1 slot 172, Factory 2.1 slot 168, Factory 3.0 slot 168, Factory 6.0 slot 160). Comparison used `mise run microfreak:compare`.
		- [Download the slot 85 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___085%20Arp%202ol9___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/085 Arp 2ol9/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: V.Analog. [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
		- Detune: 0.518. Shape: 0.799. Wave: 0.691.
		- Keyboard octave: -1. Glide: 0.182.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.595; resonance: 0.881. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.248, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.692, RiseSlp 0.000, FallLvl 1.000, FallSlp 0.000, Hold 0.152, Amount 0.536. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.000. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Cutoff: +0.363.
		- ENV → Cutoff: −0.014.
		- LFO → Cutoff: −0.306.
		- KEY/ARP → Cutoff: −0.528.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
