## Task 01 — Load the fixture and define domain models

Joke: a JSON file walks into a bar and says: “Sorry, I’m not in the mood… I’m just here for the **objects**.”

### Goal (in simple words)
You will teach the bot to **understand its own data**.

Right now the project has a JSON file with mock data. Your job is to:
- define Python classes that represent that data
- write a small loader that converts JSON → Python objects

### What to implement
- **Step A — Domain classes**
  - Open `progression_bot/domain/models.py`
  - You already have signatures there (`Schedule`, `PlanStage`, `Plan`, `Entry`, `State`)
  - Your first “real” code can be implementing:
    - `Plan.total_planned_minutes()`

- **Step B — JSON loader**
  - Open `progression_bot/storage/json_store.py`
  - Implement `JsonStore.load()`
  - It should read JSON from:
    - `fixtures/mock_state.json` (for now)
  - Convert values:
    - `start_date` (`YYYY-MM-DD`) → `datetime.date`
    - `duration` strings (`"2h"`, `"32m"`, `"1h30m"`, `"2.5h"`) → minutes (int)

Tip: for parsing duration, you can reuse the function you will implement in `task_02.md` (`parse_duration_to_minutes`).

### Expected result
You can run a tiny script and get a `State` instance without exceptions.

Example script idea (you can put it anywhere locally, don't commit if you don't want):
- call `load_fixture()` from `progression_bot/storage/json_store.py`
- print:
  - start_date
  - total planned hours
  - number of entries

### Test cases
- **Happy path**: load `fixtures/mock_state.json` and assert:
  - version is `1`
  - tz is `"Europe/Kyiv"`
  - stages count > 0
  - entries count > 0
- **Invalid JSON**: break the file (missing bracket) → loader returns a clear error.
- **Invalid date**: set `"date": "2026-13-99"` → loader rejects it.

### Beginner-friendly hints
- If you get stuck: print the raw JSON dict first, then convert it step by step.
- When converting durations, always store minutes as **int** (no floats).

_(Note for practice PRs: this file change is intentionally small.)_

