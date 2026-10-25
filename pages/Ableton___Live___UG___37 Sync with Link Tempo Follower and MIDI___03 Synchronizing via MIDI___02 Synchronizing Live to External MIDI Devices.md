logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/37 Sync with Link Tempo Follower and MIDI/03 Synchronizing via MIDI]]
prev:: [[Ableton/Live/UG/37 Sync with Link Tempo Follower and MIDI/03 Synchronizing via MIDI/01 Synchronizing External MIDI Devices to Live]]
next:: [[Ableton/Live/UG/37 Sync with Link Tempo Follower and MIDI/03 Synchronizing via MIDI/03 Sync Delay]]
- # [37.3.2 Synchronizing Live to External MIDI Devices](https://www.ableton.com/en/live-manual/12/synchronizing-with-link-tempo-follower-and-midi/#synchronizing-live-to-external-midi-devices)
	- To follow an external sequencer, set it up to send sync and enable it as a sync source in the Tempo & MIDI Settings. An **EXT** button then appears in the [[Ableton/Live/UI/Control Bar]]; turn it on, or use Options → External Sync. The upper LED beside EXT flashes when usable sync arrives.
	- Live accepts song position pointers, so it jumps when the host jumps. With [[Ableton/Live/UI/Control Bar/Toggle/Arrangement Loop]] on, positions wrap into the loop.
	- ## 37.3.2.1 MIDI Timecode Options
		- Set per MIDI device by selecting it in the MIDI Ports list of the Tempo & MIDI Settings. Both options apply only when the MIDI Sync Type is MIDI Timecode.
		- **MIDI Timecode Rate** — the SMPTE frame rate to follow. "SMPTE All" detects the format automatically. The Arrangement's display format is set separately under Options → Time Ruler Format.
		- **MIDI Timecode Offset** — a SMPTE time that Live treats as the Arrangement's start.
