logseq-entity:: [[Logseq/Entity/Concept]]
tags:: [[Diataxis/Concept]]
alias:: [[Winner's Curse]]
see-also:: [[Game/Theory]]

- # Winner's curse
	- ## Overview
		- The **winner's curse** names a systematic bias in **common-value** or **uncertain-value** auctions and procurement: the party who **wins** is often the one who **most overestimated** the item’s true worth.
		- Conditional on winning, your signal about value was probably **optimistic relative to others’ signals**, so “winning” can mean you paid too much or committed too much—bad news packaged as victory [^1].
	- ## Context
		- Classic illustrations include **oil-tract lease auctions** (early economics literature) and many **spectrum** or **natural-resource** settings where bidders share similar upside but hold **noisy private estimates** [^1].
		- Closely related to **adverse selection**: the event “you won” updates beliefs about whether your information was too rosy.
		- Parent topic: strategic reasoning under payoffs and information lives under **game theory**—see **[[Game/Theory]]** for the broader field this phenomenon sits in.
	- ## Key principles
		- **Common vs private components** — When much of the unknown value is **common** across bidders, bids aggregate optimism; the top bid tends to come from the tail of the error distribution.
		- **Winner’s information** — Winning is **informative**: it tells you your estimate ranked **highest**, which should shift how you interpret your prior signal ex post.
		- **Rational adjustment** — Sophisticated participants **shade** bids below naive best-response levels (incorporate expected regret from winning only when values are high enough).
	- ## Mechanism
		- Suppose each bidder draws an **imprecise estimate** of an underlying value with independent noise. The **maximum** of several estimates is biased **upward** relative to the true value (order-statistics intuition).
		- Whoever bids closest to their estimate among aggressive bidders is disproportionately someone whose error term was **positive**—so their expected profit conditional on winning can turn **negative** unless bids discount that selection effect.
	- ## Examples
		- **Oil and mineral lease auctions** — Early empirical work argued winners systematically overpaid relative to ex post outcomes [^1].
		- **IPO pops and asset markets** — Informally invoked when “winning” allocations correlate with paying **peak enthusiasm** prices (not identical to the auction model but shares selection logic).
		- **Career and education choices** — Informal analogy: paths chosen partly to **signal ability** can resemble paying for a scarce badge where the selection story matters more than average returns (compare discussion in today’s journal near **[[Phrase/Boil the Ocean]]**).
	- ## Misconceptions
		- “Winning always means you made a mistake” — **Too strong** in **pure private-values** settings where your value is idiosyncratic and others’ optimism doesn’t shift your own downside the same way.
		- “The curse means auctions are irrational” — **Misleading**; much of auction theory is about **equilibrium bidding** that **internalizes** the curse via shading, reserve prices, and better information design.
	- ## Footnotes
		- [^1]: https://en.wikipedia.org/wiki/Winner%27s_curse — overview of common-value auctions and Capen–Clapp–Campbell oil-tract framing (see references there for primary sources).
