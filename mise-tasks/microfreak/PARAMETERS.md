# Inspect saved preset parameters

`microfreak:inspect` reads an existing export and prints JSON. It uses Python's standard library, opens no MIDI ports, and leaves the input file unchanged.

```sh
mise run microfreak:inspect /private/tmp/preset/slot-001.bin
mise run microfreak:inspect '/private/path/project.mfprojz' --slot 1
mise run microfreak:inspect '/private/path/preset.mbp'
mise run microfreak:inspect '/private/path/preset.mfpz'
```

The binary input accepts the downloader's 35-byte saved header plus 4672-byte payload, or a standalone 4672-byte payload. A `.mfpz` preset export contains one text archive record in a ZIP; the inspector accepts its member name as exported and reports it in metadata. A project archive selects one `.mbp` whose leading slot number and final bank/slot suffix match `--slot`; ambiguous banks are rejected. Project slot numbers describe the computer project, whose contents can differ from the current device. ZIP members are read in memory, with a size limit, and never extracted.

Successful reports have `status: raw_parameters`, record/payload SHA-256 digests, and named fields. Each field retains its exact three-byte `raw_hex`, first-byte `descriptor`, and the remaining two bytes interpreted as both signed and unsigned little-endian integers. These integer interpretations preserve the bytes; they do not establish the instrument's displayed value. Reports explicitly mark descriptor semantics and display conversions as `unverified`.

The values describe saved base settings. Modulation, performance gestures and unsaved edits can change the audible result. `VCF.Cutoff`, `VCF.Reso` and `VCO.Type` have control labels matching [the guide's MIDI control names](../../pages/Microfreak___UG___21%20Appendix%20D%20-%20CC%20Values.md). [The oscillator control guide](../../pages/Microfreak___UG___06%20Dig%20Osc___02%20Param%20Controls.md) establishes the three physical controls, Wave, Timbre and Shape. [Its model pages](../../pages/Microfreak___UG___06%20Dig%20Osc___03%20Types.md) document what each control does for each oscillator: for example, Wavetable uses Table, Position and Chorus; Sample uses Start, Length and Loop; Two Op.FM uses Ratio, Amount and Shape. Thus the control's function is documented once the oscillator model is known. The inspector reports Wave, Timbre and Shape as **candidate** positions for stored `VCO.Param1`, `VCO.Param2` and `VCO.Param3`, because the manual does not identify those serialized field names or their numeric conversions.

An initialized `.mbp` produces `status: initialized` and an empty field list. Unknown layouts produce `status: unsupported_layout`, a byte-position diagnostic, and hashes, with exit status 2. Invalid input also exits 2. Failed parsing returns no partial parameter list. Keep the original file when a layout is unsupported.

## Firmware 5 interpretations

Add `--interpret-fw5` to include the existing interpretation layer alongside the exact raw report:

```sh
mise run microfreak:inspect '/private/path/preset.bin' --interpret-fw5
mise run microfreak:inspect '/private/path/project.mfprojz' --slot 1 --interpret-fw5
```

The option assumes MicroFreak firmware 5. The archive envelope does not identify the instrument's firmware, so `interpretations.firmware_detected_from_export` is `false`. Reports for initialized presets or unsupported layouts retain their original status and have no interpretations.

The added `interpretations` object names the oscillator model and its Wave/Timbre/Shape control functions where supported. Firmware 5's saved engine order is one-based: SuperWave is index 2, Wavetable is index 3, and Vocoder is index 14. Each interpreted field has a `kind`, value, range, and evidence identifiers; `evidence_sources` resolves those identifiers to the source research or guide. Existing parser fields, hashes, status and raw-value metadata remain unchanged.

The formulas and engine order come from [Freakout's firmware research](https://github.com/kmorrill/freakout/blob/main/docs/microfreak-firmware-notes.md) and [structured-payload parser](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_structured.py), as implemented by [the interpretation helper](lib/semantics.py). Model-specific control names follow the [Arturia guide transcription](../../pages/Microfreak___UG___06%20Dig%20Osc___03%20Types.md). Unknown oscillator values keep a null model and generic field labels; values outside the supported domains remain `raw_only`.

`normalized_0_1`, `normalized_minus_1_1`, and `metadata_scaled_integer` identify numeric domains. These values do not establish OLED readings in hertz, milliseconds or percentages. The report's `display_conversions` remains `unverified`; sequence contents, matrix destination meanings, and referenced sample or wavetable identities remain undecoded. The option does not modify preset pages or handwritten notes.

## Evidence and scope

The textual archive envelope follows [Elektroid's MicroFreak serialization](https://github.com/dagargo/elektroid/blob/6f3d50e2588f0236afb3510e1c55bbb292446aa2/src/connectors/microfreak_sample.c#L32-L278). [Its preset connector](https://github.com/dagargo/elektroid/blob/6f3d50e2588f0236afb3510e1c55bbb292446aa2/src/connectors/microfreak.c#L286-L443) transfers the preset payload without decoding its parameter names.

The inner framing below was inferred from MIDI Control Center exports. A repeated live slot read matched the entire payload of the corresponding export. All populated records examined round-tripped byte for byte through mask expansion and repacking. Most supported the named-field layout; one began with an unknown structure. Synthetic tests exercise the parser without storing private exports in this repository.

- Each eight-byte transport group contains a high-bit mask followed by seven low-seven-bit data bytes. Mask bit 0 supplies the first data byte's high bit, through bit 6 for the seventh byte. Expanding 4672 bytes yields 4088 bytes.
- The parameter block starts at expanded offset 0. A tag's upper three bits indicate section name (1), field name (2), or value (3); its lower five bits specify the following byte count. Names are ASCII. Values in the supported layout have three bytes.
- `0x40` closes a section; `0x20` closes the root. Bytes after the root are retained in the original export and counted in the report, but remain uninterpreted. They can include padding, stale fragments and sequence data; they must not be parsed as more named fields.
- Observed labels cover `VCO` oscillator controls, `VCF` filter, `EG1` cycling envelope, `EG2` main envelope, `LFO`, `Kbd`, `Arp`, `Gen`, `Mat`, matrix columns `Co1`–`Co7`, `Seq`, and `Voc`. Fields vary between presets and format generations. Unknown or absent fields are never filled with defaults.

The first value byte often resembles a range or type descriptor, while the remaining bytes resemble a normalized value. That interpretation is a research hypothesis. Oscillator descriptors vary between records, and modulation amounts may need signed interpretation. The manual supplies the model-specific oscillator control names and behavior. The opt-in firmware 5 layer uses the existing research-backed engine order and value-domain formulas. Converting those domains to instrument display values still requires paired display-and-export observations or further serialization evidence. Matrix destinations and sequence contents also remain to be decoded. The inspector reports raw fields so those comparisons can be made without losing information.

Archive format versions and opaque envelope attributes are retained in metadata. The envelope's version string is not assumed to be a firmware version. Export hashes identify bytes, not equivalent sounds or complete preservation of referenced samples and wavetables.

## Verification

```sh
python3 -m unittest discover -s mise-tasks/microfreak/lib -p 'test_*.py' -v
```

See [issue #157 — parameter decoding](https://github.com/codekiln/logseq-encode-garden/issues/157) for the remaining display conversions and controlled comparisons.
