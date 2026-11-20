logseq-entity:: [[Logseq/Entity/Term]]

- # MIDI Aftertouch
	- Pressure on a key or pad after it has gone all the way down, sent as one of two [[MIDI/Message]] types.
	- **Polyphonic Key Pressure** (A0h–AFh) sends a note number and a pressure value, one stream for each held key.
	- **Channel Pressure** (D0h–DFh) sends one pressure value for the whole channel: the greatest pressure among the held keys.
	- The Launchpad Pro MK3 can send either. Its guide recommends Channel Pressure with Ableton Live ([[Launchpad/UG/10 Setup/04 Aftertouch Settings]]).
	- MPE carries per-note pressure as Channel Pressure by giving each note its own channel.
