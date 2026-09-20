## `logseq-created-time-year::` - links an entity to its creation year, decade, or century

- The value is a link to the matching [[Logseq/Entity/Time/Year]] instance, at whatever precision is actually known — a specific year, or its decade or century when only that much is known.
- Distinct from `date-created::`: that property holds the display-quality date value (day, month, or year, per [[Logseq/Date]]) and does not always resolve to a [[Logseq/Entity/Time/Year]] page. `logseq-created-time-year::` always does, so every entity created in a given year, decade, or century collects there as a backlink regardless of the entity's own type.
- Applies broadly, to any entity whose creation year is known: books, movies, podcast episodes, essays, musical compositions, works of art, and others.
- Set alongside `date-created::`, not instead of it, when both are known.
