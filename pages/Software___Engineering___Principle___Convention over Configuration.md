logseq-entity:: [[Logseq/Entity/Concept]]
tags:: [[Diataxis/Concept]]
alias:: [[Convention over Configuration]], [[CoC]]
see-also:: [[Person/David Heinemeier Hansson]], [[Ruby/Rails]], [[Software/Engineering/Principle/DRY]], [[Configuration/Management]]
source:: https://chatgpt.com/s/t_6a102ca04ed081919e3b230111c8f0ea

- # Convention over Configuration
	- ## Overview
		- Convention over Configuration is the idea that a framework should infer common application structure from agreed naming, file layout, and architectural defaults, asking developers to configure only exceptional cases.
		- Historically, it is best understood as a reaction against configuration-heavy enterprise software culture in the late 1990s and early 2000s, especially around [[Java]] enterprise stacks.
		- The point is not that configuration disappears. The point is that routine choices move from per-project declarations into shared framework conventions.
	- ## Context
		- Before the phrase became popular, many frameworks required developers to describe application structure explicitly through XML mapping files, dependency wiring, route declarations, ORM table mappings, and deployment descriptors.
		- A recurring complaint was that developers spent too much time telling the framework what the application looked like instead of writing the application itself.
		- David Heinemeier Hansson popularized the phrase through [[Ruby/Rails]] around 2004-2005, where it became a whole-framework design principle rather than a small convenience.
		- Rails treated developer happiness and fast prototyping as design goals. Its counter-cultural posture made "less ceremony" part of the product identity, not merely an implementation detail.
	- ## Key Principles
		- **Shared defaults** - Common cases should work without local declarations.
		- **Naming as structure** - Names and locations carry meaning: a class, table, controller, route, or template can be connected because it follows the expected pattern.
		- **Configuration for exceptions** - Developers configure the cases that depart from the convention, not every ordinary relationship.
		- **Opinionated design** - The framework chooses a path so teams can spend less effort deciding on routine structure.
		- **DRY pressure** - It aligns with [[Software/Engineering/Principle/DRY]] because repeated declarations often duplicate knowledge already present in names or layout.
	- ## Mechanism
		- In Rails, a `User` model conventionally maps to a `users` database table.
		- Controller names can imply routes and expected action names.
		- File locations imply loading behavior.
		- Template paths are discovered by directory structure.
		- The framework reads these conventions as application metadata, reducing the amount of explicit [[Configuration/Management]] needed for ordinary cases.
	- ## Historical Lineage
		- Rails did not invent convention-based behavior from nothing. Earlier systems used conventions in narrower forms, including JavaBeans naming rules, Unix filesystem expectations, Smalltalk frameworks, code generators, and MVC frameworks with implicit routing.
		- Rails made the philosophy more visible by organizing an entire mainstream web framework around the trade: follow the framework's shape and it will do more for you automatically.
		- The idea spread into later framework culture, including Django, Laravel, Ember.js, Phoenix, Spring Boot, and many modern CLI and developer tooling ecosystems.
		- Hansson later framed Rails as "omakase" software: accepting a curated set of opinions in exchange for speed and coherence.
	- ## Tension
		- Convention over Configuration trades explicitness for velocity.
		- The benefit is that common paths become shorter, projects look more alike, and beginners can build useful software before learning every integration point.
		- The cost is that implicit behavior can feel magical, hidden rules can be hard to discover, customization can become awkward, and debugging may require framework-specific knowledge.
		- This tension explains why some programming cultures lean toward the opposite pole, captured by the Python aphorism "Explicit is better than implicit."
	- ## Misconceptions
		- "Convention means no configuration" - False. Configuration remains important for exceptions, integration boundaries, and deliberate departures from the framework's default path.
		- "Convention is only a Rails idea" - False. Rails popularized the phrase and centered the philosophy, but convention-based behavior predates Rails and appears across many ecosystems.
		- "Implicit behavior is always bad" - Too simple. Implicitness is harmful when rules are hidden or inconsistent; it can be powerful when conventions are stable, teachable, and aligned with common work.
	- ## Sources
		- [Convention over configuration - Wikipedia](https://en.wikipedia.org/wiki/Convention_over_configuration)
		- [The Ruby on Rails Doctrine](https://rubyonrails.org/doctrine)
