up:: [[Ableton/Live/v/12]]
- # Note Probability Groups
	- Live 11's Chance lane gives each note its own probability. Live 12 can share a Chance value across selected notes. Play All makes a chord or fill happen together. Play One picks a single note at random when the group plays. [Live 11 Chance Editor](https://www.ableton.com/en/live-manual/11/editing-midi-notes-and-velocities/#editing-probabilities) · [Live 12 Probability Groups](https://www.ableton.com/en/live-manual/12/editing-midi/#probability-groups)
	- ## Try a chord, then a choice of pitches
		- Put a chord on the last beat of a looping MIDI clip. Select its notes and choose **Group Notes (Play All)** from the MIDI Note Editor context menu. Open the Chance lane and set the diamond marker to 50%. Listen for the whole chord or silence at that beat.
		- Switch the group to **Play One** and set its triangle marker to 100%. Each pass plays one of the pitches at that beat. Lowering the group Chance changes how often a note sounds. Live exposes one group Chance value and chooses the member at random, so the group has no per-member weighting control.
		- To choose among whole phrases with different probabilities, set up clip-to-clip transitions with Follow Actions in [[Ableton/Live/v/12/MIDI Tools]].
	- [[Ableton/Live/UG/10 Editing MIDI/05 Editing MIDI Notes/13 Editing Probabilities]] covers the Chance lane, group markers, and ungrouping.
