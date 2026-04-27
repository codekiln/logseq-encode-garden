logseq-entity:: [[Logseq/Entity/concept]]
tags:: [[Diataxis/Concept]]
see-also:: [[Nix/Pkgs]]
via:: [[2026-04-27 Mon]]

- # Overlay
	- ## Overview
		- In **[[Nix]]** / **[[nixpkgs]]**, an **overlay** is a small piece of configuration that says: when you build the package set, **add or change these attributes** on top of whatever nixpkgs already defines.
		- New keys become new packages; **same keys replace** the previous definition.
	- ## Context
		- **[[Nix/Pkgs]]** is consumed as one large attribute set (`pkgs.git`, `pkgs.bash`, `pkgs.zed-editor`, …). Overlays are how you **customise** that set without forking nixpkgs wholesale.
	- ## Mechanism
		- An overlay is a function with this shape:
			- ~~~
			  final: prev: {
			    # new or overridden names go here
			  }
			  ~~~
		- **`prev`** — the package set **before** your changes (the normal nixpkgs view at this layer).
		- **`final`** — the package set **after all overlays** have been applied; use this when one overlay must refer to attributes defined by **another** overlay.
		- The returned attribute set is **merged** into `pkgs`: additions and overrides apply in overlay order.
	- ## Example: pre-built binary instead of a nixpkgs source build
		- **Problem:** nixpkgs may ship a package (e.g. `zed-editor`) as **`buildRustPackage`** from upstream tags. On **Darwin**, that path often **compiles from source** on your machine when **Hydra has no substitute** which is slow and brittle.
		- **Idea:** Treat the **vendor’s published artifact** (DMG, tarball, zip) as **`fetchurl` / `fetchzip`** with a **pinned version and hash** (fixed-output derivation). Unpack or copy the **`.app`** (or binaries) into **`$out`** with **`stdenvNoCC.mkDerivation`** (or similar). You are **not** compiling upstream; you are **unpacking a known-good blob**.
		- **Where the overlay fits:** Put that whole recipe behind **one new `pkgs` name** (e.g. `zed-darwin-bin`) by returning it from an overlay:
			- ~~~
			  final: prev:
			  if !prev.stdenv.hostPlatform.isDarwin then { } else {
			    zed-darwin-bin = prev.stdenvNoCC.mkDerivation { /* fetchurl src, unpack, install */ };
			  };
			  ~~~
		- After this is merged into your flake’s **`nixpkgs.overlays`**, anything that already takes **`pkgs`** — **nix-darwin** `environment.systemPackages`, **[[Nix___home-manager]]** modules, shells — can refer to **`pkgs.zed-darwin-bin`** like any other package. You can also **override** an existing name (e.g. replace **`zed-editor`**) by using the **same attribute key** in the overlay return set; the **codekiln/dotfiles** repo instead **adds** a new key and **stops referencing** the old one in system packages.
		- **Contrast:** A file like **`nix/pkgs/eilmeldung.nix`** that is only ever used via **`pkgs.callPackage …`** is a **standalone package function**, not an overlay. It does **not** by itself register a name on the global `pkgs` tree; something else must **`callPackage`** it or an overlay must expose it.
		- **Operational note:** First fetch still **downloads** the artifact; Nix **caches** the output by store path. You are avoiding the **Rust/IDE compile**, not avoiding **network + unpack** work. Bumping the pin means updating **version + `fetchurl` hash** (and any unpack steps if the vendor layout changes).