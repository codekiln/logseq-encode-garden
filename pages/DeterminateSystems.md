tags:: [[Nix]]

- [Determinate Systems](https://determinate.systems/)
	- Company built around [[Nix]]
	- They ship a distribution of nix that's downstream of the original.
		- In this version, [[Nix/flake]]s are [considered stable](https://manual.determinate.systems/release-notes-determinate/changes.html).
			- so you do not need to enable `flakes` or `nix-command` as experimental features there. That removes one of the most common “why is this still behind a flag?” annoyances for everyday use.
		- They ship downstream distribution with its own installer and upgrade path. Their manual explicitly recommends a [[GUI]] installer for [[MacOS]] and provides a curl installer for Linux/WSL; upgrades are handled through `determinate-nixd upgrade`.