logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Ableton/Instrument/Drum Rack/How To/Gate Mode]]

- # How can I make all the drums in my [[Ableton/Instrument/Drum Rack]] be the kind where I press the note and they keep playing?
	- ## [[AI Answer]]
		- **Short answer:** put each pad's sampler in **Trigger** mode, and make that the default pad so every sample you drop in arrives that way. Live has no switch that flips every pad of an existing rack at once.
		- [[Answer/Official]] from [Live 12 Manual: Defaults](https://www.ableton.com/en/live-manual/12/working-with-instruments-and-effects/#defaults) and [Live 12 Manual: Instrument Reference](https://www.ableton.com/en/live-manual/12/live-instrument-reference/)
		- **The setting on one pad** depends on which sampler the pad holds:
			- **Simpler** — set the mode switch to **One-Shot**, then turn on **Trigger**. The sample plays to the end of its region no matter how long you hold the key; **Gate** fades it out at note-off instead. See [[Ableton/Live/UG/31 Instrument Reference/11 Simpler/01 Playback Modes]].
			- **Drum Sampler** — set **Envelope Mode** to **Trigger** and **Hold** to `inf`. Trigger plays on through the Hold time after note-off, so `inf` plays the whole sample. See [[Ableton/Live/UG/31 Instrument Reference/04 Drum Sampler/01 Sample Controls Section]].
		- **For every pad you fill from now on:**
			- 1. Set up one pad as above, with no other settings you don't want copied.
			- 2. Right-click the pad and choose **Save as Default Pad**. That adds it to User Library → Defaults → Dropping Samples → On Drum Rack.
			- 3. Drop samples onto pads; each one loads in that sampler with Trigger already on.
			- The same folder can be filled by dragging an empty, configured Simpler into it. If it holds several, the last one added wins. See [[Ableton/Live/UG/23 Instruments and Effects/02 Using Devices/06 Defaults]].
		- **For a rack you already built:**
			- Quickest: clear the pads and drop the samples back in once the default is saved.
			- Or keep the rack and change each pad by hand, or map each pad's Trigger/Gate control to one Macro so a single knob flips them all.
		- **In Live 11:** there is no Drum Sampler, so pads hold Simpler. In **One-Shot** mode, Simpler plays the whole sample by default however long the note is held, so a pad that stops early is usually in **Classic** mode or has **Gate** on. The pad's context menu saves a pad default, the same as in Live 12, and dragging a configured Simpler into Defaults → Dropping Samples → On Drum Rack also works. Sources: [Live 11 Manual: Default Presets for Dropping Samples](https://www.ableton.com/en/live-manual/11/working-with-instruments-and-effects/) and [Live 11 Manual: One-Shot Playback Mode](https://www.ableton.com/en/live-manual/11/live-instrument-reference/).
		- **If a drum still stops early:** check its **Choke** group in the chain list. Any pad in the same choke group cuts it off when it plays, whatever its mode.
