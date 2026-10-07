logseq-entity:: [[Logseq/Entity/Question]]

- # Can I record two tracks in [[Ableton/Arrangement View]] while I play other clips in Session View?
	- Recording a [[Microfreak]] on a MIDI track and an audio track into the Arrangement, while launching and recording other [[Ableton/Clip]]s in Session View.
	- ## [[AI Answer]]
		- **Short answer:** yes. Arm the two Microfreak tracks, press Arrangement Record, and keep playing Session clips on other tracks. One caveat: a single track records in one place at a time.
		- **Why:**
			- Arrangement Record is per track: "Recording creates new clips in all tracks that have their Arm button on" ([Recording New Clips](https://www.ableton.com/en/live-manual/12/recording-new-clips/)).
			- Session clips you launch during the pass are recorded to the Arrangement as well ([Automation and Editing Envelopes](https://www.ableton.com/en/live-manual/12/automation-and-editing-envelopes/)).
			- With "Start Playback with Record" off, recording starts when you press Play or launch a Session clip. Holding Shift while pressing Arrangement Record flips that behavior.
		- **Caveats:**
			- A track that is also recording into a Session slot does not also get a separate Arrangement take of the same input. Record the Microfreak in the Arrangement and use Session slots on other tracks. The manual does not spell out what a Session-slot recording does to an armed track during Arrangement Record, so test it before a take that matters.
			- This does not give stacked CC lanes. The knob moves are still MIDI CC data inside the recorded clip, shown one CC at a time in its Envelopes panel. See [[Ableton/Clip/Q/How can I see all MIDI CC clip envelopes stacked in Arrangement View?]].
