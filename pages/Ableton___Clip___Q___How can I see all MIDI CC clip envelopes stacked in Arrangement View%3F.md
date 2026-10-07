logseq-entity:: [[Logseq/Entity/Question]]

- # How can I see all the MIDI CC clip envelopes of an [[Ableton/Clip]] stacked in [[Ableton/Arrangement View]], like track automation lanes?
	- Recorded a [[Microfreak]] into a Session View clip (MIDI and audio) while turning knobs, then dragged the clip into the Arrangement. In the clip's Envelopes panel the **MIDI Ctrl** chooser shows one CC at a time, but I want every automated CC as its own lane under the track, the way mixer and device automation shows.
	- ## [[AI Answer]]
		- **Short answer:** as far as the documentation and the UI show, you cannot. MIDI CC data recorded into a clip stays clip-envelope data and has no automation lanes in the Arrangement. This is an inference from the manual plus the track chooser in the screenshot, not something the manual states in one sentence.
		- **Why:**
			- The manual says "Any automation in Session View becomes track-based automation when clips are recorded or copied into Arrangement View" ([Automation and Editing Envelopes](https://www.ableton.com/en/live-manual/12/automation-and-editing-envelopes/)). That sentence covers mixer and device parameters.
			- The MIDI track's automation chooser in Arrangement View offers only `None` and `Mixer` (plus `Show Automated Parameters Only`), so there is no `MIDI Ctrl` entry to show CC lanes.
			- The manual describes MIDI controller data as clip envelopes, chosen with `MIDI Ctrl` in the clip's Device chooser ([MIDI Controller Clip Envelopes](https://www.ableton.com/en/live-manual/12/clip-envelopes/)). The only place to edit it is the Envelopes panel of the clip.
		- **What you can do:**
			- Find which CCs have data: in the `MIDI Ctrl` Control chooser, controllers that already hold recorded data have an LED dot next to the name ([manual](https://www.ableton.com/en/live-manual/12/clip-envelopes/)). In the screenshot that is 12, 13, 23, 24, 26, 28 and 29.
			- Edit one CC at a time in the Envelopes panel of the selected Arrangement clip, as you already do.
			- To get stacked, editable lanes you would need the CC to drive an automatable parameter on a device, for example a Max for Live device that maps incoming CCs to its own parameters. I have not verified that approach.
		- **Not settled:** whether a newer Live release adds CC lanes to the Arrangement. I checked the Live 12 manual only.
