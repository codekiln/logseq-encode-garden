see-also:: [[Microfreak/Sequence/Storage]], [[Microfreak/Sequence/Research]], [[Microfreak/CLI/Audition a sequence]], [[Microfreak/CLI/Upload a preset]]

- # Write a described sequence into a preset
	- `mise run microfreak:write-sequence` writes a sequence described in a JSON or YAML file into a MicroFreak preset and uploads it to a slot. `mise run microfreak:verify-sequence` also plays the slot, records it and downloads it again, then reports for every step what the description expects, what MIDI out carried and what the [[Zoom H5/My Unit]] heard. Both tasks were added for [#436 Write a described sequence into a MicroFreak preset and verify it on the instrument](https://github.com/codekiln/logseq-encode-garden/issues/436).
	- ## Put a sequence into a slot
		- Run from the garden root, with MIDI Control Center closed. Write the description to a file, then:
		- ```sh
		  mise run microfreak:write-sequence seq.json --base 358 --slot 450
		  mise run microfreak:verify-sequence seq.json --base 358 --slot 450 \
		    --backup-dir /private/tmp/mf-backup --out-dir /private/tmp/mf-verify
		  ```
		- `write-sequence` writes and uploads. `verify-sequence` with `--base` does the same write, then plays and checks the slot; without `--base` it checks the slot as it is.
		- `--base` is the preset to start from: a slot number, which is read and left unchanged, or a `.bin` file from `microfreak:download`. The new preset keeps the base's sound and every setting except the ones listed under What the write changes.
		- `--slot` is the slot to write. A slot that holds a preset is refused unless `--backup-dir` names a folder to save it in first, as with [[Microfreak/CLI/Upload a preset]]. The slot is read back and compared with what was sent.
		- `--output new.bin` also writes the result to a new file. With neither `--slot` nor `--output`, the task only prints what it would store.
		- `--name` and `--category` set the stored name and category. A `name` or `category` key in the description does the same; without either, the base's are kept.
		- Uploading does not change the sound being played. Select the slot on the panel, or over MIDI with bank select (slot − 1) // 128 and program change (slot − 1) % 128, to hear it.
	- ## Description
		- "Pattern A: C3 E3 G3, rest, C4 held for two steps, 16 steps; pattern B empty" is:
		- ```json
		  {"name": "Arp Sketch", "length": 16, "gate_percent": 50,
		   "patterns": {
		     "A": {"steps": [
		       {"notes": ["C3"]}, {"notes": ["E3"]}, {"notes": ["G3"]}, {},
		       {"notes": ["C4"], "tie": true}, {"notes": ["C4"]}]},
		     "B": {"steps": []}}}
		  ```
		- The same in YAML, in a file ending `.yaml` or `.yml`:
		- ```yaml
		  name: Arp Sketch
		  length: 16
		  gate_percent: 50
		  patterns:
		    A:
		      steps:
		        - {notes: [C3]}
		        - {notes: [E3]}
		        - {notes: [G3]}
		        - {}
		        - {notes: [C4], tie: true}
		        - {notes: [C4]}
		    B: {steps: []}
		  ```
		- `length` is the number of steps, 1–64, shared by both patterns. Steps after the last one listed are rests.
		- `gate_percent` is the gate length, 10–90. `smoothing` gives four booleans, one per modulation track. Both are optional; the base's values stay when they are left out.
		- A step lists up to four `notes`, by name (middle C, MIDI note 60, is C4) or MIDI number. `velocity` is 1–127, one value or one per note, default 100. `tie: true` holds the step's notes into the next step; repeat the same notes on that step to hear one long note. An empty step `{}` is a rest.
		- `mod` gives a step's values for modulation tracks 1–4, 0–255 or `null`, and the pattern's `mod_tracks` gives each track's destination: `"0x0101"` is filter cutoff and `"0x0602"` envelope decay.
		- A pattern left out keeps the base's steps; `"B": {"steps": []}` erases B. The printed report lists kept patterns under `kept_from_base`.
		- [[Microfreak/Sequence/Storage]] describes how each of these is stored.
	- ## What the write changes
		- The steps, modulation-track destinations and in-use marker of each pattern the description lists. A pattern with no notes or modulation values is marked erased.
		- `Seq.Length`, and `Seq.GateLen` and `Seq.Smooth1`–`Seq.Smooth4` when the description gives them.
		- `Arp.SeqOn` on, so the preset starts in sequencer mode.
		- `Gen.Parafon` (paraphony) on when a step holds more than one note. With paraphony off, the sequencer sounds only the lowest note of a step.
		- The instrument's shortest sequence is 4 steps. A 1–3 step loop is stored repeated, 1 step as 4, 2 as 4 and 3 as 6, which plays the same; the report's `stored_as` says so.
		- The task prints one JSON report: `settings_changed` with each changed setting's old and new value, `sequence` decoded again from the new preset in the description format, `differences` between that and the description (empty when it holds the description), and under `upload` the slot, any backup file and whether the read-back matched. It exits with status 1 when it refuses to write or finds a difference.
	- ## Check it on the instrument
		- `verify-sequence` uses [[Microfreak/CLI/Audition a sequence]] to select the slot, play it with MIDI Start and Clock for `--loops` loops (default 2) at `--bpm` (default 120) and record MIDI out and the H5, then downloads the slot again. It plays with that task's plain timbre unless `--preset-sound` is given. Global settings it changes are restored and read back.
		- It prints a summary and one line per step, and saves the full JSON report and the WAV in `--out-dir`, which must be outside the repository:
		- ```text
		  1.01 expected [G4/100] midi [G4/100] ok audio [G4; G4] match
		  1.02 expected [ held G4] midi [rest] ok audio [G4; G4] held
		  ```
		- `midi_out_matching_steps` and `midi_out_mismatches` compare the notes, velocities, held notes and modulation CCs that MIDI out carried with the description. `audio_checks` counts how the heard pitch compared, with the labels of [[Microfreak/CLI/Audition a sequence]]. `download_matches_description` and `download_equals_upload` check the slot downloaded afterwards. The task exits with status 0 when MIDI out and the download both match.
		- MIDI out is the exact record. The audio confirms that the instrument sounded the notes, and depends on the base's sound: a modulation track that closes the filter, or a preset whose pitch moves, reads as a mismatch.
		- A program change always loads pattern A, so playback is compared with pattern A. To compare with B, see Pattern B below.
	- ## Checked on the instrument, 2026-11-16
		- Each case was one `verify-sequence` run with `--base 358` ([[Microfreak/Preset/358 20241116.1]], Basic Waves, paraphonic, no pitch modulation), two loops at 120 BPM, plain timbre, under the shared hardware lock with no one at the panel. Descriptions, reports and recordings stay in the session's scratch folder. In every case MIDI out matched the description on every played step, and the slot downloaded afterwards decoded to the description and equalled the upload.
		- 431 SeqV L1: one step, E4, stored as 4 steps. Audio matched 8 of 8.
		- 432 SeqV L7: C4 to B4, 7 steps. Audio matched 14 of 14.
		- 433 SeqV L16: 16 steps with 5 rests. Audio matched 22 notes and heard 10 silent rests.
		- 434 SeqV L32: a 32-step scale up and down. Audio matched 64 of 64.
		- 435 SeqV L64: 64 steps, a rest every eighth step, velocities 60–119. Audio matched 112 notes and heard 16 silent rests.
		- 436 SeqV Rests: rests on the first step, on two steps in a row and on the last step. Audio matched 8 notes and 8 rests.
		- 437 SeqV TieSame: G4 held over two steps and F4 over three. MIDI out sent one Note On for each; on the held steps it listed the note as held, and the audio heard the held pitch.
		- 438 SeqV TieDiff: C5 tied into D5, A4 tied into a rest, E4 tied into G4 tied into C4. Each different note started with its own Note On. Audio matched 12 notes and 4 rests.
		- 439 SeqV TieLoop: D4 on step 8 tied into D4 on step 1. The second loop's step 1 sent no Note On and held D4.
		- 440 SeqV Chords: chords of two, three and four notes, a three-note chord held over two steps, and a four-note chord with velocities 40, 70, 100 and 127. MIDI out carried every note with its velocity. The audio chord estimate found every note on 10 of the 12 chord steps; on the other 2, the F3 A3 C4 E4 chord, it found some.
		- 441 SeqV Velocity: A4 at velocities 1, 20, 40, 60, 80, 100, 120 and 127. MIDI out sent each velocity. Audio matched 16 of 16.
		- 442 SeqV ModTrack: track 1 on filter cutoff with 0, 64, 128, 192 (on a rest), 255 and 10, sent as CC 23 0, 32, 64, 96, 127 and 5; track 2 on envelope decay with 40 and 200, sent as CC 106 20 and 100. In the audio the cutoff of 0 and 5 muted the note, as a closed filter does.
		- 443 SeqV A only: pattern A plays, B erased. Audio matched 8 of 8.
		- 444 SeqV B only: A erased, B holds A3 C4 E4 A4. Playback sent no notes and was silent; the download holds B.
		- 445 SeqV A and B: A is C4 E4 G4 C5 and B is A3 C4 E4 A4. Playback played A; the download holds both.
		- 446 SeqV B in A: slot 445's stored pattern B moved into pattern A's place in a downloaded copy, uploaded and played. It played A3 C4 E4 A4, matching on MIDI out and in the audio, so the data written for B plays as described.
		- The same cases with [[Microfreak/Preset/382 Anit]] as the base also matched on MIDI out and in the download, but held notes read a semitone sharp in the audio. A pitch track of the recording showed each Anit note rising about a semitone within 120 ms of its start, which a short note barely shows and a tied one does. Anit stores a modulation-matrix amount, `Co1.EG1`, and a glide that slot 358 lacks.
	- ## Pattern B
		- No MIDI or SysEx message found so far starts pattern B. Selecting a slot loads pattern A, and Start plays it.
		- Tried for this issue, each with slot 445 playing and MIDI out recorded:
			- Song Select 0, 1 and 2 before Start, and Song Select 1 during playback: pattern A each time.
			- Reading every global setting code from 0x00 to 0x7F with operation 0x43, which changes nothing. Every code answers. 0x20–0x4D are the settings named in MIDI Control Center's dictionary, which [Freakout's MIDI Control Center notes](https://github.com/kmorrill/freakout/blob/main/docs/microfreak-mcc-static-analysis.md#microfreak-subcommand-dictionary) recover; none of them concerns patterns. 0x4E–0x7F read 0. 0x00–0x1F hold unnamed values that stayed the same with slot 444 selected, slot 445 selected, during playback and after Stop.
			- Writing the three unnamed codes inside the dictionary's range, 0x2C, 0x48 and 0x4B: each read back unchanged, so the instrument ignored the write.
			- The unnamed codes 0x00–0x1F were not written. How the firmware handles a write to them is unknown, and other agents were sharing the instrument.
			- After these runs, all 128 global codes read back the values they had before.
		- Tried earlier for [#435 Decode how a MicroFreak preset stores its sequence](https://github.com/codekiln/logseq-encode-garden/issues/435) and [#434 Play a MicroFreak slot's sequence and detect its notes through the Zoom H5](https://github.com/codekiln/logseq-encode-garden/issues/434): program change, CCs 1–119 one at a time during playback, and swapping pattern trailer values 10 and 11.
		- [Freakout's firmware notes](https://github.com/kmorrill/freakout/blob/main/docs/microfreak-firmware-notes.md#active-preset-serializer-and-the-operation-19-boundary) found no SysEx handler that reaches the sequencer's working copy of patterns A and B.
		- Pattern B is therefore checked by the download (slots 444 and 445) and by playing B's data from A's place (slot 446). Hearing B itself takes one press on the panel.
		- ### Check pattern B with one press
			- On the MicroFreak, select preset 445, SeqV A and B, and press the B icon in the sequencer row; the display shows Sequence B Loaded.
			- Then run `mise run microfreak:audition --slot 445 --no-select`, or ask an agent to. `--no-select` plays the pattern that is loaded, without a program change.
			- Pattern B plays a rising A minor arpeggio, A3 C4 E4 A4, and MIDI out in the report lists those notes. Pattern A would play C4 E4 G4 C5.
			- To compare that playback with pattern B step by step, save slot 445's description as `a-and-b.json` and run `mise run microfreak:verify-sequence a-and-b.json --slot 445 --pattern B --keep-selection --out-dir /private/tmp/mf-verify`. Run without pressing B, it reported pattern A's notes on all 8 steps as mismatches.
			- ```json
			  {"length": 4, "gate_percent": 50, "patterns": {
			    "A": {"steps": [{"notes": ["C4"]}, {"notes": ["E4"]}, {"notes": ["G4"]}, {"notes": ["C5"]}]},
			    "B": {"steps": [{"notes": ["A3"]}, {"notes": ["C4"]}, {"notes": ["E4"]}, {"notes": ["A4"]}]}}}
			  ```
