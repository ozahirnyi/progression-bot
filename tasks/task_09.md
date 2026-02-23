# Task 09 — Implement `/start_progression` (Stage 2)

Every journey begins with a single `/start_progression`.

## Goal

The user must be able to **set (or reset) the progression start date**. This is the day from which "done" minutes and "missed" days are counted. Command: `/start_progression` or `/start_progression YYYY-MM-DD`. If no date is given, use today.

## Expected result

- After `/start_progression 2026-01-01`, the next `/status` uses that date as the start (e.g. "done" only from 2026-01-01).
- `/start_progression` with no date sets start to today.
- State is saved to the file at `STORAGE_PATH`; after restarting the bot the start date is preserved.

## Contract for tests

Tests expect in `progression_bot.use_cases.progress`:

- **`start_progression(state: State, start_date: date) -> State`** — returns a new state with `start_date` set to the given date. You can leave other fields unchanged or set minimal defaults; the important part is the updated `start_date`.

How you wire this to the command (handler/router), how you parse the optional date, and what you output to the user is up to you. If the state file does not exist yet, you can create minimal state (as in task_03), call `start_progression` on it, and save.

## Hints

- State is immutable: return a new `State(..., start_date=start_date, ...)`.
- `JsonStore.load()` for a non-existent path may already create default state; then call `start_progression` and `save`.
