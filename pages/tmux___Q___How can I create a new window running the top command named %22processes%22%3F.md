logseq-entity:: [[Logseq/Entity/Question]], [[Logseq/Entity/Card]]

- # How can I create a new window running the top command named "processes"? [[card]]
	- in the [[tmux/Command/Prompt]]:
		- [[tmux/Command/new-window/-n]] process "top"
			- e.g.. `C-b : new-window -n processes "top"`
		- after this, if you press ctrl+c, it will close the window, too.