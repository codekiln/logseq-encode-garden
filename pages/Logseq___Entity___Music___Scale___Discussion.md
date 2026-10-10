logseq-entity:: [[Logseq/Entity/Discussion]], [[Logseq/Entity/Diataxis/Explanation]]
see-also:: [[Music/Scale]], [[Logseq/Entity/Music/Scale/Frontmatter/scale-semitones-above-tonic]]

- # Music Scale Discussion
	- Why scale pages put the family noun first, nest by the scale's name, carry no fixed tonic, and leave ragas to pages of their own.
	- ## The family noun comes first
		- Variants nest under the noun they qualify: [[Music/Scale/Minor/Natural]], [[Music/Scale/Minor/Harmonic]], [[Music/Scale/Minor/Melodic]] and [[Music/Scale/Minor/Hungarian]] sit together under `Music/Scale/Minor`, and the two pentatonic scales under `Music/Scale/Pentatonic`. The namespace view of a family then lists every variant of it, and the variants sort next to each other.
		- Music theorists treat natural, harmonic and melodic minor as one family: [[Music/Scale/Minor/Natural]] describes them as teaching forms of a single minor mode from the common-practice period, and the `Minor` segment in their paths keeps them together.
		- The alternative was a flat leaf in English word order, `Music/Scale/Natural Minor`. It matches how device menus print the names, and it splits the minor family across the alphabet: Harmonic Minor, Melodic Minor and Natural Minor sort under H, M and N.
	- ## The nesting follows the scale's name
		- A scale whose common name qualifies another scale's name nests under that scale, wherever its pitches come from. [[Music/Scale/Dorian/Ukrainian]] is the fourth mode of [[Music/Scale/Minor/Harmonic]] and sits under Dorian, and [[Music/Scale/Dorian/Bebop]] sits under Dorian as well.
		- A reader looks a scale up by the name a manual or a teacher gives it, so the page path follows that name.
		- Derivation makes a poor basis for the path, because one scale often derives from several parents. Ukrainian Dorian is Dorian with a raised fourth and also a mode of harmonic minor. Each derivation goes in the first line under the H1 and in links from the page body, where a scale can name all of its parents.
	- ## Scale pages carry no fixed tonic
		- One page holds the scale on every tonic. C major is the major scale on C, and a piece or a key in C major links to [[Music/Scale/Major]].
		- A page per tonic would repeat the same history, use and quirks twelve times. What differs between tonics is only the starting pitch, and `scale-semitones-above-tonic::` records the pitches relative to whichever tonic is chosen.
		- Each page's first line spells the scale on C so the reader can read its intervals.
	- ## A raga has a page of its own
		- A raga carries characteristic phrases, ascent and descent rules, emphasized notes and a time of day on top of its pitches, so two ragas can share every pitch and still differ. A scale page records only the pitches and their names.
		- V. N. Bhatkhande grouped Hindustani ragas under ten parent scales, or thaats, in the early [twentieth century]([[19]]). A thaat is a pitch collection, so each thaat gets a scale page, as [[Music/Scale/Marwa]] and [[Music/Scale/Todi]] do, and a raga page links to the scale page of its parent thaat.
	- ## History
		- [[2026-10-10 Sat]] — codekiln and [[Anthropic/Model/Claude/5/5/Opus]] set up [[Logseq/Entity/Music/Scale]] with the naming rules this page explains, wrote a scale page for each entry in the scale menus of the [MicroFreak user guide]([[Microfreak/UG/15 Using Scales/01 Scale Settings]]) and the [Launchpad Pro user guide]([[Launchpad/UG/06 Note Mode/04 Note Mode Settings]]), and linked each menu entry to its scale page.
