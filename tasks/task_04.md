## Task 04 — Implement `/status` (progress + dynamic deadline)

Joke: deadlines are like exceptions—everyone hopes they won’t be raised.

### Goal
Implement `/status` output based on logged minutes and the learning plan.

### Rules (recap)
- Planned workdays: Mon–Fri
- Daily planned capacity: 2h per workday
- Total planned minutes: `sum(stage.expected_hours) * 60`
- Done minutes: sum of logged minutes since `start_date`
- Remaining: `max(0, total - done)`
- Project finish date: consume future workdays with 2h capacity until remaining is 0

### Expected output (minimum)
Show three formats:
- **Days to finish** (calendar days)
- **Expected deadline date** (`YYYY-MM-DD`)
- **Hours** done / total / remaining

### Test cases
- With empty state: remaining == total, deadline in the future.
- After logging: remaining decreases, deadline moves closer.
- If remaining == 0: deadline is today (or earlier), days-to-finish is 0.

