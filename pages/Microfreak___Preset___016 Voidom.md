logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 016
preset-synth-microfreak-name:: Voidom
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/015 PolyBells]]
next:: [[Microfreak/Preset/017 Tubular]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/11 Speech]]
preset-synth-file-sha256:: ef9b2913965642d96dcea1761a09b26a5b216ee675a8df9204aaf5122ddf98ae
preset-synth-microfreak-parameter-payload-sha256:: 20c1d565dc198f0c3c9ee12981f2a7982aa56ace5c01f4c6489f282a7ec3d1c9
preset-synth-file:: [Voidom — October 25 slot 16 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___016%20Voidom___Asset___Device-Read-2026-10-25.bin)
- # Notes
	- Speech patch with stepped formants and word selection, plus strong expression control of filter brightness.
	- ## Saved export and provenance
		- Saved export: September 28, 2026 MIDI Control Center user-bank archive, computer-bank slot 105, file `105-09282026 6h14-A105.mbp`. The computer-bank slot differs from this page’s observed device slot.
		- The parameter payload matches Factory 1.1, 2.1, 3.0 and 6.0. This is an archived factory-equivalent baseline; it does not establish the instrument’s saved or unsaved state during a later session.
		- The Factory 1.0 variant has a different pressure-to-cutoff route and is not the same payload.
	- ## Oscillator
		- Model: Speech. Type chooses formants or a speech library; Timbre shifts formants; Word scans the selected library’s subset.
		- Type: 0.024.
		- Timbre: 0.315.
		- Word: 0.094.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.570; resonance: 0.000. Cutoff and resonance are normalized settings, not hertz or instrument display values.
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.559, sustain 0.299. Amp Mod is on, so the main envelope controls loudness.
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, FallLvl 0.913, Hold 0.000, Amount 0.953. These are normalized stored fields; rise/fall times in milliseconds remain unverified.
	- ## LFO
		- Sample-and-Hold; clock sync on. Stored normalized rate: 0.148; division code: 8. The rate is not a hertz reading, and the musical division has not been converted.
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. The assignment destinations below resolve the saved Assign columns.
		- Cycling Envelope → Wave / Type: +0.198. The envelope moves the Speech formant/library selection.
		- LFO → Timbre: +1.000. Sample-and-Hold steps the speech formants.
		- ENV → Cutoff: +0.059. The main envelope opens the filter slightly.
		- PRESSURE → Cutoff: +0.967. Expression strongly opens the filter.
		- LFO → Assign 1 → Word: −1.000. Sample-and-Hold moves the word/subset selector in the opposite direction.
		- All other saved matrix amounts are zero.
	- ## Performance and session context
		- The expression input mainly changes brightness. The LFO changes both speech timbre and word selection, while the cycling envelope changes the Type selection. These are saved modulation routes; the recording does not establish every knob movement or the global expression mode.
		- Paraphonic mode is on in the saved export. The PRESSURE matrix row uses pressure or velocity according to the instrument’s global Utility setting; the export does not establish which expression source was used in the session.
		- [[GitP/A/Session/26/10/22-Thu]] references this sound.
	- ## Evidence and interpretation
		- Base controls use normalized 0…1 values unless a stored choice code is shown; matrix amounts use −1…+1. These describe saved base settings, before modulation, and are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix columns and assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py#L21-L107) and [assignment decoder](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_structured.py#L152-L173). Mode and waveform labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js#L1782-L1946).
		- [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]] explains matrix sources, destinations and the expression row.
