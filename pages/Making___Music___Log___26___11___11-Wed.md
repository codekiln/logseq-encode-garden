# [[2026-11-11 Wed]]
	- This morning I've been doing a bit of knowledge gardening around the Launchpad while trying to figure out more about [[Launchpad/UG/09 Sequencer/12 Projects]]; I'm trying to get better at using Launchpad Projects.
	- ## Planning the next [[Ghost in the Patch]] performance
		- Given my experience of performing classical piano, I'm tempted to draw on that practice-room identity prepare a synth performance from memory. It's thrilling to live on that edge without a score, a metronome, or other scaffolding. Part of me wants to give the audience a touch of that performative liveness.
		- Earlier this week I wanted to find the full expression of the Noise Engineering bass oscillator on the [[Microfreak]] ([[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]), but that goal now feels a bit too programmatic or artificial as a goal. What matters more is making music is fun to listen to. I can get wrapped up in concepts of musical structure rather than in making something that hits a nerve inside.
		- There's a tension between a prepared performance and improvisation. I associate [[Synth/Aesthetic/Coast/West]] with randomness and starting from a blank patch, and [[Synth/Aesthetic/Coast/East]] with presets, notes, and working things out in advance. I think of Wendy Carlos in connection with East Coast synthesis, though that is reductive and she was not working with presets.
		- A classical performance can feel like a magic trick: the hours spent in the practice room are condensed into the time of the recital. I could prepare the five-minute ceremony in that spirit.
		- My history with classical music has a strong pull. Preparing a synthesizer performance the way I used to prepare piano could close off an opportunity to investigate and stretch as an improvising musician. I would love to try that prepared approach sometime, but for this ceremony I think it may be more creatively fruitful to live on the edge and include more improvisation.
		- How much preparation and assistance should I allow? A preset feels acceptable, but I am less certain about a preset containing an entire through-composed sequencer part. A minimal backing track could be a useful creative constraint to improvise over. Deciding where to draw that line is a central question for the performance.
		- I am also interested in [[Music/Performance/Legibility]]: whether the audience can see how my actions shape the sounds they hear. Traditional playing techniques on synthesizers may help make that connection visible.
		- Saturday’s performance will center on [[Microfreak/Preset/259 Infini Pad]]. I am still deciding whether to include [[Ableton/Live/Instrument/Drum/Forevertron]], a custom drum rack made from samples of the sculpture garden in western Wisconsin.
		- ### Goals for today
			- Lock in my performance setup by the end of the day and leave it unchanged until Saturday.
			- Record two five-minute practice sessions with the setup.
			- Put out an episode with several recordings from today. It might be interesting to alternate performances with discussion, like a performance class.
			- Revisit sections of recent podcast episodes made with [[Microfreak/Preset/259 Infini Pad]]. Identify the key musical zones and memorize how to get into at least a few of them. I think of the performance as visiting these zones.
		- ### [[Person/Steve Reich/Essay/68/Music as a Gradual Process]]
			- Earlier this week I read Reich's essay on process music, and I want to read more of his writing: [Writings on Music, 1965–2000](https://read.readwise.io/read/01m701et41bm9ja7hn39zmawvb) is in Reader.
			- ((81155a77-837e-4f46-aaac-25d53beb1cbb))
			- ((84beb931-ac2e-4ec3-9233-a6d7da96814d))
			- [[AI/Response]] from [[Anthropic/Model/Claude/5/5/Opus]]
				- The recollection that process music emerges entirely from the process that created it, with no room for improvisation, holds on improvisation and needs a correction on process.
				- Improvisation: Reich's sentence is "One can't improvise in a musical process—the concepts are mutually exclusive." The phrase "no room for improvisation" is Christensen's paraphrase, quoted in Erik Schoster's paper in Reader.
				- Process: Reich rules out the process that created the piece. He means pieces that are themselves processes, audible while the music sounds. He sets this against Cage, whose I Ching procedures can't be heard in the result.
				- Reich also leaves room for things nobody intended: he lists "slight irregularities in performance" among the "psychoacoustic by-products of the intended process."
	- ## Drum Rack builder
		- I want a local web tool for building [[Ableton/Instrument/Drum Rack]]s from samples. Ableton's Drum Rack interface makes it difficult for me to browse, compare, and curate sounds.
		- From the garden root, `mise run ableton:drumrack:builder:up` would open a sample browser for searching, auditioning, excluding, and organizing recordings, including samples used in existing racks. I want to create a rack or duplicate one as a starting point.
		- Each pad could have a named shortlist of candidates, with pairwise comparisons or a sports-bracket format to choose among them. Analysis of duration, pitch, and loudness could help cluster and sort sounds; a local SQLite cache could hold the results.
		- I would like to audition rack arrangements with my Launchpad Pro MK3 over MIDI. The tool should have sensible configuration defaults and keep personal paths in local, untracked data. [Drum Rack builder issue](https://github.com/codekiln/logseq-encode-garden/issues/377)
	- ## Improvisation practice log — Forevertron / Forever Veteran
		- **Date:** November 11, 2026 (Veterans Day)
		- **Purpose:** Rehearsal for this weekend's performance
		- **Recording:** None — improvisation was unrecorded
		- **Tempo:** 60 BPM
		- **Equipment:** Ableton Live, [[Novation/Launchpad/Pro/Mk3]], [[Microfreak]], Zoom H5
		- ### 1. Overview and Reflections
			- Today's improvisation was somewhat chaotic but produced several promising musical ideas. I wish I had recorded it.
			- The most successful discovery was the contrast between a piano-based sample set called *Forever Veteran* and the MicroFreak's [[Microfreak/Preset/259 Infini Pad]] preset. The combination was particularly effective, especially when using the arpeggiator.
			- I also made progress simplifying my Ableton Live routing, organizing the crossfader, and developing an approach to timekeeping during the five-minute performance.
		- ### 2. Sound Sources and Samples
			- #### Forevertron Gamelan
				- Used a gamelan instrument I created from recordings made at Forevertron in western Wisconsin: [[Ableton/Live/Instrument/Drum/Forevertron]].
				- Assigned it to **Launchpad sequencer track 4**.
				- Saved many of the sequencer settings in the Launchpad's project grid at **column 2, row 4**.
				- Experimented with the Launchpad's mutation functionality.
				- **Finding:** Mutation applied to the full Forevertron collection produces too much chaos. The collection needs to be curated to make its variations more musically useful.
			- #### Forever Veteran
				- *Forever Veteran* is a sample set created on Veterans Day, incorporating a piano improvisation and samples recorded from a billiards table.
				- Implemented as an Ableton Drum Rack.
				- Includes piano and billiard sounds.
				- Approximately six slots remain available in its 16-pad layout.
				- Could become the central sample instrument by incorporating a carefully selected subset of the Forevertron sounds.
				- Additional cue-ball recordings made with the Zoom H5 are available for inclusion.
			- #### MicroFreak — 259 Infinipad
				- Preset: [[Microfreak/Preset/259 Infini Pad]]
				- Played in octave 0.
				- Explored the same melodic material used in *Forever Veteran*.
				- Made effective use of the MicroFreak's arpeggiator.
				- **Finding:** The contrast between the acoustic piano samples and the synthetic Infinipad sound was especially successful and should be preserved in the performance.
		- ### 3. Melodic and Harmonic Material
			- The principal melodic notes were:
				- **D – F – G – C**
			- The melodic contours also reached downward toward:
				- **A and A♭**
			- An especially interesting source of tension was the alternation between A natural and A-flat.
			- This pitch collection worked well both in the piano material and when transferred to the MicroFreak's lower register.
			- **Musical idea to preserve:** Use the shared pitch vocabulary to establish continuity between the sampled piano and the Infinipad, while exploiting their contrasting timbres.
		- ### 4. Ableton Live Configuration
			- #### Crossfader Organization
				- Reorganized the Live Set around the A and B sides of the crossfader ([[Ableton/Live/UG/18 Mixing/05 Using Live's Crossfader]]).
				- | Track      | Crossfader assignment |
				  |------------|-----------------------|
				  | 1          | A                     |
				  | 2          | A                     |
				  | 3A (audio) | A                     |
				  | 3B         | B                     |
				  | 4          | B                     |
				- Track 3 now has two parts, 3A and 3B, allowing related material to participate in opposite sides of the crossfader.
				- This provides a way to transition between contrasting musical layers using the crossfader.
			- #### Routing Simplification
				- Removed intermediate mixing buses from the Ableton Live Set.
				- I couldn't remember why they had been introduced or what functionality they provided, so I eliminated them to simplify the signal path and reduce unnecessary complexity during performance.
		- ### 5. Five-Minute Performance Timing
			- **Tempo:** 60 BPM
			- **Target duration:** 5 minutes
			- Developing an audible alarm system to keep track of the performance's elapsed time without needing to watch a clock.
			- The plan is to trigger a distinctive alarm sound:
				- Every 30 seconds during the first minute.
				- Every 60 seconds during the middle three minutes.
				- Every 30 seconds during the final minute.
			- #### Proposed Cue Schedule
				- | Elapsed time | Function             |
				  |--------------|----------------------|
				  | 0:00         | Performance begins   |
				  | 0:30         | Opening cue          |
				  | 1:00         | End of first minute  |
				  | 2:00         | Middle section       |
				  | 3:00         | Middle section       |
				  | 4:00         | Final minute begins  |
				  | 4:30         | 30 seconds remaining |
				  | 5:00         | End of performance   |
			- The alarm sound has not yet been chosen. Possibilities include an existing fire/smoke alarm recording or a distinctive sound synthesized on the MicroFreak.
			- The cue needs to be immediately recognizable without becoming overly disruptive to the music.
		- ### 6. Ideas for the Next Iteration
			- #### Consolidate the Drum Rack
				- Rather than keeping all the Forevertron recordings together in a separate, highly variable collection, select a small number of the most useful samples and integrate them into *Forever Veteran*.
				- Potential uses for the approximately six available Drum Rack slots:
					- A few carefully chosen Forevertron gamelan sounds.
					- One smoke/fire alarm sound for timing cues.
					- One or two additional billiard cue-ball recordings from the Zoom H5.
				- This should create a more coherent, playable palette of sounds while preserving some of the improvisational unpredictability.
			- #### Control Mutation
				- Avoid applying extensive mutation to the full Forevertron collection.
				- Experiment instead with mutation on a smaller curated subset of sounds, where the range of possible results remains musically meaningful.
			- #### Develop the Alarm Sound
				- Find or synthesize a recognizable timing cue, potentially with the MicroFreak.
				- Test whether the sound can be heard clearly in the musical texture and whether it interferes with the performance.
			- #### Preserve the Piano–MicroFreak Contrast
				- Recreate the particularly successful interaction between the Forever Veteran piano samples and MicroFreak preset 259 Infinipad.
				- Explore:
					- The shared D–F–G–C melodic vocabulary.
					- The tension between A and A-flat.
					- The MicroFreak's low octave.
					- Arpeggiated figures against the piano material.
		- ### 7. Next Practice Checklist
			- Back up the Launchpad project saved at column 2, row 4.
			- Confirm the Ableton crossfader assignments and track routing.
			- Review the remaining six slots in Forever Veteran.
			- Select the best Forevertron gamelan samples for the Drum Rack.
			- Review additional Zoom H5 billiard recordings.
			- Choose or create an alarm cue.
			- Configure and test the five-minute timing sequence.
			- Revisit MicroFreak preset 259 Infinipad in octave 0.
			- Practice the D–F–G–C material with A/A♭ tension.
			- Experiment with more constrained sequencer mutation.
			- **Record the next improvisation**, even if only as a stereo reference recording.
		- ### 8. Principal Takeaways
			- **The piano/Infinipad combination is worth developing.** It provided one of the most convincing moments of the improvisation.
			- **Constrained randomness is preferable to unrestricted mutation.** The Forevertron material benefits from selection and curation.
			- **Simpler routing is better for live performance.** Removing unnecessary buses and organizing around the crossfader should make the set easier to manage.
			- **Timekeeping can become part of the musical structure.** The alarm cues could help articulate the five-minute form rather than serving merely as reminders.
			- **Recording rehearsals is important.** Even chaotic improvisations can reveal material that is difficult to reconstruct afterward.
