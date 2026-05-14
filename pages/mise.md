filters:: {"diataxis/how to" true}
tags:: [[CLI/Tool]] 
created-by:: [[Person/Jeff Dickey]]

- https://mise.jdx.dev/
- > The front-end to your dev env
  Pronounced "MEEZ ahn plahs"
- ## [[mise/About]]
  id:: 67b5a9b2-f8da-41a0-a1b1-18115c27dffc
	- `mise` (pronounced "meez") or [[mise-en-place]] is a **development environment setup tool**.
		- name refers to French culinary phrase roughly translating to "setup" or "put in place"
			- **before one begins cooking, a professional chef should have all their utensils and ingredients ready to go and in their place**
	- ### Key Ideas for `mise`
		- #### [[Declarative]] configuration
			- The main idea of `mise` is that [[mise/Config/mise.toml]] can let either a project or a user declare the
			- `mise.toml` describes consistent way to setup and interact with projects across languages
			- `mise.toml` is a file type used by the `mise` cli that lets developers globally declare or individual projects locally declare the programming languages, the package manager packages, the environment variables, and the common tasks that need to be run
		- #### [[Package/Manager/Meta]]
			-
	- ### The Three Core [[Jobs to be Done]] or Main Use Cases for `mise`
		- `1`: as a **[[Declarative]] [[mise Dev Tool]] installer of [[Programming Languages]] and [[Package Managers]] packages**
			- installs versions of [[NodeJS]], [[Py]], [[tf]] as well as any package from those ecosystems
			- specify versions of tools per project or globally
			- `mise` supports [hundreds](https://mise.jdx.dev/plugins.html) of dev tools
			- [[Person/Jeff Dickey]] has also created [[aqua]] to be a "better" aka more secure meta-package manager
		- `2`: as a [[Declarative]] **environment manager**
			- manages [[EnvVar]]s for project or globally
			- lets you specify configuration like `AWS_ACCESS_KEY_ID` that may differ between projects. It can also be used to automatically activate a [Python virtualenv](https://mise.jdx.dev/lang/python.html) when entering projects too.
		- `3`: as a **task runner** to share common tasks *within* a project
			- for example, run a task when a file changes
	- [[mise/Docs/Guides/Getting Started]]
		- [[mise/Todos]]
	- [[mise/Docs/Guides/Walkthrouh]]
		- ## mise commands
			- [[mise/install]]