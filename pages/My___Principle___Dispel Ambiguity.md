see-also:: [[My/Principle/Explicit is better than Implicit]], [[My/Principle/Favor Readers Over Writers]], [[My/Principle/Make Illegal States Unrepresentable]], [[EARS]]

- # what it means
	- leave the reader, user, or caller with exactly one available interpretation
	- a thing can be explicit and still ambiguous: it states something, but more than one reading survives. dispelling ambiguity removes the surviving readings until one is left
	- this is distinct from [[My/Principle/Explicit is better than Implicit]] (is it stated at all?) and from plain language (is it easy to read?). here the question is whether the reader can take it more than one way
- ## where it applies
	- software architecture: a boundary, name, or interface should admit one obvious meaning; if two components could each own a responsibility, decide which one and make it visible
	- communication: say the one thing you mean, not the phrasing that could be read two ways
	- documentation: answer the question the reader would otherwise have to guess at
	- word choice: see below
- ## word choice
	- avoid a word with more than one meaning when one of those meanings is a plausible distractor in context — the reader has to stop and pick, and may pick wrong
	- prefer the term with a single reading over the clever one that carries two
- ## why
	- every surviving interpretation is a place the reader, user, or future maintainer can diverge from what you meant
	- ambiguity defers the cost: cheap to leave in, expensive to discover later, once someone has already acted on the wrong reading
	- [[My/Principle/Make Illegal States Unrepresentable]] is the strongest form of this — collapse the readings until the wrong one cannot even be expressed
