## High Level Reflections
	- Corey Doctorow's books (particularly [[Person/Corey Doctorow/Book/25/Picks & Shovels]] and [[Person/Corey Doctorow/Book/25/Enshittification]]) have taught me that [[Interop]] tools like `rulesync` are important because in the age of AI, vendor lock-in is likely to become a serious issue. [[pandoc]] could serve as an example for how to do an interop tool like `rulesync`
	- But the pace of AI progress is fast. The feature surface area of the underlying tools is exploding. The cost of using and maintaining an abstraction layer like `rulesync` is becoming high. If I keep my canonical [[AI/Coding/Config]]s in `rulesync`'s formats, then I can't easily use the latest features of Claude Code, such as
		- [Support for Claude Skills · Issue #422 · dyoshikawa/rulesync](https://github.com/dyoshikawa/rulesync/issues/422)
		- [Feature request: for claude code slash commands, support passing through claude-code-specific yaml markdown frontmatter keys to the generated command markdown files · Issue #413 · dyoshikawa/rulesync](https://github.com/dyoshikawa/rulesync/issues/413)
		- [Support for Claude Code plugins and Gemini CLI extensions · Issue #382 · dyoshikawa/rulesync](https://github.com/dyoshikawa/rulesync/issues/382)
	- In the past couple weeks, as Claude Code Skills emerged, I stopped primarily using `rulesync` because the latest features can't be represented in rulesync's format yet.
	  I have been thinking about [Programmatic API · Issue #377 · dyoshikawa/rulesync](https://github.com/dyoshikawa/rulesync/issues/377), and from the perspective of someone using the tool, maybe it could make sense to optimize for lossless modeling of AI code configs and best effort conversion.
	- ### Proposed rulesync architectural assumptions
		- 1 - **assume users will store AI code configs some AI coding tool's native format**, whether that's cursor, claude code, or any of the many tools that are out there
		- 2 - **optimize rulesync for "lossless conversion" within each tool**. This means that if I store my configs in Claude Code, then if I import into rulesync, then wipe away my `.claude` directory and regenerate from rulesync, every file and folder should work the way it did before.
		- 3 - **make rulesync "best effort" or "lossy" between tools**. The tools are not always going to have feature parity with each other, and the concepts are not going to match. Rulesync would
	- ### Benefits of this approach
		- Even if tool X adds feature Y which hasn't been added as a feature to rulesync, a user can still use feature Y until it's supported for conversion.
	- ### What could this look like?
		- 1 - `rulesync` could assume that one tool is the "parent" from which other code configs are adapted from that source
-