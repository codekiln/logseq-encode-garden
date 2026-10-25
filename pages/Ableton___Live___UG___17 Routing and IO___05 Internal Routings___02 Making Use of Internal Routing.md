logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/17 Routing and IO/05 Internal Routings]]
prev:: [[Ableton/Live/UG/17 Routing and IO/05 Internal Routings/01 Internal Routing Points]]

- # [17.5.2 Making Use of Internal Routing](https://www.ableton.com/en/live-manual/12/routing-and-i-o/#making-use-of-internal-routing)
	- ## 17.5.2.1 Post-Effects Recording
		- To record a guitar already processed by a gate or amp model, put the effects on a "Guitar" track with Monitor set to In, and record on other tracks whose input is the Guitar track at Post FX (or Post Mixer to include its level and pan). Set those tracks' Monitor to Off.
		- ![An example setup for post-effects recording](https://ableton-production.imgix.net/live-manual/12/PostFxRecordingRoutingExample.png?auto=&w=320)
	- ## 17.5.2.2 Recording MIDI as Audio
		- When a complex instrument turns one note into something closer to a passage, record its audio: one MIDI track hosts the instrument, and an audio track taking input from it records the result.
	- ## 17.5.2.3 Creating Submixes
		- Route several drum tracks to one submix audio track that goes to Main, so one fader controls the whole kit.
		- ![Submixing the individual drums of a drum kit](https://ableton-production.imgix.net/live-manual/12/DrumSubMixRoutingExample.png?auto=&w=320)
		- A Group Track sets up the same routing automatically and can fold its tracks away.
		- Or set each track's Output Type to Sends Only and use a send, so a return track acts as the submix.
	- ## 17.5.2.4 Several MIDI Tracks Playing the Same Instrument
		- Point a second MIDI track's Output Type at the instrument track, and choose the instrument itself (not Track In) as Output Channel. Both tracks then play one instrument, so sound changes affect both.
		- ![Feeding another MIDI track into an existing instrument](https://ableton-production.imgix.net/live-manual/12/SeveralMidiTracksPlayingSameInstrumentRoutingExample.png?auto=&w=320)
		- To mute each part separately, move the original clips to a third track and leave the instrument alone on its track, with Input Type set to No Input so it has no Arm button.
	- ## 17.5.2.5 Tapping Individual Outs From an Instrument
		- Impulse offers each of its eight sample slots as a source for other tracks. An audio track whose input is the Impulse track can choose one slot, which takes that slot out of Impulse's own mix for separate effects. Most plug-ins don't remove the tapped output this way.
		- ![Using Impulse's individual outs](https://ableton-production.imgix.net/live-manual/12/ImpulseIndividualOutRoutingExample.png?auto=&w=320)
	- ## 17.5.2.6 Using Multi-Timbral Plug-In Instruments
		- A multi-timbral instrument plays a different part on each MIDI channel. Extra MIDI tracks feed its parts by pointing Output Type at the instrument's track and Output Channel at each part's channel; audio tracks tap its individual outputs.
		- External Instrument devices on other MIDI tracks can do both at once: set MIDI To to the instrument's track and channel, and Audio From to one of its auxiliary outputs. Several can share one track inside a Rack. The instrument's main outputs stay on its own track.
	- ## 17.5.2.7 Feeding Sidechain Inputs
		- A vocoder on a strings track needs a speech signal at its sidechain input: create a "Speech" track whose Output Type is the strings track and whose Output Channel is the vocoder's sidechain. Vocoder plug-ins with their own carrier synth go on a MIDI track and are fed the same way.
		- Many of Live's built-in devices have their own sidechain choosers, so they don't need this.
	- ## 17.5.2.8 Layering Instruments
		- To double a strings part with brass, add a MIDI track with a brass instrument whose Input Type taps the strings track at Post FX. MIDI from another track is tapped after its MIDI effects and just before its instrument, so the brass gets the same notes.
		- ![Using an auxiliary MIDI track to layer instruments](https://ableton-production.imgix.net/live-manual/12/InstrumentLayeringRoutingExample.png?auto=&w=320)
