logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Ableton/Live/UG/40 MIDI Fact Sheet]]
prev:: [[Ableton/Live/UG/40 MIDI Fact Sheet/02 MIDI Timing Problems]]
next:: [[Ableton/Live/UG/40 MIDI Fact Sheet/04 Variables Outside of Live's Control]]
- # [40.3 Live’s MIDI Solutions](https://www.ableton.com/en/live-manual/12/midi-fact-sheet/#lives-midi-solutions)
	- Ableton works from two assumptions: latency is better than jitter, because it is predictable, and when playing through while recording you want to record what you hear, even if that is slightly later than what you played.
	- **Recording** — the MIDI interface driver timestamps each event on arrival, and Live places the event in the clip by that timestamp.
	- **Playthrough** — Live delays events by a constant amount rather than playing them whenever the busy system gets to them. With monitoring on, it adds a delay based on the audio buffer size, so notes land in the clip where you heard them.
	- **Playback to hardware** — Live sends timestamps for the driver to schedule outgoing events. Windows MME drivers cannot use timestamps, so Live schedules those events itself.
	- During audio dropouts Live still receives and records MIDI correctly, even if playthrough sounds wrong; playback is accurate once the system recovers.
