logseq-entity:: [[Logseq/Entity/Standard]]

- # [TAP](https://testanything.org)
	- ## Overview
		- **TAP** (Test Anything Protocol) is a simple, line-based text format for reporting test results. It originated in the [[Perl]] test suite in the late 1980s and is now used across many languages.
		- It decouples the **producer** of test results from the **consumer**: any runner that emits TAP can be read by any TAP-aware harness, so tallying and reporting are not tied to one tool's bespoke output.
	- ## Normative links
		- Official site: [testanything.org](https://testanything.org)
		- Current version: [TAP14](https://testanything.org/tap-version-14-specification.html); TAP13 introduced YAML diagnostic blocks.
	- ## Format
		- A **plan** line `1..N` declares how many tests to expect.
		- Each result is `ok` or `not ok`, a test number, and an optional description: `ok 1 - user can log in`.
		- Directives annotate a line: `# SKIP <reason>` and `# TODO <reason>`.
	- ## Implementations
		- [[bats]] emits TAP for [[Bash]] tests. Consumers include Perl's `prove` harness and CI converters to formats such as JUnit XML.
