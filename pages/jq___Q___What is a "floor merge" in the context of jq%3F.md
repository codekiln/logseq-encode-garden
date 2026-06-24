logseq-entity:: [[Logseq/Entity/Question]]

- # What is a "floor merge" in the context of [[jq]]?
	- ## [[AI Answer]]
		- Short answer: "floor merge" does not appear in the official [[jq]] manual or widely-used community sources as of June 2026; it may be an informal or community-coined term.
		- [[Answer/Official]] from [jq 1.8 Manual](https://jqlang.org/manual/) — no entry for "floor merge" exists in the manual.
		- The manual documents three relevant strategies for combining objects:
			- **Shallow merge** (`+`): inserts all key-value pairs from both objects into one; the right-hand value wins on conflicting keys.
			- **Recursive (deep) merge** (`*`): when both objects share a key whose values are also objects, those nested objects are merged recursively rather than replaced.
				- Example: `{"k": {"a": 1, "b": 2}} * {"k": {"a": 0, "c": 3}}` → `{"k": {"a": 0, "b": 2, "c": 3}}`
			- **Alternative operator** (`//`): returns the right-hand value when the left is `null`, `false`, or empty — a fallback default, not a structural merge.
		- The only official use of "floor" in [[jq]] is the math built-in `floor` (rounds a number down to the nearest integer).
		- If you encountered "floor merge" in a specific blog post, codebase, or talk, that context would clarify the intent; the term is not canonical in [[jq]].
