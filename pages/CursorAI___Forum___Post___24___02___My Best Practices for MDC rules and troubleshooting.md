date-created:: [[2025-02-12 Wed]]
tags:: [[CursorAI/Project Rule]]

- [My Best Practices for MDC rules and troubleshooting - How To - Cursor - Community Forum](https://forum.cursor.com/t/my-best-practices-for-mdc-rules-and-troubleshooting/50526)
	- #OP [[CursorAI/Forum/User/Meh-S-Eze]]
		- > I spent a bunch of time testing stuff with the AI, and we figured out that the rules load based on the numbers `<CURRENT_CURSOR_POSITION>` at the start of the filenames.
			- TODO What does this mean? #Question
		- > if you have rules that clash, the last one wins
		- #Tip
			- [[yaml]] is definitely the way to go
				- easier to read and work with. Plus you can add comments
		- #### Naming System
			- Through trial and error, I found this organization system works best.
			  I use a three-digit format and group rules like this:
				- Core Rules: 001-099
				- Integration Rules: 100-199
				- Pattern/Role Rules: 200-299
			- **Examples:**
				- **Core Rules:**
					- “001-Core-Security.mdc”
					- “015-Core-Logging.mdc”
				- **Integration Rules:**
					- “100-API-Integration.mdc”
					- “110-CLI-Handler.mdc”
				- **Pattern/Role Rules:**
					- “200-File-Pattern-Rule.mdc”
					- “210-Data-Validation.mdc”
	- Comments from [[Person/Brian Madison]]
		- comment 1
			- > As much as I hate XML - it seems to work very well. But I cannot really confirm if it works any better or worse than json or yaml or if it really matters. **But I can at least confirm Yaml is not at all the only format that works within the mdc file**. But it does look so much easier to maintain. But **I generally use the ai to create and maintain them now that I have a good rule for generating rules**, so not as concerned with the format anymore.
		- comment 2
			- > Here it is: [cursor-xml-rules-trial/.cursor/rules/cursor-rules.mdc at main · bmadcode/cursor-xml-rules-trial · GitHub](https://github.com/bmadcode/cursor-xml-rules-trial/blob/main/.cursor/rules/cursor-rules.mdc) [[GitHub/bmadcode/cursor-xml-rules-trial]]
			- > with this is place, in agent composer, just say something like ‘create a rule to always whatever…’
			  btw - if you want to use this with another format - you can ask cursor to maintain the intent but update the rule to reformat as yml or json or whatever and make that the standard
			- > biggest thing that makes this work is that it prioritizes populating the front matter properly and optimized for rule pick up automatically