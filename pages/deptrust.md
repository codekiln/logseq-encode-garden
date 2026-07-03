logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Clidey]]

- # [deptrust](https://github.com/clidey/deptrust)
	- CLI that checks a specific package **version** for known vulnerabilities across 13 ecosystems: npm, PyPI, Cargo, Go modules, RubyGems, NuGet, Maven, Packagist, pub.dev, CocoaPods, Hex.pm, Hackage, and GitHub Actions. Queries **OSV** and the GitHub Advisory Database in parallel and returns a block / review / allow recommendation based on severity.
	- [[GitHub/Star]]: 15 (checked 2026-07-03).
	- ## What it does not do
		- **No transitive resolution** — checks only the exact package and version given; does not walk a lockfile's dependency graph, so nested/indirect vulnerabilities stay invisible unless each is checked individually.
		- **No SBOM** — does not generate or consume a Software Bill of Materials.
		- **No license analysis** — vulnerability lookup only, not a full [[Software/Composition/Analysis]] program.
		- A provider it cannot query returns **"unknown,"** not a silent "safe."
	- ## Where it sits
		- Matches the **dependency vulnerability scanning (narrow slice)** category on [[Security/DevSecOps/Taxonomy]]: coordinate-to-advisory matching without the fuller SBOM, license, and provenance story that [[Software/Composition/Analysis]] promises.
		- Complements rather than replaces [[Dependency/Update/Automation]] (Dependabot/Renovate-style bots): those decide *when* to bump a dependency; deptrust answers *whether a specific version is already known-bad* before or after that bump.
		- Relevant to [[Security/Attack/Chain/Supply]] as a point-in-time check against disclosed vulnerabilities — it does not defend against zero-days or not-yet-advised malicious packages, though it does flag versions published in the last 72 hours as a secondary risk signal.
	- ## Deployment modes
		- CLI — single-package checks (e.g. `deptrust check npm lodash 4.17.20`), text or JSON output.
		- MCP server — lets an AI coding agent query it directly before adding or upgrading a dependency, instead of a human running the CLI separately.
