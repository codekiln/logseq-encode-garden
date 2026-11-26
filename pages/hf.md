logseq-entity:: [[Logseq/Entity/Software/Project]]

- # [hf](https://huggingface.co/docs/huggingface_hub/guides/cli)
	- `hf` is the command-line tool for the Hugging Face Hub. It ships inside the Python package [huggingface_hub](https://github.com/huggingface/huggingface_hub).
	- ## What I use it for
		- `hf auth login` stores an access token on the machine. A gated model, one whose license has to be accepted on its Hugging Face page, downloads only for a logged-in account that has accepted it.
		- `hf download <owner>/<model>` fetches a model's files into the shared cache at `~/.cache/huggingface/hub`, where the Python libraries look for them.
		- `hf version` prints the installed version.
	- ## Install
		- My dotfiles install it for every machine through [[mise]], as the tool `pipx:huggingface_hub` in the global [[mise/Config/mise.toml]].
