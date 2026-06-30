logseq-entity:: [[Logseq/Entity/Concept]]
tags:: [[Term]]
wikipedia-link:: https://en.wikipedia.org/wiki/Minimal_reproducible_example

- # Minimal Reproducible Example
	- The smallest self-contained program or dataset that reliably reproduces a bug, allowing someone else to copy, run, and observe the same problem without any additional context.
	- ## Key Characteristics
		- **Minimal** — include only what is necessary to demonstrate the problem; remove everything unrelated.
		- **Complete** — include everything someone else needs to run it; no external dependencies or missing setup.
		- **Reproducible** — verify it actually triggers the issue before sharing.
	- ## Context
		- Coined and popularized by the [[Stack Overflow]] community; the canonical reference is the [Stack Overflow Help Center: How to create a Minimal, Reproducible Example](https://stackoverflow.com/help/minimal-reproducible-example).
		- Also known by several older acronyms: **MCVE** (Minimal, Complete, Verifiable Example), **MWE** (Minimal Working Example), **SSCCE** (Short, Self Contained, Correct Example), and **reprex** (reproducible example, common in the [[R]] community).
		- Creating one is useful both for getting help (forces clarity) and for diagnosing the problem yourself — the process of stripping code down often reveals the root cause.
