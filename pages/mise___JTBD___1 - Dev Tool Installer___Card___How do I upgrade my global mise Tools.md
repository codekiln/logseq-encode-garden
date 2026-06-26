logseq-entity:: [[Logseq/Entity/Card]]

- # How do I upgrade my global mise Tools
	- [[mise]] [[mise/JTBD/1 - Dev Tool Installer]]
		- **How do I upgrade my global [[mise/Tool]]s?** [[Card]]
		  card-last-interval:: 4.28
		  card-repeats:: 2
		  card-ease-factor:: 2.7
		  card-next-schedule:: 2026-06-30T13:17:19.179Z
		  card-last-reviewed:: 2026-06-26T07:17:19.179Z
		  card-last-score:: 5
			- Just use [[mise/upgrade]].
			- [[My Notes]]
				- AFAIK there's no dedicated global upgrade subcommand that just upgrades global mise tools, but there might be a way to call a command only on a particular (global) [[mise/Config/mise.toml]]
				- Initially I thought you had to be in a directory that didn't have a local [[mise/Config/mise.toml]] to upgrade just the global tools, but then I asked [[mise/Q/Will calling mise upgrade in a directory that has a local mise.toml upgrade global mise Tools?]] and realized that it does actually upgrade global dependencies even if you are in a directory with a local mise config.