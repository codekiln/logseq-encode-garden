prev:: [[GitP/A/Log/26/11/23-Mon]]
next:: [[GitP/A/Log/26/11/26-Thu]]

- [[2026-11-25 Wed]]
	- Still working on a new version of Monday's ceremony, [[GitP/A/Session/26/11/23-Mon]].
	- Meanwhile, re-evaluating [[GitP/A/Template/LPP-Seq]], the template that ceremony started from.
		- Notes from [[GitP/Acolyte]], read from the open Monday Set and the template file
			- #### Which tracks make the mix
				- Monday's Set now has the recording tracks on Main and muted, as the TODO on [[GitP/A/Template/LPP-Seq]] asks. The template file still sends them to No Output.
				- Unmuting the recording tracks alone would double the music. While loops were launched, Live wrote each launch into the Arrangement on mf1 to mf3, so those tracks replay the same loops the recording tracks printed. A mix from the recording tracks also needs mf1 to mf4 muted. Soloing the recording tracks did both in one step.
				- With the recording tracks muted, the Arrangement plays mf1 to mf3 with their own volume and pan automation. That includes the loops they launched and the MicroFreak they recorded while armed.
				- The second mix is made from mf1 to mf3, with the recording tracks muted.
			- #### Are the recording tracks needed?
				- [[AI/Response]] Earlier assessment, superseded by the test below
				  collapsed:: true
					- An armed track records into the Arrangement during Arrangement Record, per [[Ableton/Live/UG/19 Recording New Clips/03 Recording/01 Recording Into the Arrangement]]. With Auto monitoring, an armed track lets its input through while it plays no clip, per [[Ableton/Live/UG/17 Routing and IO/01 Monitoring]]. The manual does not establish what the Arrangement contains while a new Session clip is still being recorded; see the question below.
					- Monday's Set contains these recordings of the MicroFreak on the mf tracks at times in the second mix:
						- mf1, 00:00 to 00:08, before the opening loop.
						- mf3, 01:17 to 01:40 and 01:44 to 01:55, before Laity's loop.
						- mf2, 05:12 to 05:35, GrowLing's sub and the pattern from the keys.
						- mf3, 06:41 to 07:18, the growl.
						- mf1, 07:55 to 08:13, a take that never became a Session clip. This is the case the recording tracks were built for: no loop playing, the track armed, the MicroFreak played. mf1 caught it.
					- The recording tracks repeat that sound, after volume and pan and without the sends. Each wrote one file for the whole pass, 12 minutes and 36 seconds, silence included. mf4 never played in the Arrangement, so mf4-rec is silent from start to end. A 24-bit stereo file at 48 kHz that long takes about 218 MB, so four of them take nearly 900 MB a session.
					- The recording tracks can catch sound the mf tracks miss in these cases:
						- An mf track set to monitor In passes its input without being armed, so you hear it and nothing records it. The template sets all four to Auto.
						- An edit removes a clip from an mf track. Take lanes keep a copy of every recording, because Live puts each take in a take lane and copies the latest one to the main lane, per [[Ableton/Live/UG/21 Comping/03 Recording Takes]].
					- One spot to check: in the Set now, mf2's main lane has no clip from 00:17 to 00:33, where GivemeSub's first take was recorded. mf2's take lane still holds that recording, and mf2-rec printed it too. Is GivemeSub's first take in the second mix?
					- A safety copy could come from one track instead of four. An audio track with its input set to Resampling records the Main output, returns included, per [[Ableton/Live/UG/17 Routing and IO/04 Resampling]].
					- Keep mf1-rec to mf4-rec in the template until the Session recording example below is tested. A single Resampling track would capture a stereo mix rather than separate tracks, which changes the options for mixing afterward.
				- [[My Note]] ok i've verified this and I'm satisfied that the recording tracks are not really needed.
				  id:: 6b0770c8-138f-410c-836a-00c053a152f5
				  collapsed:: true
					- DONE [[Ghost Gardener]] please repond to this hypothetical example
						- let's say from I have track `mf1` armed for recording in auto mode. I'm in [[Ableton/Live/Mode/Session]] and I hit the [[Ableton/Live/UI/Control-Bar/Button/Arrangement-Record]] and from 0s-15s I record audio from the microfreak into [[Ableton/Arrangement View]]. Then, in empty clip slot 1, I hit the session record button on that clip to begin recording in, which blinks from 15s-18s until the next global quantize moment. Then I'm recording into the clip from 18s-30s. Then I hit [[Ableton/Live/UI/Control-Bar/Button/Stop]]. What are the contents of the `mf1` track in [[Ableton/Arrangement View]] from 15s-30s?
						- [[AI/Response]] The manual supports an expectation for 15s–18s: the Arrangement recording continues while the Session slot waits for its quantized start. At 18s, the slot starts recording the MicroFreak into a new Session clip. I cannot establish from the manual whether Live also places that still-recording Session clip in the Arrangement from 18s–30s. The earlier claim that everything heard on an armed Auto-monitored track necessarily lands in its Arrangement is not established.
							- Ableton says that Arrangement Record creates clips on armed tracks, that a slot's Clip Record button starts a Session recording at the launch-quantized time, and that Arrangement Record logs Session clip launches. The manual does not state how an in-progress Session recording appears in the Arrangement. [[Ableton/Live/UG/19 Recording New Clips/03 Recording/01 Recording Into the Arrangement]] · [[Ableton/Live/UG/19 Recording New Clips/03 Recording/02 Recording Into Session Slots]] · [[Ableton/Live/UG/07 Session View/05 Recording Sessions into the Arrangement]]
							- To settle 18s–30s, test in a fresh Live 12 Set with a continuous audible input: reproduce the sequence, stop at 30s, and inspect and play the Arrangement at the transition. Compare it with the Session clip and the recorded audio files. Monday's `mf2` gap is a reason to test, but the saved Set alone does not establish which actions produced the gap.
						- ### [[My Notes]] ok, verified
						  collapsed:: true
							- This ended up working, much to my surprise. I was able to create a recording with four segments:
								- 0-A - recording in arrangement view
								- A-B - in session mode, initiating a clip, blinking
								- B-C - in session mode, recording a clip
								- C-D - playing the recorded clip
								- there is content from 0-D just as I heard it.
						- [[AI/Response]] Your test resolves the Session recording case above: the Arrangement contained the input while the clip waited and recorded, then the clip playback. The earlier recommendation to keep the recording tracks pending this test is superseded. Your test supports removing them for this workflow.
				- [[AI/Response]] [[2026-11-26 Thu]] Removed mf1-rec to mf4-rec from the template, both in Live's Templates folder and in the garden's copy on [[GitP/A/Template/LPP-Seq]]. Nothing else in the Set referred to them. Sets made from the template before today, Monday's included, still have them.
			- #### What the recording tracks capture
			  collapsed:: true
				- The recording tracks tap mf1 to mf4 at Post Mixer, which [[Ableton/Live/UG/17 Routing and IO/05 Internal Routings/01 Internal Routing Points]] describes as the track's output after volume and pan. Sends leave a track on their way to the returns, so the reverb and delay fed from mf1 to mf4 never reach the recording tracks.
				- On Monday, mf2 and mf3 carry reverb send automation. A mix of the recording tracks leaves it out. mf2-rec and mf3-rec carry send automation of their own, and that plays back with the mix.
				- The template page says recording these tracks captures the send moves. That holds only for sends turned on the recording tracks themselves.
				- The Post Mixer signal also carries each mf track's Glue Compressor. Each recording track then runs its own Glue Compressor with the same "Mastering - Make It Loud" preset, so a mix of the recording tracks is compressed twice. The Compressor after it is switched off on every audio track.
				- Should the reverb and delay be printed with the rest? A Reverb and a Delay placed on each mf track as devices would land in the Post Mixer signal.
				- Should the recording tracks keep their Glue Compressor?
			- #### Sunday's takes
			  collapsed:: true
				- [[AI Notes]]
					- Most tracks in the template carry hidden take lanes holding Sunday's recordings, so every new Set starts with them. Monday's Set keeps them beneath Monday's takes. [[Ableton/Live/UG/21 Comping/01 Take Lanes]]
					- mf2, mf3 and the recording tracks hold clips named after mf1, such as "mf1 2" and "mf1 5-1", which suggests the take lanes came along when mf1 was duplicated to make those tracks.
					- Clear the take lanes before the template is saved again?
				- [[My/Response]]
					- Yes, we should clear those take lanes! That's quite wasteful! We should really have some kind of automated way to "garbage collect" any unreferenced audio material in an ableton live set template
						- [[AI/Response]] Live has a built-in cleanup workflow. In a copy of the template, right-click each affected track header and choose **Delete All Take Lanes** after checking that its takes are unwanted. Save the Set, then use **File → Manage Files → Manage Project → Unused Files → Show** to review the files Live finds. Take lanes still reference their audio until removed, so finding unused files alone will not clear those takes. [Ableton: Managing Audio Clips and Samples](https://help.ableton.com/hc/en-us/articles/5068208334226-Managing-Audio-Clips-and-Samples) · [[Ableton/Live/UG/21 Comping/02 Inserting and Managing Take Lanes]] · [[Ableton/Live/UG/05 Managing Files and Sets/08 Finding Unused Files]]
							- Live considers references within the current Project; another Project can still use a file listed as unused. Collect external files into the Projects that need them before deleting, and review the list. The saved template’s location and Project ownership need checking before applying this to it. Live finds candidates, and deletion is a separate manual step. [Ableton: Finding Unused Files](https://www.ableton.com/en/live-manual/12/managing-files-and-sets/#finding-unused-files)
			- #### Launchpad faders
				- [[AI Notes]]
					- mf1-MIDI to mf4-MIDI carry volume automation, and some carry pan or send automation too. A MIDI track without an instrument passes no audio, so that automation changes nothing.
					- mf1 to mf4 all drop their volume at the same moment near the end. Both patterns fit a sweep across the Launchpad's eight faders, which cover eight tracks in a row. In this track order, every other fader lands on a MIDI track.
					- Did that automation come from the Launchpad's faders? If so, putting mf1 to mf4 first would give each MicroFreak loop its own fader. The sequencer reaches the MIDI tracks by channel, so their position in the Set doesn't matter to it.
				- [[My Note]]
					- I think this is talking about when I used the [[Launchpad/UG/05 Session Mode/04 Track Controls/04 Volume]] across all the tracks at once. But I'm not sure why AI is interested in this, or what this means: "In this track order, every other fader lands on a MIDI track." I think AI is confused about the difference between [[Launchpad/UI/Mode/1-Session]] and [[Launchpad/UI/Mode/5-Sequencer]]
						- [[AI/Response]] You are describing Session mode’s Volume view. My observation concerned those Live mixer faders, not the Launchpad’s Sequencer mode. The template lists alternating MIDI and audio tracks; if that same order is in the visible Session window, alternating faders control MIDI and audio tracks. The automation on MIDI tracks may simply be a consequence of your sweep. I cannot tell from the saved automation alone which control produced it, and there is no need to reorder tracks unless you want adjacent faders for the audio tracks. [[Launchpad/UG/05 Session Mode/04 Track Controls/04 Volume]] · [[GitP/A/Template/LPP-Seq]]
			- #### Preset changes
				- [[AI Notes]]
					- The MicroFreak plays one preset at a time, and the Set keeps no record of which one sounded when. Monday's chapters were worked out afterward from the log's list of presets and from where each new take begins.
					- A MIDI clip can send a bank and program change when it launches, per [[Ableton/Live/UG/08 Clip View/03 Extended Clip Properties/02 MIDI Clip Bank and Program Change Controls]]. The MicroFreak selects a slot from a bank select and a program change, per [[Microfreak/Sequence/Research]]. A clip per preset on a MIDI track routed to the MicroFreak could call up each sound and leave its launch in the Arrangement as a chapter mark.
					- Worth a test with one of Monday's presets?
				- [[My/Response]]
					- DONE I'd prefer to devise some method using [[Launchpad/Custom]] to send these bank and program change messages, if that's an option. Can you look into that?
						- [[AI/Response]] Yes. A Custom Mode can use CC 0 trigger pads to select a bank and Program Change pads to select presets. Changing banks takes two presses; the documented controls do not establish a single pad that sends both messages. Factory Custom Modes 5 and 6 already send Program Changes. The existing Live routing needs a test, as does whether the messages leave a useful Arrangement record. [[Launchpad/Q/Can-Custom-Mode-select-MicroFreak-presets-by-bank-and-program-change]] has the setup, an example, and a clip-based alternative for named chapter markers.