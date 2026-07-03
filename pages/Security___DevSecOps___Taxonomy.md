logseq-entity:: [[Logseq/Entity/Concept]]
tags:: [[Diataxis/Concept]]
see-also:: [[Software/Composition/Analysis]], [[Dependency/Update/Automation]], [[Security/Application/SAST]], [[Security/Application/DAST]], [[Security/Vulnerability]]

- # DevSecOps product taxonomy (composition vs code vs runtime)
	- ## Overview
		- Vendors bundle overlapping capabilities; this page **separates product classes** so you can compare apples to apples: **what you import**, **what you wrote**, **how it behaves live**, and **how you keep dependencies fresh**.
		- Quick mental model: **[[Software/Composition/Analysis]]** (**[[SCA]]**) → **risk in third-party components**; **[[Security/Application/SAST]]** → **risk in first-party source**; **[[Security/Application/DAST]]** → **risk in running behavior**; **[[Dependency/Update/Automation]]** → **operational mitigation** once you know what to bump.
	- ## Supply chain security platforms (bundled suites)
		- **What buyers usually get** — **SCA-style inventory** + **advisory / vulnerability intelligence** + **scanners/workflow** (PR comments, policy gates, ticketing) in one contract; sometimes adjacent **secret scanning**, **container scanning**, or **ASPM** messaging.
		- **Examples (illustrative, not exhaustive)** — **Snyk**, **Mend.io** (incl. legacy WhiteSource positioning), **[Heeler](https://www.heeler.com/)** (markets SCA/SAST/secrets with remediation-oriented PRs).
		- **Overlap with à-la-carte SCA** — Suites *include* composition analysis, but marketing “supply chain security” often blurs **full SBOM governance** vs **CVE matching** only; evaluate deliverables, not the label.
	- ## Software composition analysis (SCA)
		- **Primary outputs** — **SBOM**-style inventory (Software Bill of Materials), **version drift**, **license posture**, **provenance** (signing, attestations), and **reachability-aware** vulnerability context—not only “is CVE present”.
		- Canonical page: **[[Software/Composition/Analysis]]** (**[[SCA]]** alias).
	- ## Dependency vulnerability scanning (narrow slice)
		- **Focus** — Given manifests/lockfiles, **match coordinates** against **GHSA/NVD/OSV-style** databases and surface CVEs/CWEs; may skip deep license or provenance storytelling.
		- **Relationship** — Often a **component of SCA** or of **supply chain security platforms**; still useful to name separately when procurement compares “CVE scanner” vs “full composition program.”
		- **Example** — [[deptrust]] — single-package/version lookups against OSV + GitHub Advisory DB across 13 ecosystems; explicitly **no transitive resolution, no SBOM, no license checks**, so it is the narrow slice, not a full SCA program.
	- ## Dependency update automation (freshness + mitigation)
		- **Representatives** — **Dependabot**, **Renovate**, lockfile refresh bots, package-manager upgrade jobs.
		- **Security angle** — They **do not replace SCA**; with **policy + CI**, they help **close disclosed issues quickly** (pin bumps, coordinated upgrades) and reduce **stale** transitive risk—see **[[Dependency/Update/Automation]]**.
	- ## SAST vs DAST (first-party vs runtime)
		- **[[Security/Application/SAST]]** — Static analysis on **your** code/repos (taint, injection, unsafe APIs).
		- **[[Security/Application/DAST]]** — Dynamic testing against **running** services (crawling, fuzzing, authenticated flows).
	- ## Automated remediation beyond PR bots
		- **Observation** — **SCA / dependency** workflows commonly ship **bot-opened PRs**; **SAST/DAST auto-fix** is **less mature** in the market, though some **ASPM / remediation platforms** (e.g. Heeler’s positioning) claim validated PRs across multiple finding sources—**treat as evaluation claims**, not defaults.
	- ## Misconceptions
		- “**Our supply chain tool = SBOM program**” — **Maybe**; many bundles emphasize **CVE dashboards** unless you enforce **SBOM export**, **SPDX/CycloneDX** contracts, and **build-time attestation** requirements.
		- “**Renovate solved security**” — **False** without **[[Software/Composition/Analysis]]** prioritization and **risk review**; freshness can still introduce **breaking** or **malicious** upgrades.
