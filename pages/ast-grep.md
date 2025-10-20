tags:: [[CLI/Tool]], [[Code/Mod]]

- [ast-grep | structural search/rewrite tool for many languages](https://ast-grep.github.io/)
	- #via [[Person/Peter Steinberger]]
		- [Peter Steinberger on X: "Adding ast-grep has been a huge win for my codebase. Keeps agents from boundary violations and writing crappy code. https://t.co/xBVzLptl8b Supports pretty much all languages! Some examples: - Add AST-grep rules to flag .insertInto('profiles') outside lib/db/** to prevent" / X](https://x.com/steipete/status/1963411717192651154)
			- I don't totally understand Peter's examples, but it sounds generally useful to provide validators to [[LLMs]]
				- > Some #Examples
					- > Add AST-grep rules to flag `.insertInto('profiles')` outside `lib/db/**` to prevent drift.
					- > Codec boundaries (no `new Date` / `toISOString` outside validators)
					- > JSONB hygiene (Disallow `JSON.stringify(...)` in `.set`)
	- [[My Notes]] I wonder how this compares with
		- [[Py/Lib/LibCST]], [[GritQL]]