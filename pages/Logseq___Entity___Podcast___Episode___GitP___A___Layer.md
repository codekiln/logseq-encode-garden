logseq-entity:: [[Logseq/Entity/Definition]]

- # Ghost in the Patch Alpha Layer
	- In this garden, **Ghost in the Patch Alpha Layer** pages model one live-looping layer of a [[Logseq/Entity/Podcast/Episode/GitP/A]] performance, so notes can name a part of the performance the same way every time.
	- This definition is a prototype.
	- ## Layers in a performance
		- Recent performances loop three layers, A, B and C. Each layer records the [[Microfreak]]'s incoming audio on one track and its incoming MIDI on the track beside it.
	- ## Names
		- `<episode>/Layer/<letter>` is the layer, such as `GitP/A/Session/26/11/01-Sun/Layer/A`.
		- `<episode>/Layer/<letter>/Audio` and `<episode>/Layer/<letter>/MIDI` are the layer's audio and MIDI parts.
		- Chapter notes can link these names, such as `[[GitP/A/Session/26/11/01-Sun/Layer/B/Audio]]`, or say "layer B" in prose when a link adds nothing.
	- ## Page shape
		- A layer page has one H1, such as `Layer A`, and a short line on what the layer carried in the performance.
		- An Audio or MIDI page has one H1 and links the [[Logseq/Entity/Ableton/Track/Track]] page that recorded it under `<episode>/Set/Track/`, when the episode has an [[Logseq/Entity/Ableton/Set]].
		- A layer or part page exists only when something links to it with a reason; the name alone is enough for most notes.
