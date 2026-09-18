logseq-entity:: [[Logseq/Entity/Card]], [[Logseq/Entity/Keyshort]]

- ### 1. What [[Keyshort]] moves to the end of the line, and 2. what moves to the last non-blank character? [[card]]
	- 1. `$` (`Shift+4`) — last character before the newline, regardless of trailing spaces
	- 2. `g_` — last non-blank on the line (`g` then `_`; alternative combos include `$ge` or `$be`)
