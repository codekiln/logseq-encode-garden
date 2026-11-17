see-also:: [[Microfreak/CLI/Inspect a preset]], [[Microfreak/CLI/Upload a preset]], [[Microfreak/CLI/Audition a sequence]], [[Zoom H5/My Unit]]

- # Probe a patch
	- `mise run microfreak:probe` changes stored settings of a preset, writes the result to a slot, selects it and plays a short MIDI script into it while the [[Zoom H5/My Unit]] records. It prints one JSON report with the level, pitch and brightness of each note. I use it to find out what a stored field does by listening to two values of it side by side.
	- ## Run it
		- Close MIDI Control Center, connect the MicroFreak and the H5 by USB, and run the task from the garden root. Keep hands off the keys while it plays.
		- ```sh
		  mise run microfreak:probe --base 359 --slot 501 --backup-dir "$TMPDIR/mf-probe/backup"
		  mise run microfreak:probe --base 359 --slot 501 --backup-dir "$TMPDIR/mf-probe/backup" --set Gen.PrstVol=0
		  mise run microfreak:probe --base 359 --slot 501 --backup-dir "$TMPDIR/mf-probe/backup" \
		    --set VCO.BendRng=2 --script "$TMPDIR/mf-probe/bend.yaml" --output "$TMPDIR/mf-probe/bend.json"
		  ```
		- `--base` is the preset to start from: a slot number, which the task reads and leaves unchanged, or a `.bin` file from `microfreak:download`. Slot 359, Init, holds every field firmware 5 saves; an older preset can lack fields such as `Kbd.Scale` or `EG2.Snap`, and the task refuses to set a field the base lacks.
		- `--slot` is where the result goes. When the slot holds a preset, the task saves it first in a new timestamped folder under `--backup-dir`, so one test slot can be probed again and again. The preset is stored as `Probe` unless `--name` gives another name.
		- Slots 497–512 are my test slots. My own presets fill slots 1–320 and 350–402.
	- ## Setting values
		- `--set NAME=VALUE` changes one stored field, by the name `microfreak:inspect` prints. Repeat it for more fields.
			- An integer is a choice: `VCO.BendRng=2`, `Kbd.Scale=1`. The task stores choice × 32767 ÷ the field's descriptor, the number of choices minus one, the way every saved preset does.
			- A decimal is a normalized value from 0 to 1, such as `VCF.Cutoff=0.5`, or from −1 to 1 for a matrix amount, such as `Co1.LFO=-0.25`.
			- `raw:N` stores N as it is, such as `Mat.Assign1=raw:0x0d01`.
		- The report's `settings_changed` gives each changed field's stored value before and after.
	- ## Scripts
		- Without `--script` the task plays one note, C4 at velocity 100 for 1.5 seconds, then records one more second. `--note`, `--velocity`, `--hold` and `--tail` change it.
		- A script is a YAML or JSON list of timed events, in seconds from the start:
		- ```yaml
		  events:
		    - {t: 0.0, on: C4, velocity: 100}
		    - {t: 0.5, bend: 1.0}
		    - {t: 1.0, bend: -1.0}
		    - {t: 1.5, bend: 0}
		    - {t: 1.6, cc: [1, 0], to: 127, over: 1.0}
		    - {t: 2.0, pressure: 100}
		    - {t: 3.0, off: C4}
		  tail: 1.0
		  ```
		- `on` and `off` take a note name (C4 is MIDI 60) or number. `bend` runs from −1 (full down) to 1 (full up). `cc` takes a controller number and value. `pressure` sends channel pressure (aftertouch) 0–127. `to` and `over` turn a bend, CC or pressure into a ramp, with CC and pressure values rounded to whole numbers. `tail` is how long the recording runs after the last event.
		- The messages go out on the MicroFreak's MIDI input channel, which the task reads from the instrument first.
	- ## Report
		- `played` lists each event with the time it was sent.
		- `notes` has one summary per note: `onset_latency_ms`, `peak_db` and `end_db` in dB relative to the H5's full scale, `pitch` and `midi_median` from the YIN method with `cents_from_note`, the lowest and highest pitch heard during the note, and `centroid_hz_median`, the spectral centroid, which rises as the sound gets brighter.
		- A note's pitch and brightness come from its frames within 30 dB of its peak, so a decaying note's quiet tail stays out. Each frame's centroid counts only the spectrum within 40 dB of that frame's strongest component, which keeps the H5's noise floor out of it.
		- A sub-oscillator one octave down makes the waveform repeat at the sub's period, so `pitch` reads an octave low and `cents_from_note` near −1200.
		- `--frames` also prints `frames`, the recording measured every 10 ms with the same values. A frame quieter than −70 dBFS has only `t` and `db`, and a frame where no pitch was found has no `f0_hz`, `midi` or `aperiodicity`. `--output` saves the report with every frame. `--wav-dir` saves the recording. Both must be outside the repository.
		- Levels are absolute, so two runs compare directly when the H5's input gain stays the same between them.
	- ## Example
		- Slot 359's sound with `Gen.PrstVol` (Preset Volume) at 0, 12 and 24 played C4 at −27.8, −22.3 and −16.3 dBFS: about half a decibel per step of the setting. The pitch read 60.002 each time.
	- ## Source
		- [#449 Add microfreak:probe to play notes into a written patch and measure it with the H5](https://github.com/codekiln/logseq-encode-garden/issues/449) added the task, as part of [#448 Let an agent set any MicroFreak patch setting from a description](https://github.com/codekiln/logseq-encode-garden/issues/448).
		- The code is [lib/probe.py](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/probe.py). `mise run microfreak:test` runs its tests.
