logseq-entity:: [[Logseq/Entity/Software/Project]]
tags:: [[CLI/Tool]], [[Programming/Code/Analysis/Static/Lint/er]]

- # [clilint](https://github.com/codekiln/clilint)
	- A CLI conformance linter: run it against a command-line tool and get a reproducible conformance score plus machine-readable, actionable findings.
	- Implements the **CLI Lint** standard — versioned, testable criteria distilled from [[CLI/Guidelines]] and [[Person/Jeff Dickey/Blog/18/10/09/12 Factor CLI Apps]].
	- Realizes [[CLI/Agent/ic/Principle]]: a shared standard that measurably improves both human and AI-agent use of a CLI, plus the tooling to measure adherence.
	- Reports carry stable rule identifiers (prefix `CLI-`), evidence, severity, score impact, and remediation, so an [[AI/Agent]] can loop: generate a CLI, lint it, repair violations, and re-check conformance.
	- Vocabulary: CLI Lint standard, CLI Lint rules, CLI Lint score, CLI Lint conformance, and the `clilint` command.
