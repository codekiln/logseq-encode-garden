logseq-entity:: [[Logseq/Entity/Standard]]
tags:: [[Diataxis/Reference]]
alias:: [[MADR]], [[Markdown Architectural Decision Records]]
see-also:: [[Architecture/Decision/Record]]
date-created:: [[2018]]

- # [About MADR | MADR](https://adr.github.io/madr/)
	- **Markdown Architectural Decision Records** (MADR, pronounced like English “matter”[^1]) are a **lean Markdown template** for capturing **architecturally significant** decisions—each record documents **one** architectural decision (AD) and its rationale. The project positions “architecture” broadly: technology choices, tooling, libraries, or product behavior can qualify if they affect the system enough to warrant a structured record.
	- ## Normative and canonical links
		- **Project site / overview:** [About MADR](https://adr.github.io/madr/)
		- **Repository:** [github.com/adr/madr](https://github.com/adr/madr) — template files, [releases](https://github.com/adr/madr/releases/latest), [changelog](https://github.com/adr/madr/blob/develop/CHANGELOG.md), [rendered decision examples](https://adr.github.io/madr/decisions/) ([source](https://github.com/adr/madr/tree/develop/docs/decisions))
		- **Development template (moving target):** [adr-template.md on `develop`](https://github.com/adr/madr/blob/develop/template/adr-template.md)
		- **Peer-reviewed write-up:** [Markdown Architectural Decision Records: Format and Tool Support](https://dblp.org/rec/conf/zeus/KoppAZ18.html) (ZEUS 2018)
		- **License:** dual [MIT](https://opensource.org/licenses/MIT) or [CC0 1.0](https://creativecommons.org/share-your-work/public-domain/cc0/); SPDX: `MIT OR CC0-1.0`
	- ## Relationship to [[Architecture/Decision/Record]]
		- General ADR practice is wider than one file format; this page anchors the **MADR-specific** file shape, filenames, and optional YAML metadata used in the official template. For motivation and team pitfalls around ADRs, start from [[Architecture/Decision/Record]].
	- ## Template shape (summary)
		- Top matter (optional): YAML for site generators—e.g. title, `status`, `date`, `decision-makers`, `consulted`, `informed` (see live template).
		- **Title** (`#`): short title of the solved problem and chosen solution.
		- **Context and Problem Statement** — situation and the question to settle (links to issues/boards welcome).
		- **Decision Drivers** (optional) — forces and constraints.
		- **Considered Options** — bullet list of alternatives.
		- **Decision Outcome** — `Chosen option: "…", because …`
		- **Consequences** (optional) — Good/Bad bullets.
		- **Confirmation** (optional) — how you verify the decision (reviews, tests, ArchUnit-style checks, etc.).
		- **Pros and Cons of the Options** — per-option Good / Neutral / Bad bullets.
		- **More Information** (optional) — evidence, links to superseding ADRs, revisit triggers.
	- ## Applying in a codebase
		- **Layout:** create `docs/decisions` (or another root; MADR does not mandate repo layout). Copy [contents of the `template/` folder](https://github.com/adr/madr/tree/develop/template) into that directory—includes `adr-template.md`, lint config, and ancillary files.
		- **npm:** install published package and copy template:
			- ~~~
			  npm install madr && mkdir -p docs/decisions && cp node_modules/madr/template/* docs/decisions/
			  ~~~
		- **New decision file:** copy `adr-template.md` to `NNNN-title-with-dashes.md` (consecutive `NNNN`, lowercase dashed title, `.md` suffix); convention is [documented as ADR-0005](https://adr.github.io/madr/decisions/0005-use-dashes-in-filenames.html). Other filename schemes exist in the wider ADR community but may break tooling.
		- **Linting:** Markdown style can drift; the repo ships [`.markdownlint` config](https://github.com/adr/madr/tree/develop/template) and an [example GitHub Actions workflow](https://github.com/adr/madr/blob/develop/.github/workflows/lint.yaml) using [markdownlint](https://github.com/DavidAnson/markdownlint).
	- ## Large projects: categories
		- Optional subdirectory per category (e.g. `decisions/backend/`, `decisions/ui/`); numbering is then **per category**, not globally unique—see [ADR-0010](https://adr.github.io/madr/decisions/0010-support-categories.html) and the [categories discussion](https://adr.github.io/madr/).
	- ## Example (this garden)
		- **[[Person/lv416e/GitHub/dotfiles]]** — public [[dotfiles]] repo records dotfiles architecture in [docs/adr](https://github.com/lv416e/dotfiles/tree/main/docs/adr) with an explicit [MADR-format README](https://github.com/lv416e/dotfiles/blob/main/docs/adr/README.md) and numbered ADRs `0001`–`0009`.
	- ## Minimal example (from the project site)
		- ~~~
		  # Use Plain JUnit5 for advanced test assertions

		  ## Context and Problem Statement

		  How to write readable test assertions?
		  How to write readable test assertions for advanced tests?

		  ## Considered Options

		  * Plain JUnit5
		  * Hamcrest
		  * AssertJ

		  ## Decision Outcome

		  Chosen option: "Plain JUnit5", because it is a standard framework and the features of the other frameworks do not outweigh the drawbrack of adding a new dependency.
		  ~~~
	- ## Footnotes
		- [^1]: https://adr.github.io/madr/
