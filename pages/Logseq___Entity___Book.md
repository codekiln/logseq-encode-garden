logseq-entity:: [[Logseq/Entity/Definition]]

- # Book
	- **Book** pages are published works. They are usually tracked under `Person/<name>/Book/YY/<short title>`. They may be at `Book/YY/<short title>` if there are five or more sub-pages to the namespace or if the book has more than one author.
	- A book that is also a member of a sequence is both a Book and a [[Logseq/Entity/Series]] instance. Its path then interposes `Series/<Series Name>` after `Book`, per that type page.
	- ## Frontmatter on book pages
	- Standard [[Logseq/Frontmatter]] rules
		- Mark instances with **`logseq-entity:: [[Logseq/Entity/Book]]`** so this type page collects backlinks to every book entity.
		- When the author is clear, set **`created-by:: [[Person/Full Name]], [[Person/Full Name 2]]`** in frontmatter and ensure that person entity is in the garden.
		- The publication year is usually already carried in the page's own namespace segment (the `YY` in `Person/<name>/Book/YY/<short title>`), but that text is not a link. Optional: **`logseq-created-time-year::`** linking to the matching [[Logseq/Entity/Time/Year]] instance makes it one.
	- ## Page shape
	- H1 with the book’s title, linking to the book
	- **About**, optional [[My Notes]],  **Links** (publisher, Wikipedia, author).
	- ## Examples in this garden
	- [[Person/Douglas Hofstadter/Book/79/Gödel, Escher, Bach]]
	- [[Person/Buckminster Fuller/Book/75/Synergetics]]
	- [[Person/James Clear/Book/18/Atomic Habits]]