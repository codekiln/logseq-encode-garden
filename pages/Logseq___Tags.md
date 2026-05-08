# `tags::` frontmatter in Logseq
	- Tags receive special treatment in the Logseq UI before and as of [[Logseq/v/0/10/9]].
	- The tags frontmatter item may contain a comma delimited list of Logseq page references.
	- If PageA is tagged with PageB and PageC is also tagged with PageA, then PageA will list PageA and PageB in a list on the page, which is a convenient, informal way to represent set membership.
		- It might make more sense to use the more formal [[Logseq/Entity]] system, though.
	- Note: if `PageC` has an alias `IAmPageC` and `PageA` is tagged with `IAmPageC` instead of `PageC`, then `PageA` **would not contain** `IAmPageC`. It's unknown if this is a bug or an intentional implementation decision.