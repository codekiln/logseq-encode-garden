logseq-entity:: [[Logseq/Entity/Discussion]], [[Logseq/Entity/Diataxis/Explanation]]
see-also:: [[Logseq/Entity/Music/Scale]]

- # Musical Form Discussion
	- Why musical forms get pages of their own, why one `Music/Form/` namespace holds both kinds of piece and structures, and why the garden does not model genre.
	- ## Forms get their own pages, linked from works
		- A form page gathers every work in that form across composers. [[Music/Form/Prelude]] lists every prelude in the garden in its linked references, and filtering those references by a composer's page narrows the list to that composer's preludes.
		- Each work page links its form with `music-form::`, defined at [[Logseq/Entity/Music/Work/Frontmatter/music-form]]. The filter works because `music-form::` and `created-by::` sit in the same frontmatter block, so no query is needed.
		- The pattern follows [[Logseq/Entity/Music/Scale]]: concept pages under `Music/<Concept>/<Name>` with an index page above them.
	- ## One namespace for kinds of piece and structures
		- "Sonata" names two related things. A sonata is a kind of piece, usually in several movements. Sonata form is the plan of a single movement: exposition, development, recapitulation. The second movement of Beethoven's *Pathétique* Sonata belongs to a sonata and is a rondo; the first movement of Mozart's Symphony No. 40 is in sonata form and belongs to a symphony.
		- The two get sibling pages, `Music/Form/Sonata` and `Music/Form/Sonata Form`. Musicians already tell them apart that way in speech: "a sonata" and "sonata form."
		- A name that means one thing in both senses, such as fugue, gets one page.
		- codekiln finds splitting the sonata from sonata form uncomfortable, and chose the sibling pages because they match how musicians talk.
		- **Alternative: `Music/Shape/`.** "Form" is overloaded and "shape" is not, so `Music/Shape/Sonata` and `Music/Shape/Sonata Form` keep the kind of piece apart from the music-theory sense. No one in music uses "shape" this way, so every reader would learn the term from the garden. A nested `Music/Shape/Sonata/Form` would also imply that sonata form is part of a sonata, which the Mozart example contradicts.
		- **Alternative: `Music/Genre/` for kinds of piece, `Music/Form/` for structures.** Musicologists use "genre" for the symphony, sonata and nocturne: Jim Samson's "Genre" article in *Grove Music Online*, Jeffrey Kallberg's "The Rhetoric of Genre: Chopin's Nocturne in G Minor" ([1988]([[19/8/8]])), and Carl Dahlhaus on *Gattung*. The Library of Congress files "Preludes (Music)" and "Sonatas" among its Genre/Form Terms without choosing between the words. Working musicians call a sonata a form, not a genre, so the split reads as academic jargon.
	- ## Genre is not modeled yet
		- Genre means different things to different readers: a kind of piece to a musicologist, a style such as rock or ambient to most listeners.
		- codekiln would model a grouping like genre only if it worked the same way across literature, music and other disciplines of expression, and would prefer a neutral word such as "category." Form may face the same question across disciplines.
		- Works that organize music history by kinds of piece could change this. Dahlhaus's *Nineteenth-Century Music* and the Samson article are the places to start.
	- ## History
		- [[2026-10-11 Sun]] — Filed [[Logseq/Entity/Music/Form]] and [[Music/Form/Prelude]] with the first instance, Rachmaninoff's [[Person/Sergei Rachmaninoff/Music/Work/Morceaux de fantaisie Op. 3/02 Prelude in C-sharp Minor]]. Weighed `Music/Shape/` and a genre/form split, kept `Music/Form/` for both senses, and set genre aside.
	- ## Open questions
		- A cross-discipline grouping word for kinds of works, and whether form belongs in it.
