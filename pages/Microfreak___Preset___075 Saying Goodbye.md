logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 075
preset-synth-microfreak-name:: Saying Goodbye
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Pad]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/074 Sneaker]]
next:: [[Microfreak/Preset/076 AutoCHILL]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
preset-synth-file-sha256:: a988878aa3a5f964e3c59fa4373d309f1c633a077c2b2fc50f0aed59c3e9daa5
preset-synth-microfreak-parameter-payload-sha256:: 5f345b37fbe2642c85b95b2f56a559d4e022dfc0dccf9b91720175d76101a3ab
preset-synth-file:: [Saying Goodbye — October 25 slot 75 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___075%20Saying%20Goodbye___Asset___Device-Read-2026-10-25.bin)
- # Notes
	- Two-operator FM pad with a looping envelope moving cutoff and feedback; expression reduces FM intensity.
	- ## Saved export and provenance
		- Saved export: September 28, 2026 MIDI Control Center user-bank archive, computer-bank slot 159, file `159-09282026 6h14-A159.mbp`. The computer-bank slot differs from this page’s observed device slot.
		- The parameter payload matches Factory 1.1, 2.1, 3.0 and 6.0. This is an archived factory-equivalent baseline; it does not establish the instrument’s saved or unsaved state during a later session.
		- The Factory 1.0 variant has different expression and envelope routes and is not the same payload.
	- ## Oscillator
		- Model: Two Op.FM. Ratio sets the oscillator frequency ratio; Amount sets the modulation index; Shape sets operator 2 self-feedback.
		- Ratio: 0.279.
		- Amount: 0.479.
		- Shape: 0.139.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.101; resonance: 0.000. Cutoff and resonance are normalized settings, not hertz or instrument display values.
	- ## Envelopes
		- Main envelope: attack 0.343, decay/release 0.620, sustain 0.603. Amp Mod is on, so the main envelope controls loudness.
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.346, FallLvl 0.236, Hold 0.000, Amount 1.000. These are normalized stored fields; rise/fall times in milliseconds remain unverified.
	- ## LFO
		- Saw; clock sync on. Stored normalized rate: 0.148; division code: 3. The rate is not a hertz reading, and the musical division has not been converted.
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. The assignment destinations below resolve the saved Assign columns.
		- PRESSURE → Timbre / Amount: −0.449. Expression reduces the FM modulation index.
		- Cycling Envelope → Cutoff: +0.336. The looping envelope opens the filter.
		- ENV → Cutoff: +0.330. The main envelope also opens the filter.
		- Cycling Envelope → Assign 1 → Shape: +0.075. The looping envelope changes operator feedback.
		- Cycling Envelope → Assign 2 → LFO-to-Timbre matrix amount: −0.021. The envelope modulates that matrix route; its saved base amount is zero.
		- All other saved matrix amounts are zero.
	- ## Performance and session context
		- The saved attack rises gradually and the sustain holds above zero. Expression reduces FM intensity while the cycling envelope moves cutoff and feedback. The small assignment to another matrix amount creates modulation of modulation.
		- Paraphonic mode is on in the saved export. The PRESSURE matrix row uses pressure or velocity according to the instrument’s global Utility setting; the export does not establish which expression source was used in the session.
		- [[GitP/A/Session/26/10/20-Tue]] references this sound.
	- ## Evidence and interpretation
		- Base controls use normalized 0…1 values unless a stored choice code is shown; matrix amounts use −1…+1. These describe saved base settings, before modulation, and are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix columns and assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py#L21-L107) and [assignment decoder](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_structured.py#L152-L173). Mode and waveform labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js#L1782-L1946).
		- [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]] explains matrix sources, destinations and the expression row.
