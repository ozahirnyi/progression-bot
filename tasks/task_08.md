# Task 08 — Make `/log` persist (Stage 2)

If you log time but never save it to JSON — did it really happen?

## Goal

When the user sends `/log 2h` (or `/log yesterday 45m`, etc.), the bot must **update the real state file** and confirm with a message. Parse the command, add (or sum) minutes for that day, save state, and reply with a short confirmation.

## Expected result

- `/log 2h` and other variants update the file at `STORAGE_PATH` and reply with confirmation.
- After restarting the bot, `/status` and `/last14` show the new minutes.
- If the user logs twice for the same day, minutes are summed (or another clear rule you choose and document).
- Invalid format or missing duration yield a clear message (e.g. "Usage: /log 2h or /log yesterday 45m"), no crash.

## Contract for tests

Tests expect in `progression_bot.use_cases.progress`:

- **`LogRequest`** — dataclass with `day: date`, `minutes: int`, `note: str | None = None`.
- **`log_time(state: State, req: LogRequest) -> State`** — returns a new state where `req.day` has `req.minutes` added (e.g. sum with existing entry or a single entry per day).
- **`upsert_entry(state: State, entry: Entry) -> State`** — inserts or updates the entry for `entry.day`; in the result, that day has a matching entry with `entry.minutes`.

Where to implement (`progress.py` or another module), how to sum minutes, and whether to use `upsert_entry` inside `log_time` is your choice. The router/handler should: load state, parse text (e.g. via `parse_log_command` from task_02), call the use case, save state, return the reply text.

## Hints

- You can use `parse_log_command` from task_02; for "today" use `date.today()` or an injected date in tests.
- State is immutable: `log_time` returns a **new** `State` with updated `entries`; do not mutate the old one.
