logseq-entity:: [[Logseq/Entity/Term]]

- # MIDI Clock
	- The [[MIDI/Message]] types that keep devices at one tempo and start and stop them together. They are system real-time messages: they carry no channel and may arrive in the middle of any other message.
	- **Timing Clock** (F8h) — sent 24 times per quarter note. The tempo is the spacing between them; the message carries no number.
	- **Start** (FAh) plays from the beginning, **Stop** (FCh) halts, and **Continue** (FBh) resumes where playback stopped.
	- **Song Position Pointer** (F2h), a system common message, tells a follower where to resume, counted in sixteenth notes of six clocks each.
	- One device sends clock and the others follow. Ableton Live can do either ([[Ableton/Live/UG/37 Sync with Link Tempo Follower and MIDI/03 Synchronizing via MIDI]]), and sends clock to the MicroFreak over [[Microfreak/MIDI/Port/Arturia MicroFreak]].
