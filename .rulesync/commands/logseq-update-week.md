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

Execute this command with zero parameters

```
/logseq-update-week 
```
This creates the complete structure for the current week.

## What This Command Does

1. **Calculates dates** for the specified week (Monday-Sunday)
2. **Determines trimester boundaries** and adjacent weeks
3. **Updates** `pages/Logseq___Template___Today___Link.md` with new week references
4. **Creates** the week page with proper navigation links
5. **Creates** the week todos page
6. **Creates** 7 daily pages (d1-d7) with correct navigation
7. **Creates** 7 daily todo pages with proper references

## Info to gather

use the `logseq-week-info-getter` agent to gather a report of the following data

- **year**: 4-digit year (e.g., 2025)
- **trimester**: 1, 2, or 3
  - Trimester 1: Jan 1 to day before Memorial Day (last Monday in May)
  - Trimester 2: Memorial Day to day before Labor Day
  - Trimester 3: Labor Day (first Monday in September) to Dec 31
- **week**: Week number within the trimester (1-52)
- **day**: list of days in the week

## Files Created

The command creates these files in the `pages/` directory:

1. `YYYY___tT___wWW.md` - Main week page
2. `YYYY___tT___wWW___Todos.md` - Week todos page
3. `YYYY___tT___wWW___d1.md` through `YYYY___tT___wWW___d7.md` - Daily pages

Plus it updates `Logseq___Template___Today___Link.md` with the new week's day links.

## Implementation Details

The command performs relies on calculations and operations from `logseq-week-info-getter` subagent

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

In the below templates,
* `tT` means to substitute T with the Trimester number. If it was trimester 3, then it should be `t3`. 
* `wWW` means to subsitute WW with the zero-padded week number in the trimester. if it was, 6, then it should be `w06`. 

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

- # tT wWW Week Notes
  - ## What's up this week?
  - ## Week Days
    - ### log [[YYYY/tT/wWW/d1]] - [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
    - ### log [[YYYY/tT/wWW/d2]] - [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
    - ### log [[YYYY/tT/wWW/d3]] - [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
    - ### log [[YYYY/tT/wWW/d4]] - [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
    - ### log [[YYYY/tT/wWW/d5]] - [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
    - ### log [[YYYY/tT/wWW/d6]] - [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
    - ### log [[YYYY/tT/wWW/d7]] - [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
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
week-todos:: [[YYYY/tT/wWW/Todos]]
trimester-todos:: [[YYYY/tT/Todos]]


- # log [[YYYY/MM/DD]] - [[YYYY-MM-DD Day]]
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