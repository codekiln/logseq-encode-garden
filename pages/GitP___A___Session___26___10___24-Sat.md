prev:: [[GitP/A/Session/26/10/22-Thu]]
logseq-entity:: [[Logseq/Entity/Podcast/Episode/GitP/A]], [[Logseq/Entity/Podcast/Episode]]
public:: true
created-by:: [[Person/codekiln]]
date-created:: [[2026-10-24 Sat]]

- # The Unstable over USB
	- A Ghost in the Patch session recorded at the library with MicroFreak preset 151 The Unstable, a slow Launchpad sequence and USB-only MIDI: Ableton Live sends the clock, Launchpad pad pressure drives the pad, and nothing needed a MIDI panic.
	- ![Episode recording](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/GitP___A___Session___26___10___24-Sat___Asset___Audio___Full.mp3)
	- ## Recording
		- 17:54 · [[GitP/A/Session/26/10/24-Sat/Asset/Audio/Full/mp3]] · [Download the MP3](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/GitP___A___Session___26___10___24-Sat___Asset___Audio___Full.mp3)
		- Recorded in Ableton Live at 120 BPM. [[Making/Music/Log/26/10/24-Sat]] has the session notes.
		- Select a chapter timestamp to play from that point.
	- ## Setup
		- Recorded at the library, with USB cables only for MIDI. A single USB hub with all the other cables plugged into it worked well.
		- The MicroFreak takes its clock from USB only. The Launchpad receives clock but does not send it. Ableton Live's MIDI output settings send clock to both devices and take no clock input from them. [[Launchpad/UG/10 Setup/05 MIDI Settings]] · [[Microfreak/UG/14 Config/02 MIDI Control Center/01 Device Tab]]
		- Arrangement Record was armed from [[Launchpad/Custom/Mode/1 Arrangement]], used here for the first time.
		- Still to try: separate the headphone output from the audio sent to the [[Zoom H5]], so the cue mix goes to the headphones and the rendered mix to the recorder. [[Zoom H5/Q/How can I record the line out on a MacBook or iPhone while monitoring on the headphone jack?]]
	- ## Preset
		- [[Microfreak/Preset/151 The Unstable]] — Pad, V.Analog, paraphonic. The saved slot matched the factory payload after the session, so the edits heard here were not saved.
		- [Download the slot 151 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/GitP___A___Session___26___10___24-Sat___Asset___Preset___The-Unstable-Live-2026-10-24.bin)
	- ## MIDI
		- [Download the session MIDI](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/GitP___A___Session___26___10___24-Sat___Asset___MIDI___Session.mid) · [[GitP/A/Session/26/10/24-Sat/Asset/MIDI/Session/mid]]
		- Times below follow the recording. Control names come from [[Microfreak/UG/21 Appendix D - CC Values]]. With [V.Analog]([[Microfreak/UI/Oscillator/Knob/Type/VAnalog]]), the panel's [Wave knob]([[Microfreak/UI/Oscillator/Knob/Wave]]) (CC 10) sets [Detune]([[Microfreak/UI/Oscillator/Knob/Type/VAnalog/Detune]]), the [Timbre knob]([[Microfreak/UI/Oscillator/Knob/Timbre]]) (CC 12) sets [Shape]([[Microfreak/UI/Oscillator/Knob/Type/VAnalog/Shape]]), and the [Shape knob]([[Microfreak/UI/Oscillator/Knob/Shape]]) (CC 13) sets [Wave]([[Microfreak/UI/Oscillator/Knob/Type/VAnalog/Wave]]). [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
		  id:: 6add3dae-8dc8-4156-a5ea-23f7290d9173
	- ## Voices
		- **codekiln** is transcribed from the commentary microphone. Only codekiln's commentary is transcribed. Most of the recording is music without commentary.
		- The transcript is an automatic draft; [unclear] marks a word that could not be made out.
	- ## Chapters
		- ### 00:00 Arrangement Record from a custom mode
			- A short remark from the end of the session opens the episode: the first use of a Launchpad custom mode to arm Arrangement Record.
			- [[Launchpad/Custom/Mode/1 Arrangement]]
			- Transcript
				- **codekiln** · 00:00:02 — All right, that was cool. Hey, by the way, this is also the first time when I used my [[Launchpad/UG/08 Custom Modes]] to be able to enable the recording. Unfortunately I think it's inverted from what I want. I think it's a bright green when I'm recording and then if I…
			- [[My Notes]]
				- This part was actually from the end of the recording session. At the end, I stopped the recording, then used the custom mode MIDI toggle button mapped to the [[Ableton/Live/Mode/Arrangement]] record button
					- DONE [[Ghost Gardener]] please create a namespace hierarchy under [[Ableton/Live/Mode/Arrangement]] which will map out all the parts of arrangement mode and give all the buttons and settings dedicated pages that autocomplete in Logseq
					  id:: 6addc678-7052-4e91-a8af-b4e3f6d99542
		- ### 00:22 The Unstable over a slow sequence
			- Launchpad sequencer track 1, set to its slowest rate, plays The Unstable. The Wave and Shape knobs sweep between triangle and saw and between narrow pulse and square, resonance rises a little at 01:27, and cycling envelope amount goes up to about 95 at 01:36. From 02:00, cycling envelope rise, fall and hold change.
			- [[Launchpad/UG/09 Sequencer/05 Pattern Settings/01 Sync Rate]] · [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]] · [[Microfreak/Preset/151 The Unstable]]
			- #### [[My Notes]]
				- While it wasn't intentional, I like how it immediately jumps to this moody section. My modifications
		- ### 03:00 Oscillator type and the main envelope
			- Oscillator type (CC 9) changes several times between 03:04 and 03:21 and ends where it started. At 04:14, sustain (CC 29) comes down from near maximum while attack (CC 105) and decay (CC 106) change, so the swelling pad gets shorter.
			- [[Microfreak/UG/06 Dig Osc/03 Types]] · [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- ### 05:00 Cycling envelope sweeps
			- Cycling envelope rise (CC 102) and fall (CC 103) move through most of these three minutes, which have the most notes in the session. Because the cycling envelope drives resonance in this preset, those sweeps change how the resonance pulses. The section from 05:38 to 08:27 comes from a later take placed into the arrangement.
			- [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope/02 Changing Shapes]]
			- ### [[My Notes]] 07:40 detunes - [[Microfreak/UI/Oscillator/Knob/Type/VAnalog/Detune]]
				- Musically effective. Dreamy and machine-like.
		- ### 08:00 Opening the filter
			- Cutoff (CC 23) rises from 12 at 08:03, with Wave, Shape and attack changes around it. From 09:00, cycling envelope amount (CC 24), hold, rise and fall change again.
			- [[Microfreak/UG/07 Filter/01 Modifying Sound/04 Cutoff Frequency]]
		- ### 10:00 Detune and Launchpad pressure
			- Detune (the Wave knob, CC 10) changes from 10:00 and reaches 49 by 12:00. Launchpad pad pressure, recorded as per-note pressure, arrives from 11:00 and carries through to the end. Oscillator type changes again between 13:14 and 13:19 and returns to its starting value.
			- [[Launchpad/UG/10 Setup/04 Aftertouch Settings]] · [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ### 14:15 USB clock, printing clips and pressure
			- The live playing stops around 14:30, and looped Session clips carry on quietly while codekiln talks through the session: unsaved preset edits, the USB-only clock setup, wanting to print a sequencer pattern to a Session clip and play it back to the MicroFreak, and how much Launchpad pressure added to the preset.
			- [[Launchpad/UG/09 Sequencer/11 Print to Clip]] · [[Launchpad/UG/10 Setup/05 MIDI Settings]] · [[Launchpad/UG/10 Setup/04 Aftertouch Settings]]
			- Transcript
			  collapsed:: true
				- **codekiln** · 00:14:15 — Okay, that was interesting.
				- **codekiln** · 00:14:31 — I recorded a few times into MIDI channels, even though that doesn't really work.
				- **codekiln** · 00:14:35 — I'm tempted to save the preset here at the end. I had a few modifications to it, but, you know, not much. I'm actually not quite seeing the modifications that I made.
				- **codekiln** · 00:14:54 — Oh, shoot. How do I get back to the preset I was on once I browse away? That's kind of weird. If I press panel, here, maybe if I press utility. If I press panel.
				- **codekiln** · 00:15:22 — Well, now I'm not hearing anything. Well, I think I said what preset I was on earlier, so that's fine.
				- **codekiln** · 00:15:34 — So I was using sequencer there in track 1, I tied together a few of them. I did the sequencer on the slowest setting.
				- **codekiln** · 00:15:44 — I'm using all USB, no MIDI cables this time. I think I finally managed to do an entire session [unclear] a MIDI panic, because I made it so the MicroFreak only loaded its clock from USB, and I only set Novation to receive. I didn't set it to send.
				- **codekiln** · 00:16:05 — And I also appropriately configured the output settings of the Ableton Live MIDI settings so that it is outputting the clock to both the MicroFreak and the Launchpad, but it's not receiving input from them. That seems to work pretty well.
				- **codekiln** · 00:16:30 — I think my main weirdness is that I would like to be able to print from the sequencer to a MIDI track in session mode and then play that to the MicroFreak, but then potentially also have that being recorded to the global MIDI out for the MicroFreak. If that's being played, I suppose the easiest way to do that might be to try to have it so that that is output back to the MicroFreak, but I'm kind of a little bit concerned about doubling. I don't know if MIDI dedupes. I don't think it does. I think it's kind of a dumb protocol. I don't think it sends along the ID of the device that created the note.
				- **codekiln** · 00:17:28 — Some of the things I was a little bit surprised about here is how the aftertouch had so many levels on the Novation that I was able to get some extra bits of juice out of the preset.