logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/39 Audio Fact Sheet/02 Neutral Operations]]
prev:: [[Ableton/Live/UG/39 Audio Fact Sheet/02 Neutral Operations/06 Recording Internal Sources at 32 Bit]]
next:: [[Ableton/Live/UG/39 Audio Fact Sheet/02 Neutral Operations/08 Bypassed Effects]]
- # [39.2.7 Freezing Tracks](https://www.ableton.com/en/live-manual/12/audio-fact-sheet/#freezing-tracks)
	- Freeze writes 32-bit files, so frozen audio is no worse than what played before freezing. Some cases still change the result:
		- Frozen Session View clips are two loop cycles long, so longer tails get cut off. Arrangement View freezes keep tails past the clip end.
		- Frozen reverb and delay tails stop abruptly when playback stops, because they are rendered audio.
		- Frozen Arrangement clips include their automation. Frozen Session clips keep the parameter values found at the Arrangement's 1.1.1 position.
		- Frozen clips always play with Warp on in Beats mode.
		- Random device parameters, such as Beat Repeat's Chance, stop being random after freezing.
