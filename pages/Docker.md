logseq-entity:: [[Logseq/Entity/Software/Project]]
date-created:: [[2013]]

- # [Docker](https://www.docker.com)
	- Source repository: [moby/moby](https://github.com/moby/moby) (the open-source engine, formerly `docker/docker`). [[GitHub/Star]]: 71,905 (checked 2026-07-13).
	- Platform for building, shipping, and running applications in [[Container]]s: OS-level virtualization that packages an application with its dependencies into a portable image.
	- Written in [[Go]].
	- [[Docker/Compose]] orchestrates multi-container applications from a declarative YAML file.
	- ## Docker Desktop (for Mac)
		- On macOS, Docker runs through Docker Desktop — the GUI app that ships the Linux VM (daemon) plus the client tooling.
		- Installed in these dotfiles via the Homebrew `docker-desktop` cask (see [[brew/file]]); the cask symlinks the bundled [[Docker/CLI]], `docker-compose`, and `kubectl` onto [[Shell/PATH]]. The CLI is sourced from the cask rather than [[mise]] so client and daemon stay version-locked.
		- Getting the CLI onto PATH after install: [[Docker/For Mac/How to Install into Zsh]]
	- ## Related
		- [[Lazydocker]] — TUI for managing containers
		- [[Docker/Concept/vs Dagger and Devcontainers]]
