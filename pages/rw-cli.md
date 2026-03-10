- [rw-cli](https://github.com/Scarvy/readwise-reader-cli) - An open-source Python CLI by Scarvy that interacts with the Readwise Reader API
	- ## Commands
		- ### `rw-cli list` - list items in [[Readwise/Reader]]
			- `rw-cli list --location new` - nice table. its width is based on the width of the terminal. But there are strange misalignments at every width, AFAICT.
			  collapsed:: true
				- ```
				  ┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
				  ┃               ┃               ┃             ┃               ┃         ┃            ┃    ⌛ Reading ┃      🕐 Last ┃
				  ┃ 🔖 Title      ┃ 👤 Author     ┃ 📁 Category ┃ 📋 Summary    ┃ 🏷 Tags  ┃ 🗺 Location ┃      Progress ┃       Update ┃
				  ┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
				  │ NVIDIA's AI   │ Latent.Space  │   ✉️ email   │ NVIDIA is     │ ❌ tags │   ⭐️ new   │          0.0% │   2026-03-10 │
				  │ Engineers:    │               │             │ working to    │         │            │               │              │
				  │ Agent         │               │             │ make AI tools │         │            │               │              │
				  │ Inference at  │               │             │ easy to use   │         │            │               │              │
				  │ Planetary     │               │             │ and fast by   │         │            │               │              │
				  │ Scale and     │               │             │ improving     │         │            │               │              │
				  │ Speed of      │               │             │ developer     │         │            │               │              │
				  │ Light — Nader │               │             │ experience    │         │            │               │              │
				  │ Khalil        │               │             │ and software. │         │            │               │              │
				  │ (Brev), Kyle  │               │             │ They focus on │         │            │               │              │
				  │ Kranen (D…    │               │             │ helping       │         │            │               │              │
				  │               │               │             │ people run    │         │            │               │              │
				  │               │               │             │ complex AI    │         │            │               │              │
				  │               │               │             │ models        │         │            │               │              │
				  │               │               │             │ quickly on    │         │            │               │              │
				  │               │               │             │ GPUs with     │         │            │               │              │
				  │               │               │             │ simple        │         │            │               │              │
				  │               │               │             │ clicks. Their │         │            │               │              │
				  │               │               │             │ work supports │         │            │               │              │
				  │               │               │             │ new AI agents │         │            │               │              │
				  │               │               │             │ and models at │         │            │               │              │
				  │               │               │             │ large scale   │         │            │               │              │
				  │               │               │             │ and high      │         │            │               │              │
				  │               │               │             │ speed.        │         │            │               │              │
				  │               │               │             │               │         │            │               │              │
				  │ [AINews]      │ AINews        │   ✉️ email   │ AI models can │ ❌ tags │   ⭐️ new   │          0.0% │   2026-03-09 │
				  │ Autoresearch: │               │             │ now train     │         │            │               │              │
				  │ Sparks of     │               │             │ smaller       │         │            │               │              │
				  │ Recursive     │               │             │ models by     │         │            │               │              │
				  │ Self          │               │             │ themselves,   │         │            │               │              │
				  │ Improvement   │               │             │ improving     │         │            │               │              │
				  │               │               │             │ their         │         │            │               │              │
				  │               │               │             │ performance   │         │            │               │              │
				  │               │               │             │ without human │         │            │               │              │
				  │               │               │             │ help. This    │         │            │               │              │
				  │               │               │             │ progress is   │         │            │               │              │
				  │               │               │             │ making AI     │         │            │               │              │
				  │               │               │             │ research      │         │            │               │              │
				  │               │               │             │ faster and    │         │            │               │              │
				  │               │               │             │ more          │         │            │               │              │
				  │               │               │             │ efficient,    │         │            │               │              │
				  │               │               │             │ with agents   │         │            │               │              │
				  │               │               │             │ optimizing    │         │            │               │              │
				  │               │               │             │ training and  │         │            │               │              │
				  │               │               │             │ code. New     │         │            │               │              │
				  │               │               │             │ tools and     │         │            │               │              │
				  │               │               │             │ updates also  │         │            │               │              │
				  │               │               │             │ help AI work  │         │            │               │              │
				  │               │               │             │ better in     │         │            │               │              │
				  │               │               │             │ coding,       │         │            │               │              │
				  │               │               │             │ document      │         │            │               │              │
				  │               │               │             │ analysis,     │         │            │               │              │
				  │               │               │             │ robotics, and │         │            │               │              │
				  │               │               │             │ memory tasks. │         │            │               │              │
				  │               │               │             │               │         │            │               │              │
				  │ Reclaiming    │ Joe Ryan      │ 📰️ article  │ Meritocracy   │ ❌ tags │   ⭐️ new   │        62.15% │   2026-03-09 │
				  │ Democracy     │               │             │ was meant to  │         │            │               │              │
				  │ From the      │               │             │ be fair but   │         │            │               │              │
				  │ Market        │               │             │ has made      │         │            │               │              │
				  │               │               │             │ inequality    │         │            │               │              │
				  │               │               │             │ worse and     │         │            │               │              │
				  │               │               │             │ hurt workers' │         │            │               │              │
				  │               │               │             │ dignity.      │         │            │               │              │
				  │               │               │             │ Money and     │         │            │               │              │
				  │               │               │             │ markets now   │         │            │               │              │
				  │               │               │             │ dominate      │         │            │               │              │
				  │               │               │             │ society, but  │         │            │               │              │
				  │               │               │             │ this hurts    │         │            │               │              │
				  │               │               │             │ community and │         │            │               │              │
				  │               │               │             │ fairness. We  │         │            │               │              │
				  │               │               │             │ need to       │         │            │               │              │
				  │               │               │             │ rethink how   │         │            │               │              │
				  │               │               │             │ we value      │         │            │               │              │
				  │               │               │             │ work,         │         │            │               │              │
				  │               │               │             │ technology,   │         │            │               │              │
				  │               │               │             │ and democracy │         │            │               │              │
				  │               │               │             │ to build a    │         │            │               │              │
				  │               │               │             │ better        │         │            │               │              │
				  │               │               │             │ future.       │         │            │               │              │
				  │               │               │             │               │         │            │               │              │
				  │ America is    │ Ruchir Sharma │ 📰️ article  │ The U.S.      │ ❌ tags │   ⭐️ new   │        97.67% │   2026-03-09 │
				  │ now one big   │               │             │ economy is    │         │            │               │              │
				  │ bet on AI     │               │             │ heavily       │         │            │               │              │
				  │               │               │             │ relying on    │         │            │               │              │
				  │               │               │             │ artificial    │         │            │               │              │
				  │               │               │             │ intelligence  │         │            │               │              │
				  │               │               │             │ (AI) to       │         │            │               │              │
				  │               │               │             │ overcome big  │         │            │               │              │
				  │               │               │             │ problems like │         │            │               │              │
				  │               │               │             │ labor         │         │            │               │              │
				  │               │               │             │ shortages and │         │            │               │              │
				  │               │               │             │ rising debt.  │         │            │               │              │
				  │               │               │             │ AI            │         │            │               │              │
				  │               │               │             │ investments   │         │            │               │              │
				  │               │               │             │ are driving   │         │            │               │              │
				  │               │               │             │ much of the   │         │            │               │              │
				  │               │               │             │ country's     │         │            │               │              │
				  │               │               │             │ growth and    │         │            │               │              │
				  │               │               │             │ stock market  │         │            │               │              │
				  │               │               │             │ gains in      │         │            │               │              │
				  │               │               │             │ 2025. If AI   │         │            │               │              │
				  │               │               │             │ fails to      │         │            │               │              │
				  │               │               │             │ deliver, the  │         │            │               │              │
				  │               │               │             │ U.S. economy  │         │            │               │              │
				  │               │               │             │ and markets   │         │            │               │              │
				  │               │               │             │ could face    │         │            │               │              │
				  │               │               │             │ serious       │         │            │               │              │
				  │               │               │             │ trouble.      │         │            │               │              │
				  └───────────────┴───────────────┴─────────────┴───────────────┴─────────┴────────────┴───────────────┴──────────────┘
				  ```
			- `rw-cli list --location new --layout list --num-results-3` - gives a center justified list of [[Readwise/Reader]] locations.
			  collapsed:: true
				- ```
				  ~  rw-cli list --location new --layout list --num-results 3
				                ────────────────────────────────────────────────────────────────────────────────────────
				  
				                NVIDIA's AI Engineers: Agent Inference at Planetary Scale and Speed of Light —      0.0%
				                Nader Khalil (Brev), Kyle Kranen (D…
				  
				                NVIDIA is working to make AI tools easy to use and fast by improving developer 2026-03-1
				                experience and software. They focus on helping people run complex AI models
				                quickly on GPUs with simple clicks. Their work supports new AI agents and
				                models at large scale and high speed.
				  
				                ❌ No tags
				  
				                ────────────────────────────────────────────────────────────────────────────────────────
				  
				                [AINews] Autoresearch: Sparks of Recursive Self Improvement                         0.0%
				  
				                AI models can now train smaller models by themselves, improving their          2026-03-1
				                performance without human help. This progress is making AI research faster and
				                more efficient, with agents optimizing training and code. New tools and
				                updates also help AI work better in coding, document analysis, robotics, and
				                memory tasks.
				  
				                ❌ No tags
				  
				                ────────────────────────────────────────────────────────────────────────────────────────
				  
				                Reclaiming Democracy From the Market                                              62.15%
				  
				                Meritocracy was meant to be fair but has made inequality worse and hurt        2026-03-0
				                workers' dignity. Money and markets now dominate society, but this hurts
				                community and fairness. We need to rethink how we value work, technology, and
				                democracy to build a better future.
				  
				                ❌ No tags
				  ```
			- surprisingly, there isn't an AI-optimized view / layout, like `rw-cli list --layout json` or `rw-cli list --layout yaml`
		-
	- ## [[My Notes]]
		- ### [[2026-03-10 Tue]]
			- got it working. It seems to work, though it could use some spit polish, and it's not quite optimized for AI use just yet in my opinion.
			- Issues
				- #### `rw-cli lib` is meant to give "library breakdown" but it yields a pydantic error
				  collapsed:: true
					- ```
					  readwise_reader_cli/api.py", line 184, in list_documents
					      DocumentInfo(**doc_info)
					      ...
					  pydantic_core._pydantic_core.ValidationError: 1 validation error for DocumentInfo
					  category
					    Input should be 'article', 'email', 'rss', 'highlight', 'note', 'pdf', 'epub', 'tweet' or 'video' [type=enum, input_value='podcast', input_type=str]
					      For further information visit https://errors.pydantic.dev/2.12/v/enum
					  ```
				- #### all commands have usage that lists `rw-cli-unwrapped`
					- not a big deal, just a bit unpolished.
					- ```
					   ~  rw-cli lib --help
					  Usage: rw-cli-unwrapped lib [OPTIONS]
					  
					    Library breakdown
					  
					  Options:
					    -V, --view [category|location|tags]
					    --help                          Show this message and exit.
					  ```
				- ### `rw-cli lib --view location` yields pydantic error
					- ```
					   File "/nix/store/h1a52s59dj98dyv2yplwj7gcjyvxdvwi-readwise-reader-cli-0.0.1-unstable-2026-03-09/lib/python3.13/site-packages/readwise_reader_cli/api.py", line 184, in list_documents
					      DocumentInfo(**doc_info)
					      ...
					  pydantic_core._pydantic_core.ValidationError: 1 validation error for DocumentInfo
					  category
					    Input should be 'article', 'email', 'rss', 'highlight', 'note', 'pdf', 'epub', 'tweet' or 'video' [type=enum, input_value='podcast', input_type=str]
					      For further information visit https://errors.pydantic.dev/2.12/v/enum
					  ```
				-