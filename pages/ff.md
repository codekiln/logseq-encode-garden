logseq-entity:: [[Logseq/Entity/Software/Project]]
tags:: [[Task/Management/Git-Friendly]]

- # [ff](https://github.com/ff-notes/ff)
	- Distributed note taker and task manager using RON [[CRDT]]s.
	- it's pretty bare-bones:
		- ```
		  $ ff
		  Actual:
		    * buy milk
		      id 458a1456lrc-12z3opnykw, start 2018-01-10
		    * learn Haskell
		      id 459h2tqxutq-24nuhr86ae, start 2018-01-14
		  ```
	- ## [[Data/Model]]
		- Where stored:
			- **Personal mode**: configured via `ff config dataDir`; config is in XDG config at `ff/config.yaml` unless project mode applies.
			- **Project mode**: if run inside a Git repo, it creates/uses `.ff` in that repo. README example shows after `ff add`, the repo contains `.ff .git`, and you commit `.ff`.
		- On disk it appears collection-oriented, like:
			- ```
			  .ff/
			  config.yaml
			  note/
			    <RON-doc-id>
			  tag/
			    <RON-doc-id>
			  contact/
			    <RON-doc-id>
			  tag_group/
			    <RON-doc-id>
			  ```
		- Core entities in [ff-core/lib/FF/Types.hs](https://github.com/ff-notes/ff/blob/a10a66014e6f2c788f595863c65cd2af859d0e69/ff-core/lib/FF/Types.hs):
			- `Note`
				- `status`: `Active`, `Archived`, or `Wiki`
				- `text`: mergeable `RgaString`
				- `start`, `end`: dates
				- `tags`: set of `Tag` refs
				- `track`: external issue-tracking metadata
				- `links`: set of `Link` refs
				- `recurring`: bool
			- `Tag`
				- `text`
				- `desc`
			- `Contact`
				- `status`
				- `name`
			- `TagGroup`
				- `name`
				- `exclusive`
				- `member` set
			- `Link`
				- `target`: note ref
				- `type`: currently `SubNote` for [[Hierarchy]]
	- ## [[My Notes]]
		- no dependency tracking per se, but it does include a parent/child model
		- as of [[2026-05-26 Tue]], has ~200 [[Github/Star]]s
	- ## [[Engineering Choices]]
		- written in [[Haskell]]
	- ## [[Installation]]
		- ### Getting the [[Executable]]