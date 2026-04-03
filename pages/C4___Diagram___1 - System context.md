logseq-entity:: [[Logseq/Entity/concept]]
tags:: [[Diataxis/Concept]]
see-also:: [[C4/Abstraction/1 - Software System]], [[C4/Diagram/2 - Containers]]

- # **[System context diagram](https://c4model.com/diagrams/system-context)** (C4 diagram)
	- ## Overview
		- **Level 1** static-structure view: the **software system under design** as one box among **people** (actors) and **other software systems** it interacts with.
		- Deliberately **low detail**—answers *what does this system **do** for **whom*** and *what are its **external collaborators***.
	- ## Context
		- First of the four core diagrams indexed on [[C4/Diagram]]; together with [[C4/Diagram/2 - Containers]] it is **sufficient for most teams** per the C4 site.
		- Corresponds to modelling the [[C4/Abstraction/1 - Software System]] boundary in its environment—not what runs inside it.
	- ## Key principles
		- **Scope clarity** — “Inside” vs “outside” the system must be obvious.
		- **Audience fit** — Built for **non-developers** and **leadership** as much as engineers.
	- ## Mechanism
		- **Zoom in** from here to [[C4/Diagram/2 - Containers]] to open the system and show **containers**.
	- ## Examples
		- A payments platform shown with **customers**, **merchants**, **card networks**, and **internal admin users**.
	- ## Misconceptions
		- “**Context = deployment**” — **Wrong**; deployment concerns belong in [[C4/Diagram/Deployment]] (supporting view).
		- “**Must list every integration**” — **Pragmatically false**; show **material** external dependencies only.
