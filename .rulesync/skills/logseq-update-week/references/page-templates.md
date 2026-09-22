# Week page templates

Substitute `tT` with the trimester number and `wWW` with the zero-padded week number in the trimester: trimester 3, week 6 gives `t3` and `w06`. `wPREV`, `wNEXT`, `dPREV` and `dNEXT` are the neighboring week and day numbers in the same padded form.

## Week page — `pages/YYYY___tT___wWW.md`

```markdown
type:: [[Type/Logseq/Week/Page]]
created-by-template:: [[Logseq/Template/Week/Current]]
icon:: 🗓️
up:: [[YYYY/tT]]
prev:: [[YYYY/tT/wPREV]]
next:: [[YYYY/tT/wNEXT]]
week-todos:: [[YYYY/tT/wWW/Todos]]
banner:: "../assets/Logseq/Plugins/logseq-banners-plugin/deep_springs_cow_camp_01.jpg"

- # tT wWW Week Notes
  - ## What's up this week?
  - ## Week Days
    - log [[YYYY/tT/wWW/d1]] - [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
    - log [[YYYY/tT/wWW/d2]] - [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
    - log [[YYYY/tT/wWW/d3]] - [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
    - log [[YYYY/tT/wWW/d4]] - [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
    - log [[YYYY/tT/wWW/d5]] - [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
    - log [[YYYY/tT/wWW/d6]] - [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
    - log [[YYYY/tT/wWW/d7]] - [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
```

## Day page — `pages/YYYY___tT___wWW___dN.md`

```markdown
type:: [[Type/Logseq/Today/Page]]
created-by-template:: [[Logseq/Template/Today/Page Skeleton]]
banner:: "https://wallpaperaccess.com/full/1146672.jpg"
icon:: 📖
up:: [[YYYY/tT/wWW]]
prev:: [[YYYY/tT/wWW/dPREV]]
next:: [[YYYY/tT/wWW/dNEXT]]
week-todos:: [[YYYY/tT/wWW/Todos]]
trimester-todos:: [[YYYY/tT/Todos]]


- # log [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
```

## Week todos page — `pages/YYYY___tT___wWW___Todos.md`

```markdown
type:: [[types/Todos/Week]]
created-by-template:: [[Logseq/Template/Week/Todos/Skeleton]]
up:: [[YYYY/tT/wWW]]
prev:: [[YYYY/tT/wPREV/Todos]]
next:: [[YYYY/tT/wNEXT/Todos]]
trimester-todos:: [[YYYY/tT/Todos]]
icon:: 📅✅
banner:: "../assets/Logseq/Template/Week/Todos/ben_franklin_almanac.jpg"
```

## Today link template — `pages/Logseq___Template___Today___Link.md`

Rewrite this page with the new week's reference and a formatted date link for each of its days.
