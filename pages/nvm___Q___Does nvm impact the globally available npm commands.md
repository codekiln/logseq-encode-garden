tags:: Q, nvm, npx, mise

- # Does the version of [[NodeJS]] activated with [[nvm]] interact with the [[CLI/Tool]]s that are available at the CLI?
	- Yes, when using [[nvm]], the active Node.js version determines which globally installed npm packages are available
		- Each Node.js version managed by nvm has its own separate global package directory
		- When switching Node versions with nvm, you switch which global packages are available
	- ## What is the [[Best Practice]] for managing global versions of npm commands when using [[nvm]] to manage node with [[mise]]?
		- When migrating from [[nvm]] to [[mise]], there are several approaches:
			- 1. Use [[mise]] to manage Node.js versions:
			  ```bash
			  mise use --global node@20  # or whatever version you need
			  npm install -g repomix     # install global packages with active node version
			  ```
			- 2. For project-specific packages, prefer local installation in `package.json` over global installation
			- 3. Use [[npx]] to run packages without installing them globally:
			  ```bash
			  npx repomix ...           # runs latest version without global install
			  ```
			- 4. If you need multiple versions, you can specify the node version explicitly:
			  ```bash
			  mise x node@20 -- npm install -g repomix
			  ```
		- Note: After installing global packages, you may need to run `mise reshim` to ensure the commands are available in your PATH