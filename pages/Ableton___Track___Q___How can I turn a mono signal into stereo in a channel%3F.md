logseq-entity:: [[Logseq/Entity/Question]]

- # How can I turn a mono signal into stereo in a channel in [[Ableton/Live]]?
	- ## [[AI Answer]]
		- **Short answer:** the channel is already stereo and carries the same signal twice, so the work is making the left differ from the right. Utility's Width knob will not do it. Reach for a device that puts a different signal on each side: **Delay** with Stereo Link off and unequal left and right times, **Chorus-Ensemble**, a reverb, or an Audio Effect Rack holding two chains panned hard apart with a few milliseconds of delay on one of them.
		- ### There is no mono channel to convert
			- [[Answer/Official]] from [Mono/Stereo Conversions](https://www.ableton.com/en/live-manual/12/routing-and-i-o/#monostereo-conversions): "Signals in the track's device chain are always stereo, even when the track's input is mono or when the track plays mono samples. Mono is turned into stereo simply by using the identical signal for left and right channels."
			- A mono sample, a mono input and a mono synth all reach the device chain as two identical channels. Stereo is whatever difference you put between them.
		- ### Utility's Width knob does nothing here
			- Width scales the side component, which is the difference between left and right. Identical channels have no difference, so the knob sweeps with nothing to scale.
			- The manual describes Utility's Mid/Side control as "a continuous mono to stereo controller." It rebalances the mid and the side that a signal already carries. When the side is silent, every position of that knob sounds the same.
			- Utility is still worth having at the end of the chain once the width exists: the Mono switch checks what the mix collapses to, and Bass Mono holds the low end in the center.
		- ### Devices that split the two channels apart
			- | Device                           | Setting that splits the channels                      | What it does to the sound                        |
			  | -------------------------------- | ----------------------------------------------------- | ------------------------------------------------ |
			  | **Delay**                        | Stereo Link off, left 12 ms, right 30 ms, Feedback 0% | width out of arrival time                        |
			  | **Chorus-Ensemble**              | Classic or Ensemble mode, Width above 100%            | thickening with slow motion inside it            |
			  | **Reverb**                       | Stereo at 120 degrees                                 | space around the sound                           |
			  | **Auto Pan-Tremolo**             | Panning mode, Stereo Offset in Phase at 180 degrees   | the source swinging across the field             |
			  | **Shifter**                      | Wide on, small Spread values                          | detune leaning opposite ways on each side        |
			  | **Erosion**, Live 12.4 and later | Stereo Width at 100%                                  | grit that differs between the channels           |
			- The delay figures are the Delay device's own chorus recipe from [Delay Tips](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#delay-tips), which also asks for the band-pass filter at 2.56 kHz and Ping Pong on.
			- Reverb is the gentlest of these on a lone mono source, because the tail is stereo whatever arrives. At a Stereo setting of 120 degrees "each ear receives a reverberant channel that is independent of the other."
		- ### Building the width by hand
			- Two chains and a short delay give the most control. This is the Haas effect, built from Live's own devices:
				- 1. Select the track's devices and press `Cmd` `G` to group them into an Audio Effect Rack.
				- 2. Duplicate the chain so the Rack holds two.
				- 3. Pan one chain hard left and the other hard right. Chains in an Audio Effect Rack carry their own volume and pan sliders.
				- 4. On one chain add **Delay** with Dry/Wet at 100%, Feedback at 0%, Stereo Link on, and a time between 8 and 30 ms.
				- 5. Trim that chain's volume down a decibel or two to pull the image back toward the center.
			- Under roughly 30 ms the ear hears one sound pulled toward the earlier side rather than two sounds. Above it the delay starts to read as a slapback.
			- Any difference between the chains works the same way: EQ Eight tilted opposite directions, a small pitch offset, different saturation.
		- ### Check it in mono
			- Width built from short delays partly cancels when the channels are summed. Put a Utility on the Main track, press Mono, and listen for the sound thinning or going hollow. Chorus and reverb survive that sum more easily than a sub-30 ms delay does.
		- ### When the source should have been stereo already
			- A track records mono samples when its Input Channel is a mono input, so a two-channel source arriving on one input stays mono for good. Choosing a stereo pair records both sides. Which hardware inputs appear as mono and which as stereo pairs is set in the Channel Configuration dialog in the audio settings.
			- A mono patch on a Live instrument has a closer answer than any effect: Operator's Spread "creates a rich stereo chorus by using two voices per note and panning one to the left and one to the right," and Wavetable's Unison modes "use multiple oscillators with different phases, stereo locations, or wavetable positions to provide a fuller sound."
		- ### Scope of this answer
			- Parameter names and quoted lines read from Ableton's Live 12 manual in September 2026. The Live 11 copy filed at [[Ableton/Manual]] carries the same Mono/Stereo Conversions wording, and calls the device Auto Pan rather than Auto Pan-Tremolo. Erosion's Stereo Width control arrived in Live 12.4.
