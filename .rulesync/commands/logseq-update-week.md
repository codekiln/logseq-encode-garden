---
root: false
targets:
  - '*'
description: 'Automate weekly Logseq page setup process'
globs:
  - 'pages/YYYY___t*___w*.md'
  - 'pages/Logseq___Template___*.md'
---

# Update Week Command

This command automates the creation of a complete week structure in the Logseq garden, including week pages, day pages, and todo pages with proper navigation links and formatting.

## Usage

Execute this command with three parameters: year, trimester, and week number.

**Command:** `/logseq-update-week <year> <trimester> <week>`

**Example:**
```
/logseq-update-week 2025 3 6
```
This creates the complete structure for Week 6 of Trimester 3, 2025.

## What This Command Does

1. **Calculates dates** for the specified week (Monday-Sunday)
2. **Determines trimester boundaries** and adjacent weeks
3. **Updates** `pages/Logseq___Template___Today___Link.md` with new week references
4. **Creates** the week page with proper navigation links
5. **Creates** the week todos page
6. **Creates** 7 daily pages (d1-d7) with correct navigation
7. **Creates** 7 daily todo pages with proper references

## Parameters

- **year**: 4-digit year (e.g., 2025)
- **trimester**: 1, 2, or 3
  - Trimester 1: Jan 1 to day before Memorial Day (last Monday in May)
  - Trimester 2: Memorial Day to day before Labor Day
  - Trimester 3: Labor Day (first Monday in September) to Dec 31
- **week**: Week number within the trimester (1-52)

## Files Created

The command creates these files in the `pages/` directory:

1. `YYYY___tT___wWW.md` - Main week page
2. `YYYY___tT___wWW___Todos.md` - Week todos page
3. `YYYY___tT___wWW___d1.md` through `YYYY___tT___wWW___d7.md` - Daily pages
4. `YYYY___tT___wWW___d1___Todos.md` through `YYYY___tT___wWW___d7___Todos.md` - Daily todo pages

Plus updates to `Logseq___Template___Today___Link.md` with the new week's day links.

## Implementation Details

The command performs these calculations and operations:

1. **Date Calculation**: Determines the Monday-Sunday dates for the specified week
   - Week N starts (N-1) weeks after the trimester start date
   - Labor Day is calculated as the first Monday in September
2. **Trimester Logic**: Handles trimester boundaries for prev/next week navigation
3. **Template Processing**: Uses existing templates to maintain consistency
4. **Navigation Links**: Creates proper bidirectional links between all pages
   - d1 (Monday) prev:: links to previous week's d7 (Sunday)
   - d7 (Sunday) next:: links to next week's d1 (Monday)
5. **File Naming**: Follows Logseq's triple-underscore namespace convention

## Template Structure

### Week Page Template
```markdown
type:: [[Type/Logseq/Week/Page]]
created-by-template:: [[Logseq/Template/Week/Current]]
icon:: 🗓️
up:: [[YYYY/tT]]
prev:: [[YYYY/tT/wPREV]]
next:: [[YYYY/tT/wNEXT]]
week-todos:: [[YYYY/tT/wWW/Todos]]
banner:: "../assets/Logseq/Plugins/logseq-banners-plugin/deep_springs_cow_camp_01.jpg"

- # Week Notes
  - ## Week Start (logseq-garden ONLY)
    - ### DOING Week Setup
      :LOGBOOK:
      CLOCK: [YYYY-MM-DD Day HH:MM:SS]
      :END:
      - TODO update [[Logseq/Template/Today/Link]] to point to *this* week, and fill in all the days as well
      - TODO create a "today link" with `d1 link`, `d2 link`, etc in Week Days below
      - TODO book rooms for week and put on calendar
      - TODO book any group exercise classes and put on calendar
      - TODO fill in weather for each day of the week
      - TODO export calendar
      - TODO fill in day links below using cursor
      - TODO create week todos page
        - TODO open week todos page and instantiate the skeleton
          - TODO take a look at [[Logseq/Template/Week/Todos/Skeleton]]
          - TODO instantiate Week Todos Skeleton
        - TODO if we're in a downstream repository, fill in the content of the week todos page
          - TODO take a look at [[Logseq/Template/Week/Todos/Content]]
          - TODO instantiate Week Todos Content
        - TODO port over items from previous week, cutting and pasting
      - TODO do a git commit
    - ### TODO What's up this week
  - ## Week Days - (logseq-garden ONLY)
    note:: *for each day, first go to the today link for the downstream Logseq repo and fill it out, then use `Today Link` template, and inside that log entry, use [[Logseq/Template/Today/Setup Checklist]] template*
    - ### log [[YYYY/tT/wWW/d1]] - [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
    - ### log [[YYYY/tT/wWW/d2]] - [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
    - ### log [[YYYY/tT/wWW/d3]] - [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
    - ### log [[YYYY/tT/wWW/d4]] - [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
    - ### log [[YYYY/tT/wWW/d5]] - [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
    - ### log [[YYYY/tT/wWW/d6]] - [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
    - ### log [[YYYY/tT/wWW/d7]] - [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
  - ## Week End - (Downstream Repos ONLY)
    - ### TODO Week Review
- # Week Reference (Downstream Repos ONLY)
  - ### Music
  -
```

### Day Page Template
```markdown
type:: [[Type/Logseq/Today/Page]]
created-by-template:: [[Logseq/Template/Today/Page Skeleton]]
banner:: "https://wallpaperaccess.com/full/1146672.jpg"
icon:: 📖
up:: [[YYYY/tT/wWW]]
prev:: [[YYYY/tT/wWW/dPREV]]
next:: [[YYYY/tT/wWW/dNEXT]]
todos:: [[YYYY/tT/wWW/dD/Todos]]
week-todos:: [[YYYY/tT/wWW/Todos]]

- # log [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
  - ## Agenda
```

### Day Todos Page Template
```markdown
type:: [[Type/Logseq/Today/Todos]]
created-by-template:: [[Logseq/Template/Today/Todos/Skeleton]]
banner:: "../assets/Logseq/Template/Week/Todos/ben_franklin_almanac.jpg"
icon:: 📅✅
up:: [[YYYY/tT/wWW/dD]]
prev:: [[YYYY/tT/wWW/dPREV/Todos]]
next:: [[YYYY/tT/wWW/dNEXT/Todos]]
week-todos:: [[YYYY/tT/wWW/Todos]]
trimester-todos:: [[YYYY/tT/Todos]]

- # Todos [[YYYY/tT/wWW/dD/Todos]] - [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
```

### Week Todos Page Template
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

## Special Considerations

### Trimester Boundaries
The command handles trimester boundaries automatically:
- Trimester 1: Jan 1 to the day before Memorial Day (last Monday in May)
- Trimester 2: Memorial Day to the day before Labor Day
- Trimester 3: Labor Day (first Monday in September) to Dec 31

When a week is at the end or beginning of a trimester, the `prev` and `next` links will point to the appropriate week in the adjacent trimester.

**Note**: The command creates daily pages with minimal content (just the heading and empty Agenda section). Weather and Schedule details are only added if provided in the week overview page.

### Navigation Links
The command maintains correct references between:
- Week pages and their days
- Day pages and their todos
- Adjacent weeks (including across trimester boundaries)
- Adjacent days (including across week boundaries)

### Today's Link Template
The command updates the `Logseq___Template___Today___Link.md` file with references to the new week and properly formatted date links for each day.

All created files follow Logseq Flavored Markdown conventions as described in the logseq-flavored-markdown rule.