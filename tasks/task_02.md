## Task 02 — Implement `/log` parsing (time + date target)

Joke: why did the parser break up with the string? It found too many **mixed signals**.

### Goal
Implement robust parsing for log commands:
- `/log <duration>`
- `/log yesterday <duration>`
- `/log YYYY-MM-DD <duration>`
- `/logy <duration>` (alias for yesterday)

### What to implement
In `progression_bot/bot/parse.py`:
- Implement `parse_duration_to_minutes(raw: str) -> int`
  - Accept:
    - `32m`, `90m`
    - `2h`, `2.5h`
    - `1h30m`, `2h 15m`
  - Return minutes as **int**

- Implement `parse_log_command(text: str, today: date) -> LogCommand`
  - Accept:
    - `/log 2h`
    - `/log yesterday 45m`
    - `/log 2026-01-23 2.5h`
    - `/logy 1h`
  - Return:
    - `day` (date)
    - `minutes` (int)

### Expected result
The bot can accept valid formats and reject invalid ones with a helpful message.

### Beginner-friendly hints
- Start with the easiest case: `/log 2h`
- Then add “yesterday”
- Then add explicit date
- Only after that add combos like `1h30m`

### Test cases
- `/log 32m` → minutes = 32, date = today
- `/log 1h30m` → minutes = 90
- `/log 2.5h` → minutes = 150
- `/logy 45m` → date = yesterday
- `/log yesterday 45m` → same as above
- `/log 2026-01-23 2h` → date parsed correctly
- `/log 0m` → validation error
- `/log 1m30` → validation error

