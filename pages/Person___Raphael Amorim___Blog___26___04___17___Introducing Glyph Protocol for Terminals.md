source:: https://rapha.land/introducing-glyph-protocol-for-terminals/
created-by:: [[Person/Raphael Amorim]]
date-created:: [[2026/04/17]]
see-also:: [[Glyph Protocol]], [[Rio]], [[Font/Tofu]], [[iTerm2/Image/Protocol]]

- # [Introducing Glyph Protocol for Terminals](https://rapha.land/introducing-glyph-protocol-for-terminals/)
	- ## My Notes
		- [[Person/Raphael Amorim]] proposes [[Glyph Protocol]] as a terminal protocol for applications to register custom vector glyphs at runtime and query whether a codepoint is renderable.
		- The post frames missing glyphs as a distribution problem: users install large patched fonts so a TUI can render a few icons, while application authors still cannot know whether the glyphs are actually present.
		- The protocol uses APC framing with verbs for support, query, register, and clear; registrations are restricted to Unicode Private Use Area codepoints so programs cannot spoof normal text.
		- The first payload is a constrained TrueType `glyf` outline: small, vector, already understood by terminal text renderers, and rendered in the current foreground color.
		- The comparison to Kitty Image Protocol and DECDLD makes the design feel like a precise terminal-native layer: not an image protocol, not a bitmap character-set relic, but glyph registration with modern safety boundaries.
	- ## Links
		- [[Glyph Protocol]]
		- [[Rio]]
		- [raphamorim/glyph-protocol-examples](https://github.com/raphamorim/glyph-protocol-examples)
