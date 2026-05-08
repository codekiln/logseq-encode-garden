tags:: [[CLI/Tool]]
logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Person/Ken'ichiro Oyama]]
via:: [[Person/Matan Kushner/GitHub/dotfiles]]

- # [gh/grep](https://github.com/k1LoW/gh-grep)
	- ## about
		- `gh grep` is a [[gh]] [[GitHub/CLI/Extension]] that prints lines matching a pattern in repositories via the [[GitHub/API]]
		- ### install
			- `$ gh extension install k1LoW/gh-grep`
	- ## slow without [[gh/grep/--include]]
		- it scans using the github API. The dev recommends specifying `--include`
			- {{embed [[gh/grep/--include]]}}
	- ## open matched lines in browser
		- only on [[MacOS]]
		- `$ gh grep 'ioutil\.' --include=**/*.go --owner k1LoW --repo ghput --url`