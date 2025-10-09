tags:: [[Diataxis/Explanation]]

- # DevContainer Features vs Templates
	- ## Overview
		- **DevContainer Features** and **DevContainer Templates** are two complementary building blocks in the Dev Containers ecosystem. Features extend a container's functionality, while Templates define full development environments.
	- ## Context
		- Dev Containers let developers define reproducible environments for local development or GitHub Codespaces. Understanding the difference between Features and Templates helps teams decide whether they need a reusable tool installation or a full environment scaffold.
	- ## Key Principles
		- **Features** add tools or capabilities to a container.
		- **Templates** define ready-to-use environment blueprints.
		- Both use JSON metadata and can reference one another.
	- ## Mechanism
		- ### Features
			- Are modular extensions added under the `features` key in `devcontainer.json`.
			- Contain installation logic (usually `install.sh`) and a `devcontainer-feature.json` descriptor.
			- Can be published to container registries (e.g., `ghcr.io/devcontainers/features/node:1`).
			- Applied during build time to modify the base image.
		- ### Templates
			- Provide full environment scaffolds that include a Dockerfile, `devcontainer.json`, extensions, and Features.
			- Defined by a `template.json` file that describes the setup and references required Features.
			- Used when initializing new repositories or Codespaces.
			- Serve as opinionated starting points for teams or language stacks.
	- ## Examples
		- ### Feature Example
			- Adds a specific tool to any container:
			- ~~~json
			  {
			    "features": {
			      "ghcr.io/devcontainers/features/node:1": { "version": "22" },
			      "ghcr.io/devcontainers-community/features/pnpm:latest": {}
			    }
			  }
			  ~~~
		- ### Template Example
			- Scaffolds a Node + TypeScript project environment:
			- ~~~json
			  {
			    "name": "Node & TypeScript",
			    "description": "Base template for Node development",
			    "features": {
			      "ghcr.io/devcontainers/features/node:1": {},
			      "ghcr.io/devcontainers/features/git:1": {}
			    }
			  }
			  ~~~
	- ## Misconceptions
		- *Myth:* Templates and Features are interchangeable.
		- *Reality:* Templates describe environments; Features install or configure capabilities.
		- *Myth:* Features are only for languages.
		- *Reality:* They can configure any system-level dependency or toolchain.
	- ## Related
		- [Dev Containers Specification](https://containers.dev/implementors/features/)
		- [DevContainer Templates Repository](https://github.com/devcontainers/templates)