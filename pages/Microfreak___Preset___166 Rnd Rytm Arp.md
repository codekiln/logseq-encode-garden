logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 166
preset-synth-microfreak-name:: Rnd Rytm Arp
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Lead]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/165 Kick N Hard]]
next:: [[Microfreak/Preset/167 Chordrone It]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/04 Harmo]]
preset-synth-microfreak-parameter-payload-sha256:: d33089d634d7abcf0d5ef1cdf62bcdbea06e72d18fef755f71d90185a1c67cc2
preset-synth-file:: [Rnd Rytm Arp — October 25 slot 166 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___166%20Rnd%20Rytm%20Arp___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 4dbc5a2ff73b90ec36afd3f0926796726564849f3b2d6490acb492596b5336a7
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 166 over USB on October 25, 2026 with `mise run microfreak:download --slot 166`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 14, Factory 2.1 slot None, Factory 3.0 slot 241, Factory 6.0 slot 235). Comparison used `mise run microfreak:compare`.
		- [Download the slot 166 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___166%20Rnd%20Rytm%20Arp___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/166 Rnd Rytm Arp/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harmo. [[Microfreak/UG/06 Dig Osc/03 Types/04 Harmo]]
		- Content: 0.000. Sculpting: 0.278. Chorus: 0.886.
		- Keyboard octave: -1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.316; resonance: 0.473. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.330, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.580, RiseSlp 0.500, FallLvl 0.668, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sawtooth, clock sync on; stored division code: 3. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ENV → Wave: +0.084.
		- Cycling Envelope → Timbre: +0.181.
		- ENV → Cutoff: +0.514.
		- Cycling Envelope → Assign 1 → Arp/Seq Rate: +0.370.
		- LFO → Assign 1 → Arp/Seq Rate: +0.315.
		- Cycling Envelope → Assign 2 → matrix amount ENV → Cutoff: +0.068.
		- Cycling Envelope → Assign 3 → Decay/Release: +0.318.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
