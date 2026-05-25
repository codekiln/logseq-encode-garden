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
		- #### [[Declar/at/ive]] configuration
			- The main idea of `mise` is that [[mise/Config/mise.toml]] can let either a project or a user declare the
			- `mise.toml` describes consistent way to setup and interact with projects across languages
			- `mise.toml` is a file type used by the `mise` cli that lets developers globally declare or individual projects locally declare the programming languages, the package manager packages, the environment variables, and the common tasks that need to be run
		- #### [[Package/Manager/Meta]]
			- Mise integrates with multiple [[Meta Package Manager]]s or [[Universal Installer]]s. In that sense, it's a meta-meta-package-manager (LOL).
	- ### The Three Core [[Jobs to be Done]] or Main Use Cases for `mise`
		- {{embed [[mise/JTBD/1 - Dev Tool Installer]]}}
		- {{embed [[mise/JTBD/2 - Environment Manager]]}}
		- {{embed [[mise/JTBD/3 - Task Runner]]}}
	- [[mise/Docs/Guides/Getting Started]]
		- [[mise/Todos]]
	- [[mise/Docs/Guides/Walkthrouh]]
		- ## mise commands
			- [[mise/install]]