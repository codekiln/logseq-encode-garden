- [TOON | Token-Oriented Object Notation](https://toonformat.dev/)
	- A compact, human-readable encoding of the JSON data model for LLM prompts.
	- [Format Overview | TOON](https://toonformat.dev/guide/format-overview.html)
	- [Benchmarks | TOON](https://toonformat.dev/guide/benchmarks.html)
		- looks fairly performant!
			- ```
			  claude-haiku-4-5-20251001
			  → TOON           ████████████░░░░░░░░    59.8% (125/209)
			    JSON           ███████████░░░░░░░░░    57.4% (120/209)
			    YAML           ███████████░░░░░░░░░    56.0% (117/209)
			    XML            ███████████░░░░░░░░░    55.5% (116/209)
			    JSON compact   ███████████░░░░░░░░░    55.0% (115/209)
			    CSV            ██████████░░░░░░░░░░    50.5% (55/109)
			  
			  gemini-2.5-flash
			  → TOON           ██████████████████░░    87.6% (183/209)
			    CSV            █████████████████░░░    86.2% (94/109)
			    JSON compact   ████████████████░░░░    82.3% (172/209)
			    YAML           ████████████████░░░░    79.4% (166/209)
			    XML            ████████████████░░░░    79.4% (166/209)
			    JSON           ███████████████░░░░░    77.0% (161/209)
			  
			  gpt-5-nano
			  → TOON           ██████████████████░░    90.9% (190/209)
			    JSON compact   ██████████████████░░    90.9% (190/209)
			    JSON           ██████████████████░░    89.0% (186/209)
			    CSV            ██████████████████░░    89.0% (97/109)
			    YAML           █████████████████░░░    87.1% (182/209)
			    XML            ████████████████░░░░    80.9% (169/209)
			  
			  grok-4-fast-non-reasoning
			  → TOON           ███████████░░░░░░░░░    57.4% (120/209)
			    JSON           ███████████░░░░░░░░░    55.5% (116/209)
			    JSON compact   ███████████░░░░░░░░░    54.5% (114/209)
			    YAML           ███████████░░░░░░░░░    53.6% (112/209)
			    XML            ███████████░░░░░░░░░    52.6% (110/209)
			    CSV            ██████████░░░░░░░░░░    52.3% (57/109)
			  ```