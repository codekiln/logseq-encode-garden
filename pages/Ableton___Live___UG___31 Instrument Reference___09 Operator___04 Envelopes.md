logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/31 Instrument Reference/09 Operator]]
prev:: [[Ableton/Live/UG/31 Instrument Reference/09 Operator/03 LFO Section]]
next:: [[Ableton/Live/UG/31 Instrument Reference/09 Operator/05 Filter Section]]
- # [31.9.4 Envelopes](https://www.ableton.com/en/live-manual/12/live-instrument-reference/#envelopes-1)
	- Seven envelopes: one per oscillator, plus filter, pitch and LFO. All can loop; filter and pitch envelopes have adjustable slopes.
		- ![Operator's Oscillator B Envelope](https://ableton-production.imgix.net/live-manual/12/OperatorOscEnvelopeL12.png)
	- Oscillator envelopes have three rates and three levels: from Initial (often -inf dB) at the attack rate to Peak, at the decay rate to Sustain, and after note-off at the release rate back to silence. Drag breakpoints or nudge selected ones with arrow keys. Copy shapes between oscillators from the context menu.
	- **Slopes** (filter, pitch) — positive moves fast then slow, negative slow then fast, zero linear.
	- **Loop** — an envelope that reaches sustain while held restarts; **Loop Time** sets the return. Fast loops give effects you wouldn't expect from an envelope, and are the key to endless evolving FM sounds.
	- **Beat** — restarts after the **Repeat** beat time without quantizing the first note. **Sync** — quantizes the first repeat to the nearest 16th so repeats follow the song; acts like Beat when stopped.
	- Looped envelopes restart from their current level at the attack rate, so they don't click.
	- **Trigger** — ignores note-off; good for percussion.
	- Global **Time** scales all rates except Beat and Sync times; **Time < Key** speeds envelopes for higher notes; **Time < Vel** per envelope.
	- The pitch envelope has **Destination A–D** and **LFO** buttons with an amount, an on switch in the shell, and a **Dest. B** target with **Amt. B**.
	- Pitch and filter envelopes add **End**, the level after release.
	- Tip from the manual: a looping pitch envelope routed only to the LFO acts as a second LFO on its rate, and the LFO's own looping envelope as a third on its depth.
