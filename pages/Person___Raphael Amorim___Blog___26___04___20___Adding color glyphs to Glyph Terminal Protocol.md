source:: https://rapha.land/adding-color-glyphs-to-glyph-terminal-protocol/
created-by:: [[Person/Raphael Amorim]]
date-created:: [[2026/04/20]]
see-also:: [[Glyph Protocol]], [[Rio]]

- # [Adding color glyphs to Glyph Terminal Protocol](https://rapha.land/adding-color-glyphs-to-glyph-terminal-protocol/)
	- ## My Notes
		- Follow-up to [[Person/Raphael Amorim/Blog/26/04/17/Introducing Glyph Protocol for Terminals]] that extends [[Glyph Protocol]] beyond monochrome `glyf` outlines.
		- Adds color payload formats for OpenType `colrv0` and `colrv1`: layered flat-color glyphs for the simple case, and full paint-graph glyphs for gradients, transforms, and richer emoji-like rendering.
		- The key design move is reuse: terminals and text stacks already have OpenType parsers and paint walkers, so the protocol wraps COLR/CPAL plus referenced outlines instead of inventing a new vector format.
		- This keeps the same conceptual promise as the original post: the application can ship the glyph shape it needs, the terminal renders it like text, and every TUI framework above the terminal can benefit from the same registration.
	- ## Links
		- [[Glyph Protocol]]
		- [raphamorim/glyph-protocol-examples](https://github.com/raphamorim/glyph-protocol-examples)
