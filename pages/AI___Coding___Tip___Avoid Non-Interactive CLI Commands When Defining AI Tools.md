tags:: [[Latent Space/Pod/24/11/Erik Schluntz from Anthropic on SOTA Agents]]

- #Quote from [[Person/Erik Schluntz]] of [[Anthropic]] at 00:39:13: [Tool Use Prompt Engineering | 38sec snip from Latent Space: The AI Engineer Podcast](https://share.snipd.com/snip/58be7bf3-e57e-44b5-94dc-adff28ffc173)
	- > [It's important to have] ... iterations like that ... let us make the tool foolproof for the model
	- > ... if the model ... opens [[vim]], like, you know, **it's never going to return. And so the tool is stuck**. ... **the tool is just text in, text out. It's not interactive**.
	- > ... **it's not like the model doesn't know how to get out of vim**. It's that the way that the tool is *hooked up* to the computer **is not interactive**.
	- > ... basically, we just added instructions in the tool: "hey, **don't launch commands that don't return**."
- #notes *I've seen [[CursorAI/Agent]] get stuck in [[git]] commands because the pager was interactive*
	- See also [[StackOverflow/10/02/How do I prevent Git Diff from using a pager]]:
		- {{embed ((67c2dd1d-ac20-47e6-b5f8-cc816afb094f))}}