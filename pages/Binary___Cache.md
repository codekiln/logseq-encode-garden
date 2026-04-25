alias:: [[Binary Cache]]
logseq-entity:: [[Logseq/Entity/term]]
see-also:: [[Nix]], [[Nix/OS]]

- # Binary Cache
	- A binary cache is a cache of already-built artifacts, so a system can download trusted build outputs instead of rebuilding the same derivations locally.
	- In [[Nix]], binary caches are one of the practical levers that make reproducible builds usable day to day: CI can build once, publish the result, and developer machines or deploy targets can fetch the matching store paths later.
	- [[Cachix]] is centered on hosted Nix binary cache sharing.
	- [[DeterminateSystems]] offers binary-cache features through FlakeHub Cache.
