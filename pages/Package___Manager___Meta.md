alias:: [[Meta Package Manager]], [[Universal Installer]] 
logseq-entity:: [[Logseq/Entity/concept]]

- # Meta [[Package Manager]] aka Universal Installer
	- A special class of package manager that itself can reference packages from multiple package managers.
	- ## [[Examples]]
		- [[aqua]]
		- [[asdf]]
		- [[vfox]]
		- [houseabsolute/ubi: The Universal Binary Installer](https://github.com/houseabsolute/ubi)
			- This is a term from [[mise]] [here](https://mise.jdx.dev/dev-tools/backend_architecture.html#ubi-universal-binary-installer-deprecated)
				- while deprecated in the mise ecosystem, it was supported by mise for a while
				- Example: `ubi:BurntSushi/ripgrep` in [[mise/Config/mise.toml]] would install [[rg]] with mise
	- ## adjacent technologies
		- [[Nix/Package/Manager]] lets people install binaries that are built from standardized [[Nix/Derivation]]s that are pre-built in the custom CI system [[nix/Hydra]] and searchable in [[Nix/Package/Registry]]
		- [[brew]] - a package manager and ecosystem for collecting "formulas" for installing things that may themselves may or may not also be published to other package managers