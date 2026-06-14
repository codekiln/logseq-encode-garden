logseq-entity:: [[Logseq/Entity/Concept]]
tags:: [[Diataxis/Concept]]
see-also:: [[Security/DevSecOps/Taxonomy]], [[Security/Application/SAST]], [[Software/Composition/Analysis]]

- # Dynamic application security testing (DAST)
	- ## Overview
		- **DAST** exercises **running** applications and APIs—**black-, gray-, or white-box** crawling, authenticated flows, fuzzing, and runtime checks—to find issues visible only when code **executes** (misconfigurations, session flaws, authZ gaps, runtime-only injection paths).
		- Complements **[[Security/Application/SAST]]** (static view of **your** code) and **[[Software/Composition/Analysis]]** (third-party **composition** risk).
	- ## Context
		- Often scheduled in **staging**, **pre-prod**, or **synthetic prod** with safe harnesses; overlaps **IAST/RASP** conversations when sensors sit in-process.
		- **Automated remediation** of DAST findings is **rarer** than bot-driven dependency bumps; most value is still **findings → backlog → human fix**—see **[[Security/DevSecOps/Taxonomy]]**.
	- ## Misconceptions
		- “**DAST duplicates SAST**” — **Incomplete**; many bugs (routing, auth state, infra headers) appear only at runtime.
		- “**DAST must mean external black-box only**” — **False**; modern harnesses combine **traffic replay**, **OpenAPI**-driven tests, and **authenticated** journeys.
