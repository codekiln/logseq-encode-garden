tags:: [[DevContainer]], [[Diataxis/Reference]]
- # DevContainer Feature Arguments
	- ## Overview
		- Devcontainer [[DevContainer/Feature]]s are OCI images that include a `devcontainer-feature.json` specification and an `install.sh` script.
		- Feature arguments are declared as `options` in `devcontainer-feature.json`, passed from `devcontainer.json`, and exposed to `install.sh` as `FEATURE_OPTION_*` environment variables.
	- ## Where Arguments Are Defined
		- Arguments are defined in the feature's `devcontainer-feature.json` under the `options` object.
		- ~~~json
		  {
		    "id": "aws-cli",
		    "version": "1.0.0",
		    "name": "AWS CLI",
		    "options": {
		      "version": {
		        "type": "string",
		        "default": "2",
		        "description": "AWS CLI version to install"
		      }
		    }
		  }
		  ~~~
		- Common option properties:
			- `type`: Value type (for example `string`, `boolean`)
			- `default`: Fallback when user does not provide a value
			- `description`: Human-readable explanation
			- `enum`: Allowed values
			- `proposals`: Suggested values for tooling/UI
	- ## How Users Pass Arguments
		- Users pass arguments in `devcontainer.json` under the `features` key.
		- ~~~json
		  {
		    "features": {
		      "ghcr.io/devcontainers/features/aws-cli:1": {
		        "version": "2"
		      }
		    }
		  }
		  ~~~
		- If a value is omitted, the feature option's `default` is used.
	- ## How Features Receive Arguments
		- The feature system converts options to environment variables in this format:
		- ~~~text
		  FEATURE_OPTION_<OPTION_NAME>
		  ~~~
		- Example:
		- ~~~text
		  FEATURE_OPTION_VERSION=2
		  ~~~
		- Option-name normalization:
			- Uppercase all letters
			- Replace hyphens with underscores
		- Example mapping:
			- `node-version` -> `FEATURE_OPTION_NODE_VERSION`
		- Example `install.sh` usage:
		- ~~~bash
		  AWS_VERSION="${FEATURE_OPTION_VERSION}"
		  if [ "$AWS_VERSION" = "2" ]; then
		      install_aws_v2
		  fi
		  ~~~
	- ## Lifecycle Behavior
		- During build/apply, the runtime sequence is:
			- 1. Resolve features
			- 2. Merge option values with defaults
			- 3. Export options as `FEATURE_OPTION_*` environment variables
			- 4. Run `install.sh` with those variables available
		- The Dev Container specification passes option values through; feature scripts decide their effect.
	- ## Common Uses
		- Conditional installation:
			- ~~~bash
			  if [ "${FEATURE_OPTION_INSTALL_AWSCLI}" = "true" ]; then
			     ...
			  fi
			  ~~~
		- Package version selection:
			- ~~~bash
			  apt-get install nodejs=${FEATURE_OPTION_NODE_VERSION}
			  ~~~
		- Conditional dependency/tool installation inside feature logic.
	- ## Limitation
		- Feature arguments cannot change behavior outside what the feature author implemented.
		- They do not directly override broader devcontainer behavior unless the feature script/metadata consumes those options.
		- Examples:
			- They cannot disable VS Code extensions declared by feature metadata unless feature logic supports that.
			- They cannot directly modify unrelated base container configuration.
	- ## Mental Model
		- ~~~text
		  OCI image
		    + devcontainer-feature.json (metadata + options)
		    + install.sh (logic)
		  ~~~
		- ~~~text
		  devcontainer.json
		       ↓
		  feature options
		       ↓
		  env vars (FEATURE_OPTION_*)
		       ↓
		  install.sh logic
		  ~~~
	- ## References
		- [Dev Container Features - Implementors Specification](https://containers.dev/implementors/features/)
