tags:: [[GitHub/Repo/Template]], [[c74/js]], [[Example]]
date-created:: [[2024/10]]
created-by:: [[Person/Alessandro Petrone]]

- [aptrn/maxmsp-ts-example: Template Max Project with TypeScript and npm dependencies](https://github.com/aptrn/maxmsp-ts-example)
	- > Template Max Project with TypeScript and npm dependencies
	- ## [Bundle dependencies for Max](https://github.com/aptrn/maxmsp-ts-example?tab=readme-ov-file#bundle-dependencies-for-max)
		- You can install dependencies using `pnpm i -D <package-name>`. If you're sure the dependency is [**compatible with Max**](https://github.com/aptrn/maxmsp-ts-example?tab=readme-ov-file#dependencies), you can add it to the config file.
		  
		  The configuration file `maxmsp.config.json` determines which dependencies are included in the compiled output. The default `output_path` is `lib`, placed as a subdirectory of the `outDir` found in the `tsconfig.json` file.
		  
		  You can manually edit the `maxmsp.config.json` file or use command-line scripts:
		  
		  ```
		  pnpm maxmsp add <package-name> [--alias] [--path] [--files]
		  ```
		- `--alias`: Optional. Sets the prefix for the copied files. Default is the package name.
		- `--path`: Optional. Sets the path to the package. Default is the package name.
		- `--files`: Optional. Sets the files to copy. Default is `index.js`.
		  
		  Example:
		  
		  ```
		  pnpm maxmsp add @not251/not251 --alias not251 --files "index.js, index.map.js"
		  ```
		  
		  This will copy files:
		- `node_modules/@not251/not251/dist/index.js`
		- `node_modules/@not251/not251/dist/index.map.js`
		  
		  To:
		- `lib/not251/not251_index.js`
		- `lib/not251/not251_index.map.js`
		  
		  ---
		  
		  This project is heavily inspired by [TypeScript-for-Max](https://github.com/ErnstHot/TypeScript-for-Max) and uses [Max/Msp types at DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/maxmsp)
	-