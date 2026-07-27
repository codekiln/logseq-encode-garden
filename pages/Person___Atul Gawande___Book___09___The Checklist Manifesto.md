logseq-entity:: [[Logseq/Entity/Book]]
created-by:: [[Person/Atul Gawande]]
date-created:: [[2009]]

- # [The Checklist Manifesto](https://atulgawande.com/book/the-checklist-manifesto/)
	- ## About
		- Subtitle: *How to Get Things Right*. Published 2009 by Metropolitan Books. Argues that as knowledge and complexity outpace individual expertise, failures increasingly come not from ignorance but from ineptitude — not applying what we already know. The remedy is the humble checklist: a simple tool that catches the predictable, stupid mistakes and frees experts to handle the genuinely hard problems.
		- Draws examples from surgery, aviation, construction, and finance, culminating in Gawande's work on the WHO Surgical Safety Checklist.
	- ## What is a check?
		- Gawande never pins down a single *check* as a unit — his focus is the checklist as a design artifact. Read closely, an implicit definition emerges: a check is a bounded verification that a specific, high-consequence condition holds before a process advances.
		- It **verifies rather than teaches** — a checklist is not a comprehensive how-to guide; it confirms that crucial things have happened or are true.
		- It covers only **critical items** — the "killer items" that are both essential and easily missed, not everything a person knows how to do.
		- It happens at a **pause point** — the workflow deliberately stops before proceeding (before incision in surgery, before takeoff in aviation).
		- It has an **observable, binary outcome** — a good check answers a yes/no question: Has the patient been identified? Has antibiotic prophylaxis been given? Has everyone introduced themselves? Is the fuel valve open?
	- ## Ideas
		- Distinguishes **DO-CONFIRM** checklists (do the work from memory, then pause to confirm nothing was missed) from **READ-DO** checklists (read each item and immediately perform it, like a recipe).
		- Good checklists are short, precise, and practical — not exhaustive. A checklist that tries to spell out everything becomes unusable.
		- Checklists also install **communication points** — forcing a team to talk to each other (e.g. everyone stating their name and role before surgery) is itself a safeguard.
		- Frames modern failure as **ineptitude** (not applying what we already know) rather than **ignorance** (not knowing what to do); checks are designed to close the ineptitude gap.
	- ## [[My Notes]]
		- A Gawande check is much narrower than an [[AI/Eval/LLM as Judge]] criterion. His checks are intentionally binary, observable, and actionable — they answer "Can we safely proceed?" not "How good is this overall?"
		- Useful test for what deserves to be called a *check* in a CLI jig or eval harness: is it a decision gate with a yes/no answer, or a graded quality judgment? The former is a check in Gawande's sense; the latter is an evaluation.
	- ## Links
		- Author: [[Person/Atul Gawande]]
		- https://atulgawande.com/book/the-checklist-manifesto/
		- https://en.wikipedia.org/wiki/The_Checklist_Manifesto
