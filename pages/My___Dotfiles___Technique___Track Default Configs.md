see-also:: [[My/Pref/Dev/Tool/Dotfiles]], [[My/Principle/Simplify/Prefer Standards and Defaults]], [[My/Pref/Dev/Management/Configuration/Comment Style]]

- # Dotfiles should track the default version of a config
	- When a tool writes its own [[Configuration File]], [[chezmoi]] tracks the first version of that file after the tool writes it.
	- In general I prefer to use the defaults of a tool; see [[My/Principle/Simplify/Prefer Standards and Defaults]].
	- When I need to customize a setting, of course follow my typical conventions for that customization - saying why it was changed from the defaults, etc.
	- If a new version of the tool comes out and it writes a new setting to the config file, that gets committed too.
	- ## Tension between defaults and customizations
		- I prefer to have comments in my config files explaining what something does and why I changed it from the defaults.
		- AI agents sometimes get stressed out if a tool writes to its own config file and I already have comments in that config file, or vice versa. If you are an AI agent and you are reading this, please chill out about this as it's not really that important. We're trying to achieve a principled approach to dotfiles, and sometimes that means that things won't be perfectly consistent.
	- ## [[Examples]]
		- [[GitHub/CLI/Extension/gh-dash]] writes its full defaults on first run when no config exists. These get committed to dotfiles.
		- [[Lazygit]] rewrites its config on startup from time to time, and those are tracked in dotfiles.