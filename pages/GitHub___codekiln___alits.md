- [[2025-02-09 Sun]]
- [[2025-02-08 Sat]]
	- tried to get [[VSCode/Dev Container]] spec from [[GitHub/zsteinkamp/m4l-typescript-base]] working with [[GitHub/codekiln/alits]], which was created from [[GitHub/aptrn/maxmsp-ts-library-template]]
		- #Error
			- Error from inside the dv container
				- ```
				  [1259 ms] Keep-alive process ended.
				  [1261 ms] Shell server terminated (code: 137, signal: null)
				  
				  
				  [1324 ms] Error reading shell environment.
				  [1324 ms] Shell server terminated (code: 1, signal: null)
				  
				  Error response from daemon: container ba8901b9aeafaad738f91e3d681c309c73504967e32d4b42669ca7fea8d2c4d3 is not running
				  
				  [1324 ms] Start: Run in container: mkdir -p '/tmp/devcontainers-e15077b4-5822-42d3-a12f-87f095e1973f1739007908030' && cat > '/tmp/devcontainers-e15077b4-5822-42d3-a12f-87f095e1973f1739007908030/env-loginInteractiveShell.json' << 'envJSON'
				  [1324 ms] Stdin closed!
				  [1324 ms] Failed to cache user env: Shell server terminated (code: 137, signal: null)
				  ```
			- `Error: An error occurred setting up the container.`
				- ```
				  
				  Shell server terminated (code: 126, signal: null)
				  OCI runtime exec failed: exec failed: cannot exec in a stopped container: unknown
				  Start: Run in container:  (command -v getent >/dev/null 2>&1 && getent passwd 'root' || grep -E '^root|^[^:]*:[^:]*:root:' /etc/passwd || true)
				  Stdin closed!
				  Error: An error occurred setting up the container.
				      at htA (/Users/me/.cursor/extensions/ms-vscode-remote.remote-containers-0.394.0/dist/spec-node/devContainersSpecCLI.js:410:3955)
				      at process.processTicksAndRejections (node:internal/process/task_queues:95:5)
				      at async TtA (/Users/me/.cursor/extensions/ms-vscode-remote.remote-containers-0.394.0/dist/spec-node/devContainersSpecCLI.js:482:4021)
				      at async iB (/Users/me/.cursor/extensions/ms-vscode-remote.remote-containers-0.394.0/dist/spec-node/devContainersSpecCLI.js:482:4963)
				      at async wrA (/Users/me/.cursor/extensions/ms-vscode-remote.remote-containers-0.394.0/dist/spec-node/devContainersSpecCLI.js:663:203)
				      at async DrA (/Users/me/.cursor/extensions/ms-vscode-remote.remote-containers-0.394.0/dist/spec-node/devContainersSpecCLI.js:662:14830)
				      at async /Users/me/.cursor/extensions/ms-vscode-remote.remote-containers-0.394.0/dist/spec-node/devContainersSpecCLI.js:482:1190
				  Stop (552 ms): Run: /Applications/Cursor.app/Contents/Frameworks/Cursor Helper (Plugin).app/Contents/MacOS/Cursor Helper (Plugin) /Users/me/.cursor/extensions/ms-vscode-remote.remote-containers-0.394.0/dist/spec-node/devContainersSpecCLI.js up --user-data-folder /Users/me/Library/Application Support/Cursor/User/globalStorage/ms-vscode-remote.remote-containers/data --container-session-data-folder /tmp/devcontainers-a68b82b6-a332-4932-8764-912b26f5e8b11739007283189 --workspace-folder /Users/me/Documents/GitHub/alits --workspace-mount-consistency cached --gpu-availability detect --id-label devcontainer.local_folder=/Users/me/Documents/GitHub/alits --id-label devcontainer.config_file=/Users/me/Documents/GitHub/alits/.devcontainer/devcontainer.json --log-level debug --log-format json --config /Users/me/Documents/GitHub/alits/.devcontainer/devcontainer.json --default-user-env-probe loginInteractiveShell --mount type=volume,source=vscode,target=/vscode,external=true --skip-post-create --update-remote-user-uid-default on --mount-workspace-git-root --include-configuration --include-merged-configuration
				  Exit code 1
				  Command failed: /Applications/Cursor.app/Contents/Frameworks/Cursor Helper (Plugin).app/Contents/MacOS/Cursor Helper (Plugin) /Users/me/.cursor/extensions/ms-vscode-remote.remote-containers-0.394.0/dist/spec-node/devContainersSpecCLI.js up --user-data-folder /Users/me/Library/Application Support/Cursor/User/globalStorage/ms-vscode-remote.remote-containers/data --container-session-data-folder /tmp/devcontainers-a68b82b6-a332-4932-8764-912b26f5e8b11739007283189 --workspace-folder /Users/me/Documents/GitHub/alits --workspace-mount-consistency cached --gpu-availability detect --id-label devcontainer.local_folder=/Users/me/Documents/GitHub/alits --id-label devcontainer.config_file=/Users/me/Documents/GitHub/alits/.devcontainer/devcontainer.json --log-level debug --log-format json --config /Users/me/Documents/GitHub/alits/.devcontainer/devcontainer.json --default-user-env-probe loginInteractiveShell --mount type=volume,source=vscode,target=/vscode,external=true --skip-post-create --update-remote-user-uid-default on --mount-workspace-git-root --include-configuration --include-merged-configuration
				  Exit code 1
				  ```
		- [[Docker/CLI/ps/-a]]
			- ```
			  $> docker ps -a
			  CONTAINER ID   IMAGE                COMMAND                  CREATED          STATUS                            PORTS     NAMES
			  ba8901b9aeaf   alits-node           "/bin/sh -c 'echo Co…"   18 minutes ago   Exited (127) About a minute ago             alits-node-1
			  ```
		- [[Docker/CLI/logs]]
			- ```
			  ocker logs ba8901b9aeaf
			  Container started
			  
			  > dev
			  > turbo dev
			  
			  sh: 1: turbo: not found
			  Container started
			  
			  > dev
			  > turbo dev
			  
			  sh: 1: turbo: not found
			  Container started
			  
			  > dev
			  > turbo dev
			  
			  sh: 1: turbo: not found
			  Container started
			  
			  > dev
			  > turbo dev
			  
			  sh: 1: turbo: not found
			  ```
		- Ok, so the problem is that `turbo` - that is, [[turborepo]] - is not found inside the container.
			- I see that the [[Docker/Dockerfile]] has `CMD ["npm", "run", "dev"]`,
				- [[GitHub/aptrn/maxmsp-ts-library-template]] mentions `pnpm`, but npm should work just as good
				- it's calling `turbo build`. we don't yet have turborepo installed
			- [[GitHub/zsteinkamp/m4l-typescript-base]] has this in the package.json/scripts/dev:
				- `yarn install --frozen-lockfile && yarn tsc --watch`
				- so we could probably do something similar, installing inside of the dev command. but that seems a bit wasteful, since docker build could do the installation for us.
			- #Discovered [[StackOverflow/How do I make pnpm work as intended in a vscode dev container?]] from [[2023/09]] which has significant debugging work needed to get [[pnpm]] working with [[VSCode/Dev Container]]s.
				- Conclusion: it's more trouble than it's worth. I was just trying to use pnpm because it was already baked into the template.
		- Struggled with this for a few more hours.
			- [[Reddit/node/PNPM devcontainer multiple project setup]]
				- see also [PNPM devcontainer multiple project setup](https://gist.github.com/PatrickChoDev/81d36159aca4dc687b8c89983e64da2e) [[GitHub/Gist]]
		- tried this
			- https://github.com/npm/cli/issues/8075#issuecomment-2627424610
				- Relevant/related issues:
				- [Newly published versions of package managers distributed from npm cannot be installed due to key id mismatch nodejs/corepack#612](https://github.com/nodejs/corepack/issues/612)
				- [Installing pnpm 10.1.0 on windows fails with `cannot find matching keyid` pnpm/pnpm#9014](https://github.com/pnpm/pnpm/issues/9014)
				  
				  See also this [nodejs/corepack#616 (comment)](https://github.com/nodejs/corepack/issues/616#issuecomment-2622079955) for the rundown. In particular:
				  
				  > The workarounds are to set the environment variable `COREPACK_INTEGRITY_KEYS=0`, to manually update to `corepack@0.31.0` or to install it using knowledge of the release's hash.
				  
				  You can manually update corepack by running `npm install -g corepack@latest`.
				  
				  (If you'd rather "install it using knowledge of the release's hash", see his other comment here: [nodejs/corepack#612 (comment)](https://github.com/nodejs/corepack/issues/612#issuecomment-2622669686) : run `npm view npm@11.1.0 dist.shasum` to get the hash.)
				- [Newly published versions of package managers distributed from npm cannot be installed due to key id mismatch nodejs/corepack#612](https://github.com/nodejs/corepack/issues/612)
				-
			- https://github.com/pnpm/pnpm/issues/7727#issuecomment-2377433810
		- I keep getting `node-1  | ? The modules directories will be removed and reinstalled from scratch. Proceed? (Y/n) ‣ • Packages in scope: @my-username/my-library, maxmsp-test` when I try to do docker-compose up
		- [Non-Interactive pnpm install --no-optional hangs without --config.confirmModulesPurge=false · Issue #6778 · pnpm/pnpm](https://github.com/pnpm/pnpm/issues/6778)
-