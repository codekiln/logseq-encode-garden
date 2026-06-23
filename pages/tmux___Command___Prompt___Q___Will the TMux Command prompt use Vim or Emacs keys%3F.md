logseq-entity:: [[Logseq/Entity/Card]], [[Logseq/Entity/Question]]

- # Will the [[tmux/Command/Prompt]] use [[vim]] or [[Emacs]] style key bindings by default? What determines that?  [[card]]
  card-last-interval:: 3.69
  card-repeats:: 1
  card-ease-factor:: 2.36
  card-next-schedule:: 2026-06-27T01:48:05.235Z
  card-last-reviewed:: 2026-06-23T09:48:05.235Z
  card-last-score:: 3
	- [[Answer/Official]] from [Getting Started](https://github.com/tmux/tmux/wiki/Getting-Started#the-command-prompt)
		- > By **default**, the command prompt uses keys similar to emacs(1); however, if the `VISUAL` or `EDITOR` environment variables are set to something containing `vi` (such as `vi` or `vim` or `nvi`), then *vi(1)*-style keys are used instead.
	- [[My Notes]]
		- The implication is that adding `EDITOR=vim` to your [[Bash/.bash_profile]] or related file on a remote server is the easiest way to kick tmux into vi mode permanently. Or, if you can't edit that, `export EDITOR=vim`.