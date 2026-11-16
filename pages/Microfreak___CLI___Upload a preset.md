see-also:: [[Microfreak/CLI/Preset metadata over USB]], [[Microfreak/Sequence/Research]]

- # Upload a preset to a slot
	- `mise run microfreak:upload` writes one preset, from a file that `microfreak:download` saved, into a MicroFreak slot over USB. It then reads the slot back and compares it with the file. It was added for [#433 Upload a preset to a MicroFreak slot with microfreak:upload](https://github.com/codekiln/logseq-encode-garden/issues/433), so that the generated sequence presets of [#431 Create MicroFreak presets that hold a described sequence](https://github.com/codekiln/logseq-encode-garden/issues/431) can reach the instrument.
	- ## Invocation
		- Run from the garden root, with MIDI Control Center closed:
		- ```sh
		  mise run microfreak:download --slot 5 --output-dir /private/tmp/mf
		  mise run microfreak:upload /private/tmp/mf/slot-005.bin --slot 321
		  mise run microfreak:upload /private/tmp/mf/slot-005.bin --slot 323 \
		    --backup-dir /private/tmp/mf/backup --name 'Upload Test' --category SFX
		  ```
		- `--slot` takes 1–512.
		- `--backup-dir` is required when the slot holds a preset. The task downloads the slot there first, as `slot-NNN.bin` and `slot-NNN.json` in `microfreak:download`'s format. If a backup for that slot already exists in the folder, the task stops before writing.
		- `--name` and `--category` replace the name and category stored with the preset. A name has 1–14 letters, digits, spaces, periods, underscores or hyphens, with no space at either end.
		- `--port` names the MIDI port when more than one port has "microfreak" in its name.
		- The task prints whether it saved a backup, the name and category read back, and the SHA-256 of the data read back. It exits with status 1 when it refuses to write, times out, gets an unexpected answer, or reads back something other than what it sent.
	- ## Messages
		- The task follows Elektroid's [microfreak_preset_upload](https://github.com/dagargo/elektroid/blob/6f3d50e2588f0236afb3510e1c55bbb292446aa2/src/connectors/microfreak.c#L449-L552). Each message has the prefix `F0 00 20 6B 07 01`, a sequence number, a length and an operation, as in the download. The task sends, in order:
			- operation 0x52 with the 35-value header for the target slot
			- operation 0x52 with the slot address followed by 1
			- operation 0x15 with nothing
			- 146 data packets of 32 values, with operation 0x16, and 0x17 for the last one
		- The MicroFreak answered every message, each data packet included, with an empty operation 0x18 carrying the same sequence number. The task stops at any other answer.
		- Header sent: Elektroid's .mfp file keeps only the name (offsets 12–25), the category (offset 10) and the value at offset 11, so its upload sends those three with the slot address and zero everywhere else, which leaves the initialized flag (value 8 at offset 3) clear. The address is (slot − 1) // 128 at offset 0 and (slot − 1) % 128 at offsets 1 and 8.
		- Offset 9 holds (slot − 1) // 256 in every slot header read on [[2026-11-16 Mon]]. Elektroid sends 0 there; the MicroFreak stored 1 in slot 321 after receiving 0. The task sends (slot − 1) // 256, so the header read back equals the header sent.
		- The upload drops header values that Elektroid's file has no place for. Offset 3 also holds 0x10 in slots 129–256 and 402–512, and slot 300 has values at offsets 4–6. What they mean is unknown.
	- ## Verified on the instrument, 2026-11-16
		- Each check below ran under the shared hardware lock with no one at the panel. Downloads, backups and recordings stay in the session's scratch folder.
		- Round trip with [[Microfreak/Preset/005 MotivSeq]] (Sequence): downloaded slot 5, uploaded the file unchanged to slot 321, which was initialized, and downloaded slot 321 again. All 146 data packets matched (data SHA-256 `c55113dcba9f69be…`). The header matched except offsets 0, 1, 8 and 9, the slot address.
		- Round trip with [[Microfreak/Preset/113 D3 Chords]] (Sequence) to slot 322: same result (data SHA-256 `3193714b66897697…`).
		- A header read afterwards reports slot 321 as MotivSeq, Sequence, not initialized, and slot 322 as D3 Chords, Sequence, not initialized.
		- Name and category: [[Microfreak/Preset/128 KickBass]] uploaded to slot 323 with `--name 'Upload Test' --category SFX` read back with that name and category and unchanged data. D3 Chords uploaded to slot 324 with `--name 'D3 Copy 324' --category Keys` did the same.
		- Backup: with slot 323 holding a preset, an upload without `--backup-dir` stopped with `Slot 323 holds MotivSeq (Sequence); pass --backup-dir to save it before writing` and wrote nothing. An earlier upload with `--backup-dir` saved Upload Test / SFX with KickBass's data, then wrote the slot.
		- The slots now hold: 321 MotivSeq, 322 D3 Chords, 323 MotivSeq, 324 D3 Copy 324 (Keys).
	- ## Selecting a slot over MIDI
		- On MIDI channel 1, bank select (CC 0) with value (slot − 1) // 128, followed by program change (slot − 1) % 128, selects the slot. For slot 323 that is CC 0 = 2, then program 66. Elektroid selects a preset the same way, in [microfreak_midi_program_change](https://github.com/dagargo/elektroid/blob/6f3d50e2588f0236afb3510e1c55bbb292446aa2/src/connectors/microfreak.c#L554-L559) and [common_midi_program_change_int](https://github.com/dagargo/elektroid/blob/6f3d50e2588f0236afb3510e1c55bbb292446aa2/src/connectors/common.c#L103-L109).
		- An upload leaves the sound being played alone, even when it writes the selected slot. Selecting the slot afterwards loads what was written.
		- Evidence: after each step, MIDI note 48 at velocity 100 was held for 1.2 s and recorded through the [[Zoom H5/My Unit]], then the recordings were compared by spectrum (correlation of log magnitude up to 8 kHz) and loudness over time.
			- Selecting slot 128 (KickBass) gave a decaying sound. Selecting slot 323 (Init) gave a sustained one; the two spectra correlate at 0.53.
			- With slot 323 selected, uploading KickBass to slot 323 left the Init sound playing: 0.92 against the Init recording, 0.53 against KickBass.
			- Selecting slot 323 again played KickBass: 0.95 against the slot 128 recording. Since only slot 323 received KickBass, bank select reached bank 2.
			- With slot 323 still selected, uploading MotivSeq over it left KickBass playing (0.85) until slot 323 was selected again.
		- MotivSeq gave no sound for the held note in slots 5, 321 and 323; each recording stayed at the input's noise floor. The sequencer was stopped, and starting it was not tried.
		- What the MicroFreak's screen showed during these steps was not observed.
