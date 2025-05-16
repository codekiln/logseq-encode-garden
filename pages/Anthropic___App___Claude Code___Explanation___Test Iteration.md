tags:: [[Claude Code]], [[Testing]], [[Diataxis/Explanation]]

- # Claude Code & [[Programming/Test]] Iteration — Conceptual Guide
	- ## Overview
		- **Claude Code** is Anthropic’s terminal-native agentic coding tool.
		- In a *test-iteration* workflow Claude alternates between **generating / editing tests**, **running them**, and **patching code** until all tests pass.
		- The loop accelerates *test-driven development* (TDD) and bug-fix cycles without hiding the repo’s real history.
	- ## Context & Motivation
		- Traditional TDD is powerful but time-consuming; engineers hand-write red tests, implement code, rerun, repeat.
		- Large-language-model agents can draft failing tests, propose fixes, and validate in seconds—freeing humans to review intent instead of boilerplate.
		- Claude Code embeds this agent inside the developer’s shell, so test iteration happens *in situ* with minimal context switching.
	- ## Key Concepts
		- **Agentic Loop**: Claude gathers context → writes/edits tests → invokes `pytest` → parses results → patches code.
		- **/tests Command**: one-shot prompt that asks Claude to create or update tests for a target module.
		- **Fail-First Strategy**: Claude intentionally produces failing tests to anchor behavior before touching implementation, mirroring human TDD habits.
		- **Safety Prompts**: every file change lands in a diff with *Yes / No* review gates—essential for preventing runaway edits.
		- **Extended Thinking**: adding “think hard” or `/think` triggers deeper planning before the loop.
	- ## Examples
		- *Prompt to seed tests*  
		  ~~~text
		  /tests for utils/date_parser.py covering edge cases
		  ~~~
		- *Iterative bug fix*  
		  ~~~text
		  fix failing test_parse_iso8601
		  ~~~
		  Claude proposes a patch → you approve → `/pytest -q` re-runs automatically.
		- *Generate property-based tests*  
		  ~~~text
		  add hypothesis strategies for the same module
		  ~~~
	- ## Common Misconceptions
		- **“Claude replaces my test suite.”**
			- No. Claude accelerates *authoring*; you still curate, review, and own the tests.
		- **“One pass is enough.”**
			- Agentic iterations often need multiple cycles: generate → refine → finalize.
		- **“It ignores costing.”**
			- Repeated runs consume tokens; use `/cost` to monitor spend.
	- ## When to Use
		- Green-field TDD on a new feature.
		- Legacy code lacking coverage—ask Claude to back-fill tests before refactors.
		- Debug sessions where failing asserts already exist; use Claude to propose targeted fixes.
	- ## Related
		- [[Anthropic/App/Claude Code/How To/Bootstrap Claude Code with Mise + UV-Powered Okta Role Assumption]]
		- Anthropic docs: *Common Tasks → TDD with Claude Code*