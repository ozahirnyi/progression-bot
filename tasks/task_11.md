# Task 11 — Delete entry (Stage 2, optional)

Sometimes the best log is no log.

## Goal

Let the user **remove logged time for a specific day**. Command: `/delete YYYY-MM-DD` or `/delete yesterday`. After that, that day has 0 minutes; in `/last14` it will show as missed/empty/weekend per the rules.

## Expected result

- `/delete 2026-01-24` removes the entry for that day; `/status` and `/last14` reflect the change.
- `/delete yesterday` removes yesterday's entry.
- If there was no entry for that day, you can reply "No entry for that day" and leave state unchanged.
- Add the command to `/help`.

## Contract for tests

Tests expect in `progression_bot.use_cases.progress`:

- **`delete_entry(state: State, day: date) -> State`** — returns a new state whose `entries` contain no entry for the given day. If there was no entry, you may return the state unchanged.

You can parse the date ("yesterday", `YYYY-MM-DD`) similarly to `/log` (shared helper), wire the command in the router, load state, call `delete_entry`, save, and reply with confirmation.

## Hints

- New entries list: `tuple(e for e in state.entries if e.day != day)`.
