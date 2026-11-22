tags:: [[Idea]]
date-created:: [[2026-11-22 Sun]]
see-also:: [[git/hook]], [[Logseq/mise/Task/fix-wikilink-labels]]

- # Declare checks per technology once, and enforce them in every repository that uses the technology
	- ## Problem
		- Most checks belong to a technology rather than to a repository. A Logseq graph should have its labeled wikilinks rewritten before commit. A Rust crate should pass `cargo fmt` and `clippy`. An OpenSpec directory should pass strict validation.
		- Today each repository wires its checks into its own [[lefthook]] config by hand. Nothing records the rule "a repository with a Logseq graph runs these hooks", so the rule lives only in whoever remembers to copy it.
		- On [[2026-11-22 Sun]], adding one check for Logseq gardens, [[Logseq/mise/Task/fix-wikilink-labels]], took a separate issue, pull request and `lefthook.yml` edit in each of six garden repositories. In one of them, gitpa, the hooks had never been installed, so the identity guard its `lefthook.yml` declared was not running.
		- The costs that follow:
			- Repositories that use the same technology run different checks.
			- A new repository starts with no checks until someone remembers to add them.
			- Changing a standard check means editing every repository again.
	- ## What the framework would do
		- A team declares, in one central place, the checks it expects for each technology.
		- A repository receives those checks because it uses the technology, detected from files such as `logseq/config.edn`, `Cargo.toml` or `openspec/`.
		- A repository can override a default: turn a check off, change its arguments, or exclude paths such as test fixtures.
		- A change to the central declaration takes effect in every repository that uses the technology.
	- ## Relation to clilint
		- [[Person/codekiln/GitHub/clilint]] pairs a written standard with a checker that scores conformance. A per-technology expectation is the same shape one level up: the standard says what a repository using a technology should run, and the checker reports which repositories fall short.
	- ## Technologies to research
		- [[lefthook]] remote configs, with `lefthook-local.yml` for per-repository overrides
		- [[hk]], whose Pkl configs can amend a shared base
		- Trunk Check, which turns on linters for the languages it detects in a repository
		- MegaLinter and Super-Linter, which pick linters by detected language
		- pre-commit and prek shared hook repositories
		- Developer portal scorecards such as Backstage, Cortex and OpsLevel, which report on standards across repositories
