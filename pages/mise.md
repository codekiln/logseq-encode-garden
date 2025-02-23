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
	- use `mise.toml` describes consistent way to setup and interact with projects across languages
	- ### 3 categories of usage for `mise`
		- `1`: installs [[NodeJS]], [[Python]], [[Terraform]]
			- specify versions of tools per project
			- `mise` supports [hundreds](https://mise.jdx.dev/plugins.html) of dev tools
		- `2`: manages [[EnvVar]]s
			- lets you specify configuration like `AWS_ACCESS_KEY_ID` that may differ between projects. It can also be used to automatically activate a [Python virtualenv](https://mise.jdx.dev/lang/python.html) when entering projects too.
		- `3`: task runner to share common tasks *within* a project
			- for example, run a task when a file changes
- [[mise/Docs/Guides/Getting Started]]
	- [[mise/Todos]]