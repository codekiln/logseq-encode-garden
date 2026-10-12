logseq-entity:: [[Logseq/Entity/Podcast/Episode]]
created-by:: [[Person/codekiln]]
date-created:: [[2026-10-11 Sun]]
- # GitP.26.10.11
	- A slow MicroFreak improvisation that moves from harmonic tones into a blurred, pitch-bent drone and closes with a virtual analog sound. Recorded in Ableton Live without spoken commentary.
	- ![GitP.26.10.11 — episode recording](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/GitP___A___Session___26___10___11-Sun___Asset___Synth___Full.mp3)
	- ## Session notes
		- [[Making/Music/Log/26/10/11-Sun]] recalls MicroFreak presets 401 and 402, sequencer patterns A and B, short five-step sequences, paraphonic playing, and a change from the [[Microfreak/UG/06 Dig Osc/03 Types/04 Harmo]] to [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]. The log does not pin either preset to an exact passage.
		- The [[Launchpad/UG/05 Session Mode]] controlled Live's pan, send, volume, record arm, stop clip, click, device, tap tempo, and fixed-length recording. The [[Launchpad/UG/09 Sequencer]] was not used; the sequences came from the [[Microfreak/UG/13 Sequencer]].
		- ### 00:00–03:30 · Harmonic opening
			- Sparse notes give way to sweeps of filter cutoff (CC 23, reaching 91), resonance (CC 83, reaching 74), filter amount (CC 26, reaching 84), and oscillator timbre, wave, and shape (CC 12, 10, 13); see [[Microfreak/UG/21 Appendix D - CC Values]]. The note count thins after 02:00 while those oscillator controls keep moving. The session log identifies the opening sound as Harmo, though the MIDI does not encode the loaded preset.
		- ### 03:30–10:00 · Sequences and texture
			- Cycling envelope rise (CC 102) appears around 03:33. LFO sync rate (CC 94) changes around 04:33; the log recalls changing the LFO shape from sine to saw, but that waveform choice is not present in the CC capture. Spice (CC 2) begins around 06:24 and moves through values up to 82 during a denser run of notes. Around 09:34, a brief group of sequencer sync-rate changes (CC 92, up to 102) accompanies the transition into a quieter passage. See [[Microfreak/UG/13 Sequencer/01 Use/01 Select & Play]] for switching patterns A and B.
		- ### 10:00–17:30 · Pitch motion
			- Pitch-bend messages return around 10:00 and continue through the middle of the recording. Cycling envelope amount (CC 24) enters around 12:10 and reaches 127. The log recalls routing cycling envelope and keyboard pressure to pitch through the [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]; the MIDI records the bend and envelope controls but cannot establish that internal routing. Oscillator type (CC 9) changes around 14:49, while the saved sound at that instant is unknown. Around 17:00, cycling envelope fall (CC 103), hold (CC 28), and rise (CC 102) changes join the filter sweeps.
		- ### 18:00–26:53 · Drone and closing gestures
			- Long passages of cutoff and resonance movement, continuing pitch bend, and fewer notes make the middle more droning. From about 22:00, the note activity increases along with Spice, oscillator shape, timbre, and wave changes. Glide (CC 5) appears at 23:44 and rises as high as 31 in the final minutes. A further oscillator-type change (CC 9) occurs near 26:30; the log says the session ended on V.Analog, but the CC value alone does not identify that oscillator model.
		- These times follow the Ableton arrangement at a constant 56.818 BPM. The captured MIDI contains note and controller events from the “mf MIDI ALL” track. [[Microfreak/UG/21 Appendix D - CC Values]] identifies the controls; the [[GitP/A/Session/26/10/11-Sun/Asset/MIDI/Full/mid]] preserves their recorded values for inspection.
	- ## Downloads
		- [Download the full-session MIDI](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/GitP___A___Session___26___10___11-Sun___Asset___MIDI___Full.mid)
	- ## Recording
		- [[Making/Music/Log/26/10/11-Sun]] · [[GitP/A/Session/26/10/11-Sun/Asset/Synth/Full/mp3]] · 26:53.
