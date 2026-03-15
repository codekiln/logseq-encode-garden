---
---
- # [A minimal flake for a shell](https://fnordig.de/til/nix/minimal-flake.html) — [[TIL]]
	- Author: **[[Person/Jan-Erik Rediger]]**
	- Source: [fnordig.de TIL](https://fnordig.de/til/nix/minimal-flake.html)
	- ## Flake (minimal dev shell)
		- ~~~
		{
		  description = "A very basic flake";
		  outputs = { self, nixpkgs, ... }:
		    let
		      supportedSystems = [ "aarch64-linux" "aarch64-darwin" "x86_64-darwin" "x86_64-linux" ];
		      forAllSystems = nixpkgs.lib.genAttrs supportedSystems;
		    in
		    {
		      devShells = forAllSystems (system:
		        let
		          pkgs = nixpkgs.legacyPackages.${system};
		        in
		        {
		          default = pkgs.mkShell {
		            buildInputs = with pkgs;
		              [
		                ripgrep
		              ];
		          };
		        });
		    };
		}
		~~~
		- Run with: `nix develop`
	- ## Old way (shell.nix)
		- ~~~
		with import <nixpkgs> {};
		pkgs.mkShell {
		  nativeBuildInputs = with pkgs; [
		    ripgrep
		  ];
		}
		~~~
		- Run with: `nix-shell`
