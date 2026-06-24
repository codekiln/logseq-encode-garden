logseq-entity:: [[Logseq/Entity/Card]], [[Logseq/Entity/Term]]
alias:: [[chezmoi/Concept/Target/State]]
tags:: [[chezmoi/Concept]]

- # What does the [[Term]] *target state* mean in [[chezmoi]]? [[card]]
  card-last-interval:: 4
  card-repeats:: 2
  card-ease-factor:: 2.22
  card-next-schedule:: 2026-06-28T07:20:22.829Z
  card-last-reviewed:: 2026-06-24T07:20:22.829Z
  card-last-score:: 3
	- ## [[My Answer]]
		- The *target state* of a [[chezmoi/Target]] is the chezmoi-computed runtime value that answers: Given the value of the target file [[Declared]] in the [[dotfiles repo]] and the chezmoi configuration, what file contents **should chezmoi write** to the [[Home/Dir]]? It depends on [[chezmoi/.toml]], [[EnvVar]]s, etc.
		- ### [[Example]]
			- For the *target state* of the [[zsh/.zshrc]], is the [[Declared]] representation of `dot_zshrc.tmpl`, including everything configured about chezmoi, such as aspects of [[chezmoi/.toml]] such as how to handle templates, what context variables there are, the values of environment variables, etc.
		- ### Why it matters
			- If the *target state* is different than the [[chezmoi/Destination/State]] for a [[chezmoi/Target]], then the next [[chezmoi/apply]] of that target will change the destination file to match the [[Declared]] representation of that file.
		- ### It's a runtime construct or computational construct
			- *Target State* as a term exists in chezmoi because a core assumption of how chezmoi is that people want to use [[Templating]] to manage their dotfiles.
			- The *target state* of [[chezmoi/Target]] isn't just the contents of a particular file in the dotfiles repo. Well, technically, it could be, if it's literally just a file without any templating. But chezmoi has a runtime state that's influenced by its configuration files, environment variables, etc, and that runtime state potentially changes the interpretation of each target file.
	- ## [[Their Answer]]
		- The *target state* is the **desired** state of the [[chezmoi/Destination/Directory]]. It is computed from the source state, the [[chezmoi/.toml]] config file, and the [[chezmoi/Destination/State]]. The target state includes regular files and directories, and may also include symbolic links, scripts to be run, and targets to be removed.
	- [[My Notes]]
		- This is like [[Math/Projection]]
		- [[Confused]] because I just did the flashcard for [[chezmoi/Source/State]] and it seems like it's the same thing?