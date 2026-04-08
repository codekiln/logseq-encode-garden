- How to install github copilot cli with nix
	- This is from [[Numtide/llm-agents.nix]]
		- [llm-agents.nix/packages/copilot-cli/package.nix at main · numtide/llm-agents.nix](https://github.com/numtide/llm-agents.nix)
			- ok, it's up to date at least!
			- Maybe I should use this for all my [[Agentic Coding Tool]]s?
			- ```
			  nix run github:numtide/nix-ai-tools#copilot-cli -- --version
			  GitHub Copilot CLI 1.0.21.
			  
			  npm view @github/copilot version
			  1.0.21
			  
			  ```
	- [github-copilot-cli on nixpkgs is very, very old](https://search.nixos.org/packages?buckets=%7B%2522package_attr_set%2522:%5B%2522No+package+set%2522%5D,%2522package_license_set%2522:%5B%2522Unfree%2522%5D,%2522package_maintainers_set%2522:%5B%5D,%2522package_teams_set%2522:%5B%5D,%2522package_platforms%2522:%5B%5D%7D&channel=25.11&query=copilot&show=github-copilot-cli)
		- it points to here [nixpkgs/pkgs/by-name/gi/github-copilot-cli/package.nix at nixos-25.11 · NixOS/nixpkgs](https://github.com/NixOS/nixpkgs/blob/nixos-25.11/pkgs/by-name/gi/github-copilot-cli/package.nix#L41)
			- current version from npm is 1.0.21, but the version hardcoded there is 0.0.362
			-
	-