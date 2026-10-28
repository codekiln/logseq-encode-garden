logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Agent/Skills]]
- # Can you make plugin reference material in both [[Codex/Plugin]]s and [[Claude/Code/Plugin]]s?
	- ## [[AI Answer]]
		- **Short answer:** Yes. Both can distribute reference documents alongside a skill. A small `SKILL.md` describes when the material is relevant and which files to read; the detailed material lives in supporting files.
		- [[Answer/Official]] from [OpenAI: Build skills — Add supporting resources](https://developers.openai.com/plugins/build/skills#add-supporting-resources) and [Claude Code: Add supporting files](https://code.claude.com/docs/en/skills#add-supporting-files).
		- ### Shared reference layout
			- The same skill and reference files can be packaged for both hosts. For example:
				- ~~~text
				  my-plugin/
				  ├── plugin.json
				  ├── .claude-plugin/
				  │   └── plugin.json
				  └── skills/
				      └── product-reference/
				          ├── SKILL.md
				          └── references/
				              ├── terminology.md
				              └── architecture.md
				  ~~~
			- In `SKILL.md`, name the trigger and link to each document, such as: “When answering questions about product terminology, read [terminology.md](references/terminology.md).” The example link resolves inside the packaged skill directory.
			- OpenAI's portable package uses root `plugin.json`; `.codex-plugin/plugin.json` remains a supported compatibility format. Claude Code uses `.claude-plugin/plugin.json` and discovers skills under root `skills/`. The reference contents can stay shared while the manifests describe the package for each host. [OpenAI package structure](https://developers.openai.com/plugins/build/plugins#plugin-structure), [Claude Code standard layout](https://code.claude.com/docs/en/plugins-reference#standard-layout).
		- ### When the material is read
			- Supporting files are read when needed. Bundling documents does not load all their contents into every conversation. Link the documents from `SKILL.md` and explain when to consult each one.
			- A reference skill can answer questions from documentation without running scripts or connecting to an MCP server. OpenAI explicitly supports skills containing only packaged instructions and resources; Claude Code describes reference material as a skill content type. [OpenAI skills](https://developers.openai.com/plugins/build/skills), [Claude Code skill content types](https://code.claude.com/docs/en/skills#types-of-skill-content).
