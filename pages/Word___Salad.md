tags:: [[Term]]
alias:: [[Neuralese]]
logseq-entity:: [[Logseq/Entity/Concept]], [[Logseq/Entity/Term]]

- # Word Salad
	- Language that is grammatically intact but semantically hollow — the words flow, but the information density is close to zero.
	- ## Origin
		- Clinical term for incoherent speech associated with neurological and psychiatric conditions.
		- Adopted in AI criticism for model output that sounds fluent but conveys little.
		- > "Where I think the word 'hallucination' is useful ... is not to describe what the AI is doing, but what we do when we encounter a word salad, and we impute a writer to the word salad." — [[Person/Cory Doctorow]], [The Guardian, 2026/06/24](https://www.theguardian.com/technology/2026/jun/24/cory-doctorow-on-elon-musk-ai-bubble-bosses-cruel-fantasies)
	- ## "Neuralese" [[Examples]]
		- I have observed [[Claude Code]] and other agents coining useless phrases
			- caveat-of-shame 😂
				- > Accurate disclosure (not a caveat-of-shame):
			- a departing setting
				- > a departing setting's comment explains why, not what
				- what claude should have used: "a setting that is customized"
			- "the co-existence case" and "the absolute fallback"
				- > A test that pins this — the co-existence case resolving to the absolute
				    fallback.
		- [[Person/Tamay Besiroglu/Post/26/06/One interesting pattern with Fable 5 is that it will]]
			- > "The morning's slim-scan fix cured the scan hang"
			- > "this is a latent-drift API-shape wrinkle", etc.
		- PR description [Umbrella: consolidate Beads repo-local Dolt runtime layer · Issue #2685 · gastownhall/beads](https://github.com/gastownhall/beads/issues/2685)
			- ah, "final-tail hardening" 😂
				- > "The landing sequence follows that dependency order: lifecycle precursor / runtime foundations / doctor/runtime alignment / repair safety / final-tail hardening / embedded/schema tail"
		- Mixed metaphors stacked into one sentence — see [[My/Pref/Writing/Avoid Distractors such as Awkward or Superfluous Metaphors]]
			- > Your sketch is ambiguous on one hinge, and it's the same illegal-state knot from before wearing new clothes.
		- Double negatives and so many useless turns of phrase
			- > That's why example 1 (wrap/linebreak) felt like a non-example to you — an unfamiliar reader doesn't obviously know what linebreak does, so spelling it out is earning its place under the real preference, even though the spec's current wording would tell an agent to omit it.
	- ## Buzzword / Jargon [[Examples]]
		- Fluent, grammatical language with near-zero falsifiable content; optimized for sounding reasonable rather than saying something.
		- > "Organizations should leverage holistic synergy through adaptive transformational frameworks that maximize strategic innovation across scalable paradigms."
		- > "Effective collaboration emerges when stakeholders engage in meaningful dialogue that supports innovative outcomes and drives value creation across multiple dimensions."
	- ## Token Bloat (Reasoning Traces)
		- Reasoning traces that repeat rather than converge, exhausting the decoding budget without adding information. The model may be aware it is looping.
		- > "...a significant portion of these tokens are useless self-repetitions—what we call 'word salad'—that exhaust the decoding budget without adding value."
		- Source: [[arXiv/Article/25/11/Word Salad Chopper]]
	- ## Clinical / True Word Salad
		- Semantically incoherent language where sentences parse grammatically but carry no recoverable meaning; the original psychiatric sense.
		- > "The blue window sings tomorrow because electricity sleeps under the pancake."
	- ## Practical Test
		- Can you swap 80% of the nouns for different buzzwords and the paragraph still "works"? If yes, information density is near zero.