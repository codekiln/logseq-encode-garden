logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Music/Making/Log/26/10/28 Wed]]

- # What's the difference between Post FX and Post Mixer for a track's audio input in [[Ableton]] Live?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [Live 12 Manual, 17.5.1 Internal Routing Points](https://www.ableton.com/en/live-manual/12/routing-and-i-o/#internal-routing-points)
		- **Short answer:** both include the tapped track's devices. Post Mixer also includes its mixer, meaning its volume and pan. Post FX does not.
		- When a track's **Audio From** is another track, the **Input Channel** chooser sets the tap point ([[Ableton/Live/UG/17 Routing and IO/05 Internal Routings/01 Internal Routing Points]]):
			- **Post FX** — "taps the signal at the output of a track's device chains (FX), but before it has been passed back to the track mixer. Changes to the tapped track's devices will therefore alter the tapped signal, but changes to its mixer settings will not."
			- **Post Mixer** — "taps the final output of a track, after it has passed through its device chains and mixer."
		- **In practice:**
			- Post FX records the processed sound at its device-chain level. Moving the source track's fader or pan, whether to mix or to silence it, leaves the recording unchanged.
			- Post Mixer records what the source track sends to its output: fader moves and panning are recorded too. The manual's post-effects recording example: "we could also tap the Guitar track Post Mixer if we wished to record any level or panning from it."
		- **Solo:** soloing the receiving track still lets you hear a source tapped Post FX, but not one tapped Post Mixer.
		- Rack chains offer the same three tap points. There, Post Mixer is the chain's output after its chain mixer, just before the chains are summed ([[Ableton/Live/UG/17 Routing and IO/05 Internal Routings/02 Making Use of Internal Routing]]).
