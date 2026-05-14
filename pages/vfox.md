see-also:: [[mise/Backend/vfox]]
tags:: [[Package/Manager/Meta]]

- # [vfox | The Multiple SDK Version Manager](https://vfox.dev/)
	- {{embed [[vfox/GitHub]]}}
	- > A cross-platform and extendable [[Meta Package Manager]] with support for [[Java]], [[NodeJS]], [[Go]], [[Python]], Flutter, .NET & more
	- If you frequently switch between projects that require different runtime environments or runtime versions, or are tired of complicated environment configuration, `vfox` is your best choice.
	- `vfox` is a cross-platform, extensible universal version manager that supports **Windows (native)** and **Unix-like** systems, enabling you to **quickly install and switch** development environments.
	- ## [[Declarative]]
		- It saves all tool version information in a `.vfox.toml` file, making it convenient to share configuration across projects and ensuring team members use the same tool versions.
		- Traditional solutions require installing multiple version managers (such as [[nvm]], `fvm`, `sdkman`, `asdf-vm`, etc.), each with different APIs, configuration files, and implementations (involving `$PATH` operations, shims, environment variables, etc.). `vfox` provides a unified interaction method and configuration file to simplify the workflow, and can be extended to any tool and runtime environment through a simple plugin interface.