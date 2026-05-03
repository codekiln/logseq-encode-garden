alias:: [[Glyph Terminal Protocol]]
logseq-entity:: [[Logseq/Entity/standard]]
created-by:: [[Person/Raphael Amorim]]
see-also:: [[Rio]], [[Font/Tofu]], [[iTerm2/Image/Protocol]]

- # Glyph Protocol
	- ## Normative links
		- [Introducing Glyph Protocol for Terminals](https://rapha.land/introducing-glyph-protocol-for-terminals/)
		- [Adding color glyphs to Glyph Terminal Protocol](https://rapha.land/adding-color-glyphs-to-glyph-terminal-protocol/)
		- [raphamorim/glyph-protocol-examples](https://github.com/raphamorim/glyph-protocol-examples)
	- ## Scope
		- Terminal protocol for registering custom glyphs at runtime and querying whether a codepoint can be rendered.
		- Uses APC framing, a small verb set for support/query/register/clear, and Unicode Private Use Area codepoints as the safety boundary.
		- Initial monochrome payloads use TrueType `glyf` outlines; color support extends the protocol with OpenType `colrv0` and `colrv1` payload containers.
	- ## Notes
		- The practical target is the "patched font" problem for prompts, editors, and TUIs: apps can ship the few glyphs they need instead of requiring users to install a full Nerd Font.
		- The security idea is clean: do not allow arbitrary text codepoints to be visually overwritten; keep registered glyphs in PUA codepoints so normal URLs, commands, filenames, and shell output keep rendering as their bytes.
		- [[Rio]] is the reference implementation.
