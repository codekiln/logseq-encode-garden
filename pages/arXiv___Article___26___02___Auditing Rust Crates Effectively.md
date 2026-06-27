logseq-entity:: [[Logseq/Entity/Article]]
date-created:: [[2026/02/06]]
see-also:: [[Rust/crate]], [[Security/Attack/Chain/Supply]], [[Software/Composition/Analysis]]

- # [Auditing Rust Crates Effectively](https://arxiv.org/abs/2602.06466)
	- arXiv:2602.06466 · Lydia Zoghbi, David Thien, Ranjit Jhala, Deian Stefan, Caleb Stanford
	- ## Summary
		- Introduces Cargo Scan, an interactive Rust auditing tool for third-party crate review.
		- Frames dangerous Rust dependency behavior as effects: unsafe operations, system effects such as filesystem/network/process access, and higher-order control flow.
		- Uses effect analysis plus call-graph context to narrow human review to code that can actually cross a security boundary.
		- Reports that Cargo Scan reduced potentially dangerous audit work to a median of 0.2% of lines of code in the evaluated crates, and could automatically classify about 3.5K of the top 10K crates on crates.io as safe.
	- ## Notes
		- This is relevant to supply-chain review because CVE scanning alone does not answer whether an unfamiliar Rust crate behaves safely in context.
		- Cargo Scan sits between manual reading and broad static-analysis alerts: it tries to find the code paths a human should inspect instead of declaring an entire dependency graph trustworthy.
