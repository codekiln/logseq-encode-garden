logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Ableton/Live/UG/29 Audio Effect Reference]]
prev:: [[Ableton/Live/UG/29 Audio Effect Reference/10 Corpus]]
next:: [[Ableton/Live/UG/29 Audio Effect Reference/12 Drum Buss]]
- # [29.11 Delay](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#delay)
	- ![The Delay Effect](https://ableton-production.imgix.net/live-manual/12/DelayEffectL12.png?auto=&w=320)
	- Delay has a separate delay line for each stereo channel, a band-pass filter, and LFO modulation.
	- **Delay Time Mode** — **Sync** (beat divisions) or **Time** (1 ms to 5 s)
		- In Sync, numbered buttons set the delay in sixteenths; 4 is one beat. **Offset** sliders move each delay slightly early (negative) or late (positive), for swing.
	- **Stereo Link** — one delay time for both channels; Offset stays separate
	- **Feedback** — output fed back into each channel's own delay line; left and right do not cross
	- **Freeze** — loops whatever is in the buffer at that moment and ignores new input until released
	- **Filter** — band-pass before the delay. Drag in the display: horizontal for frequency, vertical for width; or use **Freq** and **Width**.
	- An LFO can modulate delay time and filter frequency, from chorus to chopped glitches. The **LFO Controls** toggle expands the full LFO section; its LED flashes at the LFO rate.
		- ![Use the LFO Controls Toggle to Expand the LFO Section](https://ableton-production.imgix.net/live-manual/12/DelayEffectLFOToggleL12.png?auto=&w=320)
		- ![LFO Modulation Options in Delay](https://ableton-production.imgix.net/live-manual/12/DelayEffectLFOL12.png?auto=&w=320)
		- **Delay** — LFO amount on delay time; **Filter** — on filter frequency
		- **Rate** mode — Rate, Time, Synced, Triplet, Dotted, Sixteenth
		- **Wave** — Sine, Triangle, Ramp Up, Ramp Down, Square, S&H, Wander; **Morph** reshapes it
	- Smoothing, for when the delay time changes during playback:
		- **Repitch** (default) — pitch bends like an old tape delay
		- **Fade** — crossfades old and new times; gradual changes can sound granular
		- **Jump** — switches at once, possibly clicking
		- LFO modulation sounds different in each mode.
	- **Ping Pong** — bounces the delay between left and right
	- **Dry/Wet** — set to 100% on a return track
	- {{embed [[Ableton/Live/UG/29 Audio Effect Reference/11 Delay/01 Context Menu Options for Delay]]}}
	- {{embed [[Ableton/Live/UG/29 Audio Effect Reference/11 Delay/02 Delay Tips]]}}