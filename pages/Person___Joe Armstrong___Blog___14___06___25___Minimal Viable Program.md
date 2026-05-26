created-by:: [[Person/Joe Armstrong]]
source-link:: https://joearms.github.io/published/2014-06-25-minimal-viable-program.html
date-created:: [[2014/06/25]]
logseq-entity:: [[Logseq/Entity/Article]]
alias:: [[Minimal Viable Program]]

- # [Minimal Viable Program](https://joearms.github.io/published/2014-06-25-minimal-viable-program.html)
	- Author: **[[Person/Joe Armstrong]]**
	- ## Summary
		- Joe Armstrong defines a minimal viable program as the smallest program that solves a particular problem with no non-essential features.
		- His example is a tiny Erlang-era ticketing system built from numbered text files, version control, and a few shell scripts, arguing that extreme simplicity is a major reason such tools remain understandable and durable.
	- ## Notes
		- Removing a necessary feature would make the program useless; adding extra features would make it less minimal without making it more essential.
		- The ticket system centered on one command to create a new ticket file, with reporting delegated to simple shell tooling.
		- The piece is a useful precedent for terminal-native, text-file-oriented tools that prefer leverage from the surrounding Unix environment over application-level complexity.
	- ## Links
		- [[tk]]