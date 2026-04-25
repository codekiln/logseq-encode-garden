tags:: [[Nix]]
alias:: [[Determinate Systems]]
logseq-entity:: [[Logseq/Entity/company]]
see-also:: [[Binary/Cache]], [[Nix]], [[Nix/OS]]

- # [Determinate Systems](https://determinate.systems/)
	- Company built around [[Nix]], focused on making Nix reproducibility, security, and deployment workflows fit enterprise software delivery.
	- They ship a distribution of nix that's downstream of the original.
		- In this version, [[Nix/flake]]s are [considered stable](https://manual.determinate.systems/release-notes-determinate/changes.html).
			- so you do not need to enable `flakes` or `nix-command` as experimental features there. That removes one of the most common “why is this still behind a flag?” annoyances for everyday use.
		- They ship downstream distribution with its own installer and upgrade path. Their manual explicitly recommends a [[GUI]] installer for [[MacOS]] and provides a curl installer for Linux/WSL; upgrades are handled through `determinate-nixd upgrade`.
	- ## Feature offerings
		- **[[Determinate/Nix]]** — downstream Nix distribution for developer workstations, CI/CD, cloud, and enterprise control.
		- **FlakeHub** — platform for publishing and discovering Nix flakes; Determinate positions it as private flake sharing plus [[Binary/Cache]] support for teams.
		- **FlakeHub Cache** — advanced Nix [[Binary/Cache]] with repository-level access control and authentication via trusted builders or `determinate-nixd login`.
		- **Determinate Secure Packages** — signed and auditable Nix package offering.