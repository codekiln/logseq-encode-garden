## [[Why]]
	- runtime checks can be forgotten or skipped under pressure; compile-time type constraints cannot
	- making invariants part of the data model shifts enforcement from "every callsite must check" to "the type guarantees it"
	- bugs from illegal state are often the hardest to reproduce because they depend on a particular sequence of mutations
- ## origin
	- phrase coined by [[@yminsky]] ([[Yaron Minsky]]) in the context of [[OCaml]] at [[Jane Street]]
	- popularized further in the [[Elm]] and [[Haskell]] communities
- ## source
	- [[Person/Yaron Minsky/Talk/Effective ML]] ([~18 min](https://youtu.be/-J8YyfrSwTk?t=1081))