tags:: [[chezmoi/Command]]

- # [chezmoi add](https://www.chezmoi.io/reference/commands/add/)  *target...*
	- ## What will `chezmoi add ~/.config/mise/config.toml` do if that file exists as a chezmoi template already? [[card]]
		- it will interactively ask,
			- > adding `.config/mise/config.toml` would remove template attribute, continue?
		- this is because it doesn't know how to do the "reverse" of applying a template.
		- This is a big disadvantage of using [[chezmoi/Template]]