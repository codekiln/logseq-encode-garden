see-also:: [[Microfreak/CLI/Preset metadata over USB]], [[Microfreak/Sequence/Storage]], [[Microfreak/Preset]]

- # Inspect a saved preset's parameters
	- `mise run microfreak:inspect` reads a preset I already saved and prints its named parameters as JSON. It uses only Python's standard library, opens no MIDI port and leaves the file unchanged.
	- ## Run it
		- ```sh
		  mise run microfreak:inspect /private/tmp/preset/slot-001.bin
		  mise run microfreak:inspect '/private/path/project.mfprojz' --slot 1
		  mise run microfreak:inspect '/private/path/preset.mbp'
		  mise run microfreak:inspect '/private/path/preset.mfpz'
		  ```
		- Keep the exports outside the repository: the presets are mine and the repository is public.
	- ## What it reads
		- A `.bin` from `microfreak:download`: the 35-value saved header plus the 4672-value payload, or the payload alone.
		- A `.mfpz` preset export from MIDI Control Center: one text archive record in a ZIP. The report names the member as exported.
		- A `.mfprojz` project export with `--slot N`: the inspector picks the one `.mbp` whose leading slot number and final bank/slot suffix match, and refuses ambiguous banks. Project slot numbers describe the project on the computer, which can differ from what is on the instrument.
		- ZIP members are read in memory with a size limit and never extracted.
	- ## What it reports
		- `status: raw_parameters`, SHA-256 digests of the record and the payload, and the named fields.
		- Each field keeps its stored three values as `raw_hex`, the first as `descriptor`, and the other two read as signed and as unsigned little-endian integers. These readings preserve what is stored; they don't give the value the instrument's display shows. Descriptor meanings and display conversions are marked `unverified`.
		- The values are the saved base settings. Modulation, performance gestures and unsaved edits can change what I hear.
		- `VCF.Cutoff`, `VCF.Reso` and `VCO.Type` match the control names in [[Microfreak/UG/21 Appendix D - CC Values]].
		- The oscillator has three physical controls, Wave, Timbre and Shape ([[Microfreak/UG/06 Dig Osc/02 Param Controls]]), and [[Microfreak/UG/06 Dig Osc/03 Types]] says what each does per oscillator: Wavetable uses Table, Position and Chorus; Sample uses Start, Length and Loop; Two Op.FM uses Ratio, Amount and Shape. The inspector reports Wave, Timbre and Shape as **candidate** names for the stored `VCO.Param1`, `VCO.Param2` and `VCO.Param3`, because the manual names neither those stored fields nor their conversions.
		- An initialized `.mbp` gives `status: initialized` and no fields.
		- An unknown layout gives `status: unsupported_layout`, the position where parsing stopped and the digests, and exits with status 2. Invalid input also exits 2. A failed parse returns no partial list. Keep the original file when the layout is unsupported.
	- ## Firmware 5 interpretations
		- `--interpret-fw5` adds an interpretation layer next to the raw report:
			- ```sh
			  mise run microfreak:inspect '/private/path/preset.bin' --interpret-fw5
			  mise run microfreak:inspect '/private/path/project.mfprojz' --slot 1 --interpret-fw5
			  ```
		- It assumes MicroFreak firmware 5. Exports don't record the firmware, so `interpretations.firmware_detected_from_export` is `false`. Initialized presets and unsupported layouts keep their status and get no interpretations.
		- `interpretations` names the oscillator model and what its Wave, Timbre and Shape controls do, where supported. Firmware 5 numbers its saved engines from 1: SuperWave is 2, Wavetable is 3 and Vocoder is 14. Each interpreted field has a `kind`, a value, a range and evidence ids, and `evidence_sources` maps those ids to the research or manual page behind them. The raw fields, digests and status stay as they are.
		- The formulas and engine order come from [Freakout's firmware notes](https://github.com/kmorrill/freakout/blob/main/docs/microfreak-firmware-notes.md) and its [structured-payload parser](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_structured.py), implemented in [lib/semantics.py](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/semantics.py). Control names per oscillator follow [[Microfreak/UG/06 Dig Osc/03 Types]]. An unknown oscillator value keeps a null model and generic field labels; values outside the supported ranges stay `raw_only`.
		- `normalized_0_1`, `normalized_minus_1_1` and `metadata_scaled_integer` name numeric ranges. They don't give the display's hertz, milliseconds or percentages, so `display_conversions` stays `unverified`. Matrix destinations and the identity of referenced samples or wavetables are not decoded. The option doesn't change preset pages or handwritten notes.
	- ## Sequence
		- `--sequence` adds both sequencer patterns, decoded by [lib/sequence.py](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/sequence.py):
			- ```sh
			  mise run microfreak:inspect /private/tmp/preset/slot-005.bin --sequence
			  ```
		- The `sequence` object holds the shared length, gate length and smoothing, and for patterns A and B: whether the pattern is in use, its modulation-track destinations, and one entry per played step with its status (`note`, `tie`, `rest`), notes, note names (C4 = MIDI 60), velocities and modulation values. Steps past the sequence length are counted, not listed.
		- [[Microfreak/Sequence/Write a sequence]] goes the other way: it writes a described sequence into a slot. [[Microfreak/Sequence/Storage]] has the layout and the experiments behind it.
	- ## How a saved preset is laid out
		- The text archive envelope follows [Elektroid's MicroFreak serialization](https://github.com/dagargo/elektroid/blob/6f3d50e2588f0236afb3510e1c55bbb292446aa2/src/connectors/microfreak_sample.c#L32-L278). [Elektroid's preset connector](https://github.com/dagargo/elektroid/blob/6f3d50e2588f0236afb3510e1c55bbb292446aa2/src/connectors/microfreak.c#L286-L443) moves the payload without decoding parameter names.
		- The framing inside it was inferred from MIDI Control Center exports. A live slot read matched the whole payload of the matching export, and every populated record examined went through expansion and repacking unchanged. Most followed the named-field layout; one began with an unknown structure. The tests use synthetic data, so no private export is stored here.
		- Each group of eight holds a mask of high bits followed by seven 7-bit values. Mask bit 0 is the first value's high bit, through bit 6 for the seventh. Expanding 4672 values gives 4088.
		- The parameter block starts at expanded position 0. A tag's upper three bits say whether a section name (1), a field name (2) or a value (3) follows, and its lower five bits give how many values follow. Names are ASCII. In the supported layout a parameter value is three values long.
		- `0x40` closes a section and `0x20` closes the root. What follows the root is kept in the export and counted in the report but not interpreted: padding, stale fragments and, from expanded position 1980, the sequence patterns that `--sequence` decodes. It must not be parsed as more named fields.
		- Labels seen so far: `VCO` oscillator controls, `VCF` filter, `EG1` cycling envelope, `EG2` main envelope, `LFO`, `Kbd`, `Arp`, `Gen`, `Mat`, matrix columns `Co1`–`Co7`, `Seq` and `Voc`. Fields vary between presets and format generations. Unknown or missing fields are never filled with defaults.
	- ## Open questions
		- The first stored value of each parameter often looks like a range or type descriptor and the other two like a normalized value. That is a hypothesis: oscillator descriptors vary between records, and modulation amounts may need a signed reading.
		- Converting the firmware 5 ranges to the values on the display needs paired display-and-export observations or more evidence about how presets are serialized. Matrix destinations are still undecoded.
		- Archive format versions and other envelope attributes are kept in the metadata. The envelope's version string is not assumed to be a firmware version. Export digests identify what is stored, not equivalent sounds, and don't show that referenced samples and wavetables were kept.
		- [#157 parameter decoding](https://github.com/codekiln/logseq-encode-garden/issues/157) tracks the remaining display conversions and controlled comparisons.
	- ## Test it
		- `mise run microfreak:test` runs the tests for every MicroFreak task, this one included.
