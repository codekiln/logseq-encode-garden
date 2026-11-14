logseq-entity:: [[Logseq/Entity/AI/Model]]
alias:: [[claude-fable-5-2]]
tags:: [[AI/Model]]
date-created:: [[2026-11-09 Mon]]

- # Claude Fable 5.2
	- {{embed [[Anthropic/Model/Claude/5/2/Fable/Doc/API]]}}
	- Successor to [[Anthropic/Model/Claude/5/1/Fable]]. Part of the [[Anthropic/Model/Claude]] 5 family with [[Anthropic/Model/Claude/5/5/Opus]], [[Anthropic/Model/Claude/5/5/Sonnet]] and [[Anthropic/Model/Claude/5/5/Haiku]]. [[Anthropic/Model/Claude/5/2/Mythos]] is the same model, open only to organizations in Anthropic's verification programs.
	- ## Where Anthropic says it does best
		- Anthropic describes Fable 5.2 as built "for demanding reasoning and long-horizon agentic work." Its examples are agent sessions that run for hours, multistep deep research, and analysis carried through to a finished document, spreadsheet or deck. Source: [Claude Fable 5.2 overview](https://platform.claude.com/docs/en/models/fable-5-2/overview), [Choosing the right model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)
		- Anthropic recommends Opus 5.5 as the starting model for most workloads, and Fable 5.2 when Opus 5.5 evals at `xhigh` or `max` effort still fall short. Source: [Choosing the right model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model), [What's new in Claude Fable 5.2](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2)
		- Coding: the launch post reports FrontierCode 2.0 at 49.1% (Opus 5.5: 45.5%) and FrontierSWE v2 at 69.9% (Opus 5.5: 62.3%). At `high` effort it scores about level with Opus 5.5 on FrontierCode at roughly half the cost per task. Anthropic ran or reported these figures itself. Source: [Introducing Claude Fable and Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2)
		- Agentic and computer-use work: the launch post reports Remote Labor Index 41.3% (Opus 5.5: 21.3%), OSWorld 2.1 89.3% (Opus 5.5: 87.2%) and Terminal-Bench-Science 74.6% (Opus 5.5: 58.7%). Source: [Introducing Claude Fable and Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2)
		- Science, mathematics and hardware: Anthropic reports Humanity's Last Exam with tools at 74.2% (Opus 5.5: 67.7%), a formalization of Fermat's Last Theorem by about 1,000 Fable 5.2 agents in 30 hours, and three electronic devices designed through to boards ready for manufacture. The prompting guide names scientific discovery and mathematics as the work where `max` effort makes most sense. Source: [Introducing Claude Fable and Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2), [Prompting Claude Fable 5.2](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2)
		- Long unattended runs and orchestration: the prompting guide says Fable 5.2 "works well on long-running asynchronous tasks," and early testers had good results using it to plan for and direct other models. Source: [Prompting Claude Fable 5.2](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2)
		- ### Limits and gaps in the sources
			- Every benchmark figure above comes from Anthropic. The launch post notes that the outside evaluators do not endorse its claims, and no independent scores are filed here yet.
			- The launch post shows Fable 5.2 behind other models on AutomationBench (51.4% vs. Gemini 4 Carbon 53.9%) and on AA-Briefcase Elo (1785 vs. Opus 5.5 1800).
			- Cybersecurity: Fable 5.2's safeguards "will block most cybersecurity-related tasks." Anthropic points security work to Mythos 5.2.
			- Writing: the launch post says testers found it communicates more clearly than earlier Fable models. The prompting guide rates its writing similar in clarity to Opus 5.5, so the sources support an improvement over Fable 5.1 and leave the comparison with Opus 5.5 even.
