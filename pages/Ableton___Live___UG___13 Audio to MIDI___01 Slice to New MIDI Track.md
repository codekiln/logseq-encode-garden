logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Ableton/Live/UG/13 Audio to MIDI]]
next:: [[Ableton/Live/UG/13 Audio to MIDI/02 Convert Harmony to New MIDI Track]]

- # [13.1 Slice to New MIDI Track](https://www.ableton.com/en/live-manual/12/converting-audio-to-midi/#slice-to-new-midi-track)
	- Slicing cuts the audio into pieces of time, one per MIDI note, without analysing pitch or rhythm. The pieces keep playing the original sound.
		- ![The slicing dialog](https://ableton-production.imgix.net/live-manual/12/SlicingDialog.png?auto=&w=320)
	- The dialog slices by beat division, by transients or by Warp Markers, and offers a Slicing Preset. A Rack holds at most 128 chains, so Live refuses settings that would make more than 128 slices.
		- Your own slicing presets go in the Defaults folder of the User Library.
		- **Preserve warped timing** keeps timing changes from warping; with it off, slices sound like the raw audio.
	- The result:
		- a new MIDI track with a clip holding one note per slice, in a rising chromatic sequence;
		- a [[Ableton/Instrument/Drum Rack]] on that track with one chain per slice, each a [[Ableton/Instrument/Simpler]] loaded with its slice;
		- the Drum Rack's [[Ableton/Macro]] controls mapped to envelope, loop and crossfade settings across every Simpler, as set by the slicing preset.
	- {{embed [[Ableton/Live/UG/13 Audio to MIDI/01 Slice to New MIDI Track/01 Resequencing Slices]]}}
	- {{embed [[Ableton/Live/UG/13 Audio to MIDI/01 Slice to New MIDI Track/02 Using Effects on Slices]]}}
