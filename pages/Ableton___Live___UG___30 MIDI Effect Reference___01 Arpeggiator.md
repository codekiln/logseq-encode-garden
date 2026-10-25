logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Ableton/Live/UG/30 MIDI Effect Reference]]
next:: [[Ableton/Live/UG/30 MIDI Effect Reference/02 CC Control]]
- # [30.1 Arpeggiator](https://www.ableton.com/en/live-manual/12/live-midi-effect-reference/#arpeggiator)
	- ![The Arpeggiator Effect](https://ableton-production.imgix.net/live-manual/12/ArpeggiatorL12.png?auto=&w=320)
	- Arpeggiator turns a held chord or single note into a rhythmic pattern.
	- **Style** sets the order of notes in the pattern, and the display draws it. Previous and Next Style Pattern buttons in the display step through the styles.
		- Most styles are the usual ones: Up, Down, Converge, Diverge.
		- **Play Order** plays notes in the order they were pressed.
		- **Chord Trigger** repeats all held notes together as a block chord.
		- Random styles:
			- **Random** — a continuously shuffled sequence
			- **Random Other** — random, but no note repeats until every held note has played
			- **Random Once** — one random pattern, repeated until the held notes change
	- **Rate** sets the speed, in milliseconds or in tempo-synced divisions depending on the Sync/Free toggle.
	- **Distance** and **Steps** transpose the pattern on each repeat. Distance is the interval in semitones or scale degrees; Steps is how many transposed repeats follow. With Distance +12 st and Steps 2, a pattern starting on C3 plays at C3, then C4, then C5. Negative Distance goes down.
	- **Root** and **Scale** keep the transposition inside a scale. **Use Current Scale** in the title bar takes the clip's scale instead and disables those two choosers.
	- **Gate** sets note length as a percentage of Rate. Over 100% the notes overlap for a legato sound.
	- **Hold** keeps the pattern going after the keys are released, until a new key is pressed. Holding keys and adding more builds up the pattern; playing a held note again removes it.
	- **Pattern Offset** rotates the start of the pattern by a number of steps. At 1 the second note plays first and the first note plays last.
	- **Groove** adds swing from the groove library; the Global Groove Amount in the Groove Pool or Control Bar sets how strong it is.
	- **Retrigger** restarts the pattern:
		- **Off** — never
		- **Note** — on each new note
		- **Beat** — every bar or beat set by **Interval**
		- An LED next to the Retrigger controls flashes on each restart.
	- **Repeats** sets how many times the pattern plays; the default is ∞. Values of 1 or 2 suggest a strummed guitar, and combining Repeats with Retrigger gives patterns with rests between them.
	- The **Velocity** toggle shows the velocity controls. **Decay** is the time to reach the **Target** velocity; a long Decay with Target 0 fades the pattern out. With Retrigger on, the velocity ramp restarts with the pattern.