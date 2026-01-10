---
name: logseq-week-info-getter
description: Get the logseq week days for specified or current week
tools:
  - agent/runSubagent
---
# Get the logseq days for this week

## Usage

Execute this command in one of two ways.

### 1 - Supplying a date as an argument.
#### 1 - Command: `/logseq-week-info-getter <date>`
#### 1 - Example Invocation `/logseq-week-info-getter 2025-11-03`
This would produce a report of the data related to the days of the week in which the supplied date falls.

Example Output:
```yaml
year: 2025
trimester: 3
week: 10
day: 
 - d1: 2025-11-03 Mon
 - d2: 2025-11-04 Tue
 - d3: 2025-11-05 Wed
 - d4: 2025-11-06 Thu
 - d5: 2025-11-07 Fri
 - d6: 2025-11-08 Sat
 - d7: 2025-11-09 Sun
```
### 2 - Supplying no parameters
If no parameters are supplied, assume that the user is interested only in the current week.
#### 2 - Command: `/logseq-week-info-getter`
This would produce a report of the data related to the days of the week in which the current date falls. 


Follow `Workflow` to get `LOGSEQ_NAMESPACED_PAGE_NAME` then `Report` the completed work.


## Arguments

One argument (optional), which is the anchor day in which the week occurs

ANCHOR_DAY: $ARGUMENTS[0]

## Workflow

- if $ANCHOR_DAY is not defined, use the `date` CLI tool to find the current date today
  - `date "+%Y-%m-%d %a"`
- use other tools to calculate the current week number in the trimester

## Report

The report block should be in yaml. One of the below blocks should be the entire report.
Keys to include
- **year**: 4-digit year (e.g., 2025)
- **trimester**: 1, 2, or 3
  - Trimester 1: Jan 1 to day before Memorial Day (last Monday in May)
  - Trimester 2: Memorial Day to day before Labor Day
  - Trimester 3: Labor Day (first Monday in September) to Dec 31
- **week**: Week number within the trimester (01-16)
- **day**: yaml list of day(s) within the week, specified from d1 (monday) to d7 (sunday), in the format `dD: +%Y-%m-%d %a`

## Implementation

Python script to calculate week days:

```python
from datetime import datetime, timedelta
import calendar
import sys

# Get anchor date from argument or use current date
if len(sys.argv) > 1:
    anchor_date_str = sys.argv[1]
else:
    # Get current date in format YYYY-MM-DD
    anchor_date_str = datetime.now().strftime('%Y-%m-%d')

anchor_date = datetime.strptime(anchor_date_str, '%Y-%m-%d')
year = anchor_date.year

# Calculate Memorial Day (last Monday in May)
# Start from May 31 and go backwards to find the last Monday
memorial_day = None
for day in range(31, 0, -1):
    try:
        date = datetime(year, 5, day)
        if date.weekday() == 0:  # Monday
            memorial_day = date
            break
    except ValueError:
        continue

# Calculate Labor Day (first Monday in September)
labor_day = None
for day in range(1, 8):
    date = datetime(year, 9, day)
    if date.weekday() == 0:  # Monday
        labor_day = date
        break

# Determine trimester
if anchor_date < memorial_day:
    trimester = 1
    trimester_start = datetime(year, 1, 1)
    trimester_end = memorial_day - timedelta(days=1)
elif anchor_date < labor_day:
    trimester = 2
    trimester_start = memorial_day
    trimester_end = labor_day - timedelta(days=1)
else:
    trimester = 3
    trimester_start = labor_day
    trimester_end = datetime(year, 12, 31)

# Find the Monday of the week containing anchor_date
days_since_monday = anchor_date.weekday()
monday_of_week = anchor_date - timedelta(days=days_since_monday)

# Calculate week number within trimester
# Count how many Mondays have passed since trimester start
days_diff = (monday_of_week - trimester_start).days
week_number = (days_diff // 7) + 1

# Calculate all 7 days of the week (Monday-Sunday)
week_days = []
for i in range(7):
    day_date = monday_of_week + timedelta(days=i)
    day_name = calendar.day_abbr[day_date.weekday()]
    week_days.append((f'd{i+1}', day_date.strftime('%Y-%m-%d'), day_name))

# Output YAML
print(f'year: {year}')
print(f'trimester: {trimester}')
print(f'week: {week_number:02d}')
print('day:')
for d_num, date_str, day_abbr in week_days:
    print(f' - {d_num}: {date_str} {day_abbr}')
```

Usage:
- With date argument: `python3 script.py 2025-11-03`
- Without argument (uses current date): `python3 script.py`
