logseq-entity:: [[Logseq/Entity/Definition]]

- # Musical Form
	- In this garden, **Musical Form** pages model a named kind of composition that works across composers share, such as the prelude, the nocturne or the fugue, and the structural forms such as ternary or sonata form.
	- ## What counts
		- A named kind of piece or structure that more than one composer has written in. The page describes the form itself, apart from any one work.
		- A named kind of piece and the structure of the same name get separate pages: the sonata and sonata form are two pages.
		- A work's title alone does not make a form: the *Morceaux de fantaisie* are not fantasias.
	- ## Naming and placement
		- A form lives at `Music/Form/<Name>`, under [[Music/Form]], using its common English name in the singular, as [[Music/Form/Prelude]].
	- ## Relationships
		- A [[Logseq/Entity/Music/Work]] page links each of its forms with `music-form::`, defined at [[Logseq/Entity/Music/Work/Frontmatter/music-form]]. Those links are the form's list of works, so a form page lists works only to add notes about them.
		- A form page's linked references filtered by a composer's page show that composer's works in the form, since a work page's `created-by::` sits in the same frontmatter block as its `music-form::`.
	- ## Instance shape
		- Start each form page with `logseq-entity:: [[Logseq/Entity/Music/Form]]` and one H1 with the form's common name.
		- Follow with a short description of the form and its history.
