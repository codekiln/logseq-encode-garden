see-also:: [[Logseq/Docs/The basics of block references]]

- # Logseq Block Id
	- In Logseq, a block **can** have an id. For example:
		- here is a block with an id
		  id:: 6ab79a92-405e-4723-9253-252e619fdc57
			- here's a child block of a block with an id
	- By default, blocks **don't** have an id. It's added to [[Logseq/Block/Attribute/id]] **at the moment one copies a reference to** the block (for example, if one's cursor is in edit mode in a block without text selected, and one presses Cmd+c, then the a block id is generated and placed on that block). Once you have a reference to the block, you can point to it elsewhere, like this:
		- ((6ab79a92-405e-4723-9253-252e619fdc57))
	- You can also embed block, which also embeds that block's children.
		- {{embed ((6ab79a92-405e-4723-9253-252e619fdc57))}}
	- You could  logseq doesn't show the id by default, but it exists on disk.
	- Logseq block ids are [[UUID]]s. Here's the text that renders the block link above: `((6ab79a92-405e-4723-9253-252e619fdc57))`. In the markdown file, block attributes look like `id:: 6ab79a92-405e-4723-9253-252e619fdc57`.
	-