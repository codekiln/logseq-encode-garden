date-created:: [[2026-11-22 Sun]]
see-also:: [[GitP/A/Template/Pattern A and B]], [[Launchpad/UI/Mode/5-Sequencer/Track]]

- # LPP Seq
	- A [[GitP/A]] setup for [[Ableton/Live]] 12 in which the four [[Launchpad/UI/Mode/5-Sequencer/Track]]s each play the [[Microfreak]] through their own MIDI track, and each MicroFreak sound is caught as an audio loop beside it. [[Person/codekiln]] built it with [[Ableton/Live/ProducerPal]] on [[2026-11-22 Sun]] and saved it in Live's Templates folder as `GitP-LPP-Seq`.
	- [Live 12 template Set](../assets/.remote/logseq-encode-garden/GitP___A___Template___LPP-Seq___Asset___Set.als)
	- ## Tracks
		- Four MIDI and audio pairs, `mf1-MIDI`/`mf1` through `mf4-MIDI`/`mf4`, colored after the sequencer tracks. Each MIDI track takes one Launchpad channel, 1 to 4, and sends it to the MicroFreak on channel 1. Each audio track records the MicroFreak from external input 3 through a Glue Compressor with the "Mastering - Make It Loud" preset and a switched-off Compressor, and outputs to Main. `mf1-MIDI` and `mf1` start armed.
		- A `buffer` MIDI track with no input or output holds spare clips.
		- There are no separate recording tracks. With Arrangement Record on, Live logs each loop an audio track launches, and an armed audio track records the MicroFreak into the Arrangement while it plays no clip. So mf1 to mf4 keep the whole improvisation, including the playing between loops.
			- Leave their monitoring on Auto. On In, a track passes the MicroFreak even when it isn't armed, and nothing records it.
			- The recording tracks `mf1-rec` to `mf4-rec` were removed on [[2026-11-26 Thu]], after [[GitP/A/Log/26/11/25-Wed]] showed they only repeated mf1 to mf4.
		- A `utility` group holds `LPP to MF`, `MF to LPP`, which records the MicroFreak's own MIDI output, and a SonoBus bridge.
		- A `Producer Pal` MIDI track holds the Producer Pal device that lets Claude read and change the Set.
		- Returns A-Reverb and B-Delay. Twelve scenes. The tempo is 58.39 BPM.
	- ## Making the episode mix
		- Mix from mf1 to mf4. They replay the loops and takes Live wrote into the Arrangement, with their volume, pan and send automation, and the reverb and delay returns are part of the mix.
		- The first mix of [[GitP/A/Session/26/11/23-Mon]] soloed the four recording tracks together. Its second mix was made from mf1 to mf3.
	- ## Episodes
		- [[GitP/A/Session/26/11/22-Sun]]
		- [[GitP/A/Session/26/11/23-Mon]]