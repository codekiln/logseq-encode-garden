logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Music/Making/Log/26/10/28 Wed]]

- # What's the difference between Post FX and Post Mixer for a track's audio input in [[Ableton]] Live?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [Live 12 Manual, 17.5.1 Internal Routing Points](https://www.ableton.com/en/live-manual/12/routing-and-i-o/#internal-routing-points)
		- **Short answer:** both include the tapped track's devices. Post Mixer also includes the track's own volume and pan, and likely its mute and crossfader assignment. Post FX includes none of these. Neither tap includes sends.
		- When a track's **Audio From** is another track, the **Input Channel** chooser sets the tap point ([[Ableton/Live/UG/17 Routing and IO/05 Internal Routings/01 Internal Routing Points]]):
			- **Post FX** — "taps the signal at the output of a track's device chains (FX), but before it has been passed back to the track mixer. Changes to the tapped track's devices will therefore alter the tapped signal, but changes to its mixer settings will not."
			- **Post Mixer** — "taps the final output of a track, after it has passed through its device chains and mixer."
		- **In practice:**
			- Post FX records the processed sound at its device-chain level. Moving the source track's fader or pan, whether to mix or to silence it, leaves the recording unchanged.
			- Post Mixer records what the source track sends to its output: fader moves and panning are recorded too. The manual's post-effects recording example: "we could also tap the Guitar track Post Mixer if we wished to record any level or panning from it."
		- **What "mixer" covers in Post Mixer:** the track's own output after its gain stage. The manual doesn't list the controls, so the following is read from [[Ableton/Live/UG/18 Mixing]]:
			- **Volume and pan** — included; the manual's guitar example names level and panning.
			- **Track Activator** — likely included. A return's Post send taps "after the track's pan, volume and activator" ([[Ableton/Live/UG/18 Mixing/04 Return Tracks and the Main track]]), which places the activator in that same stage.
			- **Crossfader A/B assignment** — likely included. It changes "volume at each track's gain stage" ([[Ableton/Live/UG/18 Mixing/05 Using Live's Crossfader]]).
			- **Sends** — not included. Send knobs sit in the mixer section, but a send copies the signal to a return track without changing the track's own output. The return's effects never reach a Post Mixer tap, and send levels don't change what it records.
			- **Solo and Arm** — don't alter the sound.
			- To test the two "likely" items: tap a track Post Mixer, then mute the source, or assign it to A and move the crossfader to B, and watch the receiving track's input meter.
		- **Solo:** soloing the receiving track still lets you hear a source tapped Post FX, but not one tapped Post Mixer.
		- Rack chains offer the same three tap points. There, Post Mixer is the chain's output after its chain mixer, just before the chains are summed ([[Ableton/Live/UG/17 Routing and IO/05 Internal Routings/02 Making Use of Internal Routing]]).
