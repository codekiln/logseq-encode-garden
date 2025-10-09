tags:: [[Diataxis/Explanation]]

- # DevContainer Features vs Templates
	- ## Overview
		- [[DevContainer Feature]]s and [[DevContainer/Template]]s are two complementary building blocks in the Dev Containers ecosystem. Features define a pluggable, reusable way to define a container's functionality, while Templates define full development environments, including [[VSCode/Extension]]s, etc, typically in such a way that relies on features.
	- ## Context
		- Dev Containers let developers define reproducible environments for local development or GitHub Codespaces. Understanding the difference between Features and Templates helps teams decide whether they need a reusable tool installation or a full environment scaffold.
	- ## Key Principles
		- **Features** add tools or capabilities to a container.
		- **Templates** define ready-to-use environment blueprints.
		- Both use JSON metadata and can reference one another.
	- ## Mechanism
		- ### [[DevContainer Feature]]s
			- Are modular extensions added under the `features` key in `devcontainer.json`.
			- Contain installation logic (usually `install.sh`) and a `devcontainer-feature.json` descriptor.
			- Can be published to container registries (e.g., `ghcr.io/devcontainers/features/node:1`).
			- Applied during build time to modify the base image.
		- ### [[DevContainer/Template]]s
			- Provide full environment scaffolds that include a Dockerfile, `devcontainer.json`, extensions, and Features.
			- Defined by a `devcontainer-template.json` file that describes the setup and references required Features.
			- Used when initializing new repositories or Codespaces.
			- Serve as opinionated starting points for teams or language stacks.
	- ## Examples
		- ### [[DevContainer Feature]] #Example
			- Adds a specific tool to any container:
			- ~~~json
			  {
			    "features": {
			      "ghcr.io/devcontainers/features/node:1": { "version": "22" },
			      "ghcr.io/devcontainers-community/features/pnpm:latest": {}
			    }
			  }
			  ~~~
		- ### [[DevContainer/Template]] #Example
			- [TypeScript Node Template](https://github.com/devcontainers/templates/tree/main/src/typescript-node)
			  collapsed:: true
				- Scaffolds a Node + TypeScript project environment:
					- [Template Configuration](https://github.com/devcontainers/templates/blob/main/src/typescript-node/devcontainer-template.json)
						- ~~~json
						  {
						      "id": "typescript-node",
						      "version": "4.0.2",
						      "name": "Node.js & TypeScript",
						      "description": "Develop Node.js based applications in TypeScript. Includes Node.js, eslint, nvm, yarn, and the TypeScript compiler.",
						      "documentationURL": "https://github.com/devcontainers/templates/tree/main/src/typescript-node",
						      "publisher": "Dev Container Spec Maintainers",
						      "licenseURL": "https://github.com/devcontainers/templates/blob/main/LICENSE",
						      "options": {
						          "imageVariant": {
						              "type": "string",
						              "description": "Node.js version (use -bookworm, -bullseye variants on local arm64/Apple Silicon):",
						              "proposals": [
						                  "22-bookworm",
						                  "22-bullseye",
						                  "20-bookworm",
						                  "18-bookworm",
						                  "20-bullseye",
						                  "18-bullseye"
						              ],
						              "default": "22-bookworm"
						          }
						      },
						      "platforms": [
						          "Node.js",
						          "TypeScript"
						      ],
						      "optionalPaths": [
						          ".github/*"
						      ]
						  }
						  ~~~
					- [DevContainer Configuration](https://github.com/devcontainers/templates/blob/main/src/typescript-node/.devcontainer/devcontainer.json)
						- ~~~json
						  // For format details, see https://aka.ms/devcontainer.json. For config options, see the
						  // README at: https://github.com/devcontainers/templates/tree/main/src/typescript-node
						  {
						  	"name": "Node.js & TypeScript",
						  	// Or use a Dockerfile or Docker Compose file. More info: https://containers.dev/guide/dockerfile
						  	"image": "mcr.microsoft.com/devcontainers/typescript-node:1-${templateOption:imageVariant}"
						  
						  	// Features to add to the dev container. More info: https://containers.dev/features.
						  	// "features": {},
						  
						  	// Use 'forwardPorts' to make a list of ports inside the container available locally.
						  	// "forwardPorts": [],
						  
						  	// Use 'postCreateCommand' to run commands after the container is created.
						  	// "postCreateCommand": "yarn install",
						  
						  	// Configure tool-specific properties.
						  	// "customizations": {},
						  
						  	// Uncomment to connect as root instead. More info: https://aka.ms/dev-containers-non-root.
						  	// "remoteUser": "root"
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
- # Conceptual Overview — DevContainer Features vs Templates
	- ## 🧩 Core Idea
		- **Features** and **Templates** serve different purposes in the Dev Containers ecosystem.
		- Features extend the functionality *inside* a container. Templates define a *complete* development environment.
	- ## 🔍 Conceptual Difference
		- | Aspect | **Features** | **Templates** |
		  |---------|---------------|----------------|
		  | **Purpose** | Add or configure tools in a dev container | Define and scaffold full dev environments |
		  | **Granularity** | Micro — one capability per module | Macro — full environment definition |
		  | **Timing** | Applied during container build | Applied when initializing a new repo or Codespace |
		  | **Analogy** | Like installing packages (`apt install node`) | Like generating a new project (`cookiecutter node-template`) |
		  | **Scope** | Inside the container image | Repository + workspace structure |
		  | **Visibility** | Used under the `features` key | Used via the Dev Container Template UI or CLI |
	- ## ⚙️ What You *Can Do* with Templates That Features Can't
		- 1. **Define a Complete Environment**
			- Templates can include `.devcontainer/devcontainer.json`, a `Dockerfile`, VS Code settings, and multiple Features.
		- 2. **Scaffold New Projects**
			- Templates can generate the `.devcontainer` folder and starter files — bootstrapping new repos or Codespaces.
		- 3. **Set Workspace Defaults**
			- Templates can define editor extensions, workspace settings, and post-create commands.
		- 4. **Bundle and Compose Features**
			- Templates curate multiple Features (Node, pnpm, Git) into a cohesive stack with predefined versions.
		- 5. **Control Base Images**
			- Templates specify base images or Dockerfiles — Features cannot.
		- 6. **Provide Organizational Standards**
			- Templates let teams share opinionated baselines (e.g., `typescript-course-template`) that enforce consistent environments.
		- 7. **Include Documentation and Metadata**
			- Templates include `template.json`, `NOTES.md`, and optional `README` files for discoverability and onboarding.
		- 8. **Integrate with UI Workflows**
			- Templates appear in the VS Code "Add Dev Container Configuration" and GitHub Codespaces galleries.
	- ## 🧠 Conceptual Model
		- ~~~text
		  Template → (Dockerfile/Base Image) → Features → Installed Tools → Developer Workspace
		  ~~~
		- **Templates** define the outer structure and intent.
		- **Features** act as modular building blocks plugged into that structure.
	- ## ✅ Practical Example
		- A **team template** might include:
		- ~~~json
		  {
		    "name": "TypeScript Course Environment",
		    "features": {
		      "ghcr.io/company/team-devcontainers/pnpm": {},
		      "ghcr.io/company/team-devcontainers/postgres": {}
		    },
		    "customizations": {
		      "vscode": {
		        "extensions": ["esbenp.prettier-vscode", "dbaeumer.vscode-eslint"]
		      }
		    }
		  }
		  ~~~
		- This defines a consistent environment across all TypeScript course repos, while each Feature handles a modular install task.
	- ## 📎 Summary
		- **Use Features** for **reusable tool installation**.
		- **Use Templates** for **complete environment definitions**.
		- Together, they enable composable, standardized, and reproducible dev setups.