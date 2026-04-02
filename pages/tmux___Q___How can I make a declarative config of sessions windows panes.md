tags:: [[Question]]

- I'd like to be able to have predefined tmux sessions, windows, and panes, all renamed and ready to go. Can I do this with tmux, something kind of like IaC but for shells?
	- [[My Notes]]
		- I saw that [[Username/typecraft]] had an example of implementing something like this in his [[Person/Chris Power/GitHub/dotfiles]] for tmux.  Unfortunately, it was kind of cobbled together, but it looked like it worked for him.
	- [[AI/Response]]
		- Nix users approach declarative tmux in a few distinct ways, depending on how "pure" and reproducible they want the environment to be. Below is a structured map of the ecosystem.
		- ## 1. Home Manager: Declarative `tmux` as a First-Class Module
			- [[Nix/home-manager]], [[tmux]]
			- This is the most common Nix-native approach. Home Manager exposes:
			- ~~~nix
			  programs.tmux = {
			  enable = true;
			  terminal = "tmux-256color";
			  baseIndex = 1;
			  keyMode = "vi";
			  extraConfig = ''
			    set -g mouse on
			    set -g history-limit 100000
			  '';
			  };
			  ~~~
			- ### What this gives you
				- Fully declarative `.tmux.conf`
				- Version-controlled configuration
				- Reproducible across machines
				- Automatic install of tmux
			- ### What it does NOT give you
				- Declarative sessions
				- Predefined windows/panes
				- Layout orchestration
			- Home Manager solves **configuration-as-code**, not **session topology-as-code**.
		- ## 2. Nix-Wrapped `tmuxp` / `teamocil`
			- [[tmuxp]], [[teamocil]]
			- Very common in Nix setups: package tmuxp via Nix, store YAML specs in repo, expose them as `flake apps`. Example:
			- ~~~
			  {
			  apps.dev = {
			    type = "app";
			    program = "${pkgs.tmuxp}/bin/tmuxp load ./tmux/dev.yaml";
			  };
			  }
			  ~~~
			- Now: `nix run .#dev`. This is extremely clean: layout spec lives in repo, environment defined by Nix, tmux topology defined by YAML, launch command reproducible. This is probably the most popular pattern among Nix users who want topology-as-code.
		- ## 3. Nix DevShell + Bootstrap Script Pattern
			- Very common in flake-based projects. Example:
			- ~~~
			  devShells.default = pkgs.mkShell {
			  packages = with pkgs; [ tmux ];
			  shellHook = ''
			    if [ -z "$TMUX" ]; then
			      tmux new-session -A -s dev
			    fi
			  '';
			  };
			  ~~~
			- Or:
			- ~~~
			  shellHook = ''
			  if ! tmux has-session -t dev 2>/dev/null; then
			    ./scripts/tmux-bootstrap.sh
			  fi
			  '';
			  ~~~
			- ### Pattern
				- DevShell ensures tools
				- Bootstrap script ensures layout
				- Entire environment reproducible
			- This is lightweight and very common.
		- ## 4. Pure Nix-Generated tmux Layouts
			- Advanced users sometimes: generate `.tmux.conf` from Nix, generate startup scripts via `writeShellScriptBin`, compose layouts as Nix expressions. Example:
			- ~~~
			  pkgs.writeShellScriptBin "dev-session" ''
			  tmux new-session -d -s dev -n editor
			  tmux split-window -h
			  tmux attach -t dev
			  ''
			  ~~~
			- This is full "Infrastructure-as-Code" purity: no YAML, layout logic expressed in Nix, can parameterize sessions. You can even abstract layout builders as functions.
		- ## 5. `direnv` + `nix-direnv` + Auto Sessions
			- [[direnv]]
			- A pattern seen in serious Nix workflows: `direnv` loads flake devShell automatically, devShell runs tmux bootstrap, entering a directory = full environment + session topology. Effect: `cd project/` → nix env loads → tmux session auto-creates. This creates project-scoped tmux infrastructure.
		- ## 6. `nixos` System-Level tmux Orchestration
			- On NixOS: tmux can be configured globally, login shells can auto-start sessions, systemd user services can launch tmux sessions. Example pattern:
			- ~~~
			  systemd.user.services.dev-tmux = {
			  Service.ExecStart = "${pkgs.tmux}/bin/tmux new -A -s dev";
			  };
			  ~~~
			- Less common, but possible.
		- ## 7. Emerging Pattern: Devcontainers + Nix + tmux
			- Among developers combining flakes, Devcontainers, and reproducible shells. Common approach: Devcontainer ensures OS-level environment, flake ensures tools, flake app launches tmux topology. You effectively get: container-as-code, environment-as-code, terminal topology-as-code. Very close to "ephemeral workstation provisioning."
		- ## What Nix Users Typically Optimize For
			- From observed patterns:
			- | Goal | Solution |
			  | ---- | ---- |
			  | Reproducible tools | devShell |
			  | Reproducible config | Home Manager |
			  | Reproducible layout | tmuxp or bootstrap script |
			  | Project isolation | direnv + flake |
			  | Full purity | Nix-generated shell scripts |
		- ## If You Want Maximum Declarative Control
			- For someone building agent-first, reproducible workflows:
			- ### Clean architecture
				- ~~~
				  flake.nix
				  tmux/
				  dev.yaml
				  scripts/
				  bootstrap.sh
				  ~~~
				- Flake: provides tools, exposes `apps.dev`. App: calls tmuxp, loads YAML. This gives you: version-controlled session topology, parameterizable sessions, reproducible execution, works locally + Codespaces.
		- ## There Is No "Official" Nix-native tmux Layout DSL
			- Important insight: Nix does not have a first-class tmux session module. Most people layer one of: tmuxp, shell bootstrap scripts, flake apps. That's the current state of the ecosystem.
		- If you'd like, I can: design a Nix-native layout abstraction function, show a flake pattern tailored to multi-agent coding, or sketch a declarative tmux DSL in Nix that compiles to tmux commands.