---
root: false
targets:
  - '*'
description: ''
globs: []
---
# Once a week setup to prepare week markdown files 
- be familiar with [logseq-directory-structure.mdc](mdc:.cursor/rules/logseq-cursor-rules/logseq-directory-structure.mdc)
- Look at the files that match the glob `pages/2025___t1___w14*.md` to find the pattern of what the pages should look like. 

## Preparation - Setting up the links
- the first step is to update [Logseq___Template___Today___Link.md](mdc:pages/Logseq___Template___Today___Link.md) to the next week. the user will tell you which week to update this to.
- the next step is to have the user instantiate the current week logseq template [Logseq___Template___Week___Current.md](mdc:pages/Logseq___Template___Week___Current.md) inside the current week's markdown page, which will follow the template of `pages/YYYY___tT___wWW.md`, where YYYY is the year, T is the trimester (1, 2, 3), and WW is the week number of the trimester (zero-padded).
- The user may ask you to fill in the days of the week in the current week's page so they can take some notes under them.

## Filling out the day page headers
- given the user's requested week number, set up the week's day pages to match the pattern of week 14
  - important note: the agendas and days for the current week will likely be different than week 14!
- there should be two files created for each day of the week, 1-7. The first will be for the day, the second will be for the todos for that day.
  - for each day's page I instantiate the logseq template [Logseq___Template___Today___Page Skeleton.md](mdc:pages/Logseq___Template___Today___Page Skeleton.md)
  - for each day's today page I instantiate the logseq template [Logseq___Template___Today___Todos___Skeleton.md](mdc:pages/Logseq___Template___Today___Todos___Skeleton.md)
- DO NOT INVENT PAGE LEVEL ATTRIBUTES - I'm hoping you can basically simulate instantiating the logseq template for each day.
- in particular, note the links to the next and previous day in the header, *particularly at d1 and d7* since those will reference the previous and next week, respectively. Also, note the relationship between the day files and the week files. 
- "up" in the page properties refers to the page "up" in the logseq namespace. 
  - for example, [[2025/t1/w07]] is "up" from [[2025/t1/w07/Todos]] 
- **Special note for trimester boundaries:**
  - Trimester 1: Jan 1 to the day before Memorial Day
  - Trimester 2: Memorial Day to the day before Labor Day
  - Trimester 3: Labor Day to Dec 31
  - When a week is at the end or beginning of a trimester, the `prev` and `next` links in the week and day pages should point to the last week of the previous trimester or the first week of the next trimester, respectively. For example, the week before Memorial Day (end of T1) should have its `next` link point to the first week of T2, and the week before Labor Day (end of T2) should have its `next` link point to the first week of T3. Similarly, the first week of a trimester should have its `prev` link point to the last week of the previous trimester.

# Individual 
- the `up:: ` page-level attribute should always point up to the next level up in the logseq hierarchy. So if we are in a page [[A/B/C]], it should be `up:: [[A/B]]`. Remember here that the logseq slashes translate to triple underscores in the filename. so `pages/A___B___C.md` would have `up:: [[A/B]]` in its logseq frontmatter
- For example:

Example for day pages in w08 (this example is for day 2 of that week, [[2025/t1/w14/d2]]):
~~~
type:: [[Type/Logseq/Today/Page]]
created-by-template:: [[Logseq/Template/Today/Page Skeleton]]
banner:: "https://wallpaperaccess.com/full/1146672.jpg"
icon:: 📖
up:: [[2025/t1/w14]]
prev:: [[2025/t1/w14/d1]]
next:: [[2025/t1/w14/d3]]
todos:: [[2025/t1/w14/d2/Todos]]
week-todos:: [[2025/t1/w14/Todos]]
- # Daylog [[2025/04/01]] - [[2025-04-01 Tue]]
	- ## Agenda
		- ### Weather
			- Temperature: 52°F
			- Wind: 13 to 16 mph NW
			- Conditions: Chance rain showers then mostly sunny
			- Evening: 30°F, mostly clear
		- ### Schedule
			- 0730-0830 item title 1
			- 0830-0900 item title 2
			- 1000-1030 item title 3
~~~

In the example day page above, the agenda, weather and schedule should ONLY be filled in if there is anything filled in under that day under "- ## Week Days" in the week page.
- **If there is no agenda or weather for a given day in the week overview page (under '- ## Week Days - (logseq-garden ONLY)'), then nothing needs to be propagated to the content inside individual day pages for that day except for the heading and page properties as indicated below.**

Example for todos pages in w08 (this example is for day 2 of that week at [[2025/t1/w14/d2/Todos]]; note that the `up:: ` link points to the equivalent day as above):
~~~
type:: [[Type/Logseq/Today/Todos]]
created-by-template:: [[Logseq/Template/Today/Todos/Skeleton]]
banner:: "../assets/Logseq/Template/Week/Todos/ben_franklin_almanac.jpg"
icon:: 📅✅
up:: [[2025/t1/w14/d2]]
prev:: [[2025/t1/w14/d1/Todos]]
next:: [[2025/t1/w14/d3/Todos]]
week-todos:: [[2025/t1/w14/Todos]]
trimester-todos:: [[2025/t1/Todos]]
- # Todos [[2025/t1/w14/d2/Todos]] - [[2025/04/01]] - [[2025-04-01 Tue]]
~~~


## Example week pages 
- [2025___t1___w14.md](mdc:pages/2025___t1___w14.md)
- [2025___t1___w14___Todos.md](mdc:pages/2025___t1___w14___Todos.md)

## Example day pages
- [2025___t1___w14___d1.md](mdc:pages/2025___t1___w14___d1.md).md
- [2025___t1___w14___d2___Todos.md](mdc:pages/2025___t1___w14___d2___Todos.md)
- [2025___t1___w14___d2.md](mdc:pages/2025___t1___w14___d2.md)
- [2025___t1___w14___d2___Todos.md](mdc:pages/2025___t1___w14___d2___Todos.md)
- [2025___t1___w14___d3.md](mdc:pages/2025___t1___w14___d3.md)
- [2025___t1___w14___d3___Todos.md](mdc:pages/2025___t1___w14___d3___Todos.md)
- [2025___t1___w14___d4.md](mdc:pages/2025___t1___w14___d4.md)
- [2025___t1___w14___d4___Todos.md](mdc:pages/2025___t1___w14___d4___Todos.md)
- [2025___t1___w14___d5.md](mdc:pages/2025___t1___w14___d5.md)
- [2025___t1___w14___d5___Todos.md](mdc:pages/2025___t1___w14___d5___Todos.md)
- [2025___t1___w14___d6.md](mdc:pages/2025___t1___w14___d6.md)
- [2025___t1___w14___d6___Todos.md](mdc:pages/2025___t1___w14___d6___Todos.md)
- [2025___t1___w14___d7.md](mdc:pages/2025___t1___w14___d7.md)
- [2025___t1___w14___d7___Todos.md](mdc:pages/2025___t1___w14___d7___Todos.md)
