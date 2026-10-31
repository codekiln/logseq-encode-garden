logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Ableton/Live/UG/37 Sync with Link Tempo Follower and MIDI]]
prev:: [[Ableton/Live/UG/37 Sync with Link Tempo Follower and MIDI/02 Synchronizing via Tempo Follower]]
- # [37.3 Synchronizing via MIDI](https://www.ableton.com/en/live-manual/12/synchronizing-with-link-tempo-follower-and-midi/#synchronizing-via-midi)
	- Devices without Link can sync over [[MIDI]]. Both MIDI methods use a sync host that sends the signal and devices that follow it.
		- **MIDI Clock** — ticks at a tempo-dependent rate, like a fast metronome, plus song position messages. Live can be host or device.
		- **MIDI Timecode** — the MIDI form of SMPTE, giving time in seconds and frames. Live reads it as an Arrangement position. It carries no tempo, so tempo changes are not tracked and the tempo must be set by hand. Live can only follow Timecode, not send it.
	- {{embed [[Ableton/Live/UG/37 Sync with Link Tempo Follower and MIDI/03 Synchronizing via MIDI/01 Synchronizing External MIDI Devices to Live]]}}
	- {{embed [[Ableton/Live/UG/37 Sync with Link Tempo Follower and MIDI/03 Synchronizing via MIDI/02 Synchronizing Live to External MIDI Devices]]}}
	- {{embed [[Ableton/Live/UG/37 Sync with Link Tempo Follower and MIDI/03 Synchronizing via MIDI/03 Sync Delay]]}}
