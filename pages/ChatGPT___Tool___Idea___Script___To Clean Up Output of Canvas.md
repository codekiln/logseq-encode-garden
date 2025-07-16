# script to clean up `NNBSP` and other garbage characters from documents produced by #ChatGPT
	- ## prior art
		- [Humanize Your AI Text in One Click for Free](https://humanize-ai.click/)
			- replaces the wrong thing
			- not a script - online tool
		- [[Person/unixwzrd/GitHub/UnicodeFix]] https://unixwzrd.ai/
			- Code
				- [UnicodeFix/bin/cleanup-text.py at main · unixwzrd/UnicodeFix](https://github.com/unixwzrd/UnicodeFix/blob/main/bin/cleanup-text.py)
			- [[Person/unixwzrd/Project/Unicodefix]] [UnicodeFix | Distributed Thinking Systems](https://unixwzrd.ai/projects/UnicodeFix/)
				- ## What UnicodeFix Does
				  id:: 6876be2b-ce70-4ad0-9048-ee5a712a86ac
					- Converts smart quotes, em-dashes, en-dashes, ellipses, and other punctuation into standard ASCII equivalents
					- Removes invisible or disruptive Unicode characters, including:
					- `U+200B` (Zero-Width Space)
					- `U+200C` (Zero-Width Non-Joiner)
					- `U+200D` (Zero-Width Joiner)
					- `U+2018` (Left Single Quotation Mark ‘ )
					- `U+2019` (Right Single Quotation Mark ’ )
					- `U+201C` (Left Double Quotation Mark “ )
					- `U+201D` (Right Double Quotation Mark ” )
					- `U+2013` (En Dash – )
					- `U+2014` (Em Dash — )
					- `U+2026` (Horizontal Ellipsis … )
					- Cleans AI-generated, copied, or web-sourced content to prevent downstream parsing errors
					- Reduces risks when working across editors, file formats, and systems
					  
					  **Bonus Trouble makers**
					- `U+FEFF` (Byte Order Mark, BOM) — invisible but can totally screw up parsing in some languages.
					- `U+00A0` (Non-Breaking Space) — looks like a regular space but acts differently in many contexts.
	- ## observations
		- perhaps having a tool like [[Py/Lib/black]] but for [[Markdown]] would be best; [[ChatGPT/Tool/Idea/Script/To Clean Up Output of Canvas/Report]] summarizes these
		-