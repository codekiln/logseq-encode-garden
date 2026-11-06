logseq-entity:: [[Logseq/Entity/Question]]

- # When I select an aggregate device under Sound in the [[Mac/OS]] menu bar, there is no volume slider. How do I control the volume?
	- ## [[AI Answer]]
		- **Short answer:** macOS has no master volume for an aggregate device. Because it combines several devices, there is no single volume for the Sound menu slider or the volume keys to change. Set the level downstream of macOS instead: in the app or DAW, on the interface's own knob, per channel in Audio MIDI Setup, or with a third-party volume tool.
		- **Why it happens:** [[Answer/Official]] from [Create an Aggregate Device to combine multiple audio devices](https://support.apple.com/en-us/102171): an aggregate device merges the inputs and outputs of several devices into one device, for example an eight-channel and a two-channel device into one ten-channel device. Users report the same missing slider for aggregate and multi-output devices on [Apple Community](https://discussions.apple.com/thread/8071644).
		- **Ways to control the level**
			- **In the app or DAW.** This is the usual route for music work. Ableton Live, Logic Pro and similar apps send audio to the aggregate device's outputs, so the master fader sets the level.
			- **On the hardware.** Most audio interfaces control output level with an analog knob after the converter, so macOS cannot set their volume even when you use them on their own. Use the monitor or headphone knob.
			- **Per channel in Audio MIDI Setup.** Select a member device (not the aggregate) in the Audio Devices sidebar, open its **Output** tab, and drag the channel sliders. This works only for devices whose driver exposes software volume, such as built-in speakers. On many interfaces the sliders are greyed out.
			- **Third-party tools.** [SoundSource](https://rogueamoeba.com/soundsource/) sets per-app and per-device volume. [MultiSoundChanger](https://github.com/rlxone/MultiSoundChanger) is an open-source menu bar app that changes the volume of every device in an aggregate device.
		- **If you only need to play to several outputs at once:** that is a multi-output device, not an aggregate device ([Apple guide](https://support.apple.com/guide/audio-midi-setup/play-audio-through-multiple-devices-at-once-ams7c093f372/mac)). It has the same volume limitation, so the options above still apply.
