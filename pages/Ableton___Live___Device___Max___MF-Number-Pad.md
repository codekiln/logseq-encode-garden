logseq-entity:: [[Logseq/Entity/Ableton/Device/Max]]

- # MF Number Pad
	- Max MIDI Effect that turns a slot number typed on a Launchpad into the bank select and Program Change that load that preset on the [[Microfreak]].
	- ## Used by
		- [[Launchpad/Custom/3-MF-Number-Pad]], whose twelve pads send the digits, Clear and Enter.
	- ## Set up in Live
		- 1. On a MIDI track, such as `LPP CM2 to MF`, set MIDI From to `Launchpad Pro MK3 (LPProMK3 MIDI)` and `Ch. 16`, Monitor to `In`, and MIDI To to `Arturia MicroFreak (unknown mididevice)` and `Ch. 1`.
		- 2. Drag MF Number Pad from the browser's User Library, under Presets › MIDI Effects › Max MIDI Effect, onto that track.
	- ## Display
		- **Slot:** the digits typed so far, or `-` when nothing is typed. Enter and Clear empty it.
		- **Sent:** the last slot sent to the MicroFreak.
	- ## How it works
	  collapsed:: true
		- Each digit pressed (notes 60 to 69) is added to the end of the slot number, up to three digits. A fourth digit is ignored. 0 1 6 and 1 6 both mean slot 16.
		- Clear (note 70) empties the number.
		- Enter (note 71) with a number from 1 to 512 sends CC 0 = `(N − 1) // 128`, then Program Change `(N − 1) % 128`, on MIDI channel 1, and empties the number. With nothing typed, 0, or a number above 512, Enter only empties it.
		- Note-on, note-off and poly aftertouch never leave the device, so pad presses don't play the MicroFreak. All other MIDI passes through unchanged.
		- The device reads notes 60 to 71 on any channel; the track's MIDI From does the channel filtering.
		- The logic is JavaScript in a `v8.codebox` between `midiin` and `midiout`, which needs Max 9. Live 12.4 bundles Max 9.1.
	- ## Files
		- [[Launchpad/Idea/Pick-MicroFreak-Presets-through-Live/Asset/Device/MF-Number-Pad/amxd]], the device.
		- [[Launchpad/Idea/Pick-MicroFreak-Presets-through-Live/Asset/Device/MF-Number-Pad/maxpat]], its patcher as JSON.
		- Installed copy: `~/Music/Ableton/User Library/Presets/MIDI Effects/Max MIDI Effect/MF Number Pad.amxd`.
	- ## History
		- [[2026-11-26 Thu]] Built for [[Launchpad/Idea/Pick-MicroFreak-Presets-through-Live]].
		- [[2026-11-27 Fri]] First test: 2 5 9 Enter loaded [[Microfreak/Preset/259 Infini Pad]] ([[GitP/A/Log/26/11/27-Fri]]).
