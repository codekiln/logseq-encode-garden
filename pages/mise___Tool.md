alias:: [[mise/Docs/Tool]], [[mise Dev Tool]]

- # [Dev Tools | mise-en-place](https://mise.jdx.dev/dev-tools/)
	- The first of the three core [[Jobs to be Done]] of mise is to **install specific versions of the dev tools that you need**, whether that is globally or in a specific project.
	- ## [[Examples]] of dev tools that can be managed with `mise`
		- [[Programming Languages]]
			- [[NodeJS]]
			- [[Python]]
			- etc
		- Anything from a [[Package Manager]]
			- anything from [[npm]], [[pipx]], [[cargo]], etc
		- Anything from a "[Universal Installer](https://mise.jdx.dev/dev-tools/backend_architecture.html#universal-installers)" such as [[aqua]]
			- [[aqua]] — [[Meta Package Manager]] from [[Person/Shunsuke Suzuki]]; [[mise]] and other installers use it for verified OSS binaries with checksums
	- ## [[mise/Tool/GitHub Token]]
		- Credential patterns for tools that call the GitHub API—start at [[mise/Tool/GitHub Token/Native GitHub OAuth]].
	-