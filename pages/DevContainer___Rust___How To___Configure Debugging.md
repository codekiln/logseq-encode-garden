tags:: [[DevContainer]], [[Rust]], [[Debug]], [[Docker]], [[Diataxis/How To]]

- # How To Configure Rust Debugging in DevContainers
	- ## Overview
		- This guide explains how to configure Rust debugging in Docker-based DevContainers by enabling the necessary Linux capabilities and security settings.
		- Rust uses a ptrace-based debugger (like GDB or LLDB) which requires special permissions to function inside containers.
	- ## Prerequisites
		- Docker or Docker Compose configured DevContainer
		- Rust development environment (can be added via DevContainer features)
		- Basic understanding of Docker security settings
	- ## Understanding the Problem
		- **Why Debugging Fails by Default**:
			- Rust debuggers use the `ptrace` system call to inspect and control running processes
			- Docker containers have restricted security settings by default that block `ptrace`
			- This prevents debuggers from attaching to processes inside the container
		- **Languages Affected**:
			- Rust (using GDB, LLDB, or CodeLLDB)
			- C++ (using GDB)
			- Go (using Delve)
			- Any language using ptrace-based debugging tools
	- ## Steps
		- ### 1. For Dockerfile-based DevContainers
			- Add `capAdd` and `securityOpt` to your `devcontainer.json`:
				- ~~~json
				  {
				    "name": "Rust Dev Container",
				    "image": "mcr.microsoft.com/devcontainers/rust:latest",
				    "capAdd": ["SYS_PTRACE"],
				    "securityOpt": ["seccomp:unconfined"],
				    "customizations": {
				      "vscode": {
				        "extensions": [
				          "rust-lang.rust-analyzer",
				          "vadimcn.vscode-lldb"
				        ]
				      }
				    }
				  }
				  ~~~
		- ### 2. For Docker Compose-based DevContainers
			- Add the capabilities to your service in `docker-compose.yml` or override file:
				- ~~~yaml
				  version: '3'
				  services:
				    rust-dev:
				      image: rust:latest
				      cap_add:
				        - SYS_PTRACE
				      security_opt:
				        - seccomp:unconfined
				      volumes:
				        - .:/workspace:cached
				      command: /bin/sh -c "while sleep 1000; do :; done"
				  ~~~
			- Reference the service in your `devcontainer.json`:
				- ~~~json
				  {
				    "dockerComposeFile": ["docker-compose.yml"],
				    "service": "rust-dev",
				    "workspaceFolder": "/workspace"
				  }
				  ~~~
		- ### 3. Configure VS Code Debugger
			- Create or update `.vscode/launch.json` with Rust debugging configuration:
				- ~~~json
				  {
				    "version": "0.2.0",
				    "configurations": [
				      {
				        "type": "lldb",
				        "request": "launch",
				        "name": "Debug Rust Program",
				        "cargo": {
				          "args": [
				            "build",
				            "--bin=your-binary-name",
				            "--package=your-package-name"
				          ],
				          "filter": {
				            "name": "your-binary-name",
				            "kind": "bin"
				          }
				        },
				        "args": [],
				        "cwd": "${workspaceFolder}"
				      }
				    ]
				  }
				  ~~~
		- ### 4. Verify the Configuration
			- Rebuild the DevContainer (Command Palette: "Dev Containers: Rebuild Container")
			- Set a breakpoint in your Rust code
			- Start debugging (F5 or Debug > Start Debugging)
			- Verify the debugger attaches and hits breakpoints
	- ## Security Considerations
		- **Understanding the Permissions**:
			- `SYS_PTRACE`: Allows using ptrace to trace processes
			- `seccomp:unconfined`: Disables seccomp security filtering
		- **Security Implications**:
			- These settings reduce container security isolation
			- Only use in development containers, never in production
			- The container has more access to the host system's process information
		- **Alternatives**:
			- For production debugging, use application-level observability tools
			- Consider using `--cap-add=SYS_PTRACE` only (without `seccomp:unconfined`) for slightly better security
	- ## Troubleshooting
		- **Debugger won't attach**:
			- Verify capabilities are set: `docker inspect <container-id> | grep CapAdd`
			- Check security options: `docker inspect <container-id> | grep SecurityOpt`
			- Ensure VS Code CodeLLDB extension is installed
		- **Breakpoints not hit**:
			- Verify debug build is being used (not release build)
			- Check that debug symbols are enabled in `Cargo.toml`:
				- ~~~toml
				  [profile.dev]
				  debug = true
				  ~~~
		- **Permission denied errors**:
			- Rebuild the container to apply new security settings
			- Verify the user has necessary permissions inside the container
	- ## Related
		- [[DevContainer]]
		- [[DevContainer/Docker Compose/Concept/Using Docker Compose]]
		- [[Rust]]
		- [[VSCode/Extension/CodeLLDB]]
