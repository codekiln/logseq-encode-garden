logseq-entity:: [[Logseq/Entity/Card]], [[Logseq/Entity/Keyshort]]

- ### 1. What [[Keyshort]] stops at punctuation-delimited words on `myObj.methodName('foo')`, and 2. what [[Keyshort]] jumps by whitespace-delimited words instead? [[card]]
	- 1. `w` — treats punctuation as word boundaries (many stops across `methodName('foo', …)`)
	- 2. `W` — moves to just after the next whitespace character (fewer, bigger stops on the same line)
