logseq-entity:: [[Logseq/Entity/Concept]]
tags:: [[Diataxis/Concept]]
alias:: [[SCA]]
see-also:: [[Security/DevSecOps/Taxonomy]], [[Dependency/Update/Automation]]

- # Software composition analysis
	- ## Overview
		- **Software composition analysis (SCA)** is the discipline of **understanding what ships inside your software** beyond first-party code: direct and **transitive** open-source and vendor components, their **versions**, **licenses**, **provenance**, and **known vulnerabilities**.
		- Strong programs publish **SBOMs** (Software Bill of Materials), track **license** obligations, and retain **provenance** signals—not only **match packages to CVEs** (that narrower slice is still often labeled “SCA” in marketing; see **[[Security/DevSecOps/Taxonomy]]**).
		- It answers “**what are we made of?**” and “**where is the risk?**” so engineering, security, and legal can prioritize fixes, replacements, or policy exceptions.
	- ## Context
		- SCA overlaps **application security**, **license compliance**, and **SBOM** (Software Bill of Materials) work; outputs often feed **[[Dependency/Update/Automation]]** (which component to bump first) and incident response.
		- Modern graphs are deep (frameworks pull hundreds of packages); manual spreadsheets do not scale—**graph scanners** and **registry APIs** do.
	- ## Key Principles
		- **Transitives matter** — A CVE in a nested dependency is still your release surface.
		- **Version + hash identity** — Same package name can denote different artifacts; **lockfiles** and **checksum policies** (e.g. **[[aqua]]**-style registries) tighten identity.
		- **Signal over noise** — Effective SCA ranks reachable vs unreachable findings and de-duplicates across environments.
	- ## Mechanism
		- **Inventory** — Parse manifests, lockfiles, container layers, and binaries; map to canonical coordinates (PURL, CPE, ecosystem IDs).
		- **Enrichment** — Join with advisory databases (GHSA, NVD), license metadata, maintainer activity, and signing status.
		- **Governance** — Policies block merges on critical severities, require SBOM exports, or mandate upgrade SLAs.
	- ## Examples
		- CI step that fails on **critical** CVSS in reachable `npm` / `pip` / `go` modules with an SBOM attached to the build.
		- License policy that flags **copyleft** in statically linked mobile binaries.
	- ## Misconceptions
		- “**SCA = only CVE scanning**” — **Incomplete**; license, **yanking**, typosquatting, and **unmaintained** signals are part of composition risk.
		- “A clean scan **forever** absolves us” — **False**; new advisories land daily; **[[Dependency/Update/Automation]]** must keep inventory current.
