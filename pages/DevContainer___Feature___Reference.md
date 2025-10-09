# [Dev Container Features reference](https://containers.dev/implementors/features/)
	- ## Quotes
		- ### Intro
			- **Development Container Features** are self-contained, shareable units of installation code and development container configuration. The name comes from the idea that referencing one of them allows you to quickly and easily add more tooling, runtime, or library “features” into your development container for you or your collaborators to use.
			- Feature metadata is captured by a `devcontainer-feature.json` file in the root folder of the feature.
			- **Note:** While Features may be installed on top of any base image, the implementation of a Feature might restrict it to a subset of possible base images. For example, some Features may be authored to work with a certain Linux distro (e.g. debian-based images that use the `apt` package manager).
		- ### [Folder Structure](https://containers.dev/implementors/features/#folder-structure)
			- A Feature is a self contained entity in a folder with at least a `devcontainer-feature.json` and `install.sh` entrypoint script. Additional files are permitted and are packaged along side the required files.
			- ```
			  +-- feature
			  |    +-- devcontainer-feature.json
			  |    +-- install.sh
			  |    +-- (other files)
			  ```
		- ## [devcontainer-feature.json properties](https://containers.dev/implementors/features/#devcontainer-feature-json-properties)
			- The `devcontainer-feature.json` file defines metadata about a given Feature.
			- [devContainerFeature.schema.json](https://github.com/devcontainers/spec/blob/main/schemas/devContainerFeature.schema.json) defines the schema for the `devcontainer-feature.json` file.
		- ### [User environment variables](https://containers.dev/implementors/features/#user-env-var)
			- Feature scripts run as the `root` user and sometimes need to know which user account the dev container will be used with.
			- `_REMOTE_USER` and `_CONTAINER_USER` environment variables are passsed to the Features scripts with `_CONTAINER_USER` being the container’s user and `_REMOTE_USER` being the configured `remoteUser`. If no `remoteUser` is configured, `_REMOTE_USER` is set to the same value as `_CONTAINER_USER`.