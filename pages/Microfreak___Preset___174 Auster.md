logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 174
preset-synth-microfreak-name:: Auster
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Keys]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Unknown]]
prev:: [[Microfreak/Preset/173 AfterBurner]]
next:: [[Microfreak/Preset/175 Wuuut]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
preset-synth-file-sha256:: 3bc40c2d5b229e611915d05af60ff65dcdbe093a286065dafb4e2d03879c46cd
- # Notes
	- BasicWaves keys with moving waveform shape and expression-controlled sub level and decay.
	- ## Saved export and provenance
		- Saved export: September 28, 2026 MIDI Control Center user-bank archive, computer-bank slot 249, file `249-09282026 6h14-A249.mbp`. The computer-bank slot differs from this page’s observed device slot.
		- The parameter payload matches Factory 2.0, 2.1, 3.0 and 6.0. This is an archived factory-equivalent baseline; it does not establish the instrument’s saved or unsaved state during a later session.
	- ## Oscillator
		- Model: BasicWaves. Morph moves from square to sawtooth to two sawtooths; Sym changes pulse width or the sawtooths’ relative phase; Sub adds a sine-wave sub-oscillator.
		- Morph: 0.918.
		- Sym: 1.000.
		- Sub: 0.669.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.000; resonance: 0.255. Cutoff and resonance are normalized settings, not hertz or instrument display values.
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.185, sustain 0.000. Amp Mod is on, so the main envelope controls loudness.
		- Cycling Envelope mode: Env. Stored RiseLvl 0.089, FallLvl 0.193, Hold 0.000, Amount 1.000. These are normalized stored fields; rise/fall times in milliseconds remain unverified.
	- ## LFO
		- Sine; clock sync off. Stored normalized rate: 0.148; division code: 0. The rate is not a hertz reading, and the musical division has not been converted.
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. The assignment destinations below resolve the saved Assign columns.
		- Cycling Envelope → Wave / Morph: −1.000. The envelope moves the waveform morph downward.
		- LFO → Timbre / Sym: +0.729. The sine LFO changes pulse width or sawtooth phasing according to Morph.
		- ENV → Cutoff: +0.728. The main envelope opens the filter from its zero base setting.
		- PRESSURE → Assign 1 → Sub: +1.000. Expression adds sub-oscillator level.
		- PRESSURE → Assign 2 → Decay/Release: +0.683. Expression lengthens decay/release.
		- All other saved matrix amounts are zero.
	- ## Performance and session context
		- The saved main envelope has an immediate attack and no sustained level. Expression changes bass weight and note length. The strong envelope-to-cutoff route opens an otherwise closed filter; Morph and Sym modulation change the oscillator spectrum.
		- Paraphonic mode is on in the saved export. The PRESSURE matrix row uses pressure or velocity according to the instrument’s global Utility setting; the export does not establish which expression source was used in the session.
		- [[GitP/A/Session/26/10/18-Sun]] references this sound.
	- ## Evidence and interpretation
		- Base controls use normalized 0…1 values unless a stored choice code is shown; matrix amounts use −1…+1. These describe saved base settings, before modulation, and are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix columns and assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py#L21-L107) and [assignment decoder](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_structured.py#L152-L173). Mode and waveform labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js#L1782-L1946).
		- [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]] explains matrix sources, destinations and the expression row.
