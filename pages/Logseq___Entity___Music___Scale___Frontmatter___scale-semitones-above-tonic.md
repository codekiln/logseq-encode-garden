logseq-entity:: [[Logseq/Entity/Frontmatter/Definition]]
alias:: [[scale-semitones-above-tonic]]

- # `scale-semitones-above-tonic::` — pitches of a scale
	- The pitches of a [[Logseq/Entity/Music/Scale]] instance, as semitones above the tonic in twelve-tone equal temperament, in ascending order.
	- ## Values
		- Space-separated integers from 0 to 11, starting with 0. For example, `scale-semitones-above-tonic:: 0 2 4 5 7 9 11` on [[Music/Scale/Major]].
		- A scale with different ascending and descending forms records the ascending form. The page body describes the other.
		- A name that sources spell in several ways records the most common form. The page body lists the variants.
		- A scale from a tradition that does not use equal temperament records the nearest equal-tempered pitches.
