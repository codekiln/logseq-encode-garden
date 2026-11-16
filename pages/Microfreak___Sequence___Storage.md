see-also:: [[Microfreak/Sequence/Write a sequence]], [[Microfreak/Sequence/Research]], [[Microfreak/CLI/Upload a preset]], [[Microfreak/UG/13 Sequencer]]

- # How a preset stores its sequence
	- A preset keeps sequencer patterns A and B at fixed positions after its named parameters. Each pattern holds 64 steps, whatever the sequence length, followed by a short pattern trailer. The length, gate length and smoothing are named parameters that both patterns share.
	- `mise run microfreak:inspect FILE --sequence` adds the decoded patterns to the inspector's JSON. `mise run microfreak:write-sequence` writes a sequence description into a preset and uploads it, using [lib/sequence.py](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/sequence.py). [[Microfreak/Sequence/Write a sequence]] describes the task and the checks on the instrument:
		- ```sh
		  mise run microfreak:write-sequence sequence.json --base 358 --slot 450
		  ```
		- `sequence.json` looks like this; `velocity` defaults to 100, and patterns left out keep what the base holds:
		- ```json
		  {"length": 16, "gate_percent": 50,
		   "patterns": {"A": {"steps": [
		     {"notes": ["C4"], "velocity": 100},
		     {},
		     {"notes": ["G4"], "tie": true},
		     {"notes": ["G4"]},
		     {"notes": ["C4", "E4", "G4", "B4"], "velocity": [30, 60, 90, 120]},
		     {"notes": [72], "mod": [128, null, null, null]}],
		    "mod_tracks": ["0x0101", null, null, null]}}}
		  ```
		- An empty step is a rest. `tie` holds the step's notes into the next step. `mod` gives the values of modulation tracks 1–4, 0–255, and `mod_tracks` gives each track's destination id; `0x0101` is filter cutoff.
		- Note names put middle C, MIDI note 60, at C4.
	- The layout follows [Freakout's sequence parser](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_sequence.py) and its [firmware notes](https://github.com/kmorrill/freakout/blob/main/docs/microfreak-firmware-notes.md), which say the instrument saves `0x824` values of Sequence A/B state with each preset: two patterns of 1042.
	- ## Where the patterns sit
		- Positions count in the 4088 values that a preset's 4672 transferred values expand to, as described in [PARAMETERS.md](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md).
		- 0 up to the root's `0x20`: named parameters. They ended between 1027 and 1188 in the 23 presets read on [[2026-11-16 Mon]]. `0xFF` and leftover fragments fill the rest up to 1979.
		- 1980–3003: pattern A's 64 step records of 16 values each. 3004–3021: pattern A's trailer.
		- 3022–4045: pattern B's step records. 4046–4063: pattern B's trailer.
		- 4064–4087: zero in every preset read.
	- ## Step record
		- Step n of a pattern starts at the pattern's start + 16 × (n − 1).
		- 0–3, notes: one MIDI note per voice. A value of `0x80` or more means no note there; the instrument writes `0xFF`, and some factory presets hold `0xFB` or `0xFD`. The instrument plays voices from voice 1 up to the first empty one: a step whose voice 1 was empty stayed silent with a note in voice 2 or voice 4, and `[60, empty, 64, empty]` played only 60.
		- 4–7, velocities: one per voice, sent as the note's MIDI velocity. Use 1–127. Velocity 0 went out as a note-on with velocity 0, which receivers treat as a note-off. Velocity 200 sent no note-on.
		- 8–11, modulation-track values: one per track, 0–255. With smoothing off, track 1 aimed at filter cutoff sent CC 23 at half the stored value on each step that held a value: 0, 32, 64, 128, 192, 255, 10 and 200 went out as 0, 16, 32, 64, 96, 127, 5 and 100.
		- 12, status: 0 rest, 1 note, 2 note held into the next step.
			- 1: the notes sound for the gate length, then stop.
			- 2 followed by a step with the same notes: one note, with no new note-on. G4 (2) then G4 (1) sounded once for 1.5 steps at a 50% gate. F4 (2), F4 (2), F4 (1) sounded for 2.5 steps.
			- 2 followed by different notes: the held note stops at the end of its step and the next step's notes start. C5 (2) then D5 (1) gave C5 for 1 step, then D5.
			- 2 followed by a rest: the note sounds to the end of its step.
			- 2 on the last step with the same notes on step 1: the note carries across the loop without a new note-on.
			- Saved presets store a tie this way: the held step gets 2 and the step that ends the tie gets 1 with the same notes. [[Microfreak/Preset/113 D3 Chords]] and [[Microfreak/Preset/382 Anit]] hold such pairs and played them as single long notes.
			- 0, a rest: nothing plays, whatever notes are stored. The instrument writes `FF FF FF FF` with velocities 0 for a recorded rest, and velocities of 100 in steps it never wrote.
			- A status of 3 played like 1. Other values were not tried.
		- 13, modulation presence: bit 0 set means track 1 holds a value on this step, through bit 3 for track 4. A step without the bit sends nothing for that track.
		- 14–15: zero in the presets read. Setting them to 7 and 9 changed nothing heard.
	- ## Pattern trailer
		- 0–7, modulation-track destinations: four little-endian ids, one per track, `FFFF` for an unused track. `0x0101` sent CC 23 (filter cutoff) and `0x0602` sent CC 106 (envelope decay). The other ids in the decoder's table come from Freakout's [live-parameter map](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/freakout_live_map.py) and were not played here.
		- 8, gate copy: equals the gate length in percent in every preset read, but playback ignores it. With `Seq.GateLen` at 90% and this value at 20, notes lasted 5 of 6 clocks; with `Seq.GateLen` at 20% and this value at 90, 1 of 6 clocks. Freakout reports that this value shortened the gate; on this instrument the named parameter decided.
		- 9, length copy: equals the sequence length in every preset read. With `Seq.Length` at 8 and this value at 16, the pattern looped every 8 steps. Setting it to 0 changed nothing heard. Freakout found the same.
		- 10 and 11: in factory presets, 10 is 0 in A and 1 in B, and 11 is 1 in exactly one of the two patterns. Swapping both between A and B left pattern A playing A's steps, so neither picks the pattern that plays.
		- 16, in use: `0xA5` in a pattern that holds steps, `0xFF` in an erased one. Pattern A with all its steps and `0xFF` here played nothing.
		- 12–15 and 17: zero in the presets read. Setting 12–15 to 1–4 changed nothing heard.
	- ## Settings shared by both patterns
		- These are named parameters in the `Seq` and `Arp` sections. Each value is the 0–32767 number that `microfreak:inspect` reports as `value_le_unsigned`.
		- `Seq.Length`: steps = 4 + round(value × 60 / 32767), so 4–64 steps. 6553 is 16 steps and 32767 is 64. Lengths 1–3 do not exist on the instrument; `microfreak:write-sequence` stores a 1–3 step loop repeated to fill 4 or 6 steps.
		- `Seq.GateLen`: percent = 10 + round(value × 80 / 32767), so 10–90%. 16384 is 50%.
		- `Seq.Smooth1`–`Seq.Smooth4`: 0 off, 32767 on. With smoothing on, [[Microfreak/Preset/005 MotivSeq]] sent a run of CC values gliding toward each stored value; with smoothing off, each step sent one CC.
		- `Arp.SeqOn`: 32767 puts the preset in sequencer mode. [[Microfreak/Preset/003 Trance]] holds a pattern with this off and played nothing; a copy with it on played the pattern.
		- `Arp.Div` sets the clocks per step under external clock: 22937 gave 6 clocks (sixteenth notes) and 16384 gave 12. Other values were not measured.
	- ## How the playback was checked
		- Each experiment preset started from [[Microfreak/Preset/382 Anit]], a preset with the sequencer on and paraphony on. `lib/sequence.py` wrote the steps, sometimes followed by a direct edit of one value, and [[Microfreak/CLI/Upload a preset]] wrote the result to a slot from 330 to 339 and read it back unchanged.
		- A script then selected the slot (CC 0 bank select, program change), turned the global Arp/Seq MIDI Out setting on (SysEx operation `0x42`, code `0x2B`), sent MIDI Start and 24-per-quarter-note clock at 240 BPM, recorded the notes and CCs the MicroFreak sent back, sent Stop and set Arp/Seq MIDI Out back to off. Clock Source (code `0x2E`) was already USB. [#434 Audition a MicroFreak slot's sequence](https://github.com/codekiln/logseq-encode-garden/issues/434) builds the same procedure into a task.
		- Before any upload, playing [[Microfreak/Preset/382 Anit]], [[Microfreak/Preset/113 D3 Chords]], [[Microfreak/Preset/005 MotivSeq]] and [[Microfreak/Preset/035 FM Seq]] sent the notes, chords and velocities the decoder reads from their downloads.
		- Experiments on [[2026-11-16 Mon]], one slot each:
			- 330: a 16-step pattern A with single notes, a rest, a four-note chord with four velocities, and three kinds of tie. Everything played as listed under Step record, and step 17 started the loop again.
			- 331 and 333: gate and length copies against `Seq.GateLen` and `Seq.Length`.
			- 332: pattern A marked erased with its steps in place.
			- 334: two modulation tracks with smoothing off.
			- 335: status 3, empty voice 1, a note only in voice 4, velocities 0 and 200, non-zero reserved values.
			- 336: 64 steps with notes 36–99 and velocities 1–64. All 64 played in order, then looped.
			- 337: trailer values 10 and 11 swapped between the patterns.
			- 338: a voice gap, a tie into a different note, and a tie across the loop.
			- 339: [[Microfreak/Preset/003 Trance]] with `Arp.SeqOn` on.
	- ## Open questions
		- Playing pattern B from the Mac. A preset always starts with pattern A after a program change, even when A is erased and B holds steps ([[Microfreak/Preset/395 26.06.25]] stayed silent). Song Select, CCs 1–119 sent one at a time during playback (except 32 and 64), swapping trailer values 10 and 11, and the global settings tried in [[Microfreak/Sequence/Write a sequence]] did not switch to B. Pattern B data written here played as described once moved to pattern A's place, and downloads hold it unchanged. Pressing B on the panel and running `mise run microfreak:audition --slot 445 --no-select` would play it in its own place.
		- What trailer values 10 and 11 record. Pattern identity kept through a copy, and the pattern selected when the preset was saved, fit the factory data but are untested.
		- Whether the instrument treats `0xFB`, `0xFD` and `0xFF` differently anywhere besides playback.
		- What a velocity of 0 or above 127 does to the sound. Only MIDI out was observed.
		- Whether pressure (aftertouch) recorded in real time is stored anywhere in the step record.
		- The `Arp.Div` values that give other step lengths.
