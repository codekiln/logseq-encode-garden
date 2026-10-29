- # Pattern A and B
	- A live-looping setup for [[GitP/A]] in [[Ableton/Live]], with paired audio and MIDI tracks for Pattern A and Pattern B, a full performance capture, commentary, and the [[Launchpad/Custom/Mode/1 Arrangement]] controls.
	- Record an audio loop alongside its MIDI in Session View. Arrangement Record captures launched clips on the timeline; the performance capture tracks preserve the combined signal.
	- ## Recording routes
		- Pattern A and Pattern B audio use external input 3 and feed Performance Audio. Their MIDI feeds Performance MIDI; Performance MIDI has no hardware output, so recorded loops do not replay into the MicroFreak.
		- Launchpad to MicroFreak carries live playing to the synth. MicroFreak to Launchpad preserves the existing return route. The commentary microphone uses external inputs 1/2.
		- Arm the active Pattern audio/MIDI pair to capture a loop. Keep Performance Audio, Performance MIDI, commentary, and the MIDI bridges armed for Arrangement recording. Disarm the completed Pattern pair before recording the other.
		- Audio and MIDI monitoring follow the existing template. Check the interface inputs before recording.
	- [Live 11 base Set](../assets/GitP___A___Template___Pattern%20A%20and%20B.als)
	- ## Declare and compile
		- An episode selects this setup with the page property `ableton-template::` linking here. Its Ableton Session block overrides tempo or replaces a complete Tracks, Scenes, Locators, or Controls section.
		- [[GitP/mise/Task/ableton/sync]] compiles the declaration into a new Live Set.
	- Ableton Session
	  spec-version:: 1
	  live-version:: 11
	  base-template:: assets/GitP___A___Template___Pattern A and B.als
	  tempo:: 120
	  time-signature:: 4/4
		- Tracks
			- Pattern A
			  track-key:: pattern-a
			  source-track-id:: 30
			  type:: group
			- Pattern B
			  track-key:: pattern-b
			  source-track-id:: 31
			  type:: group
			- Pattern A Audio
			  track-key:: pattern-a-audio
			  source-track-id:: 23
			  type:: audio
			  monitor:: auto
			  arm:: false
			- Pattern A MIDI
			  track-key:: pattern-a-midi
			  source-track-id:: 24
			  type:: midi
			  monitor:: auto
			  arm:: false
			- Pattern B Audio
			  track-key:: pattern-b-audio
			  source-track-id:: 21
			  type:: audio
			  monitor:: auto
			  arm:: false
			- Pattern B MIDI
			  track-key:: pattern-b-midi
			  source-track-id:: 22
			  type:: midi
			  monitor:: auto
			  arm:: false
			- Performance Audio
			  track-key:: performance-audio
			  source-track-id:: 26
			  type:: audio
			  monitor:: auto
			  arm:: true
			- Performance MIDI
			  track-key:: performance-midi
			  source-track-id:: 27
			  type:: midi
			  monitor:: auto
			  arm:: true
			- Commentary
			  track-key:: commentary
			  source-track-id:: 8
			  type:: audio
			  monitor:: auto
			  arm:: true
			- Launchpad to MicroFreak
			  track-key:: launchpad-to-microfreak
			  source-track-id:: 28
			  type:: midi
			  monitor:: auto
			  arm:: true
			- MicroFreak to Launchpad
			  track-key:: microfreak-to-launchpad
			  source-track-id:: 29
			  type:: midi
			  monitor:: auto
			  arm:: true
		- Scenes
			- Opening
			  scene-key:: opening
			- Pattern A
			  scene-key:: pattern-a
			- Pattern B
			  scene-key:: pattern-b
			- Improvisation
			  scene-key:: improvisation
			- Reflection
			  scene-key:: reflection
		- Locators
			- Opening
			  bar:: 1
		- Controls
			- Arrangement Record
			  action:: record
			  cc:: 119
			  channel:: 16
			- Set Locator
			  action:: set-locator
			  cc:: 116
			  channel:: 16
			- Previous Locator
			  action:: previous-locator
			  cc:: 117
			  channel:: 16
			- Next Locator
			  action:: next-locator
			  cc:: 118
			  channel:: 16
