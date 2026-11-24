date-created:: [[2026-11-22 Sun]]
see-also:: [[GitP/A/Template/Pattern A and B]], [[Launchpad/UI/Mode/5-Sequencer/Track]]

- # LPP Seq
	- A [[GitP/A]] setup for [[Ableton/Live]] 12 in which the four [[Launchpad/UI/Mode/5-Sequencer/Track]]s each play the [[Microfreak]] through their own MIDI track, and each MicroFreak sound is caught as an audio loop beside it. [[Person/codekiln]] built it with [[Ableton/Live/ProducerPal]] on [[2026-11-22 Sun]] and saved it in Live's Templates folder as `GitP-LPP-Seq`.
	- [Live 12 template Set](../assets/GitP___A___Template___LPP%20Seq.als)
	- ## Tracks
		- Four MIDI and audio pairs, `mf1-MIDI`/`mf1` through `mf4-MIDI`/`mf4`, colored after the sequencer tracks. Each MIDI track takes one Launchpad channel, 1 to 4, and sends it to the MicroFreak on channel 1. Each audio track records the MicroFreak from external input 3 through a Glue Compressor and a Compressor, and outputs to Main.
		- A `buffer` MIDI track with no input or output holds spare clips.
		- Four recording tracks, `mf1-rec` to `mf4-rec`, take the post-mixer output of the matching audio track and are armed for Arrangement recording. Recording them captures the whole improvisation, including its volume, pan and send moves.
		- A `utility` group holds `LPP to MF`, `MF to LPP`, which records the MicroFreak's own MIDI output, and a SonoBus bridge.
		- A `Producer Pal` MIDI track holds the Producer Pal device that lets Claude read and change the Set.
		- Returns A-Reverb and B-Delay. Twelve scenes. The tempo is 58.39 BPM.
	- ## Making the episode mix
		- In [[GitP/A/Session/26/11/23-Mon]] the episode was mixed by soloing the four recording tracks together, because the template routes them to no output.
		- TODO Route the recording tracks to Main and leave them muted, so a mix only needs them unmuted.
	- ## Episodes
		- [[GitP/A/Session/26/11/22-Sun]]
		- [[GitP/A/Session/26/11/23-Mon]]