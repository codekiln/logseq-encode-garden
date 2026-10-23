logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 077
preset-synth-microfreak-name:: Eonz
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Lead]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/076 AutoCHILL]]
next:: [[Microfreak/Preset/078 A Juno Vibe]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
preset-synth-file:: [Eonz — September 28 MCC export](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/GitP___A___Session___26___10___20-Tue___Asset___Preset___Eonz-Archived-2026-09-28.mbp)
preset-synth-file-sha256:: 919e785b1427854c339994cdaf9d1bf51404801d6905d5ce5edfe1de81c67b61
- # Notes
	- SuperWave lead with expression-controlled waveform selection and note length.
	- ## Saved export and provenance
		- Saved export: September 28, 2026 MIDI Control Center user-bank archive, computer-bank slot 160, file `160-09282026 6h14-A160.mbp`. The computer-bank slot differs from this page’s observed device slot.
		- The parameter payload matches Factory 1.1, 2.1, 3.0 and 6.0. This is an archived factory-equivalent baseline; it does not establish the instrument’s saved or unsaved state during a later session.
		- [Download the archived Eonz preset](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/GitP___A___Session___26___10___20-Tue___Asset___Preset___Eonz-Archived-2026-09-28.mbp).
	- ## Oscillator
		- Model: SuperWave. Wave chooses saw, square, triangle or sine; Timbre changes detuning; Shape changes the volume of the detuned copies.
		- Wave: 3 (stored choice code).
		- Detune: 0.440.
		- Volume: 0.353.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.187; resonance: 0.415. Cutoff and resonance are normalized settings, not hertz or instrument display values.
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.300, sustain 0.000. Amp Mod is on, so the main envelope controls loudness.
		- Cycling Envelope mode: Run. Stored RiseLvl 0.055, FallLvl 0.057, Hold 0.000, Amount 1.000. These are normalized stored fields; rise/fall times in milliseconds remain unverified.
	- ## LFO
		- Triangle; clock sync on. Stored normalized rate: 0.148; division code: 1. The rate is not a hertz reading, and the musical division has not been converted.
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. The assignment destinations below resolve the saved Assign columns.
		- PRESSURE → Wave: −1.000. Expression moves the SuperWave waveform selection.
		- ENV → Timbre / Detune: −0.430. The main envelope reduces detuning.
		- ENV → Cutoff: +0.471. The main envelope opens the filter.
		- PRESSURE → Assign 1 → Decay/Release: +0.561. Expression lengthens the main envelope decay/release.
		- All other saved matrix amounts are zero.
	- ## Performance and session context
		- The saved main envelope has an immediate attack and no sustained level. Expression changes both waveform selection and decay/release. The Cycling Envelope, LFO and Key/Arp rows have no nonzero matrix routes in this export.
		- Paraphonic mode is on in the saved export. The PRESSURE matrix row uses pressure or velocity according to the instrument’s global Utility setting; the export does not establish which expression source was used in the session.
		- [[GitP/A/Session/26/10/20-Tue]] references this sound.
	- ## Evidence and interpretation
		- Base controls use normalized 0…1 values unless a stored choice code is shown; matrix amounts use −1…+1. These describe saved base settings, before modulation, and are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix columns and assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py#L21-L107) and [assignment decoder](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_structured.py#L152-L173). Mode and waveform labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js#L1782-L1946).
		- [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]] explains matrix sources, destinations and the expression row.
