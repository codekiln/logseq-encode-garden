tags:: [[Diataxis/Concept]], [[Term]]
alias:: [[Progressive Disclosure]] 
see-also:: [[AI/LLM]], [[AI/LLM/Problem/Context Limit]], [[AI/Coding/Tool/Report/25/Skills Comparison]]

- # Progressive disclosure — conceptual overview
	- ## Overview
		- **Progressive disclosure** here means an agent loads **domain knowledge in stages**, pulling each layer from the environment only when it becomes relevant, instead of putting the full bundle into the model context up front
		- In Anthropic's **Agent Skills** design, that staging is explicit: lightweight **discovery metadata** stays always available; **procedural instructions** load when a skill matches the task; **extra guides, data, and code** load or run only as the workflow needs them[^1] [^2]
		- The goal is practical: keep the **context window** for reasoning focused on what matters for the current step while still allowing **large, composable** capability packs on disk
	- ## Context
		- **Bounded context**: Large language models operate under a fixed or costly context budget, so shipping entire playbooks, references, and scripts into every turn wastes capacity and dilutes attention
		- **Skills vs one-off prompts**: A long user or system prompt repeats the same guidance every conversation; filesystem-based skills are **reusable**, **discoverable**, and **loaded on demand**, which scales better as you add more specialties[^1]
		- **Why a VM and bash matter**: Skills are described as living in a **code-execution environment with filesystem access**. The agent can **read files** and **run scripts** like a developer opening the right section of an onboarding binder—navigation replaces preloading[^1]
	- ## Key Principles
		- **Separation of “that it exists” from “what it contains”**: The system can know many skills cheaply if only **names and trigger descriptions** sit in the always-on layer
		- **Match, then expand**: After the user’s intent aligns with a skill’s description, the agent pulls the **main instruction file**; unrelated skills never pay that token cost[^1]
		- **Depth on demand**: Follow-up files (guides, schemas, examples) and **executable utilities** participate only when instructions or the task point at them
		- **Different media, different costs**: Prose instructions are flexible; **deterministic scripts** can do reliable work; the doc emphasizes that **script source** need not flood the window if only **stdout or results** return[^1]
		- **Composition without context explosion**: Many skills can coexist as directories; **unused files on disk cost no tokens** until read[^1]
	- ## Mechanism
		- Anthropic's overview describes **three loading levels** for a typical skill directory[^1]:
			- **Level 1 — Metadata (always loaded)**: YAML frontmatter on the skill’s main markdown file (for example `name` and a rich `description` of what the skill does **and when to use it**) is included **at startup** so the model can choose skills without loading bodies[^1]
			- **Level 2 — Core instructions (loaded when triggered)**: The body of `SKILL.md` (workflows, conventions, steps) is read **via the shell** only after the skill is selected, so that text enters context **just for matching tasks**[^1]
			- **Level 3 — Bundled resources (as needed)**: Additional markdown, reference material, templates, and **scripts** are accessed **when referenced**; running a script can surface **only outputs** to the model rather than the full program text[^1]
		- **Illustrative flow** (PDF-oriented example from the same documentation): at startup the model sees a short **summary line** derived from metadata; when the user asks to extract text, the agent **reads** `SKILL.md`; if form filling is irrelevant, **optional** files such as a forms guide are **never read**; work proceeds from the loaded slice only[^1]
	- ## Examples
		- **Skill-shaped directory** (conceptual layout)[^1]:
			- ~~~
			  pdf-skill/
			    SKILL.md
			    FORMS.md
			    REFERENCE.md
			    scripts/
			      fill_form.py
			  ~~~
		- **Token posture** (order of magnitude from the doc's table): metadata on the order of **~100 tokens per skill** at baseline; main instructions often **under roughly five thousand tokens** when loaded; **large reference corpora** can remain on disk until a read pulls in a slice[^1]
	- ## Misconceptions
		- **“More installed skills always mean a bigger system prompt”** — Incorrect for this architecture: **many skills** can register through **compact descriptions**; cost spikes when a skill is actually **activated and read**[^1]
		- **“The agent must paste every script into context to use it”** — Misrepresents the documented pattern: **execution** can return **results or logs** without treating the whole source file as prompt text[^1]
		- **“Progressive disclosure is only marketing language”** — In this design it is **operational**: loading is **gated** on filesystem reads and tool use, not on a single static block of instructions[^1]
	- ## Footnotes
		- [^1]: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md
		- [^2]: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills