logseq-entity:: [[Logseq/Entity/concept]]
tags:: [[Diataxis/Concept]]
see-also:: [[My/Principle/Simplify/Minimize Surface Area]], [[My/Principle/Simplify/Fewer and Deeper]], [[My/Principle/Simplify/Prefer Standards and Defaults]]

- # Risk Profile
	- ## Overview
		- The overall shape of the risks a tool, dependency, system, or decision carries: what can go wrong, how likely it is, and how much it would expose.
		- A profile is understood, not just measured — the goal is a mental model legible enough to reason about before committing.
	- ## Context
		- Every choice to adopt a tool or design pattern imports its failure modes along with its benefits.
		- Comparing options is less about feature counts and more about which option's risk profile is easier to hold in your head and defend.
	- ## Key Principles
		- ### Legibility beats raw count
			- A small, well-understood set of risks is safer than a larger set that is individually milder but collectively opaque.
		- ### Surface area drives exposure
			- More entry points, dependencies, and configuration knobs widen the profile. [[My/Principle/Simplify/Minimize Surface Area]].
		- ### Fewer, deeper choices concentrate risk where it can be scrutinized
			- Consolidating on fewer tools that are more secure yields a more understandable profile. [[My/Principle/Simplify/Fewer and Deeper]].
		- ### Defaults shift the profile
			- Well-chosen standards and sensible defaults inherit the vetting of a broad community; bespoke variants carry undocumented risk. [[My/Principle/Simplify/Prefer Standards and Defaults]].
	- ## Misconceptions
		- A lower risk profile does not mean fewer features — it means the residual risk is bounded and explainable.
		- More security controls do not automatically improve the profile if they add complexity no one fully understands.
