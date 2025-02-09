- [[GitHub/codekiln/dev-container-test]]
- [[VSCode/Extension/QuickStage]] not installed
- one of the reasons I created this test repo was to see if I could reproduce the issue I saw [[2025-02-08 Sat]] in [[GitHub/codekiln/alits]] where QuickStage wasn't installed, even though I had it in my [[VSCode/Dev Container/.devcontainer.json]] file. Sure enough, this minimal test repo does reproduce it.
	- ```
	  [6895 ms] Extensions cache, install extensions: dbaeumer.vscode-eslint, bs-code.git-quick-stage, ms-azuretools.vscode-docker, GitHub.vscode-pull-request-github
	  
	  [6895 ms] Extensions cache, install extensions: dbaeumer.vscode-eslint, bs-code.git-quick-stage, ms-azuretools.vscode-docker, GitHub.vscode-pull-request-github
	  [6895 ms] Start: Run in container: test -d /home/node/.cursor-server/extensionsCache && ls /home/node/.cursor-server/extensionsCache || true
	  [6896 ms] 
	  [6896 ms] 
	  [6896 ms] Start: Run in container: test -d /vscode/cursor-server/extensionsCache && ls /vscode/cursor-server/extensionsCache || true
	  [6896 ms] 
	  [6896 ms] 
	  [6896 ms] Extensions cache, link in container: None
	  [6897 ms] Start: Run in container: /home/node/.cursor-server/bin/f5f18731406b73244e0558ee7716d77c8096d150/bin/cursor-server --log debug --force-disable-user-env --server-data-dir /home/node/.cursor-server --use-host-proxy --telemetry-level all --accept-server-license-terms --host 127.0.0.1 --port 0 --connection-token-file /home/node/.cursor-server/data/Machine/.connection-token-f5f18731406b73244e0558ee7716d77c8096d150 --extensions-download-dir /home/node/.cursor-server/extensionsCache --install-extension dbaeumer.vscode-eslint --install-extension bs-code.git-quick-stage --install-extension ms-azuretools.vscode-docker --install-extension GitHub.vscode-pull-request-github --start-server --disable-websocket-compression --skip-requirements-check
	  [6963 ms] userEnvProbe PATHs:
	  Probe:     '/usr/local/share/nvm/current/bin:/usr/local/share/npm-global/bin:/pnpm:/usr/local/share/nvm/current/bin:/usr/local/share/npm-global/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/node/.local/bin'
	  Container: '/pnpm:/usr/local/share/nvm/current/bin:/usr/local/share/npm-global/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
	  
	  [7980 ms] [09:19:18] Extension 'bs-code.git-quick-stage' not found.
	  Make sure you use the full extension ID, including the publisher, e.g.: ms-dotnettools.csharp
	  
	  
	  
	  [15991 ms] [09:19:26] Extension 'dbaeumer.vscode-eslint' v3.0.10 was successfully installed.
	  [09:19:26] Extension 'github.vscode-pull-request-github' v0.102.0 was successfully installed.
	  [09:19:26] Extension 'ms-azuretools.vscode-docker' v1.29.4 was successfully installed.
	  [15992 ms] [09:19:26] Error: Failed Installing Extensions: bs-code.git-quick-stage
	      at Kc.installExtensions (file:///vscode/cursor-server/bin/linux-arm64/f5f18731406b73244e0558ee7716d77c8096d150/out/server-main.js:71:35452)
	  ```
- I pushed up the repo to [codekiln/dev-container-test: testing a simple dev container](https://github.com/codekiln/dev-container-test/tree/main), now I'd like to contact the QuickStage plugin author, [[GitHub/Bluesteel-Software]]
	- I looked through [git-stage-file/extension.js at main · Bluesteel-Software/git-stage-file](https://github.com/Bluesteel-Software/git-stage-file/blob/main/extension.js) and it looks remarkably easy to create a [[VSCode/Extension]]; I'll have to do that sometime.
	-