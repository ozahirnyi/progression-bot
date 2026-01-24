## Task 05 — Implement `/last14` (detailed view)

Joke: the last 14 days are like a sprint—except the only thing running is your brain.

### Goal
Implement a detailed view for the last 14 days:
- date + weekday
- total duration logged
- status (missed/partial/done/bonus/weekend/empty)
- optional note

### Status thresholds
Let `H` be minutes for a day:
- Missed (red): workday, past day, `H = 0`
- Partial (yellow): `0 < H < 120`
- Done (green): `120 ≤ H < 180`
- Bonus (dark green): `H ≥ 180`
- Weekend (dark gray): weekend and `H = 0` (not missed)
- Empty (gray): before `start_date` or future

Today is never missed while it’s still today.

### Test cases
- Output always contains exactly 14 days (plus header/footer).
- Weekend with 0 minutes shows as weekend (not missed).
- Workday in the past with 0 minutes shows missed.
- Today with 0 minutes is not missed.

