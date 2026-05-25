alias:: [[chezmoi/Concept/Source/Directory]]
tags:: [[chezmoi/Concept]]

- # What is the Chezmoi *Source Directory*? [[card]]
	- ## [[My Answer]]
		- It's the [[dotfiles repo]] directory on disk that contains the [[Declarative]] chezmoi representation of what you want your [[dotfiles]] to be.
	- ## [[Their Answer]]
		- According to [[chezmoi/Ref/Concepts]], it's
			- > where chezmoi stores the [[chezmoi/Concept/Source/State]]. By default it is `~/.local/share/chezmoi`
		- According to [[chezmoi/User Guide/Setup]],
			- > The *source directory*, `~/.local/share/chezmoi`, is common to all your machines, and is a clone of your dotfiles repo. Each file that chezmoi manages has a corresponding file in the source directory.
		- [[My Notes]]
			- Their answer is confusing and not intuitive to me.
			- I'm not sure if I'm using it wrong, I wouldn't prefer to store my dotfiles repo in `~/.local/share/chezmoi`. Furthermore, if I `ls -la ~/.local/share`, I don't see `chezmoi` there, and I'm not sure why I don't.
			- I get the sense that this is the default because one can apply an arbitrary github repo in chezmoi.