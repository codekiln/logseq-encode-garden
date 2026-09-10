logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Person/Jeff Dickey]]
date-created:: [[2026/09/03]]
see-also:: [[mise]], [[mise/Backend/packslip]], [[aqua]], [[hk]]

- # [packslip](https://packslip.dev/)
	- Signed release manifest format and toolchain: publishers ship `packslip.sigstore.json` beside release artifacts so consumers can verify signer identity, digests, platform metadata, and executable paths before install.
	- [jdx/packslip](https://github.com/jdx/packslip) — [[GitHub/Star]]: 28 (checked 2026-09-10).
	- Written in [[Rust]].
	- Developed by [[Person/Jeff Dickey]] (author of [[mise]] and [[usageCLI]]).
	- [[mise]]'s preferred Tier 1 install path for tools that publish these manifests — see [[mise/Backend/packslip]]. No separate Packslip CLI install is required to consume via mise.
	- Complements [[aqua]]: aqua uses curated registry metadata; packslip carries a signed vendor description with the release itself (completions, agent skills, and host requirements can travel in the same manifest).
