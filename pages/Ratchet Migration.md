logseq-entity:: [[Logseq/Entity/Concept]]
tags:: [[Diataxis/Concept]]

- # Ratchet Migration
	- ## Overview
		- A ratchet migration moves a codebase from an old framework to a new one component by component, under a written policy that only lets the migration go forward.
		- A typical policy: maintain the old thing in the old framework, write new components in the new framework, and if a change would touch more than 10% of an old component, rewrite that component in the new framework.
	- ## Mechanism
		- Every new component and every rewritten component lands in the new framework, so the share of code in the old framework can only shrink.
		- The threshold decides when a rewrite pays for itself. A small fix to an old component stays in the old framework. A change past the threshold is the time to rewrite, because the team is reworking that component anyway.
		- The migration happens as part of regular feature work, so it needs no rewrite project of its own.
	- ## Examples
		- Replacing the UI framework that a set of front-end components is written in.
		- Replacing the template that new services are generated from.
		- Replacing how applications load their secrets and configuration.
	- ## Related
		- [[My/Principle/Follow Ratchet Migrations]]
		- [[Refactor]]
