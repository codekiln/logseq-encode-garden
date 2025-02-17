# DONE How to make CursorAI activate a Project Rule
	- Use a [[CursorAI/Project Rule/Glob]] to ensure a rule is activated
	- In the description, mention a "command", and then use the command, for example, `Use this when Foo! is entered`, and then use `Foo!`
		- [[Person/Brian Madison]] says in [[CursorAI/Forum/Post/24/02/Rules for ultra context memories lessons scratchpad]] [here](https://forum.cursor.com/t/rules-for-ultra-context-memories-lessons-scratchpad-with-plan-and-act-modes/48792/37?u=codekiln)
			- > for me when using `.cursor/rules` - no combination of `USE ME ALWAYS` or `ALWAYS USE THIS FILE` or whatever in the mdc file is not reliable whatsoever.
			- > ... with Claude sonnet at least, if the rules `.mdc` file **has a use command** it will almost always get used.
			- > its also **obvious whenever agent uses an .mdc file it will mention it in the chat**.
			- > something in the mdc description field like `Use this file when the command Foo! is entered` - or whatever you want to use to start your chat threads with.